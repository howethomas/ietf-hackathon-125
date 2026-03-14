# Principle of Constant Change

## Introduction

The principle of constant change stands as one of the foundational tenets of Internet architecture, asserting that "the Internet must continue to evolve" and mandating that engineers "design for extensibility." First articulated in [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) by Brian Carpenter in 1996, this principle recognizes that the Internet is not a static system but a living, breathing network that must adapt to new requirements, technologies, and use cases over time. Unlike traditional telecommunications systems designed with fixed specifications, the Internet's architecture explicitly embraces change as both inevitable and desirable.

This principle has proven prescient in the decades since RFC 1958's publication. The Internet has successfully evolved from a research network connecting universities to the global communications backbone supporting everything from social media to autonomous vehicles, precisely because its protocols were designed with extensibility in mind. The principle manifests in everything from the layered architecture that allows new applications to run over existing transport protocols, to extension mechanisms in HTTP headers, to the modular design of routing protocols that can accommodate new algorithms and capabilities.

In IETF working groups today, this principle continues to guide protocol design decisions, ensuring that new standards can adapt to unforeseen future requirements while maintaining backward compatibility with existing deployments. The analysis of 565 working group sessions across IETF meetings 110-123 reveals how deeply embedded this principle remains in the IETF's engineering culture and decision-making processes.

## Key References

- [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — The seminal document establishing the fundamental design principles of Internet architecture, including the principle of constant change.
- [RFC 6709: Design Considerations for Protocol Extensions](https://www.rfc-editor.org/rfc/rfc6709) — Provides guidance on how to design protocols and protocol extensions that can evolve gracefully over time.

## This Principle in IETF Discussions

The principle of constant change emerges consistently across diverse working groups, reflecting its fundamental role in Internet protocol design. Analysis of recent IETF sessions reveals several key themes in how this principle guides contemporary protocol development.

**Designing for Future-Proofing and Extensibility**

In the MASQUE working group's March 2021 session, participants emphasized the importance of explicit extensibility mechanisms:

> "i think we need to use the settings um just how it is is i believe the correct way i think it's more for future proofing also to be very explicit that the h3 application is intending to do this"

This discussion centered on HTTP/3 settings mechanisms within the MASQUE protocol framework. The participants recognized that while a simpler approach might work for immediate needs, proper use of the settings framework would enable future extensions and make the protocol's intentions explicit to implementers and future protocol developers.

**Balancing Innovation with Backward Compatibility**

The MPLS working group demonstrated how extensibility can be achieved while preserving compatibility with existing deployments:

> "have a field of 16 bit which is reserved so this draft split that 16 bit reserve field into two different fields and the eight bit the first eight bit field is used as the algorithm field so this is backward compatible because uh you know if it is the default flex algo then the value will be zero"

This example illustrates a classic extensibility pattern: repurposing reserved fields to add new capabilities while ensuring that existing implementations continue to function correctly. The zero-default value ensures that legacy systems interpret the new field correctly without modification.

**Learning from Past Limitations**

The BESS working group's approach to a new protocol reflected lessons learned from legacy constraints:

> "we have focused on defining extensions that provide efficiency and extensibility and improve upon some of the legacy uh constraints we have you know seen in the past"

This comment reveals how the principle of constant change informs not just individual protocol decisions, but the broader evolution of Internet architecture. Working groups actively identify limitations in existing protocols and design new solutions with enhanced extensibility to avoid repeating past mistakes.

**Security and Extensibility Considerations**

The RTGWG working group highlighted how extensibility requirements intersect with other design constraints:

> "security is important but doing uh security or authentication at 3.3 milliseconds of uh for each packet is very expensive uh extensibility is uh very important and useful and we want to minimize the number of oem protocols"

This discussion illustrates the practical trade-offs involved in designing extensible systems. While extensibility is crucial, it must be balanced against performance requirements and deployment complexity, particularly in time-sensitive applications like routing protocols.

## Historical Analysis

The frequency of discussions about the principle of constant change across IETF meetings 110-123 shows remarkable consistency, indicating its enduring relevance to protocol design:

| Meeting | Date | Location | Discussion Frequency |
|---------|------|----------|---------------------|
| IETF 110 | March 2021 | Online | 48 |
| IETF 111 | July 2021 | Online | 31 |
| IETF 112 | November 2021 | Online | 42 |
| IETF 113 | March 2022 | Vienna | 40 |
| IETF 114 | July 2022 | Philadelphia | 35 |
| IETF 115 | November 2022 | London | 39 |
| IETF 116 | March 2023 | Yokohama | 48 |
| IETF 117 | July 2023 | San Francisco | 44 |
| IETF 118 | November 2023 | Prague | 36 |
| IETF 119 | March 2024 | Brisbane | 32 |
| IETF 120 | July 2024 | Vancouver | 43 |
| IETF 121 | November 2024 | Dublin | 45 |
| IETF 122 | March 2025 | Bangkok | 39 |
| IETF 123 | July 2025 | Madrid | 43 |

Several notable patterns emerge from this data. The highest discussion frequencies occurred during IETF 110 and 116 (both with 48 instances), suggesting periods of particularly active protocol development where extensibility concerns were paramount. The transition from online meetings (IETF 110-112) to hybrid and in-person formats didn't significantly impact the frequency of these discussions, indicating that extensibility concerns are fundamental to protocol work regardless of meeting format.

The working groups most frequently discussing this principle—**netmod** (12), **iabopen** (11), **lsr** (11), **masque** (11), and **quic** (11)—represent diverse areas of Internet technology. The netmod and netconf working groups' prominence reflects the critical importance of extensibility in network management protocols, which must adapt to diverse and evolving network environments. The strong showing by masque and quic working groups indicates how newer application-layer protocols continue to grapple with extensibility challenges, particularly as they seek to enable new use cases while maintaining interoperability.

The IAB's frequent discussion of this principle (iabopen with 11 instances) reflects the architectural oversight body's role in ensuring that protocol development across working groups adheres to fundamental Internet design principles. With 149 unique working groups discussing extensibility across this period, the principle's influence spans virtually the entire spectrum of Internet protocol development.

## Resources

- **[RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958)** — Essential reading for understanding the foundational principles that guide Internet architecture, including detailed discussion of why constant change and extensibility are crucial for the Internet's continued success.

- **[RFC 6709: Design Considerations for Protocol Extensions](https://www.rfc-editor.org/rfc/rfc6709)** — Provides practical engineering guidance on implementing extensibility in protocols, including common patterns, security considerations, and lessons learned from successful and failed extension mechanisms.

- **[Protocol Extensibility (Wikipedia)](https://en.wikipedia.org/wiki/Extensibility)** — Offers broader context on extensibility as a software and systems design principle, with examples from both Internet protocols and other computing systems.

- **[RFC 5218: What Makes for a Successful Protocol?](https://www.rfc-editor.org/rfc/rfc5218)** — Analyzes factors contributing to protocol success and failure, with extensibility identified as a key factor in protocols' ability to adapt to changing requirements over time.

- **[Internet Architecture Evolution](https://www.iab.org/activities/evolution/)** — The Internet Architecture Board's ongoing work on understanding and guiding the evolution of Internet architecture, including contemporary challenges to the principle of constant change.

---
*This report was generated from analysis of vCon (virtual Conversation) data spanning IETF meetings 110-123 (March 2021 - July 2025), encompassing 565 working group sessions across 149 working groups.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `ca07c18a-c675-46f1-afce-251143c309e8` |
Sessions analyzed: 565 |
Generated: 2026-03-14*
