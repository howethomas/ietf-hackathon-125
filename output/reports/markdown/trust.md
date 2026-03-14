# Trust as architectural principle

## Introduction

Trust as an architectural principle represents one of the foundational concepts in Internet protocol design, emphasizing that trust relationships must be explicitly defined and understood before any protocol architecture is developed. This principle, formally articulated in [RFC 3724](https://www.rfc-editor.org/rfc/rfc3724) "The Rise of the Middle and Future of End-to-End: Reflections on the Evolution of the Internet Architecture," emerged from the Internet Architecture Board's (IAB) recognition that many protocol failures and security vulnerabilities stem from poorly defined or assumed trust relationships between network entities.

The principle fundamentally challenges protocol designers to explicitly identify who trusts whom, for what purpose, and under what conditions, rather than making implicit assumptions about trust. This approach has become increasingly critical as the Internet has evolved from a relatively closed academic network to a global, heterogeneous infrastructure where adversarial behavior is commonplace. The principle directly influences decisions about cryptographic mechanisms, authentication protocols, authorization frameworks, and the placement of trust anchors within distributed systems.

In the context of modern IETF work, this principle has gained renewed importance with the emergence of zero-trust architectures, IoT security challenges, and the need for interoperable trust frameworks across diverse network environments. From DNS security extensions to automated certificate management, from IoT device onboarding to real-time communications, virtually every protocol development effort must grapple with fundamental questions about trust relationships and their architectural implications.

## Key References

- [RFC 3724: The Rise of the Middle and Future of End-to-End](https://www.rfc-editor.org/rfc/rfc3724) - The seminal IAB document establishing trust as an explicit architectural principle for Internet protocol design.
- [NIST SP 800-207: Zero Trust Architecture](https://csrc.nist.gov/publications/detail/sp/800-207/final) - Comprehensive framework for understanding trust boundaries in modern network architectures.
- [RFC 8555: Automatic Certificate Management Environment (ACME)](https://www.rfc-editor.org/rfc/rfc8555) - Practical example of trust anchor establishment in Web PKI systems.

## This Principle in IETF Discussions

The principle of trust as an architectural foundation appears consistently across diverse IETF working groups, often emerging at critical decision points in protocol design. The conversation excerpts from recent meetings illustrate how this principle shapes real-world protocol development discussions.

During the IETF 110 ANIMA Working Group session in March 2021, participants grappled with fundamental trust relationship questions in device onboarding scenarios:

> "we discussed about the trust relationship between the device of the agent that is basically onboarding the pledge"

This discussion in the autonomic networking context highlights how trust relationships must be clearly defined before automated systems can securely provision new devices. The ANIMA working group's focus on "pledge" devices joining autonomic networks requires explicit modeling of which entities can trust which others during the bootstrapping process.

The GNAP Working Group's session at the same meeting revealed how trust relationships are prerequisite to privacy-preserving design:

> "you identify the primary appointment first once you have the model component and once you have the trust relationship since we have no trust relationship it's impossible to do a privacy by design"

This quote demonstrates a crucial insight: without clearly defined trust boundaries, it becomes impossible to implement meaningful privacy protections. The speaker's concern reflects the principle's requirement that trust relationships be established before other protocol features can be properly designed.

In the SIDROPS Working Group discussion, also from IETF 110, the complexity of multi-party trust relationships in routing security emerged as a central challenge:

> "rta suggests that multiple signers subordinate to multiple different trust anchors could together composite a cms-signed object a issue i perceive there is that there co[uld be conflicts]"

This excerpt illustrates how the principle applies to complex scenarios where multiple trust anchors must cooperate. The Resource Trust Anchors (RTA) discussion shows how careful architectural analysis is required when trust relationships become hierarchical and distributed across multiple authorities.

The T2TRG Working Group session highlighted a common challenge in applying this principle - the conceptual confusion that arises when trust relationships aren't clearly defined:

> "this is about roots of trust and trust anchors and these terms are sounds really confusing to some people even in the security space"

This observation underscores why the principle is so important: even security experts can become confused when trust relationships and trust anchor concepts aren't clearly articulated from the beginning of the design process.

## Historical Analysis

Analysis of discussions from IETF 110 through 123 (March 2021 to July 2025) reveals consistent attention to trust as an architectural principle, with notable patterns in both frequency and focus areas.

| Meeting | Date | Location | Discussions |
|---------|------|----------|-------------|
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

The data shows elevated discussion levels during key transition periods, particularly IETF 113, 114, 116, and 118, which corresponded to the return to in-person meetings and increased focus on IoT security and zero-trust architectures. The consistently high numbers (typically 16-22 discussions per meeting) indicate that trust architectural considerations remain central to ongoing protocol development work.

The working groups with highest discussion frequency reflect areas where trust relationships are most complex and critical. **SIDROPS** (11 discussions) leads the list, which is unsurprising given that routing security fundamentally depends on carefully constructed trust relationships between network operators. **DNSOP** (9 discussions) follows closely, reflecting ongoing work on DNS security extensions and trust anchor management. The **STIR** working group (8 discussions) addresses caller authentication, where trust relationships between telecommunications providers are central to the protocol's effectiveness.

Emerging areas show significant attention as well, with **ACE** (Authorization and Authentication for Constrained Environments), **IOTOPS** (IoT Operations), and **RATS** (Remote Attestation Procedures) each showing 7 discussions. This pattern reflects the growing importance of trust architectural considerations in resource-constrained and IoT environments, where traditional trust assumptions often don't apply.

The research-oriented groups **PANRG** and **DINRG** (6 discussions each) indicate that trust architecture remains an active area of fundamental research, while **SCITT** (6 discussions) reflects emerging work on supply chain integrity, where trust relationships span multiple organizational boundaries.

## Resources

- [RFC 3724: The Rise of the Middle and Future of End-to-End](https://www.rfc-editor.org/rfc/rfc3724) - Essential reading for understanding the IAB's foundational thinking on trust as an architectural principle, including historical context about how implicit trust assumptions have caused protocol failures.

- [NIST Special Publication 800-207: Zero Trust Architecture](https://csrc.nist.gov/publications/detail/sp/800-207/final) - Comprehensive framework that operationalizes trust architectural principles in modern network environments, particularly valuable for understanding how to implement "never trust, always verify" approaches.

- [RFC 8555: Automatic Certificate Management Environment (ACME)](https://www.rfc-editor.org/rfc/rfc8555) - Concrete example of how trust architectural principles translate into practical protocol design, showing how trust anchors and validation relationships are established in automated certificate management.

- [RFC 6962: Certificate Transparency](https://www.rfc-editor.org/rfc/rfc6962) - Demonstrates how trust architectural principles can be enhanced through transparency mechanisms that allow verification of trust anchor behavior.

- [IETF Security Considerations Guidelines](https://www.rfc-editor.org/rfc/rfc3552) - Practical guidance for protocol designers on how to identify and document trust assumptions in Internet protocol specifications.

---
*This report was generated through analysis of IETF working group session transcripts using vCon (Virtual Conversation) data from meetings 110-123 (March 2021 - July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `58c23ba4-cfc6-4837-a087-7163b5544553` |
Sessions analyzed: 252 |
Generated: 2026-03-14*
