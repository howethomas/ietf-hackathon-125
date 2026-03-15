# Fate sharing

## Introduction

Fate sharing is one of the Internet's most fundamental architectural principles, codified in [RFC 1958](https://www.rfc-editor.org/rfc/rfc1958) as part of the core design philosophy that has guided Internet protocol development for decades. The principle states that "related parts of a system fail together" and that "state should be maintained only at endpoints." This seemingly simple rule has profound implications for how we build distributed systems that can survive failures and scale across the globe.

The concept emerged from the early work of Internet pioneers like David Clark, whose seminal 1988 paper "[The Design Philosophy of the DARPA Internet Protocols](http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf)" articulated the fundamental trade-offs that shaped the Internet's architecture. Fate sharing was born from hard-won experience with earlier network architectures that failed catastrophically when critical intermediate components went down, taking entire systems with them.

In IETF working groups today, fate sharing continues to be a touchstone for protocol design decisions. As our analysis of IETF meetings 110-123 (March 2021 to July 2025) shows, this principle was discussed in 544 sessions across 141 working groups, demonstrating its enduring relevance as the Internet evolves to support new applications, from IoT devices to quantum networking.

## Understanding This Principle

**The Core Idea** — If two parts of a system depend on each other to work, they should fail together rather than independently. Think of it like a restaurant kitchen: instead of having one shared grill that serves all tables (where a grill failure kills everyone's orders), each cooking station has its own equipment, so when something breaks, only that station's customers are affected, not the entire restaurant.

This analogy reveals why fate sharing exists: it's about containing failures and avoiding mysterious, hard-to-debug problems. When the shared grill breaks, customers don't understand why their food isn't coming — the failure is invisible to them, and the restaurant staff has to manage the complex problem of redistributing orders or rebuilding shared state. But when each station's equipment fails independently, the impact is localized and the problem is obvious.

**Why It Matters** — When you violate fate sharing, you create hidden dependencies that turn small failures into big disasters. Consider the difference between two email systems: one that stores all user sessions on a central server versus one that keeps session state in the client. In the centralized system, if the session server goes down, every user loses their login state simultaneously, even though the mail servers are still running. Users see a confusing failure: they can't access email, but the service appears to be "up." 

In the fate-sharing design, if a user's device crashes, only that user loses their session — and they understand why (their device rebooted). The failure is obvious and contained. More importantly, when the email service itself fails, users naturally lose access, which is the expected behavior. The failures are aligned with user expectations rather than creating mysterious partial failures.

**The Tension** — The real-world pressure against fate sharing is efficiency and resource sharing. Centralized state often seems more efficient: one shared cache serves everyone, one connection pool handles all requests, one coordinator manages all transactions. It's tempting to build shared infrastructure because it reduces resource usage and can seem easier to manage. Organizations often prefer centralized control because it feels more manageable and observable.

This efficiency argument is seductive but often false economy. Shared state requires complex coordination protocols, failure recovery mechanisms, and creates single points of failure that demand expensive high-availability solutions. The "simpler" centralized design becomes vastly more complex when you account for all the failure handling it requires.

**How to Recognize It** — You're seeing fate sharing at work when:

- A web application stores session data in browser cookies rather than server-side databases, so user sessions survive server restarts
- Microservices avoid shared databases, even though it means duplicating some data, because they want service failures to be independent
- Your team chooses to replicate configuration data to each server rather than having all servers query a central config service
- A distributed system puts related data on the same physical machine, accepting that both pieces fail together rather than trying to spread them across different failure domains

## Early IETF Work

The Internet's original design embodied fate sharing through its radical architectural choice: making the network itself stateless and pushing all intelligence to the endpoints. This was a deliberate rejection of the telephone network model, where circuit switches maintained connection state and a single switch failure could break thousands of calls. Early Internet protocols like TCP deliberately maintained connection state only at the communicating hosts, allowing packets to flow through any available path and making the core network much more resilient to individual router failures.

However, the principle wasn't always perfectly applied. Early routing protocols like RIP and some of the initial multicast designs created shared state in the network that violated fate sharing principles. The painful lessons learned from these designs — where network state could become inconsistent or where single points of failure emerged — helped reinforce the principle's importance. The development of BGP and later routing protocols showed how to build distributed coordination while respecting fate sharing: each router maintains its own view of the network topology, and failures are contained rather than cascading.

Perhaps the most instructive early example was the contrast between connection-oriented network layer proposals (like X.25) and the Internet's connectionless IP design. X.25 networks maintained per-connection state in intermediate nodes, creating fate sharing violations that made the network fragile and complex to manage. The Internet's choice to keep network layer stateless, despite seeming "inefficient," proved its wisdom through decades of robust operation.

## Key References

- [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — The foundational document codifying Internet architectural principles including fate sharing
- [The Design Philosophy of the DARPA Internet Protocols](http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf) — David Clark's seminal 1988 paper explaining the engineering trade-offs that shaped Internet architecture
- [Fate-sharing (Wikipedia)](https://en.wikipedia.org/wiki/Fate-sharing) — Accessible overview with examples from various distributed systems contexts

## This Principle in IETF Discussions

Fate sharing discussions in recent IETF meetings reveal how this principle continues to guide protocol design decisions across diverse working groups. The conversations show engineers grappling with when to share state versus when to keep it separate, often in the context of new technologies that challenge traditional assumptions.

In the [babel](https://datatracker.ietf.org/wg/babel/about/) working group during IETF 110, participants discussed a clear violation of fate sharing:

> "agmentation required packets are going to fail to reach the sending host and you're going to have mysterious failures where some things work and then get stuck so the problem here is that you have no fate sharing between the data between on the one hand the date and act pass and on the other hand th"

This excerpt illustrates the classic fate sharing problem: when path discovery and data transmission use different mechanisms, you get "mysterious failures" where some things work but others don't. The failure modes aren't aligned, creating the kind of hard-to-debug problems that fate sharing is designed to prevent.

The principle surfaces regularly in security contexts, as seen in [ipsecme](https://datatracker.ietf.org/wg/ipsecme/about/) discussions during IETF 119:

> "is different it's native as extension header so basic IPv6 header will just indicate that inside we have as extension header and everything else is hidden it actually has some advantages uh if ESP is stateless allow through your uh filtering then you don't need you don't need any keep Al lives if th"

This conversation touches on a key fate sharing benefit: when security state is stateless (no shared state in intermediate nodes), you eliminate the need for keepalive mechanisms and the associated failure modes. The security processing fails or succeeds with the packet itself, rather than depending on separate state management.

Storage and state management challenges appear across multiple working groups. In [6lo](https://datatracker.ietf.org/wg/6lo/about/) during IETF 120, engineers discussed how to handle device restarts:

> "good point uh about the usage of nonvolatile memory because like in other documents um if by any chance uh a node restarts so basically what it does it checks in the nonvolatile memory if he has some State he can re-register okay so the text has been um updated in a few places in order to to uh cons"

This reflects the ongoing tension in IoT contexts between fate sharing (where device state should disappear with device failure) and practical concerns about recovery time and user experience. The solution being discussed — storing minimal state locally for faster recovery — represents a careful balance that maintains fate sharing principles while addressing operational needs.

Emerging protocols continue to wrestle with these trade-offs. A [moq](https://datatracker.ietf.org/wg/moq/about/) discussion from IETF 115 showed concerns about protocol complexity:

> "otocol from three dropped but there is a lot of things in quick cards missing here I think the pop sub relationship and they use Quick datagram and for the pub sub I think maybe it can bring a lot of State in the Renee I think that's why you drop it"

This conversation reveals how fate sharing concerns influence protocol design decisions. The worry about "a lot of State in the Renee" (relay) reflects classic fate sharing thinking: putting state in intermediate nodes creates complexity and failure modes that violate the principle.

## Historical Analysis

Analysis of fate sharing discussions across IETF 110-123 reveals interesting patterns in how the principle is applied to emerging technologies. The frequency of discussions has remained relatively stable, with a notable spike in IETF 123 (Madrid, July 2025) suggesting renewed focus as new architectural challenges emerge.

| Meeting | Date | Location | Sessions |
|---------|------|----------|----------|
| IETF 110 | March 2021 | Online | 33 |
| IETF 115 | November 2022 | London | 51 |
| IETF 116 | March 2023 | Yokohama | 48 |
| IETF 123 | July 2025 | Madrid | 61 |

The working groups with the highest frequency of fate sharing discussions reflect the areas where the principle remains most actively relevant. [Core](https://datatracker.ietf.org/wg/core/about/) and [dtn](https://datatracker.ietf.org/wg/dtn/about/) (Delay-Tolerant Networking) lead the list, which makes sense given their focus on constrained environments where fate sharing is crucial for resilience. The prominence of [6lo](https://datatracker.ietf.org/wg/6lo/about/) and IoT-related groups reflects the challenges of applying Internet principles to resource-constrained devices.

Interestingly, [quic](https://datatracker.ietf.org/wg/quic/about/) and [masque](https://datatracker.ietf.org/wg/masque/about/) appear prominently, suggesting that even modern transport protocol development continues to grapple with fate sharing questions. This indicates the principle's relevance isn't diminishing but rather evolving to address new architectural contexts like encrypted transport and application-layer protocols.

The geographic distribution of high-discussion meetings (London, Yokohama, Madrid having peaks) doesn't show obvious patterns, suggesting that fate sharing discussions are driven more by technical evolution than by regional concerns or in-person versus virtual meeting dynamics.

## Resources

- [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — Essential reading for anyone working on Internet protocols; provides the authoritative statement of fate sharing and other core principles
- [Clark 1988: Design Philosophy of DARPA Internet Protocols](http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf) — The intellectual foundation explaining why fate sharing emerged from practical engineering trade-offs rather than theoretical considerations  
- [Fate-sharing (Wikipedia)](https://en.wikipedia.org/wiki/Fate-sharing) — Accessible introduction with examples spanning networking, distributed systems, and organizational design
- [End-to-End Arguments in System Design](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf) — Saltzer, Reed & Clark's foundational paper on end-to-end design principles, which provides the theoretical foundation for fate sharing

---
*This report was generated through analysis of IETF working group session transcripts using vCon conversation analysis techniques.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `61316700-7ee6-41bc-b12f-a6f4f5707bbf` |
Sessions analyzed: 544 |
Generated: 2026-03-14*
