---
title: "Connecting Sites to the Cato Cloud"
slug: "connecting-sites-to-the-cato-cloud"
tags: ["Best Practices", "Networking", "Sites", "Sockets"]
updated: 2026-06-15T09:34:19Z
published: 2026-06-22T09:20:31Z
canonical: "knowledge.catonetworks.com/connecting-sites-to-the-cato-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connecting Sites to the Cato Cloud

This article discusses the different options to connect sites for physical offices and cloud-based data centers to the Cato Cloud.

## Cato SASE vs SSE Services

Cato offers two services to connect sites to the Cato Cloud, SASE and SSE. SASE is a comprehensive, cloud-native service that converges networking and security capabilities, while SSE focuses on security. For customers using SASE, they rely on our backbone for SD-WAN features. With SSE, customers can use a third-party network as their SD-WAN, which can integrate with Cato using IPsec solutions and rely on secure Internet connectivity from the Cato Cloud.

Cato Sockets provide significant advantages for holistic SASE services, including last-mile acceleration and optimal synchronization with the Cato PoP due to a shared code base. For more details, see below [Sockets vs IPsec Sites](/v1/docs/connecting-sites-to-the-cato-cloud-1#sockets-vs-ipsec-sites).

## Overview of Site Types

There are types of connections that you can use to connect a site to the Cato Cloud. Each connection type provides distinctive benefits and is chosen based on specific use cases, performance requirements, and existing infrastructure. These are the connection types for sites:

1. Cato Socket and vSocket - Easy to set up at physical premises and virtual cloud data centers.

The Socket is a proprietary Cato physical or virtual appliance that connects your office or data center to the Cato Cloud platform. There are different Socket models to fit the requirements of the specific physical sites and in addition, there are virtual Sockets (vSockets) for AWS, Azure, GCP, and VMware cloud data centers. Setting up the Socket is a quick and automated process, taking just a few minutes and no complicated configurations for physical or virtual devices. Advantages include:
  - The Socket and vSocket sites always connect to optimized PoP, and continuously monitor and calculate the best network performance for the site. For more information, see [Configuring the Connection SLA Settings](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites).
  - Recovery mechanisms - direct site-to-site connections ([WAN Recovery](/v1/docs/socket-site-resiliency-with-wan-recovery)) and [Internet Recovery](/v1/docs/using-cato-networks-internet-recovery).
  - Full support for active/active traffic.
2. IPsec Tunnel - Connect existing appliances and solutions to the Cato Cloud.

If you have existing third-party appliances like firewalls or routers, you can still connect them to the Cato Cloud using a secure IPsec tunnel. The appliance connects to a PoP in the Cato Cloud over the public Internet.
3. Cloud Interconnect Connectivity - Direct physical connections to data centers.

For physical and cloud-based data centers with a high volume of traffic, you can use Cloud Interconnect to directly connect them to the Cato Cloud. This option gives you a direct and fast connection to your data centers without any intermediate devices.

This table summarizes the different connection types:

| Criteria | Socket/vSocket | IPsec | **Cloud Interconnect** |
| --- | --- | --- | --- |
| **Tunnel Details** | DTLS encrypted overlay | IPsec encrypted overlay | Private link, no encryption |
| **Performance** | Up to 10 Gbps | Up to 3 Gbps | Up to 10 Gbps |
| **Analytics** | Full monitoring and visibility | Partial (e.g no packet loss visibility) | Partial (e.g no packet loss visibility) |
| **QoS** | Upstream and downstream | Downstream | Downstream |
| **High Availability Details** | Full HA – Up to 4 different tunnels, with recovery mechanisms | Full HA – Up to 3 different tunnels | Active/Passive – 2 different PoP Locations |
| **Limitations** | N/A | N/A | Only available at specific PoP locations BW must be 400 Mbps and higher |

## Sockets vs IPsec Sites

Sockets provide several advantages and features that are not supported by IPsec.

- **Last-Mile Optimization:** Sockets include these [traffic optimization](/v1/docs/accelerating-and-optimizing-traffic) features:
  - Packet size optimization - For example, we can tell the client the best TCP parameters to fit the MTU for the flow
  - TCP acceleration - reduce the RTT by involving the PoP as part of the communication between the client and server
  - MTU optimization - The Socket and the PoP continuously monitor and adjust the MTU for upstream and downstream traffic for the best performance
  - Packet loss mitigation - Duplicate packets so if there is packet loss, the data is still there. The duplicate packets are sent over the multiple links
  - Per-packet load balancing - For active/active configurations, a smart algorithm in the Socket monitors the links and determines the best route for the traffic
- **Improved Metrics and Visibility:** Sockets let you view extensive [metrics for network traffic](/v1/docs/site-monitoring-1) measured every second, including:

single pane of glass to monitor. IPsec requires comparing data in different consoles or apps. Includes historical data and real-time data.
  - Packet loss

(For IPsec, there is no ability to monitor packet loss)
  - Jitter
  - Distance
  - Latency
  - [Experience Monitoring probes](/v1/docs/configuring-the-experience-monitoring-probes-and-policy) (requires a separate DEM license)
- **Centralized Management:** The Cato Management Application handles all Sockets through a single interface, reducing complexity and ensuring consistency across all sites.

IPsec sites may require separate configuration and updates and could potentially have inconsistent settings and performance.
- **Better Performance and Stability:** Sockets dynamically connect to the best PoP location for optimal performance. If a PoP experiences performance issues, all Sockets will automatically switch to a different one.

IPsec connections are statically connected to one PoP location and don't offer this level of performance adaptability and are more likely to suffer from performance and connectivity issues.
- **Internet and WAN Resilience:** In the unlikely event that the Cato Cloud PoP is unavailable, Sockets have a backup mechanism, and the Sockets continue to provide Internet and WAN connectivity for the site.

IPsec doesn't provide the same level of resilience, potentially impacting your site's connectivity if there are PoP issues.
- **Simplified High Availability:** Two Sockets can operate in active/passive High Availability (HA) mode, ensuring continuous service in case of a failure related to the physical Socket.

HA for third-party appliances and solutions often requires an additional complex setup.
- **Improved Security:** Sockets automatically use encrypted tunnels for secure connections, reducing vulnerabilities and enhancing overall security.

While IPsec also offers secure connections, if not configured and managed correctly then it's liable to be more vulnerable.
- **Flexibility for Hybrid Environments:** Sockets can communicate through different transports, including MPLS or direct site-to-site tunnels, allowing flexibility in how your sites connect.
- **Bandwidth Management:** Sockets and the Cato Cloud apply end-to-end bandwidth management for all traffic types to ensure that critical applications receive the necessary bandwidth. Centrally manage the bandwidth policies and profiles in the Cato Management Application.

Sophisticated bandwidth management may not be as straightforward to implement with IPsec. Bandwidth management for IPsec sites is only for downstream traffic (from the Cato Cloud to the site).
- **Packet Loss Mitigation:** Cato's proprietary technology lets Socket intelligently optimize the Last Mile service and [mitigates packet loss](/v1/docs/packet-loss-mitigation-for-multi-tunnel-links) to provide a highly optimized network and improved user experience.

IPsec tunnels do not provide the same level of packet loss mitigation, potentially impacting network performance.
- **Managed Upgrade Service:** The Cato platform automatically manages upgrading Sockets to the newest version
  - Hands-free process that includes support for new features, performance enhancements, and security updates
  - Published vulnerabilities in the appliance infrastructure are also resolved as part of a version upgrade
