---
title: "Part 2: PBR and Network Rules within the Socket"
slug: "part-2-pbr-and-network-rules-within-the-socket"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/part-2-pbr-and-network-rules-within-the-socket"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Part 2: PBR and Network Rules within the Socket

## Overview of Routing Traffic with Cato

Controlling the traffic routing for your network helps you maximize the network performance, provide the best connectivity, and at the same time can minimize use of expensive network bandwidth. When you route the traffic correctly, you can guarantee that the specific traffic is sent over the best transport and link and it lets you optimize any application traffic based on the relevant requirements.

The **Network Rules** policy lets you easily configure rules and settings for each type of traffic. The rules in this window are an ordered rulebase and define the networking policy for your account. These are the categories of network rules:

- Internet rules that control the outbound traffic to the public Internet
- WAN rules that control the traffic over the WAN, and between sites or SDP users in your account

This article describes how you can use the Cato Management Application to configure routing with the network rules to best manage the traffic.

## Routing Traffic over Specific Networks

Cato supports different transport options for the traffic in your account and route certain traffic types over a specific transport. For example, accounts with Alternative WAN (MPLS or other layer 2 traffic), can choose to route all the VoIP traffic exclusively over this transport.

The following diagram shows an example of a deployment with multiple transport options:

![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248055013917.png)

The transport options for Socket sites are:

- **Cato** – The traffic that matches this network rule is routed over the Cato Cloud. The advantages of choosing the Cato transport is to apply all the Cato features to the traffic such as security rules, acceleration and QoS.
- **Alternative WAN** – This traffic is sent over the Alt. WAN (MPLS) links.
- **Off Cloud** - This traffic is sent using Socket to Socket direct VPN tunnels over the Internet with DTLS tunnels.

### Selecting a Transport Option

Use the Cato Management Application to configure the transport options for the network traffic. For each network rule you can select a primary and secondary transport option. The traffic is routed using the primary transport. If the primary transport is unavailable (for example when it’s disconnected), the Socket then routes the traffic with the secondary transport.

The example below shows the following rules:

- Rule 1 - Steering SMBv3 traffic between branches and the DC site over the off-cloud transport
- Rule 2 - Steering VoIP traffic between all the Socket sites over Alt WAN (MPLS) transport

![Transport_NetworkRules.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248055101085.png)

> [!NOTE]
> Note:
> 
> Cato designates a transport as *unavailable* if the link is disconnected, or if the link doesn’t meet the QoS quality thresholds. For more about configuring the link quality thresholds, see [Configuring the Connection SLA Settings](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites).

### Automatically Routing Traffic with the Best Available Transport

