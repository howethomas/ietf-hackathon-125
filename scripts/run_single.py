#!/usr/bin/env python3
"""Proof-of-concept: run the full pipeline on ONE vCon to validate all three
derived vCon categories before scaling to the full corpus.

Produces:
  1. Appended vCon — principle analysis added to source
  2. Redacted vCon — PII stripped from source
  3. Group vCon   — mini example grouping this single source

All outputs saved to output/proof_of_concept/ for inspection.
"""

import json
import os
import sys

# Ensure scripts/ is on the path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from extract_transcript import extract_transcript, get_vcon_info
from keyword_detector import detect_principles_keywords
from create_derived_vcon import create_derived_vcon
from create_redacted_vcon import create_redacted_vcon
from create_group_vcon import build_group_vcon
from validate_vcon import validate_vcon
from config import PRINCIPLES

# ── Configuration ─────────────────────────────────────────────────────────────

# Try local path first, then server path
LOCAL_VCONS = os.path.join(
    os.path.dirname(SCRIPT_DIR), "..", "ietf-meeting-vcons"
)
SERVER_VCONS = "/root/ietf-hackathon-125/ietf-meeting-vcons"

PROOF_VCON = "ietf120/ietf120_6man_33020.vcon.json"
OUTPUT_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "output", "proof_of_concept")


def find_source_vcon() -> str:
    """Locate the proof-of-concept source vCon."""
    for base in [LOCAL_VCONS, SERVER_VCONS]:
        path = os.path.join(base, PROOF_VCON)
        if os.path.exists(path):
            return os.path.realpath(path)
    # Also check if ietf-meeting-vcons is a sibling directory
    sibling = os.path.join(os.path.dirname(SCRIPT_DIR), "..", "ietf-meeting-vcons", PROOF_VCON)
    if os.path.exists(sibling):
        return os.path.realpath(sibling)
    print(f"ERROR: Cannot find source vCon: {PROOF_VCON}")
    print(f"  Searched: {LOCAL_VCONS}")
    print(f"  Searched: {SERVER_VCONS}")
    sys.exit(1)


def print_section(title: str):
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def print_vcon_summary(label: str, vcon: dict):
    """Print a concise summary of a vCon."""
    print(f"  [{label}]")
    print(f"  UUID:    {vcon.get('uuid', 'N/A')}")
    print(f"  Subject: {vcon.get('subject', 'N/A')}")

    # Show derivation type
    if "appended" in vcon:
        print(f"  Type:    APPENDED (references: {vcon['appended'].get('uuid', 'N/A')[:20]}...)")
        print(f"  Hash:    {vcon['appended'].get('content_hash', 'N/A')[:40]}...")
    elif "redacted" in vcon:
        print(f"  Type:    REDACTED (references: {vcon['redacted'].get('uuid', 'N/A')[:20]}...)")
        print(f"  Redact:  {vcon['redacted'].get('type', 'N/A')}")
    elif "group" in vcon:
        print(f"  Type:    GROUP ({len(vcon['group'])} member(s))")

    print(f"  Parties: {len(vcon.get('parties', []))}")
    print(f"  Dialog:  {len(vcon.get('dialog', []))}")
    print(f"  Attach:  {len(vcon.get('attachments', []))}")
    print(f"  Analysis:{len(vcon.get('analysis', []))}")
    print()


