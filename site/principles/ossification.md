# Protocol ossification

## Introduction

Protocol ossification represents one of the Internet's most insidious architectural challenges: the tendency for protocols to become rigid and resistant to change due to interference from middleboxes and the gradual loss of unused extension points. This phenomenon threatens the Internet's fundamental principle of evolvability, making it increasingly difficult to deploy new features or adapt protocols to emerging needs.

The principle is perhaps best captured in the maxim "use it or lose it" — protocol extension mechanisms that aren't regularly exercised in production networks gradually become unusable as middleboxes, firewalls, and other network infrastructure begin to treat any deviation from common patterns as suspicious or erroneous traffic. This insight was formalized in [RFC 9170: Long-Term Viability of Protocol Extension Mechanisms](https://www.rfc-editor.org/rfc/rfc9170), which provides comprehensive guidance on maintaining protocol extensibility over time.

Understanding and combating protocol ossification has become critical for the IETF's work, influencing everything from the design of new protocols like QUIC to the evolution of existing standards like TLS and HTTP. The principle shapes how protocol designers think about extension points, version negotiation, and the long-term health of Internet infrastructure.

## Understanding This Principle

**The Core Idea** — Protocol extension mechanisms become unusable if they're not regularly exercised in production traffic. Think of protocol ossification like unused fire exits in a large office building. When the building opens, all the emergency exits work perfectly and are clearly marked. But over time, if they're never used, facilities managers start storing equipment in front of them, maintenance crews forget to oil the hinges, and security systems begin treating anyone who uses these "unusual" exits as suspicious. Eventually, what were designed as safety valves become completely blocked — exactly when you need them most during an emergency.

In networking, protocols are designed with extension points — special fields, optional headers, or version numbers that allow future enhancements without breaking existing implementations. But if these mechanisms aren't regularly used, middleboxes (firewalls, load balancers, content filters) begin to assume that "normal" traffic never uses them. They start dropping packets with unfamiliar option codes or blocking connections that attempt version negotiation. The extension points calcify into unusable vestigial features.

**Why It Matters** — When protocols ossify, innovation grinds to a halt. Consider the difference between HTTP/2 deployment and QUIC deployment. HTTP/2 tried to evolve over existing TCP connections, but years of middlebox ossification around HTTP/1.1 patterns meant that many corporate firewalls and content filters broke HTTP/2 traffic. The deployment was slow and painful. In contrast, QUIC learned from this experience and was designed from day one with deliberate variation in its packet formats and aggressive use of encryption to prevent middleboxes from making assumptions about its internal structure. QUIC deployment has been dramatically faster as a result.

The consequences extend beyond just deployment speed. Ossified protocols create technical debt across the entire Internet ecosystem. Features that should take months to deploy instead take years or require complete protocol replacements. Security vulnerabilities become harder to patch when you can't safely modify protocol behavior. Performance improvements remain stranded in specifications that can't be deployed.

**The Tension** — The real-world pressure working against this principle is the fundamental conservatism of network operations. Network administrators are paid to keep things running, not to experiment with new protocol features. Middlebox vendors optimize for the common case — if 99.9% of traffic follows a predictable pattern, why complicate your firewall rules to handle edge cases that might be attack vectors? This creates a classic tragedy of the commons: everyone benefits from having extensible protocols, but no individual operator has sufficient incentive to exercise those extensions until they're needed.

There's also an inherent chicken-and-egg problem: protocol extensions aren't useful until enough endpoints support them, but extensions won't work reliably until enough middleboxes tolerate them. Breaking this deadlock requires coordinated effort that goes against the Internet's decentralized nature.

**How to Recognize It** — You're seeing this principle at work when:

* A new software feature requires "compatibility mode" flags to work through existing network infrastructure
* Protocol specifications include extensive lists of "implementation considerations" about middlebox behavior  
* Deployment guides spend more time explaining firewall configurations than the actual protocol features
* Engineers choose completely new protocols over extending existing ones, even when the extension would be technically simpler

## Early IETF Work

