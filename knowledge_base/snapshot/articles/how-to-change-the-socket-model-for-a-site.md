---
title: "How to Change the Socket Model for a Site"
slug: "how-to-change-the-socket-model-for-a-site"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/how-to-change-the-socket-model-for-a-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Change the Socket Model for a Site

This article describes how to replace an existing physical Socket model with a different physical Socket model.

## Overview

You can change the Socket model for a site, for example upgrade a site from X1500 to X1700 Socket. When you unassign and disconnect the Socket, the site gets disconnected from the Cato Cloud. All connectivity is restored once the new Socket is assigned to the site.

To change the Socket model for a site with Socket High Availability (HA), you need to unassign both Sockets and replace them with the new Sockets.

## Preparing to Replace a Socket

Before the Socket model is replaced, you are advised to consider the following preparatory steps:

- Before you change the Socket site type, make sure that the S/N (and the MAC address for the X1500 Socket model) of the new Socket is available in the **Socket Inventory** screen (Administration > Socket Inventory). The Socket must be available in the Socket Inventory to connect successfully.
- If there are static IP addresses configured for the existing Socket’s WAN interfaces, we recommend that you log in to the Socket WebUI and copy the static IP configuration. These static IP addresses are not migrated to the new Socket model and you need to configure them again.
- For X1700 Sockets that use an add-on card, you must remove the card and re-assign the ports before you change to a different Socket.

**IMPORTANT!** Replacing a socket causes downtime, we recommend scheduling the replacement during a maintenance window.

## Mapping the Socket Ports

When you migrate from one Socket to another, the ports are mapped differently for each Socket model.

The Socket ports are based on the IDs in the Socket screen (Network > Site Configuration > Socket), not the names that you configure for the ports.

**Note:** You can migrate interchangeably between all Socket models as demonstrated below.

### Changing X1500 and X1600 Sockets

The X1500 Socket ports map to the following ports on the X1600 Socket:

| X1500 Socket | X1600 Socket |
| --- | --- |
| WAN1 | Port 1 |
| WAN2 | Port 2 |
| LAN1 | Port 5 |
| LAN2 | Port 6 |
| USB1 | USB1 |
| USB2 | USB2 |

### Changing X1500 and X1700 Sockets

The X1500 Socket ports map to the following ports on the X1700 Socket:

| X1500 Socket | X1700 Socket |
| --- | --- |
| WAN1 | Port 1 |
| WAN2* | Port 2 or port 3 |
| LAN1* | Port 2 or port 3 |
| LAN2 | Port 4 |
| USB1 | Not migrated |
| USB2 | Not migrated |

* This mapping depends if the X1500 Socket has one or two active ports for WAN traffic:

- If WAN2 is **used as a secondary WAN link**, it maps to port 2 and LAN1 maps to port 3
- If WAN2 is **not used for WAN traffic**, it maps to port 3 and LAN1 maps to port 2

### Changing X1600 and X1700 Sockets

The X1600 Socket ports map to the following ports on the X1700 Socket:

| X1600 Socket | X1700 Socket |
| --- | --- |
| Port 1 | Port 1 |
| Port 2 | Port 2 |
| Port 5 | Port 3 |
| Port 6 | Port 4 |
| USB1 | Not migrated |
| USB2 | Not migrated |

## Changing the Socket Model for a Site

Use the Cato Management Application to change the site type to the new Socket model. Then disconnect the existing Socket, and connect the network cables to the new Socket. When the new Socket is ready, assign it to the new site.

**To change the Socket model for a site:**

1. In the Cato Management Application, unassign the existing Socket from the site.

For more about unassigning a Socket, see [Managing Sockets](/v1/docs/managing-sockets).
  1. From the navigation menu, click **Network > Sites**, and select the site with the Socket you are unassigning.
  2. From the navigation menu, click **Site Configuration > Socket**.

![unassign.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247834902813.png)
  3. From the **Actions** menu of the site you are unassigning, select **Unassign**.

A warning window opens.
  4. Click **OK**.

The Socket is unassigned from the site. The account receives a new **Notification** to activate a new Socket.
2. From the navigation menu, click **Network > Sites**, and confirm that the **Connectivity Status** for the site is **Disconnected**.
3. Change the site's **Connection Type** .
  1. From the navigation menu, click **Network > Sites** and select the site.
  2. Expand the **General** section.
  3. From the **Connection Type** drop-down menu, select the new Socket model site type (for example, Socket X1700).

![Change_Connection_Type.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247790281373.png)
  4. Click **Save**.
4. Connect the WAN port of the new Socket (WAN1 for the X1500 or port **1** for the X1600 and X1700 Sockets) to the Internet.

The Socket automatically upgrades to the newest Socket OS version.
5. Open the notification area ![notification.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247790354077.png) (in the upper-right menu bar), and expand the **Activate New Socket** message.

![Activate_Socket.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247774101405.png)
6. Click **Accept**. Select the site that the Socket is assigned to.
7. For sites using a Socket High Availability (HA) configuration: If necessary, change the Socket MGMT interface IP address to meet your requirements.
