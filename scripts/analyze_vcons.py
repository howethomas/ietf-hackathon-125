"""Main orchestrator: iterate over vCons, detect IETF principles, create derived vCons."""

import argparse
import asyncio
import glob
import json
import os
import sys
import time

from extract_transcript import extract_transcript, get_vcon_info
from keyword_detector import detect_principles_keywords
from create_derived_vcon import create_derived_vcon


def find_vcon_files(input_dir: str, meetings: list[str] | None = None) -> list[str]:
    """Find all .vcon.json files in the input directory."""
    files = []
    if meetings:
        for meeting in meetings:
            pattern = os.path.join(input_dir, meeting, "*.vcon.json")
            files.extend(sorted(glob.glob(pattern)))
    else:
        pattern = os.path.join(input_dir, "**", "*.vcon.json")
        files = sorted(glob.glob(pattern, recursive=True))
    return files


def merge_results(keyword_results: list[dict], llm_results: list[dict]) -> list[dict]:
    """Merge keyword and LLM detection results by principle."""
    merged = {}

    for r in keyword_results:
        pid = r["principle_id"]
        merged[pid] = {
            "principle_id": pid,
            "principle_name": r["principle_name"],
            "keyword_matches": r.get("matches", []),
            "keyword_match_count": r.get("match_count", 0),
            "keyword_confidence": r.get("confidence", "low"),
            "llm_evidence": [],
            "llm_confidence": None,
            "detection_methods": ["keyword"],
            "overall_confidence": r.get("confidence", "low"),
        }

    for r in llm_results:
        pid = r["principle_id"]
        if pid in merged:
            merged[pid]["llm_evidence"] = r.get("evidence", [])
            merged[pid]["llm_confidence"] = r.get("confidence")
            merged[pid]["detection_methods"].append("llm")
            # Upgrade confidence if LLM confirms
            conf_order = {"low": 0, "medium": 1, "high": 2}
            best = max(
                conf_order.get(merged[pid]["keyword_confidence"], 0),
                conf_order.get(r.get("confidence", "low"), 0),
            )
            merged[pid]["overall_confidence"] = {0: "low", 1: "medium", 2: "high"}[best]
        else:
            merged[pid] = {
                "principle_id": pid,
                "principle_name": r["principle_name"],
                "keyword_matches": [],
                "keyword_match_count": 0,
                "keyword_confidence": None,
                "llm_evidence": r.get("evidence", []),
                "llm_confidence": r.get("confidence"),
                "detection_methods": ["llm"],
                "overall_confidence": r.get("confidence", "low"),
            }

    return list(merged.values())


async def process_vcon(
    vcon_path: str,
    output_dir: str,
    use_llm: bool = False,
    api_key: str | None = None,
) -> dict:
    """Process a single vCon file. Returns a result summary dict."""
    filename = os.path.basename(vcon_path)
    meeting = os.path.basename(os.path.dirname(vcon_path))

    # Extract transcript
    text, metadata = extract_transcript(vcon_path)
    if not text:
        return {"file": filename, "meeting": meeting, "status": "skipped", "reason": "no_transcript"}

    # Get source vCon info
    info = get_vcon_info(vcon_path)

    # Tier 1: keyword detection
    keyword_results = detect_principles_keywords(text)

    # Tier 2: LLM detection (optional)
    llm_results = []
    if use_llm and api_key:
        from llm_detector import detect_principles_llm
        llm_results = await detect_principles_llm(text, api_key)

    # Merge results
    detection_methods = ["keyword"]
    if use_llm:
        detection_methods.append("llm")

    all_results = merge_results(keyword_results, llm_results)

    if not all_results:
        return {
            "file": filename,
            "meeting": meeting,
            "status": "no_principles",
            "transcript_length": len(text),
        }

    # Create derived vCon
    derived_filename = filename.replace(".vcon.json", ".derived.vcon.json")
    derived_path = os.path.join(output_dir, meeting, derived_filename)

    derived_path, _ = create_derived_vcon(
        source_vcon_path=vcon_path,
        source_info=info,
        analysis_results=all_results,
        detection_methods=detection_methods,
        transcript_length=len(text),
        output_path=derived_path,
    )

    return {
        "file": filename,
        "meeting": meeting,
        "status": "analyzed",
        "transcript_length": len(text),
        "principles_found": [r["principle_id"] for r in all_results],
        "principles_count": len(all_results),
        "derived_vcon": derived_path,
    }


async def main():
    parser = argparse.ArgumentParser(description="Analyze IETF vCons for network design principles")
    parser.add_argument("--input-dir", default="/root/ietf-hackathon-125/ietf-meeting-vcons",
                        help="Path to ietf-meeting-vcons repo")
    parser.add_argument("--output-dir", default="/root/ietf-hackathon-125/output/derived",
                        help="Output directory for derived vCons")
    parser.add_argument("--meetings", type=str, default=None,
                        help="Comma-separated list of meetings to process (e.g., ietf120,ietf121)")
    parser.add_argument("--use-llm", action="store_true",
                        help="Enable Tier 2 LLM detection")
    parser.add_argument("--keyword-only", action="store_true",
                        help="Only use keyword detection (skip LLM)")
    parser.add_argument("--api-key", type=str, default=None,
                        help="Anthropic API key (or set ANTHROPIC_API_KEY env var)")
    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("ANTHROPIC_API_KEY")
    use_llm = args.use_llm and not args.keyword_only and api_key is not None

    meetings = args.meetings.split(",") if args.meetings else None
    vcon_files = find_vcon_files(args.input_dir, meetings)

    print(f"Found {len(vcon_files)} vCon files to process")
    if use_llm:
        print("LLM detection enabled (Tier 2)")
    else:
        print("Keyword-only detection (Tier 1)")
    print()

    results = []
    stats = {"analyzed": 0, "skipped": 0, "no_principles": 0, "total": len(vcon_files)}
    start_time = time.time()

    for i, vcon_path in enumerate(vcon_files):
        filename = os.path.basename(vcon_path)
        print(f"[{i+1}/{len(vcon_files)}] {filename}...", end=" ", flush=True)

        result = await process_vcon(vcon_path, args.output_dir, use_llm, api_key)
        results.append(result)

        status = result["status"]
        stats[status] = stats.get(status, 0) + 1

        if status == "analyzed":
            principles = ", ".join(result["principles_found"])
            print(f"✓ {result['principles_count']} principles: {principles}")
        elif status == "skipped":
            print(f"⊘ skipped ({result.get('reason', 'unknown')})")
        else:
            print(f"— no principles found")

    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"Done in {elapsed:.1f}s")
    print(f"  Total:          {stats['total']}")
    print(f"  Analyzed:       {stats['analyzed']}")
    print(f"  No principles:  {stats.get('no_principles', 0)}")
    print(f"  Skipped:        {stats['skipped']}")

    # Save results summary
    os.makedirs(os.path.join(os.path.dirname(args.output_dir), "reports"), exist_ok=True)
    results_path = os.path.join(os.path.dirname(args.output_dir), "reports", "results.json")
    with open(results_path, "w") as f:
        json.dump({"stats": stats, "results": results}, f, indent=2, default=str)
    print(f"\nResults saved to {results_path}")


if __name__ == "__main__":
    asyncio.run(main())
