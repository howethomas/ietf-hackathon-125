# The Design of the Internet, Revealed by Conversation

**An exploration of Internet architecture principles as they surface in real IETF working group deliberations — extracted and analyzed using vCons.**

---

## What Is This?

The Internet wasn't designed in a single blueprint. It emerged over decades through thousands of conversations — debates, compromises, and moments of clarity in working group sessions at the [Internet Engineering Task Force (IETF)](https://www.ietf.org/). The design principles that hold the Internet together are not just written in RFCs. They are *lived* in these conversations, invoked when engineers face hard trade-offs, and sometimes bent when reality pushes back.

This site is an attempt to surface those principles by analyzing **2,249 IETF session recordings** from meetings 110 through 123 (March 2021 – July 2025). We processed the transcripts of every recorded working group session, searching for moments where participants discussed, debated, or applied core network design principles — from the end-to-end principle to Postel's Law, from fate sharing to protocol ossification.

The result is a **design guide to the Internet**, not as it was imagined on paper, but as it is practiced in the rooms where the standards are made.

## How to Read This Guide

Each principle has its own chapter with:

- **Introduction** — What the principle is and where it came from
- **Understanding This Principle** — A plain-language explanation for anyone with a systems background, using real-world analogies (no protocol expertise required)
- **Key References** — The foundational RFCs and papers
- **IETF Conversations** — Real quotes from working group sessions where the principle was discussed, with context
- **Historical Analysis** — How discussion of this principle has evolved over four years and 14 IETF meetings
- **Resources** — Where to learn more

Whether you're a protocol designer, an engineering manager, or an executive trying to understand why Internet architecture matters for your business, this guide is for you.

## The Principles

The Internet's architecture rests on a set of design principles. Some are formal and documented in RFCs. Others are cultural norms that guide how the IETF community works. Here's what we found across 1,375 analyzed sessions:

| Principle | Sessions | Description |
|-----------|----------|-------------|
| [Principle of Constant Change](principles/constant_change.md) | 565 | The Internet must be designed to evolve; permanence is not the goal |
| [Fate Sharing](principles/fate_sharing.md) | 544 | State should be kept at endpoints that have a stake in it |
| [Layering](principles/layering.md) | 456 | Organize complexity through well-defined protocol layers |
| [Simplicity](principles/simplicity.md) | 418 | Prefer simple designs that can be understood, implemented, and debugged |
| [Rough Consensus and Running Code](principles/rough_consensus.md) | 331 | Progress through working implementations and approximate agreement |
| [Trust](principles/trust.md) | 252 | Trust is an architectural decision with cascading consequences |
| [Connectivity](principles/connectivity.md) | 165 | Universal connectivity is the Internet's primary goal |
| [Robustness / Postel's Law](principles/robustness.md) | 80 | Be conservative in what you send, liberal in what you accept |
| [Protocol Ossification](principles/ossification.md) | 71 | Protocols calcify when middleboxes depend on implementation details |
| [End-to-End Principle](principles/end_to_end.md) | 56 | Intelligence belongs at the endpoints, not in the network |
| [Tussle in Cyberspace](principles/tussle.md) | 50 | Design for ongoing conflict between stakeholders with different goals |
| [Principle of Least Surprise](principles/least_surprise.md) | 4 | Protocols should behave as users and implementers expect |

## About This Project

This analysis was produced as part of the **[IETF 125 Hackathon](https://www.ietf.org/meeting/125/)** (November 2025, Yokohama). It demonstrates how [vCons (virtualized conversations)](https://datatracker.ietf.org/doc/draft-ietf-vcon-vcon-container/) can be used not just to store conversation records, but to *analyze* them at scale and produce derived insights.

### The Technical Pipeline

1. **Source Data** — 2,249 vCons from the [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) repository, each representing a recorded IETF working group session with metadata and auto-generated transcripts.

2. **Keyword Detection** — Each vCon transcript was scanned for mentions of 12 network design principles using pattern matching against principle-specific vocabularies.

3. **Derived vCons** — For each session where principles were detected, an **appended vCon** was created following the [vCon core specification](https://datatracker.ietf.org/doc/draft-ietf-vcon-vcon-container/). These derived vCons reference the original via UUID and content hash, adding analysis metadata without modifying the source.

4. **Group vCons** — Per-principle **group vCons** aggregate all sessions discussing each principle, creating corpus-level views with collected evidence and statistics.

5. **Narrative Reports** — Claude was used to synthesize the evidence from each group vCon into the narrative reports you're reading now.

Every step of this pipeline produces spec-compliant vCons, demonstrating the format's utility for conversation analytics at scale.

### The vCon Format

A [vCon](https://datatracker.ietf.org/doc/draft-ietf-vcon-vcon-container/) is a standardized JSON container for conversation data — recordings, transcripts, metadata, and analysis. The IETF vCon working group is developing this as an Internet standard. This project showcases three types of derived vCons:

- **Appended** — Adds analysis to an existing conversation, referencing the original by UUID and cryptographic hash
- **Redacted** — Removes sensitive content while preserving analytical value
- **Group** — Aggregates multiple conversations by theme for corpus-level analysis

### Credits

- **Data**: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons)
- **Analysis**: IETF 125 Hackathon, vCon Working Group
- **Narrative Synthesis**: Generated with [Claude](https://anthropic.com/claude) from Anthropic
- **Platform**: [Conserver.io](https://conserver.io)

---

*This site is generated from vCon analysis. Source code and data are available in the [ietf-hackathon-125](https://github.com/vcon-dev/ietf-hackathon-125) repository.*
