#!/usr/bin/env python3
"""Generate rich markdown reports from per-principle group vCons.

For each group vCon, produces a markdown report with:
  1. Introduction — what the principle is and why it matters
  2. References — links to RFCs, seminal papers, and external resources
  3. IETF Conversations — illustrative quotes from actual working group sessions
  4. Historical Analysis — how discussion has evolved across IETF 110–123
  5. Resources — curated links for further learning

Uses the Claude API to synthesize narrative content from evidence data.
"""

import argparse
import asyncio
import glob
import json
import os
import sys
import textwrap
from datetime import datetime

import anthropic

# ── Principle metadata for richer reports ─────────────────────────────────────
# Extends config.py with external references, seminal papers, and resource links

PRINCIPLE_ENRICHMENT = {
    "end_to_end": {
        "seminal_papers": [
            {"title": "End-to-End Arguments in System Design", "authors": "J.H. Saltzer, D.P. Reed, D.D. Clark", "year": 1984, "url": "https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf"},
        ],
        "rfc_urls": {
            "RFC 1958": "https://www.rfc-editor.org/rfc/rfc1958",
            "RFC 3724": "https://www.rfc-editor.org/rfc/rfc3724",
        },
        "learn_more": [
            {"title": "End-to-End Principle (Wikipedia)", "url": "https://en.wikipedia.org/wiki/End-to-end_principle"},
            {"title": "RFC 3724: The Rise of the Middle", "url": "https://www.rfc-editor.org/rfc/rfc3724"},
            {"title": "IETF Architectural Principles of the Internet (RFC 1958)", "url": "https://www.rfc-editor.org/rfc/rfc1958"},
        ],
    },
    "robustness": {
        "seminal_papers": [
            {"title": "DoD Standard Internet Protocol (Postel's Law origin)", "authors": "Jon Postel", "year": 1980, "url": "https://www.rfc-editor.org/rfc/rfc760"},
        ],
        "rfc_urls": {
            "RFC 761": "https://www.rfc-editor.org/rfc/rfc761",
            "RFC 1122": "https://www.rfc-editor.org/rfc/rfc1122",
            "RFC 9413": "https://www.rfc-editor.org/rfc/rfc9413",
        },
        "learn_more": [
            {"title": "Robustness Principle (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Robustness_principle"},
            {"title": "RFC 9413: Maintaining Robust Protocols", "url": "https://www.rfc-editor.org/rfc/rfc9413"},
            {"title": "The Harmful Consequences of Postel's Maxim (draft-iab-protocol-maintenance)", "url": "https://datatracker.ietf.org/doc/html/draft-iab-protocol-maintenance"},
        ],
    },
    "layering": {
        "seminal_papers": [
            {"title": "A Protocol for Packet Network Intercommunication", "authors": "V. Cerf, R. Kahn", "year": 1974, "url": "https://www.cs.princeton.edu/courses/archive/fall06/cos561/papers/cerf74.pdf"},
        ],
        "rfc_urls": {
            "RFC 1122": "https://www.rfc-editor.org/rfc/rfc1122",
            "RFC 3439": "https://www.rfc-editor.org/rfc/rfc3439",
        },
        "learn_more": [
            {"title": "OSI Model (Wikipedia)", "url": "https://en.wikipedia.org/wiki/OSI_model"},
            {"title": "RFC 3439: Some Internet Architectural Guidelines and Philosophy", "url": "https://www.rfc-editor.org/rfc/rfc3439"},
            {"title": "Internet Protocol Suite (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Internet_protocol_suite"},
        ],
    },
    "fate_sharing": {
        "seminal_papers": [
            {"title": "The Design Philosophy of the DARPA Internet Protocols", "authors": "David D. Clark", "year": 1988, "url": "http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf"},
        ],
        "rfc_urls": {
            "RFC 1958": "https://www.rfc-editor.org/rfc/rfc1958",
        },
        "learn_more": [
            {"title": "Fate-sharing (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Fate-sharing"},
            {"title": "Clark 1988: Design Philosophy of DARPA Internet Protocols", "url": "http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf"},
            {"title": "RFC 1958: Architectural Principles of the Internet", "url": "https://www.rfc-editor.org/rfc/rfc1958"},
        ],
    },
    "least_surprise": {
        "seminal_papers": [],
        "rfc_urls": {
            "RFC 3439": "https://www.rfc-editor.org/rfc/rfc3439",
        },
        "learn_more": [
            {"title": "Principle of Least Astonishment (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Principle_of_least_astonishment"},
            {"title": "RFC 3439: Some Internet Architectural Guidelines", "url": "https://www.rfc-editor.org/rfc/rfc3439"},
        ],
    },
    "rough_consensus": {
        "seminal_papers": [
            {"title": "On Consensus and Humming in the IETF", "authors": "Pete Resnick", "year": 2014, "url": "https://www.rfc-editor.org/rfc/rfc7282"},
        ],
        "rfc_urls": {
            "RFC 7282": "https://www.rfc-editor.org/rfc/rfc7282",
        },
        "learn_more": [
            {"title": "RFC 7282: On Consensus and Humming in the IETF", "url": "https://www.rfc-editor.org/rfc/rfc7282"},
            {"title": "The Tao of IETF", "url": "https://www.ietf.org/about/participate/tao/"},
            {"title": "IETF Process (BCP 9 / RFC 2026)", "url": "https://www.rfc-editor.org/rfc/rfc2026"},
        ],
    },
    "ossification": {
        "seminal_papers": [
            {"title": "Long-Term Viability of Protocol Extension Mechanisms", "authors": "M. Thomson", "year": 2022, "url": "https://www.rfc-editor.org/rfc/rfc9170"},
        ],
        "rfc_urls": {
            "RFC 9170": "https://www.rfc-editor.org/rfc/rfc9170",
        },
        "learn_more": [
            {"title": "RFC 9170: Long-Term Viability of Protocol Extension Mechanisms", "url": "https://www.rfc-editor.org/rfc/rfc9170"},
            {"title": "GREASE (Generate Random Extensions And Sustain Extensibility)", "url": "https://www.rfc-editor.org/rfc/rfc8701"},
            {"title": "Protocol Ossification (QUIC WG context)", "url": "https://datatracker.ietf.org/doc/html/rfc9000#section-13"},
        ],
    },
    "tussle": {
        "seminal_papers": [
            {"title": "Tussle in Cyberspace: Defining Tomorrow's Internet", "authors": "D.D. Clark, J. Wroclawski, K.R. Sollins, R. Braden", "year": 2005, "url": "https://groups.csail.mit.edu/ana/Publications/PubPDFs/Tussle2002.pdf"},
        ],
        "rfc_urls": {},
        "learn_more": [
            {"title": "Tussle in Cyberspace (original paper)", "url": "https://groups.csail.mit.edu/ana/Publications/PubPDFs/Tussle2002.pdf"},
            {"title": "RFC 3724: The Rise of the Middle", "url": "https://www.rfc-editor.org/rfc/rfc3724"},
        ],
    },
    "simplicity": {
        "seminal_papers": [
            {"title": "Some Internet Architectural Guidelines and Philosophy", "authors": "R. Bush, D. Meyer", "year": 2002, "url": "https://www.rfc-editor.org/rfc/rfc3439"},
        ],
        "rfc_urls": {
            "RFC 3439": "https://www.rfc-editor.org/rfc/rfc3439",
        },
        "learn_more": [
            {"title": "RFC 3439: Some Internet Architectural Guidelines", "url": "https://www.rfc-editor.org/rfc/rfc3439"},
            {"title": "Worse is Better (Richard Gabriel)", "url": "https://www.dreamsongs.com/WorseIsBetter.html"},
            {"title": "KISS Principle (Wikipedia)", "url": "https://en.wikipedia.org/wiki/KISS_principle"},
        ],
    },
    "trust": {
        "seminal_papers": [
            {"title": "IAB Considerations for Internet Architecture", "authors": "IAB", "year": 2004, "url": "https://www.rfc-editor.org/rfc/rfc3724"},
        ],
        "rfc_urls": {
            "RFC 3724": "https://www.rfc-editor.org/rfc/rfc3724",
        },
        "learn_more": [
            {"title": "RFC 3724: The Rise of the Middle and Future of End-to-End", "url": "https://www.rfc-editor.org/rfc/rfc3724"},
            {"title": "Zero Trust Architecture (NIST SP 800-207)", "url": "https://csrc.nist.gov/publications/detail/sp/800-207/final"},
            {"title": "RFC 8555: ACME (trust anchor for Web PKI)", "url": "https://www.rfc-editor.org/rfc/rfc8555"},
        ],
    },
    "connectivity": {
        "seminal_papers": [
            {"title": "Architectural Principles of the Internet", "authors": "B. Carpenter", "year": 1996, "url": "https://www.rfc-editor.org/rfc/rfc1958"},
        ],
        "rfc_urls": {
            "RFC 1958": "https://www.rfc-editor.org/rfc/rfc1958",
        },
        "learn_more": [
            {"title": "RFC 1958: Architectural Principles of the Internet", "url": "https://www.rfc-editor.org/rfc/rfc1958"},
            {"title": "Internet Universality (UNESCO)", "url": "https://en.unesco.org/internet-universality-indicators"},
        ],
    },
    "constant_change": {
        "seminal_papers": [
            {"title": "Architectural Principles of the Internet", "authors": "B. Carpenter", "year": 1996, "url": "https://www.rfc-editor.org/rfc/rfc1958"},
        ],
        "rfc_urls": {
            "RFC 1958": "https://www.rfc-editor.org/rfc/rfc1958",
        },
        "learn_more": [
            {"title": "RFC 1958: Architectural Principles of the Internet", "url": "https://www.rfc-editor.org/rfc/rfc1958"},
            {"title": "RFC 5765: Security Design in Protocol Extensions", "url": "https://www.rfc-editor.org/rfc/rfc6709"},
            {"title": "Protocol Extensibility (Wikipedia)", "url": "https://en.wikipedia.org/wiki/Extensibility"},
        ],
    },
}

