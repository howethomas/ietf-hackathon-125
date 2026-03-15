# Protocol ossification

## Introduction

Protocol ossification represents one of the Internet's most insidious architectural challenges: the gradual hardening of protocols into rigid, unchangeable forms due to the accumulation of middleboxes and implementations that make assumptions about protocol behavior. This principle, formally documented in [RFC 9170: Long-Term Viability of Protocol Extension Mechanisms](https://www.rfc-editor.org/rfc/rfc9170), embodies the "use-it-or-lose-it" reality of Internet protocol design—extension points and flexibility mechanisms that aren't actively exercised will eventually become unusable as the ecosystem calcifies around existing patterns.

The concept emerged from decades of painful experience with protocols like TCP and HTTP, where well-intentioned features became trapped by middlebox interference and implementation assumptions. When protocols deploy with extension mechanisms but these extensions remain unused, intermediate systems begin to treat any deviation from the observed norm as an error or attack. Over time, what was designed to be flexible becomes effectively immutable, forcing protocol designers to work around their own extension points or abandon them entirely.

This principle has become central to modern IETF protocol design, particularly influencing the development of QUIC, TLS 1.3, and other recent protocols. It represents a hard-learned lesson about the difference between theoretical extensibility and practical evolvability in Internet-scale systems, where the installed base of middleboxes and implementations can effectively veto protocol evolution regardless of what the specification permits.

## Understanding This Principle

**The Core Idea** — If you don't actively exercise the extension points in your protocol, they will become unusable over time due to interference from middleboxes and assumptions made by implementations.

Think of this like maintaining hiking trails in a national park. When a trail is regularly used by hikers, it stays clear and passable—the constant foot traffic keeps vegetation from overgrowing the path, fallen trees get reported and removed, and park rangers know to maintain the route. But if a trail goes unused for several seasons, nature reclaims it. Brush grows across the path, fallen logs block the way, and eventually the trail becomes so overgrown that it's impassable. Even though the trail was originally designed and built for hiking, without regular use, it effectively ceases to exist as a viable route.

In the same way, Internet protocols contain "trails" called extension points—reserved fields, optional parameters, version numbers, and negotiation mechanisms designed to allow future enhancements. But if these extension points aren't regularly exercised by real implementations carrying real traffic, the Internet ecosystem grows around them in ways that block their use. Firewalls start dropping packets with unfamiliar options. Load balancers begin to assume certain fields will always contain specific values. Software implementations take shortcuts based on what they've observed in practice rather than what the specification allows.

**Why It Matters** — When extension points ossify, protocols become evolutionary dead ends, forcing painful workarounds or complete replacement. Consider the difference between TCP and QUIC as a stark example. TCP includes various extension mechanisms, but decades of middlebox interference have made many of them unusable. Want to deploy new TCP options? Good luck getting them through enterprise firewalls and carrier-grade NAT systems that have learned to expect TCP packets to look a certain way. This ossification forced the IETF to develop QUIC as an entirely new transport protocol running over UDP, essentially abandoning TCP's extension points and starting fresh.

In contrast, QUIC was designed from day one with aggressive "greasing"—deliberately sending random, meaningless values in extension fields to ensure that any system intolerant of variation fails immediately during development rather than after widespread deployment. This preventive exercise of extension points keeps the evolutionary pathways open. The result is a protocol that can actually evolve, whereas TCP remains largely frozen despite being the foundation of Internet transport.

**The Tension** — The counterforce is simple: exercising unused extension points costs engineering time and increases complexity with no immediate benefit. Why implement and test protocol features you don't need today? Why risk introducing bugs or compatibility issues for hypothetical future use cases? Engineering teams face constant pressure to ship features that provide immediate value to users, not to maintain abstract extensibility. Additionally, adding variability to protocols can complicate testing, debugging, and operations. It's much easier to reason about a system that behaves predictably than one that exercises random variations "just in case."

This tension is exacerbated by the fact that ossification happens gradually and invisibly. Unlike a system failure that triggers immediate attention, ossification manifests as the slow erosion of future options—a classic tragedy of the commons where individual rational decisions collectively create a suboptimal outcome.

**How to Recognize It** — You're seeing this principle at work when:

