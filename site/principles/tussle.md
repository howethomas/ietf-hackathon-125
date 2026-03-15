# Tussle in cyberspace

## Introduction

The principle of "tussle in cyberspace" recognizes a fundamental truth about Internet architecture: the network inevitably becomes an arena where different stakeholders with competing interests clash, and the technical design must accommodate rather than ignore these tensions. First articulated by David Clark and colleagues at MIT in their influential 2002 paper "[Tussle in Cyberspace: Defining Tomorrow's Internet](https://groups.csail.mit.edu/ana/Publications/PubPDFs/Tussle2002.pdf)," this principle argues that successful Internet protocols must be designed with the understanding that conflicts between users, service providers, content creators, governments, and other parties are not bugs to be eliminated, but features to be anticipated and managed.

Rather than attempting to resolve these tensions through technical fiat, the principle suggests that Internet architecture should provide mechanisms that allow different stakeholders to pursue their interests while maintaining the network's overall functionality. This approach acknowledges that the Internet is not just a technical system, but a socio-technical infrastructure where economic, political, and social forces play out through protocol choices and implementation decisions.

The significance of this principle in IETF work cannot be overstated. It has influenced everything from security protocol design to routing architectures, helping the Internet engineering community understand why purely technical solutions often fail when they don't account for the human and organizational dynamics that drive technology adoption. As our analysis of IETF meetings from 2021 to 2025 shows, this principle remains actively relevant in contemporary protocol debates, appearing across 50 working group sessions spanning nearly every major IETF meeting in this period.

## Understanding This Principle

**The Core Idea** — Design systems to accommodate inevitable conflicts between stakeholders rather than trying to eliminate them. Think of this like designing a city's transportation system: you don't build roads assuming everyone will cooperate perfectly and drive at optimal speeds in perfect coordination. Instead, you design for the reality that drivers will have different destinations, different levels of patience, different vehicle capabilities, and sometimes conflicting goals (the delivery truck that needs to double-park versus the commuter who wants clear lanes). A good transportation system provides multiple routes, traffic signals that manage conflicts fairly, and enforcement mechanisms that maintain overall flow despite individual tensions.

**Why It Matters** — When system designers ignore stakeholder tensions, they often create brittle architectures that fail catastrophically when real-world conflicts emerge. Consider email security: early email protocols assumed a cooperative environment where all mail servers would behave honestly. When spam and phishing emerged, the system had no built-in mechanisms to handle adversarial behavior. The result was an arms race of patches and bolt-on solutions like spam filters, sender authentication schemes, and reputation systems. In contrast, protocols designed with tussle in mind build flexibility and negotiation mechanisms from the start. TLS, for example, includes cipher suite negotiation that allows clients and servers with different security requirements and capabilities to find common ground, rather than forcing a one-size-fits-all solution.

**The Tension** — The natural engineering instinct is to design for the "optimal" case and eliminate sources of conflict as inefficiencies. Engineers are trained to create clean, deterministic systems where all components work in harmony. Business stakeholders often want solutions that clearly favor their interests. Acknowledging tussle means accepting that systems will be messier, more complex, and sometimes less efficient in the short term. It requires building in negotiation mechanisms, fallback options, and flexibility that may seem like unnecessary overhead when you're focused on a specific use case.

**How to Recognize It** — You're seeing this principle at work when:

* A protocol includes multiple options for the same functionality, allowing different implementations to make different trade-offs based on their stakeholders' priorities
* System designs include explicit negotiation phases where parties can discover each other's capabilities and constraints before proceeding
* Instead of mandating a single "correct" behavior, specifications define how parties should behave when they disagree or have conflicting requirements
* Protocols provide hooks or extension points that allow different stakeholders to add their own functionality without breaking the core system

## Early IETF Work

The roots of the tussle principle can be traced back to fundamental tensions in early Internet architecture, though it wasn't explicitly named until the 2000s. The original Internet design embodied this principle in several key ways. The end-to-end principle, articulated in RFC 1958, reflected an understanding that different applications would have different requirements, and the network should provide basic connectivity while allowing endpoints to implement their own optimizations. This was a conscious decision to avoid building intelligence into the network that might serve some applications well but handicap others.

