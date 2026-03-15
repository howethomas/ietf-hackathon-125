# Principle of least surprise

## Introduction

The principle of least surprise stands as one of the fundamental tenets of good Internet architecture, asserting that systems should behave in ways that least surprise their users and implementers. This principle emerged from decades of software engineering wisdom and found formal expression in Internet architecture through [RFC 3439](https://www.rfc-editor.org/rfc/rfc3439), which codified essential guidelines for Internet design.

At its core, this principle recognizes that the Internet's success depends not just on technical correctness, but on the predictability and intuitiveness of its protocols and systems. When network protocols, APIs, or data formats behave unexpectedly, they create friction that cascades through the entire Internet ecosystem—from the engineers implementing protocols to the applications built on top of them, and ultimately to end users.

The principle's importance in IETF work cannot be overstated. As the Internet has grown from a research network to critical global infrastructure, the cost of surprising behavior has multiplied exponentially. A protocol quirk that might have affected dozens of researchers in the 1980s can now impact billions of users and countless applications. This reality has made the principle of least surprise not just a nice-to-have design goal, but an essential requirement for Internet-scale systems.

## Understanding This Principle

**The Core Idea** — Systems should work the way people naturally expect them to work. Think of a well-designed city where streets follow logical patterns, signs are placed where drivers need them, and similar-looking buildings serve similar purposes. When you arrive in such a city, you can navigate effectively using your existing mental models about how cities work. You don't constantly encounter streets that dead-end without warning, signs that use completely different symbols than everywhere else, or buildings that look like libraries but turn out to be fire stations.

The principle of least surprise operates on the same logic. When engineers encounter a new protocol or API, they bring mental models built from their experience with similar systems. A well-designed system leverages these existing mental models rather than violating them. The protocol behaves as expected based on patterns the engineer already knows, making it easier to implement correctly and maintain over time.

**Why It Matters** — Surprising behavior doesn't just create momentary confusion—it creates systemic problems that compound over time. Consider the difference between two data formats: JSON, which follows predictable rules about nesting and typing, versus early XML schemas that sometimes used attributes and sometimes used elements for the same types of data, with no clear pattern. Engineers working with JSON can quickly build reliable intuitions about how it works. They can predict how edge cases will behave and write robust parsing code. Engineers working with inconsistent XML schemas, by contrast, must constantly refer to documentation, handle special cases, and debug unexpected failures.

The consequences multiply across the ecosystem. Surprising protocols take longer to implement correctly, leading to more bugs in initial deployments. They're harder to debug when problems arise, increasing operational costs. They're more likely to be implemented differently by different vendors, creating interoperability problems. Most critically, they create a cognitive burden that accumulates as systems become more complex. An engineer who encounters surprising behavior in one part of a system becomes more cautious and slower when working with other parts, even when those parts are well-designed.

**The Tension** — The pressure to violate this principle comes from legitimate engineering constraints. Sometimes the most surprising solution is also the most efficient, secure, or backwards-compatible. Protocol designers face the constant temptation to optimize for technical elegance or performance at the expense of intuitive behavior. They may reuse existing message formats in creative ways to save bandwidth, or overload existing fields to avoid protocol changes. These optimizations often make sense when viewed through the narrow lens of a single protocol, but they create surprising behavior that radiates outward to affect everyone who implements or operates the system.

There's also the "expert bias" problem: protocol designers become so familiar with their own systems that they lose the ability to see them through fresh eyes. What seems obvious and natural to someone who has spent months designing a protocol can be completely opaque to an implementer encountering it for the first time.

**How to Recognize It** — You're seeing this principle at work when:

* APIs use consistent naming patterns and parameter orders across similar functions, making it easy to guess how an unfamiliar function works based on familiar ones
* Error messages provide clear indication of both what went wrong and what action the user should take, rather than cryptic codes that require documentation lookup
* Configuration file formats follow the same syntax rules throughout, so learning one section teaches you how to work with other sections
* Protocol extensions use the same design patterns as the base protocol, making them feel like natural evolution rather than bolted-on additions

## Early IETF Work

The principle of least surprise emerged from hard-won experience in the Internet's formative years, though it wasn't always explicitly articulated as such. Early Internet protocols often prioritized functionality over consistency, leading to systems that worked but surprised implementers in subtle ways. The Simple Mail Transfer Protocol (SMTP), for instance, evolved organically through multiple RFCs, accumulating various command formats and response codes that didn't always follow consistent patterns. While SMTP succeeded in enabling email across the Internet, implementers regularly encountered edge cases where the protocol's behavior didn't match their intuitions.

A more positive example came with the design of the Domain Name System (DNS), which established consistent patterns for message formats, error handling, and hierarchical naming that have proven remarkably durable. DNS's designers made deliberate choices to keep the protocol's behavior predictable: queries and responses follow the same basic structure, error conditions are handled consistently, and the hierarchical namespace works the same way at every level. This consistency contributed significantly to DNS's success and widespread adoption.

The IETF community's growing appreciation for design consistency culminated in RFC 3439, which explicitly articulated the principle of least surprise alongside other architectural guidelines. This RFC represented a shift from purely functional protocol design toward more holistic thinking about how protocols fit into the broader Internet ecosystem. It recognized that technical correctness alone wasn't sufficient—protocols also needed to be approachable and maintainable by the global community of implementers who would ultimately determine their success.

## Key References

- [RFC 3439: Some Internet Architectural Guidelines](https://www.rfc-editor.org/rfc/rfc3439) — The foundational document that formally articulated the principle of least surprise in Internet architecture
- [Principle of Least Astonishment (Wikipedia)](https://en.wikipedia.org/wiki/Principle_of_least_astonishment) — Comprehensive overview of the principle's application across software engineering and user interface design

## This Principle in IETF Discussions

The principle of least surprise manifests regularly in IETF working group discussions, often as a decisive factor in design decisions. During IETF 112's [jsonpath](https://datatracker.ietf.org/wg/jsonpath/about/) working group session, participants grappled with how comparison operations should behave when applied to different data types:

> "this is out of order no no it's highly material i mean we could say that we could say that unless the left-hand side selects a primitive the answer is always false yeah and i think that violates the principle of least surprise in the case that would also make it hard to actually extend this later"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf112/ietf112_jsonpath_29129.vcon.json)*

This discussion exemplifies how the principle influences detailed technical decisions. The working group recognized that having comparison operations return false in unexpected cases would create cognitive friction for implementers and users, even if it simplified the initial specification.

The principle also appears in broader architectural discussions. During IETF 114's [iabopen](https://datatracker.ietf.org/wg/iabopen/about/) session on data minimization, participants connected the principle to privacy considerations:

> "this it's a hard problem but maybe there are some things to say next slide please so we came up with this simple thing it's just called the data minimization principle and and we're trying to use the principle of least privilege and sort of set it in the protocol context"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf114/ietf114_iabopen_29668.vcon.json)*

While this speaker mentioned "least privilege" rather than "least surprise," the discussion shows how IETF participants think about predictability principles across different domains, recognizing that consistent behavior reduces surprises for both implementers and end users.

In more recent discussions, the principle has influenced operational considerations. During IETF 116's [sidrops](https://datatracker.ietf.org/wg/sidrops/about/) session, a participant emphasized the importance of keeping configuration formats intuitive:

> "and has documents and procedures or maybe some tooling how to generate the slurm file but but it is based on my experience very useful to keep this format as simple as possible and and adhere to the principle of least astonishments"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf116/ietf116_sidrops_30204.vcon.json)*

