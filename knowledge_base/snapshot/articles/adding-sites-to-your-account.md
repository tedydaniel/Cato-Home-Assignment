---
title: "Site to Site WAN Connectivity with the Cato Cloud"
slug: "site-to-site-wan-connectivity-with-the-cato-cloud"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/site-to-site-wan-connectivity-with-the-cato-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Site to Site WAN Connectivity with the Cato Cloud

After completing the basic provisioning process, sites and SDP users establish secure connectivity to the Cato Cloud. The routing information of all sites and SDP users is managed by the Cato Cloud in a shared routing context. This allows layer-3 connectivity between all sites and SDP users connected to the account.

![Topology_WAN_transport.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275578117661.png)

All the routing information between sites and SDP users is shared through a single routing table in the Cato Cloud.

![routing_table.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275619232285.png)

You can use the Network policy to apply specific settings for the WAN traffic such as QoS bandwidth management priority, TCP optimization, and so on. For more information, see below [Using the Network Policy to Steer Traffic over Different Transports](/v1/docs/site-to-site-wan-connectivity-with-the-cato-cloud#using-the-network-policy-to-steer-traffic-over-different-transports).

## Managing the WAN Connectivity Policy Using the WAN Firewall

To manage the connectivity policy for the WAN traffic, configure WAN Firewall rules to allow or block communication between sites, users, hosts, and so on. This identity-based and application aware policy provides all the needed granularity to manage the WAN traffic.

For more information about Cato's WAN firewall, see the relevant articles in [Internet & WAN Firewalls](/v1/docs/cato-firewalls).

## Establishing Site to Site WAN Connectivity Using Additional Transports

In addition to the default transport over the Cato Cloud, there is an option for creating site to site tunnel meshes over the Internet and MPLS transports.

For more information, see [Routing Traffic to an Off-Cloud Link](/v1/docs/routing-traffic-to-an-off-cloud-link).

### Establishing Site to Site Connectivity over the Internet Transport (Off-Cloud)

The site to site off-cloud connectivity for Socket sites uses Socket to Socket direct VPN tunnels over the Internet with DTLS tunnels. The Sockets automatically discover each other over the Internet transport, and create a full mesh topology with each other. For example, when there are regular backups between branch sites and the data center site in the same region, you can configure network rules to steer this backup traffic to use the off-cloud transport.

By default, all Socket sites are preconfigured for the off-cloud transport, on precedence 1 and 2 links and this allows the auto-discovery process to take place automatically without any user configuration. You can disable off-cloud transport for specific sites or links within a site, to prevent the site from joining the off-cloud tunnel mesh.

Configure the network policy to control the traffic that uses off-cloud as the transport.

The following example shows the **data-center** site has established point to point tunnels to other sites via the Internet (off-cloud) transport

![off_cloud_monitoring.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275619329821.png)

### Establishing Site to Site Connectivity over the MPLS Transport (Alt. WAN)

Another option for establishing WAN connectivity between sites, is to use the MPLS transport (Alternative WAN). Each site that is configured for the MPLS transport, automatically discovers all remote sites that have a similar configuration. Point to point VPN tunnels are automatically established between all relevant Socket sites over the MPLS transport.

## Using the Network Policy to Steer Traffic over Different Transports

The Cato Cloud is the default WAN transport option for all Socket sites as defined in the Network policy. Alternatively, you can configure granular Network rules for specific sites, applications, groups, hosts, and so on, and select an alternative transport option, such as off-cloud or Alt WAN.

The example below shows the following rules:

- Rule 1 - Steering SMBv3 traffic between branches and the DC site over the off-cloud transport
- Rule 2 - Steering VoIP traffic between all the Socket sites over Alt WAN (MPLS) transport

![Transport_NetworkRules.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275603204381.png)

For more about configuring Network rules, see the relevant articles in [Network Rules & QoS](/v1/docs/network-rules-qos).
