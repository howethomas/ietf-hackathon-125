# Tussle in cyberspace

## Introduction

"Tussle in cyberspace" is one of the Internet's foundational design principles, articulating a profound truth about network architecture: the Internet is not just a technical system, but a social and economic battleground where different stakeholders constantly compete for control, resources, and advantage. This principle emerged from the seminal 2002 paper ["Tussle in Cyberspace: Defining Tomorrow's Internet"](https://groups.csail.mit.edu/ana/Publications/PubPDFs/Tussle2002.pdf) by David D. Clark, John Wroclawski, Karen R. Sollins, and Robert Braden, which fundamentally changed how Internet architects think about protocol design.

The principle argues that Internet protocols should be designed not to eliminate these tensions—an impossible task—but to accommodate them gracefully. Rather than trying to pick winners or enforce particular business models, the architecture should provide a neutral playing field where different interests can compete and evolve over time. This approach has been crucial to the Internet's success, allowing it to adapt to countless unforeseen uses while remaining robust in the face of competing commercial, governmental, and social pressures.

In the IETF's work from 2021 to 2025, this principle has remained highly relevant, appearing in discussions across 50 sessions and 13 meetings. As the Internet faces new challenges around privacy, content moderation, economic models, and geopolitical tensions, understanding how to design for tussle rather than against it has become more critical than ever.

## Understanding This Principle

**The Core Idea**

Design Internet protocols to accommodate inevitable conflicts between stakeholders rather than trying to resolve them.

Think of this like designing a city's road system. A naive approach might try to eliminate traffic conflicts by dictating exactly where every type of vehicle can go—delivery trucks only on certain streets, taxis banned from residential areas, bicycles confined to specific lanes. But this rigid approach would fail spectacularly because the city's needs constantly evolve. New businesses emerge, neighborhoods change character, and transportation technology advances. Instead, successful cities design flexible road systems with general rules of the road, traffic signals, and enforcement mechanisms that let different types of users negotiate their conflicts dynamically. The system doesn't prevent competition for road space—it provides a framework where that competition can happen safely and fairly.

**Why It Matters**

When protocol designers ignore the tussle principle, they typically try to "solve" political or economic problems through technical means—and this backfires dramatically. Consider early attempts at digital rights management in streaming protocols. Engineers tried to build copyright enforcement directly into the technical architecture, assuming they could prevent piracy through clever crypto and access controls. This approach failed because it ignored the fundamental tussle between content creators (who wanted control), consumers (who wanted convenience), and technology companies (who wanted to build platforms). The protocols became brittle, user-hostile, and ultimately ineffective.

In contrast, successful Internet protocols like HTTP and TCP work precisely because they don't take sides in the business and social tussles happening above them. HTTP doesn't care whether you're serving cat videos or academic papers—it just moves data reliably. This neutrality allowed an explosion of innovation because entrepreneurs, activists, governments, and corporations could all build on the same foundation while competing at higher layers.

**The Tension**

The pressure to violate this principle is enormous and constant. Engineers naturally want to "solve" problems they see, especially when those problems cause real harm. If spam is clogging email, why not build anti-spam directly into the email protocol? If misinformation spreads on social platforms, why not require truth verification in the underlying communication standards? If some companies have too much power, why not engineer in limitations?

This interventionist impulse is understandable but dangerous. When protocol designers try to encode particular solutions to social problems, they're essentially picking winners and losers in disputes they don't fully understand—and freezing those choices into infrastructure that's extremely hard to change. What looks like a clear-cut technical fix often becomes a straitjacket that prevents adaptation as society's needs evolve.

**How to Recognize It**

You're seeing this principle at work when protocols provide mechanisms rather than policies—giving parties tools to negotiate their own arrangements rather than enforcing particular outcomes. When Bitcoin provides a way to transfer value without specifying what should be valuable. When encrypted messaging protocols protect privacy without defining what communications are legitimate. When cloud computing APIs let customers deploy any software without the cloud provider controlling what applications are worthwhile.

You can spot violations of this principle when technical systems try to be judge and jury—when protocols embed assumptions about what business models are good, which uses are legitimate, or how social problems should be solved. These systems may work in the short term but tend to become obsolete as the world changes around their hardcoded assumptions.

## Key References

