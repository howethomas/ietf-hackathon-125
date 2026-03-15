# Rough consensus and running code

## Introduction

"Rough consensus and running code" stands as perhaps the most iconic principle governing Internet protocol development and IETF decision-making. First articulated by David Clark at a 1992 IETF meeting and later formalized in [RFC 7282](https://www.rfc-editor.org/rfc/rfc7282), this principle fundamentally shapes how the Internet's technical standards evolve. It captures the IETF's pragmatic approach to engineering: address all technical concerns raised by participants, but don't let perfect be the enemy of good, and always prefer solutions that have been proven to work in practice over elegant theories.

The principle operates on two interconnected levels. "Rough consensus" means that while the IETF doesn't vote or require unanimity, it does demand that all significant objections be heard and addressed—even if not every participant ends up completely satisfied with the final solution. "Running code" means that working implementations carry enormous weight in technical discussions, often more than theoretical arguments or simulation results. Together, these concepts create a bias toward practical, deployable solutions that can actually improve the Internet.

This approach has proven remarkably successful in building the global Internet we rely on today. Unlike traditional standards bodies that might spend years perfecting specifications before any implementation, the IETF's emphasis on running code has enabled rapid iteration and real-world validation of protocol designs. From TCP/IP to HTTP to BGP, the Internet's most critical protocols emerged through this process of building consensus around working implementations.

## Understanding This Principle

**The Core Idea** — The best technical decisions emerge when you address everyone's serious concerns but don't let holdouts block progress, and you trust working prototypes over perfect theories.

Think of it like designing a new city transportation system. The traditional approach might involve urban planners creating elaborate theoretical models, running simulations, and trying to get every stakeholder group to sign off on the perfect plan before breaking ground. The "rough consensus and running code" approach would instead say: listen carefully to concerns from commuters, business owners, environmental groups, and accessibility advocates, but once you've addressed the major issues, build a pilot route and see how it actually works. If the buses run on time and people use them, that tells you more than any number of traffic flow equations.

The "rough consensus" part means you don't need the taxi lobby to love your bus system—you just need to ensure their concerns about unfair competition have been heard and reasonably addressed, perhaps through regulated ride-sharing integration. The "running code" part means that a single functioning bus route carrying real passengers trumps a hundred theoretical studies about optimal route spacing.

**Why It Matters** — Without this principle, technical standards become either paralyzed by perfectionism or dominated by whoever has the loudest voice. Consider the difference between two approaches to developing a new data format. In the traditional committee approach, experts might spend two years debating edge cases, theoretical optimal structures, and ensuring every possible use case is perfectly supported—only to discover that when implementations finally appear, the format is too complex for real systems and nobody adopts it.

The rough consensus approach would instead start with a working parser and generator, address the major technical objections raised by implementers and users, and ship something that demonstrably works for 80% of use cases. The remaining edge cases get addressed in future versions, guided by real deployment experience rather than speculation.

**The Tension** — The pressure against this principle comes from two powerful forces: the perfectionism of engineers and the politics of organizations. Engineers naturally want to solve problems completely and elegantly before shipping—it feels wrong to leave known issues unaddressed. Meanwhile, organizations often want unanimous buy-in to avoid later blame or resistance. It's much easier to say "everyone agreed to this" than "we listened to everyone and made a judgment call."

This creates a constant temptation to keep polishing, keep seeking more consensus, keep adding features to address every concern. But in the fast-moving world of Internet protocols, waiting for perfection often means arriving too late. By the time your perfectly consensual, theoretically optimal protocol is ready, three competing solutions are already deployed and gaining network effects.

**How to Recognize It** — You're seeing this principle at work when:

- A technical team ships a working prototype to validate an architecture decision rather than debating alternatives in meetings for another month
- A standards body adopts a specification that has rough edges but multiple interoperable implementations rather than waiting for theoretical perfection
- An engineering organization moves forward with a design after addressing major concerns, even though some stakeholders still prefer alternative approaches
- A project prioritizes compatibility with existing deployed systems over clean-slate theoretical elegance

## Early IETF Work

The "rough consensus and running code" principle emerged from hard-won experience in the Internet's formative decades. The early Internet protocols succeeded precisely because they prioritized working implementations over elaborate specifications. TCP/IP displaced more theoretically elegant alternatives like OSI partly because it had functioning code that network administrators could deploy immediately. The original HTTP specification was famously brief and informal, but it enabled the World Wide Web to explode into existence because browsers and servers could interoperate from day one.

However, the IETF also learned painful lessons about the limits of this approach. The IPv4 address space crisis demonstrated what happens when rough consensus settles on a "good enough" solution (32-bit addresses) without fully considering long-term scalability. Similarly, early email protocols like SMTP were designed in an era when the Internet was a trusted academic network—their lack of authentication mechanisms created security problems that plague us today. These experiences taught the IETF that "rough consensus" must still be informed consensus, and "running code" must be code that actually addresses the real problem space.

The principle also reflects the IETF's cultural rejection of traditional standards-making approaches that dominated industries like telecommunications. Where ITU-T might spend years developing comprehensive specifications in isolation, the IETF embraced an iterative approach where implementation experience directly informed specification development. This created a virtuous cycle: protocols that couldn't be implemented or deployed well would fail in the marketplace of running code, while successful protocols would evolve based on operational experience.

## Key References

- [RFC 7282: On Consensus and Humming in the IETF](https://www.rfc-editor.org/rfc/rfc7282) — The definitive explanation of how consensus works in IETF decision-making processes
- [RFC 2026: The Internet Standards Process](https://www.rfc-editor.org/rfc/rfc2026) — Describes how rough consensus and running code fit into the formal standardization process
- [The Tao of IETF](https://www.ietf.org/about/participate/tao/) — Newcomer's guide explaining IETF culture and decision-making principles

## This Principle in IETF Discussions

The principle of rough consensus and running code continues to guide IETF deliberations across diverse technical domains, as evidenced by working group discussions spanning from March 2021 to July 2025. These conversations reveal how the principle adapts to modern challenges while maintaining its core effectiveness.

In early pandemic-era meetings, working groups grappled with validating their theoretical work against implementation reality. The [ippm](https://datatracker.ietf.org/wg/ippm/about/) working group exemplified this approach in March 2021:

> "we converted those shoulds to uh to a must and we've had a running code section in the draft since about last september uh when the running code was released"

This quote illustrates the iterative nature of IETF work—specifications evolve based on implementation experience, with actual code informing the tightening of requirements from suggestions ("shoulds") to mandates ("musts").

The principle's philosophical foundations were explicitly discussed in educational contexts, such as this November 2022 explanation from the [emodir](https://datatracker.ietf.org/wg/emodir/about/) working group:

> "the uh iesg um so I hinted a little bit earlier that we were going to talk about ietf and consensus um the uh Mantra I guess of the ietf is that we reject King's presidents and votings we believe in rough consensus and running code and this has been around for at least 30 years"

This articulation emphasizes the anti-authoritarian nature of IETF decision-making—rejecting both autocratic decisions and pure democracy in favor of merit-based consensus guided by working implementations.

Modern challenges to the principle emerged in discussions about existing deployments versus evolving standards. The [dispatch](https://datatracker.ietf.org/wg/dispatch/about/) working group in March 2023 faced exactly this tension:

> "we have 17 implementations and they deployed it and they've kind of decided that Z means something right and so if uh you know through consensus-based process we decide that Z means something else we would create a bit of Chaos"

This highlights a contemporary challenge: when "running code" has already established de facto standards, the consensus process must weigh backward compatibility against technical improvement. The principle doesn't just favor running code—it must grapple with the ecosystem effects of existing running code.

By July 2024, discussions showed both the persistence and evolution of the principle. The [dmm](https://datatracker.ietf.org/wg/dmm/about/) working group demonstrated the ongoing emphasis on implementation validation:

> "in the real world well something we running working on ITF running code R consensus so what you assume as a running system well we may develop a running system"

Meanwhile, the [grow](https://datatracker.ietf.org/wg/grow/about/) working group showed how the principle enables flexible standardization approaches:

> "just because something is mentioned does not mean people should or must use it um it's just an option um and that makes it ideally easier to find some form of rough consensus whether what is in there is actually okay"

This reflects a mature understanding of how rough consensus can embrace optional mechanisms rather than forcing universal agreement on single solutions.

## Historical Analysis

Analysis of IETF meetings 110-123 reveals consistent engagement with the principle of rough consensus and running code across the Internet engineering community, with notable patterns in both frequency and working group participation.

| Meeting | Date | Location | Discussions |
|---------|------|----------|-------------|
| IETF 110 | March 2021 | Online | 23 |
| IETF 117 | July 2023 | San Francisco | 30 |
| IETF 123 | July 2025 | Madrid | 32 |

The data shows sustained discussion with a notable increase in recent meetings, suggesting the principle remains highly relevant to contemporary Internet engineering challenges. The peak at IETF 123 (32 discussions) may reflect growing complexity in consensus-building as the Internet infrastructure matures and deployment considerations become more critical.

Working group participation patterns reveal interesting insights about where consensus and implementation challenges most frequently arise. The [ietf](https://datatracker.ietf.org/wg/ietf/about/) plenary sessions lead with 11 discussions, reflecting the principle's foundational role in IETF governance. The [emu](https://datatracker.ietf.org/wg/emu/about/) working group's 9 discussions suggest active consensus-building around EAP methods, while [netmod](https://datatracker.ietf.org/wg/netmod/about/)'s 8 discussions likely reflect ongoing implementation challenges in network modeling standards.

The [hackathon](https://datatracker.ietf.org/wg/hackathon/about/)'s presence with 7 discussions is particularly significant, demonstrating how the IETF's code-focused events directly embody the "running code" aspect of the principle. Similarly, operational working groups like [ippm](https://datatracker.ietf.org/wg/ippm/about/) and [grow](https://datatracker.ietf.org/wg/grow/about/) appear frequently, suggesting that measurement and routing groups regularly grapple with balancing theoretical improvements against deployed practice.

The breadth of participation—135 unique working groups—indicates that rough consensus and running code isn't confined to specific technical domains but rather permeates all areas of Internet standardization work, from security ([rats](https://datatracker.ietf.org/wg/rats/about/)) to routing ([lsr](https://datatracker.ietf.org/wg/lsr/about/)) to operational practices ([sidrops](https://datatracker.ietf.org/wg/sidrops/about/)).

## Resources

- [RFC 7282: On Consensus and Humming in the IETF](https://www.rfc-editor.org/rfc/rfc7282) — Essential reading for understanding how the IETF operationalizes consensus-building without formal voting
- [The Tao of IETF](https://www.ietf.org/about/participate/tao/) — Practical guide for newcomers explaining IETF culture, including how rough consensus works in practice
- [RFC 2026: The Internet Standards Process](https://www.rfc-editor.org/rfc/rfc2026) — Formal description of how implementation requirements and consensus evaluation fit into the standards track
- [David Clark's 1992 IETF presentation](https://www.ietf.org/about/participate/tao/) — Historical context for the original articulation of this principle
- [IETF Hackathon](https://www.ietf.org/how/runningcode/hackathons/) — See the "running code" principle in action through collaborative implementation events

---
*This report was generated from analysis of IETF working group session transcripts using vCon (virtual Conversation) data processing techniques.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `0fbed9be-ab53-430f-8a04-e5f386a4934d` |
Sessions analyzed: 331 |
Generated: 2026-03-14*
