---
title: "Product Update - May 19, 2025"
slug: "product-update-may-19-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-may-19-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - May 19, 2025

## New Features & Enhancements

- **New Windows Client v5.15 Release:** During the week of May 19, 2025, we are starting the rollout of the new [Client version for Windows](/v1/docs/summary-of-cato-windows-client-releases) (v5.15). This version includes:
  - **Advanced Device Posture Collection:** To improve performance when connecting, Device Posture is now collected continuously, even before connecting, to ensure Device Posture stays up-to-date.
  - Bug fixes and enhancements, including:
    - Improved the Client flows for better connection and reconnection time, and reduced errors
- **Reporting Client Version Known Limitations and Resolved Issues:** We are now reporting the Known Limitations and Resolved Issues as part of the [Client releases](/v1/docs/summary-of-cato-windows-client-releases).
  - You can also ask the [Knowledge AI Assistant](/v1/docs/what-is-cato-s-ask-ai-agent) in the CMA for information about Client versions
- **Enhanced Admin Experience for Managing TLS Inspection Policy:** We have enhanced the [TLS Inspection Policy](/v1/docs/configuring-tls-inspection-policy-for-the-account) to give administrators more flexibility, speed, and control when configuring policies.
  - API support for managing the policy For more information see the [Cato GraphQL API Reference](https://api.catonetworks.com/documentation/#introduction)
  - Ability to [modify the policy](/v1/docs/working-with-policy-revisions) in parallel by multiple admins
  - Faster and more responsive for policies with many rules
- **Identical Internet-Only IP Ranges:** To simplify network management and improve security for guest traffic, you can now configure [identical IP ranges](/v1/docs/configuring-network-ranges-for-a-site) in multiple sites to be used for Internet-only traffic. These ranges are not propagated to the global routing table, preventing communication with the WAN.
  - We recommend as a guest WiFi best practice, to use the Internet-only ranges together with the [Cato captive portal](/v1/docs/configuring-the-cato-captive-portal)
  - Supported for physical Sockets only, v21 and higher
  - Click [here](https://academy.catonetworks.com/internet-only-ranges) to watch a video recording of this feature
- **BGP Inbound Route Filters for Socket Sites**: We are adding support for [inbound Route Filters](/v1/docs/working-with-bgp-filtering), providing granular control and improved scalability to accept or drop BGP routes.
  - You can use CIDR lists or BGP communities to determine which routes to filter
  - Supported for Socket sites v21.1 and higher (support for IPsec sites is coming soon)
  - Click [here](https://academy.catonetworks.com/bgp-inbound-filters) to watch a video recording of this feature
- **New PoP Location for Cloud Interconnect:** A new PoP for [Cloud Interconnect](/v1/docs/cloud-interconnect-availability) in Los Angeles is now available to immediately connect a site, expanding connectivity and access on the West Coast of the US.
- **API Support for App Catalog and DLP Content Types:** We added the following [new API queries](https://api.catonetworks.com/documentation/):
  - App Catalog - Query the data for apps, including Compliance, Security, and CASB Activities:
    - catalogApplicationList - All apps and data
    - catalogApplication - Single app
  - DLP Content - Query the types of content for the DLP Data Inline Protection rule
    - contentTypeGroupList

## PoP Announcements

- New ranges are available for the following PoP locations:
  - **Charlotte, US:** 199.27.39.0/24
  - **Seattle, US:** 199.27.38.0/24
  - **Tokyo, JP:** 123.253.154.0/24

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