- [Tussle in Cyberspace: Defining Tomorrow's Internet](https://groups.csail.mit.edu/ana/Publications/PubPDFs/Tussle2002.pdf) — The foundational 2002 paper by Clark, Wroclawski, Sollins, and Braden that introduced this principle and changed how Internet architects think about protocol design.

## This Principle in IETF Discussions

The principle of designing for tussle appears frequently in IETF working group discussions, often when participants grapple with competing stakeholder interests that cannot be resolved through technical means alone. These conversations reveal how the principle guides practical protocol design decisions.

In the EMAILCORE working group at IETF 120, participants wrestled with email authentication mechanisms where perfect technical solutions are impossible:

> "there's not going to be perfect here and by no means will there be perfect here there's there's a there's a tussle going on in in in all this as we've heard and so there has to be really clear words as to how"

This excerpt captures the essence of the tussle principle—recognizing that email involves competing interests (senders wanting deliverability, receivers wanting to block spam, providers wanting to reduce costs) that cannot be perfectly reconciled. Instead of trying to engineer away these tensions, the working group focused on creating clear mechanisms that let different parties negotiate their own solutions.

The Human Rights Protocol Considerations (HRPC) working group frequently encounters tussle dynamics when examining how technical standards affect social values. At IETF 118, a participant explicitly referenced the concept:

> "I think are you familiar with the idea we talk about here often of a tussle the kind of disagreement tension between two parties in a conversation it happens a lot here"

This acknowledgment reflects how the HRPC working group has embraced tussle as a lens for understanding their work. Rather than trying to encode specific human rights outcomes into protocols, they focus on ensuring that protocols don't inadvertently foreclose important social negotiations.

The tension between standardization and implementation reality emerged clearly in EDM working group discussions. At IETF 123, participants debated how to handle situations where implementations diverge from specifications:

> "we still at the ITF have to put our specification first. We shouldn't be like I understand there is a value of running code what has actually worked but not give up our stuff in the middle there is a tussle there because people come all the time to the IT say this is already implemented I'm not goin"

This quote illustrates the institutional tussle within the IETF itself—between the standards process and market reality. The working group recognized they couldn't simply ignore deployed code, but also couldn't abandon their standardization mission. The solution involves creating mechanisms that accommodate both perspectives rather than choosing sides.

In Internet of Things contexts, the IOTOPS working group at IETF 118 discussed certificate management challenges:

> "I think we have a real a real tussle here right because you you many cases you just don't ever want those things to ever expire"

Here the tussle emerges between security best practices (regular certificate rotation) and operational reality (devices that may never be updated). Rather than mandating one approach, effective protocols need to provide flexibility for different deployment scenarios.

## Historical Analysis

The frequency of tussle-related discussions across IETF meetings from 110 to 123 shows interesting patterns:

| Meeting | Date | Location | Discussions |
|---------|------|----------|-------------|
| IETF 110 | March 2021 | Online | 4 |
| IETF 111 | July 2021 | Online | 1 |
| IETF 112 | November 2021 | Online | 3 |
| IETF 113 | March 2022 | Vienna | 3 |
| IETF 114 | July 2022 | Philadelphia | 5 |
| IETF 115 | November 2022 | London | 2 |
| IETF 116 | March 2023 | Yokohama | 3 |
| IETF 117 | July 2023 | San Francisco | 1 |
| IETF 118 | November 2023 | Prague | 7 |
| IETF 120 | July 2024 | Vancouver | 7 |
| IETF 121 | November 2024 | Dublin | 7 |
| IETF 122 | March 2025 | Bangkok | 3 |
| IETF 123 | July 2025 | Madrid | 4 |

Discussion frequency increased significantly from 2023 onward, with IETF 118, 120, and 121 showing the highest activity. This trend coincides with growing tensions around Internet governance, content moderation, and geopolitical fragmentation—all areas where the tussle principle becomes particularly relevant.

The Human Rights Protocol Considerations (HRPC) working group leads discussions with 7 sessions, reflecting their explicit focus on how technical standards interact with social and political conflicts. The Global Access to the Internet for All (GAIA) research group follows with 4 sessions, examining how Internet architecture affects global digital divides. The diversity of working groups—spanning 29 different groups from core Internet protocols to emerging applications—demonstrates how broadly this principle applies across Internet standards work.

Notably, the principle appears most frequently during periods of heightened external pressure on Internet governance, suggesting that IETF participants increasingly recognize the importance of designing protocols that can withstand various social and political forces without breaking.

## Resources

- [Tussle in Cyberspace (original paper)](https://groups.csail.mit.edu/ana/Publications/PubPDFs/Tussle2002.pdf) — Essential reading that introduces the concept with clear examples and explains why Internet architecture must accommodate rather than resolve stakeholder conflicts.
- [RFC 3724: The Rise of the Middle](https://www.rfc-editor.org/rfc/rfc3724) — Explores how Internet architecture creates space for innovation by avoiding over-specification at protocol layers.
- [HRPC Research Group](https://datatracker.ietf.org/rg/hrpc/about/) — The working group that most frequently applies tussle analysis to examine how protocol design decisions affect human rights and social values.

---
*This report was generated from analysis of IETF working group session transcripts using vCon (virtual Conversation) data from meetings 110-123.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `38a47da1-a32e-4d6d-83a0-8bf23b00bf8b` |
Sessions analyzed: 50 |
Generated: 2026-03-14*
