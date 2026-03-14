# Layering principle

## Introduction

The layering principle stands as one of the fundamental architectural concepts that has shaped the Internet since its inception. This principle organizes protocol design into distinct layers, each with clearly defined responsibilities and interfaces, enabling modular development and maintenance of complex network systems. The concept traces its origins to the early work of Vint Cerf and Bob Kahn in their seminal 1974 paper ["A Protocol for Packet Network Intercommunication"](https://www.cs.princeton.edu/courses/archive/fall06/cos561/papers/cerf74.pdf), which laid the groundwork for what would become the Internet Protocol suite.

Formally documented in [RFC 1122](https://www.rfc-editor.org/rfc/rfc1122) and further elaborated in [RFC 3439](https://www.rfc-editor.org/rfc/rfc3439), the layering principle enables different aspects of network communication to be developed independently while maintaining interoperability. Each layer provides services to the layer above it while utilizing services from the layer below, creating a hierarchy that ranges from physical transmission at the bottom to application-specific protocols at the top. This separation of concerns allows engineers to modify or replace protocols at one layer without disrupting the entire system.

The principle's significance in IETF work cannot be overstated, as it provides the foundational framework for virtually all Internet protocol development. From routing protocols that operate at the network layer to application protocols that depend on reliable transport services, the layering principle guides how new technologies are integrated into the existing Internet architecture while preserving backward compatibility and enabling future innovation.

## Key References

- [RFC 1122](https://www.rfc-editor.org/rfc/rfc1122): Requirements for Internet Hosts, which formally defines the Internet protocol stack layering architecture.
- [RFC 3439](https://www.rfc-editor.org/rfc/rfc3439): Some Internet Architectural Guidelines and Philosophy, providing guidance on how layering principles should influence protocol design decisions.
- [A Protocol for Packet Network Intercommunication](https://www.cs.princeton.edu/courses/archive/fall06/cos561/papers/cerf74.pdf): The foundational 1974 paper by Cerf and Kahn that introduced the concept of internetworking through layered protocols.

## This Principle in IETF Discussions

Analysis of IETF working group discussions reveals that the layering principle remains actively relevant across diverse protocol development efforts. The principle manifests in discussions ranging from basic layer separation to complex cross-layer optimization challenges.

In the BESS (BGP Enabled Services) working group during IETF 110, participants grappled with the intersection of layer 2 and layer 3 functionality in integrated routing and bridging (IRB) scenarios:

> "one comment first question is about symmetric and asymmetric irb support for the p support symmetric irb what it will be the folding behavior when it does the intersecting routing is going to do layer 2 eventually do layer 2 forwarding to p1 that that is correct when we would do layer 2 forward"

This discussion illustrates a common challenge in modern networking where traditional layer boundaries become blurred, requiring careful consideration of how different protocol layers interact while maintaining architectural clarity.

The DMM (Distributed Mobility Management) working group highlighted another aspect of layering during IETF 110, focusing on cross-layer data frame consistency:

> "clarification and conclusion and next step next slide please so to recap the objective this draft discusses our solution approach and its architectural benefits of common data frame across domains and across layers background for this is that the current mobility related discussion in ietf"

This excerpt demonstrates how mobility solutions must consider data consistency across multiple protocol layers, showing that while layers provide separation, they must also coordinate effectively to support mobile devices moving across network boundaries.

The LSVR (Link State Vector Routing) working group encountered a classic layering challenge when discussing potential layer 2 broadcast storms:

> "aware that also that rob is contemplating upgrading updating the lsoe open source implementation to l3dl so that kind of wraps the status so sue raised an issue about the hello pdu possibly causing a layer 2 storm next slide please if you remember the hello is a multicast layer 2 pdu being sent from"

This discussion exemplifies how protocol designers must carefully consider the implications of their designs on lower layers. A layer 3 routing protocol's hello mechanism, if not properly designed, can create unintended consequences at layer 2, demonstrating the importance of understanding layer interactions.

The BMWG (Benchmarking Methodology) working group discussion during IETF 110 revealed how measurement and testing must account for different layer behaviors:

> "the second point is the rsa2544 says okay you measure the throughput with zero packet loss right but you as you know this is layer 7. there's a retransmission tcp and you of course you will see packet loss and then you have a"

This conversation highlights how network measurement must consider the behavior of different layers independently. While layer 3 might experience packet loss, layer 7 applications using TCP may not see this loss due to retransmission mechanisms, illustrating why layered measurement approaches are essential for accurate performance assessment.

## Historical Analysis

The frequency of layering principle discussions across IETF meetings 110-123 shows sustained engagement with this foundational concept, with notable variations that reflect the evolution of Internet technologies and challenges.

| Meeting | Sessions | Notable Trends |
|---------|----------|----------------|
| IETF 110 (Mar 2021) | 23 | Post-pandemic virtual meeting baseline |
| IETF 111-112 (Jul-Nov 2021) | 32 each | Increased virtual collaboration |
| IETF 113-116 (Mar 2022-Mar 2023) | 35-38 | Peak discussion period, hybrid meetings |
| IETF 117-121 (Jul 2023-Nov 2024) | 30-36 | Stabilized discussion levels |
| IETF 122 (Mar 2025) | 23 | Lower activity period |
| IETF 123 (Jul 2025) | 39 | Recent surge in layering discussions |

The data reveals several interesting patterns. The peak discussion period during IETF 113-116 coincided with the return to in-person meetings and the development of several major protocol initiatives including network slicing, intent-based networking, and advanced routing technologies. These developments required careful consideration of how new capabilities would fit within existing layered architectures.

The working groups most actively discussing layering principles reflect areas where layer interactions are particularly complex. BESS (14 sessions) deals extensively with bridging layer 2 and layer 3 services, while CCAMP (13 sessions) focuses on control and management of optical networking layers. TEAS (12 sessions) works on traffic engineering across multiple layers, and DMM (11 sessions) addresses mobility across protocol stack layers. The presence of PIM (11 sessions) and 6man (10 sessions) in the top groups indicates ongoing evolution in multicast and IPv6 architectures that requires careful attention to layering boundaries.

The recent surge in discussions at IETF 123 suggests renewed focus on layering principles, possibly driven by emerging technologies such as network function virtualization, edge computing, and IoT protocols that challenge traditional layer boundaries while requiring adherence to fundamental architectural principles.

## Resources

- **[OSI Model (Wikipedia)](https://en.wikipedia.org/wiki/OSI_model)**: Provides comprehensive background on the theoretical seven-layer model that influences Internet protocol design, though the Internet uses a more pragmatic four-layer model.

- **[RFC 3439: Some Internet Architectural Guidelines and Philosophy](https://www.rfc-editor.org/rfc/rfc3439)**: Essential reading for understanding how layering principles should guide protocol design decisions and architectural evolution in the Internet.

- **[Internet Protocol Suite (Wikipedia)](https://en.wikipedia.org/wiki/Internet_protocol_suite)**: Detailed explanation of the actual four-layer Internet model (Link, Internet, Transport, Application) with examples of protocols at each layer.

- **[RFC 1122: Requirements for Internet Hosts](https://www.rfc-editor.org/rfc/rfc1122)**: The definitive specification of Internet protocol stack layering, including detailed requirements for how layers should interact and the services each layer provides.

- **[A Protocol for Packet Network Intercommunication](https://www.cs.princeton.edu/courses/archive/fall06/cos561/papers/cerf74.pdf)**: The historical foundation document that introduced internetworking concepts and layered protocol design, essential for understanding the origins of current Internet architecture.

---

*This report was generated from analysis of vCon (Virtual Conversation) transcripts from IETF working group sessions, meetings 110-123 (March 2021 - July 2025).*

---

*This report was generated from vCon analysis of IETF working group session transcripts (meetings 110–123).
Source: [vcon-dev/ietf-meeting-vcons](https://github.com/vcon-dev/ietf-meeting-vcons) |
Analysis: IETF 125 Hackathon — vCon Principles Detection |
Group vCon UUID: `7cdc109d-9157-4b3c-b121-84cb5c5dc590` |
Sessions analyzed: 456 |
Generated: 2026-03-14*
