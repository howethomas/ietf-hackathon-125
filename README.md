# The Design of the Internet, Revealed by Conversation

> An exploration of Internet architecture principles as they surface in real IETF working group deliberations — extracted and analyzed using [vCons](https://datatracker.ietf.org/doc/draft-ietf-vcon-vcon-container/).

**[Read the full report →](https://howethomas.github.io/ietf-hackathon-125/)**

---

## What Is This?

The Internet wasn't designed in a single blueprint. It emerged through thousands of conversations — debates, compromises, and moments of clarity in working group sessions at the [IETF](https://www.ietf.org/). This project surfaces those design principles by analyzing **2,249 IETF session recordings** from meetings 110–123 (March 2021 – July 2025).

We processed every recorded working group transcript, searching for moments where participants discussed core network design principles — from the end-to-end principle to Postel's Law, from fate sharing to protocol ossification. The result is a design guide to the Internet, not as imagined on paper, but as practiced in the rooms where the standards are made.

## Results at a Glance

| Principle | Sessions | What It Means |
|-----------|:--------:|---------------|
| Constant Change | 565 | The Internet must be designed to evolve |
| Fate Sharing | 544 | State belongs at endpoints with a stake in it |
| Layering | 456 | Organize complexity through protocol layers |
| Simplicity | 418 | Prefer designs that can be understood and debugged |
| Rough Consensus | 331 | Progress through working code and approximate agreement |
| Trust | 252 | Trust is an architectural decision with cascading effects |
| Connectivity | 165 | Universal connectivity is the primary goal |
| Robustness / Postel's Law | 80 | Be conservative in what you send, liberal in what you accept |
| Ossification | 71 | Protocols calcify when middleboxes assume implementation details |
| End-to-End | 56 | Intelligence belongs at the endpoints, not in the network |
| Tussle | 50 | Design for ongoing conflict between stakeholders |
| Least Surprise | 4 | Protocols should behave as implementers expect |

**1,375 sessions** contained principle discussions across **14 IETF meetings** and **100+ working groups**.

## How It Works

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  2,249 Source    │────▶│  Keyword Detection│────▶│ 1,375 Appended  │
│  vCons (IETF     │     │  (12 principles)  │     │ Derived vCons   │
│  110–123)        │     └──────────────────┘     └────────┬────────┘
└─────────────────┘                                        │
                                                           ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  12 Narrative    │◀────│  Claude API       │◀────│ 12 Group vCons  │
│  Markdown Reports│     │  Synthesis        │     │ (per principle) │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

1. **Source Data** — vCons from [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons), each a recorded IETF session with metadata and transcript.
2. **Keyword Detection** — Pattern matching against principle-specific vocabularies across all transcripts.
3. **Derived vCons** — Spec-compliant [appended vCons](https://datatracker.ietf.org/doc/draft-ietf-vcon-vcon-container/) referencing originals by UUID and SHA-512 hash.
4. **Group vCons** — Per-principle aggregations with collected evidence and statistics.
5. **Narrative Reports** — Claude synthesizes each group vCon into a readable report with introduction, teaching section, IETF quotes, historical analysis, and resources.

## Repository Structure

```
├── docs/                          # GitHub Pages source (Jekyll/Minimal theme)
│   ├── README.md                  # Landing page
│   ├── SUMMARY.md                 # Navigation / table of contents
│   └── principles/                # 12 principle reports
├── site/                          # GitBook-compatible mirror of docs/
│   ├── README.md
│   ├── SUMMARY.md
│   ├── book.json                  # GitBook configuration
│   └── principles/
├── scripts/                       # Analysis pipeline
│   ├── analyze_vcons.py           # Main orchestrator
│   ├── keyword_detector.py        # Principle keyword matching
│   ├── create_derived_vcon.py     # Appended vCon generator
│   ├── create_group_vcon.py       # Group vCon aggregator
│   ├── create_redacted_vcon.py    # Redacted vCon demo
│   ├── generate_markdown_reports.py  # Claude-powered report gen
│   ├── validate_vcon.py           # Spec compliance checker
│   └── ...
├── output/
│   ├── group/                     # 12 per-principle group vCons
│   └── reports/                   # Summary data + markdown reports
└── README.md                      # This file
```

## vCon Derived Types Demonstrated

This project showcases three types of derived vCons from the [core specification](https://datatracker.ietf.org/doc/draft-ietf-vcon-vcon-container/):

| Type | Purpose | Example |
|------|---------|---------|
| **Appended** | Add analysis to an existing vCon, referencing original by UUID + hash | 1,375 principle-detection results |
| **Redacted** | Remove sensitive content while preserving analytical value | PII removal proof-of-concept |
| **Group** | Aggregate multiple vCons by theme for corpus-level analysis | 12 per-principle collections |

## Quick Start

```bash
# Clone
git clone https://github.com/howethomas/ietf-hackathon-125.git
cd ietf-hackathon-125

# Get the source vCons
git clone https://github.com/vcon-dev/ietf-meeting-vcons.git

# Run the full analysis pipeline (keyword-only, no API key needed)
python3 scripts/analyze_vcons.py --keyword-only \
  --input-dir ./ietf-meeting-vcons \
  --output-dir ./output/derived

# Generate group vCons
python3 scripts/create_group_vcon.py \
  --derived-dir ./output/derived \
  --output-dir ./output/group

# Generate markdown reports (requires ANTHROPIC_API_KEY)
export ANTHROPIC_API_KEY=sk-ant-...
python3 scripts/generate_markdown_reports.py \
  --group-dir ./output/group \
  --output-dir ./output/reports/markdown
```

## About

Produced at the **[IETF 125 Hackathon](https://www.ietf.org/meeting/125/)** (March 2026, Shenzhen) by the vCon Working Group.

- **Data**: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons)
- **Analysis**: Keyword detection + [Claude](https://anthropic.com/claude) narrative synthesis
- **Platform**: [Conserver.io](https://conserver.io)
- **Spec**: [draft-ietf-vcon-vcon-container](https://datatracker.ietf.org/doc/draft-ietf-vcon-vcon-container/)

## License

MIT
