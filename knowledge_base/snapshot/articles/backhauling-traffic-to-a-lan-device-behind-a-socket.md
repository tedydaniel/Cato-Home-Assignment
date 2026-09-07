---
title: "Backhauling Traffic to a LAN Device behind a Socket"
slug: "backhauling-traffic-to-a-lan-device-behind-a-socket"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/backhauling-traffic-to-a-lan-device-behind-a-socket"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Backhauling Traffic to a LAN Device behind a Socket

This article discusses how to configure a Socket site as a backhauling gateway and create network rules to route traffic to a LAN device that is behind the Socket for that site.

## Overview

Cato's Internet traffic backhauling lets you use network rules to backhaul the relevant traffic to an on-premise appliance behind a backhauling gateway Socket site.

For more about Internet traffic backhauling with Cato, see [Configuring Internet Traffic Backhauling](/v1/docs/configuring-internet-traffic-backhauling).

### 

### Diagram of Internet Traffic Backhauling to a LAN Device

This section is an example of Internet traffic backhauling from sites and SDP users to the on-premise LAN device for the primary or secondary gateway site.

![Internet_Backhauling_Callouts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247959377181(1).png)

| Item | Name | Description |
| --- | --- | --- |
| 1 | Source sites | Sites defined as the source in the network rules that backhaul traffic to **data center 1** as the primary gateway site (item 2a) |
| 2a | Gateway site (data center 1) | Data center 1 is defined as a gateway site, and the backhauled Internet traffic is forwarded to the on-premise appliances for further processing. |
| 2b | Gateway site (data center 2) | Data center 2 is also defined as a gateway site, and the backhauled Internet traffic is forwarded to the on-premise appliances for further processing. |
| 3 | SDP users | SDP users defined as the source in the network rules that backhaul traffic to **data center 2** as the primary gateway site (item 2b) |

## Configuring Internet Backhauling for the Account

This section shows the overview of configuring your account to backhaul Internet traffic to a gateway site.

1. Define one or more backhauling gateway sites.
2. Create Internet network rules that backhaul Internet traffic to the gateway sites.

### Defining a Site as a Backhauling Gateway for a LAN Device

Define an existing Socket site as the backhauling gateway site where the Local gateway IP is the destination for the traffic. Make sure that this site meets the prerequisites above.

For each gateway site, enable the site as a backhauling gateway and then configure the destination as the **Local Gateway IP** of the site's LAN device, a firewall or layer-3 appliance. The Socket forwards the matching backhauled Internet traffic to the specified Local Gateway IP address.

Cato does not perform Source NAT for traffic that is backhauled to a LAN device. The traffic keeps the sender's original source IP address. Make sure that return routing is configured correctly to support symmetric traffic flows.

> [!NOTE]
> **Note:**
> 
> The Local Gateway IP must be within a configured network range for the gateway site.

![GatewaySite_LocalIP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247956219037(1).png)

**To define a site as a backhauling gateway for a LAN device:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Backhauling**.
3. Select **Use this site as backhauling gateway**.
4. In **Select the destination for the traffic**, select **Local gateway IP**.
5. Enter the **Local Gateway IP** for the LAN device.
6. Click **Save**.

### Configuring Network Rules to Backhaul Traffic to a LAN Device

Create an Internet network rule and configure the routing setting to route the traffic to the backhauling gateway. We recommend that you configure more than one backhauling gateway site, so in case the primary gateway site loses connectivity, the Cato PoP backhauls the traffic to the secondary gateway site (and so on if the secondary gateway site is also unreachable).

When you define a domain for the App/Category of a network rule, only the traffic for that specific domain is backhauled. Other related traffic flows for different domains aren't backhauled.

> [!NOTE]
> **Note:**
> 
> For users and sites located in China, make sure that the network rules for the backhauled traffic don't violate China's Internet regulations.

For more about the settings for network rules, see [Configuring Network Rules](/v1/docs/configuring-network-rules).

For more information about routing options, you can also [watch this video tutorial](https://academy.catonetworks.com/routing-options-in-the-cato-cloud).

**To configure a network rule to backhaul Internet traffic:**

1. From the navigation menu, click **Network > Network Rules**.
2. Click **New**. The **Add Network Rule** panel opens.
3. Expand the **General** section, and from the **Rule Type** drop-down menu select **Internet**.
4. Configure the other **General** settings.
5. Configure the **Source** and **App/Category** settings for the rule.
6. Expand the **Configuration** section, and if required, configure the **Bandwidth Management** and **Primary Transport** and **Secondary Transport** settings.
7. In the **Routing Method** section, configure the rule to route the Internet traffic to the Backhauling Gateway sites:

![Backhaul_RoutingMethod.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247939952925(1).png)
  1. In the **Route/NAT** drop-down menu, select **Backhaul via**.
  2. In **Backhauling Gateway sites**, click ![Domain_plus.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247931791517(1).png) and select the primary site.
  3. **(Optional)** Repeat the previous step for one or more backup sites.

The order of the **Backhauling Gateway sites**, defines the priority for the sites. The first site is the primary gateway site, the second site is the secondary gateway site, and so on.
8. Click **Apply**, and then click **Save**.
