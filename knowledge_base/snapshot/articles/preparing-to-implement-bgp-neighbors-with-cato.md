---
title: "Preparing to Implement BGP Neighbors with Cato"
slug: "preparing-to-implement-bgp-neighbors-with-cato"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/preparing-to-implement-bgp-neighbors-with-cato"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Preparing to Implement BGP Neighbors with Cato

Implementing the BGP dynamic routing protocol in your network lets the Socket make real-time routing decisions and can offer improved network performance and increased flexibility. The available BGP features and functionality are different for Socket sites and for sites configured for IPsec connections.

The process to define a BGP neighbor depends on the site connections:

- [Configuring BGP Neighbors for a Cato Socket](/v1/docs/configuring-bgp-neighbors-for-a-cato-socket)
- [Configuring BGP Neighbors for an IPsec Connection](/v1/docs/configuring-bgp-neighbors-for-an-ipsec-connection)

You can also add [BGP summary routes](/v1/docs/working-with-bgp-summary-routes) to sites.

## Preparing to Define a BGP Neighbor in Your Network

Before you define a BGP neighbor, make sure that you are familiar with the Cato Socket implementation of BGP.

- If your network needs to use the Floating Range feature for BGP, make sure that it is configured correctly for the BGP neighbors
- If your network uses IPsec and BGP with cloud services, review the supported IPsec configurations

### Configuring a Floating Range of IP Addresses

Floating ranges are global IP ranges that are not connected to a specific site, but can be learned from any site with a BGP neighbor. For example, in a Disaster Recovery (DR) scenario, many applications (such as VMware NSX) can move servers from one location to another while maintaining their IP addresses. In these cases, BGP helps to update the remaining network objects and advertises where these servers now reside.

In addition, the Cato Socket cannot use a dynamic range of IP addresses in security and network rules. Use the **Floating Range** Global Setting to define a range of IP addresses in the Cato Management Application.

### Using IPsec and BGP with AWS and Azure

For sites that use IPsec connections to the Amazon Web Service (AWS) and Azure, these are the supported configurations:

- Azure's implementation of IPsec IKEv1 does not support BGP
- Azure IPsec IKEv2 supports BGP
  - Azure IPsec HA requires BGP
- AWS IPsec IKEv1 and IKEv2 support BGP
- For AWS, one BGP neighbor per VPN gateway is supported

## Defining a BGP Peer with a 4 Bytes ASN

Cato's ASN for BGP is a 2 bytes ASN, you can also establish BGP with 4 bytes ASN peers. This solution is according to RFC 4893.

The ASN value should be configured in AS-Plain format (i.e. 600000) and the 4 bytes ASN range is 1-4294967295. The following values are reserved and can't be used as a 4 bytes ASN:

- 65552-131071
- 4294967295

Configure the 4 bytes ASN value in the **Peer** field in AS-Plain format (e.g. 600000). Enter the **Cato** 2 bytes ASN for the BGP neighbor.

![BGP_ASN_4_byte.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247924396957.png)

The [Routing Table](/v1/docs/showing-the-routing-table-for-your-account) shows the AS Path according to the **Peer** value for the BGP neighbor.

## Using BGP Analytics and Events

This section explains how events are generated for updates and changes to BGP sessions and routes.

**To show events for the BGP routing table:**

1. From the navigation menu, click **Home > Events**.

The **Events** screen opens and shows events for **All Sites & Users**.
2. In the **Fields** section, enter **BGP** in the search box.

The window only shows events related to the BGP routing table.

| Event Type | Action | Description |
| --- | --- | --- |
| BGP Session | Establish | BGP session is established with the BGP neighbor |
| BGP Session | Disconnect | BGP session is ended and the site is disconnected from the BGP neighbor |
| BGP Routing | Added | BGP neighbor sends update that this route is added to the routing table |
| BGP Routing | Deleted | BGP neighbor sends update that this route is deleted from the routing table |
| BGP Routing | BGP range ignored | The advertised range for the BGP neighbor was ignored. This may be triggered by: - The route limit was met (1024 routes by default) - Route collision was detected - An invalid route has been advertised, such as 0.0.0.0/0 |
