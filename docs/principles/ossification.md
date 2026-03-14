# Protocol ossification

## Introduction

Protocol ossification is one of the most insidious threats to Internet evolution — the tendency for network protocols to become rigid and unchangeable over time, not by design but by accident. This phenomenon occurs when middleboxes, firewalls, and other network equipment begin to expect and enforce specific protocol behaviors, making it nearly impossible to modify or extend those protocols later, even when the changes would be beneficial.

The principle emerged from hard-learned lessons across decades of Internet evolution, most notably documented in [RFC 9170: Long-Term Viability of Protocol Extension Mechanisms](https://www.rfc-editor.org/rfc/rfc9170) by Martin Thomson in 2022. This work crystallized observations from protocol designers who watched promising extensions fail not due to technical flaws, but because the network infrastructure had calcified around existing behaviors. The TCP protocol's struggles with new features, and more recently the challenges faced during HTTP/2 deployment, provided stark examples of how ossification constrains innovation.

In IETF discussions from 2021 through 2025, ossification has become a central concern influencing the design of new protocols and the evolution of existing ones. The principle has driven the adoption of techniques like GREASE (Generate Random Extensions And Sustain Extensibility) and shaped architectural decisions across working groups from QUIC to TLS to emerging protocols in IoT and edge computing.

## Understanding This Principle

**The Core Idea** — Protocols become unchangeable when the network assumes they'll never change. Think of this like a city's informal walking paths: the first few people who walk across a park create barely visible traces in the grass, but once enough people follow those same routes, the paths become worn dirt tracks that channel all future foot traffic, making it nearly impossible to create new routes even when they'd be more efficient.

**Why It Matters** — When protocols ossify, innovation grinds to a halt in subtle but devastating ways. Consider the story of TCP, the fundamental protocol that carries most Internet traffic. Over decades, network operators deployed middleboxes that made assumptions about how TCP packets should look and behave. These devices began blocking or "correcting" any TCP traffic that didn't match their expectations, even when that traffic represented legitimate protocol improvements. The result? New TCP features that would benefit everyone — better congestion control, improved security, enhanced performance — simply couldn't be deployed because the network infrastructure would reject them.

Contrast this with protocols designed with anti-ossification measures from the start. QUIC, the transport protocol underlying HTTP/3, was built with the explicit goal of preventing ossification. It encrypts almost all header fields, making them opaque to middleboxes, and includes mechanisms to regularly exercise extension points. The result is a protocol that can evolve rapidly — QUIC has seen multiple versions deployed successfully, something that would be nearly impossible with an ossified protocol like TCP.

**The Tension** — The pressure toward ossification comes from a fundamental mismatch between how protocols are designed and how networks operate. Protocol designers create extension points and optional features assuming they'll be used later. But network operators deploy equipment that needs to make real-time decisions about traffic, often under pressure to block anything that looks unusual or potentially malicious. Every middlebox vendor faces the same choice: should their device allow unknown protocol variations (risking security vulnerabilities) or block them (ensuring safety but contributing to ossification)? The economic incentives overwhelmingly favor the conservative choice.

This creates a vicious cycle. When extension points go unused for extended periods, network equipment learns to expect their absence. The longer an extension point remains dormant, the more likely it is that some middlebox somewhere has started blocking its use. Protocol designers call this "use it or lose it" — extension points that aren't regularly exercised become unusable.

**How to Recognize It** — You're seeing ossification at work when new protocol features fail to deploy despite clear technical benefits, when "obviously good" improvements to existing systems are rejected by network infrastructure, or when protocol designers spend significant effort making new features look exactly like old ones to slip past network monitoring. In broader technical contexts, you see similar patterns when APIs become impossible to evolve because too many clients make undocumented assumptions, when file formats can't be extended because parsers expect exact structures, or when organizational processes become unchangeable because too many stakeholders have built rigid workflows around current procedures.

## Key References

- [RFC 9170: Long-Term Viability of Protocol Extension Mechanisms](https://www.rfc-editor.org/rfc/rfc9170) — Martin Thomson's comprehensive analysis of protocol ossification and strategies for maintaining evolvability
- [RFC 8701: GREASE](https://www.rfc-editor.org/rfc/rfc8701) — The "Generate Random Extensions And Sustain Extensibility" mechanism for preventing ossification
- [RFC 9000: QUIC](https://www.rfc-editor.org/rfc/rfc9000) — A transport protocol designed from the ground up with anti-ossification principles

## This Principle in IETF Discussions

The concept of protocol ossification has been a consistent thread throughout IETF discussions, with Martin Thomson's foundational work serving as a catalyst for broader awareness. In the IAB Open session at IETF 110 (March 2021), participants discussed the evolution program's focus on Thomson's "use it or lose it" draft, recognizing it as a critical work item for the Internet's future:

> "the one that we're currently talking most about is actually one that existed prior to this program being created but we think is a very important work item that we want to progress that martin thompson began it's the draft use it or lose it"

This work continued to gain prominence through IETF 111, where the IAB identified the document as "probably the next one we will look at in evolution," highlighting its importance to the broader Internet architecture community.

The practical impact of ossification concerns became evident in protocol-specific discussions. During the TLS working group session at IETF 111, participants grappled with design decisions specifically aimed at preventing ossification:

> "it's not entirely accurate which of these would prevent exactly what i think they all prevent ossification somewhat but like maybe some of the windfall streaming"

The QUIC working group's approach to ossification prevention through GREASE mechanisms was particularly notable. At IETF 113, the group was progressing their GREASE document, which implements the "use it or lose it" principle by ensuring extension points are regularly exercised:

> "the grease bit document uh is dura shepherd write-up from me um so that's on me and that'll be coming soon"

Perhaps most telling was a candid discussion in the PANRG session at IETF 113, where a participant explained the fundamental problem with middleboxes and their role in protocol ossification:

> "people hate them they try to help out in tcp and in fact you know because well they sometimes do something useful right they have good intentions well intended but but you know terrible outcomes of ossification of playing tricks to tcp that they have to do"

By IETF 116, the EDM working group was making ossification a central theme of their evolvability work:

> "mainly been focused around a couple documents that Martin had actually started previously we had our uh use it or lose it uh draft uh that talked about the importance of active use"

The influence of anti-ossification thinking even reached individual protocol designs. At IETF 116, the MLS working group incorporated GREASE mechanisms based on architectural guidance:

> "our distinguished colleague David scanzi of the architecture board came around and suggested we add grease"

## Historical Analysis

The discussion frequency data reveals interesting patterns in how ossification concerns have evolved across the IETF community:

| Meeting | Sessions | Context |
|---------|----------|---------|
| IETF 110 | 7 | Initial "use it or lose it" momentum |
| IETF 113 | 8 | Peak discussion during Vienna meeting |
| IETF 116 | 8 | Focus on practical implementation |
| IETF 119 | 1 | Minimum discussion |
| IETF 121 | 8 | Renewed focus in Dublin |

The highest concentration of discussions occurred during the transition period from 2021-2023, coinciding with the maturation of RFC 9170 and its integration into active protocol development. The QUIC working group led these discussions with 7 sessions, reflecting their pioneering role in implementing anti-ossification measures. The TLS and EDM working groups followed closely, indicating that ossification concerns span both established protocols seeking evolution and new architectural thinking.

Notably, discussion frequency dropped significantly during 2024 (IETF 119-120), possibly indicating that anti-ossification techniques had become more standardized and routine rather than requiring active debate. The spike at IETF 121 suggests ongoing refinement of these approaches as new protocols encounter real-world deployment challenges.

The breadth of working groups involved — 36 in total — demonstrates that ossification has become a cross-cutting concern rather than a niche architectural topic, influencing everything from core transport protocols to application-layer designs.

## Resources

- **[RFC 9170: Long-Term Viability of Protocol Extension Mechanisms](https://www.rfc-editor.org/rfc/rfc9170)** — Essential reading for understanding the theoretical foundations and practical strategies for preventing protocol ossification
- **[RFC 8701: GREASE](https://www.rfc-editor.org/rfc/rfc8701)** — Detailed specification of the GREASE technique, showing how "use it or lose it" principles translate into concrete protocol mechanisms
- **[Path MTU Discovery (RFC 1191)](https://www.rfc-editor.org/rfc/rfc1191)** — A classic example of a useful protocol feature that suffered from ossification due to middlebox interference
- **[QUIC Loss Detection and Congestion Control (RFC 9002)](https://www.rfc-editor.org/rfc/rfc9002)** — Demonstrates how modern protocols can be designed to remain evolvable while providing concrete functionality
- **[Internet-Draft: Architectural Considerations for Transport Evolution](https://datatracker.ietf.org/doc/draft-iab-path-signals-collaboration/)** — Ongoing IAB work examining how transport protocols can collaborate with network elements without creating ossification

---
*This report was generated from analysis of IETF working group session transcripts using vCon (virtual Conversation) data covering meetings 110-123 (March 2021 - July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `c93a4657-0f71-49f0-b5f2-870455334d73` |
Sessions analyzed: 71 |
Generated: 2026-03-14*
