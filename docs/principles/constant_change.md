# Principle of constant change

## Introduction

The "Principle of constant change" stands as one of the foundational architectural principles of the Internet, formally articulated in [RFC 1958](https://www.rfc-editor.org/rfc/rfc1958) by Brian Carpenter in 1996. The principle states simply: "The Internet must continue to evolve. Design for extensibility." This deceptively straightforward directive has shaped decades of Internet protocol development, emphasizing that successful network protocols must be designed not just for today's requirements, but for the unknown needs of tomorrow.

This principle emerged from hard-learned lessons in the Internet's early development, where rigid protocol designs often became barriers to innovation and adaptation. The Internet's remarkable longevity and continuous growth can be attributed in large part to the IETF community's commitment to this principle, ensuring that protocols can accommodate new technologies, changing requirements, and unforeseen use cases without requiring complete architectural overhauls.

In the IETF's ongoing work from 2021 to 2025, this principle has been discussed in 565 working group sessions across all 14 meetings analyzed, making it one of the most consistently relevant architectural considerations in modern Internet protocol development. Its application spans everything from data modeling standards to security protocols to routing mechanisms, demonstrating its universal importance in network design.

## Understanding This Principle

**The Core Idea** — Design systems to gracefully accommodate future changes you cannot predict today. Think of this principle like designing a city's infrastructure: the best urban planners don't just build roads for current traffic patterns, but design street grids, utility conduits, and zoning frameworks that can adapt as neighborhoods grow, technologies evolve, and citizens' needs change in ways no one can foresee today.

When a city planner designs a new district, they might not know whether residents will primarily use cars, bicycles, or some future transportation technology twenty years from now. But they can design street widths that accommodate different vehicle types, lay utility conduits with extra capacity and access points, and create zoning frameworks with clear extension mechanisms. The infrastructure becomes a platform that enables future innovation rather than constraining it.

This same thinking applies to Internet protocols. When engineers design a protocol today, they cannot predict every future requirement—new security threats, emerging applications, changing network topologies, or novel hardware capabilities. But they can design extension points, reserve space for future options, create flexible data structures, and establish clear mechanisms for adding new features without breaking existing implementations.

**Why It Matters** — When protocols violate this principle, they become evolutionary dead ends that either fragment into incompatible variants or require painful complete rewrites. Consider the contrast between IPv4 and SMTP. IPv4 was designed with a fixed 32-bit address space that seemed enormous in the 1980s, but its lack of extensibility led to the decades-long struggle with address exhaustion and the complex transition to IPv6. Meanwhile, SMTP was designed with extensible command structures and clear mechanisms for adding new capabilities—which is why email protocols have continuously evolved for over forty years without requiring a wholesale replacement.

Without extensibility, protocols face a tragic choice: either stagnate and become irrelevant as technology advances, or undergo disruptive migrations that fragment the Internet. The principle of constant change prevents this by ensuring protocols can grow organically with their ecosystems, maintaining backward compatibility while enabling innovation.

**The Tension** — The counterforce is implementation complexity and the pressure to ship quickly. Designing for extensibility requires additional work upfront—more complex data structures, additional testing scenarios, careful specification of extension mechanisms, and ongoing maintenance of compatibility. When faced with immediate deadlines and concrete requirements, it's tempting to build exactly what's needed today and defer extensibility concerns to "version 2.0." 

Organizations often resist extensibility because it makes initial implementations harder to understand, potentially slower, and definitely more complex to test. There's also the "YAGNI" (You Aren't Gonna Need It) philosophy that argues against building features before they're required. This creates constant pressure to oversimplify protocols and remove extension points to meet delivery schedules.

**How to Recognize It** — You're seeing this principle at work when:

* A protocol reserves unused bits or fields in its message formats, even when there's no immediate use for them
* APIs include version negotiation mechanisms that allow clients and servers to discover each other's capabilities before communicating
* Data schemas define clear rules for adding optional fields without breaking older parsers
* Configuration formats use extensible key-value structures instead of fixed positional parameters
* System designs include plugin architectures or standardized extension points, even when no extensions are planned yet

