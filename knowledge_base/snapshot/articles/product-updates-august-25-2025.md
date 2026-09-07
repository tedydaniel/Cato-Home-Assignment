---
title: "Product Updates - August 25, 2025"
slug: "product-updates-august-25-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-august-25-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - August 25, 2025

## New Features & Enhancements

- **Enhanced Admin Experience for Client Connectivity Policy at Scale:** Easily manage complex rulebases with more speed, flexibility, and control across the [Client Connectivity policy](/v1/docs/configuring-the-client-connectivity-policy). Enhancements include:
  - **Concurrent editing** – Multiple admins can [modify policies](/v1/docs/working-with-policy-revisions) in parallel without conflicts
  - **Improved performance** – Policy page is more responsive, especially for a large number of rules
  - **GraphQL API support** – Use the <kbd>ClientConnectivityAddRule</kbd> API to manage the Client Connectivity policy
- **BGP Inbound Route Filters for IPsec and Cloud Interconnect:** IPsec and Cloud Interconnect sites now support [inbound route filters](/v1/docs/working-with-bgp-filtering), providing granular control and improved scalability to accept or drop BGP routes.
  - You can use CIDR lists or BGP communities to determine which routes to filter
  - Previously, this was available only for Socket sites
  - Click [here](https://academy.catonetworks.com/bgp-inbound-filters) to watch a video recording of this feature
- **New Release for macOS Client v5.10:** During the week of August 24, 2025, we are starting to roll out the new macOS Client version 5.10. This version includes:
  - **Remote internet security with one-time authentication:**[One-time authentication](/v1/docs/remote-internet-security-with-one-time-authentication) enables users to always have connectivity and protection with minimal interaction with the Client. Previously supported only for the Windows Client. To see if this impacts your users, read our [FAQ](/v1/docs/faqs-upgrading-to-macos-client-v5-10-aug-2025).
  - An updated user interface that now includes more connectivity details
  - Performance enhancements and bug fixes
- **DEM Enhancements:** We added the following improvements to the Experience Monitoring page:
  - The Remote Users and Office Users tabs provide the following new data columns:
    - **Device Name** - To help you monitor activity for the same user across multiple devices
    - **Email** - To distinguish between different users with the same name, each user’s email address is shown
  - For better data granularity, metrics that previously were limited to 5-minute buckets now report data in 1-minute buckets
    - Applies to Wi-Fi, CPU, and LAN Gateway metrics
- **New PoP Location API Query:** The <kbd>PoPLocationList</kbd> query retrieves a list of all the PoP Locations in the Cato Cloud with details such as name and country. For example, you can use this API to configure Network Rules (such as traffic routing) or set a Socket to use a [preferred PoP location](/v1/docs/defining-a-preferred-pop-for-a-site).
- **CMA Enhancement to the Users Page:** A new column indicating the Authentication Status is available in the Users Directory tab. This indicates whether your users have successfully set up their authentication.

## PoP Announcements

- New Cato PoPs will become available soon in the following locations:
  - **Fortaleza, Brazil**
  - **Rome, Italy**

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
