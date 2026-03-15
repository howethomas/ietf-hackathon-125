# Trust as architectural principle

## Introduction

The principle that "trust relationships must be defined before protocol design" represents one of the most fundamental yet challenging aspects of Internet architecture. Codified in [RFC 3724](https://www.rfc-editor.org/rfc/rfc3724), this principle emerged from decades of hard-learned lessons about the critical importance of understanding who trusts whom, for what purposes, and under what circumstances before building the technical mechanisms that will enforce those relationships.

This principle sits at the heart of Internet security and governance debates. It recognizes that trust is not a technical afterthought but an architectural foundation — much like how a building's structural requirements must be understood before designing the electrical and plumbing systems. The Internet's early designers learned that protocols built without clear trust models often fail catastrophically when deployed at scale, creating security vulnerabilities, governance disputes, and operational nightmares that can persist for decades.

The ongoing relevance of this principle is evident in its consistent discussion across IETF working groups from 2021 through 2025, appearing in 252 sessions across 100 different working groups. From DNS security to IoT device authentication, from routing protocols to identity management, every major Internet protocol ultimately grapples with fundamental questions about trust relationships and how to encode them into technical systems.

## Understanding This Principle

**The Core Idea** — You must decide who trusts whom before you design how they'll interact. Think of this like designing the governance structure for a new city: before you build the roads, utilities, and buildings, you need to establish whether there will be neighborhood councils, a mayor, federal oversight, or some other authority structure. The technical infrastructure follows from these trust relationships, not the other way around.

Consider a simple real-world analogy: a farmers market. Before opening day, organizers must decide fundamental trust questions: Do customers trust individual farmers to accurately represent their produce, or do they need a central market authority to certify everything? Do farmers trust other farmers not to misrepresent their goods, or do they need enforceable stall assignments? Do both trust the market operator to handle disputes fairly? These aren't technical questions about payment systems or stall construction — they're foundational trust relationships that determine how everything else gets designed.

**Why It Matters** — When you violate this principle, you end up with systems that work fine in small, controlled environments but collapse under real-world conditions. The classic example is building a protocol that assumes all participants are honest, then discovering in deployment that malicious actors can exploit these assumptions to disrupt or compromise the entire system.

Consider the difference between a system designed with clear trust boundaries versus one where trust relationships are an afterthought. A well-designed system might explicitly require that routing announcements be cryptographically signed by authorized entities, creating clear accountability. A poorly designed system might simply assume that anyone announcing routes is trustworthy, leading to the kinds of BGP hijacking attacks that have plagued the Internet for decades. The technical mechanisms are secondary to the fundamental question: who do we trust to announce what routes, and how do we verify that trust?

**The Tension** — The pressure against this principle is enormous because defining trust relationships is politically and organizationally hard, while building technical mechanisms feels like "real work." Engineers often want to start coding immediately, and trust conversations can feel abstract or contentious. It's much easier to say "we'll figure out the security model later" than to have difficult conversations about who should have what authority over whom.

Furthermore, trust relationships often cross organizational boundaries, requiring coordination between groups that may have competing interests. A protocol designer working on their piece of the puzzle may not want to wait for broader consensus on trust models, especially when those conversations involve lawyers, policy makers, and business stakeholders rather than just engineers.

**How to Recognize It** — You're seeing this principle at work when:

* A design document begins with explicit threat models and trust assumptions rather than jumping straight to protocol mechanics
* Working groups spend significant time debating "who should be authorized to..." questions before designing the authorization mechanisms themselves
* Protocols include explicit trust anchor configuration rather than assuming some universal trust infrastructure
* Security analysis focuses on trust boundary violations and what happens when trust relationships change over time

## Early IETF Work

The roots of this principle can be traced back to some of the Internet's earliest security disasters and design debates. The original Internet protocols were largely designed for a research environment where all participants were known and generally trustworthy. As the network expanded beyond academic institutions, the implicit trust assumptions embedded in protocols like the original routing protocols and email systems became serious vulnerabilities.

A key lesson emerged from the deployment of BGP (Border Gateway Protocol), where the assumption that all autonomous system operators would behave honestly led to persistent security problems. The lack of explicit trust relationships in the original design made it extremely difficult to retrofit authentication and authorization mechanisms later. Similar patterns emerged in DNS, where the original design's implicit trust model had to be extensively retrofitted with DNSSEC to provide cryptographic verification of responses.

The [IPSEC architecture work](https://www.rfc-editor.org/rfc/rfc2401) in the 1990s represented one of the first systematic attempts to make trust relationships explicit in Internet protocol design. Rather than assuming that network communications were secure, IPSEC began with explicit threat models and trust assumptions, then built cryptographic mechanisms to enforce those relationships. This approach influenced subsequent security protocol designs and helped establish the principle that trust relationships must be architectural foundations rather than afterthoughts.

## Key References

* [RFC 3724: The Rise of the Middle and the Future of End-to-End](https://www.rfc-editor.org/rfc/rfc3724) — The seminal IAB document that articulates this and other key architectural principles for Internet design.
* [RFC 2401: Security Architecture for the Internet Protocol](https://www.rfc-editor.org/rfc/rfc2401) — An early example of explicit trust modeling in protocol design.
* [RFC 4033: DNS Security Introduction and Requirements](https://www.rfc-editor.org/rfc/rfc4033) — Shows how trust relationships were retrofitted into an existing protocol.

## This Principle in IETF Discussions

The principle of defining trust relationships before protocol design emerges consistently across IETF working groups, often in the context of designing authentication and authorization mechanisms for new protocols or extending existing ones.

In early 2021 discussions, the [gnap](https://datatracker.ietf.org/wg/gnap/about/) working group grappled directly with this principle:

> "am very concerned with privacy and i have done some design using privacy by design which means that you identify the primary appointment first once you have the model component and once you have the trust relationship since we have no trust relationship it's impossible to do a privacy by design at t"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf110/ietf110_gnap_28577.vcon.json)*

This quote illustrates the foundational nature of trust relationships — even privacy-preserving design, which might seem like a purely technical challenge, depends on first establishing who trusts whom and for what purposes. The GNAP working group was designing next-generation authorization protocols and discovering that technical privacy mechanisms are meaningless without clear trust boundaries.

The [anima](https://datatracker.ietf.org/wg/anima/about/) working group's discussions in IETF 110 showed how trust relationships become particularly complex in automated systems:

> "working on we had some some rework specifically in the use case too regarding the push what we called the push model because in the last itf meeting and also in the design team we discussed about the trust relationship between the device of the agent that is basically onboarding the pledge and in th"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf110/ietf110_anima_28679.vcon.json)*

This reflects the challenge of defining trust relationships in scenarios where devices must automatically establish trust without human intervention — a fundamental challenge for IoT and autonomous network management systems.

By 2022, the [lake](https://datatracker.ietf.org/wg/lake/about/) working group was demonstrating mature application of this principle:

> "e protocol so this is addressing that the issues with mentioned in the previous slide thanks a lot so here is the details of the protocol or some of the details and this first we look at what are the trust relationships we assume between these nodes for some reason we've given the nodes names U V an"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf115/ietf115_lake_29921.vcon.json)*

This quote shows the principle being applied correctly — beginning protocol design by explicitly enumerating trust relationships between different entities rather than assuming them or building them implicitly into the technical mechanisms.

The evolution toward zero-trust architectures is evident in more recent discussions. The [6lo](https://datatracker.ietf.org/wg/6lo/about/) working group in 2022 discussed extending zero-trust principles to routing:

> "owned by a single node or if the different owners share the same key then it's possible to ensure that a route can only be injected in the routing fabric by the real owners okay so the same zero conf zero trust I'm sorry the same zero trust capabilities we have for host now becomes available for pre"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf115/ietf115_6lo_29941.vcon.json)*

This reflects how the principle has evolved to embrace explicit distrust as a design foundation — rather than assuming network components will behave correctly, modern protocols increasingly require cryptographic proof of authorization for every action.

By 2024, working groups like [oauth](https://datatracker.ietf.org/wg/oauth/about/) were dealing with complex multi-party trust relationships:

> "says that it's okay for me to get an access token to access this data uh and then it can respond with an access token the reason that this can work is because again both of these applications have a trust relationship with the Enterprise IDP through a single sideon so we're able to actually have a c"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf120/ietf120_oauth_33158.vcon.json)*

This illustrates how modern identity and authorization systems must carefully choreograph multiple trust relationships — not just between a user and a service, but between services, identity providers, and various organizational boundaries.

## Historical Analysis

Discussion of trust as an architectural principle has remained remarkably consistent across IETF meetings from 110 through 123, appearing in every single meeting with relatively stable frequency:

| Meeting | Date | Location | Sessions |
|---------|------|----------|----------|
| IETF 110 | March 2021 | Online | 19 |
| IETF 111 | July 2021 | Online | 11 |
| IETF 112 | November 2021 | Online | 13 |
| IETF 113 | March 2022 | Vienna | 22 |
| IETF 114 | July 2022 | Philadelphia | 22 |
| IETF 115 | November 2022 | London | 18 |
| IETF 116 | March 2023 | Yokohama | 22 |
| IETF 117 | July 2023 | San Francisco | 14 |
| IETF 118 | November 2023 | Prague | 22 |
| IETF 119 | March 2024 | Brisbane | 16 |
| IETF 120 | July 2024 | Vancouver | 17 |
| IETF 121 | November 2024 | Dublin | 19 |
| IETF 122 | March 2025 | Bangkok | 17 |
| IETF 123 | July 2025 | Madrid | 20 |

The most frequent discussions occur in working groups dealing with security infrastructure and identity management. The [sidrops](https://datatracker.ietf.org/wg/sidrops/about/) working group leads with 11 discussions, reflecting ongoing work to retrofit trust relationships into Internet routing. The [dnsop](https://datatracker.ietf.org/wg/dnsop/about/) working group follows with 9 discussions, as DNS continues to grapple with trust anchor management and secure resolution.

Notably, newer working groups like [scitt](https://datatracker.ietf.org/wg/scitt/about/) (Supply Chain Integrity, Transparency and Trust) and [rats](https://datatracker.ietf.org/wg/rats/about/) (Remote ATtestation ProcedureS) appear prominently, indicating that trust-as-architecture is central to emerging security protocols rather than just legacy retrofit efforts.

The principle spans an extraordinarily broad range of working groups — 100 different groups in total — suggesting that trust relationship definition is not a specialized security concern but a fundamental aspect of almost all Internet protocol design work.

## Resources

* [RFC 3724: The Rise of the Middle and the Future of End-to-End](https://www.rfc-editor.org/rfc/rfc3724) — Essential reading for understanding the architectural principles that guide Internet design, including detailed discussion of trust relationships.
* [NIST Special Publication 800-207: Zero Trust Architecture](https://csrc.nist.gov/publications/detail/sp/800-207/final) — Modern treatment of how to build systems that make trust relationships explicit rather than implicit.
* [RFC 4949: Internet Security Glossary, Version 2](https://www.rfc-editor.org/rfc/rfc4949) — Comprehensive definitions of trust-related terminology used in Internet standards.
* [Security Engineering by Ross Anderson](https://www.cl.cam.ac.uk/~rja14/book.html) — Classic textbook with excellent coverage of how trust models translate into technical security mechanisms.

---

*This report was generated from analysis of IETF meeting vCon (virtual conversation) records covering meetings 110-123 (March 2021 - July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `58c23ba4-cfc6-4837-a087-7163b5544553` |
Sessions analyzed: 252 |
Generated: 2026-03-15*
