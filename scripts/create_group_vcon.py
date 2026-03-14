"""Create per-principle group vCons that aggregate all sessions discussing a principle.

Uses the 'group' field per draft-ietf-vcon-vcon-container to reference
multiple source vCons. Creates 12 group vCons (one per IETF principle),
each serving as a standalone analysis target for that principle's discussion
across IETF meetings.
"""

import argparse
import glob
import json
import os
import uuid
from collections import defaultdict
from datetime import datetime, timezone

from config import PRINCIPLES


def load_derived_vcons(derived_dir: str) -> list[dict]:
    """Load all appended derived vCons from the output directory."""
    pattern = os.path.join(derived_dir, "**", "*.derived.vcon.json")
    files = sorted(glob.glob(pattern, recursive=True))

    vcons = []
    for path in files:
        with open(path, "r") as f:
            data = json.load(f)
        data["_file_path"] = path
        vcons.append(data)

    return vcons


def build_group_vcon(
    principle: dict,
    matched_sessions: list[dict],
) -> dict:
    """Build a group vCon for a single principle.

    Args:
        principle: Principle definition from config.PRINCIPLES.
        matched_sessions: List of dicts with session info and evidence.

    Returns:
        The group vCon dict.
    """
    now = datetime.now(timezone.utc).isoformat()

    # Collect unique source vCon UUIDs for the group array
    group_refs = []
    seen_uuids = set()
    for session in matched_sessions:
        source_uuid = session["source_uuid"]
        if source_uuid not in seen_uuids:
            group_refs.append({"uuid": source_uuid})
            seen_uuids.add(source_uuid)

    # Collect meeting and working group statistics
    meetings = sorted(set(s["meeting"] for s in matched_sessions))
    working_groups = sorted(set(s.get("working_group", "unknown") for s in matched_sessions))

    # Count per working group
    wg_counts = defaultdict(int)
    for s in matched_sessions:
        wg_counts[s.get("working_group", "unknown")] += 1
    top_wgs = sorted(wg_counts.items(), key=lambda x: -x[1])

    # Count per meeting for trend analysis
    meeting_counts = defaultdict(int)
    for s in matched_sessions:
        meeting_counts[s["meeting"]] += 1

    # Build the evidence attachment
    evidence_sessions = []
    for session in matched_sessions:
        evidence_sessions.append({
            "source_uuid": session["source_uuid"],
            "meeting": session["meeting"],
            "working_group": session.get("working_group", "unknown"),
            "subject": session.get("subject", ""),
            "matches": session.get("matches", []),
            "confidence": session.get("confidence", "low"),
        })

    # Determine meeting range
    meeting_range = f"{meetings[0]}-{meetings[-1]}" if meetings else "unknown"

    group_vcon = {
        "vcon": "0.0.1",
        "uuid": str(uuid.uuid4()),
        "created_at": now,
        "updated_at": now,
        "subject": f"{principle['name']} — IETF Discussion Corpus ({meeting_range})",
        # Spec-compliant: 'group' references multiple vCons
        # (mutually exclusive with 'appended' and 'redacted')
        "group": group_refs,
        "parties": [],
        "dialog": [],
        "attachments": [
            {
                "type": "application/json",
                "purpose": "principle_definition",
                "body": json.dumps({
                    "principle_id": principle["id"],
                    "name": principle["name"],
                    "description": principle["description"],
                    "rfc_refs": principle["rfc_refs"],
                }),
                "encoding": "json",
            },
            {
                "type": "application/json",
                "purpose": "collected_evidence",
                "body": json.dumps({
                    "total_sessions": len(matched_sessions),
                    "sessions": evidence_sessions,
                }),
                "encoding": "json",
            },
        ],
        "analysis": [
            {
                "type": "ietf_principle_corpus_summary",
                "dialog": [],
                "vendor": "ietf-hackathon-125",
                "body": {
                    "principle_id": principle["id"],
                    "principle_name": principle["name"],
                    "total_sessions": len(matched_sessions),
                    "total_unique_sources": len(group_refs),
                    "meetings_represented": meetings,
                    "working_groups": working_groups,
                    "top_working_groups": [
                        {"group": wg, "count": count} for wg, count in top_wgs[:10]
                    ],
                    "meeting_frequency": {
                        m: meeting_counts[m] for m in sorted(meeting_counts)
                    },
                },
                "encoding": "json",
            }
        ],
    }

    return group_vcon


