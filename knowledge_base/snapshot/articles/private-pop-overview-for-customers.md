---
title: "Private PoP Overview for Customers"
slug: "private-pop-overview-for-customers"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/private-pop-overview-for-customers"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Private PoP Overview for Customers

This article provides a high-level overview of the Cato Private PoP, including its features, architecture, and FAQ.

## Overview

A Cato Private PoP is an exclusive deployment of the Cato Cloud PoP, hosted within the customer's data center. It delivers a secure, high-performance, and fully managed SASE environment dedicated solely to the customer traffic. This private setup offers localized control, enhanced performance, and security while remaining fully integrated with the global Cato Cloud network.

### Key Features

Cato Private PoPs include all the core features of a standard Cato Cloud PoP, with additional benefits tailored to customer environments:

- **Full SASE Stack:** Delivers a complete set of integrated security and networking services, including SWG, NGFW, IPS, ZTNA, CASB, and SD-WAN.
- **Dedicated Resource Allocation:** Guarantees high availability and performance by isolating resources exclusively, avoiding shared usage with other Cato customers.
- **Local Internet Peering:** Utilizes the customer's own internet backbone, maintaining SLA guarantees and allowing the customer to use their own IP transit routes for optimized routing and performance.
- **Global Reach, Local Control:** While hosted locally, the Private PoP is fully connected to Cato’s global network of public PoPs, allowing you to deliver seamless worldwide connectivity from a unified management platform.

### Managing a Cato Private PoP

One of the defining advantages of the Cato Private PoP is that it is delivered as a fully managed service, operated by Cato Networks.

- **Remote Management by Cato:** Although the PoP is physically installed and hosted by the customer, Cato handles all infrastructure management, maintenance, and operations remotely.
- **Unified Management Interface:** Manage and monitor the entire solution through the Cato Management Application (CMA). There is also visibility into the Private PoP infrastructure through the same platform.
- **Streamlined Software Lifecycle:** Cato provides regular updates, patches, and feature rollouts across the full SASE stack, eliminating the need for manual coordination, multi-vendor integration, or tracking CVEs.
- **Comprehensive Hardware Lifecycle Support:** Cato manages all hardware aspects, including RMA, inventory, and lifecycle transitions, significantly reducing the operational burden on the customer.

### Service Capabilities on Cato Private PoP

The Cato Private PoP supports the full suite of Cato SASE services, identical to those available in Cato’s public PoP locations. This includes Secure Web Gateway (SWG), next-generation firewall (NGFW), IPS, Zero Trust Network Access (ZTNA), Cloud Access Security Broker (CASB), SD-WAN, and more.

In addition to these core capabilities, the Private PoP offers unique advantages by preferring the connection of sites and users to the Private PoP when they are located within the same country or region, ensuring optimal performance, compliance, and reduced latency. If a site or user is located outside the Private PoP’s geographic region, it will seamlessly connect to the nearest available Cato PoP, ensuring a consistent and secure global experience across the entire network.

## Frequently Asked Questions

This section addresses common questions that might arise during the deployment or operation of a Private PoP.

### Technical & Infrastructure

**What are the infrastructure requirements to host a Cato Private PoP?**

To host a Private PoP, the customer must supply the following:

- Rack space in a secure data center
- Redundant power and cooling
- Reliable internet uplinks (for public internet peering or customer connections)
- Physical and network security controls

Cato provides the hardware and manages installation, configuration, and ongoing operations remotely.

**Is high availability (HA) supported in a Private PoP deployment?**

Yes. Cato Private PoPs are designed with high availability in mind. The architecture includes redundant hardware components and failover capabilities to ensure continuous service even during hardware or connectivity failures.

**Is the Private PoP connected to the Cato Cloud backbone?**

The Private PoP is fully integrated into the Cato global backbone. While customer traffic can remain local to the Private PoP, it can also traverse Cato’s global network for remote sites, roaming users, or SaaS access, allowing seamless connectivity and consistent policy enforcement worldwide.

**Can the Private PoP support both IPsec and Socket-based connections?**

Yes. Just like public PoPs, the Private PoP supports both Cato Sockets and standard IPsec tunnels, allowing flexible connectivity options for branch offices, data centers, and third-party integrations.

### Operations & Management

**How are software updates and patches handled in the Private PoP?**

All software updates and patches, including CVE fixes, security enhancements, and new feature rollouts, are managed by Cato. Updates occur automatically by the same cadence as Cato’s public PoPs, ensuring consistency and minimal operational effort.

**Is the Private PoP eligible for the same SLAs as Cato public PoPs?**

Yes. Cato offers the same enterprise-grade SLAs (including up to 99.999% availability) for Private PoPs, leveraging the customer's own high-performance infrastructure while ensuring end-to-end service reliability.

**What happens in case of hardware failure within the Private PoP?**

Cato handles all aspects of hardware support, including RMA, inventory management, and replacement logistics. The customer does not need to stock spares or coordinate with multiple vendors, Cato owns the full hardware lifecycle.

**Can a customer migrate from public PoP to Private PoP over time?**

Yes. Cato offers flexible migration options. Customers can begin with public PoP connectivity and move to a Private PoP later - without disrupting service. Traffic routing and configurations are managed centrally, making the transition smooth and transparent.