You can configure a rule to automatically use the best available transport based on available bandwidth and QoS parameters. Use the **Automatic** routing option to configure the Socket to compare the Cato and Alt WAN transport options and select the one that provides the best network performance. In the event that a link is overloaded, the Socket chooses a different link with better performance. However, you can’t select the **Interface Role** with the **Automatic** option. For more about the how Cato determines the best available transport, see below, [Selecting a Transport Option](/v1/docs/part-2-pbr-and-network-rules-within-the-socket#selecting-a-transport-option).

We recommend that you select **Automatic** for traffic types that are sensitive to latency but don’t require Cato features (such as security and acceleration) such as VoIP. The Socket can choose not to route the traffic through the Cato Cloud and these features can’t be applied.

> [!NOTE]
> Note:
> 
> When selecting the **Automatic** routing option, the Socket chooses either Cato or Alternative WAN. It doesn’t use the Off-Cloud option.

## Routing Traffic over the Socket Interfaces

The **Interface Roles** for a network rule let you configure how the traffic is sent over the Socket interfaces. You can configure a rule to only send the traffic type over a specific Socket interface. This section explains how to set the Interface Roles to provide redundancy and load balancing for a network rule. The following screenshot shows the Interface Roles settings for a network rule:

![mceclip2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248007719837.png)

### Achieving Redundancy and Load Balancing with Network Rules (Active/Active)

For active/active deployments that both links are connected with the same bandwidth, you can use the **Automatic** Interface Role to configure a network rule so that the Socket decides which link is the best connection for each flow. This rule automatically chooses the best interface to provide redundancy and load balancing for that traffic type. If each link is connected to a different ISP, and one ISP goes down or when the traffic doesn’t meet the QoS settings – then the Socket routes the traffic over the other link. In addition, if one link is experiencing traffic congestion, then the Socket load balances and sends the traffic over the other link.

For example, to configure the network rule to automatically choose the best interface - select **Cato** for the **Transport**, and **Automatic** for the **Interface Role**. The **Secondary Interface Role** isn’t relevant and is greyed out. The following screenshot shows a sample rule that automatically uses the best link:

![mceclip3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248055303453.png)

> [!NOTE]
> Note:
> 
> The Socket interfaces must be set to the same precedence for an active/active deployment. For more about configuring precedence, see [Working with Socket Sites](/v1/docs/working-with-socket-sites).

### Routing Traffic to Fail Over to an Interface

You can assign a primary and secondary interface for a network rule, if the primary interface is unavailable, then the traffic fails over to the secondary interface. For example, WAN1 is connected to one ISP with high bandwidth and WAN2 is connected to another ISP with low bandwidth. You can create a network rule that routes VoIP traffic over the high bandwidth link and only when the first link goes down, the Socket then routes this traffic over the low bandwidth link.

Configure the **Interface Role** for the network rule and set the **Interface Role** and **Secondary Interface Role** to different links. The following screenshot shows an example of a network rule with **WAN1** as the primary interface and **WAN2** as the secondary interface:

![mceclip4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248038813981.png)

### Planning Network Rules with Two Interfaces (Active/Passive Deployment)

For Socket sites that are configured with different precedence for the links (active/passive), traffic is only sent over the active link. If you configure a network rule with primary and secondary interfaces, it’s possible that the traffic that matches this rule is dropped. For example, if the Socket determines that the best available link is the secondary interface, and this interface is currently passive, then the Socket can’t send traffic over it. Instead the Socket drops the connections and doesn’t send the traffic. You can configure a rule with this behavior when the passive link is an expensive 4G/LTE cellular link. As a result, you minimize the amount of traffic that is routed to this link.

**Note:** If you configure a network rule to only route traffic over a specific interface, the Socket only sends traffic over this link when it is active. However, if the link is passive, then traffic that matches this rule is dropped. Once the link is active, the Socket resumes sending the traffic for this rule.

## Under the Hood – How does Cato Select the Best Transport or Link

When you set the routing for a transport or interface to Automatic, how do the Cato Sockets decide which one to use? The Cato Sockets use an algorithm that calculates a score to determine which is the best available transport and interface used for the traffic flow. The algorithm uses three kinds of objects, the Outlet, the Selector and the Entry.

The Outlet is responsible for checking all the transports and interfaces and determines which is the best transport to pass traffic. Each available transport is called an Entry and the Outlet compares all the Entries and gives each Entry a score based on the current network status and requirements. The Selector is a container that holds the list of the available Entries and the acceptable thresholds based on the network rules configuration. The Selector skips unavailable Entries such as a passive link.

This section explains how the algorithm selects a better transport or link for active/active and active/passive deployments.

The following diagram shows the Socket routing mechanism and how it routes traffic based on the network rules:

![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248007933213.png)

### Changing Transports or Links

The Outlet regularly checks to see if a better transport or link is available for the traffic flow. It compares the link quality for these metrics: packet loss, latency and jitter to calculate the score for the transport or link. The Outlet also compares the links of the current transport, to the other available transports. However, there is a preference to remain with the current transport instead of changing to a different one.

The behavior of the Outlet is different for the active/active and active/passive deployments.

#### Active/Active Deployments

In active/active deployments both links are available, so the Outlet compares the Entry scores every second. In addition, every four seconds the Outlet checks if the packet loss, latency, or jitter exceeds the quality threshold. If there is a better link, or the quality of the current link doesn’t meet the thresholds, then the traffic is changed to a different link.

When the Socket changes the transport or link for an existing flow, to prevent link flapping it waits before changing back to the original link. The amount of time that the Socket waits exponentially increases after each transport or link change. For example, the Socket changes from WAN1 to WAN2 and waits two seconds before comparing the Entry score of WAN1. After the next transport or link change, it waits 4 seconds, and then 16 seconds, and so on.

#### Active/Passive Deployments

In active/passive deployments, the passive link isn’t currently available for traffic flows, and the Outlet can only send traffic over this link when it becomes available. In other words, the Socket fails over to the passive link when there is a problem with the connectivity or quality of the active link. After the failover, the Outlet checks to see when the Socket can fall back to the original link.

Continue reading [Part 3 The Socket Traffic Prioritization and QoS.](/v1/docs/part-3-the-socket-traffic-prioritization-and-qos)
