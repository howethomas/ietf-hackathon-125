# Rough consensus and running code

## Introduction

"Rough consensus and running code" stands as one of the foundational mantras of Internet engineering, embodying the IETF's pragmatic approach to building the world's most successful distributed system. This principle emerged from the early days of the Internet when Dave Clark famously declared that the IETF "rejects kings, presidents and voting" in favor of a decision-making process that addresses concerns without necessarily accommodating everyone, while preferring solutions backed by actual working implementations.

The principle is formally documented in [RFC 7282: On Consensus and Humming in the IETF](https://www.rfc-editor.org/rfc/rfc7282), which clarifies that consensus isn't about unanimous agreement or majority rule, but about addressing all issues and objections in a way that leaves participants feeling their concerns have been heard and considered. The "running code" component emphasizes that theoretical perfection matters less than practical solutions that demonstrably work in real-world conditions.

This approach has proven essential to Internet architecture because it balances the need for technical excellence with the reality of deployment at scale. Rather than endlessly debating theoretical edge cases, the IETF moves forward when there's reasonable agreement and evidence that proposed solutions actually function. This principle has enabled the Internet to evolve rapidly while maintaining interoperability across billions of devices, making it a cornerstone of how the world's most critical infrastructure gets designed and deployed.

## Understanding This Principle

**The Core Idea** — Build solutions that work in practice while addressing everyone's concerns, but don't let perfect become the enemy of good enough. Think of this like planning a neighborhood block party: you listen to everyone's input about timing, food, and activities, but at some point you pick a date and start cooking rather than endlessly debating whether Saturday at 3pm with BBQ is theoretically optimal for every single neighbor's schedule and dietary preferences.

In the block party analogy, "rough consensus" means most people think the plan is reasonable and their major concerns have been addressed — even if some would prefer different timing or menu options. "Running code" means you've actually tested whether your grill works, confirmed the park permit is valid, and verified that your planned activities fit in the available space. You don't wait until you've solved every possible edge case (what if it rains? what if someone's vegetarian cousin visits?) before moving forward.

**Why It Matters** — Without this principle, technical standards become either dictatorial or paralyzed. The dictatorial path leads to solutions imposed without considering real-world constraints, like a city planning department that designs beautiful bike lanes without consulting the people who actually bike to work. The paralyzed path leads to endless committee discussions that never produce anything deployable, like a software project that spends three years debating the perfect architecture but never ships a working product.

In networking specifically, we've seen both failure modes. Protocols designed by committee without running implementations often contain fatal flaws that only become apparent during deployment — like security vulnerabilities, performance bottlenecks, or interoperability problems. Meanwhile, protocols that ignore community input may technically work but fail to gain adoption because they don't address real operator needs or conflict with existing infrastructure.

**The Tension** — The pressure against this principle comes from two opposing forces: perfectionism and authoritarianism. Engineers naturally want elegant, theoretically complete solutions, while business pressures push for quick decisions without consultation. The perfectionist camp argues for delaying decisions until every edge case is analyzed and the solution is mathematically proven optimal. The authoritarian camp argues for moving fast by having experts make unilateral decisions without community input.

Both approaches feel faster in the short term. It's genuinely quicker to either have one person decide everything or to postpone all decisions until you've done exhaustive analysis. The rough consensus and running code approach feels messy and slow because it requires both building working prototypes and navigating human disagreements. The temptation is always to skip one half or the other.

**How to Recognize It** — You're seeing this principle at work when:

* A team chooses a slightly imperfect solution that everyone can live with over an elegant solution that half the team thinks is fundamentally wrong
* Architectural decisions are validated by building and testing actual implementations rather than relying purely on theoretical analysis  
* Technical discussions focus on addressing specific objections and use cases rather than achieving unanimous enthusiasm
* Projects ship working systems that get improved iteratively rather than waiting for complete specifications before any implementation begins

## Early IETF Work

