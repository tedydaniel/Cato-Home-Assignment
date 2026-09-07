---
title: "Understanding Acceptable and Unacceptable SLA for Sites"
slug: "understanding-acceptable-and-unacceptable-sla-for-sites"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/understanding-acceptable-and-unacceptable-sla-for-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding Acceptable and Unacceptable SLA for Sites

## Overview

The Cato connectivity SLA for the last mile assures optimal performance and resiliency for the site application flows. The Socket and the connected PoP use real-time SLA based path selection algorithms to select the optimal link for each flow in the upstream and downstream directions. The algorithm constantly monitors SLA KPIs such as packet loss, latency, congestion, port status, Internet connectivity status, and the Socket can seamlessly move flows between links if SLA degradation is detected.

Link performance is classified as either acceptable or unacceptable based on the thresholds for packet loss, latency, and other metrics. This classification determines when the Socket uses the active WAN link, activates a backup link, or initiates a connection to a different PoP. Understanding how the Socket reacts to SLA degradation is essential for ensuring reliable application delivery.

The Socket optimally distributes traffic between all active links, including links with different bandwidth capacities and asymmetric upstream/downstream bandwidth. The Socket's connectivity SLA mechanism is programmed to react to any connectivity problem and take actions to automatically overcome the issue. In situations where the connectivity SLA becomes unacceptable and it can't meet the thresholds, the Socket and the PoP take action to repair the connectivity. For example, the Socket activates the passive links. If these actions don't solve the connectivity problem, the Socket will connect to a different PoP.

We recommend using the active/active configuration for Socket sites for the best resiliency and performance. For more information, see [Cato Socket Link SLA Architecture](/v1/docs/cato-socket-link-sla-architecture).

### Customizing SLA Thresholds for Active/Passive Sites

The [Connection SLA page](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites) lets you define acceptable and unacceptable SLA thresholds that are applied to Socket sites in active/passive deployments.

When there is an unacceptable SLA for the primary link in a site, the Socket activates the secondary passive link and sends traffic over it to the PoP. When the primary link returns to an acceptable SLA, the Socket moves the flows back to the primary link, and the secondary link is deactivated.

### Customizing SLA Thresholds for Active/Active Sites

The [Connection SLA page](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites) also lets you define acceptable and unacceptable SLA thresholds for active/active deployments. For more information on traffic distribution and configuring custom thresholds for active/active sites, see [Configuring the Connection SLA Settings for Active/Active Socket Sites](/v1/docs/configuring-the-connection-sla-settings-for-active-active-socket-sites).

## Operating within Acceptable SLA

Within the acceptable SLA, the Socket uses all the active links and selects the best link for each new flow based on a health score that is calculated in real time. These SLA KPI metrics include: packet loss, latency, jitter, congestion, and more. For more information, see [Part 1: The Socket Interfaces and Precedence](/v1/docs/part-1-the-socket-interfaces-and-precedence).

For active/passive configurations, the passive links remain inactive as long as there is at least one active link with an acceptable SLA.

### Example of Packet Loss within Acceptable SLA

The following examples show Socket site configurations where the unacceptable SLA threshold is set to 10% packet loss. Link 1 is experiencing 3% packet loss, and link 2 has 0% packet loss.

| ![AA_Good_SLA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35398744071453.png) - For new flows, the Socket or PoP chooses the link with the best quality In the example above, new flows would open on link 2 with 0% packet loss | ![AP_Good_SLA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35398744116125.png) - Link 2 (the passive link) is not activated because link 1 meets the acceptable SLA threshold. All flows continue to use the active link. |
| --- | --- |

## Operating with Unacceptable SLA

When the Socket determines that all active links don't meet the SLA over the time range, this is considered an unacceptable SLA, and the Socket automatically takes actions to remediate the connectivity issues. Depending on the link configuration and Connection SLA settings, the Socket will activate a lower-precedence passive link, or if none of the links meet the acceptable SLA thresholds, it connects all links to a different PoP.

### Example of Remedy Actions for Unacceptable SLA

The following examples show Socket site configurations where the unacceptable SLA threshold is set to 10% packet loss. Link 1 is experiencing 15% packet loss and link 2 has 0% packet loss. These examples are during the evaluation period where the PoP is using self-healing mechanisms.

| ![AA_Bad_Link.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35398777743005.png) - For new flows, the Socket or PoP chooses the link with the best quality - For existing flows, the [Socket gradually moves flows](/v1/docs/part-1-the-socket-interfaces-and-precedence) to the best quality link In the example above, flows would move to link 2 with 0% packet loss | ![AP_Bad_Link.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35398728907293.png) - The passive link (link 2) is activated - Socket now works in active/active configuration - New flows use link 2 - Existing flows gradually move from link 1 to link 2 - For configurations where link 2 is a [Last-Resort link](/v1/docs/configuring-a-last-resort-link), the Grace-timer starts counting The Grace-time gives extra time to resolve connectivity issues before activating the cellular link - If an acceptable SLA isn't restored on link 1 during the grace time, then link 2 (the Last-Resort link) is activated |
| --- | --- |

### Example of Connecting to a Different PoP for Unacceptable Connectivity SLA

If the remedy actions during the evaluation period don't resolve the connectivity issues, then the Socket connects to a different PoP. For example, if there is an issue with the tier-1 cloud provider for the PoP location.

When a Socket connects to a new PoP, this is the behavior:

1. The Socket starts the initial connectivity SLA evaluation period of up to 40 - 50 seconds.

The SLA evaluation period is 40 seconds, and it is checked every 10 seconds, this means that the total time of the evaluation period is between 40 - 50 seconds.
  1. If the links to the PoP have an acceptable SLA, the Socket remains connected to the PoP.
  2. If the links to the PoP have unacceptable SLA, the Socket connects to a different PoP and repeats the initial connectivity SLA evaluation period of up to 40 - 50 seconds.
2. If the Socket can't locate a PoP with an acceptable SLA, it returns and connects to the original PoP.

The following examples show Socket site configurations where the unacceptable SLA threshold is set to 10% packet loss. Link 1 is experiencing 20% packet loss, and link 2 has 15% packet loss as a result of tier-1 provider connectivity issues. The second diagram shows how connecting to a different PoP resolves the issue. The behavior is the same for active/active and active/passive site deployments.

| ![T1_Bad_SLA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35398760976669.png) - After the evaluation period, there is unacceptable SLA (more than 10% packet loss) on all active links For example, packet loss related to the tier-1 service provider | ![T1_Good_SLA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35398752872477.png) - Socket connects to the next best PoP - After 40 - 50 seconds, the Socket confirms that the links meet the acceptable SLA - A reconnect event is generated |
| --- | --- |

## Reconnecting to the Original PoP

For optimal performance and lowest latency, it is always recommended that the Socket connects to the nearest physical PoP location. If the Socket moves to a different PoP location, due to SLA issues with the primary PoP, it will automatically attempt to reconnect to the preferred PoP location (the nearest PoP to the site) in 60 minutes. The Socket will verify that the preferred PoP is available and provides good service before reconnecting to it. You can also choose to manually reconnect the Socket to the preferred PoP, see [Defining a Preferred PoP for a Site](/v1/docs/defining-a-preferred-pop-for-a-site).
