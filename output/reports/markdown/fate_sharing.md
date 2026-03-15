# Fate sharing

## Introduction

Fate sharing is one of the Internet's most fundamental architectural principles, dictating that related parts of a system should fail together rather than maintaining dependencies that can leave the system in inconsistent states. First articulated in David Clark's seminal 1988 paper ["The Design Philosophy of the DARPA Internet Protocols"](http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf) and later codified in [RFC 1958](https://www.rfc-editor.org/rfc/rfc1958), this principle emerged from hard-won lessons about building resilient distributed systems at Internet scale.

The principle's core insight is deceptively simple: state should be maintained only at endpoints, and when failures occur, all related components should fail together rather than leaving orphaned state scattered throughout the network. This approach trades some theoretical efficiency for dramatically improved robustness and recovery characteristics. Rather than trying to maintain perfect consistency across distributed components—a notoriously difficult problem—fate sharing accepts that failures will happen and designs systems to fail gracefully and recover cleanly.

Fate sharing has profoundly shaped Internet protocol design for over three decades, influencing everything from TCP's endpoint-centric state management to modern application architectures. Its continued relevance is evident in contemporary IETF discussions spanning 544 working group sessions from 2021 to 2025, where it remains a touchstone for evaluating new protocols and architectural decisions across diverse working groups from [core](https://datatracker.ietf.org/wg/core/about/) to [quic](https://datatracker.ietf.org/wg/quic/about/) to [spring](https://datatracker.ietf.org/wg/spring/about/).

## Understanding This Principle

**The Core Idea**

When things break, related parts should break together rather than leaving some components working and others failing in ways that create inconsistent or unrecoverable states.

Imagine a restaurant where the kitchen, wait staff, and payment system all operate independently with their own record-keeping. A customer orders dinner, the kitchen starts cooking, the waiter records the order, and the payment system reserves the charge on their credit card. Now suppose the kitchen equipment fails mid-service. In a poorly designed system, you might end up with the waiter still expecting to serve a meal that can't be cooked, while the payment system charges for food that was never delivered. Each component maintained its own state, and when one failed, the others didn't know how to respond.

Fate sharing would redesign this system so that when the kitchen fails, the entire order process fails together—the waiter is immediately notified, the payment authorization is automatically cancelled, and the customer is informed before they're left wondering where their food is. Instead of three separate systems maintaining independent state that can get out of sync, the failure of any critical component cascades to related components, ensuring the system fails into a clean, recoverable state rather than an inconsistent mess.

**Why It Matters**

The practical consequences of violating fate sharing are painfully familiar to anyone who has worked with distributed systems. Without fate sharing, failures create "zombie state"—orphaned records, dangling references, and half-completed transactions that can persist long after the original operation failed. These inconsistencies compound over time, creating systems that become progressively less reliable and harder to debug.

Consider a network where intermediate routers maintain detailed state about every connection passing through them. When a router fails, all that connection state is lost, but the endpoints don't know this—they keep sending data into a black hole while the failed router's neighbors still think those connections exist. Recovery requires complex coordination between multiple network elements, and there's no guarantee that all parties will agree on what state should be restored.

In contrast, TCP follows fate sharing by keeping connection state only at the endpoints. When a router fails, the connection endpoints detect the failure through timeouts and either re-establish connectivity through alternate paths or fail the connection entirely. There's no orphaned state in the network to clean up, no complex coordination required, and recovery is straightforward because only two parties need to agree on what happened.

**The Tension**

The fundamental tension with fate sharing is efficiency. It's often more efficient—at least in the short term—to cache state, maintain shortcuts, and optimize for the common case where everything works perfectly. Keeping connection state in network routers could enable faster forwarding decisions. Maintaining transaction state in intermediate servers could reduce the coordination overhead between endpoints. These optimizations can provide real performance benefits when everything is working correctly.

The temptation is especially strong when building new systems where the complexity of proper state management isn't yet apparent. It's easier to build a working prototype that maintains state wherever it's convenient than to carefully design state management to survive arbitrary component failures. The costs of violating fate sharing—debugging complex failure modes, handling orphaned state, coordinating recovery across multiple components—only become apparent later, often in production systems under stress.

**How to Recognize It**

You're seeing fate sharing at work when:

- A system fails fast and completely rather than limping along with partial functionality
- Recovery procedures only require restarting endpoints rather than coordinating state recovery across multiple intermediate components  
- System components can be restarted independently without complex dependency management or state synchronization protocols
- Failure diagnostics point to clear root causes rather than cascading from mysterious inconsistencies between component states

## Early IETF Work

The principle of fate sharing emerged from the early Internet's fundamental design decisions, most notably the choice to make the network layer stateless and keep complex state management at the endpoints. This was a deliberate departure from the telecommunications industry's circuit-switched model, where the network maintained detailed state about every connection and recovery from failures required complex coordination between network elements.

TCP's design exemplifies early fate sharing thinking. Rather than having intermediate routers maintain connection state that could be lost during failures, TCP keeps all connection state at the endpoints and uses end-to-end acknowledgments to detect and recover from failures. This design choice, documented in RFC 793, made TCP remarkably resilient to network failures while keeping the network layer simple and scalable. The principle was further reinforced by the end-to-end arguments articulated in Saltzer, Reed, and Clark's influential 1984 paper, which argued that complex functions should be implemented at the endpoints rather than in intermediate network elements.

However, the Internet's evolution has also seen notable tensions with pure fate sharing. Network Address Translation (NAT), widely deployed despite violating fate sharing principles, maintains connection state in intermediate devices and creates the exact kinds of failure modes that fate sharing was designed to avoid. Similarly, various attempts at "intelligent" network services that cache or proxy application state have repeatedly demonstrated the principle's wisdom when these services fail and leave applications dealing with inconsistent state.

## Key References

- [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — The foundational document that codified fate sharing as a core Internet architectural principle
- [The Design Philosophy of the DARPA Internet Protocols](http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf) — David Clark's seminal 1988 paper that first articulated fate sharing and other key Internet design principles
- [End-to-End Arguments in System Design](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf) — Saltzer, Reed, and Clark's 1984 paper laying the theoretical foundation for endpoint-centric system design

## This Principle in IETF Discussions

Fate sharing continues to be a vital consideration in contemporary IETF protocol development, appearing regularly in discussions about state management, failure recovery, and architectural trade-offs. The principle's application has evolved to address new challenges in modern networking while maintaining its core insight about failure resilience.

In early discussions during the pandemic period, working groups grappled with fundamental questions about where to maintain state in constrained environments. During IETF 110, the [babel](https://datatracker.ietf.org/wg/babel/about/) working group examined fate sharing challenges in packet fragmentation scenarios:

> "fragmentation required packets are going to fail to reach the sending host and you're going to have mysterious failures where some things work and then get stuck so the problem here is that you have no fate sharing between the data between on the one hand the date and act pass and on the other hand th"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf110/ietf110_babel_28702.vcon.json)*

This discussion highlighted how violations of fate sharing create "mysterious failures" where part of a system continues to function while other parts fail, leading to difficult-to-debug scenarios where some packets succeed while others silently fail.

By the middle period around IETF 119, the conversation had shifted to more nuanced applications in security protocols. The [ipsecme](https://datatracker.ietf.org/wg/ipsecme/about/) working group discussed the benefits of stateless ESP implementations:

> "is different it's native as extension header so basic IPv6 header will just indicate that inside we have as extension header and everything else is hidden it actually has some advantages uh if ESP is stateless allow through your uh filtering then you don't need you don't need any keep Al lives if th"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf119/ietf119_ipsecme_32044.vcon.json)*

This reflects the principle's application to security protocols, where stateless designs eliminate the need for keepalive mechanisms and reduce the complexity of state synchronization across security boundaries.

In more recent discussions during IETF 120, the [6lo](https://datatracker.ietf.org/wg/6lo/about/) working group addressed how to handle state persistence across node restarts in constrained environments:

> "good point uh about the usage of nonvolatile memory because like in other documents um if by any chance uh a node restarts so basically what it does it checks in the nonvolatile memory if he has some State he can re-register okay so the text has been um updated in a few places in order to to uh cons"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf120/ietf120_6lo_33113.vcon.json)*

This discussion shows how modern IoT and constrained networking scenarios require careful consideration of fate sharing when dealing with resource limitations and intermittent connectivity, balancing the principle's benefits against practical deployment constraints.

## Historical Analysis

Analysis of fate sharing discussions across IETF 110–123 reveals interesting patterns in how the principle has been applied to emerging networking challenges. The frequency of discussions has remained consistently high, with a notable spike to 61 sessions in IETF 123, suggesting renewed attention to state management issues in current protocol development.

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

The working groups most actively discussing fate sharing reflect the principle's broad applicability across different networking domains. The [core](https://datatracker.ietf.org/wg/core/about/) and [dtn](https://datatracker.ietf.org/wg/dtn/about/) working groups' prominence indicates significant attention to state management in constrained and delay-tolerant networking scenarios. Meanwhile, the presence of [quic](https://datatracker.ietf.org/wg/quic/about/), [masque](https://datatracker.ietf.org/wg/masque/about/), and [webtrans](https://datatracker.ietf.org/wg/webtrans/about/) suggests that fate sharing remains relevant for modern transport and application protocols.

The increase in discussions around IETF 115–116 (London and Yokohama) coincided with renewed focus on Internet architecture principles as the IETF grappled with lessons learned from the pandemic's impact on Internet infrastructure. The recent spike in IETF 123 likely reflects ongoing work on emerging technologies like compute-aware networking and new transport protocols where state management decisions have significant architectural implications.

## Resources

- [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — Essential reading for understanding fate sharing in the context of the Internet's overall architectural philosophy
- [Fate-sharing (Wikipedia)](https://en.wikipedia.org/wiki/Fate-sharing) — Accessible overview with examples from different computing contexts beyond networking
- [Clark 1988: Design Philosophy of DARPA Internet Protocols](http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf) — The original articulation of fate sharing and other Internet design principles that shaped decades of protocol development
- [End-to-End Arguments in System Design](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf) — Foundational paper on endpoint-centric design that provides the theoretical basis for fate sharing
- [IETF Internet Architecture Board](https://www.iab.org/) — Current IAB documents and statements that continue to refine and apply architectural principles including fate sharing

---

*This report was generated from analysis of IETF meeting transcripts stored in vCon format, covering working group sessions from IETF 110 (March 2021) through IETF 123 (July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `61316700-7ee6-41bc-b12f-a6f4f5707bbf` |
Sessions analyzed: 544 |
Generated: 2026-03-15*
