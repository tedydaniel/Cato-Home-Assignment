---
title: "Recommendations for IPsec Connections"
slug: "recommendations-for-ipsec-connections"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/recommendations-for-ipsec-connections"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Recommendations for IPsec Connections

## Overview

Cato Networks enables you to easily set up an IPsec tunnel between your existing edge devices and the Cato Cloud. You can use the IPsec tunnel connection method for sites that aren’t using Cato Sockets. Using IPsec allows you to send traffic in a secure VPN tunnel with authentication and data encryption between the peers. Cato can initiate and maintain IPsec tunnels from selected PoPs (using the allocated IP addresses) towards your edge device (usually a firewall) in a site or data center.

> [!NOTE]
> For FTP traffic, Cato recommends configuring the FTP server with a connection timeout of 30 seconds or higher.

This article provides best practices for how to connect your on-premises or cloud resources to the Cato Cloud with IPsec tunnels.

![blobid0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248159540253.png)

For more about configuring an IPsec site in the Cato Management Application, see [Configuring Sites with IPsec Connections](/v1/docs/configuring-sites-with-ipsec-connections).

## Best Practices for IPsec Connections

The following sections contain best practices for setting up an IPsec tunnel to the Cato Cloud.

### Using Identical Configuration on Both Peers

One of the most common issues when setting up an IPsec connection is misconfiguring the IPsec settings. The key element when configuring an IPsec tunnel is to make sure that the settings 100% match for both connection peers. If the configuration settings don't match for the two sides of the connection, both connectivity and routing problems may occur. In some cases, the tunnel can come up, but if the routing isn’t configured properly, traffic can’t be sent over the tunnel.

Therefore, we highly recommend that you verify the IPsec settings on your edge device (router, firewall, VM, etc.) before you configure the Cato IPsec connection settings. Then use the exact same settings to configure the IPsec site.

### Selecting a Suitable Diffie-Helman Group

One of the most common configuration mistakes is using an incompatible Diffie-Helman (DH) group. The DH group determines the strength level of the keys used for the Auth and Init messages between the connection peers. If the DH group doesn’t match on both sides, the tunnel fails to connect. Therefore, you must select the DH group that matches on both sides of the IPsec connection. Configure the DH group parameter in the Cato Management Application that matches your edge device configuration.

Another important recommendation is for configurations that use PFS (Perfect Forward Secrecy) for key renewal. When the DH group parameter is set to **None**, the PFS is disabled. Therefore, if you’re enabling the PFS, verify that the DH group is configured under the **Auth Message Parameters** section.

The following screenshot shows a sample of Auth Message Parameters and DH group options:

![blobid1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248161259037.png)

We recommend that you avoid using weak encryption settings if possible and use a higher DH group to provide a higher level of security.

### Configuring Child Security Association (SA)

When you are configuring the site in the Cato Management Application, if no DH group is configured for IKEv2 in the **Auth Message Parameters**, a DH group can still show up in **Init Message Parameters** for the Child Security Association (SA). This is because the first Child SA is always created in the initial IKE_AUTH exchange and uses the same key material as the IKE SA. The IKE SA uses the DH group that is configured in the **Init Message Parameters** section. There's no DH group exchange in the IKE_AUTH.

If a DH group is configured in the **Auth Message Parameters** section, it's only used during CREATE_CHILD_SA exchanges which either create additional Child SAs or rekey existing ones.

One thing to look out for is mismatched DH groups configured in the Cato Management Application and the IKEv2 peer. In this situation, the tunnel comes up initially following the IKE_AUTH exchange but fails to rekey using the CREATE_CHILD_SA exchange. There might be a brief disruption before the IKE_SA_INIT and IKE_AUTH exchanges bring the tunnel back up.

### Selecting Specific Encryption Algorithms

It’s very important to use the same encryption algorithm for both connection peers. Sometimes users enable multiple encryption algorithms on their edge devices instead of choosing a single algorithm. Enabling too many algorithms takes more time for the device to establish the connection. Therefore, we recommend that you enable only the algorithm that you use in both sides of the tunnel – less is better.

For IPsec sites with bandwidth of 100Mbps or more, use only the AES 128 GCM-16 or AES 256 GCM-16 algorithms. AES CBC algorithms are only used on sites with bandwidth less than 100Mbps.