# IETF meeting dates for historical context
IETF_MEETING_DATES = {
    "ietf110": "March 2021 (Online)",
    "ietf111": "July 2021 (Online)",
    "ietf112": "November 2021 (Online)",
    "ietf113": "March 2022 (Vienna)",
    "ietf114": "July 2022 (Philadelphia)",
    "ietf115": "November 2022 (London)",
    "ietf116": "March 2023 (Yokohama)",
    "ietf117": "July 2023 (San Francisco)",
    "ietf118": "November 2023 (Prague)",
    "ietf119": "March 2024 (Brisbane)",
    "ietf120": "July 2024 (Vancouver)",
    "ietf121": "November 2024 (Dublin)",
    "ietf122": "March 2025 (Bangkok)",
    "ietf123": "July 2025 (Madrid)",
    "ietf124": "November 2025 (Shenzhen)",
}


def load_group_vcon(path: str) -> dict:
    """Load a group vCon and parse its embedded JSON attachments."""
    with open(path, "r") as f:
        data = json.load(f)

    # Parse the JSON-encoded attachment bodies
    parsed = {
        "raw": data,
        "principle": None,
        "evidence": None,
        "analysis": None,
    }

    for att in data.get("attachments", []):
        body = att.get("body", "")
        if isinstance(body, str):
            try:
                body = json.loads(body)
            except (json.JSONDecodeError, TypeError):
                pass
        if att.get("purpose") == "principle_definition":
            parsed["principle"] = body
        elif att.get("purpose") == "collected_evidence":
            parsed["evidence"] = body

    for analysis in data.get("analysis", []):
        if analysis.get("type") == "ietf_principle_corpus_summary":
            parsed["analysis"] = analysis.get("body", {})

    return parsed


