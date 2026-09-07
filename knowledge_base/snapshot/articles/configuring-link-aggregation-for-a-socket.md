---
title: "Configuring Link Aggregation for a Socket"
slug: "configuring-link-aggregation-for-a-socket"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/configuring-link-aggregation-for-a-socket"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Link Aggregation for a Socket

This article provides information and guidelines about deploying link aggregation on multiple Socket ports.

## Overview of Link Aggregation on Cato Sockets

Link Aggregation (LAG) lets you combine up to four physical Socket LAN ports into one single logical bundle. The LAG provides link level redundancy and greater throughput than a single link.

The following diagram show a sample physical topology for link aggregation on X1700 Sockets that are connected to two standalone switches with the same LAG settings for each X1700 Socket:

- The 2x10G example shows two 10Gbps LAN ports aggregated into a single LAG bundle
- The 4x1G example shows four 1Gbps LAN ports aggregated into a single LAG bundle

![LAN_LAG-topology.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247833796765.png)

### Distributing Traffic between Link Aggregation Members

The Cato Socket implements a per-flow six-tuple scheduler algorithm to distribute the traffic flows between the operational LAG members. The tuple is composed of these values:

- Source IP address
- Destination IP address
- Source port
- Destination port
- Source MAC address
- Destination MAC address

The scheduler hash maps each traffic flow to a specific operational LAG member. If a LAG member state changes to Link-Down, then the scheduler re-maps the traffic flows to the remaining operational LAG links.

### Guidelines for Link Aggregation

- LAGs are supported on all models for the X1500, X1600, and the X1700 Socket (not supported for vSockets)
- For X1500 Sockets, the USB ports aren't supported as LAG members
  - If you configure the LAN2 port as a LAG master or LAG member, the default LAN2 port Management IP is no longer available
- For X1600 and X1700 Sockets, all the LAG members can use either 1Gbps or 10Gbps ports
  - You can't combine ports with different speeds in one LAG
