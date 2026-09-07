---
title: "Why Can't I Ping the Secondary PoP For My IPSec HA Site?"
slug: "why-can-t-i-ping-the-secondary-pop-for-my-ipsec-ha-site"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/why-can-t-i-ping-the-secondary-pop-for-my-ipsec-ha-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Why Can't I Ping the Secondary PoP For My IPSec HA Site?

## Question

For an IPSec site that has set up primary and secondary tunnels for high availability (HA), when both tunnels are up, why can I ping only the primary PoP and not the secondary PoP from my Firewall (VPN gateway)?

## How Routing Works

As mentioned in [Cato Socket vs IPsec Sites and Tunnels](/v1/docs/cato-socket-vs-ipsec-sites-and-tunnels), IPsec sites only support Active-Passive configurations. This means that even when both primary and secondary tunnels are established, traffic will only be sent over the primary tunnel. Before answering the question of why ping to secondary PoP will fail when both tunnels are up, it is essential to understand how routing works for such deployment.

### Both Tunnels Established

#### Upstream Traffic (Site to PoP)

For an IPSec site running HA, the customer's firewall decides which tunnel to use for traffic. It is recommended that a routing protocol, BGP, be enabled so that it will route the traffic through the preferred (primary) tunnel.

#### Downstream Traffic (PoP to Site)

The PoPs detect incoming traffic on the primary tunnel and, hence, return the traffic through the same tunnel. This is done to prevent asymmetric routing.

### Primary Tunnel Down

#### Upstream Traffic (Site to PoP)

The customer's firewall detects that the primary tunnel is down and will direct all traffic to the secondary tunnel. If BGP were running at the site, it would detect that the primary uplink is down and dynamically route traffic through the secondary tunnel.

#### Downstream Traffic (PoP to Site)

The PoPs detect incoming traffic on the secondary tunnel and, hence, will also return the traffic through the same tunnel.

## Answer

To verify connectivity and proper setup of the IPSec tunnels, the customer may ping the remote PoP IP from the respective tunnel. However, when both tunnels are up and if the ICMP **ping was performed from the secondary tunnel** to the secondary PoP IP address, the PoP will not return the ICMP response since the return flow should be through the primary tunnel.

To verify connectivity and proper setup on the secondary tunnel, enabling BGP and pinging the secondary BGP (private) IP is recommended. For configuration details, refer to [Configuring-BGP-Neighbors-for-an-IPsec-Connection](/v1/docs/configuring-bgp-neighbors-for-an-ipsec-connection).
