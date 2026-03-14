# End-to-end principle

## Introduction

The end-to-end principle stands as one of the Internet's most fundamental architectural guidelines, establishing that intelligence and complexity should reside at the network's endpoints—the applications and devices that users actually interact with—rather than being embedded within the network infrastructure itself. This principle emerged from the seminal 1984 paper ["End-to-End Arguments in System Design"](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf) by Saltzer, Reed, and Clark at MIT, and was subsequently codified in the Internet's architectural foundations through [RFC 1958](https://www.rfc-editor.org/rfc/rfc1958) and further examined in [RFC 3724](https://www.rfc-editor.org/rfc/rfc3724).

At its core, this principle argues that many functions can only be correctly and completely implemented by the applications themselves, not by intermediate network elements. The network's job should be to provide simple, general-purpose packet delivery, while applications handle the complex logic of reliability, security, ordering, and other sophisticated behaviors. This design philosophy has been instrumental in creating the Internet's flexibility, innovation capacity, and global scalability.

The principle remains actively relevant in IETF discussions today, appearing across 56 working group sessions from March 2021 to July 2025, as engineers grapple with modern challenges like edge computing, AI/ML integration, and the rise of content delivery networks that seem to challenge traditional end-to-end thinking. Understanding this principle is crucial for anyone involved in Internet architecture, as it continues to shape debates about where intelligence should reside in our increasingly complex digital infrastructure.

## Understanding This Principle

**The Core Idea**

The network should be a simple messenger service, with all the smart decisions happening at the endpoints.

Think of this like a postal system. The post office doesn't need to know whether you're sending a love letter, a legal contract, or a birthday invitation. It doesn't need to understand the contents, verify that contracts are legally sound, or ensure that birthday invitations arrive at exactly the right emotional moment. The postal infrastructure has one job: reliably move sealed envelopes from point A to point B. All the intelligence—what to write, how to format it, whether to send it registered mail, what to do if it doesn't arrive—stays with the people at the endpoints.

Now imagine if the postal service tried to be "smart." What if mail sorting facilities started opening letters to optimize delivery based on content, or if postal workers began editing your writing to make it clearer? The system would become incredibly complex, fragile, and slow to adapt. Every new type of communication would require updating the entire postal infrastructure. Innovation would grind to a halt because inventors would need permission from the postal authority to try new forms of correspondence.

**Why It Matters**

When you violate the end-to-end principle, you typically get systems that are brittle, hard to evolve, and hostile to innovation. Consider the difference between the Internet and traditional telephone networks. The old telephone system embedded intelligence in the network switches—they knew about call routing, billing, special services like call waiting, and even basic applications like voicemail. Adding a new feature meant upgrading expensive equipment throughout the entire network infrastructure.

The Internet took the opposite approach. Routers and switches just move packets around based on addresses. All the intelligence—web browsing, email, video streaming, social media—happens in the applications running on end devices. This meant that Tim Berners-Lee could invent the World Wide Web from his office at CERN without asking permission from every Internet service provider. The network didn't need to understand HTTP; it just needed to move the packets.

The result? Explosive innovation on the Internet versus decades of slow, expensive feature rollouts in traditional telecom. When intelligence lives at the endpoints, innovation happens at the speed of software deployment, not infrastructure replacement.

**The Tension**

The real-world pressure against this principle is performance and control. It's often tempting to add intelligence to the network because it seems more efficient. Why make every application implement its own error correction when the network could do it once? Why not have the network compress data, cache popular content, or block malicious traffic?

Sometimes this temptation makes sense—content delivery networks (CDNs) improve performance by caching popular content closer to users, even though this technically violates pure end-to-end thinking. The key insight is that such violations should be optimizations, not replacements for end-to-end functionality. Netflix can still stream video even if a CDN goes down, because the intelligence remains at the endpoints.

The deeper organizational temptation is control. Network operators often want to manage, prioritize, or monetize traffic flows. Governments want to filter or monitor communications. Platforms want to optimize user experiences. But each time intelligence moves into the network, it typically reduces the system's flexibility and concentrates power away from users and innovators.

**How to Recognize It**

You're seeing this principle at work when new applications can be deployed without upgrading network infrastructure. The fact that Zoom could handle massive video conferencing growth in 2020 by scaling their servers, not by upgrading every router between users, demonstrates end-to-end design.

You're violating it when adding new features requires coordinated changes throughout your system's infrastructure layers. If launching a new application type means updating firewalls, routers, and middle boxes across your network, you've probably embedded too much application-specific intelligence in the wrong places.

You're thinking about it correctly when you ask "what's the simplest, most general service the infrastructure can provide?" rather than "how can we make the infrastructure smarter?" The goal is to push complexity to the edges where it can evolve independently, keeping the shared infrastructure as simple and general-purpose as possible.

## Key References

