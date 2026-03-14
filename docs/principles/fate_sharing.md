# Fate sharing

## Introduction

Fate sharing is one of the foundational design principles of the Internet, captured succinctly as "related parts of a system fail together, with state maintained only at endpoints." This principle emerged from the early Internet's design philosophy, first articulated by David Clark in his seminal 1988 paper "[The Design Philosophy of the DARPA Internet Protocols](http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf)" and later formalized in [RFC 1958](https://www.rfc-editor.org/rfc/rfc1958), "Architectural Principles of the Internet."

At its essence, fate sharing argues that if multiple components depend on each other to function, they should be designed so that they fail together rather than creating situations where some parts fail while others continue operating in a broken state. This principle has profound implications for how we design distributed systems, influencing everything from protocol design to error handling strategies across the Internet's architecture.

The principle remains remarkably relevant in modern Internet development, as evidenced by its consistent discussion across IETF meetings from 2021 to 2025. With 544 sessions discussing fate sharing across 14 consecutive IETF meetings, it continues to guide decisions in areas ranging from routing protocols to emerging technologies like QUIC and WebTransport, demonstrating its enduring importance in maintaining the Internet's robustness and reliability.

## Understanding This Principle

**The Core Idea**

If parts of a system must work together to be useful, design them so they fail together rather than creating half-working, broken states.

Think of fate sharing like the electrical system in your house. When a circuit breaker trips, it cuts power to an entire circuit rather than randomly shutting off individual outlets. This might seem wasteful—why kill power to the working outlets just because one has a problem? But imagine the alternative: outlets that randomly stop working while others keep going, with no clear indication of what's broken. You'd spend hours troubleshooting phantom problems, never knowing whether an unpowered device meant a local outlet failure, a partial circuit failure, or something else entirely. The circuit breaker's "all or nothing" approach means that when something breaks, the failure is obvious and complete, making diagnosis and repair straightforward.

**Why It Matters**

The alternative to fate sharing creates one of the most frustrating problems in distributed systems: partial failures that masquerade as working systems. Consider a simple example from web applications: imagine an online store where the shopping cart and payment processing are handled by separate systems with independent failure modes. Without fate sharing, you might have scenarios where customers can add items to their cart but can't check out, or worse—where payments process but orders don't get recorded. The system appears to work from some perspectives but fails from others, creating an inconsistent and confusing experience.

With fate sharing, the entire checkout process would be designed to succeed or fail as a unit. If any critical component is unavailable, the whole process fails cleanly with a clear error message, rather than partially succeeding and leaving customers and administrators in an ambiguous state. This "fail fast and obvious" approach makes systems much easier to monitor, debug, and repair.

**The Tension**

The primary tension against fate sharing is efficiency and resource optimization. It often seems wasteful to shut down perfectly good components just because a related component has failed. Organizations and engineers face constant pressure to maximize uptime and resource utilization. Why should a working server stop serving requests just because another server in the cluster fails? Why should a network connection be terminated just because some state information is lost?

This pressure is particularly intense in cloud environments where resources cost money and executives want maximum return on infrastructure investments. Engineering teams often face incentives to keep as much of a system running as possible during partial failures, viewing complete shutdowns as unnecessary and expensive. The principle of fate sharing can seem counterintuitive to managers who equate "more uptime" with "better system design."

**How to Recognize It**

You're seeing fate sharing at work when you observe these patterns: **Clean failure boundaries** — when something breaks, related components stop working immediately and obviously rather than limping along in degraded states. A well-designed microservices architecture that shuts down dependent services when a critical dependency fails exemplifies this. **Stateless intermediate components** — systems where the network routers, load balancers, and middleware don't maintain critical state that could become inconsistent during failures, pushing state management to the endpoints that actually care about the data. **Explicit error propagation** — when systems are designed to fail loudly and propagate failures up the stack rather than trying to hide or work around problems internally.

## Key References