* Your API includes optional parameters that no clients use, and you're afraid to remove them but suspect they wouldn't work if someone tried
* Your system's configuration format supports features that were never implemented, and now updating the parser risks breaking assumptions in downstream tools
* Your protocol includes version negotiation, but in practice only one version works reliably across different network environments due to middlebox interference
* Your database schema has "reserved for future use" columns that have been empty for years, and you're not sure if applications would handle non-null values correctly

## Early IETF Work

The roots of understanding protocol ossification stretch back to the early days of TCP/IP development, though the phenomenon wasn't well understood until years of deployment experience revealed its effects. The original Internet Protocol suite was designed with extensibility in mind—IPv4 included an Options field, TCP provided space for options and flags, and many application protocols included version negotiation mechanisms. The assumption was that these extension points would enable graceful evolution as needs changed.

However, the 1990s and early 2000s brought painful lessons about the gap between specification and reality. The deployment of Network Address Translation (NAT) devices, firewalls, and various "application-aware" middleboxes created a parallel evolution pressure that protocol designers hadn't anticipated. These devices made assumptions about protocol behavior based on observed traffic patterns rather than specification compliance. IPv4 options became largely unusable due to middlebox interference. TCP options faced similar problems, with many enterprise networks dropping packets containing unfamiliar option types. The IPv6 transition revealed how difficult it was to deploy even well-designed protocol evolution when the installed base of middleboxes wasn't prepared for change.

The IETF's response evolved gradually. Early efforts focused on documenting middlebox behavior and encouraging "liberal in what you accept" implementations, but experience showed this wasn't sufficient. The development of protocols like SCTP demonstrated that even clean-slate designs could face deployment challenges if they didn't account for existing middlebox ecosystems. It wasn't until the development of TLS 1.3 and QUIC that the community fully embraced proactive measures like greasing—deliberately exercising extension points to prevent ossification. These experiences culminated in the formal documentation of the "use-it-or-lose-it" principle in RFC 9170, representing decades of hard-won wisdom about protocol evolution in Internet-scale systems.

## Key References