These guidelines are due to the fact that GCM encryption is more efficient and scalable than CBC, enabling better performance and reliability for high-throughput encrypted traffic in the Cato Cloud.

> [!NOTE]
> Note:
> 
> For situations where GCM isn’t supported for the INIT phase, we recommend that you use the CBC algorithm for the INIT phase, and GCM for AUTH

### Configuring Primary and Secondary Connections

We recommend that you configure both primary and secondary IPsec connections for redundancy. In addition, you should use different source IP addresses and different destination PoPs for the connections. In case one source or destination fails to connect, and the tunnel goes down, the second tunnel passes the traffic to the other PoP. If you configure the same source IP address in both primary and secondary connections and this source IP has a failure, no other connections are available to pass to the traffic.

### Using IKEv1 or IKEv2

Cato supports both IKEv1 and IKEv2 for negotiation between the two connection peers. When you create an IPsec site in the Cato Management Application, select the supported Internet Key Exchange version (IKEv1 or IKEv2) that matches your edge device. If IKEv2 is supported, then generally we recommend using it However, some devices don’t support the same IKEv2 parameters that are available in the Cato Management Application. In that case, use IKEv1 instead. For example, if your firewall doesn’t support the AES CBC 256 encryption, don’t use it in your IPsec configuration. For more about IKEv1 and IKEv2, see [Cato IPsec Guide: IKEv1 vs IKEv2](/v1/docs/cato-ipsec-guide-ikev1-vs-ikev2)

### Use Cato as a Connection Initiator

If you have an IKEv2 site enabled, we highly recommend that you select the Initiate connection by Cato option. In most cases, edge devices are configured with a long delay between the reconnect attempts. When these devices initiate the connection, the VPN negotiation process takes a long time. In contrast, when Cato initiates the connection, the negotiation takes much faster.

The following screenshot shows the IKEv2 initiator option:

![blobid2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248169754141.png)

### Default IPsec Connectivity Settings for Cloud Providers

The IPsec configurations for different cloud vendor VPNS can be incompatible. Each cloud vendor (for example: Amazon AWS, Microsoft Azure or GCP) uses different default configuration settings for IPsec tunnels. Check the IPsec configuration of your cloud vendor and use a configuration that matches the Cato IPsec site.

**Note**: If you change the default cloud IPsec settings, remember to use the same settings in the Cato Management Application IPsec site settings.

For example, Azure handles PFS differently depending on whether it's the initiator or responder for a Child SA (ESP SA). When it's the initiator, Azure does not send a DH group by default. When it's the responder, Azure accepts a DH group from the peer. This means that if a DH group is configured under the **Auth Message Parameter** section in the Cato Management Application and Azure attempts to create an ESP SA using the CREATE_CHILD_SA exchange, Cato responds with "No proposal chosen" and the SA fails to establish. If Cato initiates the CREATE_CHILD_SA exchange, however, the ESP SA establishes if the DH group configured is one that Azure accepts as a responder. Therefore, to ensure maximum compatibility with Azure, either set the DH group to **None** in the **Auth Message Parameter** section of the IKEv2 site configuration or configure a custom policy in Azure that specifies the same PFS group as the DH group configured in the Cato Management Application.

The following screenshot shows an example of Azure custom configuration:

![azure_ipsec.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26295344391069.png)

For more about Azure VPN parameters, see [About VPN Devices and IPsec Parameters](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-devices).

### Select the Exact Configuration Settings

Cato Networks allows you to select **Automatic** parameters for the IKEv2 **Init** and **Auth Message Parameters** such as encryption, RPF and integrity algorithms. If you encounter connectivity or routing issues when using the automatic configuration, we recommend that you select the exact configuration that matches your edge device settings and avoid using **Automatic**.

However, for sites configured with GCM for the **Encryption algorithm** (AES GCM 128 or AES GCM 256), then the **Integrity algorithm** is not relevant because GCM also provides integrity. When you select an **AES GCM** encryption algorithm, the Integrity algorithm is set to **Automatic**.

## Verifying the IPsec Connection

Use the **Connection Status** button for the site in the Cato Management Application to check the primary and secondary tunnel information. For example:

![blobid5.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248169921437.png)