- [RFC 1958 - Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958): The foundational RFC that established core Internet design principles including end-to-end arguments.
- [RFC 3724 - The Rise of the Middle and the Future of End-to-End](https://www.rfc-editor.org/rfc/rfc3724): Examines how the principle has evolved and been challenged by the growth of middleboxes and network address translation.
- [End-to-End Arguments in System Design](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf): The original 1984 paper by Saltzer, Reed, and Clark that introduced and formalized the end-to-end principle.

## This Principle in IETF Discussions

The end-to-end principle continues to generate active discussion in IETF working groups, often in the context of tensions between traditional Internet architecture and modern deployment realities.

In the Data and Information-Centric Networking Research Group (DINRG), participants have been grappling with how the principle applies to today's Internet structure. As one participant observed at IETF 115:

> "drives the user base up and that builds the economy of scale in today's internet the result is really a flattening of the traditional topology of the internet what we've got is a situation where the end-to-end principle isn't really the principle that's at work here right in fact one of the things t"

This reflects ongoing concerns that the Internet's evolution toward content delivery networks and edge computing is fundamentally altering the end-to-end assumptions that guided its original design. The discussion continued at IETF 116, where researchers noted:

> "o be honest and so in terms of the recent evolution of the internet what we see is that principles that were true 20 years ago no longer hold true now for instance we'll talk a little later about the end-to-end principle but one of the things that we see in the last two years in the ITF is this conc"

These conversations highlight a key tension: while the Internet's physical topology has become more centralized around major content providers, the question remains whether this violates the end-to-end principle in practice or simply implements it differently.

The Security Dispatch (SECDISPATCH) working group provided a more nuanced view at IETF 117, discussing how tunneling technologies can preserve end-to-end properties even when intermediate processing occurs:

> "ys like okay that sounds great and and we're only going to send traffic through that and here's my client certificate or something like that uh so this works this is not considered a violation of the end-to-end principle right like packets are still flowing end to end there's a tunnel in the middle"

This illustrates how modern interpretations of the principle focus on preserving end-to-end functionality rather than requiring pure end-to-end packet flows.

In the Secure Asset Transfer Protocol (SATP) working group at IETF 116, participants drew explicit parallels between the end-to-end principle and blockchain consistency models:

> "t to finish the commitment and to ensure both networks are consistent and you hear the word consistent use meaning that there's no double spend literally what that means and this is the analog to the end-to-end principles principle for those who are on the din mailing list uh with lyxia there there"

This connection shows how the principle's core insights about where to place consistency guarantees extend beyond traditional networking into distributed systems design.

By IETF 120, working groups were considering how to apply the principle to emerging user-centric design approaches:

> "nk would be instructive is to consider the end user in all of this um as a starting point uh we wouldn't be starting from scratch um if we did that because there are existing principles including the end to end principle um and rfc's looking at how that's being how it's evolving uh but we think that"

These discussions demonstrate that while the Internet's physical implementation has evolved significantly, the IETF community continues to find the end-to-end principle relevant for guiding architectural decisions, even as they adapt its application to modern realities.

## Historical Analysis

Discussion of the end-to-end principle peaked during the 2022-2023 period, with particularly intense focus at IETF 115 (London, November 2022) and IETF 118 (Prague, November 2023), each featuring 7 sessions where the principle was discussed. This period coincided with growing concerns about Internet centralization and the rise of edge computing architectures.

| Meeting | Date | Location | Discussion Frequency |
|---------|------|----------|----------------------|
| IETF 110 | March 2021 | Online | 5 |
| IETF 111 | July 2021 | Online | 6 |
| IETF 113 | March 2022 | Vienna | 5 |
| IETF 114 | July 2022 | Philadelphia | 6 |
| IETF 115 | November 2022 | London | 7 |
| IETF 116 | March 2023 | Yokohama | 2 |
| IETF 117 | July 2023 | San Francisco | 6 |
| IETF 118 | November 2023 | Prague | 7 |
| IETF 119 | March 2024 | Brisbane | 3 |
| IETF 120 | July 2024 | Vancouver | 1 |
| IETF 121 | November 2024 | Dublin | 1 |
| IETF 122 | March 2025 | Bangkok | 3 |
| IETF 123 | July 2025 | Madrid | 4 |

The Data and Information-Centric Networking Research Group (DINRG) led discussions with 7 sessions, followed by the Delay Tolerant Networking (DTN) and Network Management Research Group (NMRG) with 4 sessions each. This concentration in research groups suggests that much of the current debate around the end-to-end principle is exploratory, examining how the principle should evolve rather than applying it to immediate protocol standardization.

The notable drop in discussions during 2024 (IETF 119-121) may indicate that the community reached some consensus on how to interpret the principle in modern contexts, or that attention shifted to other architectural concerns. The modest uptick in 2025 suggests continued relevance as new technologies like AI/ML integration and quantum networking begin to raise fresh questions about where intelligence should reside in network architectures.

The principle's discussion across 36 different working groups demonstrates its fundamental nature—it's not confined to any single protocol area but emerges whenever engineers must decide how to distribute functionality between network infrastructure and endpoint applications.

## Resources

- [End-to-End Principle (Wikipedia)](https://en.wikipedia.org/wiki/End-to-end_principle): Provides accessible background and examples of the principle's application across different systems.
- [RFC 1958 - Architectural Principles of the Internet](https://www.rfc-editor.org/rfc/rfc1958): Essential reading for understanding how end-to-end thinking shaped the Internet's fundamental design.
- [RFC 3724 - The Rise of the Middle](https://www.rfc-editor.org/rfc/rfc3724): Examines challenges to the end-to-end principle from NAT, firewalls, and other middleboxes—crucial for understanding modern Internet realities.
- [End-to-End Arguments in System Design](https://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf): The original MIT paper that introduced the principle; readable and relevant beyond just networking.

---

*This report was generated from analysis of IETF working group session transcripts using vCon (Virtual Conversation) technology, covering meetings IETF 110-123 (March 2021 - July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `317f8ebe-3225-45da-8907-8704b0027aab` |
Sessions analyzed: 56 |
Generated: 2026-03-14*