- Each site supports only one LAG bundle For HA Socket sites, see below [Configuring LAG for Socket High Availability](/v1/docs/configuring-link-aggregation-for-a-socket#configuring-lag-for-socket-high-availability).
- A LAG can contain up to a maximum of four LAG members
- LAG is supported only for LAN links
- Only static LAG configuration is supported (LACP isn't supported)
- Switches must support static LAG, and configured for static LAG, before you configure the site for link aggregation

## Configuring Link Aggregation

Use the Cato Management Application to enable and configure the LAG settings for a Socket.

### High-Level Overview of Defining a LAG

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Define one LAN port as the **LAG Master**.
4. **(Optional)** Customize the setting for the minimum number of links (**Min links**) in the LAG that must be operational for the LAG itself to be operational.
5. Associate the other LAN ports as LAG members.

### Customizing the Minimum Number of Operational Links

The **Min links** setting for the LAG master defines the minimum-links condition for the LAG bundle. When the number of operational LAG member meets the **Min links** setting, then the LAG is considered operational. However, if there aren't enough operational LAG members, then the LAG doesn't meet the minimum-links condition, and the LAG bundle state changes to Link-Down. When the LAG is in the Link-Down state, the Socket doesn't send or receive traffic over the LAG bundle.

The default **Min links** setting is **1**. This means that by default, the LAG is operational as long as one LAG member is operational. You can customize this setting, and define that the LAG is only operational when there is more than one operational LAG member.

> [!NOTE]
> Note:
> 
> The Socket port for the LAG master, is also considered as a LAG member. So, it is also counted as a LAG member for the minimum-links condition.

### Configuring the LAG Master and LAG Member Ports

Use the **Socket** screen to define the Socket ports that are the LAG master and LAG members. The LAG master contains the logical settings for the LAG and these settings are applied to the LAG members. The port that is configured as the LAG master is automatically associated to the LAG as a LAG member.

**To configure the LAG master and LAG members:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Configure the LAG master port:
  1. Click the LAN port that is the LAG master.

The **Edit Socket Interface** panel opens.
  2. Enter the **Name** for the port and set the **Destination** to **LAN LAG Master**.
  3. **(Optional)** In **Min links**, enter the minimum number of LAG members that must be operational (in the Link-Up state).
  4. Click **Apply**. The LAG master port is added to the Socket.
4. Configure each LAG member port:
  1. Click the LAN port that is the LAG member.

The **Edit Socket Interface** panel opens.
  2. Enter the **Name** for the port and set the **Destination** to **LAN LAG Member**.
  3. Click **Apply**. The LAG member port is added to the Socket.
5. Click **Save**. The LAG configuration is saved and pushed to the Socket.

### Configuring LAG for Socket High Availability

For Socket high availability (HA) deployments, you can choose to send VRRP keep-alive packets over the LAG bundle. Alternatively, you can also choose to use a dedicated LAN port for the VRRP traffic instead of the LAG. Use the LAN port **Destination** settings in the LAG master to configure that the VRRP traffic is sent over the LAG bundle.

**To configure the LAG bundle to send VRRP traffic:**

1. From the LAN port for the LAG master, set the **Destination** to **LAN LAG Master & VRRP**.
2. Click **Save**.

> [!NOTE]
> Note:
> 
> For sites working in high availability (HA) mode, because the LAG configuration is applied to both Sockets, make sure that the physical layout of the network cables is the same for both Sockets.

### Disabling the LAG Bundle

If you need to disable the LAG bundle, first disable the LAG members and then disable the LAG master. You can't disable the LAG master without disabling the LAG members first.

**To disable the LAG bundle:**

1. Disable the LAG member links:
  1. Select the LAG member link.
  2. From **Destination**, select **Disabled**.
  3. Repeat the previous two steps for each LAG member link.
2. Disable the LAG master link:
  1. Select the LAG master link.
  2. From **Destination**, select **Disabled**.
3. Click **Save**. The LAG bundle is disabled.

## Sample LAG Configuration

The following diagram shows a sample LAG configuration in the **Sockets** screen. There are two ports (ports 3, and 4) in the LAG, port 3 is the LAG master and port 4 is the LAG member. The **Min Links** is set to **1**, this means that at least one of the two ports must have connectivity for the LAG to be considered operational.

| ![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247833894301.png) |
| --- |

![LAN_LAG.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247772943773.png)

## Showing the LAG Status and Throughput

Use the **Monitor** tab in the Socket WebUI to show the real-time status and throughput of the entire LAG, and the individual LAG members.

For more about logging in to the Socket WebUI, see [Accessing the Socket WebUI](/v1/docs/accessing-the-socket-webui).

> [!NOTE]
> Note:
> 
> For an x1500 Socket that has LAN2 port configured as a LAG master or LAG member, the default LAN2 port Management IP is no longer available. Use the Local IP address of the LAG (**Site Settings > Networks > Native Range**) as the Management IP to access the Socket WebUI.

![LANLAG_webui.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247789271709.png)

The following table explains the LAG status in the sample Socket WebUI above:

| Name | Description |
| --- | --- |
| Link Status | The green icons indicate that **LAG 3** (the LAG bundle) and LAG member ports **2** and **3** are in the Link-Up state. |
| Id | **LAG3** represents the LAG bundle. **2** and **3** are the LAG member ports. |
| IP | The IP address of the LAG is **10.24.0.1**. The LAG members aren't assigned with an IP address. |
| Throughput | **LAG3** shows the upstream and downstream throughput of the LAG bundle. **2** and **3** show the specific upstream and downstream throughput for each LAG member. |

## Analyzing Link Aggregation Events

The **Events** screen shows all the LAG events for your account.

You can learn more about using the Events screen in [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network).

### Explaining the Link Aggregation Events

These are the events that are generated when the LAG bundle or LAG members change state (Up or Down). The event type is **Connectivity - Link Aggregation**.

| Action Name | Event Message | Description |
| --- | --- | --- |
| Up | LAG-Member state changed to Up | State for the LAG member changed from Link-Down to Link-Up |
| Up | LAG state changed to Up | State for the LAG bundle changed from Link-Down to Link-Up |
| Down | LAG-Member state changed to Down | State for the LAG member changed from Link-Up to Link-Down |
| Down | LAG state changed to Down due to Min-links condition violation | State for the LAG changed from Link-Up to Link-Down because the LAG doesn't have the minimum number of Link-Up links |

The value for the **socket interface** field shows the physical port for the LAG member.
