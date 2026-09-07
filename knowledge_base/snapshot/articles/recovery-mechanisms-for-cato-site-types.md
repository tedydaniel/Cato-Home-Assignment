---
title: "Recovery Mechanisms for Cato Site Types"
slug: "recovery-mechanisms-for-cato-site-types"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/recovery-mechanisms-for-cato-site-types"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Recovery Mechanisms for Cato Site Types

## Overview

Cato is designed to maintain traffic continuity even when there is a connectivity issue between a site and a Point of Presence (PoP). Sites connect to PoPs, and traffic then egresses either to the WAN over the Cato Cloud or to the Internet for access to SaaS and Internet applications. Resiliency ensures that when there is a connectivity issue, traffic flows continue with minimal or no impact to end users.

This article explains how Cato achieves resiliency for different site types and how traffic behaves during PoP connectivity issues.

### Cato PoP Architecture

A Cato PoP is a cloud location composed of multiple processing servers. Each PoP is built to handle customer tunnels, apply security services, and forward traffic without relying on a single processing node.

Each PoP node:

- Terminates customer tunnels (DTLS or IPsec)
- Processes and forwards network traffic
- Runs the full Cato software stack, including routing, optimization, and security services such as WAN and Internet Firewall, IPS, and TLS inspection, and so on

This PoP node-based architecture allows the Cato Cloud to maintain traffic processing and security enforcement while minimizing the impact of infrastructure-related issues.

## Socket and vSocket Traffic Resiliency for WAN and Internet

Socket and vSocket sites provide the most resilient model for maintaining WAN connectivity between sites over the Cato Cloud and Internet connectivity for traffic to SaaS applications. This deployment model is designed for sites where traffic continuity and predictable recovery behavior are operationally critical, such as data centers and primary branch locations, and where end users should experience minimal impact when there is a connectivity issue to a PoP.

### Resiliency for PoP Connectivity Issues

When a site has a connectivity issue to a PoP, the Socket automatically works to maintain traffic flows with minimal disruption, without administrator intervention. Recovery is handled progressively to minimize disruption and avoid unnecessary topology changes.

Capabilities include:

1. Automatic reconnection to a different PoP node when a node-level issue is detected
2. Automatic failover to a different PoP when PoP-level connectivity issues persist

These behaviors reduce the impact of transient PoP connectivity issues and help maintain traffic continuity for end users. For more information, see [Understanding Acceptable and Unacceptable SLA for Sites](/v1/docs/understanding-acceptable-and-unacceptable-sla-for-sites).

### Last-Mile and ISP Resiliency

Socket and vSocket sites actively monitor last-mile connectivity to maintain stable tunnels to the Cato Cloud. Traffic steering decisions are based on real-time link conditions rather than static preferences.

Capabilities include:

1. Continuous monitoring of quality and connectivity metrics on each WAN link
2. Support for up to four WAN interfaces per Socket to provide ISP redundancy
3. Active use of multiple WAN links to improve availability and resilience

This model reduces dependency on a single ISP and improves recovery outcomes during last-mile failures.

### Traffic-Specific Recovery Behavior

Sockets apply separate recovery logic to WAN traffic and Internet-bound traffic when there is a PoP connectivity issue. This distinction ensures that loss of PoP connectivity does not unnecessarily impact site-to-site communication or Internet access.

For WAN traffic, the Socket prioritizes maintaining connectivity between sites:

1. WAN traffic is redirected to off-cloud DTLS tunnels (WAN Recovery) when the PoP is unreachable
2. Existing site-to-site sessions continue over the recovery path without requiring re-establishment

For Internet traffic, the Socket applies a different recovery path:

1. Internet-bound traffic is routed directly to the local ISP (Internet Recovery)
2. Traffic egresses from the Socket using the Socket public IP address instead of the PoP IP address

This traffic-specific handling limits the scope of outages and allows WAN and Internet traffic to recover independently based on the type of disruption.

## Operational Best Practices for Socket Resiliency

Correct Socket deployment directly impacts recovery effectiveness. Applying these practices helps ensure predictable behavior and minimal impact to users during PoP connectivity issues.

### General Deployment Best Practices

Best practices include:

1. Deploy at least two ISPs per site in an active/active configuration to avoid single-provider dependency
2. Use Socket High Availability (HA) to protect against local hardware failures
3. Ensure physical path diversity between the site and upstream ISPs
4. Configure static public IP addresses for WAN interfaces, especially for data center sites

For more information, see [Cato Socket Connection Prerequisites and Known Limitations](/v1/docs/cato-socket-connection-prerequisites-and-known-limitations)

### Planning for WAN Recovery

WAN Recovery maintains site-to-site connectivity when a site loses connectivity to the PoP by routing WAN traffic over off-cloud DTLS tunnels. A stable WAN interface configuration is critical to ensure fast convergence and reliable recovery behavior.

