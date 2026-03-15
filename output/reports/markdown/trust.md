# Trust as architectural principle

## Introduction

Trust as an architectural principle represents one of the most fundamental yet challenging aspects of Internet protocol design. Codified in [RFC 3724: The Rise of the Middle and the Future of End-to-End](https://www.rfc-editor.org/rfc/rfc3724), this principle establishes that trust relationships must be explicitly defined before protocol design begins. Rather than assuming trust exists or leaving it to be figured out later, architects must first map out who trusts whom, for what purposes, and under what conditions.

This principle emerged from decades of hard-won experience in the Internet architecture community. Early Internet protocols often assumed a relatively benign environment with implicit trust relationships. As the network evolved from a research environment to a global communications infrastructure, the consequences of undefined trust became increasingly severe. Security vulnerabilities, privacy breaches, and operational failures repeatedly traced back to protocols that failed to clearly articulate their trust assumptions.

The IETF's embrace of this principle reflects a maturation in thinking about distributed systems security. Modern Internet protocols must operate in environments where some actors are malicious, some are merely incompetent, and even trusted parties may have conflicting interests. By requiring explicit trust models upfront, the principle forces protocol designers to confront these realities rather than hoping they will resolve themselves through implementation experience.

## Understanding This Principle

**The Core Idea** — Trust relationships must be defined before protocol design. Think of this like designing the organizational chart and access controls for a new company before you build the office building and IT systems.

Consider how a well-run corporation handles sensitive information. Before they design workflows, install computer systems, or even hire employees, leadership maps out who needs access to what information and why. The CEO trusts the CFO with financial data, but perhaps not with customer service decisions. The engineering team trusts the product manager to define requirements, but not to push code to production. Department heads trust each other for coordination, but validate claims about budget and timeline independently. These trust relationships aren't accidents — they're deliberate architectural decisions that shape every process, system, and policy that follows.

When a company skips this step and just "figures out permissions later," chaos ensues. Employees either can't access what they need to do their jobs, or they can access everything and sensitive data leaks everywhere. Projects stall while people argue about who has authority to make decisions. The IT team builds systems that encode the wrong assumptions about information flow, requiring expensive retrofits when the real trust model becomes clear.

**Why It Matters** — The practical consequences of undefined trust are severe and expensive to fix after the fact. In networking protocols, undefined trust creates three categories of failure: security vulnerabilities, operational brittleness, and deployment conflicts.

Consider the difference between early email protocols and modern messaging systems. SMTP, designed in a more trusting era, assumed mail servers would honestly identify themselves and faithfully relay messages. This worked fine in the 1980s academic Internet, but became a spam and phishing nightmare as the network grew. Retrofitting authentication and anti-abuse mechanisms required decades of additional protocols (SPF, DKIM, DMARC) and never fully solved the fundamental trust problem.

Contrast this with modern encrypted messaging protocols like Signal, which explicitly define trust relationships upfront: users trust their own devices completely, trust the service provider not to retain metadata, and trust contacts only after explicit key exchange. This clear trust model shaped every technical decision — from the cryptographic protocols to the data retention policies to the user interface design. The result is a system that's both more secure and more transparent about its limitations.

**The Tension** — The real-world pressure working against this principle is time and cognitive load. Defining trust relationships forces architects to confront difficult questions they'd rather defer: Who might become an adversary? What happens when trusted parties disagree? How do we handle partial trust? These conversations are often political and uncomfortable, involving trade-offs between security, usability, and business requirements.

Engineers naturally want to focus on the interesting technical problems — the algorithms, the performance optimizations, the clever protocol mechanisms. Trust modeling feels like boring paperwork that slows down development. Product managers want to ship quickly and iterate based on user feedback. Defining trust relationships upfront feels like premature optimization when you're not even sure the basic functionality will work.

There's also a cognitive bias toward assuming good faith. Most protocol designers are honest people working with other honest people, so it's easy to unconsciously assume that all participants will behave reasonably. Explicitly modeling adversarial scenarios requires a paranoid mindset that doesn't come naturally to collaborative environments.

**How to Recognize It** — You're seeing this principle at work when:

- System architects spend time mapping out "who trusts whom for what" before writing any code, even for internal tools
- Security reviews begin by examining trust assumptions rather than just looking for implementation bugs
- Deployment documentation clearly states what entities must be trustworthy for the system to work correctly
- Protocol specifications include explicit threat models that name potential adversaries and their capabilities
- Design discussions include phrases like "assuming the PKI is honest" or "if the cloud provider is compromised" rather than treating infrastructure as uniformly trustworthy

## Early IETF Work

The emergence of trust as an architectural principle reflects the Internet's painful evolution from a research network to a global infrastructure. Early Internet protocols like Telnet, FTP, and SMTP were designed for environments where all participants were known, vetted researchers at collaborating institutions. These protocols often transmitted passwords in clear text and assumed that network intermediaries would behave honestly — reasonable assumptions for the ARPANET, but catastrophic for the modern Internet.

The turning point came in the 1990s as commercial traffic grew and security incidents proliferated. The Morris Worm of 1988 demonstrated how protocol vulnerabilities could cascade across the entire network. Meanwhile, the deployment of the World Wide Web created a need for protocols that could operate between strangers with potentially conflicting interests. The IETF's response included both immediate security patches (like SSH replacing Telnet) and deeper architectural reflection about trust assumptions in protocol design.

[RFC 3724](https://www.rfc-editor.org/rfc/rfc3724), published in 2004, represented the culmination of this learning process. The IAB's analysis explicitly connected protocol failures to inadequate trust modeling, arguing that the Internet's evolution toward more "middle boxes" and intermediaries required clearer thinking about end-to-end trust relationships. This RFC didn't just document best practices — it elevated trust modeling from an implementation concern to a fundamental architectural discipline.

## Key References

- [RFC 3724: The Rise of the Middle and the Future of End-to-End](https://www.rfc-editor.org/rfc/rfc3724) — The foundational IAB document establishing trust relationships as a prerequisite for protocol design
- [Zero Trust Architecture (NIST SP 800-207)](https://csrc.nist.gov/publications/detail/sp/800-207/final) — Modern framework for designing systems that assume no implicit trust
- [RFC 8555: ACME](https://www.rfc-editor.org/rfc/rfc8555) — Example of explicit trust modeling in Web PKI automation

## This Principle in IETF Discussions

The principle of trust as architecture manifests across diverse IETF working groups, each grappling with how to make trust relationships explicit in their domains. The discussions reveal both the universal importance of this principle and the domain-specific challenges of applying it.

In authentication and authorization contexts, the principle surfaces as careful mapping of trust boundaries. During IETF 110, the [gnap](https://datatracker.ietf.org/wg/gnap/about/) working group confronted this directly:

> "i am very concerned with privacy and i have done some design using privacy by design which means that you identify the primary appointment first once you have the model component and once you have the trust relationship since we have no trust relationship it's impossible to do a privacy by design"

This comment captures a crucial insight — privacy protections are impossible to design without first understanding who trusts whom. The participant recognized that jumping into technical mechanisms without establishing trust relationships would undermine the entire privacy model.

Routing security discussions show how trust modeling applies to infrastructure protocols. The [6lo](https://datatracker.ietf.org/wg/6lo/about/) working group in IETF 115 discussed extending zero-trust concepts to routing:

> "owned by a single node or if the different owners share the same key then it's possible to ensure that a route can only be injected in the routing fabric by the real owners okay so the same zero conf zero trust I'm sorry the same zero trust capabilities we have for host now becomes available for pre"

This reflects the evolution from traditional routing protocols that trusted network topology announcements to modern approaches that require explicit cryptographic proof of authority.

Certificate and PKI discussions demonstrate how trust relationships must be defined at multiple layers. The [danish](https://datatracker.ietf.org/wg/danish/about/) working group at IETF 110 grappled with certificate chain validation:

> "first one is called the certificate usage parameter which tells you whether the data corresponds to an end entity certificate or some issuing ca in the certificate chain that you should use as a valid trust anchor"

The technical mechanism (certificate usage parameters) exists specifically to make trust relationships explicit — defining which certificates can serve as trust anchors for different purposes.

More recent discussions show increasing sophistication in trust modeling. The [oauth](https://datatracker.ietf.org/wg/oauth/about/) working group at IETF 120 explored enterprise identity federation:

> "says that it's okay for me to get an access token to access this data uh and then it can respond with an access token the reason that this can work is because again both of these applications have a trust relationship with the Enterprise IDP through a single sideon"

This demonstrates mature thinking about transitive trust — understanding that A trusting C and B trusting C enables certain interactions between A and B, but only for specific purposes and under defined conditions.

The discussions also reveal ongoing challenges in trust modeling. The [deleg](https://datatracker.ietf.org/wg/deleg/about/) working group at IETF 120 acknowledged the complexity of different trust models:

> "there are going to be people for both of these who are very passionate about different trust models I think that there is a meta requirement here not meta the company Ben meta the real me"

This highlights that even with broad agreement on the principle of explicit trust modeling, communities often disagree about which trust model is appropriate for their use case.

## Historical Analysis

Discussion of trust as an architectural principle has remained consistently high across IETF 110–123, appearing in 252 sessions across all 14 meetings. The frequency shows remarkable stability, ranging from 11 discussions in IETF 111 to 22 discussions in multiple meetings (113, 114, 116, 118).

| Meeting | Date | Location | Sessions |
|---------|------|----------|----------|
| IETF 110 | March 2021 | Online | 19 |
| IETF 113 | March 2022 | Vienna | 22 |
| IETF 114 | July 2022 | Philadelphia | 22 |
| IETF 116 | March 2023 | Yokohama | 22 |
| IETF 118 | November 2023 | Prague | 22 |

The principle spans an exceptionally broad range of working groups (100 unique groups), indicating its fundamental nature rather than domain-specific relevance. The most active working groups reveal clear patterns: [sidrops](https://datatracker.ietf.org/wg/sidrops/about/) (11 discussions) focuses on routing security, [dnsop](https://datatracker.ietf.org/wg/dnsop/about/) (9) handles DNS security, and [stir](https://datatracker.ietf.org/wg/stir/about/) (8) works on telephone call authentication — all domains where trust relationships are particularly complex and consequential.

The emergence of newer working groups like [rats](https://datatracker.ietf.org/wg/rats/about/) (Remote Attestation Procedures, 7 discussions) and [scitt](https://datatracker.ietf.org/wg/scitt/about/) (Supply Chain Integrity, Transparency, and Trust, 6 discussions) suggests that trust modeling is becoming more sophisticated and specialized. These groups exist specifically to define trust relationships for emerging security challenges.

The sustained discussion frequency across the 2021-2025 timeframe likely reflects several trends: the continued growth in Internet-connected devices requiring authentication, increased awareness of supply chain security after high-profile compromises, and the maturation of zero-trust architectural concepts from enterprise IT into Internet protocols.

## Resources

- [RFC 3724: The Rise of the Middle and the Future of End-to-End](https://www.rfc-editor.org/rfc/rfc3724) — Essential reading for understanding how trust assumptions shape protocol design decisions
- [Zero Trust Architecture (NIST SP 800-207)](https://csrc.nist.gov/publications/detail/sp/800-207/final) — Comprehensive framework for designing systems that make trust relationships explicit rather than implicit
- [RFC 8555: ACME (Automatic Certificate Management Environment)](https://www.rfc-editor.org/rfc/rfc8555) — Practical example of how explicit trust modeling enables automated certificate management for the Web PKI
- [Remote ATtestation ProcedureS (RATS) Architecture](https://datatracker.ietf.org/wg/rats/about/) — Modern IETF work on defining trust relationships for device attestation and verification

---

*This report was generated from analysis of IETF working group session transcripts from meetings 110-123 (March 2021 - July 2025) using vCon (Conversation Container) methodology.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `58c23ba4-cfc6-4837-a087-7163b5544553` |
Sessions analyzed: 252 |
Generated: 2026-03-14*
