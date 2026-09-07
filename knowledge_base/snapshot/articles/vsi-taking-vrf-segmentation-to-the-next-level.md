---
title: "VSI: Taking VRF Segmentation to the Next Level"
slug: "vsi-taking-vrf-segmentation-to-the-next-level"
updated: 2026-08-31T13:11:06Z
published: 2026-08-31T13:11:06Z
canonical: "knowledge.catonetworks.com/vsi-taking-vrf-segmentation-to-the-next-level"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# VSI: Taking VRF Segmentation to the Next Level

## Overview

Network segmentation has long been a cornerstone of enterprise security architecture. Virtual Routing and Forwarding (VRF) technology introduced the ability to create isolated routing domains within a single physical infrastructure — a powerful concept, but one constrained by the limitations of traditional networking. Cato Networks has fundamentally reimagined this concept with the introduction of Virtualized SASE Instances (VSI), bringing full-stack network and security isolation to the cloud-native SASE era.

## The Limits of Traditional VRF

VRF allows a single physical router or switch to maintain multiple independent routing tables simultaneously, enabling network segmentation without deploying separate physical infrastructure. While this solved early segmentation requirements, the approach carries significant operational and architectural limitations in today's complex enterprise environments.

### Common Use Cases for Traditional VRF

- Separating production, development, and management networks
- Isolating multi-tenant environments in shared infrastructure
- Regulatory compliance requiring network segregation
- Separating IT and OT/IoT environments in industrial settings

### Operational Challenges

- Routing isolation only — security policies are managed separately per-VRF, with no integrated enforcement
- Complex inter-VRF connectivity requires route leaking or additional firewall integration
- Shared management plane — all VRFs are visible and managed from the same administrative context
- Troubleshooting complexity increases significantly with multiple VRFs across distributed environments
- No native RBAC isolation — all network admins typically have visibility across all VRFs
- Overlapping IP address spaces become complex when traffic must cross VRF boundaries or be integrated into a shared routing/security domain.
- Each VRF may require dedicated security tooling integration, multiplying management overhead

## Cato VSI: VRF Reimagined for the SASE Era

Cato's Virtualized SASE Instance (VSI) takes the core concept of VRF - isolated network domains - and extends it across the entire SASE stack. Rather than isolating only the routing layer, a VSI creates a completely independent SASE environment with its own network fabric, security policies, management plane, and administrative access controls.

Each VSI is, in effect, a dedicated SASE cloud instance operating within the Cato global backbone. Organizations can deploy multiple VSIs within the Cato Management Application, each tailored to the specific requirements of a distinct business unit, environment type, or subsidiary.

### What Each VSI Provides

- Independent security policy stack — Firewall, CASB, DLP, IPS, and more, configured per-VSI
- Isolated management and data planes — each VSI has separate configuration, traffic handling, and operational visibility
- Granular RBAC — only grant admins access to the VSIs they are responsible for managing
- Feature set flexibility — different capabilities enabled per VSI to match use-case requirements
- Dedicated network topology — independent SD-WAN, routing, and connectivity settings
- Full audit and logging isolation — separate event streams per VSI

## Use Case 1: Parallel Environments for IT, IoT, and OT

One of the most compelling applications of VSI is enabling organizations to run distinct SASE environments for fundamentally different network populations — IT users, IoT devices, and OT systems — each with independent security postures appropriate to their risk profiles and operational requirements.

![usecase_1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35754037310365.png)

### Why This Matters

IT, IoT, and OT environments have dramatically different security and connectivity requirements. Traditional VRF-based segmentation isolates routing but still requires shared security infrastructure and management tooling, creating risk and complexity. With VSI, each environment operates as an independent SASE instance:

**IT / IoT / OT VSI Architecture**