This comment, using the alternative phrasing "least astonishment," shows how the principle extends beyond protocol design into operational tooling. The speaker recognized that surprising configuration file formats create ongoing operational burden for network operators.

The principle also intersects with security considerations, as seen in IETF 116's [suit](https://datatracker.ietf.org/wg/suit/about/) working group discussion about information exposure:

> "if the suit report is unencrypted within an encrypted eat token then what we're doing is exposing private in from our um privileged information to the verifier that they don't actually need so by the principle of least privilege we should at least consider the possibility that there are use cases"

*[View source vCon](https://github.com/vcon-dev/ietf-meeting-vcons/blob/main/ietf116/ietf116_suit_30292.vcon.json)*

Again referencing "least privilege" rather than "least surprise," this discussion shows how related predictability principles influence security design. Unexpected information exposure creates both security risks and cognitive surprises for implementers trying to understand what data flows where.

## Historical Analysis

Discussion of the principle of least surprise occurred sporadically across the analyzed IETF meetings, appearing in 4 sessions across 3 meetings between November 2021 and March 2023. The distribution shows concentrated activity during this period:

| Meeting | Date | Sessions |
|---------|------|----------|
| IETF 112 | November 2021 (Online) | 1 |
| IETF 114 | July 2022 (Philadelphia) | 1 |
| IETF 116 | March 2023 (Yokohama) | 2 |

The discussions spanned diverse working groups—[jsonpath](https://datatracker.ietf.org/wg/jsonpath/about/), [iabopen](https://datatracker.ietf.org/wg/iabopen/about/), [sidrops](https://datatracker.ietf.org/wg/sidrops/about/), and [suit](https://datatracker.ietf.org/wg/suit/about/)—suggesting that the principle's relevance transcends specific protocol domains. The [jsonpath](https://datatracker.ietf.org/wg/jsonpath/about/) discussion focused on API design consistency, [iabopen](https://datatracker.ietf.org/wg/iabopen/about/) addressed architectural principles, [sidrops](https://datatracker.ietf.org/wg/sidrops/about/) concerned operational tooling, and [suit](https://datatracker.ietf.org/wg/suit/about/) dealt with security architecture.

Notably, several discussions used related terminology like "principle of least privilege" and "principle of least astonishments," indicating that IETF participants often think about predictability and consistency principles as a family of related concepts rather than distinct rules. This suggests the underlying values of predictable, intuitive system behavior permeate IETF discussions even when not explicitly labeled as "least surprise."

The concentration of discussions during 2021-2023 may reflect increased attention to user experience and operational complexity as Internet systems have matured. Working groups appear to be more explicitly considering how their technical decisions affect the broader community of implementers and operators, not just the immediate functional requirements.

## Resources

- [RFC 3439: Some Internet Architectural Guidelines](https://www.rfc-editor.org/rfc/rfc3439) — Essential reading for understanding how the principle of least surprise fits into broader Internet architectural thinking
- [Principle of Least Astonishment (Wikipedia)](https://en.wikipedia.org/wiki/Principle_of_least_astonishment) — Provides broader context on how this principle applies across software engineering, user interface design, and system architecture
- [The Design of Everyday Things by Don Norman](https://en.wikipedia.org/wiki/The_Design_of_Everyday_Things) — While not Internet-specific, this classic work explores how good design makes complex systems intuitive and predictable

---

*This report was generated through analysis of IETF meeting transcripts stored in vCon (Virtual Conversation) format, covering meetings 110-123 from March 2021 through July 2025.*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `ee2eb6e6-72cd-4a66-9afc-e80eed3cda06` |
Sessions analyzed: 4 |
Generated: 2026-03-15*
