---
title: "Product Updates - July 28, 2025"
slug: "product-updates-july-28-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-july-28-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - July 28, 2025

## New Features & Enhancements

- **Design Customized Reports for Your Specific Needs:** To generate reports that reflect your unique requirements, you can define the widgets and layout of your reports.
  - This lets you mix and match widgets from other reports, such as Site Experience and Security Events, into a [single report](/v1/docs/generating-a-custom-report)
  - A new preview option lets you validate the structure and content before generating the report to ensure that it highlights the most important data for your environment
  - Click [here](https://academy.catonetworks.com/custom-reports) to watch a video recording of this feature

- **Socket Sites Bulk Upgrades:** We added the option to [bulk upgrade multiple sites](/v1/docs/manually-upgrading-a-socket) with a single action. This lets admins efficiently maintain the latest Socket version for account sites without having to upgrade each Socket separately. This helps your account meet Cato’s recommended best practice to use the latest Socket version to ensure Sockets are running a secure, high-performance version with all the latest innovations and features.
  - API support: Use the <kbd>socketBulkUpgrade</kbd> API to initiate a bulk upgrade
  - Up to 100 sites can be upgraded at once
  - You can only bulk upgrade sites with the same connection type (e.g. all of your X1500 sites at once)
  - Click [here](https://academy.catonetworks.com/sockets-bulk-upgrade) to watch a video recording of this feature

- **Connectivity Health Alert Enhancements:** To help you stay better informed about your network's health, Connectivity Health rules now generate alerts not only when a site WAN link goes down, but also when connectivity is restored.
  - These are the alert types for different cases where connectivity is established:
    - **Connected**
    - **Reconnected**
    - **Changed PoP**
  - This change may lead to an increase in the number of alerts. To reduce alert volume, consider adjusting the thresholds in the [Connectivity Health rules](/v1/docs/working-with-link-health-rules) by increasing the **Link Down Duration** or **Event** **Occurrences** values

- **Manage Secondary AWS and Azure vSockets via API:** You can now use the [Cato GraphQL API](https://api.catonetworks.com/documentation/) to monitor, update, and delete the passive secondary vSockets in your AWS and Azure cloud environments.
  - Creating secondary vSockets [via the API](https://api.catonetworks.com/documentation/#mutation-sites.addSecondaryAwsVSocket) is already supported
  - Support for Google Cloud Platform (GCP) is coming soon
- **Join Cato's Product Rewind Session on Aug 6:** Product Rewind is a fast-paced monthly webinar, where we will break down the most compelling product updates from July 2025. See the latest innovations in action with live demos and get practical insights on how these updates can enhance your experience.
  - Register [here](https://academy.catonetworks.com/product-monthly-rewind/269140) for Aug 6, 12 pm ET

## PoP Announcements

- **Beijing, CN:** The following new ranges are now available for the Beijing PoP location:
  - 106.39.250.192/26
  - 111.202.125.0/25

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
