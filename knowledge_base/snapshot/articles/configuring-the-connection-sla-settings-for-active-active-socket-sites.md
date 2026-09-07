---
title: "Configuring the Connection SLA Settings for Active/Active Socket Sites"
slug: "configuring-the-connection-sla-settings-for-active-active-socket-sites"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/configuring-the-connection-sla-settings-for-active-active-socket-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring the Connection SLA Settings for Active/Active Socket Sites

This article explains Connection SLA behavior for active/active Socket sites and how to customize the SLA thresholds.

## Overview

Connection SLA thresholds determine when a WAN link is considered healthy or degraded and how the Socket responds to changing network conditions. You can customize these thresholds for active/active Socket sites to control how traffic is distributed across multiple WAN links based on link health and performance. This gives you control over link selection for load balancing, traffic stability, and failover behavior, while still benefiting from Cato’s real-time path selection and self-healing mechanisms.

By default, active/active sites use Cato’s built-in SLA logic. You can optionally customize these settings at the account level or for specific sites.

### Prerequisites

- Supported from Socket version 25 and higher

## How Traffic Distribution Works for Active/Active Sites (Default Behavior)

For active/active Socket sites, traffic is distributed across WAN links based on real-time link health, link preference, and the relative bandwidth configured for each link. Traffic distribution is flow-based rather than packet-based, which means all packets belonging to the same flow use the same WAN link.

A flow is a conversation between a client and a server where all packets share the same 5-tuple:

- Source IP address
- Source port
- Protocol
- Destination IP address
- Destination port

For example, when a client sends traffic to a mail server, a single flow is created and assigned to one WAN link for the lifetime of that flow.

### Link Health Evaluation

Every second, Cato evaluates the health of each active WAN link. Each link receives a quality score based on health metrics that include:

- Packet loss
- Jitter
- Latency

By default, the minimal acceptable link quality metrics are:

- Packet loss: 3%
- Jitter: 30 ms
- Latency: 600 ms

For new flows when both links are within acceptable SLA, the Socket prefers the link with the best quality score. For example, if Link 1 has packet loss and jitter and Link 2 does not, the Socket is more likely to use Link 2 for new flows because Link 2 has a better quality score.

If a WAN link has no Internet connectivity, it is not selected for traffic distribution.

If a link exceeds one or more of the defined thresholds, it is considered degraded and is less likely to be selected for new flows.

Cato continuously monitors the health of a link carrying existing flows. If the link remains within acceptable SLA, traffic continues uninterrupted. If the link becomes unhealthy and crosses unacceptable SLA thresholds, the Socket selects a better link and moves traffic accordingly.

### Preferred Interfaces and Bandwidth Ratios

If a network rule defines a preferred interface, that preference is applied as long as the link meets the SLA requirements. If there is no preferred interface (automatic role), the Socket distributes traffic based on the configured active/active bandwidth ratios.

![Connection_SLA_Active_Active_interface_role.png](https://support.catonetworks.com/hc/article_attachments/35315910426653)

In the example below, the WAN1 link is configured with a bandwidth of 100 Mbps down/up, and the WAN2 link is configured with 20 Mbps down/up.

![Active-Active_Socket.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35315938080541(1).png)

The bandwidth ratio between WAN1 and WAN2 is 5:1. In this case, approximately five new flows are assigned to WAN1 for every one flow assigned to WAN2, assuming both links meet the SLA requirements.

The Socket and the connected PoP share responsibility for traffic distribution:

- The Socket considers upstream bandwidth, because it controls traffic sent from the site to the PoP
- The PoP considers downstream bandwidth, because it controls traffic sent from the PoP to the site

### Failover Behavior

If one WAN link goes down, traffic belonging to flows assigned to that link is redirected to the remaining active link. Existing flows are preserved, although connection-sensitive applications (such as voice or video) may experience a brief disruption during the transition.

## Customizing the Connection SLA Settings for Active/Active Sites

You can customize the Connection SLA thresholds for active/active Socket sites to control how quickly a link is considered degraded and how traffic is redistributed during suboptimal conditions. The Socket continuously evaluates each link against the configured SLA thresholds. If a WAN link does not meet the SLA thresholds, the Socket considers the link unacceptable and reduces its participation in traffic distribution.

If all active links for a site fail to meet the SLA thresholds, the SLA is ignored and traffic distribution continues across the available links.

The Connection SLA settings let you adjust the following thresholds:

- Jitter
- Packet loss
- Latency

### Scope of SLA Settings

You can define Connection SLA settings at two levels:

- Account level – Applies to all active/active Socket sites in the account
- Site level – Overrides the account settings for a specific site

### Temporary Link Exclusion

You can optionally configure the Socket to temporarily exclude a WAN link from traffic selection when SLA thresholds are breached. When this option is enabled, a link is excluded from traffic selection for a specified number of seconds if any single SLA sample, within a 4-second window, exceeds one of the configured thresholds. During this exclusion period, new flows are not assigned to the degraded link. After the exclusion timer expires, the Socket reevaluates the link and returns it to traffic selection if it meets the SLA thresholds.

### Considerations When Customizing SLA Thresholds

Configuring overly aggressive SLA thresholds can cause frequent traffic shifts between WAN links. For example, setting very low packet loss thresholds can result in constant rebalancing of flows, which may reset application sessions and impact user experience.

Cato recommends using conservative values unless you have a specific use case that requires higher sensitivity.

![Active_Active_Connection_SLA_config.png](https://support.catonetworks.com/hc/article_attachments/35315949439389)

**To customize the Connection SLA settings for active/active sites:**

1. To customize SLA settings:
  - On the account level:
    - From the navigation menu, click **Network > Connection SLA**.
  - For a specific site:
    - From the navigation menu, click **Network >Sites** and select the site.
    - From the navigation menu, click **Network > Connection SLA**.
2. Expand the **Active-Active SLA Thresholds** section.
3. Select **Use custom SLA thresholds for Packet Loss, Latency and Jitter**.
4. Configure the SLA threshold values for the WAN links:
  - **Jitter** – Enter the maximum acceptable jitter value in milliseconds.
  - **Packet Loss** – Enter the maximum acceptable packet loss percentage.
  - **Average Latency** – Enter the maximum acceptable latency value in milliseconds.
5. (Optional) Configure temporary link exclusion.
6. Click **Save**.
