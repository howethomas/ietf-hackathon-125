# Robustness principle / Postel's law

## Introduction

The Robustness principle, known throughout the Internet engineering community as "Postel's law," stands as one of the most influential yet controversial design principles in network architecture. Formulated by Jon Postel in 1980 and codified in [RFC 761](https://www.rfc-editor.org/rfc/rfc761), the principle states simply: "Be conservative in what you send, be liberal in what you accept." This deceptively straightforward maxim has shaped decades of Internet protocol design and implementation, from the foundational TCP/IP stack documented in [RFC 1122](https://www.rfc-editor.org/rfc/rfc1122) to modern web protocols.

Named after Jon Postel, one of the principal architects of the Internet and longtime editor of the RFC series, this principle emerged from the pragmatic needs of early Internet development. In an era when different computer systems had varying implementations and interpretations of protocols, being tolerant of minor deviations while maintaining strict standards for one's own output enabled interoperability across a heterogeneous network. The principle became so fundamental that it influenced not just technical specifications but the entire culture of Internet engineering.

However, as networks have evolved and security concerns have intensified, the principle has faced increasing scrutiny. [RFC 9413](https://www.rfc-editor.org/rfc/rfc9413), published in 2023, reflects the IETF's ongoing examination of when robustness helps versus when it can inadvertently harm protocol evolution and security. This tension between flexibility and precision continues to generate active debate in IETF working groups, making it one of the most discussed principles in contemporary Internet architecture discussions.

## Understanding This Principle

**The Core Idea**

Be conservative in what you send, be liberal in what you accept. Think of this like being a gracious dinner host while also being a considerate guest. When you're hosting (sending data), you follow proper etiquette meticulously—you use the right silverware, serve courses in the correct order, and ensure everything meets the highest standards. But when you're a guest at someone else's table (receiving data), you're understanding and flexible—if they serve salad after the main course or use a dessert fork for the appetizer, you don't make a scene or refuse to participate. You work with what you're given while maintaining your own high standards.

This analogy captures why the principle exists: it enables cooperation across diverse environments while preventing a race to the bottom. Just as dinner parties would become impossible if everyone insisted that others follow their exact customs while being sloppy about their own hosting, computer networks would fragment if every system demanded perfect compliance from others while being careless about its own outputs. The asymmetry is crucial—strict about yourself, tolerant of others—because it creates a stable foundation for interaction even when participants have different capabilities or interpretations.

**Why It Matters**

When this principle is followed correctly, networks become resilient and interoperable. Consider email: your email client might send perfectly formatted messages, but it can usually read emails from older systems that have slightly malformed headers or unusual character encodings. This tolerance means you don't lose important communications just because someone is using outdated software. The principle prevents network fragmentation—the nightmare scenario where systems can only talk to identical systems, creating isolated islands instead of a unified network.

But when violated, the consequences cascade quickly. Imagine if web browsers were strict about HTML compliance—millions of websites with minor markup errors would suddenly become unreadable. Conversely, if browsers generated sloppy HTML while remaining tolerant of others' mistakes, the web would devolve into a chaotic mix of incompatible formats. The principle's genius is in breaking this symmetry: everyone produces high-quality output (preventing degradation) while accepting imperfect input (ensuring connectivity).

**The Tension**

The real-world pressure working against this principle is simple: being liberal in what you accept is hard and expensive. It means writing more code, handling edge cases, testing against malformed inputs, and maintaining compatibility with legacy systems. There's a constant temptation to say "that's not my problem" and reject anything that doesn't perfectly match your expectations. Additionally, security concerns have intensified this pressure—being too liberal can mean accepting malicious inputs that exploit your tolerance.

Organizations face this tension daily. Product teams want to move fast and drop support for old versions. Engineers prefer clean interfaces over messy compatibility layers. Business leaders don't want to spend resources supporting competitors' legacy formats. The principle demands that you absorb the complexity of an imperfect world rather than pushing it back onto others—a choice that feels like taking on everyone else's technical debt.

**How to Recognize It**

You're seeing this principle at work when your smartphone can read documents created in old versions of Microsoft Word, even though Microsoft has changed the format multiple times. The phone's software is conservative (generates clean, standard files) but liberal (reads messy legacy formats).

You see it in API design when a service accepts requests with extra fields it doesn't understand rather than rejecting them, while ensuring its own requests contain only necessary, well-structured data. This allows clients to evolve independently without breaking integration.

You recognize it in organizational design when a team has high standards for their own deliverables but works constructively with inputs from other teams that don't quite match their preferred format, rather than constantly sending work back for reformatting. This prevents bureaucratic gridlock while maintaining quality standards.

## Key References

- [RFC 761: Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc761) — The original formulation of Postel's law in the context of TCP specification.
- [RFC 1122: Requirements for Internet Hosts](https://www.rfc-editor.org/rfc/rfc1122) — Codifies the robustness principle as a fundamental requirement for Internet host implementations.
- [RFC 9413: Maintaining Robust Protocols](https://www.rfc-editor.org/rfc/rfc9413) — A modern examination of when robustness helps versus harms protocol evolution and security.

## This Principle in IETF Discussions

The robustness principle continues to surface regularly in IETF working group discussions, often at moments when implementers must decide how strict to be about protocol compliance. These conversations reveal the ongoing tension between maintaining interoperability and ensuring protocol integrity.

In the EMU (EAP Method Update) working group during IETF 110, participants grappled with session ticket requirements:

> "something along the lines of should uh issue one session ticket or and and not going with must might make sense i don't know what's your opinion on that um sure i mean you know in the principle of um be conservative in what you send and and liberal in what you expect um it really is a hard question to"

This exchange illustrates the principle's direct application to specification language—the classic tension between "MUST" (strict) and "SHOULD" (flexible) requirements. The working group was trying to balance ensuring consistent behavior while allowing implementation flexibility.

The 6MAN (IPv6 Maintenance) working group demonstrated how the principle applies to packet processing during IETF 111:

> "processing that we just saw is probably a subset of this this um draft more addresses the the larger problem with hopi hop options uh this is just a little bit of background so we do want to apply the robustness principle to limits so when we sign be conservative deliver on what you receive but i thi"

Here, the discussion centered on IPv6 hop-by-hop options processing—a notoriously problematic area where different implementations handle malformed or unexpected options differently. The working group was explicitly invoking Postel's law to guide their specification decisions.

The DTN (Delay-Tolerant Networking) working group, which shows up most frequently in these discussions, often deals with extreme networking conditions where robustness becomes critical. During IETF 120, they discussed algorithm interoperability:

> "editorial changes uh in the last revision of the document uh we added um minimum interoperability for a few different algorithms that were just missing this doesn't change the behavior but it just restricts uh at the very least you have to support these specific kind of algorithms and allows uh sing"

This reflects a nuanced application of the principle—being conservative by requiring minimum algorithm support while being liberal by allowing additional algorithms beyond the baseline.

The EDM working group during IETF 114 highlighted how the principle's definition itself has become a subject of debate:

> "nd we decided oh well let's let's chat in person things always work out better when we're face to face uh even if virtually so what i was thinking is um maybe starting with like the definition of the robustness principle that we chose to use in this document because it became clear that those words"

This meta-discussion reveals an important evolution: the IETF is now questioning not just how to apply Postel's law, but what it means in different contexts. This reflects the broader industry conversation captured in RFC 9413 about when robustness helps versus when it can harm security and protocol evolution.

## Historical Analysis

Analysis of discussion frequency across IETF meetings 110-123 reveals interesting patterns in how the community engages with this principle:

| Meeting | Date | Location | Frequency |
|---------|------|-----------|-----------|
| IETF 110 | March 2021 | Online | 9 |
| IETF 111 | July 2021 | Online | 4 |
| IETF 112 | November 2021 | Online | 5 |
| IETF 113 | March 2022 | Vienna | 2 |
| IETF 114 | July 2022 | Philadelphia | 6 |
| IETF 115 | November 2022 | London | 3 |
| IETF 116 | March 2023 | Yokohama | 7 |
| IETF 117 | July 2023 | San Francisco | 7 |
| IETF 118 | November 2023 | Prague | 8 |
| IETF 119 | March 2024 | Brisbane | 3 |
| IETF 120 | July 2024 | Vancouver | 7 |
| IETF 121 | November 2024 | Dublin | 7 |
| IETF 122 | March 2025 | Bangkok | 7 |
| IETF 123 | July 2025 | Madrid | 5 |

The data shows elevated discussion during the early online meetings (especially IETF 110), which may reflect the community's heightened focus on interoperability challenges during the pandemic-era shift to virtual collaboration. The relatively lower discussion frequency during the first in-person meeting (IETF 113 in Vienna) suggests that some of these conversations may have moved to hallway discussions.

The DTN working group's dominance (12 discussions) makes sense given their focus on networks operating under extreme conditions where robustness is paramount. The Human Rights Protocol Considerations (HRPC) working group's presence (4 discussions) reflects growing interest in how technical design principles affect Internet accessibility and inclusivity. The broad distribution across 56 working groups—from ACME (automated certificate management) to TVR (time-variant routing)—demonstrates that robustness considerations permeate virtually every area of Internet protocol design.

The sustained discussion frequency in recent meetings (7+ discussions in most meetings from 2023-2025) coincides with the publication of RFC 9413 and suggests the community is actively re-evaluating this foundational principle rather than simply accepting it as dogma.

## Resources

- [RFC 9413: Maintaining Robust Protocols](https://www.rfc-editor.org/rfc/rfc9413) — Essential reading for understanding the modern critique of Postel's law and when robustness can harm protocol evolution.
- [Robustness Principle (Wikipedia)](https://en.wikipedia.org/wiki/Robustness_principle) — Provides historical context and examples of the principle's application across different Internet protocols.
- [The Harmful Consequences of Postel's Maxim](https://datatracker.ietf.org/doc/html/draft-iab-protocol-maintenance) — The IAB's analysis of when liberal acceptance can undermine protocol maintenance and security.
- [RFC 1122: Requirements for Internet Hosts](https://www.rfc-editor.org/rfc/rfc1122) — Shows how the principle was systematically applied to TCP/IP implementation requirements.
- [DoD Standard Internet Protocol](https://www.rfc-editor.org/rfc/rfc760) — Jon Postel's original work that established the philosophical foundation for robust Internet protocols.

---
*This report was generated from analysis of IETF working group session transcripts using vCon (Virtualized Conversation) data processing.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `439ba615-90d3-4236-b5bb-adc5180162a6` |
Sessions analyzed: 80 |
Generated: 2026-03-14*
