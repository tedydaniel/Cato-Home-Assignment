---
title: "Using Sockets in an HA Deployment"
slug: "using-sockets-in-an-ha-deployment"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/using-sockets-in-an-ha-deployment"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Sockets in an HA Deployment

This article explains how to configure Sockets in a High Availability (HA) active/passive configuration for a site. We recommend that you read [What is Socket High Availability (HA)](/v1/docs/what-is-socket-ha) before you implement a Socket HA deployment.

For more about using Socket HA with Alt. WAN links, see [Integrating Cato with Alternative WAN Network](/v1/docs/integrating-cato-with-an-alt-wan-network).

## Prerequisites for Socket HA

- Each Socket must have a unique IP address
- We recommend that both Sockets are running the same major Socket OS version (for example 23.1.13986 and 23.0.12764)

## Installing a Backup Cato Socket

For more about adding a Socket to a site, see [Using the Cato Management Application to Add Sites](/v1/docs/using-the-cma-to-add-sites).

**To enable High Availability at a new site:**

1. Connect the first Cato Socket.
2. In the Cato Management Application, verify that the Cato Socket has been detected and associate it to the required site.
3. Continue with the following procedure.

**To enable High Availability at an existing site:**

1. Connect the backup Cato Socket.
2. Make sure there is Ethernet connectivity between the LAN1 ports of both Cato Sockets.
3. In the Cato Management Application, verify that the backup Cato Socket has been detected and assign it to the relevant site.
4. The Cato Management Application **automatically** identifies that the selected site already has a Cato Socket connected to it. It then designates the second Cato Socket as the backup for High-Availability mode.

## High Availability Configurations and Status

You can change the VRID and the management IP addresses for the HA sockets.

### Showing the High Availability Information and Status

The High Availability section shows you the following information about the Sockets:

- Serial number (S/N)
- Socket version
- Management IP address for the Socket WebUI
  - Option to open Socket WebUI with SSO
- High Availability Status - overall HA status for the site (see below for status description)
- Which Socket is the master (currently active)
- The connectivity status for each Socket to the Cato Cloud
- VRID number (see below [Changing the VRID](/v1/docs/using-sockets-in-an-ha-deployment#changing-the-vrid))

![SocketHA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247818797213.png)![Socket_HA_Configurations.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247834235293.png)

| Item | Description |
| --- | --- |
| Status | The HA status for the site (Ready or Not Ready), only shows ready when each status HA status indicator is OK |
| Connected | The green icon indicates that both Sockets have WAN connectivity to the Cato Cloud |
| Keepalive | The green icon indicates that one Socket is the primary and one is the secondary (If both Sockets are status primary, then there is an HA split brain issue) |
| Compatible Version | The green icon indicates that both Sockets are running compatible (the same major) Socket versions, for example 14.1.13986 and 14.0.12764 |

**To show the Socket HA information and status:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.

### Working with the Web Management IP Address

The **High Availability Configurations** section lets you configure the management IP address that you can use to open the browser-based Socket WebUI for each Socket. In addition, with one click you can open the login page for the Socket WebUI in a new tab.

> [!NOTE]
> Notes:
> 
> - The management IP address must be within the native range for one of the LAN links.
>   - Make sure that the secondary Socket's management IP address is within the LAN native range for the site.
>   - When BGP is enabled, pinging the secondary management IP from a device on the socket LAN will fail. This is a known behavior.
> - If you unassign the primary or secondary Socket from the site, the Sockets are assigned new management IP addresses.
> - By default, Cato assigns the last two IP addresses in the Native Range as the management IPs for each Socket. If these management IPs are within the DHCP range, then the DHCP range is automatically updated so that the management IPs are not included in the DHCP range, and remain the last two IP addresses in the native range.

**To change the management IP address:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Expand the **High Availability Configurations** section, and enter the new **Primary Management IP** address for the Socket that is used for the Socket WebUI.
4. Repeat the previous step for the **Secondary Management IP** address.
5. Click **Save**.

To open the Socket WebUI, from the **Actions** drop-down menu for a Socket, select **Socket WebUI**. The Socket WebUI opens in a new browser tab and automatically logs in. For more information see [Accessing the Socket WebUI](/v1/docs/accessing-the-socket-webui).

### Changing the VRID

Sockets use VRRP messages (following RFC 5798) to identify when the primary Socket had a failure and when it is functional again.

VRRP messages have an ID that enables other network entities in the same network to identify VRRP messages that are applicable for them. By default, Cato Networks uses VRID 100.

**To change the VRID:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Expand the **High Availability Configurations** section, and enter the new VRID.
4. Click **Save**.

### Changing the LAN Port for HA Keepalive Traffic

By default, the LAN port with the lowest number is used both for the HA keepalive traffic and for the user traffic. The remaining LAN ports carry only the user traffic.

You can choose any LAN port for the HA keepalive traffic by changing the port **Destination** from **LAN** to **LAN & VRRP**. The following screenshot shows port 3 for LAN user traffic and port 4 for the HA keepalive traffic and for the user traffic.

![LAN_VRRP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247800448029.png)

You can only define one LAN port with the **Destination** as **LAN & VRRP**.

**To change which LAN port is used for HA keepalive traffic:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Select the LAN port that is currently being used for the HA keepalive traffic.

The **Edit Socket Interface** panel opens.
4. In the **Destination** drop-down menu, select **LAN**, and then click **Apply**.
5. Select the new LAN port for the HA keepalive traffic.
6. In the **Destination** drop-down menu, select **LAN & VRRP**, and then click **Apply**.
7. Click **Save**. The new LAN port is used for the HA keepalive traffic and user traffic.

### Known Limitations

For Sockets that use multiple WAN links, if there is a NAT device between the Socket and the PoP, then it’s possible that one or more of the WAN links can’t connect to the PoP. This can create connectivity issues, such as the HA status of the site is **Not Ready**.

The PoP uses the source port of each incoming DTLS connection to connect each WAN link to the same logical tunnel. The NAT device may change the source port, and prevent a WAN link from connecting to the same logical tunnel as the other WAN links.
