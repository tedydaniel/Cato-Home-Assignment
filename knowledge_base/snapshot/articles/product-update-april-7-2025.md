---
title: "Product Update - April 7, 2025"
slug: "product-update-april-7-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-april-7-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - April 7, 2025

## New Features & Enhancements

- **Mitigate Suspicious Targets with Cato XDR:** You can add suspicious IP addresses or FQDNs to a [Container](/v1/docs/integrating-custom-ioc-lists-with-containers) directly from the [story drill-down page](/v1/docs/drilling-down-and-analyzing-xops-security-stories), and then include them in your firewall rules.
  - The **Add Target to Blocklist** [mitigation](/v1/docs/mitigating-threats-in-xops-stories) is available in the **Actions** menu in Security stories
  - Click [here](https://academy.catonetworks.com/xdr-mitigation-actions-add-target-to-blocklist) to watch a video recording of this feature
- **Upcoming Rollout of Socket v23:** We will be starting the rollout of [Socket version 23](/v1/docs/socket-version-23-0-release-notes) to all customers, which includes all v22 and v23 features, enhancements, and bug fixes.
  - Sockets v21.x and lower will be automatically upgraded directly to v23 (and will skip v22)
  - No customer action is required

- **EPP Agent v1.4:** Starting April 6, 2025, we are rolling out EPP Agent version 1.4. This version includes the following bug fixes and enhancements:
  - Fixed the “Error-Action timed out” when trying to terminate a full system scan that’s running
  - Improved memory utilization
  - Stability improvements and bug fixes
  - Security updates

- **Android Client v5.2 Supporting Chromebook:** Android Client version 5.2 will be gradually rolled out in the [Google Play Store](https://play.google.com/apps/testing/com.catonetworks.vpnclient) starting from the week of April 6, 2025. This version contains bug fixes and enhancements.
- **Update to Detection and Response Policy for MXDR Customers:** The [Mute Stories](/v1/docs/muting-xops-stories) and [Response Policy](/v1/docs/creating-the-response-policy-for-xops-stories) tabs in the Detection and Response Policy are now editable for MXDR customers. You can add a new rule or edit an existing rule directly in the CMA.
  - Only stories created by the Network XDR producer can be muted

- **CMA Enhancement for Cloud Interconnect:** We improved how the CMA shows information for Manual Cloud Interconnect connections. For each connection, the page shows a table containing the PoP location, VLAN ID, and BGP status.
  - Previously, these parameters were only shown for the Public Cloud connection type

- **New Logistics Admin Predefined Role for RBAC:** To target our operation personas who use the CMA, we are adding **Logistics Admin** to the [predefined Roles & Permissions](/v1/docs/managing-admin-roles-using-rbac). The role provides editor access to the [Socket & Accessories](/v1/docs/using-the-socket-assignment-page) page.

- **Join Cato's Product Rewind Session on April 9:** To help you stay up to speed with our fast-evolving platform, Cato is launching a new monthly live session - Product Rewind. Each session will recap the previous month’s key highlights, share live demos, and leave time for your questions.
  - Look for details for future Product Rewind in the 'What's New' menu in the CMA and in the [Cato Connect community](https://connect.catonetworks.com/)
- **Next Week Product Update Will be Sent on April 14:** Due to holidays, there will be a 24-hour delay of the Product Update for next week, and it will be sent on Monday, April 14, 2025.
- **Register for May 6 Academy Live Tech Hour:** Join a live session and unlock the full potential of Cato’s Application Control. Discover best practices, new features, and hidden capabilities to protect your SaaS applications with inline and out-of-band connections. Register [here](https://academy.catonetworks.com/live-master-application-control).

## PoP Announcements

- **Amsterdam, NL:** A new range (216.252.186.0/24) will soon be added to the Amsterdam PoP location.
- **Brussels, BE:** A new range (216.252.189.0/24) will soon be added to the Brussels PoP location.
- **Madrid, ES:** A new range (216.252.188.0/24) will soon be added to the Madrid PoP location.
- **Manila, PH:** A new range (123.253.155.0/24) will soon be added to the Manila PoP location.
- **Paris, FR:** A new range (216.252.190.0/24) will soon be added to the Paris PoP location.
- **Tel Aviv, IL:** A new range (216.252.187.0/24) will soon be added to the Tel Aviv PoP location.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
