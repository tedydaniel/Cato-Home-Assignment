---
title: "Alternative WAN Troubleshooting"
slug: "alternative-wan-troubleshooting"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/alternative-wan-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Alternative WAN Troubleshooting

## Overview

Alternative WAN (Alt. WAN) enables organizations to improve their network connectivity by offering flexible and resilient WAN traffic management solutions. It supports two types of configurations: Layer-2 for Sockets on the same subnet and Layer-3 for Sockets on different networks. For more details on deployment, refer to [Integrating-Cato-with-Alternative-WAN-Network](/v1/docs/integrating-cato-with-an-alt-wan-network).

This article covers common issues with Alt. WAN and provides troubleshooting steps to resolve them.

## Symptoms

Here are some common symptoms when Alt. WAN is not functioning as expected:

- The Alt. WAN connection fails to get established
- CMA shows the site as disconnected despite traffic flowing through Alt. WAN
- TLS Connection Reset by Server When Using Alt. WAN
- WAN recovery to Alt. WAN failed when the primary tunnel went down
- The BGP connection fails to be established through Alt. WAN

## Possible Causes

- Wrong Configuration
- UDP/20049 is blocked between Alt. WAN Sites
- High Socket CPU

## Troubleshooting the Issue

### Alternative WAN Tunnels Do Not Get Established

#### Review Configuration

- To ensure correct configuration, navigate to the Socket Site where the Alternate WAN is enabled. Go to **Network > Site > Socket** and verify that the **Port Status** for the Alternate WAN interface shows as **UP**.
- If the status displays **Down**, check the port connection to confirm it is properly connected to the network. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22956910173085.png)
- Ensure that the interface is configured with the correct option—either **Alternate WAN (Layer-2)** or **Alternative WAN (Layer-3)**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22983816847773.png)
- Next, confirm that the IP addresses and subnet settings are accurately configured. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22983845786909.png)
- To confirm that the Alternative WAN tunnels are active, access the Socket using the [Socket WebUI](/v1/docs/using-the-socket-webui-tools). If the Alternative WAN tunnels are successfully established, it will display the number of connected channels under the **SDWAN Tunnels**.
- . ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22958985729053.png)

#### Ensure UDP Port 20049 is Not Blocked

- The Alternative WAN tunnel is established over **UDP/20049**.
- Access the SocketUI of both Sockets and navigate to the Traffic Capture tab.
- Select the WAN interface that the Alt. WAN is configured and starts capturing for UDP protocol. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21913272403613.png)
- The PCAP should show bidirectional traffic on UDP port 20049. If you do not see bidirectional flow, check if any devices between the 2 sites is blocking UDP/20049.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21913283042589.png)**NOTE:** In the Alternative WAN Layer 2 configuration, the tunnel is initiated using the Alternative WAN IP. In contrast, with an Alternative WAN Layer 3 configuration, the tunnel is initiated using the local IP of the native subnet. The table below highlights the differences in traffic flow between Layer 2 and Layer 3 configurations, specifically focusing on the tunnel's source IP.

| **LAYER 2** | **LAYER 3** |
| --- | --- |
| ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22960352948637.png) The Alternative WAN tunnel will originate from the Alternative WAN IP. A packet capture from the Alternative WAN interface shows that the tunnel was initiated from IP address 192.168.20.2, establishing connections with the Alternative WAN IPs of the remote sites: 192.168.20.3 and 192.168.20.4. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22960344390429.png) | ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22960344394781.png) Although the Alternative WAN IP address is configured as 192.168.20.2 in the Socket UI, the Alternative WAN tunnel does not originate from this IP. A packet capture from the Alternative WAN interface shows that the tunnel instead originates from 192.168.2.1 and establishes connections with the native local IPs of the remote sites configured for Alternative WAN: 192.168.3.1 and 192.168.4.1. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22960344395805.png) |

### The Site is Disconnected in CMA Despite Traffic Flowing Through Alt. WAN

- The site appears disconnected in the CMA because the tunnel to the Cato Cloud is down.
- Traffic continues to flow through the Alt. WAN link ensures network operations, but the CMA registers the site offline because it cannot be reached.
- To restore visibility in CMA, troubleshoot and re-establish the tunnel connection to the Cato Cloud. For detailed troubleshooting steps, please see [Socket-Site-Tunnel-Connectivity-Troubleshooting](/v1/docs/socket-site-tunnel-connectivity-troubleshooting).

### TLS Connection Failure on Alt. WAN Links

