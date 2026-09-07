---
title: "What is Cato SD-WAN"
slug: "what-is-cato-sd-wan"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/what-is-cato-sd-wan"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is Cato SD-WAN

## Overview

Traditional WAN architectures are difficult to scale for modern enterprises that rely on multiple branch sites, cloud resources, SaaS applications, and Internet-based connectivity. Static routing, limited visibility into last-mile performance, and dependence on manually managed WAN links make it harder to maintain application performance and resiliency. SD-WAN addresses these challenges by using centralized, policy-based routing to steer traffic according to real-time link conditions, application requirements, and business priorities. This lets you use multiple WAN transports more efficiently while improving availability and simplifying operations.

Cato SD-WAN extends these core capabilities with a cloud-native architecture that connects sites to the Cato Cloud over encrypted overlay tunnels. Cato Sockets continuously monitor link health and calculate the best path for traffic based on metrics such as latency, jitter, packet loss, and distance. This lets you optimize traffic for sensitive applications and maintain service continuity when link quality degrades or a path becomes unavailable. Cato also supports active/active traffic handling, packet loss mitigation, MTU optimization, TCP acceleration, and bandwidth management to improve last-mile performance.

This solution reduces the operational complexity that is common in traditional WAN deployments. Instead of managing separate devices and policies for routing, optimization, and connectivity, you manage SD-WAN behavior from the Cato Management Application (CMA) as part of a single converged platform. This provides centralized visibility into site and link performance and lets you apply consistent networking and security policies across sites, cloud environments, and remote users.

## Using SD-WAN to Connect to the Cato Cloud

There are multiple ways for sites and edge devices to connect to PoPs in the Cato Cloud:

- Physical edge sites with Sockets
- Edge sites with third-party device interoperability using IPSec
- Software-based access, such as Cato’s ZTNA Client, Enterprise Browser, or Browser Extension

For more information about comparing Socket vs. IPsec sites, please see [Connecting Sites to the Cato Cloud](/v1/docs/connecting-sites-to-the-cato-cloud).

### Secure Overlay

Cato uses DTLS to establish secure, low-latency tunnels between sites and the Cato Cloud backbone. Using UDP enables efficient transport for latency-sensitive traffic, while encryption ensures data integrity and confidentiality across public networks.

### Steering

Steering is the algorithm used to determine which of the many globally dispersed Cato PoPs a Socket attempts to connect to for the optimal traffic flow.

Most sites can connect to almost any PoP in the Cato Cloud infrastructure, barring [specific and limited regional considerations.](/v1/docs/country-s-allocation-to-license-groups-and-ztna-users) There are a few algorithmically defined balancing factors designed to ensure any given user or site is connected to the optimal PoP, based on:

- Physical and logical distances between the site and the PoP
- PoP health and load status
- PoPs in the same country as connecting sites
- Underlay connection quality between the site and the PoP

## Redundancy and Availability for Sockets

SD-WAN topologies support multiple links, combined with real-time monitoring to provide multi-link resilience and precedence-based, SLA driven redundancy.

For more information on Socket link redundancy and precedence behaviours, see [Cato Socket Link SLA Architecture](/v1/docs/cato-socket-link-sla-architecture).

### Connection Health

Cato monitors connection health across all WAN links in real time. This allows Sockets to switch between multiple active links or activate passive links. For example, the Socket can activate a backup cellular link if there is an issue with the wired cables.

When the connectivity SLA is within the acceptable SLA thresholds, the Socket remains connected to the same PoP and uses the real-time path-selection algorithms to select the best link for each new flow.

When there is an unacceptable SLA for the primary link in a site, the Socket activates the secondary passive link and sends traffic over it to the PoP. If no link has good SLA metrics, the site connects to an alternative PoP. When the primary link returns to an acceptable SLA, the Socket moves the flows back to the primary link, and the secondary link is deactivated.

For more information on fine-tuning what thresholds are used for each site, see [Configuring the Connection SLA Settings](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites)

Cato offers a range of connection health alert triggers that administrators can use to inform them of dynamic network health conditions with different configurable triggers. For more information, see [Working with Link Health Rules](/v1/docs/working-with-link-health-rules).

