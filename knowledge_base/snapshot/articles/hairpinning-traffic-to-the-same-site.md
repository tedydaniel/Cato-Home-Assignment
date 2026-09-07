---
title: "Hairpinning Traffic to the Same Site"
slug: "hairpinning-traffic-to-the-same-site"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/hairpinning-traffic-to-the-same-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Hairpinning Traffic to the Same Site

This article discusses how to configure a site as a backhauling gateway and create network rules to send Internet traffic from the site to the PoP (for the Cato Security services) and then back to the same site for further processing.

## Overview

In some scenarios, it is necessary to send Internet traffic from the site to the PoP and then back to the same site for further processing. Some examples include:

- Migrating site from an on-premise security appliance to Cato. You can hairpin the traffic via the PoP to inspect the traffic with Cato security services, and then forward the traffic to the appliance. This way you can gradually migrate and adjust policies as required.
- Secured access to Internet applications using the fixed IP public addresses for a site. For example, IT personnel require secured access to a cloud-based console that is configured with an allowlist of public IPs. You can hairpin this specific traffic via the Cato PoP, for security inspection.

### Prerequisites for Internet Traffic Backhauling

- The backhauling gateway site must be Socket version 16.0 or higher
  - There is no minimum Socket version for the source sites

### Diagram of Internet Traffic Hairpinning to the Same Site

This is an example of hairpinning Internet traffic from a site to the PoP in the Cato Cloud and then back to the originating site for further processing. For example the hairpinned traffic is:

- Egressed directly to the Internet with direct NAT (gateway site is set to **Internet breakout**)
- Sent to a LAN device (gateway site is set to **Local gateway IP**)

![Hairpinning_diagram.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247955831709.png)

## Configuring Hairpinning for Sites in Your Account

This section explains the steps to configure hairpinning.

1. Define the gateway sites and the traffic destination.

To use a site for hairpinning, you need to configure the site as a backhauling gateway.
2. Create Internet network rules that hairpin Internet traffic from each site to the PoP and back to the site.

### Defining a Site as a Backhauling Gateway

Enable the site as a backhauling gateway and then set the traffic destination based on the requirements for your organization.

![GatewaySite_LocalIP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247931389725.png)

**To define a site as a backhauling gateway for hairpinning traffic:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Backhauling**.
3. Select **Use this site as backhauling gateway**.
  - To egress the traffic to the Internet, in **Select the destination for the traffic**, select **Internet breakout**, and select the **Preferred Socket Port** for the Internet traffic.
  - To send the traffic to a LAN device, in **Select the destination for the traffic**, select **Local gateway IP** and enter the **Local Gateway IP** for the LAN device.
4. Click **Save**.

### Configuring Network Rules to Hairpin Traffic to the Same Site

Create an Internet network rule and configure the routing setting to hairpin the traffic back to the originating site.

The network rule defines the sites and the traffic type for which hairpinning is applied. The site routes the traffic based on the traffic destination setting configured above in, [Defining a Site as a Backhauling Gateway](/v1/docs/hairpinning-traffic-to-the-same-site#defining-a-site-as-a-backhauling-gateway).

When you define a domain for the App/Category of a network rule, only the traffic for that specific domain is backhauled. Other related traffic flows for different domains aren't backhauled.

For more about the settings for network rules, see [Configuring Network Rules](/v1/docs/configuring-network-rules).

For more information about routing options, you can also [watch this video tutorial](https://academy.catonetworks.com/routing-options-in-the-cato-cloud).

**To configure a network rule to backhaul Internet traffic:**

1. From the navigation menu, click **Network > Network Rules**.
2. Click **New**. The **Add Network Rule** panel opens.
3. Expand the **General** section, and from the **Rule Type** drop-down menu select **Internet**.
4. Configure the other **General** settings.
5. Configure the **Source** and **App/Category** settings for the rule.
6. Expand the **Configuration** section, and if required, configure the **Bandwidth Management** and **Primary Transport** and **Secondary Transport** settings.
7. In the **Routing Method** section, configure the rule to hairpin traffic to the PoP and back to the same source site:

![Routing_Hairpinning.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247908162205.png)
  1. In the **Route/NAT** drop-down menu, select **Backhaul hairpinning**.

**Note:** Only Socket sites v16.0 or higher are supported for hairpinning network rules
8. Click **Apply**, and then click **Save**.
