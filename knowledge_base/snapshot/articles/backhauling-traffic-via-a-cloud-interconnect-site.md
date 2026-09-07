---
title: "Backhauling Traffic via a Cloud Interconnect Site"
slug: "backhauling-traffic-via-a-cloud-interconnect-site"
updated: 2026-06-28T09:16:04Z
published: 2026-06-28T09:16:04Z
canonical: "knowledge.catonetworks.com/backhauling-traffic-via-a-cloud-interconnect-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Backhauling Traffic via a Cloud Interconnect Site

## Overview

Cato lets you backhaul Internet traffic to a third-party cloud or proxy-based security service through a Cloud Interconnect site. Use network rules to select the relevant traffic and route it over the private Cloud Interconnect connection to the backhauling gateway site.

For more about Internet traffic backhauling with Cato, see [Configuring Internet Traffic Backhauling](/v1/docs/configuring-internet-traffic-backhauling).

### Resiliency for Cloud Interconnect Backhauling

Each Cloud Interconnect backhauling gateway uses two BGP sessions for resiliency. If the primary BGP peer is disconnected, the Cato PoP routes traffic over the secondary path. When the primary peer restores connectivity, the PoP routes traffic through the primary peer again.

If a network rule includes multiple backhauling gateways, the PoP fails over to the next gateway only when both BGP peers for the first gateway are disconnected. If all configured gateways are disconnected, the traffic egresses directly from the Cato PoP to the Internet. When connectivity is restored for any gateway site, the PoP resumes routing traffic through that site.

## Configuring Internet Backhauling for the Account

This section shows the overview of configuring your account to backhaul Internet traffic to a gateway site.

1. Define one or more backhauling gateway sites.
2. Create Internet network rules that backhaul Internet traffic to the gateway sites.

### Defining a Cloud Interconnect Site as a Backhauling Gateway

Define an existing Cloud Interconnect site as the backhauling gateway site.

For each gateway site, enable the site as a backhauling gateway. The PoP in the Cato Cloud forwards matching backhauled Internet traffic to the remote end through the Cloud Interconnect connection.

![Backhauling Cloud Interconnect.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36656714236957.png)

**To define a site as a backhauling gateway:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Backhauling**.
3. Select **Use this site as backhauling gateway**.
4. Click **Save**.

### Configuring Network Rules to Backhaul Traffic to a Cloud Interconnect Site

Create an Internet network rule and configure the routing setting to route the traffic to the backhauling gateway. We recommend that you configure more than one backhauling gateway site, so in case the primary gateway site loses connectivity, the Cato PoP backhauls the traffic to the secondary gateway site (and so on if the secondary gateway site is also unreachable).

For network rules that use the **Backhaul via** option, you can use a combination of different types of backhauling gateway sites in a single rule.

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

![Backhauling Cloud Interconnect -Network Rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36657322371357.png)
  1. In the **Route/NAT** drop-down menu, select **Backhaul via**. **Note:** The **Backhaul hairpinning** option is not supported for Cloud Interconnect sites.
  2. In **Backhauling Gateway sites**, select the primary site.
  3. **(Optional)** Repeat the previous step for one or more backup sites.

The order of the **Backhauling Gateway sites** defines the priority for the sites. The first site is the primary gateway site, the second site is the secondary gateway site, and so on.
8. Click **Apply**, and then click **Save**.
