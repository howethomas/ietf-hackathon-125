# Principle of Constant Change

## Introduction

The principle of constant change stands as one of the foundational tenets of Internet architecture, formally articulated in [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) by Brian Carpenter in 1996. Simply stated, "The Internet must continue to evolve. Design for extensibility." This principle recognizes that the Internet is not a static system but a living, growing organism that must adapt to new technologies, changing user needs, and unforeseen requirements.

The principle emerged from the early Internet's remarkable success in adapting beyond its original scope. What began as ARPANET—a research network connecting a handful of universities—evolved into the global Internet supporting billions of users and applications that its creators never imagined. This transformation was possible precisely because the original designers built extensibility into the core protocols, allowing the network to grow organically rather than requiring complete redesign.

In the IETF's work from 2021 through 2025, this principle has remained critically relevant as engineers grapple with emerging challenges like quantum computing threats, massive IoT deployments, and new application paradigms. The principle guides protocol designers to build systems that can evolve gracefully, ensuring the Internet's continued adaptability in an uncertain future. It's not just about accommodating known future needs—it's about creating space for the unknown innovations that will inevitably emerge.

## Understanding This Principle

**The Core Idea**

Design systems so they can grow and change without breaking what already exists.

Think of this like designing a city. When urban planners lay out a new city, they don't just build for today's population—they create infrastructure that can expand. They design street grids that can accommodate new neighborhoods, leave space for utility corridors that can carry future services, and establish zoning patterns that can evolve with changing needs. The best cities have "bones" that remain stable while everything around them adapts and grows.

The principle of constant change applies this same thinking to Internet protocols. Just as a city planner might require that all new buildings include conduit space for unknown future utilities, protocol designers build in extension points, reserved fields, and negotiation mechanisms that allow new capabilities to be added later without disrupting existing systems.

**Why It Matters**

When you violate this principle, you create digital dead ends—protocols that work perfectly today but become obsolete tomorrow, requiring painful migrations or complete replacements.

Consider IPv4 versus IPv6 as a stark example. IPv4 was designed when the Internet was a small research network. Its 32-bit address space seemed vast for connecting university computers, but offered no room to grow. When the Internet exploded globally, we hit the fundamental limit—you simply cannot fit more than 4.3 billion addresses into 32 bits. The result? A decades-long, still-ongoing migration to IPv6 that has cost billions of dollars and created enormous technical complexity.

Contrast this with HTTP, which was designed with extensibility from the start. HTTP includes header fields that can carry new information, status codes that can be extended, and method names that can be added. This extensibility allowed HTTP to evolve from serving simple web pages to supporting everything from video streaming to real-time gaming to IoT device communication—all without breaking existing browsers or servers.

**The Tension**

The counterforce here is the natural human tendency to optimize for known requirements rather than unknown future needs. Extensibility often means added complexity, reduced performance, and increased implementation cost today to solve problems you might never actually encounter.

Engineers face constant pressure to ship quickly and efficiently. Adding extension points feels like over-engineering when you have concrete requirements and tight deadlines. Business stakeholders question why they should pay for capabilities they don't need. The temptation is always to build exactly what's required today and assume you can add features later—but "later" often means starting over entirely.

This tension is especially acute in resource-constrained environments. Every reserved bit field, every optional parameter, every negotiation handshake consumes bytes, processing cycles, and implementation complexity. When you're designing protocols for IoT devices with severe power and bandwidth constraints, extensibility can feel like an expensive luxury.

**How to Recognize It**

You're seeing this principle at work when protocols include version numbers that actually get used, when APIs have optional parameters that start empty but fill in over time, or when data formats include "reserved for future use" fields that eventually carry new information. You see it violated when systems require complete replacement rather than gradual upgrade, when adding new features breaks existing implementations, or when protocols fragment into incompatible variants because they couldn't accommodate different needs within a single framework.

## Key References

- [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — The foundational document that articulates this principle along with other core Internet design tenets.

## This Principle in IETF Discussions

The principle of constant change manifests throughout IETF working groups as engineers grapple with balancing immediate needs against future flexibility. These discussions reveal how the principle applies across diverse protocol domains, from low-level networking to application-layer services.

In the BESS (BGP Enabled ServiceS) working group, participants explicitly focused on extensibility when developing new safety mechanisms:

> "we have focused on defining extensions that provide efficiency and extensibility and improve upon some of the legacy uh constraints we have you know seen in the past"

This comment from IETF 110 illustrates how working groups use new protocol development as opportunities to address extensibility limitations in existing systems, ensuring that today's solutions don't become tomorrow's constraints.

The challenge of achieving true extensibility became apparent in the CALEXT working group's work on calendar extensions. Engineers discovered that their carefully designed extension mechanism had unexpected limitations:

> "we found out that the uh alternate extensible quote extensible syntax for defining the alarms wasn't quite as extensible as we thought"

This honest assessment from IETF 110 highlights how extensibility is often harder to achieve than initially anticipated, requiring iterative refinement as real-world usage reveals gaps in the original design.

Forward compatibility emerged as a key concern in the MASQUE working group, where participants emphasized the importance of explicit signaling for future-proofing:

> "i think we need to use the settings um just how it is is i believe the correct way i think it's more for future proofing also to be very explicit that the h3 application is intending to do this"

This discussion from IETF 110 shows how engineers must balance simplicity with future flexibility, often choosing more explicit approaches specifically to preserve extensibility options.

The MPLS working group demonstrated practical backward compatibility techniques when extending existing protocols:

> "this draft split that 16 bit reserve field into two different fields and the eight bit the first eight bit field is used as the algorithm field so this is backward compatible because uh you know if it is the default flex algo then the value will be zero"

This approach from IETF 110 exemplifies how reserved fields enable graceful evolution—the protocol can support new functionality while remaining compatible with implementations that only understand the original specification.

## Historical Analysis

The discussion frequency data reveals consistent attention to the principle of constant change across all IETF meetings from 110 through 123, with notable peaks during transition periods:

| Meeting | Date | Location | Discussions |
|---------|------|----------|-------------|
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

The highest discussion frequencies occurred during IETF 110 and 116 (48 sessions each), suggesting heightened attention to extensibility during periods of significant protocol evolution. IETF 110 coincided with major developments in post-pandemic network requirements, while IETF 116 aligned with quantum-readiness discussions that required extensive protocol extensibility planning.

The working groups most engaged with this principle—netmod, iabopen, lsr, masque, and quic—represent diverse protocol layers but share common challenges in managing protocol evolution. Network modeling (netmod), routing protocols (lsr), and emerging application protocols (masque, quic) all require careful attention to extensibility to accommodate rapidly changing requirements and maintain long-term viability.

The broad distribution across 149 working groups demonstrates that extensibility concerns permeate all aspects of Internet protocol development, from low-level transport mechanisms to high-level application services.

## Resources

- [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — Essential reading for understanding the foundational principles that guide Internet protocol design, including the complete context for the constant change principle.

- [RFC 6709: Design Considerations for Protocol Extensions](https://www.rfc-editor.org/rfc/rfc6709) — Practical guidance for protocol designers on implementing extensibility mechanisms that actually work in practice.

- [Protocol Extensibility (Wikipedia)](https://en.wikipedia.org/wiki/Extensibility) — Accessible overview of extensibility concepts across different types of systems, providing broader context beyond Internet protocols.

---
*This report was generated from vCon analysis of IETF working group session transcripts from meetings 110-123 (March 2021 - July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `ca07c18a-c675-46f1-afce-251143c309e8` |
Sessions analyzed: 565 |
Generated: 2026-03-14*
