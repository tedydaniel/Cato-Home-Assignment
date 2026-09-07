---
title: "Configuring the Connection SLA Settings for Active/Passive Socket Sites"
slug: "configuring-the-connection-sla-settings-for-active-passive-socket-sites"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/configuring-the-connection-sla-settings-for-active-passive-socket-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring the Connection SLA Settings for Active/Passive Socket Sites

This article discusses the SLA for Socket link connectivity for active/passive sites, and how to customize the settings for the account or specific sites. For more information, see [Understanding Acceptable and Unacceptable SLA for Sites](/v1/docs/understanding-acceptable-and-unacceptable-sla-for-sites).

## Overview

The Connection SLA page in the Cato Management Application lets you define custom acceptable and unacceptable SLA thresholds for active/passive Socket sites. When the connectivity SLA is within the acceptable SLA thresholds, the Socket remains connected to the same PoP and uses the real-time path-selection algorithms to select the best link for each new flow.

When there is unacceptable SLA for the primary link in a site, the Socket activates the secondary passive link and sends traffic over it to the PoP. When the primary link returns to acceptable SLA, the Socket moves the flows back to the primary link, and the secondary link is deactivated.

The Cato Cloud monitors the SLA thresholds inside the DTLS tunnel between the Socket and the PoP. Last-mile and ISP traffic to the Internet are not part of the site SLA.

The unacceptable SLA thresholds are defined for the account level and can also be customized for specific sites, see below [Customizing the SLA Thresholds Settings](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites#customizing-the-sla-thresholds-settings).

### Example of Unacceptable SLA

The following examples show Socket site configurations where the unacceptable SLA threshold is set to 10% packet loss. Link 1 is experiencing 15% packet loss and link 2 has 0% packet loss. These examples are during the evaluation period where the PoP is using self-healing mechanisms.

![AP_Bad_Link.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28022664833821.png)

- The passive link (link 2) is activated
- Socket now works in active/active configuration
- New flows use link 2
- Existing flows gradually move from link 1 to link 2
- For configurations where link 2 is a [Last-Resort link](/v1/docs/configuring-a-last-resort-link), the Grace-timer starts counting

The Grace-time gives extra time to resolve connectivity issues before activating the cellular link
  - If acceptable SLA isn't restored on link 1 during the Grace-time, then link 2 (the Last-Resort link) is activated

## Defining the Connectivity SLA Thresholds

There are two options to define the Connectivity SLA thresholds:

1. Cato Smart SLA - automatically set by Cato (this is the default option)
2. Custom SLA settings - customize the SLA thresholds for the entire account or specific sites

### Using Cato Smart SLA

The Cato Smart SLA option automatically sets the recommended SLA settings for the last-mile connectivity between the Socket and the PoP. This setting includes a 10-minute SLA evaluation period to decide if the existing connectivity to the PoP meets the default SLA requirements or not. If the SLA requirements are not met for 50% of the 10-minute period, the Socket automatically moves the tunnels to a different PoP to restore the connectivity SLA.

The goal of this 10-minute period is to allow the internal mechanisms in the PoP to identify and resolve the connectivity problem and to avoid moving the site to a different PoP. For example, the PoP automatically identifies a poor quality Tier-1 provider peer and temporarily removes it from the service. Then all traffic from the connected sites uses the remaining Tier-1 provider peers.

These are the default values for the connectivity SLA thresholds for the Cato Smart SLA option:

- Evaluation period - 10 min
- Packet loss - 10%
- Latency - 300 ms
- % of the time window - 50%

We recommend that you use the Cato Smart SLA option to define the Connection SLA thresholds for your account.

### Customizing the SLA Thresholds Settings

You can customize the SLA settings for active/passive sites to change the default evaluation period, packet loss, and latency SLA thresholds, as well as the percentage of the time window that the Packet Loss and Latency are over the thresholds. For example, the connection SLA with an **Evaluation period** of 600 seconds. In that time, you want to make sure that **Packet Loss** is no greater than 10% for more than 30% of that evaluation period, so you set the **% of the time window** to 30. When the active link has unacceptable SLA, the Socket activates the passive link and starts sending traffic over it.

You should be aware that if you configure the SLA settings to be too sensitive, for example, reducing the packet loss to 1% and setting the evaluation period to 20 sec, you can cause the site to frequently move to different PoPs. This can then cause application flows to reset and temporarily impact the user experience until the flows are re-established.

These are the default values for the custom SLA thresholds:

- Evaluation period - 130 sec
- Packet loss - 10%
- Latency - 300 ms
- % of the time window - 100%

You can define the Connection SLA setting as a global setting for the entire account, and different Link SLA settings for specific sites. The Link SLA for a specific site overrides the account settings.

Use the [Socket webUI](/v1/docs/accessing-the-socket-webui) to check the current Connection SLA Latency between the Socket and the PoP. In the **Tunnels > SLA Parameters** section the Latency is displayed in near real-time. The latency used in the Connection SLA calculation is the one-way latency and not the Round-Trip Time (RTT). The Distance graph in the [Network Analytics](/v1/docs/showing-the-site-network-analytics) page displays the Round-Trip Time. For an approximate analysis of historical latency, from the Distance graph, half the Distance (RTT) in milliseconds.

#### Customizing the SLA Thresholds for the Account

Use the Network > Connection SLA page to customize the SLA thresholds for the account, and these settings are applied to the active/passive Socket sites.

![connectionsla.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28022686224413.png)

**To customize the SLA Thresholds settings for the account:**

1. From the navigation menu, click **Network > Connection SLA**. The **Connection SLA** screen opens.
2. Expand the **SLA Thresholds** section.
3. Click **Use custom SLA thresholds for Packet Loss and Latency**.
4. Customize the evaluation period for the links, and enter the number of seconds that **A link is considered as an unacceptable SLA if any of the following thresholds is exceeded for**.
5. Customize the SLA threshold settings for the **Packet Loss** and **Average Latency**.
6. Determine what the **% of the time window** the **Packet Loss** and **Average Latency** should not exceed the SLA thresholds.
7. Click **Save**.

#### Customizing the SLA Thresholds for a Site

Use the Connection SLA page for a specific site to customize the SLA thresholds for that site, and override the account setting.

**To customize the SLA Thresholds for a specific site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Advanced Settings > Connection SLA**.
3. Expand the **SLA Thresholds** section.
4. Select **Override Account Settings**.
5. Customize the evaluation period for the links, and enter the number of seconds that **A link is considered as an unacceptable SLA if any of the following thresholds is exceeded for**.
6. Customize the SLA threshold settings for the **Packet Loss** and **Average Latency**.
7. Determine what the **% of the time window** the **Packet Loss** and **Average Latency** should not exceed the SLA thresholds.
8. Click **Save**.