- IT VSI: Full user-centric security stack — ZTNA, CASB, DLP, malware prevention, user identity integration
- IoT VSI: Lightweight connectivity profile — device allowlisting, strict egress controls, minimal attack surface
- OT VSI: Air gap-style isolation for OT systems, with policy-controlled connections to the IT VSI for approved data flows

Each team's administrators manage only their own VSI, eliminating the risk of inadvertent cross-environment configuration changes while enabling specialized expertise for each domain.

## Use Case 2: Mergers & Acquisitions

IP address conflicts are among the most common and challenging integration challenges following a merger or acquisition. When the acquired company uses overlapping RFC 1918 address space, administrators face a difficult choice: undertake a costly and disruptive re-addressing project, or implement complex NAT-based workarounds.

### The Traditional Approach - and Its Problems

- IP re-addressing projects are time-consuming, disruptive, and expensive — often spanning 12–24 months
- Complex double-NAT configurations introduce latency, break applications, and create persistent troubleshooting challenges
- VRF-based workarounds require ongoing configuration management and limit integration flexibility
- Shared management infrastructure creates visibility and access control concerns during the integration period

### The VSI Approach

With VSI, the acquired company is simply onboarded to a new, dedicated SASE instance. Their existing IP addressing scheme remains completely intact. The parent company's VSI and the acquired company's VSI are then interconnected with precise, policy-governed access controls — allowing specific traffic flows while enforcing Zero Trust principles at the boundary.

#### M&A Integration Pattern with VSI

Step 1: Spin up a new VSI for the acquired company — takes minutes, not months

Step 2: Onboard acquired company sites, users, and workloads to the new VSI

Step 3: Retain the existing IP addressing scheme — no re-addressing required

Step 4: Define VSI interconnect policies — granular, Zero Trust access between the two VSIs

Step 5: IT integration projects can proceed at a measured pace without operational disruption

![usecase_2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35754005797917.png)

This approach is especially well-suited to holding companies managing multiple operating subsidiaries (op-cos). Each op-co can maintain a degree of IT and network independence within its own VSI, while the parent organization retains governance and the ability to selectively share resources or services across VSI boundaries.

## VSI Interconnection: Zero Trust at the Boundary

VSIs are not isolated islands — Cato provides controlled interconnection between VSIs with policy-based access controls rooted in Zero Trust principles. Rather than the coarse-grained route leaking of traditional VRF designs, VSI interconnect enforces:

- Identity and context-aware access — who can reach what, under which conditions
- Application-level segmentation - specific applications or services, not entire subnets
- Continuous inspection — traffic crossing VSI boundaries passes through Cato's security stack
- Centralized policy visibility - interconnect rules are managed within the familiar Cato Management Application

This capability transforms VSI interconnection from an operational afterthought into a first-class security control — aligning with modern Zero Trust architectures without introducing additional infrastructure complexity.

## Traditional VRF vs. Cato VSI: At a Glance

| Capability | Traditional VRF | Cato VSI |
| --- | --- | --- |
| Routing Isolation | Layer 3 only | Full SASE stack (L3–L7) |
| Security Policies | Separate per-VRF config | Independent per VSI |
| Management Plane | Shared | Fully isolated |
| RBAC | Limited | Granular, per-VSI |
| Interconnection | Complex route leaking | Zero Trust policy-based |
| Overlapping IPs (M&A) | Complex NAT required | Native support |
| Provisioning Time | Days/weeks | Minutes |
| Troubleshooting | Complex, multi-tool | Single pane of glass |

## Summary

Virtualized SASE Instances represent a fundamental evolution beyond traditional VRF technology. By extending isolation from the routing layer to the full SASE stack — encompassing security policy, management plane, RBAC, and data plane — VSI enables organizations to architect truly independent network and security environments at cloud scale.

Whether the goal is separating IT from OT, managing a post-acquisition integration, or enabling subsidiary independence within a holding company structure, VSI delivers the isolation of a dedicated infrastructure deployment with the operational simplicity of a unified cloud platform.
