---
title: "Part 1: The Socket Interfaces and Precedence"
slug: "part-1-the-socket-interfaces-and-precedence"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/part-1-the-socket-interfaces-and-precedence"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Part 1: The Socket Interfaces and Precedence

The Socket is responsible for both WAN and Internet traffic. You can assign each one of the WAN Socket’s interfaces to connect to a different ISP (Internet Service Provider) or MPLS over the last mile. This article focuses on the Socket deployment options and explains the relevant transport mechanism.

![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24708840284701.png)

## Working with Socket Interfaces and Precedence

The Cato Socket deployment defines how traffic is sent over the links. Use the Cato Management Application to configure the precedence for each Socket link to select the deployment for the site. These are the available deployments:

- Active/Active – both links with the same precedence for load balancing
- Active/Passive – both links with different precedence for redundancy
- More than two links – two or more different precedence for both load balancing and redundancy

For more about configuring precedence, see [Working with Socket Sites](/v1/docs/working-with-socket-sites).

### Active / Active – Interfaces with the Same Precedence

In active/active deployments, the Sockets establish DTLS tunnels to the Cato PoP and use SLA scores for smart bi-directional flow distribution to assure the best SLA for the traffic. The Socket calculates the score for each flow based on several parameters, for example, latency, MOS, packet loss, and more. The Socket then routes the traffic over the links based on the network policy.

If there is a problem detected for a link (such as port disconnection or degraded SLA), the Socket seamlessly transfers the traffic to another link, and keeps the flows alive and connected. Cato recommends implementing the active/active configuration for the best user experience and immediate real-time reaction to connectivity issues.

In the Cato Management Application, all links are configured with the same precedence – **1 (Active)**. The following diagram shows a Socket connected to the Cato Cloud with two active links:

![mceclip1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24708801163549.png)

### Active / Passive – Interfaces with Different Precedence

When a Socket is configured for an active/passive deployment, the Socket establishes DTLS tunnels to the PoP via all active and passive links. The Sockets and PoPs activate the passive links for traffic only after detecting connectivity problems on all active links. During this time, the precedence 1 and precedence 2 links operate in an active/active mode and use the smart bi-directional flow distribution to steer the flows over the link with the best SLA score. After a time period of 10 minutes, the Socket re-evaluates the SLA conditions and can deactivate the precedence 2 link.

The thresholds for activating passive links for traffic is defined by the SLA settings. For more information see [Configuring the Connection SLA Settings](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites).

> [!NOTE]
> Note:
> 
> The traffic over the passive link is used for monitoring link quality and performing PoP connectivity checks. If you use the passive link with a cellular LTE provider, you can configure it as a [precedence 3 (Last Resort) link](/v1/docs/configuring-a-last-resort-link) to preserve data usage by minimizing the control traffic.

The following diagram shows a Socket connected to the Cato Cloud with one active link and one passive link:

![mceclip2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24708801190557.png)

### Working with More Than Two Links

For deployments where you have more than two links for transport, you can implement an active/active/active or active/active/passive deployment. A sample active/active/passive deployment uses two active links connect to different ISPs and a passive link that connects to a 4G/LTE network. If the active links are disconnected or exceed the link SLA thresholds, the Socket then activates the passive link.

The following diagram shows one Socket with two active links and one passive link connected to the same PoP in the Cato Cloud:

![mceclip3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24708801218205.png)

## Understanding Active/Active Deployments

One of the Socket’s challenges in active/active deployments is to avoid splitting a connection flow between the active links. To solve the challenge, the Socket uses the stickiness method and distributes the traffic over the two active links based on flows instead of individual packets. Each flow is a network connection based on the following five-tuple that allows flows to stick with the initially chosen tunnel: source IP address, source port number, destination IP address, destination port number, and the protocol. When packets of a flow arrive to the Socket, they are sent over the same tunnel that was used when the flow was created.

For active/active deployments, the Socket considers both DTLS tunnels as one Multi-Tunnel. The Multi-Tunnel is a logical tunnel that holds all the information about the flows. If one tunnel disconnects, the Socket quickly restores the connection with the other tunnel and there is no impact for the end-user.

For more about the settings and thresholds for traffic in active/active deployments, see [Active-Active Traffic Distribution](/v1/docs/active-active-traffic-distribution).

### When Do the Flows Move Between Interfaces?

This section describes the cases when the Socket decides to move the flows from one active link to another.

#### Tunnel Disconnection

The Socket immediately moves flows to the other active link if it identifies that the tunnel is disconnected, either because there is 100% packet loss, or the Socket doesn’t receive responses for the keep-alive messages.

#### Port Disconnection

If the Socket identifies that the physical port is disconnected, for example if the network cable is unplugged, it immediately moves all flows to the other active link. When the connection is restored, the Socket calculates the SLA score for the link and gradually starts using it for new flows in active/active mode.

#### Better Transport

The Socket checks periodically for a better transport by calculating the SLA score based on the health metrics for each of the available transports. The metrics for the quality thresholds are: packet loss, latency, and jitter. For new flows in each direction, the Socket selects the best link based on the SLA score.

## Understanding Active/Passive Deployment

In active/passive WAN link deployments, the Socket uses the active links during normal operation, and only activates the passive link when the Socket or PoP detects a connectivity issue on all active links.

### When Does the Socket Activate the Passive Link?

The Socket activates the passive link if all active tunnels are disconnected, or they can't meet the Connection SLA thresholds.

#### Tunnel Disconnection

The Socket activates the passive link, when all active link tunnels go down or they all have 100% packet loss.

#### Port Disconnection

The Socket immediately activates the passive link, when all active ports are disconnected.

#### Poor Link Quality

If all active links don't meet the SLA link thresholds, the Socket activates the passive link. For more information about the SLA thresholds, see [Configuring the Connection SLA Settings](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites).
