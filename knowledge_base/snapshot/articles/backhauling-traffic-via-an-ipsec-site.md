---
title: "Backhauling Traffic via an IPsec Site"
slug: "backhauling-traffic-via-an-ipsec-site"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/backhauling-traffic-via-an-ipsec-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Backhauling Traffic via an IPsec Site

This article discusses how to configure an IPsec site as a backhauling gateway and create network rules to route traffic to third-party cloud/proxy based security service.

## Overview

Cato's Internet traffic backhauling lets you use network rules to backhaul the relevant traffic to a third-party cloud/proxy based security service via the IPsec VPN tunnel.

For more about Internet traffic backhauling with Cato, see [Configuring Internet Traffic Backhauling](/v1/docs/configuring-internet-traffic-backhauling).

### Diagram of Internet Traffic Backhauling via an IPsec Site

This is an example of Internet traffic backhauling from sites and SDP users to the the primary or secondary gateway IPsec site.

![IPsec_GW_site.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247940486173(1).png)

## Configuring Internet Backhauling for the Account

This section shows the overview of configuring your account to backhaul Internet traffic to a gateway site.

1. Define one or more backhauling gateway sites.
2. Create Internet network rules that backhaul Internet traffic to the gateway sites.

### Defining an IPsec Site as a Backhauling Gateway

Define an existing IPsec site as the backhauling gateway site.

For each gateway site, enable the site as a backhauling gateway. The PoP in the Cato Cloud forwards the matching backhauled Internet traffic via the IPsec tunnel to the remote end.

![IPsec_Backhauling_Enabled.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247942620061(1).png)

**To define a site as a backhauling gateway:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Backhauling**.
3. Select **Use this site as backhauling gateway**.
4. Click **Save**.

### Configuring Network Rules to Backhaul Traffic to an IPsec Site

Create an Internet network rule and configure the routing setting to route the traffic to the backhauling gateway. We recommend that you configure more than one backhauling gateway site, so in case the primary gateway site loses connectivity, the Cato PoP backhauls the traffic to the secondary gateway site (and so on if the secondary gateway site is also unreachable).

For network rules that use the **Backhaul via** option, you can use a combination of Socket and IPsec backhauling gateway sites in a single rule.

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

![backhauling.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36368124159261.png)
  1. In the **Route/NAT** drop-down menu, select **Backhaul via**.
  2. In **Backhauling Gateway sites**, select the primary site.
  3. **(Optional)** Repeat the previous step for one or more backup sites.

The order of the **Backhauling Gateway sites**, defines the priority for the sites. The first site is the primary gateway site, the second site is the secondary gateway site, and so on.
8. Click **Apply**, and then click **Save**.
