---
title: "Configuring Sites with IPsec Connections"
slug: "configuring-sites-with-ipsec-connections"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/configuring-sites-with-ipsec-connections"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Sites with IPsec Connections

You can use IPsec tunnels to connect sites and the internal networks to the Cato Cloud and remote networks. Generally sites with IPsec connections are used for:

- Sites that are in a public cloud such as AWS and Azure
- Sites for offices that use a 3rd party firewall

The Cato Cloud supports IPsec connections for IKEv1 and IKEv2. We recommend that you use IKEv2, however some technologies only support IKEv1.

For Cisco ASA appliances, there is a known incompatibility with Cato IKEv2 sites, see [Configuring IPsec IKEv2 Sites](/v1/docs/configuring-ipsec-ikev2-sites).

For FTP traffic, Cato recommends configuring the FTP server with a connection timeout of 30 seconds or higher.

## Selecting the IPsec IKEv1 Connection Type

The IPsec IKEv1 Connection Type for IPsec IKEv1 is Cato-Initiated. The Cato Cloud is responsible for creating the IPsec connection to the site. If the connection goes down, then the Cato Cloud attempts to re-establish it

## Configuring the Native Range

The native range for a site is the IPv4 address (and CIDR) for the primary LAN network that is behind the firewall or router device.

You can configure the native range settings in Network > *<site>* > Site Configuration > Networks. You can also use this section to configure additional network ranges for the site.

## Configuring the VPN Tunnels

IPsec sites support a primary and an optional secondary VPN tunnel. You can configure each tunnel to connect to a different PoP to provide resiliency. However, unlike Cato Sockets, IPsec connections do not automatically connect to different PoPs if there is a problem. They can only connect to the Destination IP address that is configured for each tunnel.

> [!NOTE]
> IMPORTANT:
> 
> - We strongly recommend that you configure a secondary tunnel (with different Cato public IPs) for high availability. Otherwise, there is a risk that the site can lose connectivity to the Cato Cloud.
> - Cato conducts periodic maintenance on its PoPs, which may result in both the primary and secondary VPN tunnel PoPs being unavailable during the same maintenance window. To avoid this risk and ensure resiliency, please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new) to help you make sure the site tunnels use PoPs with separate maintenance schedules.

For sites that use IKEv1, there are pre-configured **Service Types** for AWS and Azure.

- **Cato IP (Egress)** for the **Primary** and **Secondary** tunnels - The source IP addresses are the PoP IP addresses that initiate the IPsec tunnel. Select the available IP address for the PoP. If you need more IP addresses, use the **IP Allocation Settings** option to define other IP addresses.
- **Site IP** for the **Primary** and **Secondary** tunnels - The IP addresses for the site that are used for the VPN tunnels.
- **Bandwidth** - You can use the Cato Management Application to control the maximum upstream and downstream bandwidth from the Cato Cloud to each site. If you do not want to configure a specific bandwidth value for a site, we recommend that you use the actual bandwidth from the ISP or according to your Cato Networks license.
- **Private IPs** - The IP addresses that are inside the VPN tunnel that are used to configure BGP dynamic routing for a site.
- **Primary and Secondary PSK** - The public pre-shared keys (PSKs) for the VPN tunnels.

> [!NOTE]
> Note:
> 
> You can optionally use the same allocated IP address for one or more IPsec sites as long as the **Site IP** is different for each site. Cato recommends using different allocated IPs per each site.

## Configuring Routing for IKEv1

IPsec IKEv1 sites have the option to select the **Routing** options for Phase II VPN tunnel:

- **Implicit** - A single tunnel is used to route all internal LAN traffic for the site to the remote IP addresses.
- **Specific** - In the **Network Ranges** field, define the remote IP ranges on the other side of the IPsec tunnel. This creates a full mesh between the local and remote IP ranges.

## Configuring IKEv2 Settings

IPsec IKEv2 sites have these additional settings that you can configure:

- **Initiate Connection by Cato** - You can configure who initiates the connection of the VPN tunnel, the Cato Cloud or the firewall. By default, this feature is enabled so that the Cato Cloud initiates the IPsec connection and minimizes downtime.
- **Network Ranges** - For IPsec connections with a remote side that has SAs (Security Associations) defined for this tunnel, in **Network Ranges**, enter the remote IP ranges (typically networks from other sites) for the SAs in this format **<label:IP range>**.

> [!NOTE]
> Note:
> 
> We strongly recommend that you use the default setting and enable the Initiate Connection by Cato feature.
