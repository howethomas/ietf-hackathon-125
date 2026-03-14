# End-to-end principle

## Introduction

The end-to-end principle stands as one of the foundational architectural principles of the Internet, articulating that network intelligence should reside at the endpoints rather than within the network infrastructure itself. First formally articulated by J.H. Saltzer, D.P. Reed, and D.D. Clark in their seminal 1984 paper ["End-to-End Arguments in System Design"](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf), this principle argues that functions can only be correctly and completely implemented at the application layer, where the communicating endpoints have full knowledge of their requirements and constraints.

This principle has profoundly shaped Internet architecture and protocol design, establishing a philosophy that keeps the network core simple and "dumb" while pushing complexity to the edges where applications and users reside. The IETF has formally recognized this principle in [RFC 1958](https://www.rfc-editor.org/rfc/rfc1958) as a core architectural principle of the Internet, and later examined its evolution in [RFC 3724](https://www.rfc-editor.org/rfc/rfc3724), which explores how the rise of middleboxes and network intermediaries has challenged traditional end-to-end assumptions.

The principle's enduring relevance to Internet engineering is evident in its continued discussion across IETF working groups, where it serves both as a design guideline for new protocols and as a lens for evaluating how the Internet's architecture continues to evolve in response to changing requirements, business models, and technological capabilities.

## Key References

- **[RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958)** — Establishes the end-to-end principle as a fundamental architectural principle of the Internet.
- **[RFC 3724: The Rise of the Middle and the Future of End-to-End](https://www.rfc-editor.org/rfc/rfc3724)** — Examines how middleboxes and network intermediaries challenge traditional end-to-end assumptions.
- **[End-to-End Arguments in System Design](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf)** — The original 1984 paper by Saltzer, Reed, and Clark that introduced the principle.

## This Principle in IETF Discussions

The end-to-end principle continues to be actively discussed across IETF working groups, often in the context of how modern Internet realities challenge traditional architectural assumptions. These discussions reveal both the principle's enduring relevance and the ongoing tension between ideal architectural principles and practical network evolution.

In the DINRG (Decentralized Internet Infrastructure Research Group), participants frequently grapple with how the principle applies to today's Internet landscape. At IETF 115 in London, one speaker observed a fundamental shift in Internet topology:

> "drives the user base up and that builds the economy of scale in today's internet the result is really a flattening of the traditional topology of the internet what we've got is a situation where the end-to-end principle isn't really the principle that's at work here"

This observation reflects a broader concern within the research community about how content delivery networks, cloud services, and platform consolidation have altered the Internet's original end-to-end architecture. The speaker suggests that economic forces and scale effects have created a reality where traffic increasingly flows through intermediary platforms rather than directly between endpoints.

The evolution of Internet principles was further discussed at IETF 116 in Yokohama, where DINRG participants acknowledged that long-held assumptions about Internet architecture are being challenged:

> "to be honest and so in terms of the recent evolution of the internet what we see is that principles that were true 20 years ago no longer hold true now for instance we'll talk a little later about the end-to-end principle"

This frank assessment highlights the ongoing tension between maintaining architectural principles and adapting to technological and economic realities that weren't anticipated when these principles were first articulated.

Interestingly, the principle also appears in discussions of newer technologies where its application remains valid. In the SECDISPATCH working group at IETF 117, participants discussed how VPN tunnels can coexist with end-to-end principles:

> "this works this is not considered a violation of the end-to-end principle right like packets are still flowing end to end there's a tunnel in the middle"

This discussion demonstrates how the principle continues to provide guidance for evaluating new security architectures, helping engineers distinguish between mechanisms that preserve end-to-end communication (like tunneling) and those that fundamentally alter it.

The SATP working group at IETF 116 even applied end-to-end thinking to blockchain and distributed ledger contexts, showing the principle's broader applicability:

> "literally what that means and this is the analog to the end-to-end principles principle for those who are on the din mailing list"

This cross-pollination of ideas demonstrates how fundamental Internet principles continue to inform thinking in adjacent technical domains.

At IETF 120, DINRG participants called for renewed focus on end users and existing principles when considering future Internet architecture:

> "we wouldn't be starting from scratch um if we did that because there are existing principles including the end to end principle um and rfc's looking at how that's being how it's evolving"

This suggests recognition that while the Internet has evolved significantly, foundational principles like end-to-end design remain valuable starting points for addressing contemporary challenges.

## Historical Analysis

Analysis of IETF discussions from meetings 110-123 (March 2021 to July 2025) reveals interesting patterns in how the end-to-end principle has been discussed across this period. The principle was discussed in 56 sessions across 36 different working groups, demonstrating its broad relevance across IETF work.

| Meeting | Date/Location | Discussion Count |
|---------|---------------|-----------------|
| IETF 110 | March 2021 (Online) | 5 |
| IETF 111 | July 2021 (Online) | 6 |
| IETF 113 | March 2022 (Vienna) | 5 |
| IETF 114 | July 2022 (Philadelphia) | 6 |
| IETF 115 | November 2022 (London) | 7 |
| IETF 116 | March 2023 (Yokohama) | 2 |
| IETF 117 | July 2023 (San Francisco) | 6 |
| IETF 118 | November 2023 (Prague) | 7 |
| IETF 119 | March 2024 (Brisbane) | 3 |
| IETF 120 | July 2024 (Vancouver) | 1 |
| IETF 121 | November 2024 (Dublin) | 1 |
| IETF 122 | March 2025 (Bangkok) | 3 |
| IETF 123 | July 2025 (Madrid) | 4 |

The data shows peak discussion periods in 2022-2023, particularly at IETF 115 and 118, both with seven sessions discussing the principle. This period coincides with increased focus on Internet architecture research and concerns about platform concentration and content delivery evolution.

The most active working groups provide insights into where end-to-end principles are most relevant today. DINRG leads with seven discussions, reflecting the research community's focus on how decentralization and traditional Internet principles interact. DTN (Delay-Tolerant Networking) and NMRG (Network Management Research Group) each had four discussions, suggesting that end-to-end principles remain particularly relevant in challenging networking environments and management contexts.

Notably, discussions appear to decline in 2024-2025, with significantly fewer sessions addressing the principle. This could indicate either that the principle has become well-understood and implicit in discussions, or that attention has shifted to other architectural concerns as the Internet continues to evolve.

The broad distribution across 36 working groups—including security (SECDISPATCH), routing (LSR), and even blockchain (SATP) groups—demonstrates that end-to-end thinking remains a cross-cutting concern that influences work across many technical domains within the IETF.

## Resources

- **[RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958)** — Essential reading that codifies the end-to-end principle as a foundational Internet design principle alongside other architectural guidelines.

- **[RFC 3724: The Rise of the Middle and the Future of End-to-End](https://www.rfc-editor.org/rfc/rfc3724)** — Provides crucial historical perspective on how the Internet has evolved away from pure end-to-end architecture and examines the implications for future protocol design.

- **[End-to-End Arguments in System Design](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf) by Saltzer, Reed, and Clark** — The foundational 1984 paper that introduced the principle; essential for understanding the original reasoning and scope of end-to-end arguments.

- **[End-to-End Principle (Wikipedia)](https://en.wikipedia.org/wiki/End-to-end_principle)** — Accessible overview with examples and discussion of how the principle applies to various network functions and modern Internet challenges.

---

*This report was generated from analysis of IETF working group session transcripts covering meetings 110-123 (March 2021 – July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `317f8ebe-3225-45da-8907-8704b0027aab` |
Sessions analyzed: 56 |
Generated: 2026-03-14*
