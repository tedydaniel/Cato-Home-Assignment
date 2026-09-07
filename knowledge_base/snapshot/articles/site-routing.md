---
title: "Using BGP in the Cato Cloud"
slug: "using-bgp-in-the-cato-cloud"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/using-bgp-in-the-cato-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using BGP in the Cato Cloud

## Introduction to BGP

BGP is a standardized exterior gateway protocol designed to exchange routing and reachability information among autonomous systems (AS) on the Internet.

Based on your configurations and by leveraging BGP routing information, Cato Cloud can make informed real-time routing decisions without you being required to manually configured multiple static paths and/or take any actions. This enables enhanced support for scenarios such as direct connect and/or active-active configuration in AWS, disaster recovery (DR) with virtual IPs, integration with autonomous systems (AS) within sites, and greater flexibility in gradual deployments.

## How Does Cato Support BGP?

This section describes Cato’s BGP components (including global objects), and how Cato's support for BGP is designed and performs.

### Cato’s BGP Components

Cato BGP support is comprised of three main components: BGP neighbors, dynamic ranges, and floating ranges.

> [!NOTE]
> Note:
> 
> All ranges defined in a site's Native Range are referred to as “static ranges” throughout this section.

#### BGP Neighbors

Connectivity is required to establish BGP sessions with neighbors. These are the options for where a BGP neighbor can reside, and their resulting interaction with your account in the Cato Cloud.

