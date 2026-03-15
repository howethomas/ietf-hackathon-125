# End-to-end principle

## Introduction

The end-to-end principle stands as one of the foundational architectural principles of the Internet, asserting that intelligence should reside at the network's endpoints rather than in the network infrastructure itself. First articulated by J.H. Saltzer, D.P. Reed, and D.D. Clark in their seminal 1984 paper ["End-to-End Arguments in System Design"](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf), this principle fundamentally shaped how the Internet was designed and continues to influence protocol development today.

The principle's core insight is deceptively simple: functions can only be correctly and completely implemented with the knowledge and help of the application standing at the endpoints of the communication system. This philosophy was formally adopted by the IETF in [RFC 1958](https://www.rfc-editor.org/rfc/rfc1958) as one of the architectural principles of the Internet, and later examined in detail in [RFC 3724](https://www.rfc-editor.org/rfc/rfc3724), which explored how this principle evolved as networks grew more complex.

The end-to-end principle matters because it defines a fundamental division of labor in network design. It argues against placing application-specific functionality within the network infrastructure, instead advocating for a simple, general-purpose network that provides basic connectivity while leaving complex, application-specific logic to the endpoints. This architectural choice has enabled the Internet's remarkable innovation and scalability, allowing new applications to flourish without requiring changes to the underlying network infrastructure.

## Understanding This Principle

**The Core Idea**

Intelligence should live at the edges, not in the middle. Think of the end-to-end principle like a highway system. The roads themselves don't need to know whether you're driving to a wedding, a grocery store, or a hospital—they just provide reliable transportation infrastructure. All the specialized knowledge about your destination, route preferences, and cargo stays with you, the driver. The highway's job is simply to get you from point A to point B safely and efficiently.

This analogy captures why the end-to-end principle exists: specialization and flexibility. Just as highways become more useful when they serve many different types of travelers without favoring any particular trip purpose, networks become more powerful when they provide general-purpose connectivity without embedding assumptions about specific applications. If highways had to understand every possible journey type—with special lanes for wedding parties, different speed limits for grocery runs, and mandatory stops for medical emergencies—they would become impossibly complex and couldn't adapt to new travel needs.

In networking terms, this means the network infrastructure (routers, switches, and transmission systems) should focus on delivering packets reliably, while applications (web browsers, video calls, email) handle their own specific requirements for security, reliability, and functionality.

**Why It Matters**

When this principle is violated, systems become brittle and innovation stalls. Consider email as a concrete example. Early email systems often embedded delivery logic, message formatting, and even user interface decisions into the network infrastructure itself. Each network had its own email format and delivery mechanisms. This meant that sending email between different networks required complex gateways that understood multiple email formats, and adding new email features required updating network infrastructure.

The Internet's approach followed the end-to-end principle instead. The network simply delivers packets containing email data, while email applications at the endpoints handle message composition, encryption, spam filtering, and user interfaces. This separation allowed email innovation to flourish—we got rich HTML emails, attachment handling, mobile email clients, and advanced spam filtering without requiring any changes to routers or network protocols. A network operator doesn't need to understand or upgrade their equipment when someone invents a new email feature.

The contrast is stark: violating the end-to-end principle creates a system where every new application feature requires coordinated updates across network infrastructure, while following it enables rapid innovation at the application layer without network changes.

**The Tension**

The real-world pressure against this principle is compelling: putting intelligence in the network often seems like the obvious solution. Network operators can see all the traffic, have control over performance, and can potentially optimize in ways that individual applications cannot. Why not add video compression to routers to improve streaming performance? Why not build spam filtering into email servers? Why not optimize web traffic at the network level?

This temptation is particularly strong when facing performance problems or security challenges. Network operators think, "I can see this inefficient behavior across thousands of applications—surely I can fix it better than each application can fix it individually." The appeal of centralized optimization and control is powerful, especially when individual applications seem to be making suboptimal choices.

The pressure intensifies with business incentives. Telecommunications companies and internet service providers often want to offer "value-added services" that differentiate their networks. Cloud providers want to offer network-level optimizations. Equipment vendors want to sell more sophisticated, feature-rich network devices.

**How to Recognize It**

You're seeing the end-to-end principle at work when:

* A platform provides simple, general-purpose APIs rather than building specific features for each use case—like how cloud storage offers basic read/write operations instead of specialized interfaces for photos, documents, and backups
* A system pushes complexity to the edges—like how the web allows browsers to handle different content types (video, documents, interactive apps) rather than requiring web servers to understand each format
* New capabilities can be added without changing core infrastructure—like how smartphone app stores enable thousands of new applications without requiring cellular network upgrades

## Early IETF Work

The Internet's design fundamentally embodied the end-to-end principle from its earliest days, distinguishing it from the more centralized telecommunications networks of the era. The decision to implement TCP at the endpoints rather than in the network infrastructure was a crucial early application of this principle. While telephone networks managed connection state and reliability guarantees within their switching infrastructure, the Internet pushed these functions to the endpoints, allowing the network layer (IP) to remain stateless and focused solely on packet delivery.

This architectural choice proved prescient during the development of the Domain Name System (DNS) in the 1980s. Rather than embedding name resolution logic throughout the network infrastructure, [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034) and [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035) established a distributed system where endpoints perform their own name lookups using specialized DNS servers. This allowed naming policies and resolution strategies to evolve independently of routing infrastructure.

However, the IETF community also learned through experience about the challenges of maintaining this principle. Network Address Translation (NAT), while solving practical IPv4 address shortage problems, represented a significant departure from end-to-end connectivity. The complexity and application compatibility issues that NAT introduced served as a cautionary tale about the costs of violating end-to-end principles, ultimately motivating many of the design choices in IPv6 and influencing ongoing discussions about network architecture in IETF working groups today.

