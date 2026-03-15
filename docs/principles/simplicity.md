# Simplicity / complexity management

## Introduction

"Complexity is the primary impediment to scaling. Keep designs simple." This fundamental principle, codified in [RFC 3439](https://www.rfc-editor.org/rfc/rfc3439), represents one of the Internet's most enduring architectural philosophies. While it sounds deceptively straightforward, this principle has guided decades of Internet protocol development and continues to shape how engineers approach network design challenges.

The principle emerged from hard-won experience in the Internet's early decades. As documented in RFC 3439, "Some Internet Architectural Guidelines and Philosophy" by Bush and Meyer in 2002, the Internet's remarkable success stems partly from deliberate choices to favor simple, composable protocols over complex, monolithic ones. This wasn't academic theorizing — it was a response to witnessing both spectacular failures of over-engineered systems and surprising successes of minimalist approaches.

In IETF working groups today, this principle remains vibrantly relevant. As our analysis of 418 sessions across IETF meetings 110-123 (March 2021 to July 2025) demonstrates, engineers continue to invoke simplicity as both a design goal and a critical lens for evaluating proposals. From routing protocols to cryptographic frameworks, the tension between functionality and complexity shapes every significant technical decision.

## Understanding This Principle

**The Core Idea** — Simple systems scale; complex ones break under their own weight. Think of a small neighborhood restaurant that serves exceptional food with a focused menu, efficient kitchen workflow, and staff who know every dish intimately. As it grows popular, the owners face pressure to add more menu items, expand seating, offer delivery, create a rewards program, and accommodate special dietary needs. Each addition seems reasonable, but collectively they transform a smoothly-running operation into a chaotic system where orders get confused, quality suffers, staff turnover increases, and customers leave frustrated. The restaurant's original strength — simplicity that enabled excellence — gets buried under accumulated complexity.

**Why It Matters** — In network protocols, complexity manifests as interoperability failures, security vulnerabilities, implementation bugs, and operational nightmares. Consider IPv6 adoption versus IPv4 network address translation (NAT). IPv6 represents the "clean" solution — a simple expansion of address space with straightforward forwarding rules. NAT, by contrast, is a complexity band-aid that breaks end-to-end connectivity, complicates application design, and creates subtle failure modes. Yet NAT succeeded because it solved an immediate problem simply, while IPv6's comprehensive approach initially seemed too complex to deploy incrementally. The irony is that NAT's accumulated complexity has now become far more burdensome than IPv6's original design, but the immediate simplicity advantage mattered more than long-term architectural purity.

**The Tension** — The counterforce to simplicity is feature pressure. Customers demand new capabilities, vendors want competitive differentiation, and engineers see elegant ways to solve multiple problems simultaneously. Standards bodies face intense pressure to accommodate diverse use cases, leading to protocols that try to be everything to everyone. This pressure is often legitimate — the world genuinely needs these capabilities — but each addition increases the protocol's cognitive load, implementation complexity, and potential failure modes.

**How to Recognize It** — You're seeing this principle at work when:

* A team chooses to build three focused tools instead of one swiss-army-knife application, even though it means more repositories to maintain
* An architecture review rejects a clever optimization because it makes the system harder to reason about and debug
* A protocol design deliberately omits requested features to keep the core specification implementable by a small team
* Engineers debate whether a new feature belongs in an existing system or deserves its own separate component

## Early IETF Work

The Internet's foundational protocols embody this simplicity principle through deliberate design choices that favored minimal, composable components over monolithic solutions. TCP/IP succeeded partly because it separated concerns cleanly — IP handles packet delivery, TCP manages reliable streams — rather than bundling everything into a single complex protocol like the ISO's OSI stack attempted. The original HTTP specification was famously simple: request/response semantics, human-readable headers, and stateless operation. This simplicity enabled rapid adoption and experimentation.

However, the IETF learned some hard lessons about complexity through failures. The original SNMP (Simple Network Management Protocol) lived up to its name initially, but successive versions accumulated features and complexity that made implementation and deployment increasingly difficult. Similarly, early attempts at comprehensive solutions like the ISO/OSI protocol suite foundered partly due to their complexity, while the Internet's "rough consensus and running code" philosophy favored simpler, incremental approaches.

The principle was formalized through experience with protocols that violated it. X.400 email systems, comprehensive but complex, lost to SMTP's simplicity. Complex routing protocols with extensive feature sets struggled with interoperability while simpler approaches like BGP (despite its own complexities) achieved widespread deployment. These experiences shaped RFC 3439's explicit articulation of simplicity as a fundamental architectural principle, recognizing that the Internet's success came not despite its simplicity, but because of it.

## Key References

- [RFC 3439: Some Internet Architectural Guidelines and Philosophy](https://www.rfc-editor.org/rfc/rfc3439) — The foundational document that explicitly codifies simplicity as a core Internet design principle
- [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — Earlier articulation of Internet design philosophy that influenced the simplicity principle
- [End-to-End Arguments in System Design](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf) — Saltzer, Reed, and Clark's seminal paper on keeping network complexity at the edges

## This Principle in IETF Discussions

The principle of simplicity management appears consistently across IETF working groups, often arising when engineers must choose between comprehensive solutions and focused approaches. In the [netmod](https://datatracker.ietf.org/wg/netmod/about/) working group during IETF 111, this tension emerged clearly during discussions of YANG module versioning:

> "we were um looking at one point about having two different extensions one was revision or derived and one was revision or derived compatible but in the end we decided to kind of keep it simple and we think the majority of the realistic use cases don't require a derived or compa"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf111/ietf111_netmod_28884.vcon.json)*

This exemplifies a common pattern: engineers initially design comprehensive solutions to handle edge cases, then deliberately simplify to focus on core use cases. The [netmod](https://datatracker.ietf.org/wg/netmod/about/) group recognized that trying to solve every versioning scenario upfront would create implementation complexity that might prevent adoption of the basic functionality.

The research community explicitly embraces simplicity as a decision-making tool. During IETF 115, the [coinrg](https://datatracker.ietf.org/wg/coinrg/about/) working group discussed using simplicity as a tiebreaker between competing approaches:

> "for um the inspiration we'll then look at the Simplicity principle which basically states that we should always Thrive to the simplest solution or"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf115/ietf115_coinrg_29890.vcon.json)*

This shows how the principle operates not just as a design guideline, but as an explicit evaluation criterion when multiple technical approaches seem equally viable. The simplest solution often wins not because it's necessarily superior technically, but because it's more likely to be implemented correctly and adopted widely.

In more recent discussions, the [masque](https://datatracker.ietf.org/wg/masque/about/) working group at IETF 120 demonstrated how simplicity thinking helps avoid scope creep:

> "fair enough I think we can just keep it simple and move on okay Alexander gini Cloud flare yeah the the whole capsule thing seems li"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf120/ietf120_masque_33088.vcon.json)*

The phrase "keep it simple and move on" captures a crucial aspect of complexity management: recognizing when additional features would provide marginal benefit at disproportionate complexity cost. This kind of disciplined scope management prevents protocols from growing beyond their implementers' ability to handle them reliably.

The [mls](https://datatracker.ietf.org/wg/mls/about/) working group at IETF 121 illustrates how complexity can accumulate gradually through well-intentioned extensions:

> "Richard I hate all of this I the bottom bullet yes absolutely we should do that easy quick fix bug fix clear Omission um the rest of it I feel like we've worked ourselves into well of complexity with a bunch of extra assumptions we've made in safe extension the way safe extensions is"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf121/ietf121_mls_33433.vcon.json)*

This candid observation reveals how complexity accumulates: each individual extension seems reasonable, but collectively they create a "well of complexity" that makes the system harder to understand, implement, and maintain. The speaker's frustration reflects a common experience in protocol development where good intentions lead to overwhelming complexity.

## Historical Analysis

Analysis of simplicity discussions across IETF meetings 110-123 reveals consistent engagement with this principle, with notable variations in intensity:

| Meeting | Date | Location | Sessions Discussing Simplicity |
|---------|------|----------|-------------------------------|
| IETF 110 | March 2021 | Online | 33 |
| IETF 111 | July 2021 | Online | 16 |
| IETF 112 | November 2021 | Online | 27 |
| IETF 113 | March 2022 | Vienna | 24 |
| IETF 114 | July 2022 | Philadelphia | 27 |
| IETF 115 | November 2022 | London | 34 |
| IETF 116 | March 2023 | Yokohama | 31 |
| IETF 117 | July 2023 | San Francisco | 25 |
| IETF 118 | November 2023 | Prague | 31 |
| IETF 119 | March 2024 | Brisbane | 30 |
| IETF 120 | July 2024 | Vancouver | 28 |
| IETF 121 | November 2024 | Dublin | 38 |
| IETF 122 | March 2025 | Bangkok | 35 |
| IETF 123 | July 2025 | Madrid | 39 |

The data shows an interesting pattern: discussion frequency was highest during the early online meetings (IETF 110) and recent in-person meetings (IETF 121-123), suggesting that complexity management becomes more prominent during periods of transition or intensive development activity.

The working groups most engaged with simplicity span diverse technical domains. Research groups like [nmrg](https://datatracker.ietf.org/wg/nmrg/about/) and [coinrg](https://datatracker.ietf.org/wg/coinrg/about/) frequently invoke simplicity as an evaluation criterion for competing approaches. Infrastructure groups like [rtgwg](https://datatracker.ietf.org/wg/rtgwg/about/) and [6man](https://datatracker.ietf.org/wg/6man/about/) wrestle with balancing feature requests against operational simplicity. Security-focused groups like [cfrg](https://datatracker.ietf.org/wg/cfrg/about/) recognize that cryptographic complexity often introduces vulnerabilities.

The prominence of [netmod](https://datatracker.ietf.org/wg/netmod/about/) in these discussions reflects the inherent tension in network management: operators want comprehensive modeling capabilities, but complex data models become unmaintainable. Similarly, [masque](https://datatracker.ietf.org/wg/masque/about/)'s frequent simplicity discussions stem from building proxy protocols where each feature addition impacts every implementation.

## Resources

- [RFC 3439: Some Internet Architectural Guidelines and Philosophy](https://www.rfc-editor.org/rfc/rfc3439) — Essential reading for understanding how simplicity fits into the broader Internet architectural philosophy
- [The Worse is Better Philosophy](https://www.dreamsongs.com/WorseIsBetter.html) — Richard Gabriel's influential essay exploring how simple, imperfect solutions often succeed where complex, comprehensive ones fail
- [KISS Principle (Wikipedia)](https://en.wikipedia.org/wiki/KISS_principle) — Good overview of "Keep It Simple, Stupid" and its applications across engineering disciplines
- [End-to-End Arguments in System Design](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf) — Classic paper showing how pushing complexity to network edges rather than the core enables scalability and innovation

---
*This report was generated through analysis of IETF working group session transcripts stored in vCon format, covering meetings 110-123 from March 2021 through July 2025.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `719bcf65-a036-4d0c-a959-7ee59ae43328` |
Sessions analyzed: 418 |
Generated: 2026-03-15*
