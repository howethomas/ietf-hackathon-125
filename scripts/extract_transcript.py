"""Extract transcript text from a vCon file."""

import json


def extract_transcript(vcon_path: str) -> tuple[str | None, dict]:
    """Extract transcript text and metadata from a vCon file.

    Returns (transcript_text, metadata) or (None, {}) if no transcript found.
    """
    with open(vcon_path, "r") as f:
        data = json.load(f)

    for analysis in data.get("analysis", []):
        if analysis.get("type") == "wtf_transcription":
            body = analysis.get("body", {})
            transcript = body.get("transcript", {})
            text = transcript.get("text")
            if text:
                metadata = {
                    "language": transcript.get("language"),
                    "duration": transcript.get("duration"),
                    "confidence": transcript.get("confidence"),
                    "segments_count": len(body.get("segments", [])),
                    "youtube_metadata": body.get("metadata", {}),
                }
                return text, metadata

    return None, {}


def get_vcon_info(vcon_path: str) -> dict:
    """Extract basic info from a vCon file."""
    with open(vcon_path, "r") as f:
        data = json.load(f)

    return {
        "uuid": data.get("uuid"),
        "subject": data.get("subject", ""),
        "created_at": data.get("created_at"),
        "parties": data.get("parties", []),
        "dialog": data.get("dialog", []),
        "dialog_count": len(data.get("dialog", [])),
        "analysis_count": len(data.get("analysis", [])),
    }
