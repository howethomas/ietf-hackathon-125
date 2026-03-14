"""Tier 2: LLM-based detection of IETF principles using Claude API."""

import json
import asyncio
from anthropic import AsyncAnthropic
from config import PRINCIPLES


CHUNK_SIZE = 40000
CHUNK_OVERLAP = 2000
MAX_CONCURRENT = 3

SYSTEM_PROMPT = """You are an expert in IETF standards and Internet architecture principles.
Analyze the following transcript excerpt from an IETF meeting and identify any discussions
of network design principles. Look for both explicit references (naming the principle)
and implicit discussions (describing the concept without naming it).

Return your analysis as a JSON array. Each element should have:
- principle_id: one of the IDs listed below
- confidence: "high", "medium", or "low"
- evidence: array of objects with "quote" (exact text from transcript) and "explanation"

If no principles are discussed, return an empty array [].

Principles to look for:
"""

def _build_principle_list() -> str:
    lines = []
    for p in PRINCIPLES:
        lines.append(f'- {p["id"]}: {p["name"]} — {p["description"]}')
    return "\n".join(lines)


def _chunk_text(text: str) -> list[str]:
    """Split text into overlapping chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        chunks.append(text[start:end])
        start = end - CHUNK_OVERLAP
    return chunks


async def _analyze_chunk(client: AsyncAnthropic, chunk: str, chunk_idx: int, semaphore: asyncio.Semaphore) -> list[dict]:
    """Analyze a single chunk with Claude."""
    async with semaphore:
        try:
            response = await client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                system=SYSTEM_PROMPT + _build_principle_list(),
                messages=[{
                    "role": "user",
                    "content": f"Analyze this IETF meeting transcript excerpt (chunk {chunk_idx + 1}):\n\n{chunk}"
                }],
            )
            text = response.content[0].text
            # Extract JSON from response
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0]
            elif "```" in text:
                text = text.split("```")[1].split("```")[0]
            return json.loads(text.strip())
        except Exception as e:
            print(f"  Warning: LLM analysis failed for chunk {chunk_idx}: {e}")
            return []


async def detect_principles_llm(text: str, api_key: str) -> list[dict]:
    """Detect IETF principle discussions using Claude API.

    Returns a list of principle match results.
    """
    client = AsyncAnthropic(api_key=api_key)
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)
    chunks = _chunk_text(text)

    print(f"  LLM analysis: {len(chunks)} chunks...")
    tasks = [_analyze_chunk(client, chunk, i, semaphore) for i, chunk in enumerate(chunks)]
    chunk_results = await asyncio.gather(*tasks)

    # Merge results across chunks by principle
    principle_map = {}
    for chunk_result in chunk_results:
        for item in chunk_result:
            pid = item.get("principle_id")
            if not pid:
                continue
            if pid not in principle_map:
                principle_map[pid] = {
                    "principle_id": pid,
                    "principle_name": next((p["name"] for p in PRINCIPLES if p["id"] == pid), pid),
                    "evidence": [],
                    "confidence": item.get("confidence", "low"),
                    "detection_method": "llm",
                }
            principle_map[pid]["evidence"].extend(item.get("evidence", []))
            # Upgrade confidence if higher found
            conf_order = {"low": 0, "medium": 1, "high": 2}
            if conf_order.get(item.get("confidence"), 0) > conf_order.get(principle_map[pid]["confidence"], 0):
                principle_map[pid]["confidence"] = item["confidence"]

    results = list(principle_map.values())
    for r in results:
        r["match_count"] = len(r["evidence"])

    return results
