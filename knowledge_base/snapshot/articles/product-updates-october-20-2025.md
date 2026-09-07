---
title: "Product Updates - October 20, 2025"
slug: "product-updates-october-20-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-october-20-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - October 20, 2025

## New Features & Enhancements

- **Manage IP Ranges at Scale with Advanced Groups:** We recently released advanced [groups](/v1/docs/working-with-cma-advanced-groups-and-groups), and now you can use them to define and reuse large sets of [IP ranges](/v1/docs/using-ip-ranges-in-policies) across multiple policies, reducing manual configuration and ensuring consistency at scale.
  - Available for use in Internet and WAN Firewall policies (support for other polices coming soon)
- **New Cato Clients Available:** During the week of October 19, the following Clients will be available:
  - **Windows Client v5.18:** The new Windows Client version 5.18 will be gradually rolled out and includes:
    - Updated the Client embedded browser to Chromium version 139.0.280
  - **iOS Client v5.6.2:** The new iOS Client version 5.6.2 will be available to download from the App Store
  - **Android Client v5.2.1:** The new Android Client version 5.2.1 will be available to download from the Google Play Store
  - Each Client includes:
    - Stability improvements
    - Security updates
    - Bug fixes
- **Provision CMA Admins from your IdP:** You can now streamline admin management by using your Identity Provider (IdP) to [provision CMA admins](/v1/docs/manage-admins-with-your-identity-provider-idp). Previously, the IdP integration only applied to Cato users and user groups. This lets you:
  - Simplify onboarding and offboarding of admins
  - Centrally manage both users and admins with a single IdP
- **Upcoming New CMA Instance for Japan:** As part of Cato’s global expansion, in January 2026, we are introducing a Cato Management Application (CMA) instance based in the Japan region. [This new region](/v1/docs/welcome-to-the-cma) is designed specifically for new customers based in Japan and their respective partners. The new CMA instance offers the same functionality as the existing CMA to manage global accounts and networks, and seamlessly connects to all PoPs worldwide.
  - The Japan CMA instance has no impact on existing Cato customers and partners
- **Granular RBAC for API:** [Cato API queries](/v1/docs/generating-api-keys-for-the-cato-api) and configurations now follow the same feature and entity-level [permissions as CMA admins](/v1/docs/what-are-admins-and-role-based-access-control-rbac), providing consistent and secure access control. There is no impact on existing API keys and integrations.
  - **Granular Control**: API Keys inherit RBAC permissions from the admin or account-level service principal. You can downgrade edit permissions to view-only.
  - **Admin-Bound API Keys**: Keys are tied to specific admins, making them suitable for personal use cases such as individual automation or manual API work.
  - **Service Principals**: Designed for shared automation and integrations, the service principal can’t log in to the CMA. Service keys are not tied to a specific admin and support account-level integrations.
- **Scheduling for Socket Bulk Upgrades:** For improved Socket management, you can now [schedule bulk upgrades](/v1/docs/manually-upgrading-a-socket) to automatically run in a planned maintenance window up to 30 days in advance.
- **Locate Assets Based on Their Last Seen IP:** To help you quickly locate assets across large or distributed environments, the Device Inventory page now supports filtering devices by their Last Seen IP. To create this filter, use the following new operators:
  - **Between** – Specifying an IP range (From–To)
  - **Within** – Based on a CIDR range (for example, <kbd>10.0.0.0/24</kbd>)
  - IoT/OT Security license required
- **New Socket v24.0.20639:** We started the gradual release of minor Socket version 24.0.20639. The build contains bug fixes and internal enhancements.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