The "rough consensus and running code" principle emerged organically from the Internet's early development process in the 1980s and 1990s, when the network was still small enough for its architects to experiment rapidly. Unlike traditional standards bodies that developed detailed specifications before implementation, Internet protocols evolved through a cycle of implementation, deployment, and refinement. The original TCP/IP protocol suite exemplifies this approach — rather than waiting for perfect specifications, researchers built working implementations, deployed them across the growing Internet, and refined the protocols based on operational experience.

The ARPANET-to-Internet transition in the early 1980s demonstrated both the power and necessity of this approach. The original Network Control Protocol (NCP) was replaced by TCP/IP not through committee decree but because TCP/IP implementations proved more robust and scalable in practice. The transition succeeded because multiple working implementations existed and operators could gradually migrate based on demonstrated benefits rather than theoretical promises.

However, the IETF also learned from cases where insufficient consensus or lack of running code led to problems. The OSI protocol suite, developed through more traditional standards processes with extensive theoretical analysis but limited early implementation, ultimately failed to gain Internet adoption despite significant industry investment. Similarly, some early Internet protocols succeeded technically but failed to gain adoption because they addressed theoretical problems rather than real operator needs, highlighting the importance of both halves of the "rough consensus and running code" formula.

## Key References

* [RFC 7282: On Consensus and Humming in the IETF](https://www.rfc-editor.org/rfc/rfc7282) — Pete Resnick's definitive guide to how IETF consensus works, clarifying that consensus means addressing objections rather than achieving universal agreement.
* [RFC 2026: The Internet Standards Process](https://www.rfc-editor.org/rfc/rfc2026) — The formal IETF process document that codifies how standards are developed, including the role of implementation experience in advancement.
* [The Tao of IETF](https://www.ietf.org/about/participate/tao/) — An informal guide to IETF culture and processes that explains the practical application of these principles.

## This Principle in IETF Discussions

The principle appears regularly in IETF discussions, often when working groups need to balance theoretical perfection against practical deployment needs. During IETF 110, the [ippm](https://datatracker.ietf.org/wg/ippm/about/) working group demonstrated the "running code" aspect when discussing performance measurement protocols:

> "e that you could make where this uh where the number of these sub intervals uh needed to be set to other than the conditions we had there so we converted those shoulds to uh to a must and we've had a running code section in the draft since about last september uh when the running code was released a"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf110/ietf110_ippm_28696.vcon.json)*

This illustrates how actual implementation experience informed specification decisions — the working group strengthened requirements based on what their running code revealed about necessary protocol behaviors.

The consensus-building aspect appeared in process discussions, as seen in the [rfcefdp](https://datatracker.ietf.org/wg/rfcefdp/about/) session at IETF 110:

> "think these are just in addition to this in what's in a so we we pretty much agreed that you know the working group is going to go through its its process to develop documents and then you know gain rough consensus roughly speaking using the same sort of processes uh that you would see in an ietf wo"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf110/ietf110_rfcefdp_28608.vcon.json)*

By the middle period, working groups were grappling with tensions between the principle's two components. At IETF 116, the [dispatch](https://datatracker.ietf.org/wg/dispatch/about/) working group faced a dilemma where running code existed but consensus was unclear:

> "a great uh question we have the the tension we have right now is that we have 17 implementations and they deployed it and they've kind of decided that Z means something right and so if uh you know through consensus-based process we decide that Z means something else we would create a bit of Chaos in"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf116/ietf116_dispatch_30127.vcon.json)*

This highlights how the principle creates productive tensions — when multiple implementations exist but interpret specifications differently, the IETF must balance respecting deployment reality with achieving technical consensus.

In recent meetings, the principle continued to guide practical decision-making. At IETF 120, the [grow](https://datatracker.ietf.org/wg/grow/about/) working group applied the consensus approach to contentious technical choices:

> "'t have to do any Judgment of methods um just because something is mentioned does not mean people should or must use it um it's just an option um and that makes it ideally easier to find some form of rough consensus whether what is in there is actually okay next slide please um the status of this th"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf120/ietf120_grow_33019.vcon.json)*

This shows how working groups achieve consensus by documenting options rather than mandating single solutions, allowing the community to address diverse needs without endless debate.

## Historical Analysis

Discussion of "rough consensus and running code" has remained consistently present across IETF meetings from 110 through 123, with notable variations in frequency and focus:

| Meeting | Date | Location | Frequency |
|---------|------|----------|-----------|
| IETF 110 | March 2021 | Online | 23 |
| IETF 111 | July 2021 | Online | 20 |
| IETF 112 | November 2021 | Online | 15 |
| IETF 113 | March 2022 | Vienna | 20 |
| IETF 114 | July 2022 | Philadelphia | 27 |
| IETF 115 | November 2022 | London | 22 |
| IETF 116 | March 2023 | Yokohama | 27 |
| IETF 117 | July 2023 | San Francisco | 30 |
| IETF 118 | November 2023 | Prague | 26 |
| IETF 119 | March 2024 | Brisbane | 20 |
| IETF 120 | July 2024 | Vancouver | 21 |
| IETF 121 | November 2024 | Dublin | 25 |
| IETF 122 | March 2025 | Bangkok | 23 |
| IETF 123 | July 2025 | Madrid | 32 |

The data shows peaks during IETF 117 (San Francisco) and IETF 123 (Madrid), possibly reflecting periods of intensive standards development or process discussions. The relatively low frequency during IETF 112 (November 2021, online) may reflect pandemic-related meeting dynamics affecting discussion patterns.

The working groups most frequently discussing this principle reveal interesting patterns. The [ietf](https://datatracker.ietf.org/wg/ietf/about/) working group leads discussions (11 instances), which makes sense as it focuses on IETF processes themselves. High frequency in [emu](https://datatracker.ietf.org/wg/emu/about/) (9 instances) and [netmod](https://datatracker.ietf.org/wg/netmod/about/) (8 instances) suggests these groups dealt with particularly contentious technical issues requiring explicit consensus-building.

The presence of [hackathon](https://datatracker.ietf.org/wg/hackathon/about/) (7 instances) in the top groups highlights how the IETF's emphasis on running code has formalized into dedicated implementation events. Meanwhile, operational groups like [ippm](https://datatracker.ietf.org/wg/ippm/about/) and [grow](https://datatracker.ietf.org/wg/grow/about/) (6 instances each) frequently invoke the principle when balancing measurement theory with deployment realities.

The broad distribution across 135 unique working groups demonstrates that this principle isn't confined to process discussions but actively guides technical work throughout the IETF. From routing protocols to security mechanisms, working groups consistently return to these concepts when navigating the inherent tensions between technical correctness and practical deployment.

## Resources

* [RFC 7282: On Consensus and Humming in the IETF](https://www.rfc-editor.org/rfc/rfc7282) — Essential reading for understanding how IETF consensus actually works, with practical examples of addressing objections without achieving universal agreement.
* [The Tao of IETF](https://www.ietf.org/about/participate/tao/) — An accessible introduction to IETF culture that explains how "rough consensus and running code" plays out in practice for newcomers.
* [RFC 2026: The Internet Standards Process](https://www.rfc-editor.org/rfc/rfc2026) — The formal process document showing how implementation requirements and consensus-building are built into Internet standards development.
* [IETF Datatracker](https://datatracker.ietf.org/) — Track real-time examples of how working groups apply these principles in current standardization efforts.

---
*This report was generated through analysis of IETF meeting transcripts converted to vCon format, covering meetings 110-123 (March 2021 - July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `0fbed9be-ab53-430f-8a04-e5f386a4934d` |
Sessions analyzed: 331 |
Generated: 2026-03-15*
