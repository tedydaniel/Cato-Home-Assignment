---
title: "Exchanging Socket Ports"
slug: "exchanging-socket-ports"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/exchanging-socket-ports"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Exchanging Socket Ports

This article explains how to use the Cato Management Application to exchange the Socket port settings for your Cato site.

## Overview

You can exchange the port destination for your Socket sites in the Cato Management Application to meet changes and new requirements for a site. Exchange the physical Socket ports, after you save the settings, the new configuration is pushed to the Socket. There is no impact to existing site settings, such as BGP or LAN subnets, when you exchange Socket ports.

Exchanging ports is only supported for physical Socket models.

There are some scenarios where exchanging Socket ports is part of a hardware upgrade (such as changing Socket model X1500 to X1700), cable receiver change (for example, copper to fiber cable) or other hardware changes.

For more on Socket hardware changes, see [Changing the Socket model for a site](/v1/docs/how-to-change-the-socket-model-for-a-site).

**Notes:**

- You can't exchange the primary WAN port destination (Port 3 / WAN 1 on the X1500 model or Port 1 on the X1600 and X1700 models)
- USB ports used for the Cato destination (WAN traffic) support up to 25Mbps only
- For AWS and Azure vSockets, only one LAN port is supported

The following table describes the port destinations:

| Item | Description |
| --- | --- |
| Cato | Connected to the Cato Cloud for WAN traffic |
| LAN | LAN traffic |
| LAN & VRRP | LAN traffic and HA keepalive traffic |
| LAN LAG Master & VRRP | LAN LAG traffic and HA keepalive traffic |
| LAN LAG Master | The logical master LAG port |
| LAN LAG Member | The logical member LAG port(s) |
| Alternative WAN | MPLS network with Socket sites on different subnets |
| Alternative WAN (Layer-2) | MPLS network with Socket sites on the same subnet |
| Disabled | Port is disabled |

## Socket Ports Destinations for the X1500 Socket

The X1500 Socket ports support the following port destinations:

| Item | Description |
| --- | --- |
| 1 (LAN 1) | - LAN - LAN & VRRP - LAN LAG Master - LAN LAG Master & VRRP - LAN LAG Member Only exchange LAN1 port with LAN 2 port which is configured with the LAN destination |
| 2 (LAN 2) | - All destinations are supported |
| 3 (WAN 1) | - Cato |
| 4 (WAN 2) | - All destinations are supported |
| USB1 | - Cato - VRRP - Disabled |
| USB2 | - Cato - VRRP - Disabled |

## Socket Ports Destinations for the X1600 Socket

The X1600 Socket ports support the following port destinations:

| Item | Description |
| --- | --- |
| 1 | - Cato |
| 2-8 | - Cato - LAN - LAN & VRRP - LAN LAG Master & VRRP - LAN LAG Master - LAN LAG Member - VRRP - Alternative WAN - Alternative WAN (Layer-2) - Disabled |
| USB1 | - Cato - VRRP - Disabled |
| USB2 | - Cato - VRRP - Disabled |

**Note:** For the combination fiber and copper ports, you don’t need to make changes in the Cato Management when you exchange a copper cable for a fiber cable (and vice versa). The combo port is identified automatically.

## Socket Ports Destinations for the X1700 Socket

The X1700 Socket ports support the following port destinations:

| Item | Description |
| --- | --- |
| 1 | - Cato |
| 2-8 | - Cato - LAN - LAN & VRRP - LAN LAG Master & VRRP - LAN LAG Master - LAN LAG Member - VRRP - Alternative WAN - Alternative WAN (Layer-2) - Disabled |
| Add-on ports | - Cato - LAN - LAN & VRRP - LAN LAG Master & VRRP - LAN LAG Master - LAN LAG Member - VRRP - Alternative WAN - Alternative WAN (Layer-2) - Disabled |

## Exchanging Socket Ports

Use the Socket screen in the Cato Management Application to exchange the ports for a Socket. Then the Cato Management Application pushes the new configuration to the Socket.

**To exchange Socket ports:**

1. From the navigation menu, click **Network** > **Sites** and select the site.
2. From the navigation menu, select **Site Configuration** > **Socket**.
3. In the row for the port you are exchanging, select ![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247779879453.png) More.

**Note:** The available ports appear according to the **Port Name** and not the **Port ID**.
4. Select the port you are exchanging with.
5. In the confirmation window, click **Ok**.
6. Click **Save**. The Cato Management Application pushes the new port configuration to the Socket.