- [RFC 1958](https://www.rfc-editor.org/rfc/rfc1958) — "Architectural Principles of the Internet" - The foundational document that formally articulates fate sharing as a core Internet design principle.
- [The Design Philosophy of the DARPA Internet Protocols](http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf) — David D. Clark (1988) - The seminal paper that first described the philosophical foundations underlying Internet protocol design, including the concept of fate sharing.

## This Principle in IETF Discussions

The principle of fate sharing surfaces regularly in IETF working group discussions, often at moments when protocol designers must choose between complexity and clean failure semantics. These conversations reveal how the principle guides real-world engineering decisions across diverse networking technologies.

In routing protocols, fate sharing concerns are particularly evident. During an IETF 110 BABEL working group session, participants discussed fragmentation challenges:

> "fragmentation required packets are going to fail to reach the sending host and you're going to have mysterious failures where some things work and then get stuck so the problem here is that you have no fate sharing between the data between on the one hand the date and act pass and on the other hand"

This excerpt illustrates a classic fate sharing problem: when packet fragmentation creates situations where some data succeeds while related data fails, leading to the "mysterious failures" that the principle aims to prevent.

The principle also emerges in discussions about modern application protocols. During an IETF 115 MOQ (Media over QUIC) working group session, designers were considering how to segment video content:

> "even though ondexual encoding they don't you could break them into individual segments too you can break it down as far as you want in this case we've got a segment for an individual frame so it's not fate sharing with the other frames when it doesn't need to be and then finally you could just break"

Here, the working group was explicitly considering when fate sharing is appropriate. Video frames that don't depend on each other shouldn't be forced to fail together, demonstrating that fate sharing requires careful analysis of actual dependencies rather than blanket application.

Security protocols present another area where fate sharing influences design decisions. In an IETF 119 IPSECME working group discussion about IPSec extensions:

> "is different it's native as extension header so basic IPv6 header will just indicate that inside we have as extension header and everything else is hidden it actually has some advantages uh if ESP is stateless allow through your uh filtering then you don't need you don't need any keep Al lives if th"

The emphasis on stateless operation reflects fate sharing principles—by avoiding state in intermediate components, the protocol reduces the risk of partial failures where security state becomes inconsistent with actual connection state.

## Historical Analysis

Discussion of fate sharing has remained remarkably consistent across IETF meetings from 110 to 123, with some notable patterns emerging:

| Meeting | Date | Location | Sessions |
|---------|------|----------|----------|
| IETF 110 | March 2021 | Online | 33 |
| IETF 111 | July 2021 | Online | 31 |
| IETF 112 | November 2021 | Online | 30 |
| IETF 113 | March 2022 | Vienna | 41 |
| IETF 114 | July 2022 | Philadelphia | 38 |
| IETF 115 | November 2022 | London | 51 |
| IETF 116 | March 2023 | Yokohama | 48 |
| IETF 117 | July 2023 | San Francisco | 40 |
| IETF 118 | November 2023 | Prague | 38 |
| IETF 119 | March 2024 | Brisbane | 32 |
| IETF 120 | July 2024 | Vancouver | 38 |
| IETF 121 | November 2024 | Dublin | 30 |
| IETF 122 | March 2025 | Bangkok | 33 |
| IETF 123 | July 2025 | Madrid | 61 |

The data reveals several interesting trends. Discussion peaked during IETF 115 in London (51 sessions) and saw a dramatic surge at IETF 123 in Madrid (61 sessions), suggesting renewed focus on architectural principles as new technologies mature. The transition from online to in-person meetings (starting with IETF 113 in Vienna) coincided with increased discussion frequency, possibly reflecting the richer technical discussions that occur during face-to-face interactions.

The working groups with the most fate sharing discussions—CORE (13), DTN (13), 6LO (12), DMM (12), and SPRING (12)—represent a mix of foundational technologies and emerging protocols. This distribution suggests that fate sharing remains relevant both for established Internet infrastructure and for new protocol development, particularly in areas involving mobility, constrained devices, and delay-tolerant networking where failure modes are especially critical.

The broad distribution across 141 unique working groups demonstrates that fate sharing is not confined to specific technical domains but rather serves as a cross-cutting architectural principle that influences decisions across the entire Internet protocol stack.

## Resources

- [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — Essential reading for understanding how fate sharing fits within the broader Internet design philosophy.
- [The Design Philosophy of the DARPA Internet Protocols](http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf) — Clark's foundational paper provides the historical context and reasoning behind fate sharing as a design principle.
- [Fate-sharing (Wikipedia)](https://en.wikipedia.org/wiki/Fate-sharing) — A concise overview with additional examples of how the principle applies across different networking contexts.
- [End-to-End Arguments in System Design](https://web.mit.edu/saltzer/www/publications/endtoend/endtoend.pdf) — Saltzer, Reed, and Clark's influential paper on end-to-end arguments, which complements fate sharing principles in distributed system design.

---
*This report was generated from analysis of IETF working group session transcripts (vCon format) covering meetings 110-123.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `61316700-7ee6-41bc-b12f-a6f4f5707bbf` |
Sessions analyzed: 544 |
Generated: 2026-03-14*
