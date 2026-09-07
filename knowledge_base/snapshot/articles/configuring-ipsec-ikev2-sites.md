---
title: "Configuring IPsec IKEv2 Sites"
slug: "configuring-ipsec-ikev2-sites"
updated: 2026-08-18T06:36:46Z
published: 2026-08-18T06:36:46Z
canonical: "knowledge.catonetworks.com/configuring-ipsec-ikev2-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring IPsec IKEv2 Sites

This article discusses how to create and configure sites that use the IPsec IKEv2 connection type. For more about creating a new site, see [Using the CMA to Add Sites](/v1/docs/using-the-cma-to-add-sites).

**Note:** As part of recent enhancements introducing multiple active tunnels for IPsec sites, customers may receive false positive disconnection and reconnection events, along with related notifications. This is a one-time occurrence during the update process, and these events and notifications can be safely ignored. Note that the events and notifications may include incorrect timestamps and do not reflect an actual service disruption. IPsec tunnels remain fully operational during this process.

## Overview

You can use IPsec tunnels to connect sites and internal networks to the Cato Cloud and remote networks. Sites with IPsec connections are used for:

- Sites that are in a public cloud, such as AWS or Azure
- Sites for branches in different locations that sit behind a 3rd-party firewall

When configuring an IPsec IKEv2 site, you can initiate the connection using one of the following options:

- Responder Only - Firewall init. The site’s device initiates the connection with the Cato PoP
- Bidirectional – The connection can be initiated by your firewall or by Cato

### Responder Only Connection Mode

Cato's IKEv2 Responder Only setting is a solution for edge appliances that have a dynamic IP address or are located behind a NAT device. (i.e. firewalls or routers) This solution allows the edge appliance on the remote end to initiate and manage the IKEv2 connection.

In addition, when using Responder Only, you can configure Cato to use an FQDN as the Cato identifier. When doing so, Cato generates a hashed value and translates that into an IP address to give you the best PoP location for each tunnel.

For example, you configure the Connection Mode as Responder Only and Destination Type as FQDN. Cato generates a hashed value of somevalue.ipsec.dev.catonetworks.org. This value is then configured in the remote site and acts as the resolver for the DNS request that is using the FQDN value. The PoP is selected based on several parameters, such as geolocation, RTT, and more.

In this scenario, the PoP is selected dynamically, which means that if the original PoP that was designated to that FQDN is unavailable, a new PoP will automatically be selected. In addition, if you follow the Cato best practice and define a primary and secondary tunnel when using an FQDN, Cato automatically selects different PoP locations for ideal HA.

Alternatively, some firewall vendors do not support using the FQDN, in which case you can select IPv4 as the Destination Type. In this case, you must select a static PoP location, and if that PoP is not available for any reason, the tunnel will not be available. For information about defining static IP addresses, see [IP Allocation Policy for Remote Users](/v1/docs/ip-allocation-policy-for-remote-users).

### Bidirectional Connection Mode

In Bidirectional connection mode, both your device or Cato can initiate and maintain IPsec tunnels from selected PoPs towards your sites and/or cloud data centers using the IPsec IKEv2 protocol.

If a tunnel is unavailable, Cato does not have to wait for your device to initiate the connection so the tunnel can be reestablished quickly.

### IPsec Sites with Multiple Active Tunnels

Cato lets you configure multiple active tunnels for both the Primary and Secondary HA roles. Multiple active tunnels enable you to do the following:

- Leverage Last Mile - With multiple active tunnels, you can distribute network traffic across different paths, helping to balance the load and improve network performance.
- Redundancy - Multiple active tunnels provide redundancy. If one tunnel fails, traffic can be rerouted through another active tunnel, ensuring uninterrupted connectivity.
- 3rd-party integration - Integrate with 3rd-party SD-WAN CPEs for SSE services.
- Traffic Segregation - Different tunnels can be used to segregate different types of traffic. For example, one tunnel could be used for voice traffic, while another could be used for data traffic.

![ipsec-active-active.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29496538682525(1).png)