- A network rule was explicitly configured to use Alt. WAN as the primary transport![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21913283042973.png)
- Checking the Socket UI shows that the Alt. WAN tunnel is up.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21913272404637.png)
- However, the server constantly resets the TLS application when it traverses using the Alt. WAN.
- In this scenario, it’s crucial to ensure that no complex network rule exists above the Alt. WAN rule due to how complex rules are processed within the network. A complex network rule is one that the Socket cannot evaluate directly. Therefore, when a complex rule appears above the Alt. WAN rule, the Socket sends the traffic to the PoP to determine the appropriate network handling.
- This process can result in an asymmetric flow when the return traffic traverses over the Alt. WAN link, ultimately causing the server to reset the connection.
- For more information on the complex rule, refer to [Explaining-the-Cato-TCP-Acceleration-and-Best-Practices,](/v1/docs/explaining-the-cato-tcp-acceleration-and-best-practices) under Section "*Working with Complex Network Rules*"
- Refer to [Solution to TLS Connection Failure on Alt. WAN Links](/v1/docs/alternative-wan-troubleshooting#solution-to-tls-connection-failure-on-alt-wan-links) on how to resolve this issue.

### WAN Recovery to Alt. WAN Didn't Occur When the Primary Tunnel Went Down

- By default, WAN recovery is not enabled for Alt. WAN. This is considered a limited feature, and if you would like to opt for it, you can send in your request to your Cato Representative.
- Refer to [Recovering-Connectivity-with-Alt-WAN-Links](/v1/docs/recovering-connectivity-with-alt-wan-links) for more details.

### BGP Fails to Establish Connection

- BGP peering has been configured between the customer’s BGP router and the Socket over the Alt. WAN link, but the BGP connection fails to establish.
- In this case, the Alt. WAN configuration on the Socket is as follows: ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21913283043485.png)
- The BGP router logs show that the next hop specified is invalid. One possible reason is that the next hop advertised in the BGP update is unreachable via the BGP peer.

```plaintext
%BGP-5-ADJCHANGE: neighbor 192.168.200.1 Up
%BGP-3-NOTIFICATION: received from neighbor 192.168.200.1 3/8 (invalid next hop specified) 4 bytes 0AFD0011
```
- A potential solution is to use the next-hop-self command in the BGP configuration. This command instructs the router to advertise itself as the next hop for routes, ensuring that the advertised routes have a reachable next hop IP address for the receiving BGP neighbor.
- Refer to [Solution to BGP Fails to Establish Connection](/v1/docs/alternative-wan-troubleshooting#solution-to-bgp-fails-to-establish-connection) for the details.

### Check Socket CPU Performance

- Consistent CPU utilization above 90% can negatively impact socket performance and cause packet loss and tunnels not established or frequent disconnections.
- To view historical CPU usage per core browse to Network Analytics and select the [Hardware](/v1/docs/showing-the-site-network-analytics) Tab. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25467347853469.png)
- For Real-time Socket CPU usage browse to the Socket WebUI and select the HW Status tab. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25467347857053.png)
- In Case of constant high CPU detected [contact Support](/v1/docs/submitting-a-support-ticket).

## Resolving Discovered Issues

### Solution to TLS Connection Failure on Alt. WAN Links

- A TLS connection between two Cato sites may fail when using an Off-Cloud or Alt-WAN link if a simple network rule is placed below a complex rule involving defined applications.
- This occurs because the TCP proxy is enforced, causing the TCP handshake to go through the Cato Cloud while the data packet traverses the Alt. WAN, leading to a connection reset.
- The solution is to move the simple Off-Cloud or Alt-WAN rule above any complex rules or, alternatively, to disable TLS inspection to avoid TCP proxy enforcement.
- For details on this issue, refer to [TLS-Connection-Failure-Over-Off-Cloud-or-Alt-WAN-Links](/v1/docs/tls-connection-failure-over-off-cloud-or-alt-wan-links)

### Solution to BGP Fails to Establish Connection

- The customer should ensure that the next hop for the default route is correctly configured on their BGP router. On the customer’s router, configure the default route using one of the following options:
  1. Use the next-hop-self command to set the next hop as the BGP neighbor’s alternate WAN IP:

```plaintext
neighbor <Socket Alternate WAN IP> next-hop-self
```
  2. Apply a route map to explicitly set the next hop to the router’s alternate WAN interface IP:

```plaintext
route-map <map-name> permit 10
    set ip next-hop <Router Alternate WAN Interface IP>
```

## Limitations/Notes

- When Alt. WAN is configured on a HA site, Alt. WAN tunnel is established only with the **Master** Socket. Therefore, under normal conditions, only the **Master** Socket will establish the Alt. WAN tunnel with remote sites.
