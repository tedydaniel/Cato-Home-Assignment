---
title: "Configuring IPsec IKEv1 Sites"
slug: "configuring-ipsec-ikev1-sites"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/configuring-ipsec-ikev1-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring IPsec IKEv1 Sites

This article discusses how to configure sites that use the IPsec IKEv1 connection type. For more about creating a new site, see [Using the CMA to Add Sites](/v1/docs/using-the-cma-to-add-sites).

## Overview of IPsec IKEv1 Connections

Cato can initiate and maintain IPsec IKEv1 tunnels from selected PoPs towards your sites and/or cloud data centers.

> [!NOTE]
> Note:
> 
> If you are sending only part of your network traffic via the Cato Cloud, configure your network equipment to include the following IP ranges in your routing table to the Cato Cloud:

- 10.254.254.0/24 - default subnet reserved for traffic over the Cato Cloud (for accounts with a custom range, use the custom subnet)
- 10.41.0.0/16 - unless you configured your network's own SDP Users' IP address range (see [IP Allocation Policy for Remote Users](/v1/docs/ip-allocation-policy-for-remote-users))

### Connecting Two Tunnels to an AWS VPC for HA

Cato lets you connect your AWS VPC to the Cato Cloud using BGP over two IPsec tunnels for a high availability (HA) configuration. AWS dual tunnels are supported only when you define two customer gateways, and each one represents a different Cato public IP address. These are the requirements:

- Two Cato public IP addresses
- Configure two customer gateways in the same VPC and each one is assigned to a Cato public IP address
- In AWS, configure two site-to-site connections

## Configuring an IPsec IKEv1 Site

After you create a new site that uses IPsec IKEv1 to connect to the Cato Cloud, edit the site and configure the IPsec settings.

For more information on unique IP addresses, see [Allocating IP Addresses for the Account](/v1/docs/allocating-ip-addresses-for-the-account).

> [!NOTE]
> IMPORTANT:
> 
> We strongly recommend that you configure a secondary tunnel (with different Cato public IPs) for high availability. Otherwise, there is a risk that the site can lose connectivity to the Cato Cloud.

You can choose to manage the downstream and upstream bandwidth for an IPsec site. If you want the Cato Cloud to cap your downstream bandwidth, enter the required limits accordingly. Otherwise, enter the values as defined by your ISP link's actual connection speed. If you don't know the ISP connection speed, configure the downstream bandwidth according to this site's license. For the upstream bandwidth, the Cato Cloud doesn't control the upstream traffic, and it isn't possible to cap it with a hard limit. Instead, the upstream bandwidth setting is a best-effort by the Cato Cloud.

If you are using **Specific: x.x.x.x/y<-->a.a.a.a/b (A tunnel from each local range to specific remote ranges)** routing for the site, review ??? before you start configuring the IPsec settings.

**Best Practice:** Configure the Dead Peer Detection (DPD) settings for IKE v1 Phase II to automatically restart the connection if there is no DPD reply. You can also define how often the Cato Cloud sends a DPD packet and monitors the tunnel status (the maximum interval between DPD packets is 35 seconds).

- For IPsec sites with bandwidth greater than 100Mbps, use only the AES 128 GCM-16 or AES 256 GCM-16 algorithms. AES CBC algorithms are only used on sites with bandwidth less than 100Mbps.
- For FTP traffic, Cato recommends configuring the FTP server with a connection timeout of 30 seconds or higher.
- Cato IPsec IKEv1 sites support nonce length of up to 48 bits.
- You may set the IPSec shared secret (**PSK**) up to 64 characters.

The **SA Lifetime** is the period that the encryption key is valid before it expires and a new key is required. You can't configure the **SA Lifetime** for the IKEv1 Phase 1 and Phase 2 parameters, the settings are:

- Phase 1 - 86,400 seconds (24 hours)
- Phase 2 - 3,600 seconds (1 hour)

> [!NOTE]
> Note:
> 
> If you enter upstream/downstream values that are greater than the actual connection speed of your ISP's link, the Socket QoS engine is ineffective.

For more about QoS in Cato, see [What are the Cato Bandwidth Management Profiles](/v1/docs/what-are-the-cato-bandwidth-management-profiles).

![ikev1_site.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35161448142877.png)

**To configure the settings for an IPsec IKEv1 site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Settings > IPsec**.
3. Expand the **General** section and select a preconfigured IPsec peer type (such as AWS or Azure), or select **Generic**.
4. Expand the **Primary** section, and configure the following settings for the primary IPsec tunnel:

**Note:** You can optionally use the same allocated IP address for one or more IPsec sites as long as the **Site IP** is different for each site. Cato recommends using different allocated IPs per each site.
  - In **Public IP > Cato IP (Egress)**, select the Cato PoP and IP address that initiates the IPsec tunnel.

If you need a different IP address allocated to your account, click **IP Allocation Settings** and select the PoP location and IP address.
  - In **Public IP > Site IP**, enter the public IP address where the IPsec tunnel is initiated.
  - For sites that use BGP dynamic routing, you can enter the **Private IPs** that are inside the VPN tunnel.
  - In **Bandwidth**, configure the maximum **Downstream** and **Upstream** (Mbps) available bandwidth for the site.
  - In **Primary PSK**, click **Edit Password** to enter the shared secret for the primary IPsec tunnel.
5. **(Optional)** Expand the **IKEv1 Phase I Parameters** section, and configure the settings.
  1. In the **Algorithm** section, select the **Encryption Algorithm**: **AES-CBC-128** or **AES-CBC-256**
  2. In the **Algorithm** section, select the **Hash Algorithm**: **MD5**, **SHA1**, or **SHA256**
  3. In **Diffie-Hellman Group**, select the key length that is used in the encryption: **2 (1024-bit)**, **5 (1536-bit)**, **14 (2048-bit)**, **15 (3072-bit)**, **16 (4096-bit)**
6. **(Optional)** Expand the **IKEv1 Phase II Parameters** section, and configure the settings.
  1. In the **Algorithms** section, select the **Encryption Algorithm**: **AES-CBC-128**, **AES-CBC-256**, **AES-GCM-128**, or **AES-GCM-256**
  2. In the **Algorithm** section, select the **Hash Algorithm**: **MD5**, **SHA1**, or **SHA256**
  3. To configure the phase II **Diffie-Hellman Group** settings, first enable **Perfect Forward Secrecy**.
    1. In **Perfect Forward Secrecy**, select **Enable "protection" of past transmissions against future compromises of secret keys** to enable this feature for the site.
    2. In **Diffie-Hellman Group**, select the key length that is used in the encryption: **2 (1024-bit)**, **5 (1536-bit)**, **14 (2048-bit)**, **15 (3072-bit)**, **16 (4096-bit)**
7. Configure the DPD settings for the IKEv1 Phase II parameters:
  1. Select **Keepalive interval (sec)** and enter the number of seconds between keepalive packets (maximum value is 35).
  2. **(Best Practice)** Select **Restart connection on no DPD reply** to enable restarting an IPsec connection when no reply is received for the DPD packets within 35 seconds.

To disable **DPD** for the site, clear **Keepalive interval (sec)**.
8. Expand the **Routing** section, and select the routing option for the site:
  - **Implicit: 0.0.0.0/0<-->0.0.0.0/0 (A single tunnel from all local ranges to all remote ranges)** - all WAN traffic is transmitted over the IPsec connection in a single Phase II tunnel with one encryption key (one for each pair of ESP SAs).
  - **Explicit: x.x.x.x/y<-->0.0.0.0/0 (A tunnel from each local range to all remote ranges)** - all WAN traffic is transmitted over the IPsec connection in a single Phase II tunnel for the [local IP ranges](/v1/docs/configuring-network-ranges-for-a-site) for the site to all remote IP ranges with one encryption key (one ESP SA for each local range).
  - **Specific: x.x.x.x/y<-->a.a.a.a/b (A tunnel from each local range to specific remote ranges)** - see below ???
9. Click **Save**.
10. For sites that use a secondary IPsec tunnel, expand the **Secondary** section and configure the settings in the previous step and then click **Save**.
11. To show your connection details and status of the IPsec tunnel for this site, click **Connection Status**.

### Configuring Specific Routing

When you choose Specific Routing for the IPsec site, all WAN traffic is transmitted over the IPsec connection in a Phase II tunnel using a full mesh between the local and remote IP ranges.

Before you start configuring the IPsec settings for the site, verify that the local networks match what you set for the IPsec peer.

- The local IP ranges (subnets located behind the IPsec peer) are defined in the **Site Configuration > Networks** page:

![ipsec_native.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35161442851229.png)
- The remote IP ranges (typically networks from other sites) are defined in the **Routing** section after selecting the Specific option.

![IPsec_IKEv1_Routing.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35161427036573.png)
  - Click **Add** to enter the IP ranges
