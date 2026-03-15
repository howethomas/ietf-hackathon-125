# End-to-end principle

## Introduction

The end-to-end principle stands as one of the Internet's foundational architectural guidelines, asserting that intelligence and complex functionality should reside at network endpoints rather than within the network itself. Originally articulated by Jerome Saltzer, David Reed, and David Clark in their seminal 1984 paper ["End-to-End Arguments in System Design"](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf), this principle argues that functions can only be correctly and completely implemented at the application layer, where the endpoints have full knowledge of their specific requirements and context.

The principle was formally incorporated into Internet architecture through [RFC 1958](https://www.rfc-editor.org/rfc/rfc1958), which established the architectural principles of the Internet, and later refined in [RFC 3724](https://www.rfc-editor.org/rfc/rfc3724), which examined how the rise of middleboxes and network appliances challenged traditional end-to-end thinking. For the IETF, this principle has served as both a design philosophy and a decision-making framework, influencing everything from transport protocol design to security architecture.

The ongoing relevance of the end-to-end principle in IETF discussions reflects the Internet's continuous evolution and the constant tension between network simplicity and the desire to add intelligence within the network infrastructure. As new technologies emerge—from content delivery networks to in-network computing—the IETF community regularly revisits this principle to determine when adherence serves the Internet's goals and when thoughtful exceptions might be warranted.

## Understanding This Principle

**The Core Idea**

Intelligence should live at the edges, not in the middle. Think of this like a well-designed highway system: the roads themselves should be simple and general-purpose, capable of carrying any type of vehicle efficiently from point A to point B. The specialized intelligence—knowing where you're going, what cargo you're carrying, how fast you want to travel, and what route to take—belongs with the drivers and their vehicles, not embedded in the highway infrastructure itself.

This analogy reveals why the principle exists: the network, like a highway, serves countless different applications with vastly different needs. Email systems need reliability but can tolerate delay. Video calls need low latency but can handle some data loss. File transfers want maximum throughput. A "smart" highway that tried to optimize for one type of vehicle would inevitably harm others. Similarly, when networks try to be intelligent about application-specific needs, they often make assumptions that break other applications.

The principle recognizes a fundamental truth about complex systems: the endpoints know their own requirements better than any intermediary possibly could. Just as drivers know their destination, urgency, and preferences better than the highway department, applications understand their performance needs, security requirements, and error handling better than network equipment.

**Why It Matters**

When this principle is violated, you get brittle systems that seem to work well in specific scenarios but fail unpredictably when conditions change. Consider the difference between two approaches to video calling. In an end-to-end approach, the calling application handles compression, error correction, and adaptation to network conditions—it can adjust quality when bandwidth drops, retransmit important frames, and optimize for the specific type of content being shared. The network simply delivers packets.

Contrast this with a "smart network" approach where routers try to optimize video traffic. The routers might prioritize packets they think are video, but they're guessing based on limited information. They can't tell the difference between a critical control packet and a disposable frame enhancement. They don't know if the user prefers lower quality to avoid stuttering, or if this particular call is so important that maximum quality justifies consuming extra bandwidth. When the network makes these decisions, it inevitably makes the wrong choice for many applications.

The violation becomes particularly obvious during failures or unusual conditions. The smart network optimizes for what its designers expected, but breaks when faced with new applications, different usage patterns, or novel network conditions that weren't anticipated.

**The Tension**

The pressure to violate this principle is constant and understandable. Network operators see inefficiencies and want to fix them. When they observe that most traffic is video, it's tempting to build video-optimized networks. When security threats emerge, it's natural to want to scan and filter traffic in the network. When applications misbehave, network administrators want tools to control them directly.

There's also an economic argument: if you're building network infrastructure, selling "smart" features often commands higher prices than selling "dumb" pipes. Customers can see immediate value in a firewall that blocks malware or a cache that speeds up web browsing. The long-term architectural benefits of keeping the network simple are harder to quantify and sell.

Perhaps most importantly, the end-to-end principle can seem inefficient. Why should every endpoint implement its own security, reliability, and optimization when the network could provide these features once, centrally? The principle often appears to encourage duplication of effort.

**How to Recognize It**

- **When building systems, you find yourself asking "what does the application need?" rather than "what can the infrastructure provide?"** — pushing decisions to the layer that has the most context and control.
- **When debugging problems, the root cause turns out to be a middlebox or infrastructure component making assumptions about traffic it doesn't fully understand** — a sign that intelligence was placed too far from the endpoints.
- **When deploying new applications, they work without requiring changes to intermediate network components** — indicating that the network provides general-purpose services rather than application-specific optimizations.

## Early IETF Work

The end-to-end principle emerged from hard-won experience in the early days of computer networking, particularly through ARPANET development and the subsequent design of TCP/IP. The original Internet Protocol suite exemplifies this principle: IP provides simple, best-effort packet delivery, while TCP handles reliability, flow control, and congestion management at the endpoints. This design proved remarkably durable because it allowed the network to remain simple while applications could implement exactly the semantics they needed.

Early IETF architectural documents, particularly [RFC 1958](https://www.rfc-editor.org/rfc/rfc1958), codified this principle as fundamental to Internet design. The RFC explicitly states that "the network should be kept simple" and that complexity should be pushed to the edges. This wasn't merely theoretical—it reflected lessons learned from alternative approaches like X.25 networks, which embedded more intelligence in the network layer but proved less flexible and scalable than the Internet's simpler approach.

However, even early Internet development included deliberate exceptions that sparked ongoing debates. The Domain Name System (DNS) represented a form of in-network intelligence, providing distributed name resolution services. Network Address Translation (NAT), while originally seen as a temporary workaround, became ubiquitous and clearly violated end-to-end principles by modifying packet headers and maintaining connection state. These exceptions demonstrated that the principle, while foundational, must sometimes bend to practical constraints—but each violation came with well-documented costs in terms of application complexity and reduced functionality.

## Key References

- [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — The foundational IETF document establishing end-to-end as a core Internet design principle.
- [RFC 3724: The Rise of the Middle](https://www.rfc-editor.org/rfc/rfc3724) — Examines how middleboxes and in-network processing challenge traditional end-to-end thinking.
- [End-to-End Arguments in System Design](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf) — The original 1984 paper by Saltzer, Reed, and Clark that articulated the principle.

## This Principle in IETF Discussions

The end-to-end principle continues to surface regularly in IETF discussions, particularly as new technologies challenge traditional boundaries between network and application responsibilities. The principle often emerges when working groups grapple with where to place intelligence in evolving network architectures.

In early pandemic-era discussions, the [coinrg](https://datatracker.ietf.org/wg/coinrg/about/) (Computing in the Network Research Group) directly confronted this tension:

> "i'm going to tell you why networks should and from and can provide more expressive routing and this is a little bit controversial because it uh touches on uh the end-to-end end-to-end principle"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf110/ietf110_coinrg_28603.vcon.json)*

This quote from IETF 110 in March 2021 captures the ongoing struggle within the IETF community: how to balance the proven benefits of end-to-end design with the potential advantages of computational capabilities within the network infrastructure.

By November 2022, the [coinrg](https://datatracker.ietf.org/wg/coinrg/about/) discussions had evolved to examine the nuanced relationship between transport protocols and in-network computing:

> "what we now try to do is basically um yeah have a bit more thoughts on how we can actually combine or what is the interplay between transport protocols the end-to-end principle and Computing in the network"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf115/ietf115_coinrg_29890.vcon.json)*

This reflects a maturing perspective—rather than simply opposing in-network computing as a violation of end-to-end principles, the community began exploring how to preserve the principle's benefits while accommodating new computational paradigms.

The [dinrg](https://datatracker.ietf.org/wg/dinrg/about/) (Decentralized Internet Infrastructure Research Group) provided a broader perspective on how Internet evolution affects foundational principles. In November 2022, they observed:

> "what we've got is a situation where the end-to-end principle isn't really the principle that's at work here right in fact one of the things t[hat] drives the user base up and that builds the economy of scale in today's internet the result is really a flattening of the traditional topology"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf115/ietf115_dinrg_29908.vcon.json)*

This candid assessment acknowledges that economic and architectural forces have eroded pure end-to-end design in practice, even as it remains a stated principle.

More recently, by July 2024, [dinrg](https://datatracker.ietf.org/wg/dinrg/about/) discussions showed renewed interest in strengthening end-to-end principles:

> "we wouldn't be starting from scratch um if we did that because there are existing principles including the end to end principle um and rfc's looking at how that's being how it's evolving"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf120/ietf120_dinrg_33163.vcon.json)*

By March 2025, the conversation had shifted toward actively "reinstalling" the principle:

> "the second thing is also bit aligned to what we discussed here before is to um kind of reinstalling the end to end principle for future application development"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf122/ietf122_dinrg_33921.vcon.json)*

This progression shows how IETF thinking has evolved from questioning whether end-to-end principles can accommodate new technologies, to recognizing their erosion in practice, to actively seeking ways to restore them in future Internet architectures.

## Historical Analysis

Analysis of IETF discussions from meetings 110 through 123 (March 2021 to July 2025) reveals interesting patterns in how the end-to-end principle has been discussed across this four-year period.

| Meeting | Date | Location | Discussions |
|---------|------|----------|-------------|
| IETF 110 | March 2021 | Online | 5 |
| IETF 111 | July 2021 | Online | 6 |
| IETF 113 | March 2022 | Vienna | 5 |
| IETF 114 | July 2022 | Philadelphia | 6 |
| IETF 115 | November 2022 | London | 7 |
| IETF 116 | March 2023 | Yokohama | 2 |
| IETF 117 | July 2023 | San Francisco | 6 |
| IETF 118 | November 2023 | Prague | 7 |
| IETF 119 | March 2024 | Brisbane | 3 |
| IETF 120 | July 2024 | Vancouver | 1 |
| IETF 121 | November 2024 | Dublin | 1 |
| IETF 122 | March 2025 | Bangkok | 3 |
| IETF 123 | July 2025 | Madrid | 4 |

The data shows peak discussion activity during 2022-2023, particularly at IETF 115 and 118, which coincided with increased interest in computing-in-the-network technologies and concerns about platform centralization. The significant drop in discussions at IETF 120 and 121 may reflect either a temporary lull or the community reaching some consensus on key issues.

The [dinrg](https://datatracker.ietf.org/wg/dinrg/about/) working group dominated discussions with 7 sessions, reflecting their focus on decentralized infrastructure and fundamental Internet principles. The [dtn](https://datatracker.ietf.org/wg/dtn/about/) (Delay-Tolerant Networking) and [nmrg](https://datatracker.ietf.org/wg/nmrg/about/) (Network Management Research Group) each contributed 4 sessions, while [coinrg](https://datatracker.ietf.org/wg/coinrg/about/) and [secdispatch](https://datatracker.ietf.org/wg/secdispatch/about/) each had 3 sessions. This distribution suggests that end-to-end principle discussions are most active in research groups exploring new paradigms and in working groups dealing with challenging network environments where traditional assumptions may not hold.

The breadth of discussion across 36 different working groups indicates that this principle remains relevant across diverse areas of Internet engineering, from routing protocols in [lsr](https://datatracker.ietf.org/wg/lsr/about/) to security architectures in [ace](https://datatracker.ietf.org/wg/ace/about/). This wide engagement suggests the principle continues to serve as a useful framework for architectural decisions across the Internet engineering community.

## Resources

- [End-to-End Principle (Wikipedia)](https://en.wikipedia.org/wiki/End-to-end_principle) — Comprehensive overview with examples and criticism, valuable for understanding the principle's application beyond networking.
- [RFC 3724: The Rise of the Middle](https://www.rfc-editor.org/rfc/rfc3724) — Essential reading for understanding how middleboxes and network appliances challenge end-to-end design.
- [IETF Architectural Principles of the Internet (RFC 1958)](https://www.rfc-editor.org/rfc/rfc1958) — The foundational document establishing this and other core Internet design principles.
- [End-to-End Arguments in System Design](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf) — The original 1984 paper that remains remarkably relevant for modern system design decisions.

---

*This report was generated from analysis of IETF meeting transcripts stored as vCon (Virtual Conversation) records, covering meetings 110-123 (March 2021 - July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `317f8ebe-3225-45da-8907-8704b0027aab` |
Sessions analyzed: 56 |
Generated: 2026-03-15*
