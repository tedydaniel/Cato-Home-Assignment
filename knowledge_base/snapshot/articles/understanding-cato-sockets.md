---
title: "What are Cato Sockets"
slug: "what-are-cato-sockets"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/what-are-cato-sockets"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What are Cato Sockets

## Overview

Cato Sockets provide secure connectivity to the Cato SASE Cloud while enforcing the networking and security policies defined in the Cato Management Application (CMA). Sockets can be physical or virtual appliances, and they seamlessly connect branch offices, data centers, and cloud environments to the Cato Cloud.

Sockets are available in different form factors, and customers choose the model that best fits the required throughput for the site. All models support zero-touch deployment and automatically connect to the Cato Cloud for provisioning, monitoring, and orchestration, without requiring local configuration.

## Socket Models and Versions

Cato offers the option for customers to use the Socket upgrade service to automatically maintain the latest firmware version. So there's no need to worry about installing and updating the new versions. The upgrade service ensures minimal impact on the Socket (if any), and automatic rollback in the rare case that an issue is detected with the upgrade. The newest Socket versions include performance, connectivity, and stability enhancements, and also the latest capabilities and features.

These are the Socket models:

- X1500 – Designed for small branches.
- X1600 / X1600 LTE – Designed for medium-sized branches. The LTE model provides resiliency and out-of-band connectivity.
- X1700 – High-performance appliance for large sites and on-premises data centers.
- vSocket – A virtual Socket deployed in public cloud platforms such as Azure and AWS, or in virtualized environments like GCP and VMware ESXi. vSockets provide secure connectivity for resources hosted outside physical branches or data centers.

This is a sample topology of X1500 and X1600 LTE sites: ![LTE.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32478434331933.png)

**Related Articles**

