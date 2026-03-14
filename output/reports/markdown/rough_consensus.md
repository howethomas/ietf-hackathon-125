# Rough consensus and running code

## Introduction

"Rough consensus and running code" stands as one of the most fundamental and enduring principles guiding Internet protocol development within the Internet Engineering Task Force (IETF). This principle, first articulated by IETF co-founder Dave Clark in 1992, encapsulates a pragmatic approach to standards development that prioritizes practical implementation and inclusive decision-making over theoretical perfection or unanimous agreement. The principle embodies two interconnected concepts: that the IETF should strive for rough consensus—addressing all reasonable concerns without necessarily accommodating every possible objection—and that working implementations should inform and validate protocol specifications.

The significance of this principle extends far beyond mere process guidance; it has fundamentally shaped how the Internet's core protocols have evolved. By emphasizing running code, the IETF ensures that standards are grounded in practical experience and real-world deployment challenges. The rough consensus component prevents the standards process from being paralyzed by endless debate or held hostage by a small number of dissenting voices, while still requiring that legitimate concerns be addressed. This balance has enabled the IETF to maintain both technical rigor and operational effectiveness throughout the Internet's explosive growth.

Formally documented in [RFC 7282](https://www.rfc-editor.org/rfc/rfc7282), this principle continues to guide IETF working groups as they navigate complex technical decisions and balance competing interests. The principle's enduring relevance is evident in its frequent invocation across diverse working groups, from cryptography to network operations, as engineers grapple with evolving Internet challenges while maintaining the collaborative, implementation-focused culture that has made the Internet's technical foundations so robust.

## Key References

- [RFC 7282: On Consensus and Humming in the IETF](https://www.rfc-editor.org/rfc/rfc7282) — Pete Resnick's comprehensive guide to how the IETF achieves consensus, formally documenting the principle and its application in standards development.
- [RFC 2026: The Internet Standards Process](https://www.rfc-editor.org/rfc/rfc2026) — The foundational document describing the IETF's standards track process, emphasizing the role of implementation experience in standards advancement.

## This Principle in IETF Discussions

The principle of "rough consensus and running code" manifests regularly across IETF working groups, often emerging when participants need to balance theoretical concerns with practical implementation realities. The transcript analysis reveals how working groups invoke this principle to drive decision-making and validate their technical approaches.

In cryptographic research, the principle appears when researchers present new protocols. During IETF 111's CFRG session, a presenter emphasized their commitment to the principle while introducing a deterministic encryption mode:

> "I did write it up as a draft and this is the draft here please take a look. In the interest of running code I did implement it. I added it to my implementation of hpke which is compliant with the current version."

This illustrates how protocol designers proactively demonstrate their commitment to the principle by providing working implementations alongside their specifications, giving the community tangible code to evaluate rather than purely theoretical proposals.

The principle also guides working groups through contentious technical decisions. During IETF 112's DMARC working group session, participants wrestled with scalability concerns about the Public Suffix List, ultimately invoking rough consensus to move forward despite some reservations:

> "I have a strong aversion to anything that's based off of the public suffix list it's just proved unmanageable at scale yes and i do think that's also rough consensus of the group."

Here, the working group used the rough consensus aspect to acknowledge legitimate scalability concerns while still advancing their work, demonstrating how the principle enables progress when perfect solutions aren't immediately available.

The running code aspect frequently appears in measurement and testing contexts. During IETF 110's IPPM working group session, participants discussed converting optional implementation details to mandatory requirements based on their implementation experience:

> "We converted those shoulds to a must and we've had a running code section in the draft since about last september when the running code was released."

This example shows how actual implementation experience drives specification refinement, with running code serving as evidence for tightening protocol requirements.

The principle also shapes the broader IETF culture around hackathons and collaborative development. During IETF 110's SHMOO working group session, organizers explicitly connected hackathon activities to the running code principle:

> "It really has to do with running code related to any existing or evolving or proposed IETF standards."

This demonstrates how the IETF has institutionalized the principle through events specifically designed to foster implementation alongside standards development.

## Historical Analysis

Analysis of IETF meetings 110–123 reveals consistent engagement with the rough consensus and running code principle across the surveyed period, with some notable patterns in frequency and application.

| Meeting | Date | Discussions |
|---------|------|-------------|
| IETF 110 | March 2021 (Online) | 23 |
| IETF 111 | July 2021 (Online) | 20 |
| IETF 112 | November 2021 (Online) | 15 |
| IETF 113 | March 2022 (Vienna) | 20 |
| IETF 114 | July 2022 (Philadelphia) | 27 |
| IETF 115 | November 2022 (London) | 22 |
| IETF 116 | March 2023 (Yokohama) | 27 |
| IETF 117 | July 2023 (San Francisco) | 30 |
| IETF 118 | November 2023 (Prague) | 26 |
| IETF 119 | March 2024 (Brisbane) | 20 |
| IETF 120 | July 2024 (Vancouver) | 21 |
| IETF 121 | November 2024 (Dublin) | 25 |
| IETF 122 | March 2025 (Bangkok) | 23 |
| IETF 123 | July 2025 (Madrid) | 32 |

The data shows a notable trough during the fully online period (IETF 112 in November 2021), possibly reflecting the challenges of applying consensus-building principles in virtual settings. Discussion frequency increases significantly as hybrid and in-person meetings resume, peaking at IETF 117 (30 discussions) and again at IETF 123 (32 discussions). This pattern suggests that the principle's application benefits from the richer interaction dynamics of face-to-face meetings.

The working groups most frequently invoking this principle—IETF plenary sessions (11), EMU (9), NETMOD (8), hackathon sessions (7), and measurement/operations groups like IPPM (6)—reflect diverse application domains. The high frequency in IETF plenary sessions indicates leadership's continued emphasis on the principle as foundational to IETF culture. EMU and NETMOD's frequent discussions likely reflect these groups' focus on authentication and network management protocols, where implementation interoperability is critical. The prominence of hackathon discussions demonstrates the IETF's institutional commitment to fostering running code through collaborative development events.

The broad distribution across 135 working groups indicates that rough consensus and running code remains relevant across the full spectrum of IETF technical work, from fundamental protocols to specialized applications. This universality suggests the principle's continued vitality as Internet protocols evolve to address new challenges in security, scalability, and deployment complexity.

## Resources

- [RFC 7282: On Consensus and Humming in the IETF](https://www.rfc-editor.org/rfc/rfc7282) — The definitive guide to how the IETF achieves consensus, essential reading for anyone participating in IETF working groups or seeking to understand the technical culture behind Internet standards development.

- [The Tao of IETF](https://www.ietf.org/about/participate/tao/) — A practical newcomer's guide to IETF participation that explains how rough consensus and running code principles are applied in practice during working group meetings and standards development.

- [RFC 2026: The Internet Standards Process](https://www.rfc-editor.org/rfc/rfc2026) — Documents the formal standards track process, explaining how implementation experience and consensus-building interact to advance protocols from draft to standard, providing crucial context for understanding why both consensus and running code are necessary.

- [IETF Hackathon](https://www.ietf.org/how/hackathons/) — The IETF's institutional mechanism for fostering running code alongside standards development, demonstrating the principle's practical application in collaborative implementation efforts.

- ["The Design Philosophy of the DARPA Internet Protocols"](https://dl.acm.org/doi/10.1145/52324.52336) by David D. Clark (1988) — The foundational paper that established many of the architectural principles underlying Internet protocols, providing historical context for the emphasis on practical implementation over theoretical perfection.

---
*This report was generated from analysis of IETF working group session transcripts using vCon conversation analytics.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `0fbed9be-ab53-430f-8a04-e5f386a4934d` |
Sessions analyzed: 331 |
Generated: 2026-03-14*
