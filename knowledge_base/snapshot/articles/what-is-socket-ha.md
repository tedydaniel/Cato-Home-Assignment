---
title: "What is Socket HA"
slug: "what-is-socket-ha"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/what-is-socket-ha"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is Socket HA

This article discusses High Availability (HA) configurations and failover conditions for sites using a pair of physical Cato Sockets.

## Overview of Socket High Availability for a Site

To improve site resiliency, Cato strongly recommends deploying each site with a pair of Sockets that operate in High Availability (HA) mode. This mode of operation ensures service continuity for the site in the event of a single Socket failure. During a failover, the Cato Cloud maintains the flows state and there is minimal impact on the end-user experience.

**Supported Socket HA Sites**

Cato supports Socket HA for the following environments:

- Physical Socket site
- AWS vSocket site
- Azure vSocket Site

This article explains how HA works for a physical Socket site. For more about setting up Socket HA in a few clicks, see [Using Sockets in an HA Deployment](/v1/docs/using-sockets-in-an-ha-deployment).

- For more about AWS vSocket HA, see [Configuring HA for AWS vSockets](/v1/docs/configuring-ha-for-aws-vsockets)
- For more about Azure vSocket HA, see [Configuring High Availability for Azure vSockets](/v1/docs/configuring-ha-for-azure-vsockets)

### Socket High Availability and Different Socket Models

Socket HA sites can use two Sockets with the same Socket type X1500, X1600, X1600 LTE, or X1700. However, you can't use different Socket types, so a site with an X1600 and an X1700 Socket is not supported.

- You can use an X1500 Socket and X1500B Socket in the same HA site.
- You can't use an X1600 Socket and X1600 LTE Socket in the same HA site.

## Understanding Socket High Availability and Failover

In a Socket HA deployment, two Cato Sockets are assigned to a site. The first Socket assigned to the site is identified as the primary Socket, the second one is the secondary Socket. The Sockets operate in HA Active/Standby mode. During a site’s normal operation, the primary Socket has the HA Master status, while the secondary Socket has the HA Standby status. Only the Socket with the HA Master status handles the traffic.