## Early IETF Work

The principle of constant change was crystallized through painful early experiences with rigid protocol designs that couldn't adapt to the Internet's explosive growth. The original ARPANET protocols of the 1970s were often designed for specific, well-understood environments, but the Internet's rapid expansion in the 1980s and 1990s exposed the limitations of non-extensible designs. Early protocols like Telnet and FTP, while functional, required numerous extensions and modifications as new security requirements, internationalization needs, and performance demands emerged.

One of the most influential examples was the development of SMTP in [RFC 821](https://www.rfc-editor.org/rfc/rfc821), which included explicit extensibility mechanisms through its command-response structure and the later ESMTP extensions framework. This foresight allowed email to evolve continuously—adding authentication, encryption, multimedia support, and internationalization—without requiring a complete protocol replacement. Conversely, protocols that lacked such mechanisms often became evolutionary dead ends or required disruptive migrations that took decades to complete.

The IPv4 address space exhaustion crisis became a canonical example of what happens when fundamental protocol limitations cannot be extended around. Despite various clever workarounds like NAT and CIDR, the fixed 32-bit address structure ultimately required the development of an entirely new protocol (IPv6), leading to one of the longest and most complex transition periods in Internet history. These experiences taught the IETF community that building extensibility into protocols from the beginning was not optional but essential for the Internet's long-term health.

## Key References

* [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — Brian Carpenter's foundational document establishing core Internet architectural principles including constant change
* [RFC 6709: Design Considerations for Protocol Extensions](https://www.rfc-editor.org/rfc/rfc6709) — Comprehensive guidelines for designing extensible protocols and avoiding common pitfalls
* [RFC 5218: What Makes for a Successful Protocol?](https://www.rfc-editor.org/rfc/rfc5218) — Analysis of protocol success factors with extensive discussion of extensibility requirements

## This Principle in IETF Discussions

The principle of constant change manifests consistently across IETF working groups, often emerging in discussions about data formats, protocol extensions, and backward compatibility. In the early period of our analysis, [bess](https://datatracker.ietf.org/wg/bess/about/) participants at IETF 110 emphasized how new protocol designs focused on "defining extensions that provide efficiency and extensibility and improve upon some of the legacy constraints we have seen in the past." This reflects the ongoing effort to learn from previous limitations and build more adaptable protocols.

> focusing on the aspects listed below uh i think to highlight here is we have focused on because it is a new safety we have focused on defining extensions that provide efficiency and extensibility and improve upon some of the legacy uh constraints we have you know seen in the past

The [calext](https://datatracker.ietf.org/wg/calext/about/) working group discovered the practical challenges of extensibility during IETF 110, when they found that "the alternate extensible quote extensible syntax for defining the alarms wasn't quite as extensible as we thought." This highlights how achieving true extensibility requires careful design and testing—it's not sufficient to simply claim a protocol is extensible without validating the extension mechanisms.

> we found out that the uh alternate extensible quote extensible syntax for defining the alarms wasn't quite as extensible as we thought

By the middle period, [core](https://datatracker.ietf.org/wg/core/about/) participants at IETF 115 were grappling with more sophisticated extensibility challenges, noting that "adding something to a registry after the fact will have no effect in many environments." This reflects the evolution of understanding about extensibility—it's not enough to provide extension points if deployed implementations cannot actually use them.

> so that that's a problem with just saying oh we drop in a registry here and and that provides the extensibility we need

The [icnrg](https://datatracker.ietf.org/wg/icnrg/about/) research group at IETF 115 demonstrated practical application of the principle, describing how they "Define two keying mechanism one is a pre-shared key... and it is you know extensible you can Define more and hopefully we will get more than those two." This shows extensibility being built into security mechanisms from the beginning, rather than retrofitted later.

> Define we Define two keying mechanism one is a pre-shared key... and it is you know extensible you can Define more and hopefully we will get more than those two

In recent discussions, [6man](https://datatracker.ietf.org/wg/6man/about/) participants at IETF 120 showed concern about potential extensibility impacts, asking whether protocol changes might "close off some extensibility path" for implementers. This demonstrates how the principle now influences even detailed technical decisions, with participants actively considering future flexibility implications.

> does it close off some extensibility path for them that's fair enough

The [anrw](https://datatracker.ietf.org/wg/anrw/about/) research workshop at IETF 120 presented research on "HTP 3 extensible prioritization scheme in the wild," showing how extensibility mechanisms are being studied and validated in real-world deployments, not just designed in theory.

> and this is the results on HTP 3 extensible prioritization scheme in the wild

## Historical Analysis

Discussion of the principle of constant change has remained consistently high throughout the analyzed period, with notable peaks during IETF 110 (48 sessions) and IETF 116 (48 sessions). The principle's relevance has proven remarkably stable, never dropping below 31 sessions in any meeting, indicating its fundamental importance across diverse working groups.

| Meeting | Sessions | Period |
|---------|----------|--------|
| IETF 110 | 48 | March 2021 (Online) |
| IETF 111 | 31 | July 2021 (Online) |
| IETF 112 | 42 | November 2021 (Online) |
| IETF 113 | 40 | March 2022 (Vienna) |
| IETF 114 | 35 | July 2022 (Philadelphia) |
| IETF 115 | 39 | November 2022 (London) |
| IETF 116 | 48 | March 2023 (Yokohama) |
| IETF 117 | 44 | July 2023 (San Francisco) |
| IETF 118 | 36 | November 2023 (Prague) |
| IETF 119 | 32 | March 2024 (Brisbane) |
| IETF 120 | 43 | July 2024 (Vancouver) |
| IETF 121 | 45 | November 2024 (Dublin) |
| IETF 122 | 39 | March 2025 (Bangkok) |
| IETF 123 | 43 | July 2025 (Madrid) |

The working groups with highest discussion frequency reveal interesting patterns. [netmod](https://datatracker.ietf.org/wg/netmod/about/) leads with 12 sessions, reflecting the critical importance of extensibility in network management data models. [iabopen](https://datatracker.ietf.org/wg/iabopen/about/) sessions (11 discussions) indicate ongoing architectural attention to this principle at the highest levels. Protocol-focused groups like [quic](https://datatracker.ietf.org/wg/quic/about/), [masque](https://datatracker.ietf.org/wg/masque/about/), and [lsr](https://datatracker.ietf.org/wg/lsr/about/) (each with 11 sessions) demonstrate how extensibility concerns permeate modern protocol development.

The broad distribution across 149 working groups—nearly every active IETF working group—shows that extensibility is not confined to specific technical domains but represents a universal design concern. From data formats ([cbor](https://datatracker.ietf.org/wg/cbor/about/)) to network configuration ([netconf](https://datatracker.ietf.org/wg/netconf/about/)) to IPv6 evolution ([6man](https://datatracker.ietf.org/wg/6man/about/)), the principle influences decisions across the entire Internet protocol stack.

## Resources

* [RFC 1958: Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958) — The foundational document that established this principle, essential reading for understanding Internet architectural philosophy
* [RFC 6709: Design Considerations for Protocol Extensions](https://www.rfc-editor.org/rfc/rfc6709) — Practical engineering guidance for building extensible protocols, with detailed examples and common pitfalls
* [RFC 5218: What Makes for a Successful Protocol?](https://www.rfc-editor.org/rfc/rfc5218) — Comprehensive analysis of protocol success factors, with extensive discussion of extensibility's role in long-term protocol viability
* [Protocol Extensibility (Wikipedia)](https://en.wikipedia.org/wiki/Extensibility) — Accessible overview of extensibility concepts across different domains, helpful for understanding the broader software engineering context

---
*This report was generated from analysis of IETF working group session transcripts using vCon conversation analysis.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `ca07c18a-c675-46f1-afce-251143c309e8` |
Sessions analyzed: 565 |
Generated: 2026-03-14*
