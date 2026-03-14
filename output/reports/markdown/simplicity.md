# Simplicity / complexity management

## Introduction

The principle of simplicity and complexity management stands as one of the foundational tenets of Internet architecture, asserting that "complexity is the primary impediment to scaling" and advocating to "keep designs simple." This principle emerged from decades of experience in building large-scale distributed systems, where the accumulation of complexity often becomes the limiting factor in a system's ability to grow, adapt, and remain maintainable over time.

Formally codified in [RFC 3439](https://www.rfc-editor.org/rfc/rfc3439), "Some Internet Architectural Guidelines and Philosophy," this principle reflects hard-learned lessons from the Internet's evolution. The document, authored by Randy Bush and Dave Meyer in 2002, distilled decades of architectural wisdom into actionable guidelines. The principle draws heavily from the "worse is better" philosophy popularized by Richard Gabriel, which argues that simplicity in both interface and implementation often trumps theoretical completeness or elegance.

In IETF working groups, this principle serves as a crucial design constraint and decision-making tool. When protocol designers face choices between feature-rich solutions and simpler alternatives, the complexity management principle provides guidance toward solutions that prioritize scalability, implementability, and long-term maintainability. As evidenced by its discussion across 418 sessions spanning all 14 meetings from IETF 110 to 123, this principle remains actively relevant in contemporary protocol design debates.

## Key References

- [RFC 3439: Some Internet Architectural Guidelines and Philosophy](https://www.rfc-editor.org/rfc/rfc3439) — The foundational document establishing simplicity as a core Internet design principle
- [Worse is Better (Richard Gabriel)](https://www.dreamsongs.com/WorseIsBetter.html) — Seminal essay arguing that simple, implementable designs often succeed over theoretically superior but complex alternatives
- [KISS Principle (Wikipedia)](https://en.wikipedia.org/wiki/KISS_principle) — Overview of the "Keep It Simple, Stupid" design philosophy that underpins much of Internet architecture

## This Principle in IETF Discussions

The principle of simplicity emerges repeatedly in IETF discussions as working groups grapple with the tension between feature completeness and maintainable design. These conversations reveal how complexity management operates as both a technical constraint and a philosophical guide in protocol development.

In the NETMOD working group, complexity concerns have driven significant architectural decisions around YANG module packaging. During IETF 121 in Dublin, participants discussed their approach to module versioning:

> "what we got to was let's try and keep it simple so let's not have that distinction let's not try and to like boil the ocean and do" (IETF 121 - NETMOD Working Group)

This discussion continued into IETF 123 in Madrid, where the group reflected on their decision-making process:

> "we started discussing it just before one of the meetings and we made some decisions on how we could progress this work in a better way and we said we wanted to keep it simple. We wanted to remove this complexity between API and implementation packages" (IETF 123 - NETMOD Working Group)

These exchanges illustrate how working groups explicitly invoke simplicity as a design criterion when faced with potentially over-engineered solutions. The NETMOD group's decision to avoid "boiling the ocean" reflects a mature understanding that attempting to solve all possible use cases often leads to solutions too complex to implement or deploy effectively.

The MASQUE working group demonstrates another facet of complexity management during protocol design discussions. At IETF 120 in Vancouver, when discussing connection redirection mechanisms:

> "the server is just going to send you an IP in Port and say I'd really rather you be over here fair enough I think we can just keep it simple and move on" (IETF 120 - MASQUE Working Group)

This exchange shows how simplicity principles help working groups avoid feature creep. Rather than designing elaborate redirection mechanisms, the group opted for a straightforward approach that meets the core requirement without additional complexity.

The MLS working group's experience at IETF 121 reveals how complexity can accumulate inadvertently during the design process:

> "the rest of it I feel like we've worked ourselves into well of complexity with a bunch of extra assumptions we've made in safe extension the way safe extensions is" (IETF 121 - MLS Working Group)

This honest assessment demonstrates the importance of periodic complexity audits during protocol development. Even experienced working groups can find themselves "in a well of complexity" when incremental decisions compound over time.

The ASAP working group at IETF 110 exemplifies the practical application of the "perfect is the enemy of good" philosophy:

> "my sense again it's like you know keep it simple and you know perfect is the enemy the good i think there's gonna there's no shortage" (IETF 110 - ASAP Working Group)

This perspective reflects the engineering reality that shipping a simple, functional solution often provides more value than pursuing an idealized but complex alternative that may never reach deployment.

## Historical Analysis

Analysis of discussion frequency across IETF 110-123 reveals interesting patterns in how simplicity and complexity management concerns have evolved. The data shows relatively consistent attention to this principle throughout the period, with notable peaks during certain meetings.

| Meeting | Date | Location | Discussion Count |
|---------|------|----------|------------------|
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

The data reveals several interesting trends. First, IETF 111 shows the lowest discussion frequency (16), which may reflect the continuing adjustment to online-only meetings during the pandemic period. Subsequently, discussion levels increased significantly, with the most recent meetings (IETF 121-123) showing the highest frequencies (38, 35, 39 respectively), suggesting that complexity management has become an increasingly prominent concern in protocol design.

The working groups most frequently discussing this principle provide insight into where complexity challenges are most acute. The top groups include nmrg and rtgwg (9 discussions each), followed by cfrg, masque, netmod, and v6ops (8 each). This distribution makes sense given the nature of these groups' work. Network management (nmrg, netmod) inherently deals with complex systems requiring careful complexity management. Routing (rtgwg) and IPv6 operations (v6ops) involve protocols that must scale to global deployment. Cryptography (cfrg) and new protocol development (masque) face the challenge of balancing security requirements with implementation simplicity.

The broad distribution across 149 unique working groups (representing the vast majority of active IETF working groups) indicates that simplicity and complexity management is not confined to specific technical areas but represents a universal concern across Internet protocol development.

## Resources

- **[RFC 3439: Some Internet Architectural Guidelines](https://www.rfc-editor.org/rfc/rfc3439)** — Essential reading for any Internet protocol designer, this document provides the authoritative treatment of simplicity as an architectural principle, with practical guidance on applying it to protocol design decisions.

- **[Worse is Better (Richard Gabriel)](https://www.dreamsongs.com/WorseIsBetter.html)** — This influential essay articulates the philosophy underlying much of Internet architecture, explaining why simple, implementable designs often succeed where more theoretically complete but complex solutions fail.

- **[KISS Principle (Wikipedia)](https://en.wikipedia.org/wiki/KISS_principle)** — Provides historical context and examples of the "Keep It Simple, Stupid" principle across engineering disciplines, helping protocol designers understand how simplicity principles apply beyond just Internet protocols.

- **[The Design Philosophy of the DARPA Internet Protocols (RFC 1958)](https://www.rfc-editor.org/rfc/rfc1958.html)** — While predating RFC 3439, this document establishes many of the foundational principles that inform complexity management in Internet protocols.

- **[End-to-End Arguments in System Design (Saltzer, Reed, Clark)](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf)** — This seminal paper demonstrates how architectural principles like end-to-end can reduce system complexity by carefully placing functionality at appropriate layers.

---

*This report was generated from analysis of IETF meeting transcripts (vCon format) covering working group sessions from IETF 110 through IETF 123.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `719bcf65-a036-4d0c-a959-7ee59ae43328` |
Sessions analyzed: 418 |
Generated: 2026-03-14*