- **BGP between Cato Networks PoP and a BGP router within a tunnel** - Cato advertises account ranges, including the default route (0/0), and receives static, [Dynamic Ranges](/v1/docs/using-bgp-in-the-cato-cloud#dynamic-ranges) and [Floating Ranges](/v1/docs/using-bgp-in-the-cato-cloud#floating-ranges) for a site. For example, BGP is the preferred mode for exchanging routes in an Amazon AWS IPSec connection.
- **BGP between the Cato Cloud and a BGP router residing on the LAN / Alt. WAN link** - Cato can communicate with a BGP neighbor over established ranges in the socket: direct ranges, native ranges, or VLAN ranges.

BGP sessions can be established over routed ranges only as long as all of the ranges have the same next hop as the BGP peer.

> [!NOTE]
> Notes:
> 
> - This option doesn’t rely on the establishment of a tunnel.
> - Cato assumes all BGP connections are “next-hop-self”: the neighbor is always the next hop selected by Cato, and Cato advertises its neighbor's IP as the next hop for all advertised routes.
> - When BGP is on the Alt. WAN, it usually receives other sites’ ranges (all other sites which are reachable via the Alt. WAN link). Cato filters these ranges before it considers dynamic and floating ranges.
> - When a Socket is disconnected from the Cato Cloud, all other site ranges are withdrawn. This allows continued reachability in a case where the BGP peer has a secondary path that can be alternatively used as a next hop if it temporarily disconnects from the Cato Cloud. (Supported from Socket version 17.0 and higher)

For more about configuring a BGP neighbor, see [Defining BGP Neighbors](/v1/docs/preparing-to-implement-bgp-neighbors-with-cato).

#### How are BGP Connections Established

There are several stages to establishing the BGP connection. Depending on your connection type, BGP connections are established as follows:

- An initial TCP session is started. If the TCP session cannot be established, an attempt is scheduled every 30 seconds until the session is successfully established
- A BGP session is started immediately after the TCP session is established
- If the BGP session cannot be established, an attempt is scheduled every 15 seconds
- If a BGP session is terminated after it's been established, the next attempt is scheduled every 1 second

#### Dynamic Ranges

Dynamic ranges are IP ranges that are dynamically learned by Cato from a BGP neighbor. Once accepted by Cato, they are propagated throughout an account will become reachable via that neighbor from anywhere in the network.

> [!NOTE]
> Note:
> 
> Since dynamic ranges are dynamically learned from the BGP neighbor and cannot be configured as global objects in the Cato Management Application, they cannot be used explicitly in network and/or security rules, and therefore behave according the policy of the site they reside in.

#### Floating Ranges

Floating ranges are global IP ranges that are not connected to a specific site, but can be learned from any site with a BGP neighbor. For example, in a Disaster Recovery (DR) scenario, many applications (such as VMware NSX) can move servers from one location to the other while maintaining their IP addresses. In these cases, BGP helps to update the remaining network objects and advertises where these servers now reside.

Floating ranges are defined as global objects. Floating Ranges are not associated with a particular Site and must be defined in Security or Networking rules (Site association can change dynamically). You can leverage the global object definition to explicitly create network and/or security rules as per your organization policy requirements.

In order for a BGP dynamic range to inherit the security or network policy for a floating range, it must exactly match the floating range. For example, if the BGP dynamic range is 192.168.1.0/24 and the floating range is defined as 192.168.1.1/32, then there is no connection between them and the BGP dynamic range doesn't inherit the policies from the floating range.

> [!NOTE]
> Note:
> 
> Floating Ranges cannot overlap with static ranges.

### How BGP in Cato is Designed and Performs

#### Handling Routes

The BGP neighbor in the Cato Cloud is connected with a Cato PoP or with the site connection. The site connection can be a Socket or an IPsec tunnel. When the Cato Cloud receives a new or updated BGP route, it always synchronizes with the global WAN network (site connections and PoPs).

When a BGP route is received, Cato associates it with the relevant object as follows:

- IP ranges defined as floating ranges are associated with their defined objects and adhere to all networking and security policies assigned to the objects.
- All other IP ranges are considered as dynamic ranges, and adhere to all networking and security policies assigned to the site.

Routes can be withdrawn through a BGP message or through a neighbor disconnect (CEASE or physical), and Cato Cloud immediately propagates the withdrawal.

#### Tunnel Metrics over Cato (Routing Table)

Sites in Cato, such as IPSec or Socket sites, may have multiple connected tunnels for sending traffic over the LAN or the Internet. If multiple tunnels are connected, their priority is based on the link quality and other factors. The [Routing Table](/v1/docs/showing-the-routing-table-for-your-account) screen (Monitoring > Routing Table) shows the **Tunnel Metric** for the routes. This is the value that Cato assigns to make sure that traffic is sent over the best tunnel. The lower the value for **Tunnel Metric** indicates that this tunnel has a higher priority. For example, in a Socket High Availability deployment the active tunnel can have a metric of 5 and the tunnel from the passive socket has a metric of 10.

#### How Routes are Prioritized

In contrast to regular static ranges, BGP allows multiple routes that may overlap or even be duplicated across parts of your network. So how does Cato Cloud decide through which path to route packets?

When multiple routes can be applied to a destination IP address, routing decisions will be performed according to the following priorities:

1. More specific routes are selected over less specific routes (/24 over /22 and so on).
2. The order of preference for the following IP ranges:
  1. Static ranges
  2. Floating ranges
  3. Dynamic ranges
3. Lower Neighbor Metric is preferred.
4. Shortest AS-PATH is preferred.
5. Lower Tunnel Metric is preferred.
6. Lower BGP MED (Multi-Exit-Discriminator) from the route ID is preferred.

Since Cato Cloud performs Layer-7 Policy-Based Routing, the need to avoid asymmetric routes is decisive. For that reason, route priority is universal within the same account: in other words, a single origin will be selected from any location within the Cato Cloud network.

#### How Routes are Propagated

When routes are accepted by a BGP neighbor, information associated with it (AS-path, BGP-communities) is preserved. When dynamic ranges are advertised to BGP neighbors, the AS-Path will be appended with the Cato Cloud AS number (as usual with BGP).

Cato transparently propagates all Path Attributes marked with Transitive flag (RFC 4271), including communities.

Account ranges (static) are advertised with the Cato Socket Neighbor ASN as the originating ASN (Autonomous System Number - see below [Assigning an ASN to a Neighbor](/v1/docs/using-bgp-in-the-cato-cloud#assigning-an-asn-to-a-neighbor)).

For more about BGP route summaries, see [Working with BGP Summary Routes](/v1/docs/working-with-bgp-summary-routes).

> [!NOTE]
> Note:
> 
> Some well known communities are not propagated by Cato to BGP neighbors on egress, such as no-export.

#### Assigning an ASN to a Neighbor

The ASN is a number between 64,512 – 65,534 (private ASN), which represents the routing entity establishing the communication. Cato Networks’ default ASN is 64,515.

Cato Cloud supports eBGP, so a BGP Neighbor must have a different ASN than the Cato Cloud side.

> [!NOTE]
> Note:
> 
> It is a best practice to globally use a single ASN to represent the Cato Cloud side of communication across all BGP sessions. If you are considering using different ASNs across different neighbors, please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).

**How Loops are Prevented**

When a route is received by Cato, the AS path is scanned for the Cato Cloud ASN of the neighbor. Any route containing this ASN will be discarded. Note that the neighbor only scans the current neighbor’s ASN.

> [!NOTE]
> Note:
> 
> Cato doesn't support Graceful Restart.

#### Security and Networking

Dynamic ranges are automatically associated with the site from which the route was received, and inherit all the site’s policy groups, network and security policies. Floating ranges are defined globally and security rules are applied to them directly, or by associating them with policy groups.

### Before You Begin Using BGP

Which site Connection Types can I use?

- Cato supports BGP for sites that use Sockets, vSockets, and IPsec sites (Cato-initiated IPsec IKEv1, IPSec IKEv2). In addition, there must be requires connectivity with your existing BGP routers.

How will the BGP neighbor establish the BGP session with Cato?

- BGP sessions require established connectivity between a BGP neighbor and a site over local routes in sockets or over an IPSec tunnel.
- For Cato Socket deployment, only direct, VLAN and native ranges can be used for establishing sessions

BGP sessions can be established over routed ranges only as long as all the ranges have the same next hop as the BGP peer.

**Setting BGP Sessions over Alternative WAN links**

In Cato, Alternative WAN destinations include two (potentially VLAN-tagged) networks: public and private. A BGP neighbor must be within one of those two networks, and the BGP neighbor on the Cato Cloud side will be the corresponding Cato IP for that range.

When defining a BGP session over a public interface, you can also perform Source NAT on traffic going through that link. This means that for all outgoing traffic via that neighbor, the source address will be the Cato-side IP.

## Known Limitations

- The Cato Cloud only supports IPv4.
- If multiple ASNs are configured for multiple neighbors, the ASNs will not be detected by the neighbor and looping may result.
- The Cato Cloud allows propagation of routes containing the neighbor's ASN, relying on the neighbor to scan for loops.
- Floating Ranges cannot overlap with a static range.
- Cato does not support Graceful Restart for route withdrawal.
- BGP route changes (including route withdrawal) that are initiated by Cato, don't generate events.
- Cato does not perform route summarization.
- By default, Cato limits the number of received prefixes from each BGP neighbor to 1024. To increase this limit, contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).
- BGP isn't supported for accounts that use static range translation. If you require BGP for a translated Native Range for a Socket site, please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).
