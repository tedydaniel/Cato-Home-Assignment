---
title: "Configuring Link Aggregation for a Socket (EA-LACP)"
slug: "configuring-link-aggregation-for-a-socket-ea-lacp"
updated: 2026-08-31T08:43:53Z
published: 2026-08-31T08:43:53Z
canonical: "knowledge.catonetworks.com/configuring-link-aggregation-for-a-socket-ea-lacp"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Link Aggregation for a Socket (EA-LACP)

This article provides information and guidelines about deploying link aggregation on multiple Socket ports.

## Overview of Link Aggregation on Cato Sockets

Link Aggregation (LAG) lets you combine up to four physical Socket LAN ports into one single logical bundle. The LAG provides link level redundancy and greater throughput than a single link.

The following diagrams show a sample physical topology for link aggregation on X1700 Sockets that are connected to two standalone switches with the same LAG settings for each X1700 Socket:

- The 2x10G example shows two 10Gbps LAN ports aggregated into a single LAG bundle
- The 4x1G example shows four 1Gbps LAN ports aggregated into a single LAG bundle

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/LAG Diagram.png)

### Static and Dynamic Link Aggregation

Cato Sockets support these link aggregation group types:

- **Static** - Manually configure the member ports on both the Socket and the connected switch. The devices do not negotiate or validate the bundle.
- **Dynamic (LACP)** - The Socket and switch exchange Link Aggregation Control Protocol Data Units (LACPDUs) to verify which links can participate in the bundle. LACP validates and negotiates the bundle after both sides are configured. It does not create the LAG configuration on the switch or choose switch ports automatically. You configure a compatible LACP bundle on both the Socket and the connected switch, and LACP then validates the links and only uses members that successfully negotiate with the same LACP partner.

### Distributing Traffic for Static LAG

For static LAG configurations, Cato Socket implements a per-flow six-tuple scheduler algorithm to distribute the traffic flows between the operational LAG members. The tuple is composed of these values:

- Source IP address
- Destination IP address
- Source port
- Destination port
- Source MAC address
- Destination MAC address

The scheduler hash maps each traffic flow to a specific operational LAG member. If a LAG member state changes to Link-Down, then the scheduler re-maps the traffic flows to the remaining operational LAG links.

### Distributing Traffic for LACP Configurations

For dynamic LACP configurations, you configure the transmission hash to determine which packet fields the Socket uses to assign traffic flows to the operational member ports. You can select one of these options for which fields are used for the hash:

- **L2** - Source and destination MAC addresses
- **L2L3** - Source and destination MAC and IP addresses. This is the default setting
- **L3L4** - Source and destination IP addresses and, for eligible non-fragmented TCP/UDP traffic, transport-layer ports

In LACP configurations, the hash distributes flows across the available links but does not guarantee that every member carries the same amount of traffic. For example, with the **L2** option, traffic from the same source MAC address to the same next-hop MAC address can remain on one member. **L2L3** or **L3L4** generally provides more distribution when the traffic contains diverse IP addresses or transport-layer ports.

Each flow remains on the member selected by the hash to reduce packet reordering.

### Using the LAG for VRRP Traffic in HA Deployments

For Socket HA deployments, you can send VRRP keepalive traffic over the LAG bundle or use a dedicated port. Configuring the LAG to carry both LAN traffic and HA keep-alive traffic provides link redundancy for the LAN connection between the primary and secondary Sockets. If a LAG member link goes down, VRRP failover can still move traffic to the secondary Socket.

> [!NOTE]
> Note:
> 
> For sites working in high availability (HA) mode, because the LAG configuration is applied to both Sockets, make sure that the physical layout of the network cables is the same for both Sockets.

### Guidelines for Link Aggregation

