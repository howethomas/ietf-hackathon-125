# Protocol Ossification

## Introduction

Protocol ossification represents one of the most persistent and challenging problems in Internet architecture: the tendency for protocols to become rigid and resistant to change over time due to middlebox interference and implementation constraints. This phenomenon occurs when intermediate network devices—firewalls, NATs, deep packet inspection systems, and other middleboxes—begin to rely on specific protocol behaviors or field values, making it increasingly difficult to evolve protocols without breaking existing deployments. The principle is often summarized as "use-it-or-lose-it," emphasizing that protocol extension points must be actively exercised to remain viable for future use.

The concept gained particular prominence in IETF discussions during the development of QUIC and other modern protocols, where engineers observed firsthand how even well-designed extension mechanisms could become unusable if not regularly activated. This led to formal documentation of the problem in [RFC 9170](https://www.rfc-editor.org/rfc/rfc9170), which provides comprehensive guidance on designing protocols that can resist ossification. The principle has become central to modern protocol design, influencing everything from transport protocols to application-layer security mechanisms.

Understanding and mitigating protocol ossification is crucial for maintaining the Internet's capacity for innovation and evolution. Without active measures to prevent it, today's extension points become tomorrow's immutable constraints, potentially forcing the development of entirely new protocols when evolutionary changes would have sufficed.

## Key References

- [RFC 9170: Long-Term Viability of Protocol Extension Mechanisms](https://www.rfc-editor.org/rfc/rfc9170) — The definitive guide to understanding and preventing protocol ossification, documenting best practices for maintaining protocol evolvability.
- [RFC 8701: GREASE (Generate Random Extensions And Sustain Extensibility)](https://www.rfc-editor.org/rfc/rfc8701) — Describes a mechanism for exercising protocol extension points to prevent ossification through regular use of reserved values.
- [RFC 9000: QUIC Transport Protocol](https://www.rfc-editor.org/rfc/rfc9000) — Demonstrates modern anti-ossification techniques in practice, including extensive use of GREASE and encrypted transport headers.

## This Principle in IETF Discussions

Protocol ossification has been a recurring theme across numerous IETF working groups, reflecting both the broad applicability of the principle and the ongoing challenges it presents to protocol designers. The discussions reveal how this principle has evolved from an abstract concern to a concrete design requirement with specific technical solutions.

The Internet Architecture Board (IAB) played a central role in formalizing understanding of this principle. During IETF 110, participants discussed the progression of Martin Thomson's foundational work:

> "ently talking most about is actually one that existed prior to this program being created but we think is a very important work item that we want to progress that martin thompson began it's the draft use it or lose it and we've met now twice we had our last call in december and we're going to plan a"

This discussion from the IABOPEN working group highlights how the "use it or lose it" concept emerged as a critical architectural principle worthy of formal documentation. The IAB's focus on this work underscores its fundamental importance to Internet architecture. By IETF 111, the document had gained significant momentum within the IAB's evolution program:

> "to have a look at it and then i really wanted to draw your attention at um there are a few more documents that are somehow on the horizon for the iap but the one which is called draft ib lucid or um use it or lose it it's the one that is like probably the next one we will look at in evolution that's"

The principle's practical implications became evident in protocol-specific working groups. In the TLS working group at IETF 111, engineers grappled with how different design approaches could address ossification concerns:

> "ck one of which is having like a per specialization key um and one of which have like an ech based key um it's not entirely accurate which of these would prevent exactly what i think they all prevent ossification somewhat but like maybe some of the windfall streaming um i'm actually not entirely sur"

This discussion illustrates the complexity of applying anti-ossification principles to specific protocol mechanisms, where multiple design choices might offer different degrees of protection against rigidity.

The QUIC working group's experience with GREASE mechanisms shows how theoretical principles translate into concrete protocol features. At IETF 113, the working group discussed the progression of their anti-ossification measures:

> "the reviewers from the various areas um and for the editors in responding to those issues uh i think we're in a good place we will be working with our head to progress onto the next stage um and the grease bit document uh is dura shepherd write-up from me um so that's on me and that'll be coming soo"

QUIC's implementation of GREASE represents one of the most comprehensive applications of anti-ossification principles, making it a valuable case study for other protocol designers. The protocol actively exercises extension points to ensure they remain usable for future innovations.

The Evolution, Deployability, and Maintainability (EDM) working group explicitly incorporated ossification prevention into its charter. As discussed at IETF 114:

> "been two years yeah weird evolvability deployability and maintainability so evolvability um i think is mainly around taking up some of the work that had been done previously in iab around preventing ossification figuring out how do we maintain extensibility that's related to one of the documents we'"

This integration shows how ossification concerns have become embedded in the IETF's broader thinking about protocol lifecycle management, extending beyond individual protocols to systematic approaches for maintaining Internet architecture flexibility.

## Historical Analysis

The discussion of protocol ossification across IETF 110-123 reveals several important trends in how the Internet engineering community has approached this challenge. The frequency of discussions peaked during the early meetings of this period, particularly around IETF 113 and IETF 116, when foundational work was being completed and practical applications were being developed.

| Meeting | Date | Location | Discussion Frequency |
|---------|------|----------|---------------------|
| IETF 110 | March 2021 | Online | 7 |
| IETF 111 | July 2021 | Online | 6 |
| IETF 112 | November 2021 | Online | 5 |
| IETF 113 | March 2022 | Vienna | 8 |
| IETF 114 | July 2022 | Philadelphia | 5 |
| IETF 115 | November 2022 | London | 6 |
| IETF 116 | March 2023 | Yokohama | 8 |
| IETF 117 | July 2023 | San Francisco | 6 |
| IETF 118 | November 2023 | Prague | 4 |
| IETF 119 | March 2024 | Brisbane | 1 |
| IETF 120 | July 2024 | Vancouver | 2 |
| IETF 121 | November 2024 | Dublin | 8 |
| IETF 122 | March 2025 | Bangkok | 4 |
| IETF 123 | July 2025 | Madrid | 1 |

The distribution of discussions across working groups reveals the broad applicability of this principle. Transport and security protocols (QUIC, TLS) feature prominently, which makes sense given their fundamental role in Internet communications and their frequent interaction with middleboxes. The Evolution, Deployability, and Maintainability (EDM) working group's high frequency reflects its explicit charter to address these concerns systematically.

Notably, discussion frequency decreased significantly after IETF 118, with particularly low levels at IETF 119, 120, and 123. This pattern suggests that the principle may have become sufficiently well-understood and incorporated into standard practice that it requires less explicit discussion. The spike at IETF 121 might indicate renewed interest in specific applications or emerging challenges.

The geographic distribution of high-activity meetings (Vienna, Yokohama, Dublin) doesn't suggest any particular regional influence, indicating that ossification concerns are truly global. The sustained discussion across 36 different working groups demonstrates that this principle has achieved broad recognition across diverse areas of Internet engineering, from core protocols to specialized applications.

## Resources

**Essential Reading:**
- [RFC 9170: Long-Term Viability of Protocol Extension Mechanisms](https://www.rfc-editor.org/rfc/rfc9170) — Start here for a comprehensive understanding of ossification patterns and mitigation strategies. This document provides both theoretical framework and practical guidance based on real-world experience.
- [RFC 8701: GREASE (Generate Random Extensions And Sustain Extensibility)](https://www.rfc-editor.org/rfc/rfc8701) — Essential for understanding one of the most effective tools for preventing ossification. GREASE has become a standard technique implemented across multiple protocols.

**Case Studies and Applications:**
- [RFC 9000: QUIC Transport Protocol](https://www.rfc-editor.org/rfc/rfc9000) — Examine Section 13 and related sections for a masterclass in applying anti-ossification principles to a major transport protocol. QUIC's design represents the state-of-the-art in ossification-resistant architecture.
- [Draft-ietf-edm-terminology](https://datatracker.ietf.org/doc/draft-ietf-edm-terminology/) — Provides broader context on protocol evolution challenges and terminology. While still in development during this analysis period, it offers valuable perspective on systematic approaches to maintainability.

**Historical Context:**
- [Path MTU Discovery (RFC 1191)](https://www.rfc-editor.org/rfc/rfc1191.html) and [IPv6 transition experiences](https://www.rfc-editor.org/rfc/rfc7872.html) — These documents illustrate classic examples of how well-intentioned network practices can lead to ossification problems, providing important context for why prevention is crucial.

---

*This report was generated from analysis of IETF working group session transcripts (vCon data) covering meetings 110-123 (March 2021 - July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `c93a4657-0f71-49f0-b5f2-870455334d73` |
Sessions analyzed: 71 |
Generated: 2026-03-14*
