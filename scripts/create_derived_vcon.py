"""Create spec-compliant derived vCons with IETF principle analysis results.

Uses the 'appended' field per draft-ietf-vcon-vcon-container to reference
the original vCon being analyzed. The appended, redacted, and group fields
are mutually exclusive — this module only creates appended (amended) vCons.
"""

import json
import os
import uuid
from datetime import datetime, timezone

from config import ANALYSIS_TYPE, ANALYSIS_VENDOR, ANALYSIS_VERSION
from hash_utils import compute_content_hash


def create_derived_vcon(
    source_vcon_path: str,
    source_info: dict,
    analysis_results: list[dict],
    detection_methods: list[str],
    transcript_length: int,
    output_path: str,
) -> tuple[str, dict]:
    """Create an appended derived vCon containing principle analysis results.

    Per the vCon spec, the 'appended' field references the prior vCon to which
    new information (analysis) is being added. This preserves the provenance
    chain while allowing new analysis to be attached without modifying the
    signed original.

    Args:
        source_vcon_path: Path to the original vCon file.
        source_info: Dict with uuid, subject, parties, dialog from original.
        analysis_results: List of principle detection results.
        detection_methods: List of methods used (e.g., ["keyword", "llm"]).
        transcript_length: Length of the transcript text analyzed.
        output_path: Where to save the derived vCon.

    Returns:
        Tuple of (output_path, derived_vcon_dict) for inspection.
    """
    # Build summary
    principle_names = [r["principle_name"] for r in analysis_results]
    summary = (
        f"Found {len(analysis_results)} IETF principle(s) discussed: "
        + ", ".join(principle_names)
    )

    now = datetime.now(timezone.utc).isoformat()
    content_hash = compute_content_hash(source_vcon_path)

    # Build the appended derived vCon
    derived = {
        "vcon": "0.0.1",
        "uuid": str(uuid.uuid4()),
        "created_at": now,
        "updated_at": now,
        "subject": f"Principles Analysis: {source_info.get('subject', 'Unknown')}",
        # Spec-compliant: 'appended' references the prior vCon
        # (mutually exclusive with 'redacted' and 'group')
        "appended": {
            "uuid": source_info["uuid"],
            "content_hash": content_hash,
        },
        # Carry forward parties and dialog from source for standalone analysis
        "parties": source_info.get("parties", []),
        "dialog": source_info.get("dialog", []),
        "attachments": [],
        "analysis": [
            {
                "type": ANALYSIS_TYPE,
                "dialog": [],
                "vendor": ANALYSIS_VENDOR,
                "body": {
                    "version": ANALYSIS_VERSION,
                    "source_vcon_uuid": source_info["uuid"],
                    "source_file": os.path.basename(source_vcon_path),
                    "analysis_timestamp": now,
                    "detection_methods": detection_methods,
                    "transcript_length": transcript_length,
                    "principles_found": analysis_results,
                    "principles_count": len(analysis_results),
                    "summary": summary,
                },
                "encoding": "json",
            }
        ],
    }

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(derived, f, indent=2, default=str)

    return output_path, derived
