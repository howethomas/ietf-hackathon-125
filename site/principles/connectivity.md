# Connectivity as primary goal

## Introduction

"Connectivity as primary goal" stands as one of the foundational principles of Internet architecture, formally articulated in [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) by Brian Carpenter in 1996. This principle asserts that the Internet's fundamental purpose is to enable universal connectivity—the ability for any device, anywhere in the network, to communicate with any other device. While this may seem obvious today, this principle represents a profound architectural choice that has shaped every aspect of how the Internet operates.

The principle emerged from the early Internet's design philosophy, where researchers prioritized building a network that could survive partial failures and connect diverse systems. Unlike traditional telecommunications networks that were optimized for specific services or controlled environments, the Internet was designed as a general-purpose communication substrate. This "connectivity-first" approach meant that the network's primary job was simply to deliver packets between endpoints, regardless of what applications were running or what types of devices were communicating.

In the IETF's ongoing work, this principle continues to influence protocol design, routing decisions, and architectural choices. As evidenced by discussions across 165 working group sessions from IETF 110-123, engineers regularly return to this foundational concept when evaluating new technologies, debugging network problems, and designing systems that must operate across the Internet's vast, heterogeneous infrastructure.

## Understanding This Principle

**The Core Idea**

The Internet exists primarily to connect things, not to control, optimize, or understand what flows between them.

Think of this principle like a city's road system. A well-designed transportation network doesn't care whether you're driving to work, visiting friends, delivering packages, or heading to the hospital—it simply provides reliable paths between any two points in the city. The road system doesn't optimize specifically for commuters at the expense of delivery trucks, or prioritize shopping trips over emergency vehicles. Instead, it focuses on one fundamental capability: ensuring that anyone can get from anywhere to anywhere else.

This might seem obvious, but it represents a profound design choice. The city could instead build specialized transportation systems—dedicated commuter rails, separate truck routes, emergency-only highways—that might be more efficient for specific purposes. But by prioritizing universal connectivity, the road system becomes a general-purpose platform that enables countless activities the planners never anticipated. Street food vendors, rideshare services, mobile clinics, and popup markets all become possible because the basic infrastructure simply connects places without prejudging how those connections will be used.

**Why It Matters**

When networks prioritize connectivity, they become platforms for innovation. When they prioritize control or optimization, they become constraints.

Consider what happened with early telephone networks versus the Internet. Telephone networks were brilliantly optimized—for voice calls between two parties. They provided excellent audio quality, reliable connections, and sophisticated features like call waiting and conferencing. But their optimization for voice made them terrible platforms for data. When people wanted to use modems for computer communication, they had to work around the telephone network's assumptions about what "communication" meant. The network's focus on optimizing voice calls made it nearly impossible to innovate new services.

The Internet took the opposite approach. Instead of optimizing for any particular application, it focused purely on moving packets between addresses. This made early Internet services arguably worse than their specialized alternatives—email was less reliable than postal mail, early voice over IP was lower quality than telephone calls, and web browsing was slower than dedicated information systems. But because the network prioritized connectivity over optimization, it became a platform where anyone could experiment with new applications without asking permission or redesigning the infrastructure.

**The Tension**

The relentless pressure to optimize creates constant temptation to abandon universal connectivity in favor of specialized solutions.

Network operators face real costs and constraints: bandwidth is expensive, latency matters for user experience, and security threats require active management. It's always tempting to improve performance by treating different types of traffic differently—prioritizing video streams over file downloads, blocking suspicious connections, or optimizing routes for major customers. Each of these optimizations makes sense in isolation and can deliver measurable improvements.

But every optimization away from universal connectivity reduces the network's potential as a platform. When ISPs throttle certain applications, those applications can't compete fairly with alternatives. When networks block or redirect traffic, new services can't reach users. When routing prioritizes some destinations over others, innovation becomes concentrated in privileged locations. The pressure to optimize is constant and rational, but it gradually transforms a general-purpose platform into a collection of special-purpose services.

**How to Recognize It**

You're seeing this principle at work when networks treat unknown traffic the same as known traffic—forwarding packets based on addresses rather than contents or assumptions about what applications are running. You see it when routing protocols focus on reachability rather than optimization, ensuring every destination is reachable even if not every path is optimal. You recognize it in organizational decisions when teams choose general-purpose solutions that "work everywhere" over specialized solutions that "work better in our specific environment." The principle shows up whenever engineers ask "how do we make this work across the entire Internet?" rather than "how do we make this work perfectly in our controlled environment?"

## Key References