You can configure up to 6 active tunnels for each HA role, which are connected to the same Cato PoP. Meaning, all Primary tunnels are connected to one PoP, and all Secondary tunnels are connected to a different PoP. Each tunnel must have a unique identifier, for example, a local ID such as FQDN or [a public IP address](/v1/docs/configuring-ipsec-ikev2-sites#h_01KNHH7K1QSEHQGRTMCNV5GJB4).

#### HA for Multiple Active Tunnels

By default, when all active tunnels of an HA role go down, Cato automatically reverts to the other HA role. Meaning, if all tunnels of the Primary HA role go down, HA is triggered, and Cato uses the Secondary tunnels as the next hop of all routes of the site. However, if the Primary HA role has 2 tunnels and one tunnel remains up, a failover doesn't occur.

You can monitor tunnels through Link is down stories in the [Stories Workbench](/v1/docs/reviewing-site-operations-stories).

**Note:** It takes up to 30 seconds for Cato to determine that a tunnel went down.

### Bandwidth Management

You can choose to manage the downstream and upstream bandwidth for an IPsec site. If you want the Cato Cloud to cap your downstream bandwidth, enter the required limits accordingly. Otherwise, enter the values as defined by your ISP link's actual connection speed. If you don't know the ISP connection speed, configure the downstream bandwidth according to this site's license. For the upstream bandwidth, the Cato Cloud doesn't control the upstream traffic, and it isn't possible to cap it with a hard limit. Instead, the upstream bandwidth setting is a best-effort setting by the Cato Cloud.

**Note:** If you enter upstream/downstream values greater than the actual connection speed of your ISP's link, the Socket QoS engine is ineffective.

For more about QoS in Cato, see [What are the Cato Bandwidth Management Profiles](/v1/docs/what-are-the-cato-bandwidth-management-profiles).

For QoS for multiple active tunnels, see below [Routing QoS for Multiple Active Tunnels](/v1/docs/configuring-ipsec-ikev2-sites#h_01KNHH7K1QK4MVW4HGCWF19SGC).

### Prerequisites

- If you are sending only part of your network traffic over the Cato Cloud, configure your network equipment to include the following IP addresses in your routing table to the Cato Cloud:
  - 10.254.254.1
  - 10.254.254.5
  - 10.254.254.253
  - 10.41.0.0/16 unless you configured your network's own VPN Users' IP address range
- For IPsec sites with bandwidth of 100Mbps or more, use only the AES 128 GCM-16 or AES 256 GCM-16 algorithms. AES CBC algorithms are only used on sites with bandwidth less than 100Mbps.

These guidelines are due to the fact that GCM encryption is more efficient and scalable than CBC, enabling better performance and reliability for high-throughput encrypted traffic in the Cato Cloud.
- Cato IPsec IKEv2 sites support a nonce length of up to 256 bits.
- For FTP traffic, Cato recommends configuring the FTP server with a connection timeout of 30 seconds or higher.
- You may set the IPSec shared secret (PSK) up to 64 characters.
- For sites that connect to a Zscaler environment, an upgraded Zscaler license is required to enable encryption selection on Phase2.

## Adding the IKEv2 Site

Create a new IPsec IKEv2 site, and then configure it for the IKEv2 settings and assign the Cato-allocated IP addresses for the primary and secondary tunnels. For more information, see [Allocating IP Addresses for the Account](/v1/docs/allocating-ip-addresses-for-the-account).

**To create a new IPsec site:**

1. From the navigation menu, click **Network > Sites** and click **New**.

The **Add Site** panel opens,
2. Configure the settings for the site:
  - **Name:** Name for the site
  - **Type:** Icon shown for the site in the Topology page
  - **Connection Type:** Select **IPsec IKEv2**
  - **Country:** The country in which the site is located.
  - **State:** State where the site is located (where applicable)
  - **License:** Select the appropriate bandwidth license for the site
  - **Native Range:** LAN subnet for the IPsec site
3. Click **New**.

## Configuring the IPsec IKEv2 Settings

After you create a new site that uses IPsec IKEv2 to connect to the Cato Cloud, edit the site and configure the IPsec settings.

> [!NOTE]
> IMPORTANT:
> 
> We strongly recommend that you configure a secondary tunnel (with different Cato public IPs) for high availability. Otherwise, there is a risk that the site can lose connectivity to the Cato Cloud.

Use the **Connection Mode** settings to define if the Cato PoP only responds to connections from the remote site (**Responder Only**) or can also initiate connections (**Bidirectional**).

For sites that are working with dynamic IPs, the Cato Management Application generates a **Local ID** for the site, which is used for the **Authentication Identifier** that you select. Use the **Authentication Identifier** that is required by the third-party device: FQDN, email, or KEY_ID, and enter the Local ID in the IKE settings of your third-party device.

In addition to the Local ID, configure a pre-shared key (PSK) for authentication. You can also define primary and secondary IPsec tunnels with BGP over the device, which provides high availability. By doing so, the Cato Cloud automatically adjusts the BGP route metrics to prioritize the primary tunnel, and if it becomes disconnected, the site automatically moves to the secondary tunnel.

**To configure the settings for an IPsec IKEv2 site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Settings > IPsec**.
3. Expand the **General** section and define how the site connects and authenticates to the PoP:
  1. Select the Connection Mode for the site:
    - **Responder Only** – Firewall init. The site’s firewall initiates the connection, and Cato responds
    - **Bidirectional** - The Cato PoP responds to negotiations for incoming connections and initiates outgoing negotiations.
  2. Select the Authentication Identifier.
    - **IPv4** - use the static IP address you configured in the **Primary** and **Secondary** sections for the site

IPv6 is currently not supported with IPSec over the Cato PoP.
    - **FQDN, Email, KEY_ID** - generates the Local ID in one of these formats
4. Expand the **Primary** section, and configure the following settings for the primary IPsec tunnel:
  - In **Destination Type**, select either FQDN or IPv4. The destination must be the same for all active tunnels for the HA role (Primary or Secondary).
    - **FQDN** - A Cato-generated hashed FQDN value is generated. This value is unique to the specific tunnel. This is the value you will provide to your firewall.

When selected, you must also define the **PoP Location**. Cato recommends you use **Automatic** so that the best PoP is selected for you. If you select a specific location and are also configuring a secondary site, make sure you select different locations.
    - **IPv4** - select a static IP address from the Cato IP (Egress) drop-down.
5. Click **New**. The **Add Tunnel** page appears.
  1. Under **Role**, select which of the logical WAN interfaces to use for this tunnel. The WAN Role is used for priority-based routing in the [Network Rules](/v1/docs/configuring-network-rules) policy.
  2. Under **Name**, enter a descriptive name
  3. Under **Public IP**, enter the public IP address for this tunnel. Each tunnel must use a different public IP address
  4. For sites that use BGP, configure the **Private IPs**:
    - **Cato** - enter the Cato PoP and IP address that initiates the IPsec tunnel
    - **Site** - enter the private IP address of the BGP peer
  5. In **Last-mile Bandwidth**, configure the maximum **Downstream** and **Upstream** bandwidth (Mbps) available to the site
  6. In **PSK**, click **Edit Password** to enter the shared secret for the primary IPsec tunnel.
6. Click **Apply**. The tunnel is added to the primary table.

![primary-ipsec-tunnel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29496552291229(1).png)
7. For sites that use a secondary IPsec tunnel, expand the **Secondary** section and configure the settings in the previous step, and then click **Save**.
8. For sites that use multiple active/active tunnels, repeat steps 5-7.
9. **(Optional)** Expand the **Init Message Parameters** section and configure the settings. See [Init and Auth Parameters](/v1/docs/configuring-ipsec-ikev2-sites#h_01KNHH7K1Q9NTXG24Q87TERWW6) below for valid parameters.

As most IPsec IKEv2-supporting solutions implement automatic negotiation of the following **Init** and **Auth** parameters, we recommend that you set them to **Automatic**, unless specifically instructed to do so by your firewall vendor.
10. **(Optional)** Expand the **Auth Parameters** section and configure the settings. See [Init and Auth Parameters](/v1/docs/configuring-ipsec-ikev2-sites#h_01KNHH7K1Q9NTXG24Q87TERWW6) below for valid parameters.
11. Expand the **Routing** section, and define the routing options for the site:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/ipsec_routing.png)
  - For IPsec connections with a remote side that has SAs (Security Associations) defined for this tunnel, in **Network Ranges**, enter the remote IP ranges (typically networks from other sites) for the SAs in this format <label:IP range> and click **Add**.
  - The local IP ranges for the SAs are configured in the **Site Configuration > Networks** page by including the Local Traffic Selectors and Peer Traffic Selectors.

![ipsec_ikev2_native.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35161463088157(1).png)

Verify that the local networks match what you set for the IPsec peer.

**Note:** If no **Network Ranges** are configured for an IPsec IKEv2 site, the VPN behavior depends on the traffic selectors configured on the peer device:
    - If the peer device uses `0.0.0.0/0 &lt;&gt; 0.0.0.0/0`, the tunnel functions as a route-based VPN
    - If the peer device uses specific traffic selectors, the tunnel functions as a policy-based VPN
12. Click **Save**.

Wait at least 3 minutes before entering the primary and secondary FQDN values in your firewall to allow for the optimal PoP locations for these settings to be determined.
13. To show your connection details and the status of the IPsec tunnel for this site, click **Connection Status**.

### Routing QoS for Multiple Active Tunnels

By default, Cato is only able to control downstream traffic. Traffic is distributed across the tunnels (WAN links) based on health metrics, link preference, and the proportional ratio of the configured bandwidths for each link. The health metrics are recalculated each second, and traffic is redistributed to the best-performing link every 10 seconds.

Upstream traffic is controlled by the remote IPsec peer, and according to the policy-based routing the peer uses.

You can override the WAN link selection for downstream traffic using [Network Rules](/v1/docs/configuring-network-rules). You can configure a rule to determine which WAN link is used for specific traffic tuples, in which case traffic will be sent on the WAN link configured in the rule, and not the tunnel on which it arrived.

![active-active-rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29496581385245(1).png)

### Init and Auth Parameters

The following parameters are available when defining Init and Auth parameters. Cato recommends that you set these parameters to **Automatic** unless instructed otherwise by your firewall vendor.

| Parameter | Valid Values |
| --- | --- |
| Encryption Algorithm | - Automatic - AES-CBC-128 - AES-CBC-256 - AES-GCM-128 - AES-GCM-256 |
| Pseudo Random | - Automatic - SHA1 - SHA2 256 - SHA2 384 - SHA2 512 |
| Integrity Algorithm | - Automatic - SHA1 - SHA2 256 - SHA2 384 - SHA2 512 |
| Diffie-Hellman Group | - 2 (1024-bit) - 5 (1536-bit) - 14 (2048-bit) - 15 (3072-bit) - 16 (4096-bit) - 19 (256-bit random) - 20 (384-bit random) |

## Default IKEv2 Parameters for the Site

This is the list of the default values for the following IKEv2 parameters. If you need a custom value, please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).

| Parameter | Value |
| --- | --- |
| Keep-alive check (sends empty information requests). Number of seconds after the site doesn't receive any data on the tunnel. | 10 seconds |
| Retransmit interval (in seconds). It's not possible to configure a custom value for this parameter. | 10 seconds |
| Maximum number of retransmissions. It's not possible to configure a custom value for this parameter. | 5 retransmissions |
| Maximum time interval that the site doesn't receive any data or responses to the keep-alive checks. After this time, the site tears down the tunnel and attempts to rebuild it. | 60 seconds |
| Time interval that the site attempts to rebuild a tunnel that is down and fails to come up. | Every 90 seconds |
| IKE SA lifetime (IPsec phase 1). You can configure the value for this parameter using [advanced configurations for a site](/v1/docs/advanced-configurations-for-a-site). | 19,800 seconds (approximately 5.5 hours) |
| Child SA lifetime (IPsec phase 2). | 3,600 seconds (1 hour) |

## Sending a Single Traffic Selector for IKEv2 Sites

When creating a child SA, Cato sends multiple traffic selectors (TS) in the same TS payload in accordance with RFC 7295. Some third-party solutions, such as Cisco ASAs, only support a single TS in each child SA. A Cisco ASA will send a **TS_UNACCEPTABLE** message in response to a Cato proposal to create a child SA with multiple TS.

You can configure [your account](/v1/docs/working-with-advanced-configuration-for-the-account) or a specific [IPsec IKEv2 site](/v1/docs/advanced-configurations-for-a-site) to send each TS in a separate packet to support interoperability with these third-party solutions by enabling this configuration under **Site Configuration > Advanced Configuration**.

## Connecting Two Tunnels to an AWS VPC for HA

Cato lets you connect your AWS VPC to the Cato Cloud using BGP over two IPsec tunnels for a high availability (HA) configuration. AWS dual tunnels are supported only when you define two customer gateways, and each one represents a different Cato public IP address. These are the requirements:

- Two Cato public IP addresses
- Two customer gateways in the same VPC, and each one is assigned to a Cato public IP address
- In AWS, two site-to-site connections

## Known Limitations

- For multi-tenant accounts (such as Cato partners), make sure that each account uses IP addresses allocated from a different PoP location for the IPsec tunnels. For example, account1 uses an IP allocated from the Frankfurt PoP, and account2 should use an IP allocated from the Munich PoP location.
