---
title: "Product Updates - September 22, 2025"
slug: "product-updates-september-22-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-september-22-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - September 22, 2025

## New Features & Enhancements

- **Enhancements to Device Inventory:** We made the following enhancements to the [Device Inventory](/v1/docs/what-is-device-inventory) page:
  - **New Source Indicator for Device Data:** For improved visibility and context, the **Source** field helps identify whether a device was classified by Cato directly or via an external integration
  - **Export to CSV:** You can export the complete Device Inventory to a CSV file, enabling easier reporting, auditing, and integration with external tools
  - **Centralized Location:** To create a single location to review devices connected to your network, we combined the Device Inventory and [Device Dashboard](/v1/docs/using-the-device-dashboard) pages into a single page with two tabs
  - IoT/OT Security license required for all enhancements
- **Device Inventory Integration with CrowdStrike EDR:** Admins can now enrich Cato’s Device Inventory with data from [CrowdStrike EDR](/v1/docs/crowdstrike-configuring-the-device-management-integration). This integration adds additional device context, enabling more accurate classification and a clearer picture of connected assets. By combining endpoint insights from CrowdStrike with Cato’s own discovery, admins gain better visibility and precision in identifying devices across the network.
  - IoT/OT Security license required
- **CMA Enhancements:**
  - **Simplified Management of API Integrations:** To simplify SaaS app integration setup, on the Integrations page, the **Integrated apps** tab includes Data Protection apps, providing a single, unified view for managing all API integrations. The Data Protection API tab has been removed
  - **Improved Search in the App Catalog:** In the [App Catalog](/v1/docs/using-the-app-catalog), the search returns results for all catalog content. For example, you can search for a specific app tenant. Previously, only the app name was searchable
- **End of Support for ESXi vSphere 6.7 and 7.0:** After Dec. 31, 2025, Cato is [ending support](/v1/docs/end-of-support-eos-policy-for-cato-vsockets) for VMware vSphere versions 6.7 and 7.0, in line with VMware’s End-of-Life announcement. Issues identified as related to the outdated platforms are not addressed by Support.
  - Existing vSockets on these versions may continue to function, and Support tickets will be addressed if the issue isn't related to an outdated platform
  - Admins should upgrade to a supported vSphere version to ensure continued compatibility and support

## PoP Announcements

- **New Localized IP Ranges:** The following new localized IP ranges (serviced through the Dubai PoP location) are now available:
  - **Bahrain:** 113.30.129.0/27
  - **Kuwait:** 113.30.129.32/27
  - **Oman**: 113.30.129.64/27
  - **Qatar:** 113.30.129.96/27
  - **Saudi Arabia:** 113.30.129.128/27

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
