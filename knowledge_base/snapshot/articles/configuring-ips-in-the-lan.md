---
title: "Configuring IPS in the LAN"
slug: "configuring-ips-in-the-lan"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/configuring-ips-in-the-lan"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring IPS in the LAN

## Overview

Cato’s IPS Protection in the LAN extends Cato’s advanced threat prevention capabilities into local network traffic, defending east-west traffic against known and emerging attack vectors. The IPS engine runs locally on the Socket, and not in the PoP, which periodically receives signature and threat intelligence updates. After updates are downloaded, inspection and enforcement occur locally on the Socket. This ensures:

- Continuous protection even without connectivity to the PoP or Internet
- Inspection during WAN outages, so local traffic remains enforced at all times
- Lower latency, because LAN traffic does not need to traverse the PoP for inspection
- Reduced WAN bandwidth usage, by avoiding unnecessary backhaul of local traffic

LAN IPS enforcement is controlled granularly through LAN Firewall Network rules. You can define which traffic is inspected and at which sites. Only traffic that matches the configured LAN Firewall rules is inspected by IPS. This provides precise control over enforcement scope and allows you to align inspection with your security and performance requirements. When threats are detected, the IPS takes action based on Firewall policy settings, blocking malicious traffic or generating events for visibility and investigation. Properly configured IPS enhances on-premises security posture without the need for additional appliances.

### Prerequisites

- Supported from Socket version 26 and higher
- IPS protection is enabled. For more information about IPS protection, see [Configuring the IPS Policy](/v1/docs/configuring-the-ips-policy).
- We recommend that you enable TLS inspection so that the IPS service provides the maximum protection for your network.

## Configuring IPS Protection in the LAN

To configure LAN IPS protection, you need to:

1. Enable LAN IPS Protection Scope in the IPS policy
2. Define which traffic is inspected by the Socket LAN IPS engine using LAN Firewall rules

### Step 1: Enabling LAN IPS Protection

In the IPS policy, enable the Socket LAN Protection Scope and configure the relevant settings.

![LAN_IPS.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34309563162909.png)

**To enable LAN IPS Protection:**

1. From the navigation menu, click **Security > IPS**.
2. Click on **Socket LAN**

The **Edit** panel opens.
3. Click the slider to enable (green), and configure the required **Action** and **Track** settings.
4. Click **Apply**, and then click **Save**.

Socket LAN IPS is enabled for the account, but is not enforced unless a LAN Firewall is configured.

#### Understanding the IPS Protection Actions

You can define the **Actions** triggered by LAN IPS and set their alerts. These are the available actions:

- **Block** - Blocks the malicious traffic from reaching its destination. When applicable, the user is redirected to a dedicated block web page.
- **Monitor** - Generates events (shown in Home &gt; Events) for the malicious traffic. The traffic then continues to the destination.

### Step 2: Define which traffic is inspected by the Socket LAN IPS engine using LAN Firewall rules

To define which sites enforce IPS protection, include it in a Network LAN Firewall rules. On the **IPS** page, the link in the **Applied To** column for the **Socket LAN** displays how many LAN Firewall rules currently use LAN IPS, out of the total number of network rules.

![Network_rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34309581618973.png)

**To define traffic for IPS inspection using a LAN Firewall rule:**

1. From the navigation menu, click **Security > LAN Firewall**.
2. Edit the rule you want to add LAN IPS protection to.
3. In the **Security** section, check the **Application Awareness** and **LAN IPS** checkboxes.
4. Click **Save** and then **Publish**.
