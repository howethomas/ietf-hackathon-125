"""Generate summary reports from derived vCons."""

import csv
import glob
import json
import os
import sys
from collections import defaultdict
from config import PRINCIPLES


def load_derived_vcons(derived_dir: str) -> list[dict]:
    """Load all derived vCon files."""
    files = sorted(glob.glob(os.path.join(derived_dir, "**", "*.derived.vcon.json"), recursive=True))
    vcons = []
    for f in files:
        with open(f) as fh:
            vcons.append({"path": f, "data": json.load(fh)})
    return vcons


def generate_report(derived_dir: str, reports_dir: str):
    """Generate summary reports from derived vCons."""
    vcons = load_derived_vcons(derived_dir)
    print(f"Loaded {len(vcons)} derived vCons\n")

    # Aggregate stats
    principle_freq = defaultdict(int)  # principle_id -> count of vCons
    principle_by_meeting = defaultdict(lambda: defaultdict(int))  # meeting -> principle_id -> count
    meeting_counts = defaultdict(int)  # meeting -> count of vCons with any principle
    rows = []  # for CSV

    all_principle_ids = [p["id"] for p in PRINCIPLES]

    for vcon_entry in vcons:
        data = vcon_entry["data"]
        path = vcon_entry["path"]
        meeting = os.path.basename(os.path.dirname(path))

        for analysis in data.get("analysis", []):
            if analysis.get("type") != "ietf_principle_analysis":
                continue

            body = analysis["body"]
            source_file = body.get("source_file", "")
            meeting_counts[meeting] += 1

            found_ids = set()
            for pf in body.get("principles_found", []):
                pid = pf["principle_id"]
                found_ids.add(pid)
                principle_freq[pid] += 1
                principle_by_meeting[meeting][pid] += 1

            # CSV row
            row = {
                "meeting": meeting,
                "source_file": source_file,
                "source_uuid": body.get("source_vcon_uuid", ""),
                "principles_count": body.get("principles_count", 0),
                "transcript_length": body.get("transcript_length", 0),
            }
            for pid in all_principle_ids:
                row[pid] = 1 if pid in found_ids else 0
            rows.append(row)

    # Print summary
    print("=" * 60)
    print("PRINCIPLE FREQUENCY (across all sessions)")
    print("=" * 60)
    for p in PRINCIPLES:
        count = principle_freq.get(p["id"], 0)
        bar = "█" * min(count, 50)
        print(f"  {p['name']:<40} {count:>4}  {bar}")

    print(f"\n{'=' * 60}")
    print("BY MEETING")
    print("=" * 60)
    for meeting in sorted(meeting_counts.keys()):
        count = meeting_counts[meeting]
        print(f"\n  {meeting} ({count} sessions with principles):")
        for p in PRINCIPLES:
            mc = principle_by_meeting[meeting].get(p["id"], 0)
            if mc > 0:
                print(f"    {p['name']:<40} {mc:>3}")

    # Save summary.json
    os.makedirs(reports_dir, exist_ok=True)
    summary = {
        "total_derived_vcons": len(vcons),
        "principle_frequency": dict(principle_freq),
        "by_meeting": {m: dict(v) for m, v in principle_by_meeting.items()},
        "meeting_counts": dict(meeting_counts),
    }
    summary_path = os.path.join(reports_dir, "summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSaved {summary_path}")

    # Save summary.csv
    if rows:
        csv_path = os.path.join(reports_dir, "summary.csv")
        fieldnames = ["meeting", "source_file", "source_uuid", "principles_count", "transcript_length"] + all_principle_ids
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Saved {csv_path}")


if __name__ == "__main__":
    derived_dir = sys.argv[1] if len(sys.argv) > 1 else "/root/ietf-hackathon-125/output/derived"
    reports_dir = sys.argv[2] if len(sys.argv) > 2 else "/root/ietf-hackathon-125/output/reports"
    generate_report(derived_dir, reports_dir)
