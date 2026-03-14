# Simplicity / complexity management

## Introduction

"Complexity is the primary impediment to scaling. Keep designs simple." This foundational principle of Internet architecture, codified in [RFC 3439](https://www.rfc-editor.org/rfc/rfc3439), represents one of the most enduring yet challenging guidelines in network protocol design. Written by Randy Bush and Dave Meyer in 2002, RFC 3439 distilled decades of Internet engineering experience into a set of architectural guidelines that continue to shape protocol development today.

The principle of simplicity emerges from a hard-learned lesson: the Internet's success stems not from perfect engineering, but from designs simple enough to be widely implemented, understood, and evolved. As the Internet has grown from connecting a few research institutions to becoming humanity's critical infrastructure, this principle has become both more important and more difficult to follow. The exponential growth in users, applications, and requirements creates constant pressure to add features, capabilities, and optimizations—each seemingly reasonable in isolation, but collectively threatening the very simplicity that enables the Internet to function at global scale.

In IETF working groups, this principle appears in nearly every significant protocol discussion, serving as both a design goal and a quality gate. The principle's universal presence across 418 sessions spanning IETF 110-123 demonstrates its central role in Internet engineering, even as implementers grapple with increasingly complex requirements from security, performance, and functionality demands.

## Understanding This Principle

**The Core Idea**

The simpler a system, the more likely it is to work reliably at scale.

Think of simplicity like the difference between a Swiss Army knife and a professional kitchen. A Swiss Army knife has many tools in one compact package—it's clever, space-efficient, and covers many use cases. But when you're cooking for 500 people, professional chefs don't reach for Swiss Army knives. They use simple, specialized tools: a sharp knife that only cuts, a ladle that only scoops, a timer that only counts down. Each tool does one thing exceptionally well, and crucially, any cook can pick up any tool and immediately understand how to use it. The kitchen works because every component is simple enough to be reliable, replaceable, and understood by anyone who needs to use it.

The Internet is like that professional kitchen, but scaled to billions of users and trillions of messages. Every router, every protocol, every piece of software needs to be simple enough that it can be implemented correctly by thousands of different teams, debugged when things go wrong, and evolved as needs change. A clever, feature-rich protocol might seem more efficient, but if only a few experts can implement it correctly, it becomes a bottleneck that prevents the whole system from scaling.

**Why It Matters**

When systems become too complex, they fail in predictable ways. Implementation errors multiply, edge cases proliferate, and troubleshooting becomes nearly impossible. Consider the difference between early email (SMTP) and modern video conferencing protocols. SMTP is so simple that you can send email by typing commands manually—and that simplicity is why email still works reliably across every network, device, and software platform 40+ years later. Meanwhile, video conferencing protocols are often so complex that getting two different systems to interoperate requires specialized gateways and extensive testing.

The consequences of complexity show up everywhere. Complex protocols are harder to implement correctly, leading to subtle bugs that only surface under unusual conditions—exactly when reliability matters most. They're harder to secure, because attack surfaces multiply with features. They're harder to evolve, because changing one component might break unexpected dependencies. Most critically, they create barriers to innovation because new implementers can't understand the system well enough to improve it.

**The Tension**

The pressure against simplicity is relentless and often well-intentioned. Users want more features. Security experts want more protection mechanisms. Performance engineers want more optimization knobs. Operators want more monitoring and control capabilities. Each addition makes perfect sense in isolation—who would argue against better security or performance?

This pressure is amplified by what engineers call "second-system syndrome." After successfully building a simple system, the temptation is enormous to build the next version that solves all the problems and limitations of the first. The new system will be elegant, comprehensive, and sophisticated. It will also likely be too complex to implement reliably, debug effectively, or evolve gracefully. The engineering ego prefers sophisticated solutions, even when simple ones work better.

Standards committees face additional pressure because they're trying to satisfy diverse constituencies with different needs. It's politically easier to add optional features that make everyone happy than to make hard choices about what to exclude. But optional features aren't free—they still increase implementation complexity and create interoperability challenges.

**How to Recognize It**

You're seeing this principle at work when a team chooses to build three separate, focused APIs instead of one flexible super-API that handles all cases. When a protocol designer removes a feature because "we can add it later if we really need it, but we can't remove it once it's deployed." When an architect insists on solving one problem well instead of solving five problems adequately. When debugging instructions fit on a single page instead of requiring a manual.

## Key References

- [RFC 3439: Some Internet Architectural Guidelines](https://www.rfc-editor.org/rfc/rfc3439) — The foundational document that codifies simplicity and other core Internet design principles.

## This Principle in IETF Discussions

The principle of simplicity emerges consistently across IETF working groups as both a design aspiration and a practical constraint. In real protocol development, this often manifests as explicit decisions to resist feature creep and maintain focus.

In the NETMOD working group, this tension played out clearly in discussions about module packaging. As one participant explained in November 2024:

> "but what we got to was let's try and keep it simple so let's not have that distinction let's not try and to to like boil the ocean and do everything all at once"

This reflected a conscious choice to avoid over-engineering a solution that could handle every conceivable use case, instead focusing on the core functionality that would actually be needed and implementable.

The MASQUE working group demonstrated how simplicity guides real-time decision making during protocol design. When faced with complex endpoint management options, the discussion quickly converged on pragmatic simplicity:

> "the server is just going to send you an IP in Port and say I'd really rather you be over here fair enough I think we can just keep it simple and move on"

This shows how simplicity serves as a decision-making tool—when multiple approaches are technically feasible, the simpler one is often preferred because it reduces implementation burden and potential failure modes.

The MLS working group session revealed how complexity can creep into even well-intentioned designs. One participant's frustration was palpable:

> "I feel like we've worked ourselves into well of complexity with a bunch of extra assumptions we've made in safe extension the way safe extensions is"

This illustrates how features that seem reasonable individually can interact to create unexpected complexity. The "well of complexity" metaphor captures how these problems compound—each additional feature makes it harder to climb back out to simplicity.

In the PALS working group, complexity concerns became decisive factors in technical evaluations:

> "there were technical concerns of the proposed solution and uh it was some comments uh from myself and uh from others uh on Purely technical concerned about the complexity that PSD introduces"

This demonstrates how simplicity isn't just an aesthetic preference but a practical engineering constraint that influences whether solutions are adopted.

## Historical Analysis

The frequency of simplicity discussions across IETF meetings shows remarkable consistency, with notable increases in recent years:

| Meeting | Date | Sessions |
|---------|------|----------|
| IETF 110 | March 2021 | 33 |
| IETF 111 | July 2021 | 16 |
| IETF 112 | November 2021 | 27 |
| IETF 113 | March 2022 | 24 |
| IETF 114 | July 2022 | 27 |
| IETF 115 | November 2022 | 34 |
| IETF 116 | March 2023 | 31 |
| IETF 117 | July 2023 | 25 |
| IETF 118 | November 2023 | 31 |
| IETF 119 | March 2024 | 30 |
| IETF 120 | July 2024 | 28 |
| IETF 121 | November 2024 | 38 |
| IETF 122 | March 2025 | 35 |
| IETF 123 | July 2025 | 39 |

The data reveals several interesting patterns. The initial spike at IETF 110 (33 sessions) may reflect the transition to online meetings during the pandemic, where simplified protocols became more critical for reliable remote participation. The lower frequency at IETF 111 (16 sessions) appears to be an anomaly, followed by a return to more typical levels.

More significantly, there's a clear upward trend from 2024 onward, with the highest frequencies occurring at IETF 121, 122, and 123 (38, 35, and 39 sessions respectively). This increase likely reflects growing awareness that Internet protocols are becoming too complex to implement reliably, coinciding with industry concerns about protocol ossification and implementation barriers.

The working groups that discuss simplicity most frequently—NMRG, RTGWG, CFRG, MASQUE, NETMOD, and V6OPS—represent a mix of research groups (NMRG, CFRG), core infrastructure protocols (RTGWG, V6OPS, NETMOD), and emerging technologies (MASQUE). This distribution suggests that simplicity concerns span from theoretical research to operational deployment, reinforcing that this principle applies across all aspects of Internet architecture.

The fact that 149 different working groups have discussed this principle demonstrates its universal relevance. This isn't a specialized concern for particular protocol areas—it's a fundamental engineering constraint that applies whether you're designing routing protocols, security mechanisms, or application layer standards.

## Resources

- [RFC 3439: Some Internet Architectural Guidelines](https://www.rfc-editor.org/rfc/rfc3439) — Essential reading that establishes simplicity as a core Internet design principle alongside end-to-end connectivity and other fundamental concepts.

- [Worse is Better (Richard Gabriel)](https://www.dreamsongs.com/WorseIsBetter.html) — A influential essay that explains why simple, implementable solutions often succeed over theoretically superior but complex alternatives.

- [KISS Principle (Wikipedia)](https://en.wikipedia.org/wiki/KISS_principle) — Provides broader context for "Keep It Simple, Stupid" across engineering disciplines, with examples from aerospace, software, and systems design.

- [The Design and Implementation of the 4.3BSD UNIX Operating System](https://www.goodreads.com/book/show/5770.The_Design_and_Implementation_of_the_4_3BSD_UNIX_Operating_System) — Classic text that demonstrates how simplicity enables both reliability and evolution in complex systems.

---

*This report was generated from analysis of IETF working group session transcripts using vCon (Virtual Conversation) data format and analysis tools.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `719bcf65-a036-4d0c-a959-7ee59ae43328` |
Sessions analyzed: 418 |
Generated: 2026-03-14*
