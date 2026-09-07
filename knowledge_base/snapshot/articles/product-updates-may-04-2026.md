---
title: "Product Updates - May 04, 2026"
slug: "product-updates-may-04-2026"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-may-04-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - May 04, 2026

## New Features & Enhancements

- **New Windows Client v6.4:** During the week of May 3, 2026 we will begin the roll out of [Windows Client](/v1/docs/summary-of-cato-windows-client-releases) version 6.4. This version includes:
  - Stability improvements
  - Security updates
  - Bug fixes
- **New macOS Client v5.13:** During the week of May 3, 2026 we will begin the roll out of [macOS Client](/v1/docs/summary-of-cato-macos-client-releases) version 5.13. This version includes:
  - Stability improvements
  - Security updates
  - Bug fixes
- **Application Control via API - Support for Citrix ShareFile:** Connecting SaaS apps to Cato lets you understand who is accessing each app and identify suspicious activities or trends even when users are not connected to the Cato Cloud. You can now connect your [ShareFile](/v1/docs/citrix-sharefile-configuring-the-app-activities-integration) account to provide visibility into user activities.
  - The ShareFile connector is available from the **Integrations Catalog**, under **App Activities**
  - CASB license required
- **Near Real-Time Updates for Threat Prevention Stories:** The XOps Threat Prevention producer now updates stories in near real-time for quicker detection and response for supported threat indications.
  - Stories are gradually being enhanced to near-real-time
  - Stories requiring larger sets of aggregated data for detection continue to operate on their existing update cycles
  - Enhanced stories may generate more alerts due to increased update frequency. To adjust, update your response policy
  - XOps license required
- **Entra ID Interconnected Apps Connector Collects Plugin Usage Data**: Track plugin usage of third-party apps into [Entra ID](/v1/docs/microsoft-entra-id-configuring-the-interconnected-apps-integration). This provides deeper visibility into the apps and users involved in plugin-based access.
  - To collect this data, the connector requires the **AuditLog.Read.All** permission. For existing connectors, add the permission using one of these options:
    - In the Entra ID admin console, go to API permissions. Add the **AuditLog.Read.All** permission and grant admin consent in the registered application used for the Cato connector.
    - In the CMA, delete the existing connector. Then create a new connector and consent to all required permissions, including **AuditLog.Read.All**.
- **New Release for EPP Agent v1.6.2:** Starting April 30, 2026, we released [EPP Agent version 1.6.2](/v1/docs/summary-of-epp-agent-versions). This version includes security updates, bug fixes, and enhancements.

## PoP Announcements

- **Updated Dubai PoP Naming**: Cato consolidated the PoPs in Dubai under a single PoP named **Dubai**, replacing **Dubai_DC2**. There is no impact on your service, and no action is required.
- **Seoul, KR:** A new range (113.30.133.0/24)is now available for the Seoul PoP location.
- **Singapore:** A new range (113.30.135.0/24) will soon be added to the Singapore PoP location.
- **Upcoming Localized IP Range for Pakistan:** The following localized IP range for Pakistan (serviced through the Dubai PoP location) will soon be available:
  - **PK:** 113.30.129.160/27

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
