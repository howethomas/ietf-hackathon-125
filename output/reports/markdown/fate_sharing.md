# Fate sharing

## Introduction

Fate sharing is a fundamental architectural principle of the Internet that dictates that related parts of a system should fail together, with critical state maintained only at endpoints rather than in intermediate network elements. This principle, formally articulated in [RFC 1958](https://www.rfc-editor.org/rfc/rfc1958), emerged from the early design philosophy of the DARPA Internet protocols and has profoundly shaped how we build resilient, scalable network systems.

The concept was first systematically described by David Clark in his seminal 1988 paper "[The Design Philosophy of the DARPA Internet Protocols](http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf)," where he explained that fate sharing addresses the fundamental challenge of building robust distributed systems. Rather than trying to protect shared state in the network from all possible failures, the Internet's design philosophy embraces the reality that failures will occur and ensures that when they do, the impact is predictable and recoverable. By keeping state at the endpoints and allowing related components to fail together, the network core remains simple and stateless, contributing to the Internet's remarkable scalability and resilience.

This principle continues to be highly relevant in contemporary Internet engineering, as evidenced by its frequent discussion across IETF working groups from 2021 to 2025. As new protocols and architectures emerge—from QUIC's connection management to distributed networking paradigms—engineers must carefully consider how fate sharing applies to ensure their designs maintain the Internet's core architectural strengths.

## Key References

- **[RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958)** — The foundational RFC that formally codifies fate sharing among other key Internet design principles.
- **[The Design Philosophy of the DARPA Internet Protocols](http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf)** — David Clark's influential 1988 paper that first articulated the theoretical foundation for fate sharing in Internet architecture.

## This Principle in IETF Discussions

The principle of fate sharing appears regularly in IETF working group discussions, often arising when engineers grapple with fundamental questions of where to place state and how to handle failures in distributed systems. These conversations reveal how the principle continues to guide protocol design decisions across diverse networking domains.

In the BABEL working group at IETF 110, participants discussed the challenges of packet fragmentation and its implications for fate sharing:

> "Fragmentation required packets are going to fail to reach the sending host and you're going to have mysterious failures where some things work and then get stuck. So the problem here is that you have no fate sharing between the data... between on the one hand the data path and on the other hand..."

This discussion highlights a classic fate sharing concern: when packet fragments are handled independently by the network, the fate of the overall communication becomes unpredictable. If some fragments succeed while others fail, the receiving endpoint cannot reconstruct the original message, leading to the "mysterious failures" the speaker describes.

The MOQ (Media Over QUIC) working group at IETF 115 provided another perspective on fate sharing, specifically in the context of media streaming:

> "Even though on extensible encoding they don't... you could break them into individual segments too. You can break it down as far as you want. In this case we've got a segment for an individual frame so it's not fate sharing with the other frames when it doesn't need to be and then finally you could just break..."

Here, the discussion centers on granular control over fate sharing in media delivery. The working group was exploring how to structure media data so that individual frames don't unnecessarily share fate with unrelated content, allowing for more efficient delivery and failure recovery in streaming scenarios.

The principle also surfaces in security contexts, as seen in the IPSECME working group discussion at IETF 119:

> "It's different, it's native as extension header so basic IPv6 header will just indicate that inside we have as extension header and everything else is hidden. It actually has some advantages... if ESP is stateless allow through your filtering then you don't need... you don't need any keep alives if..."

This conversation touches on how IPsec's stateless design (ESP) embodies fate sharing principles by avoiding the need for keep-alive mechanisms that would create shared state in the network infrastructure.

These examples demonstrate how fate sharing remains a living principle in Internet engineering—not merely a historical concept, but an active consideration that shapes how modern protocols handle state management, failure scenarios, and system boundaries.

## Historical Analysis

Analysis of IETF discussions from March 2021 through July 2025 reveals interesting patterns in how fate sharing is discussed across different working groups and time periods. The principle has been consistently relevant, appearing in 544 sessions across all 14 meetings in this timeframe.

| Meeting | Date | Sessions Discussing Fate Sharing |
|---------|------|--------------------------------|
| IETF 110 | March 2021 | 33 |
| IETF 111 | July 2021 | 31 |
| IETF 112 | November 2021 | 30 |
| IETF 113 | March 2022 | 41 |
| IETF 114 | July 2022 | 38 |
| IETF 115 | November 2022 | 51 |
| IETF 116 | March 2023 | 48 |
| IETF 117 | July 2023 | 40 |
| IETF 118 | November 2023 | 38 |
| IETF 119 | March 2024 | 32 |
| IETF 120 | July 2024 | 38 |
| IETF 121 | November 2024 | 30 |
| IETF 122 | March 2025 | 33 |
| IETF 123 | July 2025 | 61 |

The data shows several notable trends. Discussion peaked at IETF 115 (November 2022) with 51 sessions, followed by a sustained period of high activity through IETF 116 and 117. Interestingly, there's a dramatic spike at IETF 123 (July 2025) with 61 sessions—nearly double the typical meeting frequency—suggesting renewed focus on fate sharing principles, possibly driven by emerging technologies or architectural discussions.

The working groups most frequently discussing fate sharing provide insight into where this principle remains most relevant. The CORE working group (13 sessions) and DTN (Delay-Tolerant Networking, 13 sessions) lead the discussions, which makes sense given their focus on fundamental protocol mechanisms and challenged network environments where fate sharing considerations are critical. The presence of 6LO (IPv6 over Low-Power Wireless Personal Area Networks, 12 sessions) and DMM (Distributed Mobility Management, 12 sessions) in the top groups reflects the ongoing challenges of applying Internet principles to constrained and mobile environments.

The appearance of QUIC (11 sessions) and MASQUE (10 sessions) among the top discussing groups indicates that fate sharing remains highly relevant to modern transport and tunneling protocols. These newer protocol efforts must carefully consider how to maintain the Internet's architectural principles while addressing contemporary requirements for performance, security, and deployment flexibility.

The broad distribution across 141 unique working groups demonstrates that fate sharing is not confined to specific technical domains but remains a cross-cutting architectural concern that influences protocol design across the entire Internet standards landscape.

## Resources

**Foundational Documents:**
- **[RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958)** — Essential reading that formally codifies fate sharing alongside other core Internet design principles; provides the authoritative definition used throughout IETF work.
- **[The Design Philosophy of the DARPA Internet Protocols](http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf)** — David Clark's foundational 1988 paper that established the theoretical framework for Internet architecture including fate sharing; crucial for understanding the "why" behind the principle.

**Additional Learning Resources:**
- **[Fate-sharing (Wikipedia)](https://en.wikipedia.org/wiki/Fate-sharing)** — Accessible introduction to the concept with practical examples and links to related networking concepts; good starting point for those new to Internet architectural principles.

These resources provide a comprehensive foundation for understanding fate sharing from both theoretical and practical perspectives, enabling engineers to apply this principle effectively in their protocol design work.

---
*This report was generated from analysis of IETF working group session transcripts (vCon format) covering meetings 110-123 (March 2021 - July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `61316700-7ee6-41bc-b12f-a6f4f5707bbf` |
Sessions analyzed: 544 |
Generated: 2026-03-14*
