---
title: "Working with Socket Sites"
slug: "working-with-socket-sites"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/working-with-socket-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Socket Sites

This article explains how to use the Socket page to configure Socket settings and monitor the status.

## Overview

The Socket page includes a detailed overview of each Socket's ports and their status. The link settings are configured as part of creating the site, and you can edit the settings and activate additional links for the Socket.

Before you install a Socket for a site, make sure the [Connectivity Requirements for Socket Upgrades](/v1/docs/connectivity-requirements-for-socket-upgrades) are met.

For more information about Socket throughput and capacity information per model, see [Cato Cloud Thresholds and Limits](/v1/docs/cato-cloud-thresholds-and-limits).

![Socket.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30810554088477.png)

The Socket overview displays each port state as follows:

- For ports configured with the **Cato** destination type
  - Green - Cable connected, port is connected to Cato
  - Yellow - Cable connected, port is disconnected from Cato (no tunnel to the Cato Cloud)
  - Red - Cable isn’t connected, port is down
- For ports configured with other destination types
  - Green - Cable connected, port is up
  - Red - Cable isn’t connected, port is down
  - Grey - port is disabled

## Working with X1500 Socket Sites

![X1500.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30810586269085.png)

These are the default X1500 Socket settings:

- **USB2 - Disabled**
- **USB1 - Disabled**
- **LAN1** / port **1** - Enabled as LAN (cannot be changed)
- **LAN2** / port **2** - **Disabled**

The LAN2 / port 2 link can be used as a WAN destination, for more information see [Exchanging Socket Ports](/v1/docs/exchanging-socket-ports)
- **WAN1** / port 3 (**WAN**) - Enabled as **Cato (Primary)** (cannot be changed)
- **WAN2** / port **4** - **Disabled** or enabled as **Cato**, depending if you selected the **Enable/Use WAN2** option when adding the new site

## Working with the X1600 Socket Site

![X1600.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30810523177117.png)

These are the default X1600 Socket settings:

- **Port 1** – Enabled as **WAN 1**
- **Port 2** – Disabled or enabled as **WAN 2**, depending if you selected the **Enable/Use WAN2** option when adding a new site
- **Port 5** – Enabled as **LAN1**
- The other ports are disabled by default

## Working with the X1700 Socket Site

![X1700.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30810551136413.png)

These are the default X1700 Socket settings:

- **Port 1** - Enabled as **WAN 1**
- **Port 2** - Disabled or enabled as **WAN 2**, depending if you selected the **Enable/Use WAN2** option in the **Add Site** window
- **Port 3** - Enabled as **LAN1**
- The remaining ports are disabled by default

## Configuring the Add-on for the X1700 Socket

The X1700 Socket may also include add-ons, which are hardware cards with additional network interfaces that are inserted into the Socket expansion slots. Configure these add-on interfaces as you configure other interfaces.

- Add-ons are often pre-ordered and installed by Cato Networks
- Add-ons support mixing LR (long-range) and SR (short-range) transceivers in the same Socket For more information, see [Supported Socket Transceivers and USB Ethernet Adapters](/v1/docs/supported-socket-transceivers-and-usb-ethernet-adapters)
- Before you insert add-ons in the expansion slot, turn off the Socket and disconnect the power supply
- The X1700 Socket supports only one network card add-on at one time, multiple network cards are NOT supported
- The X1700B Socket supports a second 4x10 Gbps fiber add-on card, the first one must also be a 4x10 Gbps fiber add-on card

This provides a total of eight 10Gbps fiber ports

The default setting for the **Add-on** option is **None**. If the configured add-on in the Cato Management Application and the actual hardware don't match, then the add-on interface is treated as if it were physically disconnected.

For more information, see the [X1700 Socket deployment guide](/v1/docs/cato-socket-deployment-guides-and-data-sheets).

**To configure the add-on for the X1700 Socket:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Click **New Add-on Card**, and in the panel select the add-on type for the Socket.

![X1700_Socket_Addon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30810570410781.png)
4. For X1700B Sockets with a second add-on, click **Additional Add-On**.
5. Click **Save**.

The additional ports are added to the Socket page.

Once you select an add-on, the **Add Add-on Ports** button is disabled until you remove the existing add-on card.
6. Wait for at least 5 minutes before installing the add-on card in the Socket.

### Removing Add-on Ports

You can only configure one set of Add-on ports at a time. To configure a new add-on port, you must first remove the existing add-on ports.

