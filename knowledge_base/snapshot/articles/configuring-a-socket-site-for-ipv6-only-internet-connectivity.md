---
title: "Configuring a Socket Site for IPv6-Only Internet Connectivity"
slug: "configuring-a-socket-site-for-ipv6-only-internet-connectivity"
updated: 2026-07-20T07:47:00Z
published: 2026-07-20T07:47:00Z
canonical: "knowledge.catonetworks.com/configuring-a-socket-site-for-ipv6-only-internet-connectivity"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring a Socket Site for IPv6-Only Internet Connectivity

> [!TIP]
> Note:
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

## Overview

Some Internet Service Providers (ISPs) deliver Internet connectivity using IPv6-only networks. In these environments, IPv4 connectivity is achieved by tunneling IPv4 traffic over IPv6 infrastructure. Cato supports several IPv4-over-IPv6 mechanisms that let you connect a Socket to the Cato Cloud while preserving IPv4 connectivity for applications and services.

Cato supports the following IPv4-over-IPv6 connection types:

- **IPIP6 Static** - IPv4-over-IPv6 with a static IPv6 address and static IPv4 assignment.
- **IPIP6 Auto** - IPv4-over-IPv6 with dynamic IPv6 prefix and manually configured suffix. The ISP provides IPv6 addressing using either SLAAC or DHCPv6 Prefix Delegation (DHCPv6-PD), as defined by the service contract. The Socket uses the IPv6 addressing method supplied by the ISP to establish WAN connectivity.
- **IPv6 DS-Lite** - IPv4-over-IPv6 using Dual-Stack Lite (DS-Lite).

Each option is designed for a specific ISP deployment model and determines how IPv6 addressing is assigned, and how the tunnel endpoint is reached.

### Prerequisites

- IPv6 for Socket sites is supported from Socket v26.0.23517 and higher For more information about manually upgrading a Socket, see this [article](/v1/docs/manually-upgrading-a-socket).

## Architecture Overview for IPv4 over IPv6 Socket Connections

When using an IPv4-over-IPv6 connection, the Socket establishes native IPv6 connectivity to the ISP and then encapsulates IPv4 traffic inside IPv6 packets. The encapsulated traffic is sent to an IPv6 tunnel endpoint, typically operated by the ISP, where the IPv4 packets are decapsulated and forwarded to the IPv4 Internet.

- IPv6 is used as the transport network between the Socket and the ISP tunnel endpoint.
- IPv4 traffic from LAN hosts is transparently encapsulated and decapsulated.
- The tunnel endpoint address is configured explicitly or learned dynamically, depending on the connection type.
- MTU values are reduced to account for IPv6 and tunnel headers.

This approach enables IPv4 connectivity when the access network itself is IPv6-only.

![IPv6_Architecture.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34310562577949.png)

## Configuring an IPIP6 Static Connection

An **IPIP6 Static** connection uses a statically configured IPv6 address on the WAN interface and a statically assigned IPv4 address for the tunnel. The IPv4-over-IPv6 tunnel is established between the Socket and an ISP-provided tunnel endpoint. This endpoint is referred to as an Address Family Transition Router (AFTR) in DS-Lite deployments and as a Border Relay (BR) in IPIP-based IPv4-over-IPv6 deployments.

This option is typically used when:

- The ISP provides fixed IPv6 addressing
- A static IPv4 address is assigned for the tunnel
- The tunnel endpoint IPv6 address is known in advance

![IPv6_IPIP6_Static.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34310546113181.png)

**To configure an IPIP6 Static Connection:**