def main():
    print_section("IETF 125 Hackathon — vCon Derived Types Proof-of-Concept")

    # ── Find and load source vCon ─────────────────────────────────────────
    source_path = find_source_vcon()
    print(f"Source vCon: {source_path}")

    info = get_vcon_info(source_path)
    print(f"  UUID:    {info['uuid']}")
    print(f"  Subject: {info['subject']}")
    print(f"  Parties: {len(info['parties'])}")
    print(f"  Dialog:  {info['dialog_count']}")

    # ── Extract transcript ────────────────────────────────────────────────
    print_section("Step 1: Extract Transcript")
    text, metadata = extract_transcript(source_path)
    if not text:
        print("ERROR: No transcript found in source vCon!")
        sys.exit(1)
    print(f"  Transcript length: {len(text):,} characters")
    print(f"  Language: {metadata.get('language', 'unknown')}")
    print(f"  Segments: {metadata.get('segments_count', 0)}")

    # ── Keyword detection ─────────────────────────────────────────────────
    print_section("Step 2: Keyword Detection (Tier 1)")
    keyword_results = detect_principles_keywords(text)

    if not keyword_results:
        print("  No principles detected via keywords.")
    else:
        for kr in keyword_results:
            print(f"  {kr['principle_name']}: {kr['match_count']} match(es) [{kr['confidence']}]")
            for m in kr["matches"][:2]:
                snippet = m["context"][:120].replace("\n", " ")
                print(f"    -> \"{snippet}...\"")

    # ── Create Category 1: Appended vCon ──────────────────────────────────
    print_section("Step 3: Create APPENDED Derived vCon (Category 1)")

    # Merge keyword results into the format expected by create_derived_vcon
    merged_results = []
    for kr in keyword_results:
        merged_results.append({
            "principle_id": kr["principle_id"],
            "principle_name": kr["principle_name"],
            "keyword_matches": kr["matches"],
            "keyword_match_count": kr["match_count"],
            "keyword_confidence": kr["confidence"],
            "llm_evidence": [],
            "llm_confidence": None,
            "detection_methods": ["keyword"],
            "overall_confidence": kr["confidence"],
        })

    appended_path = os.path.join(OUTPUT_DIR, "appended", "ietf120_6man_33020.derived.vcon.json")
    appended_path, appended_vcon = create_derived_vcon(
        source_vcon_path=source_path,
        source_info=info,
        analysis_results=merged_results,
        detection_methods=["keyword"],
        transcript_length=len(text),
        output_path=appended_path,
    )
    print_vcon_summary("Appended vCon", appended_vcon)
    print(f"  Saved to: {appended_path}")

    # ── Create Category 2: Redacted vCon ──────────────────────────────────
    print_section("Step 4: Create REDACTED Derived vCon (Category 2)")

    redacted_path = os.path.join(OUTPUT_DIR, "redacted", "ietf120_6man_33020.redacted.vcon.json")
    redacted_path, redacted_vcon = create_redacted_vcon(
        source_vcon_path=source_path,
        output_path=redacted_path,
    )
    print_vcon_summary("Redacted vCon", redacted_vcon)

    # Show what was redacted
    with open(source_path, "r") as f:
        source_data = json.load(f)
    print("  Party comparison (original -> redacted):")
    for i, (orig, redc) in enumerate(
        zip(source_data.get("parties", []), redacted_vcon.get("parties", []))
    ):
        orig_name = orig.get("name", "?")
        orig_email = orig.get("mailto", "none")
        redc_name = redc.get("name", "?")
        redc_email = redc.get("mailto", "REMOVED")
        print(f"    [{i}] {orig_name} <{orig_email}> -> {redc_name} <{redc_email}>")

    print(f"\n  Saved to: {redacted_path}")

    # ── Create Category 3: Group vCon (mini example) ──────────────────────
    print_section("Step 5: Create GROUP Derived vCon (Category 3 — Mini Example)")

    # For the proof-of-concept, create a group vCon for each detected principle
    # using just this single source vCon
    group_vcons_created = []
    for kr in keyword_results:
        pid = kr["principle_id"]
        principle = next((p for p in PRINCIPLES if p["id"] == pid), None)
        if not principle:
            continue

        session_info = {
            "source_uuid": info["uuid"],
            "meeting": "ietf120",
            "working_group": "6man",
            "subject": info["subject"],
            "matches": [{"context": m["context"][:300], "matched_pattern": m["pattern"]} for m in kr["matches"][:5]],
            "confidence": kr["confidence"],
        }

        group_vcon = build_group_vcon(principle, [session_info])
        group_path = os.path.join(OUTPUT_DIR, "group", f"{pid}.group.vcon.json")
        os.makedirs(os.path.dirname(group_path), exist_ok=True)
        with open(group_path, "w") as f:
            json.dump(group_vcon, f, indent=2, default=str)

        print_vcon_summary(f"Group vCon: {principle['name']}", group_vcon)
        print(f"  Saved to: {group_path}")
        group_vcons_created.append((group_path, group_vcon))

    # ── Validate all outputs ──────────────────────────────────────────────
    print_section("Step 6: Validate All Derived vCons")

    all_valid = True
    all_vcons = [
        ("Appended", appended_path, appended_vcon),
        ("Redacted", redacted_path, redacted_vcon),
    ]
    for path, gv in group_vcons_created:
        all_vcons.append(("Group", path, gv))

    for label, path, vcon in all_vcons:
        result = validate_vcon(vcon, f"{label}: {os.path.basename(path)}")
        print(result)
        if not result.valid:
            all_valid = False
        print()

    # ── Summary ───────────────────────────────────────────────────────────
    print_section("Summary")
    print(f"  Source vCon:     {os.path.basename(source_path)}")
    print(f"  Source UUID:     {info['uuid']}")
    print(f"  Transcript:      {len(text):,} chars")
    print(f"  Principles found:{len(keyword_results)}")
    print()
    print(f"  Category 1 (Appended):  1 vCon created")
    print(f"  Category 2 (Redacted):  1 vCon created")
    print(f"  Category 3 (Group):     {len(group_vcons_created)} vCon(s) created")
    print()
    print(f"  Output directory: {OUTPUT_DIR}")
    print(f"  All valid: {'YES' if all_valid else 'NO — check errors above'}")

    if all_valid:
        print("\n  Ready to scale to full corpus!")
    else:
        print("\n  Fix validation errors before proceeding.")
        sys.exit(1)


if __name__ == "__main__":
    main()