def select_best_quotes(sessions: list[dict], max_quotes: int = 10) -> list[dict]:
    """Select the most illustrative conversation quotes across meetings.

    Strategy: spread quotes across the full timeline (early, middle, late),
    prefer longer/more substantive excerpts, ensure working group diversity,
    and favor higher-confidence matches.
    """
    # Build candidate pool with quality scoring
    candidates = []
    for s in sessions:
        for m in s.get("matches", []):
            ctx = m.get("context", "").strip()
            if len(ctx) < 60:  # Skip very short fragments
                continue
            meeting = s.get("meeting", "unknown")
            # Extract meeting number for timeline positioning
            try:
                meeting_num = int(meeting.replace("ietf", ""))
            except ValueError:
                meeting_num = 0

            # Quality score: longer quotes are usually more substantive,
            # higher confidence is better
            conf_score = {"high": 30, "medium": 20, "low": 10}.get(
                s.get("confidence", "low"), 0
            )
            # Reward length up to ~400 chars (diminishing returns after)
            length_score = min(len(ctx), 400) / 10
            quality = conf_score + length_score

            candidates.append({
                "context": ctx,
                "meeting": meeting,
                "meeting_num": meeting_num,
                "working_group": s.get("working_group", "unknown"),
                "subject": s.get("subject", ""),
                "confidence": s.get("confidence", "low"),
                "quality": quality,
                "source_uuid": s.get("source_uuid", ""),
            })

    if not candidates:
        return []

    # Sort by quality descending
    candidates.sort(key=lambda x: x["quality"], reverse=True)

    # Divide timeline into thirds: early (110-114), middle (115-119), late (120-123)
    early = [c for c in candidates if c["meeting_num"] <= 114]
    middle = [c for c in candidates if 115 <= c["meeting_num"] <= 119]
    late = [c for c in candidates if c["meeting_num"] >= 120]

    # Allocate slots proportionally but guarantee at least some from each era
    # (if available)
    slots_per_era = max(2, max_quotes // 3)

    selected = []
    seen_keys = set()  # meeting+wg to avoid duplication

    def pick_from(pool, n):
        picked = []
        for c in pool:
            key = f"{c['meeting']}_{c['working_group']}"
            if key not in seen_keys:
                seen_keys.add(key)
                picked.append(c)
            if len(picked) >= n:
                break
        return picked

    # Pick from each era
    selected.extend(pick_from(late, slots_per_era))    # Recent first
    selected.extend(pick_from(middle, slots_per_era))
    selected.extend(pick_from(early, slots_per_era))

    # Fill remaining slots from best remaining across all eras
    if len(selected) < max_quotes:
        remaining = [c for c in candidates
                     if f"{c['meeting']}_{c['working_group']}" not in seen_keys]
        selected.extend(pick_from(remaining, max_quotes - len(selected)))

    # Sort final selection chronologically for narrative flow
    selected.sort(key=lambda x: (x["meeting_num"], x["working_group"]))

    return selected[:max_quotes]


def build_uuid_to_path_map(vcons_dir: str) -> dict:
    """Build a mapping from original vCon UUID to its relative file path."""
    uuid_map = {}
    for f in sorted(glob.glob(os.path.join(vcons_dir, "ietf*", "ietf*.vcon.json"))):
        with open(f) as fh:
            data = json.load(fh)
        uuid_map[data.get("uuid")] = os.path.relpath(f, vcons_dir)
    return uuid_map


VCON_GITHUB_BASE = "https://github.com/vcon-dev/ietf-meeting-vcons/blob/main"


def build_prompt(parsed: dict, enrichment: dict, uuid_to_path: dict = None) -> str:
    """Build the Claude API prompt with all the context needed for the report."""
    principle = parsed["principle"]
    analysis = parsed["analysis"]
    evidence = parsed["evidence"]

    # Select best quotes
    sessions = evidence.get("sessions", []) if evidence else []
    quotes = select_best_quotes(sessions, max_quotes=10)

    # Format quotes for the prompt
    quotes_text = ""
    for i, q in enumerate(quotes, 1):
        meeting_label = IETF_MEETING_DATES.get(q["meeting"], q["meeting"])
        # Clean up transcript text
        ctx = q["context"].replace("\n", " ").strip()
        quotes_text += f"\nQuote {i} — {q['subject']} ({meeting_label}), WG: {q['working_group']}\n"
        quotes_text += f'"{ctx}"\n'
        quotes_text += f"Confidence: {q['confidence']}\n"
        # Add vCon download link if available
        if uuid_to_path and q.get("source_uuid") in uuid_to_path:
            rel_path = uuid_to_path[q["source_uuid"]]
            quotes_text += f"Source vCon: [{rel_path}]({VCON_GITHUB_BASE}/{rel_path})\n"

    # Format statistics
    meetings = analysis.get("meetings_represented", [])
    meeting_freq = analysis.get("meeting_frequency", {})
    top_wgs = analysis.get("top_working_groups", [])
    total = analysis.get("total_sessions", 0)

    freq_text = ", ".join(
        f"{m} ({IETF_MEETING_DATES.get(m, m)}): {meeting_freq.get(m, 0)}"
        for m in meetings
    )

    top_wg_text = ", ".join(
        f"[{wg['group']}](https://datatracker.ietf.org/wg/{wg['group']}/about/) ({wg['count']})"
        for wg in top_wgs[:10]
    )

    # Build a lookup of all WG datatracker links for the report
    all_wgs = analysis.get("working_groups", [])
    wg_links_text = ", ".join(
        f"[{wg}](https://datatracker.ietf.org/wg/{wg}/about/)" for wg in all_wgs[:30]
    )

    # Format references
    refs_text = ""
    for ref, url in enrichment.get("rfc_urls", {}).items():
        refs_text += f"- [{ref}]({url})\n"
    for paper in enrichment.get("seminal_papers", []):
        refs_text += f"- [{paper['title']}]({paper['url']}) — {paper['authors']} ({paper['year']})\n"

    resources_text = ""
    for link in enrichment.get("learn_more", []):
        resources_text += f"- [{link['title']}]({link['url']})\n"

    prompt = f"""You are writing a detailed markdown report about the IETF network design principle "{principle['name']}" based on analysis of IETF working group session transcripts from meetings 110 through 123 (March 2021 – July 2025).

## Principle Definition
- **Name**: {principle['name']}
- **Description**: {principle['description']}
- **RFC References**: {', '.join(principle.get('rfc_refs', []))}

## Corpus Statistics
- **Total sessions where this principle was discussed**: {total}
- **Meetings represented**: {', '.join(meetings)} ({len(meetings)} of 14 meetings)
- **Discussion frequency by meeting**: {freq_text}
- **Top working groups**: {top_wg_text}
- **Total unique working groups**: {len(analysis.get('working_groups', []))}

## Key References
{refs_text}

## Working Group Links
When referencing IETF working groups in the report, always link them to their datatracker page using this format: [wgname](https://datatracker.ietf.org/wg/wgname/about/).
Here are the working groups involved: {wg_links_text}

## Selected Conversation Excerpts from IETF Sessions
These are real excerpts from IETF working group sessions where this principle was discussed. They come from YouTube auto-captions, so they may have minor transcription artifacts. The quotes are drawn from across the full timeline (early, middle, and recent meetings) to show how the principle has been discussed over time.
{quotes_text}

## Resources for Further Learning
{resources_text}

---

Now write a comprehensive, well-structured markdown report. The report should be accessible to both Internet architects AND to technical staff and executives who are not Internet protocol specialists. Use this exact structure:

# {principle['name']}

## Introduction
Write 2-3 paragraphs introducing this principle: what it is, its origins, why it matters for Internet architecture, and its significance in the IETF's work. Reference the seminal papers and RFCs where appropriate, using markdown links.

## Understanding This Principle

This is the most important section. Write it for a smart technical person or executive who understands systems (software, distributed systems, organizational design) but is NOT an Internet protocol expert. The goal is to make the principle *click* intuitively before diving into the technical IETF discussions.

Structure this section as follows:

**The Core Idea** — Start with one clear, memorable sentence that captures the principle. Then explain it using a real-world analogy that has nothing to do with networking — something from everyday life, organizational design, city planning, postal systems, manufacturing, biology, or similar. The analogy should illuminate WHY this principle exists, not just WHAT it says.

**Why It Matters** — Explain the practical consequences. What goes wrong when you violate this principle? Give a concrete example (from networking or systems in general) of what happens when the principle is ignored versus followed. Use a "before and after" or "with and without" framing so the stakes are clear.

**The Tension** — Every good principle has a counterforce. Explain the real-world pressure that makes this principle hard to follow. Why do engineers and organizations sometimes violate it? What's the temptation? This makes the principle feel real rather than academic.

**How to Recognize It** — Give 2-3 quick "you're seeing this principle at work when..." examples that help the reader spot it in their own technical or business context. Format these as a markdown bullet list (using - or *), with each item on its own line. These should be brief, concrete, and span different domains (not just networking).

Write this section in a conversational, teaching tone — like a great professor explaining something at a whiteboard. Use short paragraphs. Avoid jargon, or define it immediately when used. Aim for roughly 500-700 words in this section.

## Early IETF Work
Briefly discuss (2-3 paragraphs) early IETF work that either supports or contradicts this principle. What RFCs, architectural discussions, or protocol decisions from the Internet's formative years (1980s-2000s) shaped this principle? Were there notable cases where the IETF community learned the hard way — protocols that violated this principle and suffered for it, or deliberate exceptions that proved controversial? This historical grounding helps readers understand that these principles aren't just theoretical — they were forged through real engineering experience.

## Key References
List the RFCs and seminal papers with links and brief (1-sentence) descriptions of each.

## This Principle in IETF Discussions
Write a narrative section that weaves together the actual conversation excerpts above to illustrate how this principle comes up in real IETF deliberations. Use blockquotes (> ) for the excerpts. Attribute each quote to its working group (linked to datatracker) and meeting. Choose the most illustrative 4-6 quotes and provide context for each — what were the participants discussing, and why did this principle matter in that context? IMPORTANT: Select quotes that span the full timeline — include at least one from an early meeting (110-114), one from the middle period (115-119), and one from recent meetings (120-123) to show how the discussion has evolved. Don't use all quotes — pick the best ones for narrative impact.

For each quote used, if a "Source vCon" link was provided, include it as a small download link after the blockquote attribution, like: *[View source vCon](url)*. This lets readers download the original conversation record.

## Historical Analysis
Analyze how discussion of this principle has evolved across IETF 110–123 ({IETF_MEETING_DATES.get(meetings[0], '')} to {IETF_MEETING_DATES.get(meetings[-1], '') if meetings else ''}). Use the frequency data to identify trends. When naming working groups, always link them to their IETF datatracker page using this format: [wgname](https://datatracker.ietf.org/wg/wgname/about/). Which working groups discuss it most, and why might that be? Are there any notable patterns — periods of increased discussion, shifts in how the principle is applied? Present the frequency data in a small markdown table.

## Resources
A curated list of resources for engineers who want to learn more about this principle — the RFCs, papers, Wikipedia articles, and other references. Use markdown links. Add 2-3 brief annotations explaining why each resource is valuable.

---

IMPORTANT GUIDELINES:
- The "Understanding This Principle" section is the heart of the report — spend real effort making the analogy vivid and the explanation intuitive
- Write in a professional but accessible tone — an IETF veteran and a new engineering manager should both find value
- Use markdown formatting: headers, blockquotes, bold, links, tables
- ALWAYS link IETF working group names to their datatracker page: [wgname](https://datatracker.ietf.org/wg/wgname/about/) — every WG mentioned in the report should be clickable
- When quoting transcripts, clean up obvious auto-caption artifacts (missing punctuation, word breaks) but preserve the speaker's meaning
- Select quotes from across the FULL timeline — do not cluster quotes in early meetings. Show how the discussion evolved from 2021 to 2025
- Do NOT invent quotes — only use the excerpts provided above
- Do NOT add fabricated statistics — only use the numbers provided
- The report should be roughly 2500-4000 words (includes teaching section and early IETF history)
- Include a brief metadata footer noting this was generated from vCon analysis
"""

    return prompt


async def generate_report(
    group_vcon_path: str,
    output_dir: str,
    client: anthropic.AsyncAnthropic,
    model: str = "claude-sonnet-4-20250514",
    uuid_to_path: dict = None,
) -> str:
    """Generate a markdown report for a single group vCon."""
    parsed = load_group_vcon(group_vcon_path)

    principle = parsed["principle"]
    if not principle:
        print(f"  SKIP: No principle definition found in {group_vcon_path}")
        return ""

    pid = principle["principle_id"]
    enrichment = PRINCIPLE_ENRICHMENT.get(pid, {"seminal_papers": [], "rfc_urls": {}, "learn_more": []})

    prompt = build_prompt(parsed, enrichment, uuid_to_path=uuid_to_path)

    print(f"  Calling Claude API for {principle['name']}...", flush=True)

    response = await client.messages.create(
        model=model,
        max_tokens=8000,
        messages=[{"role": "user", "content": prompt}],
    )

    markdown = response.content[0].text

    # Add metadata footer
    analysis = parsed["analysis"] or {}
    footer = f"""

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `{parsed['raw'].get('uuid', 'N/A')}` |
Sessions analyzed: {analysis.get('total_sessions', 'N/A')} |
Generated: {datetime.utcnow().strftime('%Y-%m-%d')}*
"""
    markdown += footer

    # Save
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{pid}.md")
    with open(output_path, "w") as f:
        f.write(markdown)

    print(f"  Saved: {output_path} ({len(markdown):,} chars)")
    return output_path


async def main():
    parser = argparse.ArgumentParser(
        description="Generate markdown reports from per-principle group vCons"
    )
    parser.add_argument(
        "--group-dir",
        default="/root/ietf-hackathon-125/output/group",
        help="Directory containing group vCon files",
    )
    parser.add_argument(
        "--output-dir",
        default="/root/ietf-hackathon-125/output/reports/markdown",
        help="Output directory for markdown reports",
    )
    parser.add_argument(
        "--model",
        default="claude-sonnet-4-20250514",
        help="Claude model to use",
    )
    parser.add_argument(
        "--api-key",
        default=None,
        help="Anthropic API key (or set ANTHROPIC_API_KEY env var)",
    )
    parser.add_argument(
        "--principles",
        default=None,
        help="Comma-separated list of principle IDs to generate (default: all)",
    )
    parser.add_argument(
        "--vcons-dir",
        default="/root/ietf-hackathon-125/ietf-meeting-vcons",
        help="Path to ietf-meeting-vcons repo (for source vCon links)",
    )
    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        # Try loading from .env file
        env_path = os.path.join(os.path.dirname(args.group_dir), "..", ".env")
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    if line.strip().startswith("ANTHROPIC_API_KEY="):
                        api_key = line.strip().split("=", 1)[1].strip().strip('"').strip("'")
                        break
        # Also check /root/.env
        if not api_key and os.path.exists("/root/.env"):
            with open("/root/.env") as f:
                for line in f:
                    if line.strip().startswith("ANTHROPIC_API_KEY="):
                        api_key = line.strip().split("=", 1)[1].strip().strip('"').strip("'")
                        break

    if not api_key:
        print("ERROR: No ANTHROPIC_API_KEY found. Set it via --api-key, env var, or .env file.")
        sys.exit(1)

    client = anthropic.AsyncAnthropic(api_key=api_key)

    # Build UUID-to-path map for source vCon links
    uuid_to_path = {}
    if os.path.isdir(args.vcons_dir):
        print(f"Building vCon UUID map from {args.vcons_dir}...")
        uuid_to_path = build_uuid_to_path_map(args.vcons_dir)
        print(f"  Indexed {len(uuid_to_path)} source vCons")
    else:
        print(f"Warning: vCons directory not found at {args.vcons_dir}, reports will not include source links")

    # Find group vCon files
    pattern = os.path.join(args.group_dir, "*.group.vcon.json")
    files = sorted(glob.glob(pattern))

    if not files:
        print(f"No group vCon files found in {args.group_dir}")
        sys.exit(1)

    # Filter by principle if specified
    if args.principles:
        selected = set(args.principles.split(","))
        files = [f for f in files if os.path.basename(f).replace(".group.vcon.json", "") in selected]

    print(f"Generating markdown reports for {len(files)} principles")
    print(f"Output: {args.output_dir}")
    print(f"Model: {args.model}")
    print()

    results = []
    for path in files:
        pid = os.path.basename(path).replace(".group.vcon.json", "")
        print(f"[{len(results)+1}/{len(files)}] {pid}")
        try:
            output = await generate_report(path, args.output_dir, client, args.model, uuid_to_path=uuid_to_path)
            results.append(output)
        except Exception as e:
            print(f"  ERROR: {e}")
            results.append("")

    # Generate index
    index_path = os.path.join(args.output_dir, "README.md")
    with open(index_path, "w") as f:
        f.write("# IETF Network Design Principles — Analysis Reports\n\n")
        f.write("Reports generated from analysis of IETF working group session transcripts ")
        f.write("(meetings 110–123, March 2021 – July 2025) using vCon-based conversation analysis.\n\n")
        f.write("## Principles\n\n")
        f.write("| Principle | Sessions | Meetings | Report |\n")
        f.write("|-----------|----------|----------|--------|\n")
        for path in files:
            parsed = load_group_vcon(path)
            principle = parsed.get("principle", {})
            analysis = parsed.get("analysis", {})
            pid = principle.get("principle_id", "unknown") if principle else "unknown"
            name = principle.get("name", "Unknown") if principle else "Unknown"
            total = analysis.get("total_sessions", 0) if analysis else 0
            meetings = len(analysis.get("meetings_represented", [])) if analysis else 0
            f.write(f"| {name} | {total} | {meetings} | [{pid}.md]({pid}.md) |\n")
        f.write(f"\n---\n\n*Generated: {datetime.utcnow().strftime('%Y-%m-%d')} | ")
        f.write("Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) | ")
        f.write("IETF 125 Hackathon*\n")

    print(f"\nIndex: {index_path}")
    print(f"Done! Generated {len([r for r in results if r])} reports")


if __name__ == "__main__":
    asyncio.run(main())
