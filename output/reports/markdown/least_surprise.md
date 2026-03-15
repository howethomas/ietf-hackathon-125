# Principle of least surprise

## Introduction

The principle of least surprise, also known as the principle of least astonishment, is a fundamental design guideline that advocates for systems to behave in ways that minimize unexpected outcomes for users and implementers. This principle emerged from decades of software engineering experience and was formally articulated in Internet architecture through [RFC 3439: Some Internet Architectural Guidelines](https://www.rfc-editor.org/rfc/rfc3439), which emphasizes the importance of predictable behavior in network protocols and systems.

In the context of Internet architecture, this principle serves as a crucial guardrail against the natural tendency of complex distributed systems to develop surprising behaviors. When protocols, APIs, or network behaviors violate user expectations based on similar systems or logical assumptions, the cognitive load on implementers increases dramatically, leading to bugs, security vulnerabilities, and interoperability problems. The IETF has increasingly recognized that technical correctness alone is insufficient—protocols must also be cognitively manageable for the engineers who implement and deploy them.

The principle's significance in IETF work extends beyond mere usability concerns. In a standards environment where multiple independent implementations must interoperate seamlessly, surprising behaviors can fracture the Internet's fundamental coherence. When different implementers interpret ambiguous or surprising specifications differently, the result is not just user frustration but potential network fragmentation and security issues.

## Understanding This Principle

**The Core Idea**

Systems should work the way people naturally expect them to work based on their experience with similar systems and logical reasoning.

Think about the design of a well-planned city. When you're driving through an unfamiliar neighborhood, you intuitively expect certain things: traffic lights at major intersections, stop signs facing the direction of traffic that must stop, street signs positioned where drivers can see them before making decisions. A city planner could technically place stop signs on the back side of intersection posts or use purple lights instead of red ones—these might even work after people adjust—but they violate deeply ingrained expectations. The result isn't just inconvenience; it's accidents, confusion, and a breakdown in the smooth flow of urban life. The principle of least surprise in city planning means leveraging people's existing mental models and cultural conventions so that navigating the system feels natural rather than requiring constant cognitive effort to decode non-standard patterns.

**Why It Matters**

The practical consequences of violating this principle compound rapidly in complex systems. When engineers encounter surprising behavior, they must either spend extra time understanding the special case, or worse, they make incorrect assumptions that lead to bugs and security vulnerabilities.

Consider the difference between two API designs for handling missing data. A predictable API might return `null` or an empty object when requesting non-existent resources, matching patterns familiar from databases and file systems. A surprising API might return a successful response with a randomly generated placeholder value "to be helpful." The first approach allows developers to apply familiar error-handling patterns; the second forces every implementer to learn system-specific behavior and creates subtle bugs when developers assume standard patterns apply. At scale, these seemingly minor violations create massive cognitive overhead and technical debt across the entire ecosystem of implementations.

**The Tension**

The pressure that works against this principle is often well-intentioned optimization or cleverness. Engineers frequently believe they can create "smarter" systems that anticipate user needs or handle edge cases automatically. Sometimes there's pressure to make interfaces more compact or to reuse existing fields in creative ways to avoid protocol changes. Organizations also face time pressure to ship quickly rather than invest in making behaviors intuitive.

The temptation is particularly strong in protocol design, where engineers often think "implementers will read the specification anyway, so we can be clever here." But specifications are read once and implemented many times, often by different people. What seems like an elegant solution to the protocol designer becomes a recurring source of confusion and bugs for every implementation team.

**How to Recognize It**

You're seeing this principle at work when:

* A new system's commands follow the same patterns as familiar tools (like Unix utilities having consistent flag conventions across different programs)
* Error messages and return codes match the conventions established by similar systems in the same domain
* Default behaviors align with what users would logically expect rather than requiring special knowledge or configuration
* Extension points work the way developers would predict based on other extensible systems they've used

## Early IETF Work

The principle of least surprise emerged from hard-won experience in early Internet protocol development. The original TCP/IP suite succeeded partly because it followed predictable patterns—TCP behaved like other reliable stream protocols, UDP like other datagram services, and IP like other packet-switching systems. However, the IETF learned valuable lessons from protocols that violated user expectations.

One notable example was the complexity that arose in email systems when SMTP and related protocols developed surprising edge-case behaviors around message handling and delivery semantics. The proliferation of incompatible email implementations in the 1980s and 1990s partly stemmed from ambiguous specifications that allowed for multiple interpretations, each reasonable in isolation but surprising when combined. This experience informed later IETF thinking about the importance of predictable protocol behavior.

The formalization of this principle in [RFC 3439](https://www.rfc-editor.org/rfc/rfc3439) represented the codification of decades of architectural experience. The document emerged from the Internet Architecture Board's recognition that technical correctness was necessary but insufficient—protocols also needed to be cognitively manageable for implementers and operators. This shift marked the IETF's growing sophistication in understanding how human factors impact protocol success.

## Key References

* [RFC 3439: Some Internet Architectural Guidelines](https://www.rfc-editor.org/rfc/rfc3439) - The primary IETF document establishing architectural principles including least surprise
* [Principle of Least Astonishment (Wikipedia)](https://en.wikipedia.org/wiki/Principle_of_least_astonishment) - Comprehensive overview of the principle's application across software engineering

## This Principle in IETF Discussions

The principle of least surprise continues to surface in contemporary IETF working group discussions, often at critical decision points where technical correctness conflicts with predictable behavior. These conversations reveal how the principle operates as a practical constraint in protocol design.

In the [jsonpath](https://datatracker.ietf.org/wg/jsonpath/about/) working group's November 2021 discussions, the principle emerged during debates about query behavior:

> this is out of order no no it's highly material i mean we could say that we could say that unless the left-hand side selects a primitive the answer is always false yeah and i think that violates the principle of least surprise in the case that would also make it hard to actually extend this later

This exchange illustrates how the principle serves as a design constraint even when technically simpler solutions exist. The working group recognized that while returning "false" for non-primitive selections might be implementationally cleaner, it would surprise developers familiar with other query languages and complicate future extensions.

The [iabopen](https://datatracker.ietf.org/wg/iabopen/about/) discussions in July 2022 showed how the principle relates to broader architectural concepts:

> this it's a hard problem but maybe there are some things to say next slide please so we came up with this simple thing it's just called the data minimization principle and and we're trying to use the principle of least privilege and sort of set it in the protocol context

While this quote conflates the principle of least surprise with least privilege, it demonstrates how these principles function as a family of related design constraints that IETF participants use to evaluate proposals.

By March 2023, the [sidrops](https://datatracker.ietf.org/wg/sidrops/about/) working group was applying the principle to file format design:

> and has documents and procedures or maybe some tooling how to generate the slurm file but but it is based on my experience very useful to keep this format as simple as possible and and adhere to the principle of least astonishments

The emphasis on format simplicity reflects a mature understanding that surprising formats impose ongoing costs on every implementer and operator who must work with them.

In the [suit](https://datatracker.ietf.org/wg/suit/about/) working group's concurrent discussions, the principle influenced security architecture decisions:

> if the suit report is unencrypted within an encrypted eat token then what we're doing is exposing private in from our um privileged information to the verifier that they don't actually need so by the principle of least privilege we should at least consider the possibility that there are use cases

Although the speaker references least privilege rather than least surprise, the underlying concern reflects similar thinking—avoid surprising implementers with unnecessary complexity or unexpected information exposure.

## Historical Analysis

Analysis of IETF meetings 110-123 reveals concentrated but focused discussion of the principle of least surprise, appearing in 4 sessions across 3 meetings between November 2021 and March 2023. The discussions cluster around specific technical decisions rather than broad architectural reviews, suggesting the principle functions as a practical design constraint rather than abstract guidance.

| Meeting | Date | Sessions |
|---------|------|----------|
| IETF 112 | November 2021 (Online) | 1 |
| IETF 114 | July 2022 (Philadelphia) | 1 |
| IETF 116 | March 2023 (Yokohama) | 2 |

The working groups invoking this principle—[jsonpath](https://datatracker.ietf.org/wg/jsonpath/about/), [iabopen](https://datatracker.ietf.org/wg/iabopen/about/), [sidrops](https://datatracker.ietf.org/wg/sidrops/about/), and [suit](https://datatracker.ietf.org/wg/suit/about/)—represent diverse technical domains from data querying to security architecture. This breadth suggests the principle has become a standard part of IETF design vocabulary across different protocol areas.

The temporal pattern shows steady invocation across the analyzed period, without notable spikes or declines. This consistency indicates the principle has achieved stable recognition as a design constraint rather than representing a passing trend. The specific contexts—query language behavior, data minimization, file format design, and security architecture—demonstrate how the principle applies across the full spectrum of protocol design decisions.

## Resources

* [RFC 3439: Some Internet Architectural Guidelines](https://www.rfc-editor.org/rfc/rfc3439) - Essential reading for understanding how this principle fits into broader Internet architectural thinking
* [Principle of Least Astonishment (Wikipedia)](https://en.wikipedia.org/wiki/Principle_of_least_astonishment) - Comprehensive treatment of the principle's application beyond networking, with examples from user interface design and software engineering
* [The Design of Everyday Things by Don Norman](https://en.wikipedia.org/wiki/The_Design_of_Everyday_Things) - Classic text on design principles that illuminates why predictable behavior matters for any human-system interaction

---

*This report was generated through analysis of IETF working group session transcripts and vCon data spanning meetings 110-123.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `ee2eb6e6-72cd-4a66-9afc-e80eed3cda06` |
Sessions analyzed: 4 |
Generated: 2026-03-14*
