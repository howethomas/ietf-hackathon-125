# Robustness principle / Postel's law

## Introduction

The Robustness Principle, commonly known as Postel's Law after its originator Jon Postel, stands as one of the most influential and simultaneously controversial design principles in Internet architecture. Simply stated as "Be conservative in what you send, be liberal in what you accept," this principle has guided protocol designers for over four decades, shaping how network systems handle interoperability, error recovery, and protocol evolution. First articulated in [RFC 761](https://www.rfc-editor.org/rfc/rfc761) in 1980 and later codified in the Internet Host Requirements specification [RFC 1122](https://www.rfc-editor.org/rfc/rfc1122), Postel's Law emerged from the practical need to build robust systems that could function reliably across diverse implementations and network conditions.

However, as Internet protocols have matured and security concerns have intensified, the principle has faced increasing scrutiny. The "liberal acceptance" aspect, while promoting interoperability, has been identified as a potential source of security vulnerabilities and implementation inconsistencies. This tension has led to significant debate within the IETF community, culminating in [RFC 9413](https://www.rfc-editor.org/rfc/rfc9413), which provides updated guidance on maintaining robust protocols while addressing the principle's potential drawbacks.

The ongoing relevance of Postel's Law in contemporary protocol design reflects the fundamental challenge of balancing interoperability, security, and evolution in distributed systems. As evidenced by its frequent discussion across IETF working groups, the principle continues to inform critical decisions about protocol behavior, error handling, and implementation requirements in modern Internet infrastructure.

## Key References

- **[RFC 761](https://www.rfc-editor.org/rfc/rfc761)** - DoD Standard Transmission Control Protocol: The original specification where Postel first articulated the robustness principle in 1980.
- **[RFC 1122](https://www.rfc-editor.org/rfc/rfc1122)** - Requirements for Internet Hosts: Formalized the principle as a fundamental requirement for Internet host implementations.
- **[RFC 9413](https://www.rfc-editor.org/rfc/rfc9413)** - Maintaining Robust Protocols: Modern guidance addressing both the benefits and potential harms of the robustness principle in contemporary protocol design.

## This Principle in IETF Discussions

The robustness principle continues to surface regularly in IETF working group discussions, often at critical decision points where implementers must balance strict compliance with pragmatic interoperability. These conversations reveal both the enduring value and evolving interpretation of Postel's Law across diverse protocol domains.

In the EMU (EAP Method Update) working group during IETF 110, participants grappled with the classic tension between prescriptive requirements and flexible implementation guidance:

> "Something along the lines of should uh issue one session ticket or and and not going with must might make sense i don't know what's your opinion on that um sure i mean you know in the principle of um be conservative in what you send and and liberal in what you expect um it really is a hard question to..."

This exchange illustrates how protocol designers invoke Postel's Law when determining whether to use normative language (MUST) versus more permissive guidance (SHOULD), particularly in security-sensitive contexts where session management is critical.

The 6MAN (IPv6 Maintenance) working group at IETF 111 demonstrated how the principle applies to specific technical challenges, particularly in handling IPv6 hop-by-hop options:

> "Processing that we just saw is probably a subset of this this um draft more addresses the the larger problem with hop-by-hop options uh this is just a little bit of background so we do want to apply the robustness principle to limits so when we sign be conservative deliver on what you receive but I think..."

This discussion highlights how working groups explicitly invoke the robustness principle when designing packet processing behaviors, especially for optional protocol elements that may be implemented inconsistently across the network.

Perhaps most significantly, the EDM (Endpoints and Data Management) working group at IETF 114 engaged in fundamental definitional work around the principle itself:

> "And we decided oh well let's let's chat in person things always work out better when we're face to face uh even if virtually so what i was thinking is um maybe starting with like the definition of the robustness principle that we chose to use in this document because it became clear that those words..."

This meta-discussion reveals the IETF's growing recognition that the principle itself requires careful definition and context-specific application, rather than blanket adoption across all protocol scenarios.

The DTN (Delay-Tolerant Networking) working group's frequent engagement with robustness principles reflects the unique challenges of networks with intermittent connectivity, where liberal acceptance policies may be essential for maintaining communication in adverse conditions. Their discussions often center on custody transfer mechanisms and asymmetric acknowledgment scenarios where strict protocol adherence might actually harm network functionality.

## Historical Analysis

Analysis of discussion frequency across IETF meetings 110-123 reveals interesting patterns in how the robustness principle has been addressed within the community:

| Meeting | Date | Location | Frequency |
|---------|------|----------|-----------|
| IETF 110 | Mar 2021 | Online | 9 |
| IETF 111 | Jul 2021 | Online | 4 |
| IETF 112 | Nov 2021 | Online | 5 |
| IETF 113 | Mar 2022 | Vienna | 2 |
| IETF 114 | Jul 2022 | Philadelphia | 6 |
| IETF 115 | Nov 2022 | London | 3 |
| IETF 116 | Mar 2023 | Yokohama | 7 |
| IETF 117 | Jul 2023 | San Francisco | 7 |
| IETF 118 | Nov 2023 | Prague | 8 |
| IETF 119 | Mar 2024 | Brisbane | 3 |
| IETF 120 | Jul 2024 | Vancouver | 7 |
| IETF 121 | Nov 2024 | Dublin | 7 |
| IETF 122 | Mar 2025 | Bangkok | 7 |
| IETF 123 | Jul 2025 | Madrid | 5 |

The data shows peak discussion during the early pandemic period (IETF 110), possibly reflecting increased focus on protocol resilience as networks faced unprecedented stress. The relatively low frequency during IETF 113 and 119 suggests that certain meeting cycles may have focused more on implementation details rather than fundamental design principles.

The DTN working group's dominance in these discussions (12 occurrences) is particularly noteworthy, as delay-tolerant networking inherently requires robust handling of network disruptions and inconsistent implementations. The HRPC (Human Rights Protocol Considerations) working group's involvement highlights how robustness principles intersect with broader concerns about network accessibility and reliability.

The distribution across 56 unique working groups demonstrates the principle's cross-cutting relevance, appearing in contexts ranging from low-level protocol mechanics (6MAN, SIDROPS) to application-layer specifications (HTTPAPI, ACME). This breadth suggests that Postel's Law remains a fundamental consideration across the entire Internet protocol stack.

The sustained discussion frequency in later meetings (2024-2025) indicates that the principle's relevance has not diminished, despite ongoing debates about its appropriate application. This persistence likely reflects the continued evolution of the Internet toward more diverse deployment environments, where implementation variations and network conditions require careful consideration of robustness versus security trade-offs.

## Resources

**Core Specifications:**
- **[RFC 9413: Maintaining Robust Protocols](https://www.rfc-editor.org/rfc/rfc9413)** - Essential reading that provides modern guidance on applying robustness principles while avoiding common pitfalls, particularly relevant for contemporary protocol designers balancing security and interoperability concerns.
- **[RFC 1122: Requirements for Internet Hosts](https://www.rfc-editor.org/rfc/rfc1122)** - The foundational document that established the robustness principle as a formal requirement for Internet implementations, containing detailed examples of how the principle applies across transport and network layers.

**Historical Context:**
- **[Robustness Principle (Wikipedia)](https://en.wikipedia.org/wiki/Robustness_principle)** - Comprehensive overview covering both the principle's origins and its evolution, including discussions of criticism and alternative approaches that have emerged in recent years.

**Critical Analysis:**
- **[The Harmful Consequences of Postel's Maxim (draft-iab-protocol-maintenance)](https://datatracker.ietf.org/doc/html/draft-iab-protocol-maintenance)** - Important counterpoint that examines potential negative effects of liberal acceptance policies, particularly valuable for understanding why modern protocol design has moved toward more conservative approaches in security-critical contexts.

---
*This report was generated from analysis of IETF working group session transcripts using vCon data analysis techniques.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `439ba615-90d3-4236-b5bb-adc5180162a6` |
Sessions analyzed: 80 |
Generated: 2026-03-14*
