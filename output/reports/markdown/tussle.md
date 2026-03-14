# Tussle in cyberspace

## Introduction

The "tussle in cyberspace" principle recognizes that Internet protocols and systems must be designed to accommodate the inevitable tensions and competing interests between different stakeholders in the digital ecosystem. This fundamental design principle emerged from the seminal 2002 paper ["Tussle in Cyberspace: Defining Tomorrow's Internet"](https://groups.csail.mit.edu/ana/Publications/PubPDFs/Tussle2002.pdf) by David Clark, John Wroclawski, Karen Sollins, and Robert Braden, which argued that rather than trying to eliminate conflicts between users, service providers, governments, and other parties, Internet architecture should embrace these tensions as a natural and necessary part of the system.

The principle asserts that attempts to design protocols that favor one stakeholder group over others are likely to fail in the long term, as disadvantaged parties will find ways to work around or subvert such systems. Instead, successful Internet protocols should provide mechanisms that allow different stakeholders to pursue their legitimate interests while maintaining the overall stability and functionality of the network. This approach acknowledges that the Internet is not just a technical system, but a socio-technical infrastructure where economic, political, and social forces constantly interact and compete.

For the IETF, this principle has become increasingly relevant as the Internet has evolved from an academic research network to critical global infrastructure. Protocol designers must now consider how their technical decisions will affect diverse stakeholders including end users, network operators, content providers, governments, and security organizations, each with their own priorities and constraints.

## Key References

- [Tussle in Cyberspace: Defining Tomorrow's Internet](https://groups.csail.mit.edu/ana/Publications/PubPDFs/Tussle2002.pdf) — The foundational paper that introduced the concept and argued for designing Internet architecture to accommodate competing stakeholder interests.
- [RFC 3724: The Rise of the Middle](https://www.rfc-editor.org/rfc/rfc3724) — Explores how Internet architecture has evolved to support intermediaries and the tensions this creates between end-to-end principles and practical deployment needs.

## This Principle in IETF Discussions

The concept of tussle manifests regularly in IETF working group discussions, particularly when protocol designers grapple with conflicting requirements from different stakeholder communities. These tensions are most visible in areas where technical decisions have significant economic or policy implications.

In the Human Rights Protocol Considerations (HRPC) working group, tussle is recognized as a fundamental aspect of Internet governance. During IETF 118, a participant noted:

> "I just wanted to say thank you thank you for presenting I think are you familiar with the idea we talk about here often of a tussle the kind of disagreement tension between two parties in a conversation it happens a lot here"

This acknowledgment reflects how the HRPC community has embraced tussle as a normal part of their work, recognizing that disagreements between parties with different perspectives on human rights and technical implementation are not problems to be solved but dynamics to be managed.

The encrypted DNS measurements (EDM) working group has encountered tussle when balancing research needs against operational concerns. During IETF 118, participants discussed the challenge of conducting network measurements while using connection-greasing techniques:

> "there's a tussle here because greeting kind of opticat that or maybe exercises that so I think it might be wor[th considering]"

This example illustrates how seemingly technical decisions about measurement methodologies can create tensions between researchers who need reliable data and network operators who want to prevent ossification through protocol greasing.

Certificate management has proven to be another area where tussle emerges prominently. At IETF 118, the IOTOPS working group wrestled with the fundamental tension between security best practices and operational realities:

> "I think we have a real a real tussle here right because you you many cases you just don't ever want those things to ever expire"

This captures the classic conflict between security professionals who advocate for regular certificate rotation and operators who prefer systems that "just work" without frequent manual intervention.

The EMAILCORE working group has faced similar challenges in email security, where perfect technical solutions conflict with practical deployment constraints. During IETF 120, a participant observed:

> "there's not going to be perfect here and by no means will there be perfect here there's there's a there's a tussle going on in in in all this as we've heard and so there has to be really clear words as to how"

This recognition that perfection is unattainable reflects the mature understanding that email protocols must accommodate competing demands from different stakeholders, even when this results in technical compromises.

## Historical Analysis

Analysis of IETF discussions from March 2021 through July 2025 reveals interesting patterns in how the tussle principle is discussed across different working groups and time periods.

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

The data shows a notable increase in tussle-related discussions from IETF 118 onwards, with a peak period during IETF 118, 120, and 121. This surge coincides with increased focus on privacy-preserving technologies, encrypted DNS deployment, and post-quantum cryptography transitions—all areas where competing stakeholder interests are particularly pronounced.

The Human Rights Protocol Considerations (HRPC) working group leads discussions with 7 sessions, which is unsurprising given their explicit focus on how technical decisions affect different communities. The Global Access to the Internet for All (GAIA) research group follows with 4 discussions, reflecting their work on Internet accessibility and digital divide issues where stakeholder tensions are inherent.

Interestingly, the EDM working group appears three times in the dataset, suggesting that even seemingly objective measurement activities generate stakeholder tensions. This reflects the growing recognition that network measurement is not a neutral technical activity but one that affects privacy, competition, and operational practices.

The distribution across 29 different working groups indicates that tussle is not confined to specific technical areas but emerges wherever protocol decisions have broader implications for Internet stakeholders. This broad distribution supports the principle's foundational role in Internet architecture thinking.

## Resources

- [Tussle in Cyberspace (original paper)](https://groups.csail.mit.edu/ana/Publications/PubPDFs/Tussle2002.pdf) — Essential reading that introduces the concept and provides the theoretical foundation for understanding stakeholder conflicts in Internet architecture.

- [RFC 3724: The Rise of the Middle](https://www.rfc-editor.org/rfc/rfc3724) — Explores how Internet architecture has accommodated intermediaries and the resulting tensions with end-to-end principles, providing concrete examples of tussle in practice.

- [HRPC Working Group Charter and Documents](https://datatracker.ietf.org/wg/hrpc/about/) — The HRPC working group has developed extensive resources on how protocol decisions affect human rights, with many documents exploring stakeholder tensions in detail.

---
*This report was generated from analysis of IETF working group session transcripts (vCon format) covering meetings 110-123.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `38a47da1-a32e-4d6d-83a0-8bf23b00bf8b` |
Sessions analyzed: 50 |
Generated: 2026-03-14*