- [Understanding Cato's Managed Socket Upgrade Service](/v1/docs/understanding-cato-s-managed-socket-upgrade-service)
- [Cato Socket Deployment Guides and Data Sheets](/v1/docs/cato-socket-deployment-guides-and-data-sheets)
- [Cato Socket: Deep Knowledge](/v1/docs/cato-socket-deep-knowledge)

## Connectivity

Sockets establish DTLS-based tunnels to connect edge locations with the Cato Cloud. Once connected, the Cato Cloud automatically creates a logical mesh topology, establishing tunnels between sites. The WAN firewall enforces policies that determine which inter-site communications are allowed, providing flexible and centralized control over traffic.

Sockets also support direct site-to-site connectivity for specific scenarios, such as:

- MPLS site-to-site communication
- Redundancy using DTLS tunnels between Socket sites over the Internet when access to the Cato Cloud is temporarily unavailable
- Selective exclusion of specific traffic to bypass the Cato Cloud

**Related Articles**

- [Routing Traffic to an Off-Cloud Link](/v1/docs/routing-traffic-to-an-off-cloud-link)
- [Socket Site Resiliency with WAN Recovery](/v1/docs/socket-site-resiliency-with-wan-recovery)

## Cloud-Based Orchestration

Manage Sockets centrally through the Cato Management Application (CMA). Orchestration through the CMA ensures that configuration changes and software updates are automatically distributed to all connected Sockets. The CMA delivers a single management plane for both networking and security functions and lets you define policies once and apply them across all sites.

Capabilities include:

- Zero-touch provisioning simplifies setup by automatically connecting Sockets to the Cato Cloud without local configuration
- Policy-based orchestration applied globally
- Real-time monitoring, logging, and visibility across all connected sites

**Related Articles**

- [Working with Socket Sites](/v1/docs/working-with-socket-sites)
- [Managing Sockets](/v1/docs/managing-sockets)

## SD-WAN Functionality

Sockets deliver full SD-WAN capabilities, combining multiple WAN connections into a resilient, application-aware transport layer. This functionality lets enterprises leverage broadband, MPLS, cellular, and other access links while maintaining secure, optimized connectivity to the Cato Cloud.

The Socket acts as the connection point between the Cato Cloud and the LAN, enabling bidirectional traffic flow. The routing options are fully scalable and include both static routes and BGP dynamic routing.

The Sockets apply the Network Rules policy in the CMA to classify and route traffic based on application, source, destination, or other attributes, ensuring consistent enforcement of business intent across all links.

Key capabilities include:

- Multiple WAN link support – Each Socket can connect to multiple WAN transports (for example, fiber, broadband, LTE). Links can operate in Active/Active for load sharing or Active/Passive for failover.

For example, a branch office uses two broadband circuits in parallel. The Socket distributes traffic across both links to increase throughput and automatically reroutes flows if one circuit experiences packet loss.
- Application-aware routing – Sockets classify traffic at the application level, applying policy-based routing (PBR) rules and QoS policies that ensure business-critical and latency-sensitive traffic is prioritized.

For example, business applications such as Microsoft 365 are sent directly to the Internet from the branch, while all other traffic is routed through the Cato Cloud backbone for inspection and optimization.
- Path selection and remediation – Traffic is dynamically steered across available links based on performance metrics such as latency, packet loss, and jitter. When degradation is detected, the Socket automatically redirects flows to healthy paths.

For example, a site running Microsoft Teams or Zoom meetings detects jitter on one ISP link. The Socket automatically shifts voice and video flows to a healthier path to maintain call quality.

**Related Articles**

- [What are Network Rules](/v1/docs/what-are-network-rules)
- [Part 3: The Socket Traffic Prioritization and QoS](/v1/docs/part-3-the-socket-traffic-prioritization-and-qos)

## App Optimization

Sockets use multiple techniques to optimize application performance over WAN links. Traffic shaping prevents congestion on oversubscribed links. For packet loss mitigation, Sockets can duplicate traffic across WAN links: TCP packets can be duplicated across active links, and UDP packets can be duplicated across active or standby links to improve reliability under packet loss conditions.

Capabilities include:

- Application-aware routing with quality of service (QoS) enforcement
- SLA monitoring and health checks of WAN paths
- Dynamic path selection across multiple WAN links
- Prioritization of business-critical and latency-sensitive applications, including UCaaS and VoIP

**Related Articles**

- [What are the Cato Bandwidth Management Profiles](/v1/docs/what-are-the-cato-bandwidth-management-profiles)
- [Accelerating and Optimizing Traffic](/v1/docs/accelerating-and-optimizing-traffic)

## Cloud and SaaS Performance

Sockets enhance performance for cloud-hosted and SaaS applications by applying optimization functions at the edge and routing traffic through the Cato global backbone. This backbone offers predictable latency and loss characteristics compared to the public Internet.

This improves performance for Microsoft 365, Teams, Zoom, Salesforce, and SaaS applications such as Google Workspace, Slack, and Box.

Capabilities include:

- TCP acceleration to reduce round-trip delays
- Packet loss mitigation to improve reliability
- Duplicate packet transmission for real-time applications to reduce jitter
- UDP retransmission to improve the quality of voice and video traffic

**Related Articles**

- [Accelerating and Optimizing Traffic](/v1/docs/accelerating-and-optimizing-traffic)
- [Explaining the Cato TCP Acceleration and Best Practices](/v1/docs/explaining-the-cato-tcp-acceleration-and-best-practices)

## Socket Next Gen LAN Firewall

Each Socket includes a built-in Next Gen LAN Firewall that inspects and enforces traffic policies on packets traversing the Socket LAN interfaces. The LAN Firewall operates at Layer 3/4 (IP, port, protocol) and Layer 7 (application awareness) to control local flows (VLANs or subnets connected to the Socket), WAN, and the Internet.

Capabilities include:

- Policy enforcement - Admins can create rules to allow, block, or shape traffic based on source, destination, port, protocol, and application.

For example, restricting IoT devices to only communicate with approved external services.
- Integration with the CMA - The LAN Firewall policy is centrally defined in the CMA and automatically distributed to all relevant Sockets to ensure consistent enforcement across all sites.
- Segmentation - The LAN Firewall supports segmentation between different VLANs or subnets connected to a Socket, with policies to isolate or control access between business units, guest networks, or sensitive resources.

For example, preventing guest Wi-Fi networks from accessing internal servers.
- Visibility and logging - Socket LAN Firewall actions and events are logged in the CMA for monitoring and compliance.

**Related Articles**

- [What is the Socket Next Gen LAN Firewall](/v1/docs/what-is-the-socket-next-gen-lan-firewall)

## High Availability

High Availability (HA) with Cato Sockets ensures continuous connectivity and service resilience at your sites. There are two complementary approaches to resiliency:

- **Active/Active links** - Each Socket can use multiple WAN links simultaneously. Traffic is distributed across active links to provide load balancing and increased throughput.
- **Active/Passive links** - In an Active/Passive configuration, a Socket designates one WAN link as primary and another as secondary. The Socket continuously monitors link status for both links and automatically activates the passive link if the primary link experiences a failure or performance degradation, ensuring uninterrupted service.
- **High Availability with two Sockets** - Deploy two Sockets in an active/standby pair for redundancy. If the active Socket fails, the standby device automatically takes over, minimizing downtime and maintaining traffic forwarding.

Capabilities include:

- Automatic failover between active and standby Sockets
- Load balancing and link resiliency with Active/Active WAN connections
- Health monitoring of Sockets and links to detect failures and trigger switchover
- Consistent configuration between HA peers managed through the CMA
- Support for both hardware and virtual Socket deployments

**Related Articles**

- [What is Socket HA](/v1/docs/what-is-socket-ha)
- [Understanding Acceptable and Unacceptable SLA for Sites](/v1/docs/understanding-acceptable-and-unacceptable-sla-for-sites)
- [Active/Active Traffic Distribution](/v1/docs/active-active-traffic-distribution)
