---
title: "Product Update - Oct. 23rd, 2023"
slug: "product-update-oct-23rd-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-oct-23rd-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Oct. 23rd, 2023

## New Features & Enhancements

- **Aggregate BGP Routes into a Single Summary Routes:** For IPsec and Cross Connect sites, you can [optimize BGP routing efficiency](/v1/docs/working-with-bgp-summary-routes) by aggregating multiple individual routes into a single BGP route announcement. This lets you reduce the number of routes that are advertised and add community-based actions.
- **Establish BGP with 4 Bytes-ASN Peers:** You can now configure a [4 bytes-AS Number (ASN)](/v1/docs/preparing-to-implement-bgp-neighbors-with-cato) in the Cato Management Application to define a BGP neighbor between Cato’s 2 bytes-ASN and the 4 bytes-ASN for your BGP peer.
  - Enter the 4 bytes-ASN in the AS-plain format
  - Configuration is according to RFC 4893
- **Improved Device Visibility with Client Connectivity Policy Event:** An [event](/v1/docs/analyzing-events-in-your-network) is now created after a device complies with a [Client Connectivity Policy](/v1/docs/configuring-the-client-connectivity-policy) rule and is allowed to connect to your network. This event enables increased granularity in Client Connectivity policy rules by providing admins with a better understanding of the posture of devices connecting to the network.
- **Improved Process to Redeploy a vSocket for AWS, Azure, or ESXi Sites (Early Availability Feature):** Cato supports re-installing a vSocket for a site without removing and recreating the site. We added an option to the Cato Management Application to unregister an existing vSocket from a site, and then you can recreate the vSocket and redeploy it on a new VM resource.
  - For example, you can use this process to migrate a vSocket to a different VM resource, or reinstall a vSocket on a different VM instance type
  - During the process the site configuration is preserved
  - We’re looking for more EA participants, please contact us [ea@catonetworks.com](mailto:ea@catonetworks.com)

## Knowledge Base Updates

[Zscaler Network Error When Connected Via Cato SDP Client](/v1/docs/zscaler-network-error-when-connected-via-cato-sdp-client)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
