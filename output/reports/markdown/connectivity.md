# Connectivity as primary goal

## Introduction

"Connectivity as primary goal" stands as perhaps the most fundamental principle underlying the Internet's architecture. Formalized in [RFC 1958](https://www.rfc-editor.org/rfc/rfc1958), Brian Carpenter's seminal 1996 document on "Architectural Principles of the Internet," this principle declares that the Internet's primary purpose is to enable universal connectivity between any two endpoints, regardless of their location, technology, or administrative domain.

This principle emerged from the Internet's origins as a research network designed to survive partial failures and connect disparate computing systems. Unlike traditional telecommunications networks that prioritized specific services or performance guarantees, the Internet was built on the radical premise that getting packets from any source to any destination was more important than how efficiently or predictably they arrived. This connectivity-first philosophy enabled the Internet's explosive growth from a handful of university computers to a global network connecting billions of devices.

The principle continues to guide IETF protocol development today, influencing decisions about routing protocols, addressing schemes, and network architectures. It serves as a north star when engineers face trade-offs between connectivity and other desirable properties like performance, security, or efficiency. Understanding this principle is crucial for anyone working on Internet protocols, as it explains why certain design patterns persist and why proposals that limit connectivity face heightened scrutiny in IETF discussions.

## Understanding This Principle

**The Core Idea** — The Internet should prioritize getting any message to any destination over all other concerns, including speed, efficiency, or elegance.

Think of this like a postal system designed by someone who lived through multiple wars and natural disasters. Most postal services optimize for speed and cost — they want to deliver letters quickly and cheaply along well-established routes between major cities. But imagine designing a postal system where the primary goal isn't speed or cost, but ensuring that any letter can eventually reach any address, even if the roads are bombed, the trains aren't running, and half the post offices are closed.

This hypothetical postal system would have multiple backup routes for every destination. It would accept letters in any format — handwritten notes, formal documents, packages, messages carved on wooden blocks. Postal workers would be trained to improvise when standard procedures fail: if the main road to a town is blocked, they'd find hiking trails, boat routes, or even carrier pigeons. The system might be slower and more expensive than a conventional postal service, but it would be nearly impossible to completely cut off communication to any location.

This is the Internet's fundamental philosophy. Every other network property — speed, cost, security, quality of service — comes second to the basic goal of universal reachability.

**Why It Matters** — When you violate this principle, you create islands of connectivity that fragment the Internet's global reach.

Consider two real-world examples. In the 1980s and 1990s, many companies deployed proprietary networking protocols — IBM's SNA, Novell's IPX, Digital's DECnet — that worked beautifully within their own ecosystems but couldn't communicate with each other. Each created fast, efficient networks that served their specific communities well. However, connecting these islands required expensive gateways, complex translations, and often simply didn't work. Users faced a world where their computer could talk to some machines but not others, based on arbitrary technical decisions made years earlier.

Contrast this with the Internet's approach: TCP/IP wasn't the fastest or most elegant protocol available, but it prioritized universal connectivity. Any device implementing TCP/IP could, in principle, communicate with any other TCP/IP device. This connectivity-first design enabled explosive growth because new networks could join the Internet without asking permission or implementing complex gateway technologies.

**The Tension** — The pressure against this principle comes from the desire to optimize for specific use cases or business models.

It's tempting to design networks that work exceptionally well for particular applications, geographies, or customers. A video streaming service might want to prioritize its traffic over email. A company might want to optimize its network for internal applications while treating external traffic as second-class. A government might want to create a faster, more secure network for its citizens while limiting international connectivity.

These optimizations often make technical and business sense in isolation. They can improve performance, reduce costs, enhance security, and serve specific communities better than a general-purpose network. The problem is that each optimization creates boundaries — places where connectivity stops working. Over time, these boundaries accumulate and fragment the network into incompatible pieces.

**How to Recognize It** — You're seeing this principle at work when:

- A network protocol includes multiple fallback mechanisms that sacrifice efficiency to maintain connectivity during failures
- System architects choose standards-based solutions over proprietary ones, even when the proprietary option offers better performance
- Organizations invest in redundant network paths and diverse routing options rather than optimizing a single high-performance connection
- Protocol designers add complexity to ensure their system can interoperate with older or different technologies
- Engineers resist adding features that would prevent their system from working with future, unknown protocols or applications

## Early IETF Work

The connectivity principle emerged from hard-won experience during the Internet's formative years. The original ARPANET was designed in the late 1960s with connectivity as an explicit goal — researchers wanted to create a network that could survive nuclear attacks by routing around damaged nodes. This military requirement established the philosophical foundation that connectivity trumped efficiency.

Throughout the 1980s and 1990s, the IETF community learned this lesson repeatedly through protocol failures. Early attempts to create "better" Internet protocols — ones optimized for speed, security, or specific applications — often failed to gain adoption precisely because they sacrificed connectivity for other goals. The OSI protocol suite, despite significant technical advantages and international standardization efforts, couldn't overcome TCP/IP's installed base and universal connectivity. Similarly, various attempts to create separate "quality of service" networks or application-specific protocols foundered when they required users to choose between better performance and broader connectivity.

