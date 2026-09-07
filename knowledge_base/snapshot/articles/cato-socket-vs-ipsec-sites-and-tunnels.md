---
title: "Cato Socket vs IPsec Sites and Tunnels"
slug: "cato-socket-vs-ipsec-sites-and-tunnels"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/cato-socket-vs-ipsec-sites-and-tunnels"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Socket vs IPsec Sites and Tunnels

Customers often ask, which types of site is better - Cato Socket or IPsec. Cato always recommends that you use **Socket** deployments for a site.

These are some advantages that a Socket provides over an IPsec site.

For more information about comparing Socket vs. IPsec sites, please see [Connecting Sites to the Cato Cloud](/v1/docs/connecting-sites-to-the-cato-cloud).

## Cato Socket Sites

1. Sockets include optimized PoP selection. This lets the Socket automatically connect to the best available PoP which minimizes network latency.
2. If there's a connectivity issue with the current PoP, Sockets automatically connect to the next optimal PoP.

Sockets with one link keep connectivity to the Cato Cloud if there's an issue with the current PoP.
3. Sockets include QoS services for upstream and downstream traffic.
4. Includes various Last Mile Monitoring tools and analytics.

## IPsec Sites

1. IPsec sites are statically assigned to a specific PoP. If there is a connectivity issue with the current PoP, the site can be disconnected.

**​IMPORTANT:​​** We strongly recommend that you configure a secondary tunnel (with different Cato public IPs) for high availability. Otherwise, there is a risk that the site can lose connectivity to the Cato Cloud.
2. Due to different implementations of the IPsec protocol, IPsec sites can experience connectivity issues.
3. QoS is applied for traffic in the downstream direction (from the Cato Cloud to the site). The PoP makes a best effort to apply QoS for upstream traffic.