1. Log in to the Socket WebUI locally. For more information on logging in to the Socket WebUI locally, see [Assigning a Static IP to a Socket](/v1/docs/assigning-a-static-ip-to-a-socket).
2. Click the **Network Settings** tab.
3. From the WAN interface that is connecting to the public Internet, select the **IPIP6 Static** option.
4. In **IPv6 Address**, enter the static IPv6 address assigned by the ISP.
5. In **IPv6 Prefix Length**, enter the prefix length assigned by the ISP.
6. In **Default Gateway IPv6 Address**, enter the IPv6 gateway provided by the ISP.
7. In **AFTR/BR IPv6 Address**, enter the IPv6 address of the tunnel endpoint.
8. In **External IPv4 Address**, enter the static IPv4 address assigned for the tunnel.
9. In **Primary DNS**, enter the primary DNS server. This must be an IPv4 DNS server and is used by the Socket to check connectivity.
10. (Optional) In **Secondary DNS**, enter an additional DNS server.
11. (Optional) In **Configured MTU**, enter the MTU value recommended by the ISP.
12. (Optional) In **Configured VLAN tag**, enter the VLAN ID if required. Enter **0** if there is no VLAN tag.
13. Click **Update**. The IPIP6 Static connection settings are applied to the Socket WAN interface.

## Configuring an IPIP6 Auto Connection

An **IPIP6 Auto** connection dynamically constructs the WAN IPv6 address using an automatic prefix and a manually configured IPv6 suffix. This connection type is used in environments where the ISP requires the IPv6 prefix to be assigned dynamically.

![IPv6_IPIP6_Auto.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34310574258589.png)

**To configure an IPIP6 Auto Connection:**

1. Log in to the Socket WebUI locally. For more information on logging in to the Socket WebUI locally, see [Assigning a Static IP to a Socket](/v1/docs/assigning-a-static-ip-to-a-socket).
2. Click the **Network Settings** tab.
3. From the WAN interface that is connecting to the public Internet, select the **IPIP6 Auto** option.
4. In **IPv6 Static Suffix**, enter the suffix appended to the delegated IPv6 prefix. The suffix often starts with two colons - **::**.

This field is not required if the DHCP server provides the full /128 IPv6 address.
5. In **AFTR/BR IPv6 Address/FQDN**, enter the tunnel endpoint IPv6 address or FQDN.
6. In **External IPv4 Address**, enter the IPv4 address assigned for the tunnel.
7. In **Primary DNS**, enter the primary DNS server.
8. (Optional) In **Secondary DNS**, enter an additional DNS server.
9. (Optional) In **Configured MTU**, enter the MTU value recommended by the ISP.
10. (Optional) In **Configured VLAN tag**, enter the VLAN ID if required. Enter **0** if there is no VLAN tag.
11. Click **Update**. The IPIP6 Auto connection settings are applied to the Socket WAN interface.

## Configuring an IPv6 DS-Lite Connection

**IPv6 DS-Lite** is used in environments where the ISP does not assign an IPv4 address to the customer. As with IPIP6, with DS-Lite IPv4 traffic is encapsulated over IPv6 and processed at the ISP tunnel endpoint. However, with DS-Lite, the traffic that is sent over the IPv4 network has an IPv4 address that is shared among multiple ISP subscribers (carrier-grade NAT).

With DS-Lite:

- The Socket uses IPv6-only WAN connectivity
- IPv4 traffic is tunneled to an AFTR using IPv6
- IPv4 traffic is sent to the IPv4 network using a shared IPv4 address

![IPv6_DS-Lite.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34310574273309.png)

**To configure a DS-Lite Connection:**

1. Log in to the Socket WebUI locally. For more information on logging in to the Socket WebUI locally, see [Assigning a Static IP to a Socket](/v1/docs/assigning-a-static-ip-to-a-socket).
2. Click the **Network Settings** tab.
3. From the WAN interface that is connecting to the public Internet, select the **IPv6 DS-Lite** option.
4. In **AFTR/BR IPv6 Address/FQDN**, enter the AFTR IPv6 address or hostname provided by the ISP.
5. In **Primary DNS**, enter the primary DNS server.
6. (Optional) In **Secondary DNS**, enter an additional DNS server.
7. (Optional) In **Configured MTU**, enter the MTU value recommended by the ISP.
8. (Optional) In **Configured VLAN tag**, enter the VLAN ID if required. Enter **0** if there is no VLAN tag.
9. Click **Update**. The IPv6 DS-Lite connection settings are applied to the Socket WAN interface.
