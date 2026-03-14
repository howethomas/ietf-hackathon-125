# Trust as architectural principle

## Introduction

Trust as an architectural principle represents one of the fundamental building blocks of secure Internet infrastructure. Formally articulated in [RFC 3724](https://www.rfc-editor.org/rfc/rfc3724) "The Rise of the Middle and the Future of End-to-End" (2004), this principle establishes that trust relationships must be explicitly defined and understood before any protocol design can begin. Rather than treating trust as an afterthought or assuming it will emerge naturally, this principle demands that architects first map out who trusts whom, for what purposes, and under what conditions.

The principle emerged from hard-won lessons about Internet security failures. Early Internet protocols often operated under implicit assumptions about trust—assuming, for instance, that all network operators were benevolent or that end systems could inherently trust routing information. As the Internet scaled and became more adversarial, these assumptions proved catastrophically naive. The principle now serves as a cornerstone for modern protocol design, influencing everything from routing security to IoT device authentication.

Within the IETF's work from March 2021 through July 2025, this principle has been actively discussed across 252 working group sessions spanning all 14 meetings in this period. Its consistent appearance across diverse working groups—from routing (SIDROPS) to DNS operations (DNSOP) to emerging technologies like supply chain integrity (SCITT)—demonstrates its foundational importance in contemporary Internet architecture.

## Understanding This Principle

**The Core Idea** — You cannot build secure systems without first explicitly defining who trusts whom and why.

Think of this like designing a corporate office building. Before an architect draws a single line, they must understand the trust relationships within the organization: Which departments need to collaborate closely? Who handles sensitive financial data? Which visitors should access which floors? Who has authority over building security? The architect doesn't assume these relationships—they explicitly map them out with management, then design physical spaces, access controls, and workflows that reflect these trust boundaries.

In the same way, Internet protocol designers must first understand the trust landscape before writing any code. Is this a protocol where end users need to trust their service provider? Should routers trust each other's announcements? Can IoT devices trust cloud services with sensitive data? These aren't technical questions—they're trust architecture questions that must be answered before the technical design begins.

**Why It Matters** — When trust relationships are left implicit or undefined, systems fail in spectacular and unpredictable ways.

Consider two approaches to designing a package delivery network. In the "trust-last" approach, engineers build an elegant system for routing packages efficiently, then later realize they need to prevent theft and fraud. They bolt on security measures: cameras here, locks there, background checks as an afterthought. The result is a patchwork system with unclear accountability and numerous vulnerabilities.

In contrast, the "trust-first" approach begins by mapping out the trust relationships: Customers trust the company to deliver packages intact. The company trusts drivers but verifies their routes. Distribution centers trust each other but authenticate all transfers. Package contents are trusted to senders and recipients only. With this trust map in place, engineers can design systems where every component knows exactly what it should trust, whom it should verify, and what evidence it needs to make those decisions.

Internet history is littered with protocols designed the first way. BGP routing, for example, was built assuming all network operators would behave honestly—a reasonable assumption for the early academic Internet, but disastrous when applied to the modern commercial Internet where route hijacks and traffic interception are common threats.

**The Tension** — Defining trust is hard, uncomfortable work that slows down development.

The pressure to skip trust definition is enormous. Trust conversations force difficult questions: Do we really trust our partners? What if our assumptions are wrong? How much should we trust users versus corporations versus governments? These discussions can be politically charged and technically complex. Meanwhile, developers want to start coding, managers want to see progress, and competitors are moving fast.

It's much easier to assume "we'll figure out security later" and jump straight into the fun technical challenges. This is especially tempting in rapidly evolving fields like IoT or blockchain, where the competitive pressure to ship quickly can override architectural discipline. The result is technical debt that compounds exponentially—every component built on unclear trust assumptions makes the eventual security retrofit more expensive and fragile.

**How to Recognize It** — You're seeing this principle at work when teams spend significant time upfront mapping trust relationships before building anything. When someone asks "but who actually needs to trust whom here?" before diving into implementation details. When security isn't a feature list but a fundamental constraint that shapes every design decision.

You're seeing it violated when security discussions happen only after the core system is "done," when trust is assumed rather than documented, or when different team members have conflicting assumptions about who trusts what in the system they're building together.

## Key References

- [RFC 3724: The Rise of the Middle and the Future of End-to-End](https://www.rfc-editor.org/rfc/rfc3724) — The foundational IAB document establishing trust as a core architectural principle for Internet protocols.
- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/publications/detail/sp/800-207/final) — Modern framework applying trust-first principles to enterprise network security.
- [RFC 8555: ACME](https://www.rfc-editor.org/rfc/rfc8555) — Practical example of trust anchor management in Web PKI certificate automation.

## This Principle in IETF Discussions

The principle of defining trust relationships before protocol design appears consistently across IETF working groups, though often in the context of specific technical challenges rather than abstract architectural discussions.

In routing security, the SIDROPS working group grappled with complex trust hierarchies in resource certification:

> "rta suggests that multiple signers subordinate to multiple different trust anchors could together composite a cms-signed object a issue i perceive there is that there co..."

This excerpt from IETF 110 illustrates the challenge of designing systems where multiple trust anchors must interact—a fundamental trust architecture problem that must be resolved before the cryptographic details can be finalized.

The GNAP working group faced the principle head-on when designing authorization protocols, with one participant explicitly invoking privacy-by-design methodology:

> "i have done some design using privacy by design which means that you identify the primary appointment first once you have the model component and once you have the trust relationship since we have no trust relationship it's impossible to do a privacy by design"

This quote from IETF 110 demonstrates how undefined trust relationships block not just security design, but privacy protection—you can't protect data flows you haven't mapped, and you can't map data flows without understanding trust boundaries.

Authentication mechanisms frequently surface trust architecture questions, as seen in the EMU working group's discussion of certificate pinning:

> "are we requiring it to be sorry pinned to the web pki or is this kind of like a simple enough uh you just load you need some trust anchor so you're gonna load the ones uh that are most available yeah this is just a trust anchor"

This IETF 111 exchange reveals how even seemingly simple technical decisions (which certificates to trust) require explicit choices about trust relationships—in this case, whether to trust the existing Web PKI infrastructure or establish independent trust anchors.

The T2TRG research group highlighted how trust terminology itself can be a barrier to clear thinking:

> "this is about roots of trust and trust anchors and these terms are sounds really confusing to some people even in the security space"

This observation from IETF 110 underscores why the principle emphasizes explicit definition—if security experts find trust concepts confusing, protocols built on implicit trust assumptions are doomed to fail.

## Historical Analysis

Discussion of trust as an architectural principle has remained remarkably consistent across IETF meetings from 110 through 123, appearing in every meeting with relatively stable frequency:

| Meeting | Date | Location | Discussion Count |
|---------|------|----------|------------------|
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

The data reveals several notable patterns. Peak discussion periods (IETF 113, 114, 116, and 118) correspond to in-person or hybrid meetings, suggesting that complex trust architecture discussions benefit from face-to-face interaction. The consistently high engagement across the full four-year span indicates this is not a passing concern but a persistent architectural challenge.

The working groups most frequently discussing trust reflect the Internet's evolving security priorities. SIDROPS (routing security) leads with 11 sessions, followed by DNSOP (DNS operations) with 9 sessions, highlighting ongoing efforts to retrofit trust relationships into foundational Internet infrastructure originally designed without explicit trust models. Emerging areas like RATS (remote attestation), SCITT (supply chain integrity), and ACE (authentication and authorization for constrained environments) each contributed 7, 6, and 7 sessions respectively, indicating that new protocol development is increasingly embracing trust-first design principles from the outset.

## Resources

- [RFC 3724: The Rise of the Middle and the Future of End-to-End](https://www.rfc-editor.org/rfc/rfc3724) — The seminal IAB document that established trust definition as a prerequisite for protocol design; essential reading for understanding the principle's origins and motivation.
- [Zero Trust Architecture (NIST SP 800-207)](https://csrc.nist.gov/publications/detail/sp/800-207/final) — Comprehensive framework showing how trust-first principles apply to modern enterprise networks; excellent for seeing the principle in practice at organizational scale.
- [RFC 8555: ACME (Automated Certificate Management Environment)](https://www.rfc-editor.org/rfc/rfc8555) — Concrete example of trust anchor management in the Web PKI; demonstrates how explicit trust relationships enable automated security at Internet scale.
- [Trust in Internet Infrastructure](https://www.iab.org/documents/correspondence-reports-documents/2019-2/trust-in-internet-infrastructure/) — IAB workshop report examining trust challenges across multiple Internet technologies and governance models.

---
*This report was generated from analysis of IETF working group session transcripts using vCon (Conversation Data Container) methodology.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `58c23ba4-cfc6-4837-a087-7163b5544553` |
Sessions analyzed: 252 |
Generated: 2026-03-14*
