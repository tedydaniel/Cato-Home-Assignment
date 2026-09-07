---
title: "Enhanced X1600 Socket Wi-Fi Capabilities (EA)"
slug: "enhanced-x1600-socket-wi-fi-capabilities-ea"
updated: 2026-08-17T08:47:29Z
published: 2026-08-17T08:47:29Z
canonical: "knowledge.catonetworks.com/enhanced-x1600-socket-wi-fi-capabilities-ea"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Enhanced X1600 Socket Wi-Fi Capabilities (EA)

This article describes the enhanced Wi-Fi capabilities for X1600 and X1600 5G Sockets with integrated Wi-Fi.

**Note:** This is an Early Availability (EA) feature that is only available for limited release. For more information, contact your Cato Networks representative or send an email to [ea@catonetworks.com](mailto:ea@catonetworks.com).

## Overview

X1600 and X1600 5G Sockets with integrated Wi-Fi provide secure wireless access directly from the Socket, without deploying a separate wireless access point The features described in this article give you more control over how Wi-Fi is configured, segmented, and monitored from the Cato Management Application (CMA).

You can configure radio settings for each Wi-Fi band, create Internet-only SSIDs for guest access, and view historical Wi-Fi analytics to help identify congestion and capacity trends. These capabilities help admins operate branch Wi-Fi with better control, security, and visibility.

### Prerequisites

- Socket version 27 or higher

## Configuring Wi-Fi Radio Settings

You can configure the radio settings for each Wi-Fi band on the X1600 Socket. This lets you adjust the wireless configuration for the physical environment, client density, and available spectrum at the site.

For each band, you can configure these settings:

- Wi-Fi standard
- Channel width
- Channel
- DFS frequency usage for the 5 GHz band

Wider channels can provide higher throughput, but they can also increase the chance of interference in congested environments. Narrower channels can be useful in high-density areas where many access points or wireless networks are operating nearby.

Dynamic Frequency Selection (DFS) lets the 5 GHz band use additional channels that may have less interference. When DFS is enabled, the Socket only uses supported DFS channels that are valid for the site location.

The available radio settings are based on the site country. The CMA only shows channel and channel-width combinations that are supported for the site location, helping prevent invalid radio configurations.

**Note:** When you move a radio to a DFS channel, the Socket performs a Channel Availability Check (CAC) before using the channel. During this process, Wi-Fi clients on that band may experience a brief interruption.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Wi-Fi radio settings.png)

**To configure Wi-Fi radio settings:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. In the **Socket & Wi-Fi Radio Configuration** section, configure the settings for each Wi-Fi band.
  - For the 2.4 GHz band, configure the radio settings.
  - For the 5 GHz band, configure the radio settings and select whether to use DFS frequencies.
4. Click **Save**. The Wi-Fi settings are applied to the Socket.

## Configuring an Internet-Only SSID for Guest Access

You can configure a Wi-Fi SSID as Internet-only to provide guest access from the X1600 Socket. Devices connected to an Internet-only SSID can access the Internet, but can’t access private site resources, LAN networks, or WAN destinations.

This lets you provide guest Wi-Fi without creating separate firewall rules to block access to internal resources. Guest traffic is still sent through the Cato security stack, so security services configured for the account can inspect and enforce policy on the traffic.

Internet-only SSIDs are useful for:

- Guest networks
- Contractor access
- Networks that should be isolated from private resources

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Wi-fi guest internet only.png)

**To configure a Guest Wi-Fi (Internet-only) SSID:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. In the ports table, under **Default Ports**, click one of the Wi-Fi interfaces (labeled WBR1-WBR4).

The **Edit SSID** panel opens.
4. In the **SSID Setup** section, enable the guest Wi-Fi option.
5. Configure the remaining SSID settings.
6. Click **Apply**.
7. Click **Save**. The Wi-Fi settings are applied to the Socket.

## Viewing Historical Wi-Fi Analytics

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Wi-Fi Network Analytics.png)

You can use the Network Analytics page to view historical Wi-Fi metrics for X1600 Socket Wi-Fi networks.

Historical Wi-Fi analytics can help you:

- Identify channel utilization trends
- Understand usage patterns for the 2.4 GHz and 5 GHz bands
- Track connected device counts over time
- Plan capacity changes for sites with increasing wireless usage

The Network Analytics page shows the following metrics for each band:

- **Channel Utilization** - Shows how much of the available airtime is used on the selected Wi-Fi band over time. Use this metric to identify congestion, interference, or periods when the band is heavily used
- **Connected devices** - Shows the number of devices connected to the selected Wi-Fi band over time. Use this metric to understand client distribution between bands and identify usage trends for capacity planning

**To view historical Wi-Fi analytics:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Monitoring Pages > Network Analytics**.
3. Click the **Wi-Fi** tab. The page shows **Channel Utilization** and **Connected Devices** for the Wi-Fi bands.
