---
title: "Recovering Connectivity with Alt. WAN Links"
slug: "recovering-connectivity-with-alt-wan-links"
updated: 2026-08-18T12:53:00Z
published: 2026-08-18T12:53:00Z
canonical: "knowledge.catonetworks.com/recovering-connectivity-with-alt-wan-links"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Recovering Connectivity with Alt. WAN Links

> [!NOTE]
> Note:
> 
> This feature is only available for a limited release. For more information, contact your Cato Networks support.

## Overview of Recovery via Alt. WAN

To improve the resiliency of your network, the Recovery via Alt. WAN feature provides support if there are connectivity problems in the Cato Cloud. This feature automatically sends traffic over the Alt. WAN links for a Socket site to recover connectivity. The destination Socket then sends the traffic to the Cato Cloud. When the original Socket re-establishes connectivity to the Cato Cloud, it automatically resumes regular operation.

You can configure the site to send WAN or Internet traffic over the Alt. WAN links during recovery. In addition, you can select a priority threshold for traffic that is recovered.

All traffic that is not configured for recovery is dropped. For example, if you configure to recover only WAN traffic, then all Internet traffic for the original site is dropped.

This is the average time that it takes for the recovery mechanism to start sending traffic over the Alt. WAN link:

- Single Socket site: 30 seconds
- ​High Availability (HA) Socket site: 40 seconds

### WAN Traffic Behavior During Recovery

During network recovery, the destination Socket sends the traffic to the Cato Cloud. However, if WAN traffic is intended for the destination Socket, then it bypasses the Cato Cloud, and these are the changes to the traffic:

- The WAN firewall is not applied to the traffic
- The Threat Protection services are not applied to the traffic
- The Cato Management Application does not analyze data for connectivity and does not generate alerts for network health or quality

When connectivity is restored, these changes are no longer relevant.

## Configuring Recovery via Alt. WAN for a Site

You can configure each Socket site to use the Alt. WAN links to recover connectivity for Internet and WAN traffic. If you choose to select a traffic priority for recovery, configure the lowest priority traffic that is recovered. For example, if you select P20, then traffic that is a lower priority (such as P30) is not recovered over the Alt. WAN link.

When you select which recovery **Method** the site uses, these are the options:

- **Auto** - Automatically chooses the destination site based on the lowest site-to-site latency.
- **Specific Site** - Assign the sites that will recover the traffic using Alt. WAN links. When there are multiple sites configured for Alt. WAN recovery, the site that is physically closest to the original site is used. For example, if site A is in recovery and site B has a 500 kilometers distance from site A, and site C is 1000 kilometers away- then site B is used for the Alt. WAN recovery.

**To configure Alt. WAN Recovery for a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Recovery via Alt. WAN**.

![360003283818-RecoverAltWAN.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248178673181.png)
3. Select the options to **Enable recovery for WAN traffic**, for Internet traffic, or for both.
4. For the WAN and Internet traffic, configure the traffic that is recovered over the Alt. WAN links:
  - **All traffic**
  - **Selected traffic** -from the **Lowest traffic priority for recovery** drop-down menu, select the lowest priority traffic that is recovered.
5. In **Method**, select **Auto** or **Specific Site** to define the destination sites for the traffic.
6. For **Specific Site**, click ![Add_Icon_CMA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248148934429.png) and select the destination sites that are used for Alt. WAN recovery.
7. Click **Save**.

## Limitations

- Recovery via Alt. WAN is supported from Socket version 6.1 and higher
- Sites that are connected to BGP peers can't be recovered by Alt. WAN links
- Accounts that use Static Range Translation can't be recovered by Alt. WAN links
- During recovery, the **Network Topology** window shows sites as disconnected
- During recovery, QoS and PBR rules are not applied to the traffic