1. The secondary (Standby) Socket continuously monitors the state (liveliness) of the Master Socket by listening for the periodic keepalive messages that the primary Socket sends. The keepalive messages are sent over the designated interface with the destination set to **LAN & VRRP** or **VRRP** (see below [LAN Connectivity and Socket HA](/v1/docs/what-is-socket-ha#lan-connectivity-and-socket-ha)).
2. Once the secondary (Standby) Socket detects that the primary Socket is down, it changes its HA state to Master and starts handling the traffic. This happens after three seconds of missed HA keepalive messages.
3. The secondary Socket sends a GARP message to LAN networks to speed up the Layer 2 convergence.
4. When the primary Socket recovers and is restored to regular functionality, then it preemptively becomes the Master and the secondary Socket returns to Stand-by status.

The following image shows the HA configuration page for X1500 Sockets in the Cato Management Application in Network > Sites > {site name} > Site Configuration > Socket:

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248005421597.png)

| Item | Description |
| --- | --- |
| 1 | Socket HA role - Primary or Secondary |
| 2 | Socket HA status - Master or Standby |
| 3 | HA **Status** - Ready or Not-Ready |
| 4 | Specific conditions for the overall HA status - **Connected** - Socket WAN connectivity - ![GreenCheck.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248052973341.png)- Both primary and secondary Sockets have at least one operational tunnel connected to the Cato Cloud - ![Red_X.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248036672541.png)- Socket has no operational tunnels connected to the Cato Cloud - **Keepalive** - State of the HA keepalive channel between the Sockets - ![GreenCheck.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248052973341.png)- Secondary Socket receives HA keepalive messages from the primary Socket - ![Red_X.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248036672541.png)- Secondary Socket isn’t receiving HA keepalive messages from the primary Socket - **Compatible version** - Both primary and secondary Sockets are running compatible Socket OS versions **Note:** Socket HA failover takes place even if the Sockets are running different major versions. However, the site might experience functionality issues if the secondary Socket version does not support features that are supported for the primary Socket version. For example, if the primary Socket runs version 18.0 and the secondary Socket is running version 15.0, In the case of a failover, features that were released with versions 16 - 18 will not work while the secondary Socket is active. - ![GreenCheck.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248052973341.png)- Both Sockets are running compatible (the same major) Socket version, for example 14.0.13986 and 14.0.12764 - ![Red_X.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248036672541.png)- Sockets have different major Socket versions, for example 14.0.13986 and 13.0.48732 |

### Sample Socket HA Failover

The following diagrams show an example of an issue in the primary Socket that causes a failover to the secondary Socket. When the secondary Socket discovers that the primary Socket is down, it then changes its status to Master. The Cato Cloud transfers the traffic flows to the WAN links in the secondary Socket.

| ![Socket_HA_Regular.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248022016797.png) | ![Socket_HA_Failure.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248053469725.png) |
| --- | --- |

### Socket HA and Split-Brain Condition

A split-brain condition is when both Sockets have the Master role at the same time. This can happen due to a LAN connectivity problem between the Sockets that creates a situation where the HA keepalive messages do not reach the secondary Socket.

You can identify a split-brain condition by checking the Socket page (shown above) in the Cato Management Application.

- The primary and secondary Sockets will be shown as status **Master** (item 2)
- The **Keepalive** condition (in item 4) will be shown as **Failed** and this causes the HA **Status** (item 3) to be shown as **NOT READY**

After the LAN connectivity issue is resolved, the secondary Socket identifies that the primary Socket is the Master and the secondary Socket returns to Stand-by status.

#### Site Traffic During Split-Brain Condition

The following process makes sure that during a split-brain condition, only the secondary Socket handles the traffic for the site (even if there is a split-brain condition).

- For downstream traffic (from the PoP to the site):
  1. The PoP detects that the secondary Socket is now the Master.
  2. The PoP sets the preferred metric for the secondary Socket tunnels.

The downstream traffic is now only routed to the secondary Socket.
- For upstream traffic (from the site to the PoP):
  1. When the secondary Socket changes the HA state from Standby to Master, it sends a GARP message to the LAN to update the ARP and MAC tables that it is now the Master.

The upstream traffic from the LAN is now only routed to the secondary Socket.

## HA Socket Connectivity to the Cato Cloud

Both primary and secondary Sockets establish DTLS tunnels to the same Cato Cloud PoP on each of WAN ports. In the Upstream direction, only the Master Socket sends the traffic to the PoP. In the Downstream direction, the PoP uses only the Master Socket tunnels to send the traffic to the site. In case of a Socket HA failover event, the secondary Socket becomes the new Master, and the PoP shifts the traffic from the failed primary Socket tunnels to the secondary Socket tunnels. The PoP maintains the flow state and the NAT state to make sure that all user applications continue to operate during and after the failover.

The default deployment uses routers between the Socket and the ISP. However, it is possible to customize the site deployment to connect the Socket to the PoP without a router - please contact your official Cato representative for more information.

Below are sample physical and logical topologies for the Socket HA:

![PhysicalLogicalTopology.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248012139677.png)

For optimal WAN connectivity, performance and HA functionality, Cato recommends symmetrical (mirrored) cabling layout for both Sockets. For example, if the primary Socket port WAN1 is connected to ISP1 and port WAN2 is connected to ISP2, the secondary Socket must have the same ports connected to the same ISPs as the primary Socket.

These symmetrical topologies can include direct connections to the ISP routers or using a stack of switches.

![WAN_Connectivity_Router_Switch.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248022314269.png)

> [!NOTE]
> Note:
> 
> For standard HA configurations, Cato recommends that you use a symmetrical layout for both the Primary and Secondary Sockets. When using LTE, there are scenarios where you might want to use SIM cards from different carriers to ensure better coverage or only use a SIM card on the secondary Socket.

## LAN Connectivity and Socket HA

Cato requires that both the primary and secondary Sockets have a symmetrical (mirrored) cabling layout for the LAN connectivity. For example, LAN port 1 for both the primary and secondary Sockets is connected to the LAN switch (or LAN ports 1 and 2 for configurations with multiple LAN ports).

This section discusses the following LAN connectivity options for Socket HA:

1. Single LAN port
2. Multiple LAN ports
3. LAN link aggregation (recommended option)
4. Dedicated port for HA keepalive messages

Some of these options require additional configurations of the site in the Cato Management Application. For example, the LAN port is configured for LAN & VRRP or VRRP.

### Socket HA with a Single LAN Port

There are configurations that use a single LAN port to connect the primary and secondary Sockets to the LAN switch. With this configuration, the same port number must be used on both Sockets. The user traffic and the HA keepalive messages run over a single link. This topology doesn’t provide LAN link redundancy.

Socket HA failover (where the secondary Socket becomes the Master) only occurs when both of these conditions are met:

1. The secondary Socket stops receiving the HA keepalive messages from the primary Socket for a period of three seconds.
2. The LAN port on the secondary Socket (which is used for the HA keepalive messages) is in the CONNECTED state.

If the Secondary Socket LAN port is DISCONNECTED, it will not become the Master to avoid a possible split-brain condition.

The following diagram shows a sample Socket HA topology with a single LAN port on each Socket connected to a switch:

![HA_LAN_switch.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248053767965.png)

### Socket HA with Multiple LAN Ports

This section discusses when both the primary and secondary Sockets are connected to the LAN switches via two or more independent LAN ports. With this configuration, the same ports must be used on both Sockets for the LAN connectivity.

By default, the LAN port with the lowest number is used both for the HA keepalive traffic and for the user traffic. The remaining LAN ports carry only the user traffic.

You can choose any LAN port for the HA keepalive traffic by changing the port **Destination** from **LAN** to **LAN & VRRP**. The following screenshot shows port 3 for LAN user traffic and port 4 for the HA keepalive traffic and for the user traffic.

![LAN_VRRP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248006339357.png)

For more about changing the LAN port for HA keepalive traffic, see [Using Sockets in an HA Deployment](/v1/docs/using-sockets-in-an-ha-deployment). This topology doesn’t provide LAN link redundancy.

Socket HA failover (where the secondary Socket becomes the Master) only occurs when both of these conditions are met:

1. The secondary Socket stops receiving the HA keepalive messages from the primary Socket for a period of three seconds.
2. The LAN & VRRP port on the secondary Socket is in the CONNECTED state.

If the Secondary Socket LAN port is DISCONNECTED, it will not become the Master to avoid a possible split-brain condition.

### Socket HA with LAN Link Aggregation (Recommended Configuration)

Both the primary and secondary Sockets are connected to the LAN switches via two or more LAN ports bundled in a link aggregation (LAG). With this configuration, the same ports must be used on both Sockets for the LAN connectivity. This topology provides LAN links redundancy both for the user traffic and for the HA keepalive messages. If one of the LAG member ports fails, the other member ports will continue to carry the user traffic and the HA keepalive traffic.

This topology provides both link resiliency and Socket resiliency and is considered a best practice.

To learn more about LAN LAG, see [Configuring Link Aggregation for a Socket](/v1/docs/configuring-link-aggregation-for-a-socket).

The following diagram is an example of Socket HA LAN connectivity topology using a LAN LAG with a stack of switches:

![SocketHA_LAG.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248012547357.png)

### Dedicated Port for the HA Keepalive Traffic

In this configuration, you isolate the HA keepalive traffic from the LAN traffic. You can allocate a single port (LAN, WAN, or USB ports) only for the HA keepalive traffic while using one or more remaining LAN ports for the LAN traffic.

To set the dedicated LAN port for the HA keepalive traffic, set the **Destination** for the port to **VRRP**. Then set the **HA link between sockets** option to **Direct** or **Via Switch**.

![Direct_HA_Link.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248054006813.png)

These are the dedicated port configurations:

1. Direct (back-to-back cable between the Sockets) – With this configuration, if the secondary Socket stops receiving the HA keepalive messages, it becomes the Master regardless of the VRRP port state.
2. Via Switch – With this configuration, the VRRP port on both Sockets is connected to a switch. The failover behavior depends on the secondary Socket VRRP port state:
  1. When the secondary Socket port state is Connected but it doesn't receive keepalive messages – the secondary Socket becomes the Master.

The secondary Socket assumes that the state is caused by primary Socket failure.
  2. When the secondary Socket port state is Disconnected - the Secondary Socket does not become the Master (assuming that it is a local problem between itself to the switch.

The secondary Socket assumes that the primary Socket is operating correctly, and it does not become the Master to avoid a possible split-brain condition.

These are diagrams of the direct and via switch dedicated port configurations:

| ![Socket_HA_-_Direct_Port_for_HA_Traffic.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248037711005.png) | ![Socket_HA_-_via_Switch_Port_for_HA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248054222365.png) |
| --- | --- |

## Failover Conditions for Socket High Availability

The section describes the conditions that cause a failover from the primary Socket to the secondary Socket.

### Failover due to Primary Socket Failure

This failover scenario is caused by a failure to the primary Socket. The Socket is considered to be in a down state based on one of these reasons:

- General Socket failure or a loss of power
- VRRP connectivity (no keepalive for more than three seconds) A LAN-side connectivity loss does not trigger a failover unless VRRP advertisements are exchanged across the LAN link.
- No Internet connectivity for more than ten seconds

### Failover due to Keepalive Failure

There is also a failover scenario that is caused when the secondary Socket does not receive keepalive messages from the primary Socket for a period of three seconds.

When the secondary Socket discovers that the primary Socket is down, it then changes its status to Master. The Cato Cloud transfers the traffic flows to the WAN links in the secondary Socket. The following diagram shows this scenario.

![Socket_HA_LAN_Failure.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248022885789.png)

### Do Internet Connectivity Issues Cause Socket Failover?

The Sockets use a probing mechanism to determine the Internet connectivity status. If the primary Socket determines that Internet connectivity is down on all the Internet links (Cato links) for more than 10 seconds, then it stops transmitting the HA keepalive messages. This causes a failover to the secondary Socket.

> [!NOTE]
> Note:
> 
> It is possible for a situation where the primary Socket has Internet connectivity, however, all the DTLS tunnels are in the DISCONNECTED state. Because the Sockets have Internet and WAN recovery mechanisms, this situation does not trigger a failover to the secondary Socket. These recovery mechanisms allow the Socket to reconnect to a different PoP in the Cato Cloud.

## Monitoring Socket High Availability

This section discusses different pages in the Cato Management Application that you can use to monitor the status and events for Socket HA.

### Showing the Socket HA Status

There are different pages in the Cato Management Application that show the status of the Socket HA for a site.

| Page Name | Description | Path |
| --- | --- | --- |
| Sites | Shows all the sites in the account. The **HA Status** column shows the status of Socket HA for each site. | Network > Sites |
| Socket | Shows the details of Socket HA for a site. See above [Understanding Socket High Availability and Failover](/v1/docs/what-is-socket-ha#understanding-socket-high-availability-and-failover). | Network > Sites > *<site name>* > Site Configuration > Socket |
| Network Analytics | Shows network data for a site and the **HA Status**. | Network > Sites > *<site name>* > Site Monitoring > Network Analytics |

### Socket HA Failover Events

Whenever a Socket failover occurs, when the secondary Socket is active for more than 35 seconds, then a **Socket Fail-Over** event is generated. For example, if the primary Socket upgrades to a new Socket version, and the upgrade process takes 20 seconds, then a **Socket Fail-Over** event is NOT generated because the secondary Socket was only active for 20 seconds.

You can see the event in the Cato Management Application in the Home > Events page. Here is a sample event showing a failover from the primary to the secondary Socket.

![Failover.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248037992221.png)

## Defining Notifications for Socket High Availability Failover

You can use the Link Health Rule page (Network > Link Health Rules) to create a Connectivity Health Rule to send notifications for the Socket HA failover events.

Notifications are sent to all recipients defined in the Subscription Group that you configure in the CMA. A [Subscription Group](/v1/docs/creating-subscription-groups) can include different notification targets, such as:

- Mailing Lists with email addresses (including addresses not associated with Cato users or admins)
- [Webhook integrations](/v1/docs/sending-cma-notifications-via-webhooks) such as Slack or Jira
- Third-party notification systems

This lets you manage all notification destinations from a single location and apply them consistently across multiple rules.

This is a sample Connectivity Health Rule for Socket failover:

![Socket_Failover_Alert.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248023062173.png)

For more about configuring a Connectivity Health Rule, see [Working with Link Health Rules](/v1/docs/working-with-link-health-rules).