- [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — The foundational document articulating connectivity as the Internet's primary goal
- [End-to-End Arguments in System Design](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf) — Saltzer, Reed, and Clark's seminal paper on why networks should focus on basic connectivity

## This Principle in IETF Discussions

The principle of connectivity as a primary goal manifests throughout IETF working group discussions, often emerging when engineers grapple with fundamental questions about reachability, routing, and network resilience.

In the BESS working group sessions, connectivity concerns appear when designing multi-domain EVPN services:

> "m going to talk about a short refresh changes that we've made in version zero one and next steps next slide please the uh the draft um in the introduction talks about different ways of uh having interconnectivity across domains for evpm vpws services it talks about three different solutions which ar"

This discussion from IETF 115 illustrates how even advanced networking services must grapple with the fundamental challenge of maintaining connectivity across different administrative domains—a direct application of the universal connectivity principle.

The routing working group (RTGWG) explicitly connected connectivity to service reliability during discussions about major provider outages:

> "st year's major service disruptions at large providers mainly caused by configuration mistakes they took a large set of services down for a considerable amount of time so Services depend on resilient connectivity and the control plane connectivity is inherently important I in The Meta case for examp"

This IETF 115 discussion demonstrates how connectivity isn't just an abstract principle—it directly impacts service availability. When connectivity fails, everything built on top of the network fails with it.

In the LSR working group, engineers debated the distinction between reachability and liveness, highlighting a key tension in maintaining universal connectivity:

> "k anymore so there are a bunch of other proposals that we've discussed pua putting loopbacks in bgp don't aggregate the loopbacks many other ideas the root problem here is that igps are carrying live reachability not liveness and if we want to talk about liveness we really really need another mechan"

This IETF 113 conversation reveals how routing protocols must balance the need to advertise reachability (supporting universal connectivity) with the need to respond quickly to failures (maintaining practical connectivity).

The FANTEL working group's discussions about ATF routing protocols showed how traditional approaches may be insufficient for emerging connectivity requirements:

> "l traffic we didn't have this kind of requirement TCP transmiters here it doesn't work this way the problem statement what we have today in ATF mostly routing protocols distributing information about reachability they're not fast enough the information they distribute is not kind of information we n"

This IETF 123 excerpt illustrates how new applications and network conditions challenge existing approaches to maintaining connectivity, forcing engineers to reconsider how the principle applies in practice.

## Historical Analysis

Analysis of IETF discussions from March 2021 to July 2025 reveals consistent engagement with connectivity principles across all 14 meetings, with notable variation in intensity:

| Meeting | Sessions | Notable Focus Areas |
|---------|----------|-------------------|
| IETF 110-112 (2021) | 26 total | Post-pandemic connectivity challenges |
| IETF 113-115 (2022) | 45 total | Peak discussion period, routing resilience |
| IETF 116-118 (2023) | 34 total | Multi-domain connectivity solutions |
| IETF 119-123 (2024-2025) | 60 total | Emerging network technologies |

The highest concentration of discussions occurred during IETF 115 (London, November 2022) with 18 sessions, coinciding with industry focus on network resilience following several high-profile outages. The DTN and GAIA working groups led discussions with 8 sessions each, reflecting the principle's particular relevance to delay-tolerant networks and global Internet architecture research.

The routing-focused working groups (RTGWG, LSR, IDR) collectively contributed 17 sessions, emphasizing how fundamental routing decisions directly implement the connectivity principle. Interestingly, newer working groups like SNAC (Secure Network Access Control) contributed 6 sessions, showing how even security-focused protocols must grapple with maintaining connectivity while adding protection mechanisms.

The consistent presence of connectivity discussions across all meetings and the wide distribution across 68 working groups demonstrates that this principle remains actively relevant to IETF work, not merely a historical artifact. The principle appears to be most actively discussed during periods of network stress or when designing systems that must operate across diverse network conditions.

## Resources

- [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — The definitive statement of Internet architectural principles including connectivity as primary goal
- [End-to-End Arguments in System Design](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf) — Essential paper explaining why network functions should be kept simple to preserve connectivity
- [Internet Universality Indicators (UNESCO)](https://en.unesco.org/internet-universality-indicators) — Framework for understanding universal Internet access and connectivity from a policy perspective
- [The Design Philosophy of the DARPA Internet Protocols](https://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf) — David Clark's seminal paper on Internet design goals and the prioritization of connectivity
- [RFC 3439: Some Internet Architectural Guidelines and Philosophy](https://www.rfc-editor.org/rfc/rfc3439) — Updates and expansions on architectural principles including connectivity considerations

---
*This report was generated from analysis of IETF working group session transcripts using vCon (virtual Conversation) data from meetings 110-123 (March 2021 - July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `7caf0ca6-4750-45ff-af2f-2187c30284aa` |
Sessions analyzed: 165 |
Generated: 2026-03-14*
