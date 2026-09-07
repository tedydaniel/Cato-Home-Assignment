---
title: "Backhauling Traffic via a Socket's WAN Interface IP Address"
slug: "backhauling-traffic-via-a-socket-s-wan-interface-ip-address"
updated: 2026-07-06T14:02:02Z
published: 2026-07-06T14:02:02Z
canonical: "knowledge.catonetworks.com/backhauling-traffic-via-a-socket-s-wan-interface-ip-address"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Backhauling Traffic via a Socket's WAN Interface IP Address

> [!NOTE]
> Note:
> 
> Cato account licenses use one of two models. This article applies to the Enforcement Model only and is not relevant to the [Bursting Model](https://knowledge.catonetworks.com/docs/jan-2027-license-bursting-model) (starting in January 2027). Not sure which license model your account uses? See [Identifying your License Model](https://knowledge.catonetworks.com/docs/identifying-your-license-model).

## Overview

In some scenarios, such as migrating to Cato, you may want to keep using an existing public IP address to access specific Internet applications. For example, the IP address is allowlisted in various SaaS applications, and you are not ready to change it yet. You can configure a gateway site to egress the backhauled traffic directly to the Internet from the Socket WAN interface. In this case, the Socket performs source NAT on the traffic to the WAN interface IP address.

Each backhauling gateway site can be configured for one of the following destinations:

- [Local gateway IP](/v1/docs/backhauling-traffic-to-a-lan-device-behind-a-socket) - Sends the backhauled traffic to a LAN device
- Internet breakout - Egresses the backhauled traffic via the Socket WAN interface

### Prerequisites for Internet Traffic Backhauling

- The backhauling gateway site must be Socket version 16.0 or higher
  - There is no minimum Socket version for the source sites

### Diagram of Internet Traffic Backhauling via a Socket WAN IP Address

This is an example of Internet traffic backhauling from sites and SDP users, to egress to the Internet using the WAN interface IP address of the primary or secondary gateway site.

![InternetBreakoutDiagram.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247959650077.png)

## Configuring Internet Backhauling for the Account

This section shows the overview of configuring your account to backhaul Internet traffic to a gateway site.

1. Define one or more backhauling gateway sites.
2. Create Internet network rules that backhaul Internet traffic to the gateway sites.

### Defining a Site as a Backhauling Gateway for Internet Breakout

Define an existing Socket site as the backhauling gateway site where the Internet traffic is egressed using the IP address for the WAN Socket port. Make sure that this site meets the prerequisites above.

For each gateway site, enable the site as a backhauling gateway. Then set the destination as **Internet breakout** and select the **Socket WAN Port** that egresses the Internet traffic.

![GW_Internet_breakout.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247940171293.png)

**To define a site as a backhauling gateway for Internet breakout:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Backhauling**.
3. Select **Use this site as backhauling gateway**.
4. In **Select the destination for the traffic**, select **Internet breakout**.
5. Select the **Preferred Socket Port** for the Internet traffic.
6. Click **Save**.

#### Configuring Network Rules to Backhaul Traffic via a Socket WAN IP Address

Create an Internet network rule and configure the routing setting to route the traffic to the backhauling gateway. We recommend that you configure more than one backhauling gateway site, so in case the primary gateway site loses connectivity, the Cato PoP backhauls the traffic to the secondary gateway site (and so on if the secondary gateway site is also unreachable).

When you define a domain for the App/Category of a network rule, only the traffic for that specific domain is backhauled. Other related traffic flows for different domains aren't backhauled.

> [!NOTE]
> Note:
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

![Backhaul_RoutingMethod.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247908773149.png)
  1. In the **Route/NAT** drop-down menu, select **Backhaul via**.
  2. In **Backhauling Gateway sites**, click ![Domain_plus.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247959911453.png) and select the primary site.
  3. **(Optional)** Repeat the previous step for one or more backup sites.

The order of the **Backhauling Gateway sites**, defines the priority for the sites. The first site is the primary gateway site, the second site is the secondary gateway site, and so on.
8. Click **Apply**, and then click **Save**.