* [RFC 9170: Long-Term Viability of Protocol Extension Mechanisms](https://www.rfc-editor.org/rfc/rfc9170) — The definitive documentation of protocol ossification and the "use-it-or-lose-it" principle
* [RFC 8701: GREASE (Generate Random Extensions And Sustain Extensibility)](https://www.rfc-editor.org/rfc/rfc8701) — Describes the technique of deliberately exercising extension points to prevent ossification
* [RFC 9000: QUIC Transport Protocol](https://www.rfc-editor.org/rfc/rfc9000) — A modern protocol designed with ossification prevention as a core principle

## This Principle in IETF Discussions

Protocol ossification has been a persistent theme across IETF working groups, reflecting both the historical pain of dealing with ossified protocols and the ongoing effort to prevent future ossification. The discussions reveal how this principle has evolved from a theoretical concern to a practical design requirement that shapes day-to-day protocol development.

In the early period of our analysis, the [iabopen](https://datatracker.ietf.org/wg/iabopen/about/) working group was actively developing what would become RFC 9170. During IETF 110 in March 2021, participants discussed the importance of this work:

> "ently talking most about is actually one that existed prior to this program being created but we think is a very important work item that we want to progress that martin thompson began it's the draft use it or lose it and we've met now twice we had our last call in december and we're going to plan a"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf110/ietf110_iabopen_28684.vcon.json)*

This early discussion shows the IETF recognizing the fundamental importance of formalizing lessons learned about protocol evolution. The work was considered critical enough to warrant dedicated attention from the Internet Architecture Board.

The [tls](https://datatracker.ietf.org/wg/tls/about/) working group's discussions during IETF 111 revealed how ossification concerns directly influence protocol design decisions:

> "ck one of which is having like a per specialization key um and one of which have like an ech based key um it's not entirely accurate which of these would prevent exactly what i think they all prevent ossification somewhat but like maybe some of the windfall streaming um i'm actually not entirely sur"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf111/ietf111_tls_28904.vcon.json)*

This quote illustrates how protocol designers must constantly evaluate whether their design choices will maintain flexibility or contribute to future ossification—a consideration that affects even detailed cryptographic design decisions.

In the middle period, working groups began implementing concrete anti-ossification measures. The [masque](https://datatracker.ietf.org/wg/masque/about/) working group's discussions at IETF 115 showed wariness about features that might contribute to ossification:

> "is I I'm still not convinced that this is a good idea the the concept itself of partial reordering on the proxy uh because this starts to smell like a TCP accelerator uh and those have been great for ossification and making performance worse I have numbers for that one um so on that I'm not sure it'"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf115/ietf115_masque_29955.vcon.json)*

This comment reflects the community's hard-learned lesson that well-intentioned middlebox features often become sources of ossification, constraining future protocol evolution in unexpected ways.

The [edm](https://datatracker.ietf.org/wg/edm/about/) working group at IETF 116 addressed the practical challenges of implementing anti-ossification measures:

> "aised the question of how do we measure if greasing is actually effective or working and we talked about some of the limitations of you know there there's only really a certain category of issues and ossification bugs that greasing can help with and there are lots of other things that it does not um"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf116/ietf116_edm_30421.vcon.json)*

This discussion highlights a mature understanding that even anti-ossification techniques have limitations and require careful evaluation of their effectiveness.

In recent meetings, the focus has shifted toward operationalizing these lessons. The [edm](https://datatracker.ietf.org/wg/edm/about/) working group at IETF 120 discussed providing more concrete guidance:

> "item we have that we have kind of agreed to work on is trying to give more concrete advice around greasing and things that look like greasing uh we have previous rfc's that we've produced uh like the use it or lose it document that cover things like greasing but uh did not go into some of the more p"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf120/ietf120_edm_33301.vcon.json)*

This evolution shows the IETF moving from understanding the problem to providing practical implementation guidance for protocol designers.

## Historical Analysis

The frequency of ossification discussions across IETF meetings reveals both the persistence of this concern and its gradual evolution from theoretical principle to operational practice:

| Meeting | Sessions | Notable Trend |
|---------|----------|---------------|
| IETF 110-114 (2021-2022) | 31 total | Peak academic interest, formalizing principles |
| IETF 115-119 (2022-2024) | 25 total | Implementation focus, practical experience |
| IETF 120-123 (2024-2025) | 15 total | Operational guidance, lessons learned |

The highest activity occurred during IETF 110-114, coinciding with the finalization of RFC 9170 and the integration of anti-ossification measures into protocols like QUIC and TLS 1.3. The [quic](https://datatracker.ietf.org/wg/quic/about/) working group led discussions with 7 sessions, which makes sense given that QUIC was designed as a clean-slate transport protocol with ossification prevention as a core principle.

Interestingly, the [edm](https://datatracker.ietf.org/wg/edm/about/) working group shows sustained engagement (6 sessions) as the community worked to distill lessons learned into actionable guidance for future protocol development. The [lake](https://datatracker.ietf.org/wg/lake/about/) working group's recent adoption of greasing documents shows how these principles are now being systematically applied to new protocol development efforts.

The decline in discussion frequency in recent meetings (IETF 120-123) likely reflects the maturation of understanding—ossification prevention has moved from an emerging concern to an established best practice that's simply built into modern protocol design processes.

Working groups dealing with constrained environments like [core](https://datatracker.ietf.org/wg/core/about/) (Constrained RESTful Environments) and those working on long-lived protocols like [ntp](https://datatracker.ietf.org/wg/ntp/about/) (Network Time Protocol) show particular interest, as they must balance extensibility with resource constraints and backward compatibility requirements respectively.

## Resources

* [RFC 9170: Long-Term Viability of Protocol Extension Mechanisms](https://www.rfc-editor.org/rfc/rfc9170) — Essential reading for understanding the formal treatment of protocol ossification and the use-it-or-lose-it principle
* [RFC 8701: GREASE (Generate Random Extensions And Sustain Extensibility)](https://www.rfc-editor.org/rfc/rfc8701) — Practical guidance on implementing anti-ossification measures through deliberate exercise of extension points
* [QUIC Protocol Documentation](https://datatracker.ietf.org/doc/html/rfc9000) — Example of a modern protocol designed with ossification prevention as a core principle from day one
* [Internet Architecture Board (IAB) Evolution Working Group](https://datatracker.ietf.org/wg/edm/about/) — Ongoing work on protocol evolution and extensibility best practices
* ["Protocol Ossification: The Internet's Silent Killer"](https://www.potaroo.net/ispcol/2016-05/ossify.html) — Accessible explanation of how ossification affects real Internet infrastructure

---

*This report was generated from analysis of IETF working group session transcripts (vCon format) covering meetings 110-123 (March 2021 - July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `c93a4657-0f71-49f0-b5f2-870455334d73` |
Sessions analyzed: 71 |
Generated: 2026-03-15*