def extract_session_info(derived_vcon: dict) -> list[dict]:
    """Extract per-principle session info from an appended derived vCon.

    Returns a list of dicts, one per principle found in this vCon.
    """
    sessions = []

    # Get source UUID from the appended reference
    appended = derived_vcon.get("appended", {})
    source_uuid = appended.get("uuid", "")
    if not source_uuid:
        # Fallback: look in analysis body
        for analysis in derived_vcon.get("analysis", []):
            body = analysis.get("body", {})
            if body.get("source_vcon_uuid"):
                source_uuid = body["source_vcon_uuid"]
                break

    # Extract meeting and working group from file path or subject
    file_path = derived_vcon.get("_file_path", "")
    meeting = os.path.basename(os.path.dirname(file_path)) if file_path else "unknown"
    subject = derived_vcon.get("subject", "")

    # Try to extract working group from filename
    filename = os.path.basename(file_path) if file_path else ""
    wg = "unknown"
    # Pattern: ietf120_6man_33020.derived.vcon.json
    parts = filename.split("_")
    if len(parts) >= 2:
        wg = parts[1]

    for analysis in derived_vcon.get("analysis", []):
        if analysis.get("type") != "ietf_principle_analysis":
            continue

        body = analysis.get("body", {})
        for principle_result in body.get("principles_found", []):
            pid = principle_result.get("principle_id")
            if not pid:
                continue

            # Collect match evidence (truncate for the group vCon)
            matches = []
            for m in principle_result.get("keyword_matches", [])[:5]:
                matches.append({
                    "context": m.get("context", "")[:300],
                    "matched_pattern": m.get("matched_pattern", ""),
                })

            sessions.append({
                "principle_id": pid,
                "source_uuid": source_uuid,
                "meeting": meeting,
                "working_group": wg,
                "subject": subject.replace("Principles Analysis: ", ""),
                "matches": matches,
                "confidence": principle_result.get("overall_confidence", "low"),
            })

    return sessions


def create_all_group_vcons(
    derived_dir: str,
    output_dir: str,
) -> list[tuple[str, dict]]:
    """Create group vCons for all principles.

    Args:
        derived_dir: Directory containing appended derived vCons.
        output_dir: Directory to write group vCons.

    Returns:
        List of (path, vcon_dict) tuples for each group vCon created.
    """
    print(f"Loading derived vCons from {derived_dir}...")
    derived_vcons = load_derived_vcons(derived_dir)
    print(f"Loaded {len(derived_vcons)} derived vCons")

    # Collect all session info, grouped by principle
    principle_sessions = defaultdict(list)
    for dv in derived_vcons:
        for session in extract_session_info(dv):
            pid = session.pop("principle_id")
            principle_sessions[pid].append(session)

    # Build a group vCon for each principle
    results = []
    os.makedirs(output_dir, exist_ok=True)

    for principle in PRINCIPLES:
        pid = principle["id"]
        sessions = principle_sessions.get(pid, [])

        if not sessions:
            print(f"  {principle['name']}: no sessions found, skipping")
            continue

        group_vcon = build_group_vcon(principle, sessions)
        output_path = os.path.join(output_dir, f"{pid}.group.vcon.json")

        with open(output_path, "w") as f:
            json.dump(group_vcon, f, indent=2, default=str)

        print(
            f"  {principle['name']}: {len(sessions)} sessions, "
            f"{len(group_vcon['group'])} unique sources -> {output_path}"
        )
        results.append((output_path, group_vcon))

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Create per-principle group vCons from derived analysis vCons"
    )
    parser.add_argument(
        "--derived-dir",
        default="/root/ietf-hackathon-125/output/derived",
        help="Directory containing appended derived vCons",
    )
    parser.add_argument(
        "--output-dir",
        default="/root/ietf-hackathon-125/output/group",
        help="Output directory for group vCons",
    )
    args = parser.parse_args()

    results = create_all_group_vcons(args.derived_dir, args.output_dir)
    print(f"\nCreated {len(results)} group vCons")


if __name__ == "__main__":
    main()
