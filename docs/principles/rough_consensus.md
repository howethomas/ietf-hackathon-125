# Rough consensus and running code

## Introduction

"Rough consensus and running code" stands as one of the most influential and enduring principles in Internet governance and protocol development. This deceptively simple phrase encapsulates the Internet Engineering Task Force's (IETF) approach to decision-making: address all concerns but don't let perfect become the enemy of good, and always prefer solutions backed by working implementations over purely theoretical proposals.

The principle emerged from the early culture of Internet development, where pragmatic engineers needed to build a functioning global network without getting bogged down in endless debates. It was formally articulated by David Clark and later codified in [RFC 7282](https://www.rfc-editor.org/rfc/rfc7282) by Pete Resnick in 2014. Unlike traditional standards bodies that might require unanimous agreement before proceeding, the IETF recognized that waiting for perfect consensus would paralyze innovation in the fast-moving world of Internet technology.

This principle has shaped not just how Internet protocols are developed, but how the Internet itself has evolved—prioritizing solutions that work in practice over those that are theoretically elegant. It reflects a fundamental truth about complex systems: sometimes you need to build something and see how it behaves in the real world before you can fully understand what the right answer should be.

## Understanding This Principle

**The Core Idea** — Move forward when you've addressed everyone's concerns but not necessarily accommodated everyone's preferences, and always prefer solutions that have been proven to work over those that merely sound good on paper.

Think of this like planning a neighborhood block party. You can't wait until every single neighbor agrees on every detail—the music, the food, the timing, the decorations—or the party will never happen. Instead, you listen to everyone's concerns (noise levels, parking, cleanup), address the serious issues, and move forward even if some people would prefer jazz over rock music. Most importantly, you choose vendors and activities that have actually worked at other block parties rather than untested ideas that sound great in theory but might fail spectacularly when 200 people show up.

The "running code" part means you don't just trust that the sound system will work—you test it first. You don't just assume the caterer is reliable—you check their references from other events. You prioritize proven solutions over theoretical ones, because when the day arrives, what matters is what actually functions, not what looked best in the planning documents.

**Why It Matters** — When organizations ignore this principle, they fall into two common traps: analysis paralysis and the "sounds good on paper" fallacy.

Analysis paralysis happens when teams spend months debating every possible edge case and trying to accommodate every stakeholder's wishes. A classic example is enterprise software projects that drag on for years because every department wants their specific requirements included, and no one is willing to make the hard decisions about what's truly essential versus what's merely nice-to-have. Meanwhile, competitors ship working solutions that capture the market.

The "sounds good on paper" fallacy occurs when organizations choose elegant theoretical solutions over battle-tested practical ones. Consider the history of networking protocols: many beautifully designed protocols have failed in practice because they made assumptions that didn't hold up under real-world conditions—network latency, hardware failures, human error, or simply the messiness of how systems actually get deployed. Meanwhile, seemingly inelegant protocols like TCP/IP succeeded because they had working implementations that people could actually use and improve incrementally.

**The Tension** — The real-world pressure against this principle comes from perfectionism and the fear of making the "wrong" choice. Engineers often want to solve every possible problem before shipping. Managers want to avoid criticism for not considering all stakeholders. Committees want to appear thorough and inclusive.

There's also a deeper tension between democracy and efficiency. True consensus feels more fair—everyone gets what they want—but it's often impossible in practice when dealing with complex technical decisions where tradeoffs are inevitable. The temptation is to keep talking until everyone agrees, but in fast-moving technical fields, the cost of delay often outweighs the benefits of perfect agreement.

Additionally, "running code" can feel risky to organizations used to extensive planning. Building something to test it requires investment without guarantee of success, and it can feel wasteful compared to just thinking through the problem more thoroughly. But this thinking trap assumes you can solve complex problems purely through analysis, when in reality many issues only become apparent when you try to implement solutions in practice.

**How to Recognize It** — You're seeing this principle at work when a team says "let's prototype the top three approaches and see which one actually works" instead of debating theoretical pros and cons indefinitely. You see it when a product manager says "we've heard everyone's feedback, addressed the major concerns, and now we need to ship and learn" rather than trying to make everyone completely happy before proceeding. You see it when an architect chooses a proven but imperfect technology over a newer, theoretically superior one that lacks production experience.

## Key References

- [RFC 7282: On Consensus and Humming in the IETF](https://www.rfc-editor.org/rfc/rfc7282) — The definitive explanation of how rough consensus works in practice and why it's essential for technical decision-making
- [The Tao of IETF](https://www.ietf.org/about/participate/tao/) — A practical guide to IETF culture and processes, including how rough consensus operates in real working groups
- [RFC 2026: The Internet Standards Process](https://www.rfc-editor.org/rfc/rfc2026) — The formal process description that codifies how running code and consensus interact in standards development

## This Principle in IETF Discussions

The conversation excerpts reveal how "rough consensus and running code" manifests in day-to-day IETF work, particularly around the critical interplay between theoretical proposals and practical implementation.

In the IPPM (IP Performance Metrics) working group, participants emphasized the importance of backing specifications with actual implementations:

> "we converted those shoulds to uh to a must and we've had a running code section in the draft since about last september uh when the running code was released"

This reflects a common pattern where initial drafts start with flexible recommendations ("shoulds") but evolve toward firmer requirements ("musts") as running code demonstrates what actually works in practice. The running code doesn't just validate the concept—it often reveals which aspects of the specification are essential versus optional.

The CFRG (Crypto Forum Research Group) demonstrated another aspect of the principle—how implementers use running code to validate new cryptographic approaches:

> "in the interest of running code i did implement it uh i added it to my implementation of hpke which is compliant with v"

Rather than just proposing a new encryption mode theoretically, the presenter built it into an existing implementation. This approach allows the working group to evaluate not just whether the concept is sound, but how it integrates with real systems and what practical issues emerge.

The SIDROPS (Secure Inter-Domain Routing Operations) group illustrated how running code helps validate complex distributed systems:

> "i'll give you an update on the testing we've conducted so far and the status of running codes and then i will conclude with a question to the group on what should be done next"

Security and routing protocols are particularly dependent on real-world testing because they involve complex interactions between multiple organizations and systems. The "question to the group on what should be done next" shows how running code results inform the rough consensus process—implementation experience directly shapes the group's decisions about future directions.

The rough consensus aspect appeared clearly in a DMARC working group discussion about email authentication:

> "i do think that's also rough consensus of uh of the group"

This comment came after a participant expressed "strong aversion" to a particular technical approach based on operational experience. The working group didn't need to take a formal vote—the chair could recognize that the group had heard the concerns and generally agreed on a direction forward, even if not everyone was completely satisfied.

## Historical Analysis

Analysis of the discussion frequency across IETF 110–123 reveals interesting patterns in how this principle has been applied:

| Meeting | Date | Sessions | Notable Context |
|---------|------|----------|----------------|
| IETF 110 | March 2021 | 23 | Transition back to in-person meetings |
| IETF 117 | July 2023 | 30 | Peak discussion period |
| IETF 123 | July 2025 | 32 | Highest frequency observed |

The principle saw increased discussion frequency over time, particularly jumping from the initial online-only meetings (IETF 110-112) to the hybrid and in-person meetings that followed. This suggests that face-to-face interaction may facilitate the kind of nuanced consensus-building that this principle requires.

The top working groups discussing this principle—IETF plenary (11 sessions), EMU (9 sessions), and NETMOD (8 sessions)—span very different technical domains. The high frequency in plenary sessions makes sense, as these often address process and cultural issues. EMU (EAP Method Update) and NETMOD (Network Modeling) represent areas where running code is particularly critical: authentication mechanisms and network management tools must work reliably in diverse real-world environments.

The broad distribution across 135 unique working groups demonstrates that this isn't just a process principle confined to governance discussions—it's a practical tool that working groups across all technical areas use to make progress on complex problems.

The hackathon's appearance in the top working groups (7 sessions) is particularly telling, as hackathons specifically exist to produce running code that can inform standards work. This represents the principle in its most literal form—creating implementations during the meeting itself to test ideas before they become formal specifications.

## Resources

- [RFC 7282: On Consensus and Humming in the IETF](https://www.rfc-editor.org/rfc/rfc7282) — Essential reading for understanding how rough consensus actually works in practice, with concrete examples of good and bad consensus processes
- [The Tao of IETF](https://www.ietf.org/about/participate/tao/) — A cultural guide that explains not just the formal rules but the unwritten norms about how consensus-building and implementation validation work in IETF culture
- [RFC 2026: The Internet Standards Process](https://www.rfc-editor.org/rfc/rfc2026) — The formal process documentation that shows how running code requirements are built into the standards track
- [David Clark's "A Cloudy Crystal Ball" (1992)](https://www.ietf.org/proceedings/24/slides/managerial-overview-1992-jul-13.pdf) — The classic presentation where Clark articulated "rough consensus and running code" as the IETF's core philosophy
- [IETF Datatracker](https://datatracker.ietf.org/) — Track real working group discussions and see how consensus formation and implementation requirements play out in current standardization work

---

*This report was generated from analysis of IETF working group session transcripts using vCon (Conversation Data Container) format, covering meetings 110-123 from March 2021 through July 2025.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `0fbed9be-ab53-430f-8a04-e5f386a4934d` |
Sessions analyzed: 331 |
Generated: 2026-03-14*