However, the Internet community also learned hard lessons when they failed to anticipate stakeholder conflicts. The original Domain Name System (DNS) design assumed cooperative behavior among name server operators, leading to vulnerabilities like cache poisoning that weren't addressed until decades later. Similarly, the early routing protocols like RIP assumed that all network operators would faithfully advertise correct routing information, an assumption that proved naive as the Internet commercialized and economic incentives created conflicts between providers.

[RFC 3724: The Rise of the Middle](https://www.rfc-editor.org/rfc/rfc3724) documented how the Internet's architecture was evolving to include more "middleboxes" - devices like firewalls, load balancers, and proxies that reflected the tussle between network operators' operational needs and the end-to-end principle. Rather than condemning these devices as violations of Internet purity, RFC 3724 acknowledged them as inevitable responses to real stakeholder requirements and began developing principles for how they could coexist with traditional Internet architecture.

## Key References

* **[Tussle in Cyberspace: Defining Tomorrow's Internet](https://groups.csail.mit.edu/ana/Publications/PubPDFs/Tussle2002.pdf)** — The seminal paper by Clark, Wroclawski, Sollins, and Braden that first articulated this principle and its implications for Internet architecture.
* **[RFC 3724: The Rise of the Middle](https://www.rfc-editor.org/rfc/rfc3724)** — Documents how middleboxes represent a form of architectural tussle and provides principles for accommodating them.

## This Principle in IETF Discussions

The tussle principle appears consistently across IETF working groups, often emerging when technical decisions must navigate competing stakeholder interests. In the [Human Rights Protocol Considerations (HRPC)](https://datatracker.ietf.org/wg/hrpc/about/) working group, participants have grappled with how to balance different stakeholder perspectives in standards development. As one IETF 110 discussion noted, successful technical committees require "a balance of stakeholders so you wanted some of them to be from the manufacturing firms some of them could be from..." different constituencies, acknowledging that standards must accommodate diverse interests rather than favoring any single group.

> "munity um and again the view seemed impacted by specific personal experiences and how people perceive things you know glasses half full or empty or things like that um engaging with external impacted stakeholders uh in general there does seem to be a belief that the ietf cannot exist in a vacuum and"

*IETF 110 - [IETF Working Group](https://datatracker.ietf.org/wg/ietf/about/) Session (March 2021)* *[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf110/ietf110_ietf_28744.vcon.json)*

This recognition that the IETF "cannot exist in a vacuum" reflects a mature understanding that technical standards must account for real-world stakeholder dynamics. The discussion explicitly acknowledges that different participants bring different perspectives shaped by their experiences and interests.

By IETF 118, the principle was being invoked more explicitly in technical discussions. In an [EDM working group](https://datatracker.ietf.org/wg/edm/about/) session on network measurement, participants identified a fundamental "tussle" between the need for research data and network operators' concerns about greasing mechanisms:

> "do the greasing somehow we somehow have to know whether the tests we're doing actually go through the network so we know what works so that researchers can build big data sets over time and there's a tussle here because greeting kind of opticat that or maybe exercises that so I think it might be wor"

*IETF 118 - [EDM Working Group](https://datatracker.ietf.org/wg/edm/about/) Session (November 2023)* *[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf118/ietf118_edm_31821.vcon.json)*

This example shows how the principle applies to specific technical challenges: researchers need visibility into network behavior to build datasets, while network operators deploying greasing techniques specifically want to obscure certain behaviors to prevent ossification. Rather than viewing this as a problem to solve, the participants recognized it as a legitimate tussle requiring careful design balance.

The principle also appears in operational contexts. During an [IOTOPS working group](https://datatracker.ietf.org/wg/iotops/about/) discussion about certificate management, participants identified a "real tussle" between security requirements and operational realities:

> "ficates or something and they have some magic you know uh thing that's going to solve your problem but the problem case is real and I think that the that I think that um I think we have a real a real tussle here right because you you many cases you just don't ever want those things to ever expire an"

*IETF 118 - [IOTOPS Working Group](https://datatracker.ietf.org/wg/iotops/about/) Session (November 2023)* *[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf118/ietf118_iotops_31575.vcon.json)*

This reflects the tension between security best practices (regular certificate rotation) and operational simplicity (certificates that never expire). Rather than dismissing either concern, the discussion acknowledges both as legitimate stakeholder interests.

By 2024, the principle was being applied to email security discussions in the [EMAILCORE working group](https://datatracker.ietf.org/wg/emailcore/about/), where participants explicitly acknowledged that "there's not going to be perfect here" and that clear specifications must account for ongoing tensions:

> "lly have words to fix it right because uh my I think Daniel sort of captured this well that there's not going to be perfect here and by no means will there be perfect here there's there's a there's a tussle going on in in in all this as we've heard and so there has to be really clear words as to how"

*IETF 120 - [EMAILCORE Working Group](https://datatracker.ietf.org/wg/emailcore/about/) Session (July 2024)* *[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf120/ietf120_emailcore_33114.vcon.json)*

Most recently, IETF 123 discussions showed the principle being applied to the eternal tension between specification-first standardization and implementation-driven approaches in the [EDM working group](https://datatracker.ietf.org/wg/edm/about/):

> "we still at the ITF have to put our specification first. We shouldn't be like I understand there is a value of running code what has actually worked but not give up our stuff in the middle there is a tussle there because people come all the time to the IT say this is already implemented I'm not goin"

*IETF 123 - [EDM Working Group](https://datatracker.ietf.org/wg/edm/about/) Session (July 2025)* *[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf123/ietf123_edm_34524.vcon.json)*

This illustrates the ongoing tension between the IETF's standards-first approach and industry pressure to standardize existing implementations, showing how the tussle principle continues to inform IETF processes themselves.

## Historical Analysis

Analysis of IETF meetings 110-123 reveals consistent engagement with the tussle principle across diverse working groups, with notable concentration in areas dealing with human rights, measurement, and cross-stakeholder coordination:

| Meeting | Sessions | Notable Trend |
|---------|----------|---------------|
| IETF 110-114 | 16 sessions | Early post-pandemic discussions focused on stakeholder inclusion |
| IETF 115-117 | 6 sessions | Lower activity, possibly due to return to in-person meetings |
| IETF 118-123 | 28 sessions | Significant increase, with explicit "tussle" terminology becoming common |

The [Human Rights Protocol Considerations (HRPC)](https://datatracker.ietf.org/wg/hrpc/about/) working group leads in discussions with 7 sessions, reflecting their focus on protocols' societal impacts and multi-stakeholder concerns. The [Global Access to the Internet for All (GAIA)](https://datatracker.ietf.org/wg/gaia/about/) group's 4 sessions similarly reflect concerns about global access and digital divides that inherently involve stakeholder tensions.

Interestingly, the [Network Management Research Group (NMRG)](https://datatracker.ietf.org/wg/nmrg/about/) and [Encrypted DNS Deployment (EDM)](https://datatracker.ietf.org/wg/edm/about/) groups each had 3 sessions, suggesting that measurement and deployment contexts frequently surface stakeholder tensions between operators, researchers, and users.

The significant uptick in discussions during IETF 118-123 corresponds with increased explicit use of "tussle" terminology, suggesting the principle has become more consciously applied rather than just implicitly present in discussions. This may reflect growing maturity in how the IETF community thinks about multi-stakeholder considerations in protocol design.

## Resources

* **[Tussle in Cyberspace (original paper)](https://groups.csail.mit.edu/ana/Publications/PubPDFs/Tussle2002.pdf)** — Essential reading for understanding the theoretical foundation and key examples of how stakeholder conflicts shape Internet architecture.
* **[RFC 3724: The Rise of the Middle](https://www.rfc-editor.org/rfc/rfc3724)** — Provides concrete examples of how tussle manifests in middlebox deployment and offers architectural principles for accommodation.
* **[Internet Architecture and Innovation](https://mitpress.mit.edu/books/internet-architecture-and-innovation)** by Barbara van Schewick — Comprehensive analysis of how architectural choices affect innovation and competition, with extensive discussion of stakeholder tensions.

---

*This report was generated through analysis of video conference recordings (vCons) from IETF working group sessions spanning meetings 110-123 (March 2021 - July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `38a47da1-a32e-4d6d-83a0-8bf23b00bf8b` |
Sessions analyzed: 50 |
Generated: 2026-03-15*