- Socket sites support static LAG and dynamic LAG using LACP. You must configure the connected switch with the same aggregation type as the Socket. For dynamic LAG, the Socket operates in LACP active mode and can negotiate with a switch configured in active or passive mode
- Each site supports only one LAG bundle. For HA Socket sites, see below [Configuring LAG for Socket High Availability](/v1/docs/configuring-link-aggregation-for-a-socket#configuring-lag-for-socket-high-availability).
- LAGs are supported on all models for the X1500, X1600, and the X1700 Socket (not supported for vSockets)
- For X1500 Sockets, the USB ports aren't supported as LAG members
  - If you configure the LAN2 port as a LAG master or LAG member, the default LAN2 port Management IP is no longer available
- For X1600 and X1700 Sockets, all the LAG members can use either 1Gbps or 10Gbps ports
  - You can't combine ports with different speeds in one LAG
- A LAG can contain up to a maximum of four LAG members
- LAG is supported only for LAN links

## Configuring Link Aggregation

Use the Cato Management Application to enable and configure the LAG settings for a Socket.

### High-Level Overview of Defining a LAG

1. Define the logical LAG interface and whether it also carries VRRP traffic.
2. Choose static aggregation or dynamic aggregation using LACP.
3. Set the minimum number of operational links required for the LAG to remain active.
4. Assign the physical LAN ports that participate in the LAG.
5. For a dynamic LAG, choose how the Socket distributes traffic across the member links.
6. Apply the LAG configuration to the site.

### Customizing the Minimum Number of Operational Links

The **Minimum links** setting for the LAG master defines how many operational member links are required for the LAG bundle to remain active. If the number of operational members is lower than this value, the LAG bundle changes to **Link-Down**, and the Socket does not send or receive traffic over the LAG.

The default **Minimum links** setting is **1**. This means that by default, the LAG is operational as long as one LAG member is operational. You can customize this setting, and define that the LAG is only operational when there is more than one operational LAG member.

> [!NOTE]
> Note:
> 
> The Socket port for the LAG master, is also considered as a LAG member. So, it is also counted as a LAG member for the minimum-links condition.

### Configuring a Static or Dynamic LAG

Use the Socket page to define the Socket ports that are the LAG master and LAG members. The LAG master contains the logical settings for the LAG and these settings are applied to the LAG members. The port that is configured as the LAG master is automatically associated to the LAG as a LAG member.

Use the Socket page to define the ports that form the LAG. The LAG master contains the logical settings for the bundle, and these settings apply to all LAG members. The port configured as the LAG master is automatically included as a member of the LAG.

**To configure the LAG master and LAG members:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Click the LAN port that you want to configure as the LAG master. The **Edit Socket Interface** panel opens.
4. Enter a **Name** for the port.
5. Set **Destination** to one of these options:
  - **LAN LAG Master**
  - **LAN LAG Master & VRRP** for an HA deployment that sends VRRP traffic over the LAG
6. Under **LAN LAG (Static/LACP)**, set the **Group Type** as **Static** or **Dynamic (LACP)**.
7. In **Minimum Links**, select the minimum number of operational members required for the LAG to remain operational.
8. In **Member Ports**, select the additional LAN ports to include in the bundle.
9. For **Dynamic (LACP)**, select a **Transmission Hash** (**L2**, **L2L3**, or **L3L4**).
10. Click **Apply** and then click **Save**. The LAG configuration is saved and pushed to the Socket.

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

## How LACP Operates

### How LACP Selects Operational Members

For a dynamic LAG, the Socket sends and receives LACPDUs on each configured member port. The LACPDUs contain information that identifies the local LACP system, the peer system, and the individual member port.

The Socket uses the first valid LACP partner as the reference for the bundle. Additional member ports can join when the peer reports the same LACP system ID and aggregator key as the bundle’s recorded partner. Mismatched members remain unselected and generate a partner-mismatch event.

A configured port does not forward traffic as part of the LAG when:

- It does not receive valid LACP information from the peer
- Its partner information does not match the other members
- The local and peer LACP states are not synchronized
- The peer does not select the link for forwarding

This behavior prevents a link connected to an unrelated or incorrectly configured switch from silently joining the bundle.

#### Using Multiple Switches

You can connect members to more than one physical switch only when those switches present the same LACP system information, for example when they operate as a supported stack or multi-chassis LAG system. Independent switches that do not synchronize their LACP state are treated as different partners, and members from one of the partners are excluded.

### Understanding LACP Timers

The Socket operates in LACP active mode and advertises the fast periodic rate. It also supports peers that advertise the slow periodic rate.

Member failure detection depends on the periodic rate advertised by the peer, as follows:

- Fast periodic rate - approximately 3 seconds before expiry
- Slow periodic rate - approximately 90 seconds before expiry

The Socket automatically follows the rate advertised by the peer. You cannot configure the LACP timer in the CMA.

## Sample LAG Configuration

The following diagram shows a sample LAG configuration in the **Sockets** page. There are two ports (ports 3, and 4) in the LAG, port 3 is the LAG master and port 4 is the LAG member. The **Min Links** is set to **1**, this means that at least one of the two ports must have connectivity for the LAG to be considered operational.

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

The **Events** page shows all the LAG events for your account.

You can learn more about using the Events page in [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network).

### Explaining the Link Aggregation Events

These are the events that are generated when the LAG bundle or LAG members change state (Up or Down). The event type is **Connectivity - Link Aggregation**.

| Action Name | Event Message | Description |
| --- | --- | --- |
| Up | LAG-Member state changed to Up | State for the LAG member changed from Link-Down to Link-Up |
| Up | LAG state changed to Up | State for the LAG bundle changed from Link-Down to Link-Up |
| Down | LAG-Member state changed to Down | State for the LAG member changed from Link-Up to Link-Down |
| Down | LAG state changed to Down due to Min-links condition violation | State for the LAG changed from Link-Up to Link-Down because the LAG doesn't have the minimum number of Link-Up links |

The value for the **socket interface** field shows the physical port for the LAG member.
