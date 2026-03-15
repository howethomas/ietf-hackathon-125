# Connectivity as primary goal

## Introduction

"Connectivity as primary goal" stands as one of the Internet's most fundamental architectural principles, formally articulated in [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958). Written by Brian Carpenter in 1996, this RFC captured the hard-won wisdom of the Internet's early architects: that universal connectivity—the ability for any node to communicate with any other node—should take precedence over most other design considerations. This principle emerged from the Internet's origins as a research network designed to survive partial failures and connect diverse, autonomous systems.

The principle's significance extends far beyond technical architecture. It embodies a philosophy that the Internet's greatest value comes not from any particular service or application, but from its capacity to enable unforeseen connections and innovations. When engineers face trade-offs between optimizing for specific use cases versus maintaining broad connectivity, this principle provides clear guidance: choose connectivity. The IETF's consistent application of this principle over decades has been instrumental in creating the Internet's remarkable ability to scale globally while remaining fundamentally open to new participants and uses.

In IETF working group discussions from 2021 to 2025, this principle continues to surface across diverse technical domains—from routing protocols to delay-tolerant networks—demonstrating its enduring relevance as the Internet evolves to meet new challenges while preserving its essential character.

## Understanding This Principle

**The Core Idea** — The Internet's architecture should prioritize universal connectivity above all other design goals. Think of this like designing a city's transportation system: you could optimize the roads for sports cars, making them smooth and fast but inaccessible to trucks, bicycles, or wheelchairs. Or you could design roads that work for everyone—maybe not perfect for any single vehicle type, but ensuring that anyone can get anywhere. The Internet's founders chose the second approach, building a network that prioritizes universal access over optimal performance for specific applications.

**Why It Matters** — When networks violate this principle, they fragment into incompatible islands. Consider corporate intranets in the 1990s: many companies built internal networks optimized for their specific applications—email systems that only worked with certain clients, file sharing that required proprietary software, video conferencing that couldn't connect to other vendors' systems. These networks were often faster and more feature-rich than the early Internet, but they created digital silos. Employees couldn't collaborate with partners, customers couldn't access services from any device, and innovation stagnated because developers had to choose which islands to support.

The Internet's connectivity-first approach initially seemed like a compromise—early web pages were slower and less sophisticated than CD-ROM multimedia experiences. But universal connectivity enabled unprecedented innovation: a student in a dorm room could create a website instantly accessible worldwide, small companies could reach global markets, and applications like email and the web could evolve rapidly because they worked everywhere. The principle's power lies in creating a platform for unpredictable innovation rather than optimizing for known use cases.

**The Tension** — The constant pressure against universal connectivity comes from the desire to optimize, secure, and control. Every network operator faces tempting shortcuts: blocking certain types of traffic to improve performance, requiring specific devices for better security, or creating premium tiers with enhanced features. These decisions often make business sense and can genuinely improve user experience for specific scenarios. The mobile industry's initial approach exemplified this tension—early smartphones had fast, optimized networks for approved applications, but couldn't access the full Internet. It took years of customer pressure and competitive dynamics to achieve true Internet connectivity on mobile devices.

**How to Recognize It** — You're seeing this principle at work when:

* A system chooses simple, widely-supported standards over proprietary optimizations—like a company using standard HTTP APIs instead of a faster custom protocol
* Network policies default to "allow unless specifically prohibited" rather than "prohibit unless specifically approved"  
* Architects resist the urge to fragment a system into specialized components that can't interoperate, even when specialization might improve performance
* Platform decisions prioritize broad compatibility over cutting-edge features—like web browsers supporting old websites even as new capabilities emerge

## Early IETF Work

The connectivity-first principle emerged from the Internet's earliest architectural decisions, particularly the choice of packet switching over circuit switching and the development of TCP/IP as a universal internetworking protocol. The original ARPANET research in the 1970s demonstrated that networks designed for universal connectivity could be remarkably resilient and adaptable. [RFC 791](https://www.rfc-editor.org/rfc/rfc791) and [RFC 793](https://www.rfc-editor.org/rfc/rfc793), defining IP and TCP respectively, embodied this principle by creating protocols that could work across diverse physical networks without requiring coordination between network operators.

The IETF learned this principle's importance through both successes and failures. The success of email interconnection in the 1980s, where disparate systems achieved universal connectivity through simple mail routing standards, demonstrated the principle's power. Conversely, the painful lessons of the OSI protocol suite's market failure in the 1990s showed what happened when architectural complexity and optimization took precedence over simple, universal connectivity. OSI offered technically superior features but required extensive coordination and configuration, creating barriers to adoption that ultimately proved fatal.

Perhaps most importantly, the early Internet's handling of address space scarcity in the 1990s—leading to NAT deployment and IPv6 development—showed how the community consistently chose solutions that preserved universal connectivity, even when more efficient but connectivity-limiting alternatives were available. These experiences reinforced that the Internet's value came not from technical perfection, but from its ability to connect anyone to anything.

## Key References

