---
title: "Product Updates - August 11, 2025"
slug: "product-updates-august-11-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-august-11-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - August 11, 2025

## New Features & Enhancements

- **AI Assistant Includes API and Generates Queries:** The [AI Assistant](/v1/docs/what-is-cato-s-ask-ai-agent) now provides Cato API guidance and helps with GraphQL query generation. Simply start your prompt with **/api** and ask natural language questions to:
  - Get information about the Cato API
  - Create general GraphQL queries (these do not include data specific to your account)
  - Click [here](https://academy.catonetworks.com/api-ai-assistant) to watch a video recording of this feature

- **Enhanced Admin Experience for App Control and Data Protection Policies:** Easily manage complex rulebases with more speed, flexibility, and control across [Application Control](/v1/docs/managing-the-application-control-policy), [Data Protection](/v1/docs/creating-the-data-control-policy), and [File Control](/v1/docs/creating-file-control-rules-in-the-application-control-policy) policies. Enhancements include:
  - **GraphQL API support** – Automate policy rule management using the **Cato API**. For details, see the [Cato GraphQL API Reference](https://api.catonetworks.com/documentation/#introduction-item-0)
  - **Concurrent editing** – Multiple admins can [modify policies in parallel](/v1/docs/working-with-policy-revisions) without conflicts
  - **Improved performance** – Policy pages are more responsive, especially for rulebases with a large number of rules

- **Custom App Control & Data Protection User Client Notifications:** If an [Application Control](/v1/docs/managing-the-application-control-policy) or [Data Control](/v1/docs/creating-the-data-control-policy) rule blocks a remote user’s action, a notification is displayed. You can now customize the title and text of this notification to provide a tailored message, in any language, for your organization.

- **Support for Custom SCIM App Integration in CMA**: You can now streamline user provisioning and management by integrating custom SCIM apps with your Cato account, for IdPs that don’t have a Cato SCIM app.
  - Configure a [custom SCIM app](/v1/docs/creating-a-custom-scim-app-for-an-idp) directly in your IdP to sync users with Cato
  - Use the [SCIM API](/v1/docs/using-the-cato-scim-api-for-custom-scim-apps) to create a custom SCIM integration
  - Click [here](https://academy.catonetworks.com/support-scim-as-public-api-and-generic-app-support) to watch a video recording of this feature

- **Manage Site Bandwidth License via API:** There are new beta APIs to assign, replace, update, and remove site licenses for single and pooled licenses. For more information, see [Cato API Changelog](/v1/docs/cato-api-changelog).
  - Click [here](https://academy.catonetworks.com/site-license-assignment-api) to watch a video recording of this feature

- **Terraform Modules for Bulk Network Range Provisioning:** The new [Network Ranges module](https://registry.terraform.io/modules/catonetworks/network-ranges-bulk/cato/latest) (network-ranges-bulk) lets you automate large-scale provisioning of network ranges for sites using Infrastructure as Code. They integrate with CI/CD pipelines and support concurrent policy management, enabling multiple admins to edit and publish the network ranges in parallel.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
