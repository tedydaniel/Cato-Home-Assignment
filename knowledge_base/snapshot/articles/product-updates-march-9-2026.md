---
title: "Product Updates - March 9, 2026"
slug: "product-updates-march-9-2026"
updated: 2026-08-26T13:56:16Z
published: 2026-08-26T13:56:16Z
canonical: "knowledge.catonetworks.com/product-updates-march-9-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - March 9, 2026

## New Features & Enhancements

- **Granular Audit Trail for Policy Changes:** The [Audit Trail](/v1/docs/using-the-audit-trail) now provides additional granular details of changes made by admins to a policy, for example, changes made to the Internet or WAN Firewall. This ensures comprehensive transparency and accountability.
  - Available in the Audit Trail page and via the [auditFeed](https://api.catonetworks.com/documentation/#query-auditFeed) API
  - The Audit Trail page displays the previous and new values for a change

- **New iOS Client v5.8:** During the week of March 8, 2026, the iOS Client version 5.8 will be available to download from the App Store. This version includes:
  - Stability improvements
  - Security updates
  - Bug fixes

- **Expanded Security Events via GitHub Connector:** The [GitHub App Activities](/v1/docs/github-configuring-the-app-activities-integration) connector supports collecting additional security event data from your repositories. The connector can now retrieve code scanning, Dependabot vulnerability, and Secret scanning alerts.

- **Version Labels for Manual Socket Upgrades:** We improved the visibility for identifying the appropriate Socket version when performing a manual upgrade. The version drop-down list includes the following labels:
  - **Rollout** - Indicates the newest version currently being gradually deployed
  - **Recommended** - Indicates a previously released version

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