**To remove the add-on ports for the X1700 Socket:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Click the three dots at the end of the row for the ports you want to remove, and click **Remove Add-On Port**.
4. In the confirmation window, click **Remove Add-On**.

## Opening the Socket WebUI

To open the Socket WebUI, from the **Actions** drop-down menu, select **Connect to Socket**. The Socket WebUI opens in a new browser tab and automatically logs in. For more information see [Accessing the Socket WebUI](/v1/docs/accessing-the-socket-webui).

## Configuring Socket Link Settings

This section explains how to configure settings for links that connect to the Cato Cloud and for MPLS Alternative WAN links. It also discusses how to configure failover and fallback settings for sites that have more than one link to the Cato Cloud.

By default, Socket sites are enabled for WAN Recovery, for more information, see [Socket Site Resiliency with WAN Recovery](/v1/docs/socket-site-resiliency-with-wan-recovery).

![Socket_ports.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30810539296925.png)

### Configuring the Socket Interface Destinations

Use the **Destination** setting for a Socket interface to define where the Socket sends traffic to. These are the destination options:

- LAN - internal network for a site
- Alternative WAN (Layer-2) - MPLS network with Socket sites on the same subnet
- Disabled - this interface doesn't send or receive traffic
- Alternative WAN - MPLS network with Socket sites on different subnets
- Cato - this interface connects to the Cato cloud

You can't change the destination for these interfaces: **LAN1** (LAN) and **WAN1** (Cato).

**To configure the destination for a Socket interface:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. From the table, click the interface.

The **Edit Socket Interface** panel opens.
4. Enter the **Name** that identifies the interface in the Cato Management Application.
5. From the **Destination** drop-down menu, select the destination for this interface.
6. Click **Apply**. The new destination is added to the row for this interface.
7. Click **Save**.

### Configuring Links to Cato Cloud

Configure the link settings that connect the site to the Cato Cloud. This section is for links that use the **Cato** destination.

**Interface WAN Roles**

You can use network rules to prioritize the network traffic transport according to the WAN role. For example, you can define the WAN 1 role as the primary interface and the WAN 2 role as the secondary interface for a network rule.

You must define a **WAN Role** for all **Cato** destinations, and you can't use the same **WAN Role** for multiple interfaces.

**Interface Precedences**

The **Precedence** for a link used for failover and fallback settings determines the priority in which these links are used. Precedence 1 interfaces are active by default, and the Socket activates the other precedences if there are connectivity or performance issues with the higher precedence.

Configure the bandwidth for the site according to the terms of your Cato license.

**To configure the settings for a Cato Cloud link:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. From the table, click the interface.

The **Edit Socket Interface** panel opens.
4. Select the **WAN Role** for this interface, based on the requirements of your network rules.
5. Select the **Precedence** priority for the interface.
6. Configure the maximum **Bandwidth** settings for all traffic in the site.

> [!NOTE]
> Note:
> 
> If you enter **Upstream** or **Downstream** values that are greater than the actual connection speed of your ISPs link, the Cato Cloud QoS engine can't manage the traffic.
7. Click **Apply**. The **Edit Socket Interface** panel closes.
8. Click **Save**.

### Configuring Links for Alternate WAN Destinations

Configure the WAN interface settings for **Alternate WAN** and **Alternate WAN (Layer-2)** MPLS traffic destinations. Generally, private IPs and interfaces are used for connecting directly to the MPLS provider.

**To configure the settings for an Alternative WAN link:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. From the table, click the interface.

The **Edit Socket Interface** panel opens.
4. Verify that the **Destination** is **Alternate WAN** and **Alternate WAN (Layer-2)**.
5. Configure the maximum **Bandwidth** settings for all traffic in the site.

> [!NOTE]
> Note:
> 
> If you enter **Upstream** or **Downstream** values that are greater than the actual connection speed of your ISPs link, the Cato Cloud QoS engine can't manage the traffic.
6. Configure these settings for the **Private** or **Public** Alternative WAN networks.
  1. **Interface IP** - IP address for the Socket interface for the traffic
  2. **Gateway** - IP address for the Alternative WAN gateway (such as MPLS firewall or router)
  3. **Network** - IP range (with CIDR) for the LAN
  4. **ID (VLAN)** - Enter the VLAN tag for the interface
7. Click **Apply**. The **Edit Socket Interface** panel closes.
8. Click **Save**.
