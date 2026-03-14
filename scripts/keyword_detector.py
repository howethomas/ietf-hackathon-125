"""Tier 1: Keyword/regex-based detection of IETF principles in transcript text."""

import re
from config import PRINCIPLES, CONTEXT_CHARS


def detect_principles_keywords(text: str) -> list[dict]:
    """Detect IETF principle discussions using keyword/regex matching.

    Returns a list of principle match results (only for principles with matches).
    """
    results = []
    text_lower = text.lower()

    for principle in PRINCIPLES:
        matches = []
        for pattern_str in principle["keywords"]:
            pattern = re.compile(pattern_str, re.IGNORECASE)
            for match in pattern.finditer(text):
                start = max(0, match.start() - CONTEXT_CHARS)
                end = min(len(text), match.end() + CONTEXT_CHARS)
                context = text[start:end].strip()

                matches.append({
                    "keyword": match.group(),
                    "pattern": pattern_str,
                    "position": match.start(),
                    "context": context,
                })

        if matches:
            # Deduplicate overlapping matches (same position within 50 chars)
            deduped = []
            seen_positions = set()
            for m in sorted(matches, key=lambda x: x["position"]):
                bucket = m["position"] // 50
                if bucket not in seen_positions:
                    seen_positions.add(bucket)
                    deduped.append(m)

            results.append({
                "principle_id": principle["id"],
                "principle_name": principle["name"],
                "match_count": len(deduped),
                "matches": deduped,
                "detection_method": "keyword",
                "confidence": "high" if len(deduped) >= 3 else "medium" if len(deduped) >= 2 else "low",
            })

    return results
