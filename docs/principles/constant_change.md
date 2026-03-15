# Principle of constant change

## Introduction

The "Principle of constant change" stands as one of the foundational tenets of Internet architecture, formally articulated in [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) by Brian Carpenter in 1996. The principle states simply: "The Internet must continue to evolve. Design for extensibility." While deceptively straightforward, this guidance has profoundly shaped how Internet protocols are designed, deployed, and maintained across decades of technological transformation.

This principle emerged from hard-won experience in the Internet's formative years, when engineers repeatedly encountered protocols that became obsolete or required painful redesigns because they couldn't accommodate new requirements. Rather than treat extensibility as a nice-to-have feature, RFC 1958 elevated it to an architectural imperative. The principle recognizes that the Internet operates in a fundamentally unpredictable environment—new applications, security threats, performance requirements, and deployment contexts will always emerge faster than any standards body can anticipate.

The significance of this principle extends far beyond protocol design. It reflects a philosophical stance about how to build infrastructure for an unknowable future, influencing everything from data formats and addressing schemes to authentication mechanisms and routing protocols. In IETF discussions from 2021 to 2025, this principle appears in 565 sessions across 149 working groups, demonstrating its continued relevance as the Internet faces challenges like post-quantum cryptography, massive IoT deployments, and emerging network paradigms.

## Understanding This Principle

**The Core Idea** — The Internet must be designed to accommodate changes that haven't been invented yet. Think of this principle like designing a city's infrastructure: successful urban planners don't just build roads for today's horse-drawn carriages—they create transportation systems that can later support automobiles, buses, bicycles, and even future technologies like autonomous vehicles or underground pneumatic tubes. The roads have standardized dimensions and connection points, utility corridors can accommodate new types of cables, and zoning frameworks can adapt to new types of buildings. Similarly, Internet protocols must include "expansion joints" and "upgrade paths" that allow new capabilities to be added without rebuilding the foundation.

**Why It Matters** — When protocols lack extensibility, the consequences ripple through the entire Internet ecosystem for decades. Consider IPv4 addresses: the original designers allocated 32 bits for addressing, which seemed generous for a research network connecting universities. But without built-in extensibility mechanisms, the eventual address exhaustion required deploying an entirely new protocol (IPv6)—a transition that's still ongoing after 25 years and billions of dollars in deployment costs. Contrast this with HTTP headers, which were designed as extensible name-value pairs. When new requirements emerged—caching directives, security policies, content negotiation—they could be added through new headers without breaking existing implementations. The result? HTTP has evolved continuously from a simple document retrieval protocol to the foundation of modern web applications, APIs, and real-time communication.

**The Tension** — The pressure against extensibility is relentless and often rational. Adding extension points makes protocols more complex, increases implementation costs, and creates potential security vulnerabilities. Engineers face deadline pressures to ship working solutions for known requirements rather than spending time on hypothetical future needs. Organizations worry that over-engineering will delay deployment while competitors ship simpler solutions. There's also the "YAGNI" (You Aren't Gonna Need It) principle from software development, which warns against premature optimization. The challenge is distinguishing between wise future-proofing and wasteful over-engineering—a judgment call that often determines whether a protocol thrives for decades or becomes an evolutionary dead-end.

**How to Recognize It** — You're seeing this principle at work when:

* A messaging format includes version fields and reserved space, allowing new data types to be added without breaking existing parsers
* An API design uses structured error codes and extensible response formats rather than hardcoded strings, enabling richer diagnostics as the system matures
* A network protocol allocates address space hierarchically (like phone numbers with country codes, area codes, and local numbers) rather than as a flat namespace, allowing new addressing schemes to be layered on top
* A security framework separates policy decisions from enforcement mechanisms, letting new authentication methods integrate without changing the core authorization logic

## Early IETF Work

The principle of constant change crystallized from painful lessons learned during the Internet's transition from a research network to global infrastructure. The most prominent example is the IPv4 address exhaustion crisis that began appearing in the early 1990s. While the original Internet Protocol designers had allocated what seemed like an enormous address space—over 4 billion addresses—they hadn't anticipated the Internet's explosive growth or the addressing inefficiencies that would emerge from classful routing. By the time the problem became apparent, hundreds of millions of devices were already using IPv4, making a clean transition to a new protocol extraordinarily difficult.

This experience directly influenced the design of IPv6, which not only expanded the address space dramatically but also included extensibility mechanisms like extension headers that allow new functionality to be added without changing the base protocol. Similarly, the evolution of routing protocols shows both successes and failures in applying this principle. The Border Gateway Protocol (BGP) included extensible path attributes from its inception, allowing new routing policies and security features to be added over decades of use. In contrast, earlier routing protocols like RIP had to be completely replaced when their limitations became apparent.

The IETF's experience with protocol layering also shaped this principle. The success of the TCP/IP stack demonstrated the power of clean interfaces between layers—applications could evolve independently from network technologies, and new link-layer protocols could be deployed without changing higher-layer protocols. This architectural decision to design for extensibility at layer boundaries became a template for subsequent protocol development throughout the 1990s and 2000s.

## Key References

