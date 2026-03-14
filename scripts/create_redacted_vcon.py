"""Create spec-compliant redacted vCons with PII removed.

Uses the 'redacted' field per draft-ietf-vcon-vcon-container to reference
the unredacted original. The redacted vCon preserves all non-PII content
while anonymizing party names and removing email addresses.
"""

import copy
import json
import os
import re
import uuid
from datetime import datetime, timezone

from hash_utils import compute_content_hash

# Regex to match email addresses
EMAIL_PATTERN = re.compile(
    r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", re.IGNORECASE
)


def _redact_string(value: str) -> str:
    """Replace email addresses in a string with [REDACTED]."""
    return EMAIL_PATTERN.sub("[REDACTED]", value)


def _redact_recursive(obj):
    """Recursively redact email addresses from all string values in a JSON-like object."""
    if isinstance(obj, str):
        return _redact_string(obj)
    elif isinstance(obj, dict):
        return {k: _redact_recursive(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_redact_recursive(item) for item in obj]
    return obj


def _anonymize_parties(parties: list[dict]) -> list[dict]:
    """Anonymize party information: remove emails, replace names with roles.

    Per the spec, when data is removed from arrays, implementations should
    create empty placeholders so that array indices do not change.
    """
    anonymized = []
    chair_count = 0
    attendee_count = 0

    for party in parties:
        anon_party = {}
        role = party.get("role", "participant")

        # Assign anonymous name based on role
        if role == "chair":
            chair_count += 1
            anon_party["name"] = f"Chair {chair_count}"
        elif role == "attendee":
            attendee_count += 1
            anon_party["name"] = f"Attendee Group {attendee_count}"
        else:
            anon_party["name"] = f"Participant ({role})"

        # Keep role (not PII)
        anon_party["role"] = role

        # Explicitly remove PII fields
        # Do NOT copy: mailto, tel, name (original)

        anonymized.append(anon_party)

    return anonymized


def create_redacted_vcon(
    source_vcon_path: str,
    output_path: str,
) -> tuple[str, dict]:
    """Create a redacted vCon with PII removed.

    Per the vCon spec, the 'redacted' field references the unredacted or prior,
    less-redacted vCon. When PII is removed, the redacted version maintains
    referential integrity (array indices preserved) while stripping sensitive data.

    Args:
        source_vcon_path: Path to the original (unredacted) vCon file.
        output_path: Where to save the redacted vCon.

    Returns:
        Tuple of (output_path, redacted_vcon_dict) for inspection.
    """
    with open(source_vcon_path, "r") as f:
        source = json.load(f)

    now = datetime.now(timezone.utc).isoformat()
    content_hash = compute_content_hash(source_vcon_path)

    # Start with a deep copy, then redact
    redacted = copy.deepcopy(source)

    # New identity for the redacted version
    redacted["uuid"] = str(uuid.uuid4())
    redacted["created_at"] = now
    redacted["updated_at"] = now
    redacted["subject"] = f"[Redacted] {source.get('subject', 'Unknown')}"

    # Spec-compliant: 'redacted' references the unredacted original
    # (mutually exclusive with 'appended' and 'group')
    redacted["redacted"] = {
        "uuid": source["uuid"],
        "type": "pii_removal",
        "content_hash": content_hash,
    }

    # Remove any group/appended that might exist on the source
    redacted.pop("group", None)
    redacted.pop("appended", None)

    # Anonymize parties (preserve array indices per spec)
    redacted["parties"] = _anonymize_parties(source.get("parties", []))

    # Redact email addresses from all attachments
    redacted["attachments"] = _redact_recursive(source.get("attachments", []))

    # Redact email addresses from all analysis bodies (e.g., transcript text)
    redacted["analysis"] = _redact_recursive(source.get("analysis", []))

    # Dialog URLs (YouTube) are public, keep them as-is

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(redacted, f, indent=2, default=str)

    return output_path, redacted