Best practices include:

1. Configure static IP addresses on WAN interfaces that participate in WAN Recovery to improve off-cloud tunnel stability

This is especially important for data centers and hub sites.
2. Use the Network > Sites page in the CMA to verify the status of **WAN Recovery Tunnels** after WAN interface or routing changes

For more information, see [Socket Site Resiliency with WAN Recovery](/v1/docs/socket-site-resiliency-with-wan-recovery).

### Planning for Internet Recovery

During Internet Recovery, traffic egresses directly to the Internet from the Socket instead of the PoP. This behavior affects SaaS access and IP-based security policies.

Operational considerations include:

1. Internet traffic is sourced from the Socket public IP address during recovery
2. PoP-based public IP addresses are not used while Internet Recovery is active
3. Allowlist the Socket public IP address for critical SaaS applications to maintain access
4. For example, if applications also use PoP egress, allowlist both the allocated Cato IP address and the Socket public IP address

For more information, see [Using Cato Networks' Internet Recovery](/v1/docs/using-cato-networks-internet-recovery).

## IPsec and Cloud Interconnect Site Resiliency

IPsec and Cloud Interconnect sites rely on PoP-level redundancy to maintain traffic continuity during PoP connectivity issues. Unlike Socket-based sites, these site types do not use off-cloud recovery mechanisms. Resiliency depends on redundant connectivity paths into the Cato Cloud.

### IPsec Site Resiliency

IPsec sites maintain resiliency by establishing tunnels to multiple PoP locations. Failover behavior is determined by the configuration and capabilities of the customer-managed third-party IPsec device.

Capabilities include:

1. Support for primary and secondary tunnels to different PoP locations
2. Active/Passive or active/active tunnel configurations, depending on device support

Operational considerations include:

1. A 99.999% SLA is guaranteed only for IPsec sites connected to at least two different PoP locations, as defined in the Cato MSA
2. Internet Recovery and WAN Recovery are not supported for IPsec sites. This means that WAN connectivity between sites is unavailable during PoP outages

### Cloud Interconnect Site Resiliency

Cloud Interconnect sites use provider-backed connectivity to the Cato Cloud. Resiliency is achieved through redundant provider infrastructure and PoP connectivity.

Capabilities include:

1. Redundant connectivity over the provider backbone
2. Active and passive PoP connectivity based on the Cloud Interconnect design

Operational considerations include:

1. Internet Recovery and WAN Recovery are not supported
2. Traffic availability depends on the provider SLA and the site being connected to multiple PoPs

## Routing Resiliency with BGP

Dynamic routing is critical for maintaining traffic continuity during PoP connectivity issues and network changes. BGP provides adaptive routing behavior that allows sites to converge quickly and continue forwarding traffic when paths change.

It is also possible to use static routing for stable, predefined paths.

### BGP-Based Routing Resiliency

BGP controls how routes are learned and withdrawn during connectivity changes, allowing traffic to shift automatically to reachable paths when failures occur.

Capabilities include:

1. Dynamic path selection based on real-time reachability
2. Automatic route convergence during link, path, or PoP connectivity changes
3. Support for Bidirectional Forwarding Detection (BFD) to reduce failure detection time

Operational considerations include:

1. BGP must be configured on the site router and coordinated with Cato routing settings
2. We recommend using BGP with BFD where dynamic and resilient routing behavior is required.

For more information, see [Configuring BFD for BGP Neighbors](/v1/docs/configuring-bfd-for-bgp-neighbors).

## Summary of Recovery Mechanisms by Site Type

The following table summarizes how different site types maintain traffic continuity when there is a connectivity issue between a site and a PoP. The focus is on what traffic continues to flow and how recovery is achieved, not on feature configuration details.

| Resiliency Aspect | Socket and vSocket Sites | IPsec Sites | Cloud Interconnect Sites |
| --- | --- | --- | --- |
| Connection to multiple PoPs | Yes | Yes | Yes |
| Reconnection to an alternative PoP when the current PoP is unreachable | Yes | Yes (depends on third-party device behavior) | Yes |
| WAN traffic resiliency during PoP connectivity issues | Yes (WAN Recovery) | No | No |
| Internet traffic resiliency during PoP connectivity issues | Yes (Internet Recovery) | No | No |
| Alt WAN resiliency (MPLS) during PoP connectivity issues | Yes (Alt WAN Recovery) | No | No |
| Dependency on third-party device or provider behavior | No | Yes | Yes |

## Platform Behavior During Recovery

When traffic bypasses the PoP during Internet Recovery or WAN Recovery, certain platform services are not applied.

Operational considerations include:

1. Security inspection and Threat Prevention services are not applied to off-cloud traffic
2. PoP-based services are restored automatically when connectivity to the PoP is reestablished