[RFC 1958](https://www.rfc-editor.org/rfc/rfc1958) crystallized these experiences into explicit architectural principles, with connectivity listed first among the Internet's core design goals. The document acknowledged that this principle sometimes conflicts with other desirable properties, but argued that connectivity's primacy was essential to the Internet's success and should guide future protocol development.

## Key References

- [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — The foundational document that codified connectivity as the Internet's primary architectural principle.

## This Principle in IETF Discussions

The principle of connectivity as a primary goal appears consistently across IETF working group discussions, manifesting in various technical contexts from routing protocols to specialized networks.

Early in the analyzed period, the [bess](https://datatracker.ietf.org/wg/bess/about/) working group grappled with connectivity challenges in virtual private networks. During IETF 113 in Vienna (March 2022), participants discussed scenarios involving IPv4 and IPv6 connectivity over single-stack networks:

> "ec edge scenario where we have an ipv4 and ipv6 mlri uh from a control plane perspective they're they're being carried over a single v6 only pier uh and we're forwarding v4 and v6 and we have end end reachability cdc um and we're using the default uh per cd label allocation um we've tested with a v4"

This discussion exemplifies the principle in practice — engineers designing solutions that maintain end-to-end reachability across different protocol families, even when the underlying infrastructure supports only newer protocols.

The [lsr](https://datatracker.ietf.org/wg/lsr/about/) working group at the same meeting highlighted a fundamental tension between connectivity and liveness detection:

> "k anymore so there are a bunch of other proposals that we've discussed pua putting loopbacks in bgp don't aggregate the loopbacks many other ideas the root problem here is that igps are carrying live reachability not liveness and if we want to talk about liveness we really really need another mechan"

This quote illustrates how routing protocols prioritize reachability information over performance optimization, embodying the connectivity-first principle even when it creates technical challenges.

By the middle period, discussions had evolved to address service resilience. The [rtgwg](https://datatracker.ietf.org/wg/rtgwg/about/) working group at IETF 115 in London (November 2022) examined real-world connectivity failures:

> "st year's major service disruptions at large providers mainly caused by configuration mistakes they took a large set of services down for a considerable amount of time so Services depend on resilient connectivity and the control plane connectivity is inherently important I in The Meta case for examp"

This discussion connected the abstract principle to concrete business impacts, showing how connectivity failures affect large-scale services and reinforcing why connectivity remains paramount.

More recent discussions have extended the principle to emerging technologies. The [iepg](https://datatracker.ietf.org/wg/iepg/about/) working group at IETF 120 in Vancouver (July 2024) explored connectivity during network failures:

> "for power affluent devices that is uh a technical way of saying not resource constraint that is you know everyday devices such as phones and laptops and PCs and so on and the objective is to achieve connectivity during internet phase failures yeah uh so this is a brief description a pictorial descri"

This represents an evolution of the principle — not just maintaining connectivity under normal conditions, but ensuring it persists during infrastructure failures, extending the original resilience goals to modern device ecosystems.

The most recent discussions show the principle adapting to new protocol contexts. The [fantel](https://datatracker.ietf.org/wg/fantel/about/) working group at IETF 123 in Madrid (July 2025) noted limitations in current reachability mechanisms:

> "l traffic we didn't have this kind of requirement TCP transmiters here it doesn't work this way the problem statement what we have today in ATF mostly routing protocols distributing information about reachability they're not fast enough the information they distribute is not kind of information we n"

This suggests ongoing evolution in how the connectivity principle is implemented, with working groups seeking faster, more responsive methods to maintain reachability in modern networks.

## Historical Analysis

Analysis of discussion frequency across IETF meetings reveals sustained attention to connectivity principles throughout the surveyed period:

| Meeting | Date | Discussions |
|---------|------|------------|
| IETF 110 | March 2021 | 9 |
| IETF 115 | November 2022 | 18 |
| IETF 120 | July 2024 | 15 |
| IETF 123 | July 2025 | 11 |

The peak at IETF 115 (18 discussions) coincided with increased focus on network resilience following several high-profile Internet outages in 2022. This pattern suggests the principle gains prominence during periods when connectivity failures highlight its importance.

The [dtn](https://datatracker.ietf.org/wg/dtn/about/) and [gaia](https://datatracker.ietf.org/wg/gaia/about/) working groups lead in discussion frequency (8 sessions each), reflecting their focus on challenged networks and global access respectively. The [rtgwg](https://datatracker.ietf.org/wg/rtgwg/about/), [bess](https://datatracker.ietf.org/wg/bess/about/), and [snac](https://datatracker.ietf.org/wg/snac/about/) working groups follow closely, indicating that routing and network connectivity discussions consistently invoke this principle.

The broad distribution across 68 working groups demonstrates the principle's universal relevance in IETF work. From specialized groups like [icnrg](https://datatracker.ietf.org/wg/icnrg/about/) exploring future Internet architectures to established areas like [6man](https://datatracker.ietf.org/wg/6man/about/) maintaining IPv6 connectivity, the principle influences protocol development across all technology domains.

## Resources

- [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — Essential reading for understanding how connectivity became the Internet's primary design principle.
- [Internet Universality (UNESCO)](https://en.unesco.org/internet-universality-indicators) — Explores the policy and social implications of universal Internet connectivity.
- [End-to-End Arguments in System Design](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf) — Classic paper by Saltzer, Reed, and Clark that influenced Internet architecture principles.

---
*This report was generated from analysis of IETF working group session transcripts using vCon (Conversation Data Container) format.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `7caf0ca6-4750-45ff-af2f-2187c30284aa` |
Sessions analyzed: 165 |
Generated: 2026-03-14*
