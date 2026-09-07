---
title: "Socket Site Resiliency with WAN Recovery"
slug: "socket-site-resiliency-with-wan-recovery"
tags: ["Best Practices", "Sockets"]
updated: 2026-07-28T22:48:41Z
published: 2026-07-28T22:48:41Z
canonical: "knowledge.catonetworks.com/socket-site-resiliency-with-wan-recovery"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Site Resiliency with WAN Recovery

This article discusses the WAN Recovery feature for Socket sites that provides resiliency in the very unlikely circumstance that there is a connectivity issue with the Cato Cloud.

## Overview of WAN Recovery

The WAN Recovery feature is one of multiple recovery options that provide resiliency if your Socket sites can't communicate using the Cato Cloud. WAN Recovery uses VPN tunnels between Socket sites over the Internet to preserve the connectivity for the WAN traffic between your sites if there is a connectivity issue with the Cato Cloud.

### How Does WAN Recovery Work?

WAN Recovery is based on a full mesh topology and is enabled by default for all Socket sites. Each Socket creates a direct DTLS tunnel to every other one over the public Internet. They regularly send keep-alive messages over the tunnel and keep an open live tunnel to reduce the recovery time. This topology provides maximum resiliency for the Socket sites in your account.

The following diagram shows an example where one Socket is disconnected from the Cato Cloud. WAN Recovery is enabled for that site to provide a direct connection between the two Sockets:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/01_recovery.png)

WAN Recovery is a critical component of Cato Cloud resilience and maintaining connectivity for sites. For more information, see these videos:

- [Best Practices for WAN Recovery](https://academy.catonetworks.com/best-practices-for-wan-recovery)
- [Improved WAN Recovery](https://academy.catonetworks.com/improved-wan-recovery)
- [WAN Recovery Status in the CMA](https://academy.catonetworks.com/wan-recovery-status-in-the-management-application)

### Site Static Port and WAN Recovery

To ensure the smoothest transition for sites to WAN Recovery, you can use a static IP for the site and define the Socket interface Public IP and Static Port settings for a site to improve establishing the off-cloud tunnels between the sites.

For accounts where it is difficult to configure the static IP settings for all the Sockets, we recommend that you use static IP settings for a few key sites, such as data centers, that act as hubs for WAN Recovery. The IP address for the hub sites is sent to the PoPs and propagated to the other Sockets in your account that are configured for WAN Recovery.

### Using Hub & Spoke Topology

Full mesh topology for WAN Recovery is primarily suitable for small and medium deployments, however, this behavior generates unnecessary traffic and increases CPU load in large-scale environments. For these environments, you can transition to a hub & spoke topology to reduce the number of tunnels and probes, maintaining optimal performance and efficiency. For more information, see [Hub & Spoke Off-Cloud Topology for WAN Recovery](/v1/docs/hub-spoke-off-cloud-topology-for-wan-recovery).

### WAN Recovery for China Sites

China Socket sites support communication via off-cloud direct tunnels. This allows for routing high-volume traffic directly between sites within China and business continuity use cases.

## Recovering WAN Traffic

The Socket keeps an open tunnel for WAN Recovery, so if it loses connectivity with the Cato Cloud, the Socket recovers the connections with the other sites and minimizes the disconnection time. The Socket then immediately starts sending the WAN traffic over the WAN recovery link.

You can use the Cato Management Application (CMA) to disable the WAN Recovery either for a specific site or for the entire account. For more information, see [this article](/v1/docs/working-with-advanced-configuration-for-the-account).

Once connectivity to the Cato Cloud is restored, recovery ends, and the traffic is sent over the Cato Cloud.

### Configuring Sites for WAN Recovery

We recommend that you use static IP addresses for key sites, such as data centers, that act as hubs for WAN Recovery. Define the off-cloud **Public IP** and **Static Port** for each WAN link in the hub sites.

You can use the [Posture page](/v1/docs/reviewing-posture-checks-for-your-account) to confirm that all sites are enabled in the Advanced Configuration settings to support WAN Recovery.

**To configure a site for WAN Recovery:**

1. From the navigation menu, select **Network > Sites**, and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Configure the WAN link for WAN Recovery:
  1. Click the WAN link. The **Edit Socket Interface** panel opens. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/02_recovery.png)
  2. Set the **Traffic Status** to **Enabled**.
  3. **(Optional)** Define the static **Public IP** and **Static Port** for the link.

**Best Practice:** We recommend that you configure this setting for key hub sites.
4. Repeat step 3 for all Socket WAN links.
5. Click **Apply**, and then click **Save**.

The site is configured for WAN Recovery.

### Analyzing WAN Recovery Events

WAN Recovery events are generated when a site sends traffic to another site using the DTLS tunnels over the Internet instead of the Cato Cloud. The CMA shows the following events for WAN recovery:

- Off-Cloud Recovery Activated - this event is generated when the Socket starts to send the WAN traffic over the WAN Recovery transport.

- Off-Cloud Recovery Stopped - this event is generated when the connection to the Cato Cloud is restored, and the Socket stops sending WAN traffic over the WAN Recovery transport.

Events are not generated when WAN Recovery is functioning for a site (status is **Ready**), but the site isn't sending traffic over the recovery DTLS tunnels.

## Monitoring WAN Recovery Status

The CMA provides visibility into the WAN Recovery readiness of your Socket sites. You can proactively identify sites with issues that are preventing WAN Recovery and take corrective actions to maintain WAN resiliency.

**Best Practice:** Configure each WAN interface with a static or dynamic IP address to ensure reliable tunnel detection and accurate status reporting.

You can monitor WAN recovery in the **WAN Recovery Tunnels** column on the Network > Sites page. The real-time status for each site indicates the readiness state of the WAN links for WAN recovery:

- Ready (X/X): This site is for WAN Recovery and connected to all Socket sites
- Partial (X/Y): Site is partially ready for WAN recovery (i.e., 16/20 means that this site is connected to 16 of 20 sites for WAN recovery)
- Not Ready (0/Y): This site is not ready for WAN Recovery, and it is not connected to any Socket sites. This site will lose WAN connectivity if there is an outage with the Cato Cloud

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/03_recovery.png)

**To review the WAN Recovery status for all sites:**

- From the navigation menu, select **Network > Sites**, and review the status in the **WAN Recovery Tunnels** column.

You can also see the status for a specific site in these pages:

  - Home > Topology and select a site
  - Site Configuration > {site name} > Socket

### Remediating Partial or Not Ready Status

If a site shows a **Partial** or **Not Ready** status, take the following steps to restore full recovery readiness:

1. Verify WAN Interface Settings: Ensure that each WAN interface has a valid static or dynamic IP address and that the WAN links are operational.
2. Check Tunnel Establishment: Use the CMA or the Socket WebUI to confirm that off-cloud tunnels are created and maintained with remote sites.
3. Troubleshoot Local Network Issues: Investigate possible causes such as:

  - Inbound/outbound firewall rules are blocking traffic
  - Incorrect NAT behavior or port restrictions
  - Routing misconfigurations
4. Apply Best Practices: Where feasible, configure static WAN IPs on critical sites (e.g., data centers or hubs) to enhance tunnel stability and status accuracy.

### Known Limitations for Monitoring WAN Recovery

- Site-Specific Issues: A **Not Ready** status usually indicates a local issue at the site (such as WAN link failure, configuration issues, or IP assignment problems) rather than problems with remote sites.
- Mesh Visibility Scope: The status reflects the overall tunnel mesh between sites. It does not immediately show which specific tunnels are down. You may need to investigate per site or interface.
- Network Conditions: Temporary network issues, NAT behavior, or firewall rules may interfere with tunnel establishment and delay or impact status accuracy.

## Impact on the Account During WAN Recovery

WAN Recovery is enabled by default for all Socket sites to provide resiliency using off-cloud traffic. If it is disabled for one or more sites, those sites can't communicate with the others during WAN Recovery. For example, if WAN Recovery is enabled on Sites A and B, but not on Site C, then during WAN Recovery, Site C can't communicate with Sites A and B, and Sites A and B can't communicate with Site C.

The [LAN Firewall policy](/v1/docs/what-is-the-socket-next-gen-lan-firewall) is not impacted and continues to function normally during WAN Recovery because the Socket enforces the policy locally.

### Don't Reboot the Socket

During WAN Recovery, do **not** reboot the Socket. Rebooting the Socket during WAN Recovery can negatively impact the site and prevent it from re-establishing connectivity with the other sites.

### WAN Recovery in Active/Active or Active/Passive

For all deployments, when WAN Recovery is enabled, each Socket establishes secure DTLS tunnels to remote Socket sites on all WAN interfaces that are enabled for off-cloud traffic. In an active/active deployment, the Socket randomly selects one of the active WAN links for WAN Recovery. In an active/passive deployment, the Socket uses the active WAN link.

### Impact on the CMA During WAN Recovery

The Cato Management Application (CMA) does not receive complete site data during WAN Recovery because the impacted sites are no longer connected to the PoP.

You can log in to the [Socket WebUI](/v1/docs/accessing-the-socket-webui) and use the **SD-WAN** tab to monitor traffic and off-cloud tunnels. The following example shows traffic monitoring in the Socket WebUI:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/04_recovery.png)BGP and WAN Recovery