### WAN Recovery

Inherent in the SD-WAN model is the ability for Socket sites to leverage existing WAN connections to the public Internet. These connections are generally used to connect to the global private backbone. However, sites can also communicate with each other via site-to-site tunnels directly over these connections using off-cloud transport. If the Cato private backbone is unavailable, sites can leverage these connections to ensure resiliency for all data.

![WAN Recovery.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35675890318493.png)

To read more about Socket site resiliency, see [Socket Site Resiliency with WAN Recovery](/v1/docs/socket-site-resiliency-with-wan-recovery).

## Path Selection and Optimization Policies

Among the benefits of having Cato as an overlay across multiple ISP links is the ability to intelligently define egress paths and optimisation profiles for outbound traffic.

### Bandwidth Management and Prioritisation

Cato’s bandwidth management policy suite lets admins control prioritisation for configurable traffic classes when underlay resources are limited or constrained. In SD-WAN architectures, ISP traffic policing or shaping cannot be relied on to smartly discard non-critical packets in case of congestion. Use [Bandwidth Management Profiles](/v1/docs/configuring-bandwidth-management-profiles) to ensure that critical services and applications are not affected and are instead guaranteed bandwidth.

### Real Time Monitoring

Monitoring the health status of individual ISP links is a critical component of making informed networking and best-path decisions for traffic. The CMA has multiple pages to help you monitor the status of all individual links that make up the underlay between a site and the Cato Cloud. You can track a variety of health indicators across the underlay links, as well as how that traffic is split into the configured priority classes.

For more information on monitoring links in real time, see [Analyzing Data for a Site in Real Time](/v1/docs/analyzing-data-for-a-site-in-real-time).

### Network Rules

Traffic handling is governed by a centralized Network Rules policy that defines routing behavior, transport selection, and optimization profiles based on application, source, and destination context. Define rules to tailor handling of traffic, as well as any optimisation policies such as [TCP acceleration](/v1/docs/explaining-the-cato-tcp-acceleration-and-best-practices) or [packet loss mitigation](/v1/docs/packet-loss-mitigation-for-multi-tunnel-links).

Additional transport modes available include:

- [Bypass](/v1/docs/bypassing-the-cato-cloud-site-level-policy) - Traffic is routed via a local Socket to the Internet via a local underlay connection, bypassing the Cato Cloud infrastructure. Bypass traffic is not inspected by security engines in the PoP
- [Backhaul](/v1/docs/backhauling-traffic-to-a-lan-device-behind-a-socket) - Traffic is sent across the Cato SD-WAN to an Internet egress point at a designated Socket site
- [Off-cloud](/v1/docs/routing-traffic-to-an-off-cloud-link) - Traffic between Socket sites is sent over an encrypted tunnel between the sites over the public internet. Off-cloud traffic is not inspected by security engines in the PoP

For more information, see [What are Network Rules?](/v1/docs/what-are-network-rules)

## Migrating to Cato SD-WAN

Cato allows for a gradual transition of sites from in-use connection technologies to a full SD-WAN model by leveraging a hybrid WAN model.

Hybrid WAN configurations allow for an easy increase in bandwidth by inserting Internet connections alongside an existing MPLS network. Offloading traffic from MPLS allows for reductions in monthly bandwidth costs and to turn up new installations faster by leveraging indigenous Internet access links.

![asymmetricTrafic.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35675867632157.png)

A hybrid WAN can be a permanent solution or a temporary configuration to allow traffic to be gradually moved from the MPLS line onto the Cato SD-WAN. For example, configure the Network Rule policy to only send video and voice data over MPLS.

In addition, sites utilising IPSec to connect to corporate resources can terminate those tunnels directly to a PoP. This ensures secure connectivity is maintained as sites transition in a gradual fashion away from IPSec or MPLS forward connectivity to the Cato SD-WAN model.

For more information on transitioning to the SD-WAN model using a hybrid WAN configuration, see [Integrating Cato with an Alt WAN Network](/v1/docs/integrating-cato-with-an-alt-wan-network) and [Configuring Sites with IPsec Connections](/v1/docs/configuring-sites-with-ipsec-connections).