The IETF's understanding of protocol ossification emerged gradually through painful experience with protocol evolution in the 1990s and early 2000s. Early Internet protocols like IP and TCP were designed with seemingly ample extension space — IP had an options field, TCP had its own options mechanism, and many application protocols included version numbers and extensibility hooks. The original architects assumed that this flexibility would naturally accommodate future innovations.

However, as the Internet scaled and commercial middleboxes proliferated, these extension mechanisms began failing in unexpected ways. The deployment of IPv6, despite being standardized in 1998, encountered massive resistance partly because middleboxes had ossified around IPv4 assumptions. Similarly, TCP options beyond the most basic ones became increasingly unusable as firewalls and NAT devices started treating uncommon option combinations as potentially malicious traffic.

The HTTP/2 standardization process served as a crucial learning experience for the IETF community. Despite careful design and broad industry support, HTTP/2 deployment revealed how thoroughly HTTP/1.1 patterns had become embedded in proxy servers, content delivery networks, and corporate firewalls. This experience directly influenced the development of protocols like QUIC, which incorporated anti-ossification measures from the beginning rather than trying to retrofit them later. The IETF's growing awareness of ossification as a first-class architectural concern culminated in dedicated research groups and working groups focused on measuring and combating the phenomenon.

## Key References

* [RFC 9170: Long-Term Viability of Protocol Extension Mechanisms](https://www.rfc-editor.org/rfc/rfc9170) — The definitive guide to understanding and preventing protocol ossification, with concrete recommendations for protocol designers.
* [RFC 8701: GREASE (Generate Random Extensions And Sustain Extensibility)](https://www.rfc-editor.org/rfc/rfc8701) — Describes the technique of deliberately exercising extension points with random values to prevent ossification.
* [RFC 9000: QUIC Protocol](https://www.rfc-editor.org/rfc/rfc9000) — A modern protocol designed with extensive anti-ossification measures built in from the start.

## This Principle in IETF Discussions

The evolution of protocol ossification as a central concern in IETF work is clearly visible in working group discussions from 2021 to 2025. Early conversations focused heavily on documenting and formalizing the "use it or lose it" principle, with the [iabopen](https://datatracker.ietf.org/wg/iabopen/about/) working group driving much of the foundational work:

> "ently talking most about is actually one that existed prior to this program being created but we think is a very important work item that we want to progress that martin thompson began it's the draft use it or lose it and we've met now twice we had our last call in december and we're going to plan a"

This quote from IETF 110 shows the early prioritization of what would become RFC 9170, with Martin Thomson's "use it or lose it" draft being identified as a critical work item for the Internet Architecture Board.

By 2022, the focus had shifted from documentation to practical implementation, particularly around the GREASE technique for preventing ossification. The [quic](https://datatracker.ietf.org/wg/quic/about/) working group became a testing ground for anti-ossification strategies:

> "e're not expecting it to take a year from now um so i think the point lucas made in the um uh in the chat is probably the right one that this should take into account uh the fact that that quick will grease some of these things and it will have multiple versions some of which will be uh compatible a"

This discussion from IETF 113's [avtcore](https://datatracker.ietf.org/wg/avtcore/about/) session reflects how QUIC's built-in greasing mechanisms were influencing other protocol design efforts, with working groups explicitly considering how QUIC's approach to maintaining extensibility could be applied more broadly.

However, the practical challenges of implementing anti-ossification measures also became apparent. In IETF 115, the [masque](https://datatracker.ietf.org/wg/masque/about/) working group grappled with the tension between preventing ossification and avoiding unintended consequences:

> "is I I'm still not convinced that this is a good idea the the concept itself of partial reordering on the proxy uh because this starts to smell like a TCP accelerator uh and those have been great for ossification and making performance worse I have numbers for that one um so on that I'm not sure it'"

This comment highlights how fear of creating new ossification points can sometimes constrain protocol design, with engineers being cautious about features that might become problematic middlebox behaviors.

By 2023, discussions in the [edm](https://datatracker.ietf.org/wg/edm/about/) working group showed growing sophistication in understanding the limitations of anti-ossification techniques:

> "aised the question of how do we measure if greasing is actually effective or working and we talked about some of the limitations of you know there there's only really a certain category of issues and ossification bugs that greasing can help with and there are lots of other things that it does not um"

This reflects the maturing understanding that while techniques like GREASE are valuable, they're not panaceas — the community was developing more nuanced approaches to different types of ossification problems.

Recent discussions show the principle becoming institutionalized across multiple working groups. The [lake](https://datatracker.ietf.org/wg/lake/about/) working group's 2024 activities demonstrate how anti-ossification measures are now being built into protocols from the beginning rather than retrofitted:

> "sion. So in terms of the working group uh since the last uh ITF meeting we had a lot of activity going on mainly four documents have been adopted following the uh Dublin discussions. These are uh the grease document uh edited by Christian. App profiles edited by Marco Lake uh remote attestation work"

This systematic adoption of GREASE documents across multiple protocol efforts shows how the principle has evolved from an architectural concern to a standard engineering practice.

## Historical Analysis

The frequency of protocol ossification discussions across IETF meetings reveals several important trends in how the community has approached this challenge:

| Meeting Period | Sessions | Peak Discussion |
|----------------|----------|-----------------|
| Early (110-114) | 31 | IETF 113 (8 sessions) |
| Middle (115-119) | 21 | IETF 116 (8 sessions) |
| Recent (120-123) | 15 | IETF 121 (8 sessions) |

The data shows intense early activity as the IETF community worked to formalize the principle and develop practical countermeasures, followed by a gradual decline as the approaches became more standardized and routine. The peaks at IETF 113, 116, and 121 correspond to key milestone meetings where major documents were advancing or new applications of the principle were being explored.

The [quic](https://datatracker.ietf.org/wg/quic/about/) and [tls](https://datatracker.ietf.org/wg/tls/about/) working groups led early discussions, which makes sense given their role as pioneers in implementing comprehensive anti-ossification strategies. The later prominence of the [edm](https://datatracker.ietf.org/wg/edm/about/) working group reflects the community's shift toward more systematic analysis of extension mechanisms across all protocols.

Notably, the [lake](https://datatracker.ietf.org/wg/lake/about/) working group's consistent engagement with ossification concerns in more recent meetings demonstrates how the principle has become embedded in routine protocol design work. Rather than being an exceptional concern for a few high-profile protocols, preventing ossification is now considered standard practice across diverse protocol areas including IoT security, network time protocols, and core Internet infrastructure.

The geographic pattern of peak discussions — Vienna (IETF 113), Yokohama (IETF 116), and Dublin (IETF 121) — suggests that in-person meetings facilitated more intensive collaboration on these complex architectural issues, with working groups using face-to-face time to tackle the nuanced engineering challenges that ossification prevention requires.

## Resources

* [RFC 9170: Long-Term Viability of Protocol Extension Mechanisms](https://www.rfc-editor.org/rfc/rfc9170) — Essential reading for anyone designing extensible protocols, with concrete examples of what works and what fails in practice.
* [RFC 8701: GREASE (Generate Random Extensions And Sustain Extensibility)](https://www.rfc-editor.org/rfc/rfc8701) — Describes the most widely deployed technique for preventing ossification, with implementation guidance for protocol designers.
* [QUIC Protocol Documentation](https://www.rfc-editor.org/rfc/rfc9000) — Study QUIC as a case study in anti-ossification design, showing how modern protocols can be built to resist calcification from day one.
* [Path MTU Discovery for IP version 6](https://www.rfc-editor.org/rfc/rfc8201) — A historical example of how ossification problems compound over time, useful for understanding why prevention is easier than remediation.

---
*This report was generated from analysis of IETF working group session transcripts using vCon conversation analysis technology.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `c93a4657-0f71-49f0-b5f2-870455334d73` |
Sessions analyzed: 71 |
Generated: 2026-03-14*
