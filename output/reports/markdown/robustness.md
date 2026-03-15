# Robustness principle / Postel's law

## Introduction

The Robustness principle, commonly known as Postel's law, stands as one of the most influential and controversial design philosophies in Internet architecture. Formulated by Jon Postel in [RFC 761](https://www.rfc-editor.org/rfc/rfc761) in 1980, the principle states simply: "Be conservative in what you send, be liberal in what you accept." This deceptively simple maxim shaped decades of protocol design and implementation across the Internet stack, from TCP to HTTP to modern web APIs.

Named after Jon Postel, one of the Internet's founding architects and longtime editor of the RFC series, this principle emerged during the early days of ARPANET when interoperability between diverse systems was paramount for network growth. The principle was later codified in [RFC 1122](https://www.rfc-editor.org/rfc/rfc1122), the seminal "Requirements for Internet Hosts" document, cementing its role in Internet architecture. However, decades of experience have revealed both the power and the perils of liberal acceptance, leading to a nuanced reassessment captured in [RFC 9413](https://www.rfc-editor.org/rfc/rfc9413), "Maintaining Robust Protocols."

Today, as the Internet faces challenges ranging from security vulnerabilities to protocol ossification, the IETF continues to grapple with when and how to apply Postel's law. This principle remains central to debates about backwards compatibility, security hardening, and the evolution of Internet protocols.

## Understanding This Principle

**The Core Idea**

Be strict about what you send out, but flexible about what you're willing to receive and work with. Think of this principle like running a high-end restaurant that maintains impeccable standards for the food it serves while graciously accommodating diverse guests with varying dietary restrictions, cultural backgrounds, and communication styles.

When your restaurant sends out a dish, every detail must be perfect—the seasoning precise, presentation flawless, temperature optimal. You never compromise on what leaves your kitchen because your reputation depends on consistency and quality. But when guests arrive, you work with what they bring. Maybe they mispronounce menu items, have unclear dietary needs, or make unusual requests. A robust restaurant finds ways to serve them well despite these variations, interpreting their intent charitably and adapting where possible.

This isn't just hospitality—it's a survival strategy. If your restaurant only served customers who spoke perfect culinary French and knew every protocol of fine dining, you'd have very few customers. But if you sent out food of inconsistent quality, you'd lose the trust that makes customers willing to return. The asymmetry is crucial: strict standards for output, generous interpretation of input.

**Why It Matters**

In networked systems, this principle determines whether technologies thrive or die. When protocols are too rigid about what they accept, they create brittle ecosystems where small variations cause catastrophic failures. Imagine if email servers rejected messages with slightly non-standard header formatting, or if web browsers crashed when encountering minor HTML errors. The early Internet succeeded precisely because implementations could work together despite inevitable differences in interpretation and execution.

Before this principle was widely adopted, computer systems often failed when encountering any deviation from expected input format. A missing space or extra character would cause complete system failure. After embracing robustness, systems became resilient: a web browser might display a page with minor HTML errors rather than showing nothing, or an email server might deliver a message despite non-critical formatting issues. This tolerance enabled rapid growth and innovation because implementers didn't need perfect coordination.

However, the principle also enabled the persistence of security vulnerabilities and buggy implementations. When systems accept malformed or suspicious input "liberally," they sometimes open doors to attacks or perpetuate broken behaviors that become impossible to fix as they spread throughout the ecosystem.

**The Tension**

The pressure against this principle comes from security concerns and the desire for clean, well-defined interfaces. Engineers naturally want to reject obviously wrong input—it seems safer and more principled. Why accept garbage input that might indicate an attack or a broken client? Why not force everyone to follow the specification correctly?

This tension intensifies in security-sensitive contexts. Liberal acceptance can mask attacks: malware might hide in malformed but "tolerantly accepted" data, or implementation differences might create exploitable inconsistencies. There's also a fairness concern: why should careful implementers have to accommodate sloppy ones? The engineering instinct is often to fail fast and fail loudly when encountering problems.

**How to Recognize It**