During WAN Recovery, the Socket routing table is frozen, which means that all BGP ranges that existed before the recovery started will be routable via the off-cloud traffic to other sites. BGP ranges that are introduced after the WAN Recovery started are unreachable until the Socket exits recovery and reconnects to the PoP.

### PoP Limitations During WAN Recovery

Traffic that is passed over the WAN Recovery off-cloud transport isn’t processed by PoPs in the Cato Cloud. This means that during WAN Recovery, the PoP services are not applied to traffic, including the following items:

- Security

  - WAN and Internet firewall policies
  - Threat Prevention services (ie. IPS, Anti-Malware)
  - Managed XDR services
- Networking

  - NAT policy
  - Complex Network Rules
  - DNS Forwarding
  - DHCP Relay
  - Static Range Translation (SRT)
- Access

  - Client Access (ie. Client Connectivity policy)
  - Device Posture

## WAN Recovery and Alt. WAN Recovery

For accounts that enable [recovery via Alt. WAN](/v1/docs/recovering-connectivity-with-alt-wan-links) (ie. MPLS), if the Socket disconnects from the Cato Cloud, the Alt. WAN link has a higher priority than WAN Recovery. Therefore, the Socket first moves the traffic to the Alt. WAN link. If the Alt. WAN link is unavailable, the Socket then moves the WAN traffic to the WAN Recovery link. Generally, the WAN Recovery has the lowest priority as a transport option, and it’s only used when the other transport options are unavailable.

## Understanding NAT Punching to Connect Sockets

WAN Recovery relies on NAT punching to establish the WAN connectivity between your sites. When a Socket connects to the Cato Cloud, the PoP informs the Socket of all the other endpoints, and the Socket opens a DTLS tunnel to each one of them. The Socket uses the NAT punching technique to establish a direct connection with the other Sockets.

**Note**: The negotiation of the NAT punching starts over the Cato Cloud. Therefore, the Sockets must be connected to the Cato Cloud to allow the NAT punching.

The following diagram shows the flow to establish a direct connection between two Sockets for WAN Recovery:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/05-recovery.png)

The NAT punching technique works for each pair of Sockets in the following way:

1. The PoP selects one of the Sockets as the initiator to establish a direct connection (Socket 1) based on the site ID (the site with the highest ID value is the initiator).
2. The initiator Socket sends a request to the Cato Cloud for the following details: IP address and port number, for example, IP address 82.128.1.1 and port number 4444 (Step #2)
3. The Cato PoP sends the source IP address and port to Socket 1
4. Socket 1 sends its IP address and port to Socket 2 over the Cato tunnel
5. Socket 2 sends a request to the Cato Cloud for the following details: IP address and port
6. The Cato PoP sends the source IP address and port to Socket 2
7. Socket 2 sends its IP address and port to Socket 1 over the Cato tunnel
8. Socket 1 sends 32 packets to Socket 2 in the range of the source port, each packet with a different port number
9. Socket 2 sends 32 packets to Socket 1 in the range of the source port, each packet with a different port number
10. Once the correct port is found, the Sockets open a DTLS tunnel with the source IP address and the port number

When Socket 2 connects with Socket 1, the router adds the NAT entry to its routing table
11. From that point on, the Sockets send keep-alive messages every 15 seconds to keep the connection open

### Minimizing Reconnection Time with NAT Punching

After NAT punching succeeds, the Socket saves this NAT data. In the case of a Socket restart, it can immediately reconnect to the other Sockets with that NAT data. Saving the NAT data significantly reduces the Socket reconnection time. For Sockets that are behind a network firewall or a router, if your firewall or router restarts, the NAT entries are changed. The NAT data is no longer relevant, and the Sockets must perform the NAT punching process again.