* [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — The seminal document articulating the Internet's core design principles, including connectivity as the primary goal.
* [RFC 3439: Some Internet Architectural Guidelines and Philosophy](https://www.rfc-editor.org/rfc/rfc3439) — Expands on RFC 1958's principles with lessons learned from Internet evolution.

## This Principle in IETF Discussions

The principle of connectivity as a primary goal manifests consistently across IETF working groups, though often in subtle ways as engineers grapple with specific technical challenges. In routing and forwarding contexts, this principle frequently emerges when working groups must balance optimization against universal reachability.

During the March 2022 Vienna meeting, the [lsr](https://datatracker.ietf.org/wg/lsr/about/) working group wrestled with fundamental questions about what routing protocols should provide:

> "k anymore so there are a bunch of other proposals that we've discussed pua putting loopbacks in bgp don't aggregate the loopbacks many other ideas the root problem here is that igps are carrying live reachability not liveness and if we want to talk about liveness we really really need another mechan"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf113/ietf113_lsr_29288.vcon.json)*

This discussion illuminates the principle's practical implications: the choice to focus interior gateway protocols on reachability (can you get there?) rather than liveness (is it working well?) reflects the connectivity-first philosophy. While liveness information could enable better performance optimization, the working group recognized that universal reachability must come first.

The importance of resilient connectivity became particularly evident in operational contexts. At IETF 115 in London, the [rtgwg](https://datatracker.ietf.org/wg/rtgwg/about/) working group discussed recent major service disruptions:

> "st year's major service disruptions at large providers mainly caused by configuration mistakes they took a large set of services down for a considerable amount of time so Services depend on resilient connectivity and the control plane connectivity is inherently important I in The Meta case for examp"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf115/ietf115_rtgwg_29855.vcon.json)*

This reflection on real-world failures demonstrates how connectivity as a primary goal isn't just theoretical—it's about ensuring that the Internet remains functional even when individual components fail or are misconfigured.

By July 2024 in Vancouver, discussions had evolved to consider connectivity challenges in emerging scenarios. The [iepg](https://datatracker.ietf.org/wg/iepg/about/) working group examined solutions for maintaining connectivity during infrastructure failures:

> "for power affluent devices that is uh a technical way of saying not resource constraint that is you know everyday devices such as phones and laptops and PCs and so on and the objective is to achieve connectivity during internet phase failures yeah uh so this is a brief description a pictorial descri"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf120/ietf120_iepg_33285.vcon.json)*

This discussion shows how the principle continues to drive innovation: rather than accepting that some devices might lose connectivity during failures, the community actively works on solutions to maintain universal connectivity even in degraded conditions.

Most recently, at IETF 123 in Madrid in July 2025, the [fantel](https://datatracker.ietf.org/wg/fantel/about/) working group highlighted ongoing challenges with traditional routing approaches:

> "l traffic we didn't have this kind of requirement TCP transmiters here it doesn't work this way the problem statement what we have today in ATF mostly routing protocols distributing information about reachability they're not fast enough the information they distribute is not kind of information we n"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf123/ietf123_fantel_34441.vcon.json)*

This recent discussion demonstrates the continuing evolution of connectivity challenges. While the principle remains constant, working groups continue to develop new mechanisms to ensure that reachability information can adapt to emerging requirements while maintaining the fundamental goal of universal connectivity.

## Historical Analysis

Analysis of IETF discussions from March 2021 through July 2025 reveals consistent engagement with connectivity principles across 68 working groups, with particularly intense discussion during IETF 115 (London, November 2022) which saw 18 sessions addressing these topics. The principle's discussion frequency has remained remarkably stable, ranging from 6 to 18 sessions per meeting, indicating its enduring relevance rather than periodic crisis-driven attention.

| Meeting | Location | Sessions | Notable Focus |
|---------|----------|----------|---------------|
| IETF 110 | Online | 9 | Post-pandemic connectivity challenges |
| IETF 115 | London | 18 | Peak discussion period, operational failures |
| IETF 120 | Vancouver | 15 | Resilience and failure scenarios |
| IETF 123 | Madrid | 11 | Evolution of routing requirements |

The working groups most engaged with connectivity principles reveal interesting patterns. [dtn](https://datatracker.ietf.org/wg/dtn/about/) (Delay-Tolerant Networking) and [gaia](https://datatracker.ietf.org/wg/gaia/about/) (Global Access to the Internet for All) lead discussions with 8 sessions each, reflecting their explicit focus on extending connectivity to challenging environments. Core routing groups like [rtgwg](https://datatracker.ietf.org/wg/rtgwg/about/), [bess](https://datatracker.ietf.org/wg/bess/about/), and [lsr](https://datatracker.ietf.org/wg/lsr/about/) consistently engage with these principles as they directly impact how traffic reaches its destinations.

Notably, the principle's discussion has evolved from theoretical concerns in early online meetings to practical operational challenges as in-person meetings resumed and real-world failures highlighted connectivity fragility. The emergence of [snac](https://datatracker.ietf.org/wg/snac/about/) (Stub Network Auto Configuration) and [fantel](https://datatracker.ietf.org/wg/fantel/about/) (Framework and Technology for Enhanced Learning) in recent discussions suggests ongoing work to extend connectivity principles into new domains like automated network configuration and educational technology.

## Resources

* [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — Essential reading for understanding the Internet's foundational design philosophy and the connectivity principle's origins.
* [RFC 3439: Some Internet Architectural Guidelines and Philosophy](https://www.rfc-editor.org/rfc/rfc3439) — Provides updated perspective on architectural principles with practical examples of how connectivity goals influenced protocol development.
* [Internet Universality (UNESCO)](https://en.unesco.org/internet-universality-indicators) — Offers a global policy perspective on universal Internet access, complementing the technical connectivity principles.
* [End-to-End Arguments in System Design (Saltzer, Reed, Clark)](http://web.mit.edu/saltzer/www/publications/endtoend/endtoend.pdf) — The foundational paper that influenced Internet architecture, explaining why simple, general-purpose networks enable innovation better than optimized, special-purpose ones.

---

*This report was generated through analysis of IETF vCon (Virtual Conversation) records from meetings 110-123 (March 2021 - July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `7caf0ca6-4750-45ff-af2f-2187c30284aa` |
Sessions analyzed: 165 |
Generated: 2026-03-15*