## Key References

* [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — The foundational IETF document establishing the end-to-end principle as a core Internet architectural principle
* [RFC 3724: The Rise of the Middle and the Future of End-to-End](https://www.rfc-editor.org/rfc/rfc3724) — An examination of how the end-to-end principle has evolved and the pressures against it in modern networks
* [End-to-End Arguments in System Design](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf) — The original 1984 paper by Saltzer, Reed, and Clark that articulated the fundamental concepts

## This Principle in IETF Discussions

The end-to-end principle continues to generate active discussion across IETF working groups, particularly as new networking paradigms challenge traditional assumptions. In the [babel](https://datatracker.ietf.org/wg/babel/about/) working group during IETF 110, participants grappled with how protocol designs could inadvertently violate the principle:

> "this protocol breaks the main properties of it breaks the main properties of the end-to-end principle so okay i've already said that next please okay so what is the problem well with"

This concern about maintaining end-to-end properties reflects ongoing vigilance in the routing community about preserving fundamental architectural principles even as protocols evolve to meet new requirements.

Research groups have been particularly active in exploring the boundaries and evolution of this principle. The [coinrg](https://datatracker.ietf.org/wg/coinrg/about/) working group has extensively examined how computing in the network relates to traditional end-to-end arguments. During IETF 115, they explicitly addressed this tension:

> "had had at this research group earlier and what we now try to do is basically um yeah have a bit more thoughts on how we can actually combine or what is the interplay between transport protocols the end-to-end principle and Computing in the network"

This discussion represents a significant evolution in how the IETF community thinks about the principle—not as an absolute rule, but as a design consideration that must be balanced against other architectural goals like performance and efficiency.

The [dinrg](https://datatracker.ietf.org/wg/dinrg/about/) working group has taken a more critical perspective, questioning whether traditional principles still hold in today's Internet. During IETF 115, they observed:

> "drives the user base up and that builds the economy of scale in today's internet the result is really a flattening of the traditional topology of the internet what we've got is a situation where the end-to-end principle isn't really the principle that's at work here"

This observation reflects a mature recognition that the Internet's evolution has created new realities that challenge traditional architectural assumptions.

By IETF 122, discussions in [dinrg](https://datatracker.ietf.org/wg/dinrg/about/) had evolved toward considering how to reestablish end-to-end principles in future systems:

> "the second thing is also bit aligned to what we discussed here before is to um kind of reinstalling the end to end principle for future application development so um um Foster development on um application"

This progression from questioning the principle's relevance to actively considering its restoration demonstrates the IETF community's ongoing engagement with fundamental architectural questions.

## Historical Analysis

Discussion of the end-to-end principle across IETF meetings 110-123 reveals several interesting patterns in how the community approaches this foundational concept:

| Meeting Period | Discussion Frequency | Key Themes |
|---|---|---|
| Early (110-114) | High activity (22 sessions) | Principle violations and preservation |
| Middle (115-119) | Peak activity (25 sessions) | Research into computing-in-network tensions |
| Recent (120-123) | Declining activity (9 sessions) | Focus on restoration and future applications |

The data shows that research groups dominate these discussions, with [dinrg](https://datatracker.ietf.org/wg/dinrg/about/) leading with 7 sessions, followed by [dtn](https://datatracker.ietf.org/wg/dtn/about/), [nmrg](https://datatracker.ietf.org/wg/nmrg/about/), and [coinrg](https://datatracker.ietf.org/wg/coinrg/about/) each contributing 3-4 sessions. This concentration in research groups suggests the community is actively exploring how traditional principles apply to emerging networking paradigms rather than simply applying established doctrine.

The temporal pattern is particularly revealing. The peak discussion period (IETF 115-118) coincided with significant industry interest in edge computing, 5G networks, and computing-in-network approaches—all of which challenge traditional end-to-end assumptions. The recent decline in discussion frequency may indicate either that the community has reached some consensus on how to balance these competing considerations, or that attention has shifted to more concrete protocol work informed by these architectural discussions.

Notably, security-focused groups like [secdispatch](https://datatracker.ietf.org/wg/secdispatch/about/) and [ace](https://datatracker.ietf.org/wg/ace/about/) also appear in the discussion list, suggesting that end-to-end principles remain relevant to authentication and authorization architecture as distributed systems become more complex.

## Resources

* [End-to-End Principle (Wikipedia)](https://en.wikipedia.org/wiki/End-to-end_principle) — Comprehensive overview with additional examples and critiques of the principle
* [RFC 3724: The Rise of the Middle](https://www.rfc-editor.org/rfc/rfc3724) — Essential reading for understanding how middleboxes and network services have challenged traditional end-to-end assumptions
* [IETF Architectural Principles of the Internet (RFC 1958)](https://www.rfc-editor.org/rfc/rfc1958) — The complete set of architectural principles that guide Internet protocol development, providing context for how end-to-end arguments fit within broader design philosophy
* [RFC 8981: The Use of the IP Precedence Field in the TCP Header](https://www.rfc-editor.org/rfc/rfc8981) — Referenced in discussions as an example of how end-to-end arguments influence specific protocol design decisions

---

*This report was generated from analysis of IETF working group session transcripts using vCon (Virtual Conversation) data spanning meetings 110-123 (March 2021 - July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `317f8ebe-3225-45da-8907-8704b0027aab` |
Sessions analyzed: 56 |
Generated: 2026-03-14*