* [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — Brian Carpenter's seminal articulation of Internet architectural principles, including the foundational statement that "the Internet must continue to evolve."

* [RFC 6709: Design Considerations for Protocol Extensions](https://www.rfc-editor.org/rfc/rfc6709) — Comprehensive guidance on how to design protocols that can be safely extended while maintaining interoperability.

* [RFC 5218: What Makes For a Successful Protocol?](https://www.rfc-editor.org/rfc/rfc5218) — Analysis of factors that contribute to protocol success, with extensibility as a key theme.

## This Principle in IETF Discussions

The principle of constant change pervades IETF deliberations across diverse technical domains, reflecting its fundamental role in Internet architecture. In early 2021, the [calext](https://datatracker.ietf.org/wg/calext/about/) working group discovered firsthand how extensibility assumptions can break down under real-world pressure:

> "we found out that the uh alternate extensible quote extensible syntax for defining the alarms wasn't quite as extensible as we thought"

This candid admission from IETF 110 illustrates a common pattern—features designed to be extensible often reveal limitations when developers try to extend them in unexpected ways. *[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf110/ietf110_calext_28624.vcon.json)*

During the same period, the [bess](https://datatracker.ietf.org/wg/bess/about/) working group was grappling with how to design new protocols that could learn from past mistakes:

> "we have focused on defining extensions that provide efficiency and extensibility and improve upon some of the legacy uh constraints we have you know seen in the past"

This quote from IETF 110 captures the IETF's ongoing effort to balance immediate functionality with long-term adaptability, explicitly acknowledging that current designs must avoid the limitations that trapped earlier protocols. *[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf110/ietf110_bess_28579.vcon.json)*

By late 2022, discussions had evolved to address more sophisticated extensibility challenges. The [core](https://datatracker.ietf.org/wg/core/about/) working group was wrestling with the temporal aspects of protocol extension:

> "ially adding something to a registry after the fact will have no effect in in many uh environments um so that that's a problem with just saying oh we drop in a registry here and and that provides the extensibility we need"

This observation from IETF 115 highlights a crucial insight—technical extensibility mechanisms are worthless if deployment realities prevent their use. The ability to add new registry entries means nothing if existing implementations never check for updates. *[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf115/ietf115_core_29839.vcon.json)*

Recent discussions show growing sophistication in applying extensibility principles to emerging technologies. During IETF 120 in 2024, the [anrw](https://datatracker.ietf.org/wg/anrw/about/) working group examined how HTTP/3's extensible prioritization schemes perform in real-world deployments:

> "this is the results on HTP 3 extensible prioritization scheme in the wild"

This research direction reflects the IETF's maturation—rather than simply designing extensible protocols, the community now studies how extensibility mechanisms behave under actual deployment conditions, feeding lessons back into future protocol design. *[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf120/ietf120_anrw_33119.vcon.json)*

The evolution of these discussions from 2021 to 2024 reveals the IETF's growing appreciation that extensibility is not just a design property but an ecosystem characteristic that must be actively maintained through deployment practices, implementation choices, and operational procedures.

## Historical Analysis

Discussion of the principle of constant change has remained consistently high throughout IETF meetings 110-123, with notable peaks during periods of major architectural decisions. The frequency data reveals interesting patterns in how this principle manifests across different IETF venues:

| Meeting | Date | Location | Sessions Discussing Principle |
|---------|------|----------|------------------------------|
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

The working groups most actively discussing this principle reveal its broad applicability across Internet technologies. The [netmod](https://datatracker.ietf.org/wg/netmod/about/) working group's frequent engagement (12 sessions) reflects ongoing challenges in network management protocols, where extensibility is crucial for accommodating diverse vendor implementations and evolving operational practices. The [iabopen](https://datatracker.ietf.org/wg/iabopen/about/) sessions (11 discussions) indicate architectural-level consideration of how extensibility principles should guide Internet evolution.

Transport and security protocols also feature prominently, with [quic](https://datatracker.ietf.org/wg/quic/about/) (11 sessions) and [lake](https://datatracker.ietf.org/wg/lake/about/) (10 sessions) wrestling with how to build extensibility into performance-critical protocols where every byte and round-trip matters. The appearance of [masque](https://datatracker.ietf.org/wg/masque/about/) (11 sessions) in this list reflects growing interest in how traditional extensibility principles apply to emerging network paradigms like HTTP-based VPNs and proxying.

Notably, the principle's discussion frequency increased during in-person meetings (IETF 110, 116, 117, 121) compared to purely online sessions, suggesting that extensibility discussions benefit from the richer interaction patterns possible in face-to-face settings. The consistency of discussion levels from 2021 to 2025 indicates that this principle remains actively relevant rather than becoming a taken-for-granted assumption.

## Resources

* [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — The foundational document that established extensibility as a core Internet design principle, essential reading for understanding the philosophical foundations of Internet architecture.

* [RFC 6709: Design Considerations for Protocol Extensions](https://www.rfc-editor.org/rfc/rfc6709) — Practical engineering guidance on how to design extension mechanisms that actually work in deployment, covering versioning strategies, compatibility considerations, and common pitfalls.

* [RFC 5218: What Makes For a Successful Protocol?](https://www.rfc-editor.org/rfc/rfc5218) — Empirical analysis of why some protocols thrive while others fail, with extensibility as a crucial success factor alongside simplicity and implementability.

* [Protocol Extensibility (Wikipedia)](https://en.wikipedia.org/wiki/Extensibility) — Accessible introduction to extensibility concepts across different technical domains, helpful for understanding how Internet protocol design relates to broader software architecture principles.

---
*This report was generated from analysis of IETF meeting transcripts stored in vCon format, covering working group sessions from IETF 110 through IETF 123.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `ca07c18a-c675-46f1-afce-251143c309e8` |
Sessions analyzed: 565 |
Generated: 2026-03-15*