* **Your API accepts multiple date formats** but always returns dates in one standardized format
* **A system logs warnings about deprecated usage patterns** but continues to process the requests while planning eventual removal  
* **Your parser handles common malformed input gracefully** while producing only well-formed output
* **A protocol implementation accepts optional fields in any order** but always sends them in a consistent, standardized sequence

## Early IETF Work

The Robustness principle emerged from practical necessity during the Internet's formative years. Jon Postel first articulated it in the context of the Transmission Control Protocol, where diverse implementations needed to interoperate across different operating systems and hardware platforms. The early Internet community quickly recognized that rigid conformance testing would fragment the network, while overly permissive implementations might compromise reliability.

[RFC 1122](https://www.rfc-editor.org/rfc/rfc1122), published in 1989, elevated the principle from implementation guidance to architectural doctrine. This "Requirements for Internet Hosts" document systematically applied robustness thinking across the TCP/IP stack, specifying where implementations should be strict (in generating packets) and where they should be tolerant (in processing received packets). The RFC's influence extended far beyond TCP/IP, shaping protocol design philosophy across application layers.

The early web's explosive growth demonstrated both the power and the problems of liberal acceptance. HTML browsers that rendered pages despite syntax errors enabled rapid content creation and publishing. However, this tolerance also led to widespread deployment of broken HTML that later hindered the adoption of stricter standards like XHTML. The IETF learned that while robustness enables growth, it can also create technical debt that becomes increasingly difficult to address as the ecosystem matures.

## Key References

* [RFC 761](https://www.rfc-editor.org/rfc/rfc761) - DoD Standard Transmission Control Protocol: Original articulation of the robustness principle by Jon Postel
* [RFC 1122](https://www.rfc-editor.org/rfc/rfc1122) - Requirements for Internet Hosts: Systematic application of robustness principle across TCP/IP stack  
* [RFC 9413](https://www.rfc-editor.org/rfc/rfc9413) - Maintaining Robust Protocols: Modern reassessment of Postel's law in light of security and evolution concerns

## This Principle in IETF Discussions

IETF working groups continue to wrestle with the practical application of Postel's law across diverse protocol contexts. The principle surfaces regularly in discussions about backwards compatibility, error handling, and security trade-offs.

During IETF 110 in March 2021, the [EMU](https://datatracker.ietf.org/wg/emu/about/) working group grappled with session ticket validation, highlighting the ongoing challenge of determining appropriate boundaries for liberal acceptance:

> "sue one session ticket or and and not going with must might make sense i don't know what's your opinion on that um sure i mean you know in the principle of um be conservative in what you send and and liberal in what you expect um it really is a hard question to figure out exactly where that boundary"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf110/ietf110_emu_28716.vcon.json)*

This uncertainty reflects a broader pattern: while the principle provides philosophical guidance, determining the "right" level of tolerance requires careful case-by-case analysis. Security protocols like those developed by [EMU](https://datatracker.ietf.org/wg/emu/about/) face particular challenges, as excessive liberality can create attack vectors.

By July 2022, the [EDM](https://datatracker.ietf.org/wg/edm/about/) working group was addressing how the robustness principle intersects with protocol evolution and maintenance:

> "star of c we could find um a sensible option i i can totally see that there are other interpretations but just to set the stage um when the so the the overall message of the document is um we had the robustness principle which said uh you know follow the spec but you're you're gonna find something a"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf114/ietf114_edm_29781.vcon.json)*

The [EDM](https://datatracker.ietf.org/wg/edm/about/) discussion reflects growing recognition that liberal acceptance, while enabling initial deployment, can complicate long-term protocol maintenance. Implementations that accept "creative interpretations" of specifications may inadvertently legitimize behaviors that later prove problematic.

More recently, during IETF 120 in July 2024, the [ACME](https://datatracker.ietf.org/wg/acme/about/) working group encountered a practical manifestation of the principle in certificate management:

> "o manipulate for a lot of the same reasons people regularly produce csrs that are broken and violate uh the X5 and Ein speec in a large number of ways and anyone who wants to be at least a little bit liberal in what they accept has to deal with that so a new order doesn't work for us right now to tw"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf120/ietf120_acme_33073.vcon.json)*

This [ACME](https://datatracker.ietf.org/wg/acme/about/) discussion illustrates how Postel's law creates ecosystem dependencies: certificate authorities must handle malformed certificate signing requests because such requests are widespread in practice, even though they violate specifications. The principle becomes a practical necessity rather than just a design preference.

The [DTN](https://datatracker.ietf.org/wg/dtn/about/) working group's frequent discussions of robustness (appearing in 12 sessions across the analyzed period) reflect the particular challenges of delay-tolerant networking, where strict error handling might prevent eventual message delivery across intermittent connectivity.

## Historical Analysis

Analysis of IETF meeting transcripts from March 2021 through July 2025 reveals sustained engagement with the Robustness principle across diverse working groups and protocol contexts. The principle was discussed in 80 sessions spanning all 14 meetings in the analyzed period, indicating its continued relevance to contemporary protocol design.

| Meeting | Date | Location | Discussion Sessions |
|---------|------|----------|-------------------|
| IETF 110 | March 2021 | Online | 9 |
| IETF 111 | July 2021 | Online | 4 |
| IETF 112 | November 2021 | Online | 5 |
| IETF 113 | March 2022 | Vienna | 2 |
| IETF 114 | July 2022 | Philadelphia | 6 |
| IETF 115 | November 2022 | London | 3 |
| IETF 116 | March 2023 | Yokohama | 7 |
| IETF 117 | July 2023 | San Francisco | 7 |
| IETF 118 | November 2023 | Prague | 8 |
| IETF 119 | March 2024 | Brisbane | 3 |
| IETF 120 | July 2024 | Vancouver | 7 |
| IETF 121 | November 2024 | Dublin | 7 |
| IETF 122 | March 2025 | Bangkok | 7 |
| IETF 123 | July 2025 | Madrid | 5 |

The [DTN](https://datatracker.ietf.org/wg/dtn/about/) working group's prominence in these discussions (12 sessions) reflects the particular relevance of robustness principles to delay-tolerant networking, where strict error handling might prevent eventual message delivery. The [HRPC](https://datatracker.ietf.org/wg/hrpc/about/) working group's engagement (4 sessions) suggests growing recognition of the human rights implications of protocol robustness decisions.

Discussion frequency peaked during the early online meetings (IETF 110) and later in-person gatherings (IETF 118), possibly reflecting both the challenges of remote protocol development and renewed focus on resilience as the Internet faced increased stress during global disruptions.

The breadth of working groups engaging with this principle (56 unique groups) demonstrates its cross-cutting relevance, from security protocols ([EMU](https://datatracker.ietf.org/wg/emu/about/), [ACME](https://datatracker.ietf.org/wg/acme/about/)) to application protocols ([HTTPAPI](https://datatracker.ietf.org/wg/httpapi/about/), [CORE](https://datatracker.ietf.org/wg/core/about/)) to network layer innovations ([6MAN](https://datatracker.ietf.org/wg/6man/about/), [INTAREA](https://datatracker.ietf.org/wg/intarea/about/)).

## Resources

* [RFC 9413: Maintaining Robust Protocols](https://www.rfc-editor.org/rfc/rfc9413) - Essential modern analysis of when and how to apply Postel's law, incorporating lessons learned from decades of Internet evolution
* [Robustness Principle (Wikipedia)](https://en.wikipedia.org/wiki/Robustness_principle) - Comprehensive overview with examples across multiple domains and thoughtful discussion of criticisms  
* [RFC 1122: Requirements for Internet Hosts](https://www.rfc-editor.org/rfc/rfc1122) - Historical foundation showing systematic application of robustness principle across TCP/IP stack
* [The Harmful Consequences of Postel's Maxim (draft-iab-protocol-maintenance)](https://datatracker.ietf.org/doc/html/draft-iab-protocol-maintenance) - Critical examination of how liberal acceptance can impede protocol evolution and security

---

*This report was generated from analysis of IETF meeting vCon (virtual conversation) records spanning March 2021 through July 2025, representing 14 IETF meetings and 80 working group sessions where the Robustness principle was discussed.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `439ba615-90d3-4236-b5bb-adc5180162a6` |
Sessions analyzed: 80 |
Generated: 2026-03-15*
