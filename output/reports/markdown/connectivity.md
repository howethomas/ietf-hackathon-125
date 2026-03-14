# Connectivity as primary goal

## Introduction

The principle of "connectivity as primary goal" stands as one of the foundational tenets of Internet architecture, establishing universal connectivity as the Internet's paramount objective. This principle, formally articulated in [RFC 1958](https://www.rfc-editor.org/rfc/rfc1958), reflects the Internet's original vision as a global network that enables any device to communicate with any other device, regardless of underlying technologies, geographic location, or administrative boundaries. The principle emerged from the early Internet's design philosophy that prioritized reaching the largest possible number of destinations over optimizing for specific performance metrics or security concerns.

This connectivity-first approach has profound implications for how Internet protocols are designed, implemented, and evolved. It influences decisions ranging from routing protocol behavior to addressing schemes, from transport protocol design to network management practices. The principle continues to guide IETF working groups as they grapple with modern challenges such as network segmentation, security requirements, and the proliferation of Internet of Things devices, all while maintaining the Internet's fundamental promise of universal reachability.

The ongoing relevance of this principle is evident in contemporary IETF discussions, where working groups consistently reference connectivity concerns when evaluating new protocols, architectural changes, and operational practices. As the Internet has evolved from a research network to critical global infrastructure, the tension between universal connectivity and other requirements—such as security, performance, and reliability—has become a central theme in protocol design deliberations.

## Key References

- [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — B. Carpenter's seminal document establishing the core architectural principles that guide Internet design, including the primacy of connectivity.

## This Principle in IETF Discussions

The principle of connectivity as a primary goal manifests consistently across diverse IETF working groups, reflecting its fundamental importance to Internet architecture. Analysis of working group discussions reveals how this principle shapes technical decision-making in both obvious and subtle ways.

In routing-related working groups, connectivity concerns frequently drive protocol design discussions. During IETF 115, the RTGWG working group examined the critical relationship between service availability and connectivity infrastructure:

> "Services depend on resilient connectivity and the control plane connectivity is inherently important. In The Meta case for example..."

This discussion highlighted how major service disruptions at large providers were primarily caused by configuration mistakes that compromised connectivity, emphasizing the practical importance of maintaining robust reachability even in the face of operational errors.

The LSR working group at IETF 113 grappled with fundamental questions about how routing protocols should handle connectivity information:

> "The root problem here is that IGPs are carrying live reachability not liveness and if we want to talk about liveness we really really need another mechanism..."

This technical discussion illustrates the nuanced challenges in implementing the connectivity principle—distinguishing between whether a destination is reachable versus whether it is actually operational and responsive. The working group was addressing how to ensure that connectivity information accurately reflects the true state of network paths.

Service provider networks face particular challenges in maintaining connectivity across diverse deployment scenarios. The BESS working group at IETF 113 discussed complex multi-protocol connectivity scenarios:

> "We have an IPv4 and IPv6 MLRI from a control plane perspective they're being carried over a single v6 only peer and we're forwarding v4 and v6 and we have end-to-end reachability..."

This excerpt demonstrates how the connectivity principle drives the need for sophisticated tunneling and translation mechanisms that ensure reachability between different address families and network technologies.

Emerging applications and network scenarios continue to test the boundaries of the connectivity principle. The IEPG working group at IETF 120 examined how to maintain connectivity during network failures:

> "The objective is to achieve connectivity during internet phase failures for power affluent devices... such as phones and laptops and PCs..."

This discussion reflects ongoing efforts to extend the connectivity principle to challenging operational environments, ensuring that the Internet's fundamental promise of universal reachability can be maintained even under adverse conditions.

## Historical Analysis

Analysis of discussion frequency across IETF meetings 110-123 reveals interesting patterns in how connectivity concerns have evolved:

| Meeting | Date | Location | Discussion Count |
|---------|------|----------|------------------|
| IETF 110 | March 2021 | Online | 9 |
| IETF 111 | July 2021 | Online | 11 |
| IETF 112 | November 2021 | Online | 6 |
| IETF 113 | March 2022 | Vienna | 14 |
| IETF 114 | July 2022 | Philadelphia | 13 |
| IETF 115 | November 2022 | London | 18 |
| IETF 116 | March 2023 | Yokohama | 11 |
| IETF 117 | July 2023 | San Francisco | 12 |
| IETF 118 | November 2023 | Prague | 11 |
| IETF 119 | March 2024 | Brisbane | 12 |
| IETF 120 | July 2024 | Vancouver | 15 |
| IETF 121 | November 2024 | Dublin | 10 |
| IETF 122 | March 2025 | Bangkok | 12 |
| IETF 123 | July 2025 | Madrid | 11 |

The data reveals a notable peak in connectivity-related discussions at IETF 115 (London, November 2022), with 18 sessions addressing this principle. This increase coincided with the return to in-person meetings and growing concerns about network resilience following several high-profile Internet outages. The elevated discussion levels at IETF 113-115 suggest that the transition from pandemic-era online meetings to hybrid and in-person formats prompted renewed examination of connectivity assumptions and requirements.

The working groups most actively discussing connectivity principles—DTN (8 sessions), GAIA (8 sessions), and RTGWG (7 sessions)—reflect the diverse contexts where connectivity concerns remain paramount. The Delay-Tolerant Networking (DTN) working group's focus on connectivity in challenged network environments, the Global Access to the Internet for All (GAIA) research group's work on universal Internet access, and the Routing Area Working Group's attention to fundamental routing connectivity issues demonstrate the principle's continued relevance across different technical domains.

The broad distribution across 68 different working groups indicates that connectivity concerns permeate virtually all aspects of Internet protocol development, from low-level transport mechanisms to high-level application protocols. This widespread discussion pattern reinforces the principle's foundational role in Internet architecture.

## Resources

- [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — The foundational document that establishes connectivity as a primary goal alongside other key Internet design principles; essential reading for understanding the philosophical foundations of Internet architecture.

- [Internet Universality Indicators (UNESCO)](https://en.unesco.org/internet-universality-indicators) — A comprehensive framework for evaluating universal Internet access that provides policy context for technical connectivity decisions and helps bridge the gap between technical capabilities and social outcomes.

- [RFC 3439: Some Internet Architectural Guidelines and Philosophy](https://www.rfc-editor.org/rfc/rfc3439) — Extends and updates the architectural principles from RFC 1958, providing modern context for how connectivity principles should be applied in contemporary protocol design.

---
*This report was generated from analysis of IETF working group session transcripts using vCon (Virtual Conversation) data spanning meetings 110-123 (March 2021 - July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `7caf0ca6-4750-45ff-af2f-2187c30284aa` |
Sessions analyzed: 165 |
Generated: 2026-03-14*
