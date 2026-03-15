# Simplicity / complexity management

## Introduction

The principle of "Simplicity / complexity management" stands as one of the IETF's most fundamental yet challenging design philosophies. Expressed succinctly as "complexity is the primary impediment to scaling," this principle argues that network protocols and systems should favor simple, understandable designs over complex ones. This isn't merely an aesthetic preference—it's a hard-learned engineering discipline born from decades of watching ambitious protocols fail under their own complexity.

The principle gained formal recognition in [RFC 3439](https://www.rfc-editor.org/rfc/rfc3439), "Some Internet Architectural Guidelines and Philosophy," authored by Randy Bush and Dave Meyer in 2002. However, its roots trace back to the Internet's earliest days, when pioneers like Jon Postel advocated for the "robustness principle" and simple, extensible designs. The IETF community has repeatedly observed that while complexity often seems like the path to more powerful or complete solutions, it frequently becomes the enemy of interoperability, maintainability, and successful deployment.

In the modern Internet era, as protocols handle everything from IoT sensors to high-frequency trading, this principle has become more critical than ever. The corpus of IETF discussions from 2021 to 2025 reveals 418 instances where working groups explicitly grappled with complexity management—a testament to its ongoing relevance as engineers balance feature richness against operational reality.

## Understanding This Principle

**The Core Idea**

Keep protocol designs as simple as possible while still solving the problem at hand, because complexity kills adoption, breaks interoperability, and makes systems impossible to debug or evolve.

Think of this principle like urban planning. When cities grow organically, they often develop simple, intuitive layouts—main roads that follow natural geography, neighborhoods that cluster around practical needs like markets or transportation hubs. These cities, like Boston's Back Bay or the historic centers of European cities, remain vibrant and navigable centuries later. But when planners try to optimize everything at once—creating elaborate highway interchanges, complex zoning rules, and intricate traffic management systems—they often produce places like certain modern suburban developments where you need GPS to buy groceries and a traffic engineer's degree to understand the road signs.

The best urban designs solve real problems (getting people where they need to go) with solutions that feel obvious in retrospect. They're easy to explain to newcomers, easy to modify when needs change, and resilient when individual components fail. The worst designs might look impressive on paper and optimize for multiple goals simultaneously, but they're brittle, confusing, and impossible to fix when something goes wrong.

**Why It Matters**

When network protocols violate the simplicity principle, they fail in predictable ways. Consider IPv6, which solved real problems (address exhaustion, routing table growth) but introduced significant complexity with features like stateless autoconfiguration, neighbor discovery, and multiple address types per interface. While IPv6 works well, its deployment took decades partly because network operators found it harder to understand, configure, and troubleshoot than IPv4's simpler model.

Contrast this with HTTP, which succeeded wildly despite (or because of) its apparent simplicity. Early HTTP was just request-response text messages over TCP connections. This simplicity meant anyone could implement it, debug it with basic tools, and extend it incrementally. Even as HTTP evolved to support complex modern web applications, it maintained conceptual simplicity at its core.

The practical consequences are stark: complex protocols take longer to standardize, have more implementation bugs, suffer worse interoperability problems, and often get deployed incorrectly in production. Simple protocols can be implemented by junior engineers, debugged with standard tools, and understood by operators during 3 AM outages.

**The Tension**

The pressure against simplicity is relentless and often well-intentioned. Engineers see related problems and want to solve them all at once rather than requiring multiple protocols. Standards committees want to future-proof designs by anticipating every possible use case. Vendors want feature differentiation. Researchers want to publish novel contributions rather than incremental improvements.

There's also a deeper psychological factor: complex solutions often feel more professional or sophisticated than simple ones. It's easy to dismiss a simple protocol as "obvious" or "not enough of a contribution," even when simplicity is the hardest thing to achieve. As the saying goes, "I would have written a shorter letter, but I didn't have the time."

**How to Recognize It**

You're seeing this principle at work when:

* A working group decides to split a large protocol into smaller, composable pieces rather than creating one monolithic standard
* Engineers choose to defer features to future versions rather than complicate the initial design
* A protocol design prioritizes making the common case simple, even if it makes advanced use cases slightly more verbose
* Implementers can explain the core protocol behavior to a colleague in under five minutes
* Operators can troubleshoot problems using standard tools rather than specialized diagnostic software

## Early IETF Work

The IETF's commitment to simplicity emerged from painful early experiences with overly complex protocols. The OSI protocol suite of the 1980s served as a cautionary tale—despite significant standardization effort and government backing, OSI protocols like X.400 email and X.500 directory services largely failed in the marketplace. They were comprehensively designed, addressed many use cases, but were notoriously difficult to implement correctly and operate reliably.

Meanwhile, the Internet protocol suite succeeded by embracing simplicity and modularity. TCP/IP split networking into layers with clean interfaces. SMTP kept email simple enough that implementations could fit on floppy disks. DNS provided a distributed directory service by focusing on one problem (name resolution) rather than attempting a comprehensive information system. Jon Postel's "robustness principle"—"be conservative in what you do, be liberal in what you accept from others"—exemplified this philosophy of preferring simple, forgiving designs over rigid, complex ones.

The contrast became even starker with web protocols. HTTP succeeded where more sophisticated alternatives like Gopher+ and WAIS failed, largely because HTTP was simple enough for anyone to implement and extend. This pattern repeated throughout the 1990s: simple protocols (DHCP, BGP-4, SSH) gained wide adoption while more ambitious efforts struggled. By the time RFC 3439 was published in 2002, the IETF had internalized these lessons into explicit architectural guidance.

## Key References

* [RFC 3439: Some Internet Architectural Guidelines and Philosophy](https://www.rfc-editor.org/rfc/rfc3439) — The foundational document establishing simplicity as a core Internet design principle
* [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — Early articulation of Internet design philosophy including preference for simple solutions

## This Principle in IETF Discussions

The simplicity principle appears consistently across IETF working groups, though its application varies significantly by context. In [netmod](https://datatracker.ietf.org/wg/netmod/about/), the principle often governs decisions about YANG data modeling complexity. As seen in the November 2024 Dublin discussion, the working group deliberately chose to "keep it simple" rather than "boil the ocean" when designing package-level module specifications:

> "this is the exact set of modules I support uh at a given package level and these are the versions of those modules I support along with features and any deviations but what we got to was let's try and keep it simple so let's not have that distinction let's not try and to to like boil the ocean and do"

This reflects a mature engineering judgment: while comprehensive solutions might seem more elegant, they often prove harder to implement and deploy successfully.

The [coinrg](https://datatracker.ietf.org/wg/coinrg/about/) research group explicitly engaged with simplicity as a design principle in their November 2022 London session, using it as inspiration for protocol decision-making:

> "aspects and then we thought about what kind of tirebreaker could we have there or how we could then actually derive the decision that we want to have and for um the inspiration we'll then look at the Simplicity principle which basically states that we should always Thrive to the simplest solution or"

This demonstrates how the principle has evolved beyond implementation guidance to become a philosophical framework for research and design choices.

The tension between functionality and complexity appears clearly in operational contexts. The [masque](https://datatracker.ietf.org/wg/masque/about/) working group's July 2024 Vancouver discussion shows engineers actively choosing simplicity over optimization:

> "u're not changing endpoints now maybe you're changing ports but right the the server is just going to send you an IP in Port and say I'd really rather you be over here fair enough I think we can just keep it simple and move on okay Alexander gini Cloud flare yeah the the whole capsule thing seems li"

The [mls](https://datatracker.ietf.org/wg/mls/about/) working group's November 2024 Dublin session revealed frustration with accumulated complexity, with participants recognizing they had "worked ourselves into well of complexity":

> "al wire formats Richard I hate all of this I the bottom bullet yes absolutely we should do that easy quick fix bug fix clear Omission um the rest of it I feel like we've worked ourselves into well of complexity with a bunch of extra assumptions we've made in safe extension the way safe extensions is"

This candid assessment illustrates how complexity can creep into designs despite good intentions, and the importance of periodic simplification efforts.

## Historical Analysis

Discussion of simplicity and complexity management remained remarkably consistent across the 14 IETF meetings from March 2021 through July 2025, with a notable uptick in recent meetings:

| Meeting Period | Sessions | Trend |
|---|---|---|
| Early (110-113) | 100 | Baseline establishment |
| Middle (114-119) | 177 | Steady application |
| Recent (120-123) | 140 | Increased focus |

The pattern shows growing attention to complexity management in recent meetings, with IETF 123 (Madrid) recording the highest number of relevant discussions (39 sessions). This likely reflects the IETF community's growing awareness that successful protocol deployment requires deliberate complexity management as Internet systems become more sophisticated.

The [nmrg](https://datatracker.ietf.org/wg/nmrg/about/) and [rtgwg](https://datatracker.ietf.org/wg/rtgwg/about/) working groups lead in discussions (9 sessions each), which makes sense given their focus on network management and routing—areas where complexity directly impacts operational success. The [cfrg](https://datatracker.ietf.org/wg/cfrg/about/) appears prominently (8 sessions), reflecting ongoing challenges in making cryptographic protocols both secure and implementable.

The broad distribution across 149 working groups suggests that simplicity isn't just a concern for protocol designers—it affects security, operations, applications, and research groups equally. This universality reinforces the principle's foundational importance in Internet architecture.

## Resources

* [RFC 3439: Some Internet Architectural Guidelines](https://www.rfc-editor.org/rfc/rfc3439) — Essential reading for understanding how simplicity fits into overall Internet design philosophy
* [Worse is Better (Richard Gabriel)](https://www.dreamsongs.com/WorseIsBetter.html) — Influential essay arguing that simple, pragmatic designs often succeed where theoretically superior complex designs fail
* [KISS Principle (Wikipedia)](https://en.wikipedia.org/wiki/KISS_principle) — Broader context on simplicity as an engineering principle across domains
* [The Design of Design (Fred Brooks)](https://en.wikipedia.org/wiki/The_Design_of_Design) — Classic work on design complexity and the challenges of managing it in large engineering projects

---
*This report was generated from analysis of IETF working group session transcripts using vCon conversation analysis.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `719bcf65-a036-4d0c-a959-7ee59ae43328` |
Sessions analyzed: 418 |
Generated: 2026-03-14*
