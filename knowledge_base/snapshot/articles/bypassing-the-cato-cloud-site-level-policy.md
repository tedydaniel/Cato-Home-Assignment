---
title: "Bypassing the Cato Cloud (Site Level Policy)"
slug: "bypassing-the-cato-cloud-site-level-policy"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/bypassing-the-cato-cloud-site-level-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bypassing the Cato Cloud (Site Level Policy)

This article discusses how to configure a site to bypass the Cato Cloud and egress traffic directly to the Internet.

## Overview

The **Bypass** page lets you define bypass rules for Internet traffic that will directly egress to the Internet instead of being routed to the Cato Cloud. The PoPs in the Cato Cloud don't inspect bypassed Internet traffic or apply security polices, in addition, app or category-based traffic rules are not applied. The Socket continues to apply Bandwidth Profiles and QoS to bypassed traffic in the upstream direction. QoS is not applied in the downstream direction because the PoPs are bypassed.

Bypassed Internet traffic is sent over a Socket WAN interface. An internal Socket mechanism generates a score for each WAN interface, which is calculated each second based on a set of parameters, such as packet loss, jitter, latency, and congestion.

The default behavior is for the Socket to automatically choose the WAN port for the bypass traffic based on the best score. The Socket can select different WAN ports for different flows.

> [!NOTE]
> Notes:
> 
> - Bypassing Internet traffic is only supported for Socket and vSocket sites.
> - Bypassed traffic is not included as site traffic for the site bandwidth license.

**Preferred Socket Port**

When **Preferred Socket Port** is enabled for a site, you can choose to assign a preferred [Socket WAN Role](/v1/docs/working-with-socket-sites) for a bypass rule that is used to egress the Internet traffic. With this option, if the WAN interfaces have a similar score, the Socket will use the designated WAN Role as the preferred WAN port for the bypass traffic, as long as it has Internet connectivity. If the preferred WAN Role loses connectivity, the Socket selects a different one for the traffic.

### Bypass Rules Based on Predefined Applications

To make it easier to configure application traffic in Socket sites to egress directly to the Internet, you can define rules using predefined applications that include all the relevant destination IP addresses for the application. Cato maintains these predefined applications so that when the application's IP addresses are updated, your policy automatically applies to the new IP addresses. For example, instead of having to configure and keep track of all the public IPs for Zoom, you can simply select the **Zoom** predefined application, and Cato ensures that the correct destinations are bypassed. These are the supported predefined applications:

- Microsoft Exchange
- Google Applications
- Microsoft Defender for Endpoint
- Zoom
- Skype and MS Teams
- SharePoint and OneDrive Business

![Bypass.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29650772588957.png)

## Defining Bypass Rules

Create bypass rules for destinations and/or sources and define the parameters for the source or destination. Destination bypass rules can be defined using applications and/or IP ranges and addresses. Source bypass rules are defined using an IP range or address.

![Bypass_App_Panel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29650787821981.png)

**To define a bypass rule for Internet traffic:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, click **Site Configuration > Bypass**.
3. For the **Destination** or **Source** rule, click **New**. The **New Bypass** panel opens.
4. Configure the settings for the bypass rule:
  - The **Name** of the new bypass rule
  - Define the source or destination, as follows:
    - For a Source rule - Define the source **IP** range or address for the rule
    - For a Destination rule - Define the **Application** and/or the **IP** ranges or addresses for the rule. You can configure multiple applications and IP ranges in the same Destination rule.
  - **(Optional)** The traffic protocols that are bypassed: TCP, UDP, ICMP. By default, all the protocols are bypassed.
5. **(Optional)** In **Preferred Socket Port**, select the WAN port that egresses traffic directly to the Internet.
6. Click **Save**.

## Customizing the Flow Timeout

For Socket and vSocket sites, the default flow timeout is 60 seconds. After this time, there is an idle timeout for the traffic flow and the Socket closes the bypassed flow.

You can use the Socket WebUI to customize the flow timeout. However this custom setting is not persistent and if the Socket reboots, including upgrading to a new version, then it reverts to the default flow timeout of 60 seconds. To permanently configure a custom flow timeout, please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).

**To customize the bypass flow timeout:**

1. Log in to the Socket WebUI:
  1. From the navigation menu, select **Network > Sites**, and select the site.
  2. From the navigation menu, select **Site Configuration > Socket**.
  3. From the **Actions** menu of the socket, select **Socket WebUI**.
2. From the **Cloud Connection Settings** tab, in the **Flow timeout (for bypass flows only)** section, enter the new timeout value.
3. Click **Update**.
