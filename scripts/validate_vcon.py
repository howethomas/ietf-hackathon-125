"""Validate derived vCons against draft-ietf-vcon-vcon-container spec constraints.

Checks all three derived vCon categories:
- appended: amended vCons with added analysis
- redacted: PII-stripped vCons
- group: per-principle topic collections
"""

import json
import re
import sys


# Email pattern for redaction verification
EMAIL_PATTERN = re.compile(
    r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", re.IGNORECASE
)


def _find_emails_recursive(obj, path="") -> list[str]:
    """Find all email addresses in a JSON-like object, returning their paths."""
    found = []
    if isinstance(obj, str):
        for match in EMAIL_PATTERN.finditer(obj):
            found.append(f"{path}: {match.group()}")
    elif isinstance(obj, dict):
        for k, v in obj.items():
            found.extend(_find_emails_recursive(v, f"{path}.{k}"))
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            found.extend(_find_emails_recursive(item, f"{path}[{i}]"))
    return found


class ValidationResult:
    """Collects validation errors and warnings."""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str):
        self.errors.append(msg)

    def warn(self, msg: str):
        self.warnings.append(msg)

    @property
    def valid(self) -> bool:
        return len(self.errors) == 0

    def __str__(self):
        lines = [f"Validation: {self.file_path}"]
        if self.valid:
            lines.append("  PASS")
        else:
            lines.append(f"  FAIL ({len(self.errors)} error(s))")
        for e in self.errors:
            lines.append(f"  ERROR: {e}")
        for w in self.warnings:
            lines.append(f"  WARN:  {w}")
        return "\n".join(lines)


def validate_vcon(data: dict, file_path: str = "<unknown>") -> ValidationResult:
    """Validate a vCon dict against spec constraints.

    Returns a ValidationResult with errors and warnings.
    """
    result = ValidationResult(file_path)

    # Required top-level fields
    for field in ("vcon", "uuid", "created_at"):
        if field not in data:
            result.error(f"Missing required top-level field: '{field}'")

    # Check vcon version
    if data.get("vcon") not in ("0.0.1", "0.0.2"):
        result.warn(f"Unexpected vcon version: {data.get('vcon')}")

    # Mutual exclusivity of appended, redacted, group
    derivation_fields = [f for f in ("appended", "redacted", "group") if f in data]
    if len(derivation_fields) > 1:
        result.error(
            f"Mutual exclusivity violation: found {derivation_fields}. "
            "Only one of appended, redacted, group is allowed."
        )

    # Validate 'appended' structure
    if "appended" in data:
        appended = data["appended"]
        if not isinstance(appended, dict):
            result.error("'appended' must be an object")
        else:
            if "uuid" not in appended:
                result.error("'appended' missing required 'uuid' field")
            if "content_hash" in appended:
                ch = appended["content_hash"]
                if not isinstance(ch, str) or not ch.startswith("sha512-"):
                    result.error(
                        f"'appended.content_hash' must start with 'sha512-', got: {ch[:30]}"
                    )

    # Validate 'redacted' structure
    if "redacted" in data:
        redacted = data["redacted"]
        if not isinstance(redacted, dict):
            result.error("'redacted' must be an object")
        else:
            if "uuid" not in redacted:
                result.error("'redacted' missing required 'uuid' field")
            if "type" not in redacted:
                result.error("'redacted' missing required 'type' field")

    # Validate 'group' structure
    if "group" in data:
        group = data["group"]
        if not isinstance(group, list):
            result.error("'group' must be an array")
        else:
            for i, item in enumerate(group):
                if not isinstance(item, dict):
                    result.error(f"'group[{i}]' must be an object")
                elif "uuid" not in item:
                    result.error(f"'group[{i}]' missing required 'uuid' field")

    # Validate analysis objects
    for i, analysis in enumerate(data.get("analysis", [])):
        prefix = f"analysis[{i}]"
        for field in ("type", "vendor", "body", "encoding"):
            if field not in analysis:
                result.error(f"'{prefix}' missing required field: '{field}'")

    # Category-specific checks
    if "redacted" in data:
        _validate_redaction(data, result)

    return result


def _validate_redaction(data: dict, result: ValidationResult):
    """Additional checks for redacted vCons — verify PII is actually removed."""
    # Check parties for email addresses
    for i, party in enumerate(data.get("parties", [])):
        if "mailto" in party:
            result.error(f"Redacted vCon still has 'mailto' in parties[{i}]")

    # Scan all string values for remaining email addresses
    # (skip the 'redacted' reference object itself and known safe fields)
    scan_data = {
        k: v for k, v in data.items()
        if k not in ("redacted", "uuid", "vcon", "created_at", "updated_at")
    }
    emails = _find_emails_recursive(scan_data)
    if emails:
        result.warn(
            f"Redacted vCon may still contain {len(emails)} email address(es): "
            + "; ".join(emails[:5])
        )


def validate_file(file_path: str) -> ValidationResult:
    """Load and validate a vCon file."""
    with open(file_path, "r") as f:
        data = json.load(f)
    return validate_vcon(data, file_path)


def main():
    """Validate one or more vCon files from command line."""
    if len(sys.argv) < 2:
        print("Usage: python validate_vcon.py <file1.vcon.json> [file2.vcon.json ...]")
        sys.exit(1)

    all_valid = True
    for path in sys.argv[1:]:
        result = validate_file(path)
        print(result)
        print()
        if not result.valid:
            all_valid = False

    sys.exit(0 if all_valid else 1)


if __name__ == "__main__":
    main()
