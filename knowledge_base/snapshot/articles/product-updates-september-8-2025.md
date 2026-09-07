---
title: "Product Updates - September 8, 2025"
slug: "product-updates-september-8-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-september-8-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - September 8, 2025

## New Features & Enhancements

- **Resume Previous AI Assistant Chat:** Seamlessly return to your previous conversation with the [CMA AI Assistant](/v1/docs/what-is-cato-s-ask-ai-agent) using the **Last Chat** section. This lets you pick up where you left off, even after closing or refreshing the page.
  - Only the most recent session is saved
- **Upcoming Change to Cato Password Policies:** To enhance security and align with industry best practices, we will update the password requirements for both users and CMA admins. We will start rolling out this change on October 5, 2025, for new or updated passwords.
  - Passwords must contain one of each: lowercase letter, uppercase letter, number, and a special character (new requirement)
  - Additionally, admin passwords cannot contain an email address or be on our list of common passwords (e.g., “aB12345!”)
  - This change applies only to newly created or updated passwords. **There is no impact on existing passwords**
- **Faster Cato Client Connection for Remote Users:** Remote users now connect more quickly with the Cato Client, improving their login experience and reducing wait times.
  - Device posture checks now include only the items enabled in **Device Posture Profiles**
  - Will be gradually applied to all remote users starting next week
- **App Analytics Enhancement - Filter by Connection Type:** For more focused visibility and analysis, you can filter the **Connection Type** field in the [App Analytics page](/v1/docs/understanding-app-analytics) to show only **Remote** users or **Site Host** (users behind a site). For example, you can:
  - Filter site host and user traffic to easily understand how much licensed site bandwidth is consumed by local users/hosts versus remote clients
  - Filter remote user traffic to track which SaaS or corporate apps are most accessed by remote users
- **Terraform Modules for Bulk Azure vSocket Provisioning:** The new Azure vSocket modules let you automate large-scale provisioning of Azure vSockets for sites using Infrastructure as Code. They integrate with CI/CD pipelines and support concurrent policy management, enabling multiple admins to edit and publish the network ranges in parallel.
  - [vsocket-azure-vnet-2nic](https://registry.terraform.io/modules/catonetworks/vsocket-azure-vnet-2nic/cato/latest) - Deploys a 2 NIC Azure single vSocket and site with required resources
  - [vsocket-azure-ha-2nic](https://registry.terraform.io/modules/catonetworks/vsocket-azure-ha-2nic/cato/latest) - Deploys a 2 NIC Azure primary and secondary vSocket and HA site with required resources
- **New Page for Configuring Site Licenses:** To improve access and visibility for license details, we have created a separate **License** page under Site > Site Configuration.
  - This information was previously part of the Site Configuration > General page
  - This does not impact existing configurations or APIs
- **Join Cato's Product Rewind Session on Sep 9:** Product Rewind is a fast-paced monthly webinar, where we will break down the most compelling product updates from Aug 2025. See the latest innovations in action with live demos and get practical insights on how these updates can enhance your experience.
  - Register [here](https://academy.catonetworks.com/product-monthly-rewind/269140) for Sep 9, 12 pm ET

## PoP Announcements

- **Fortaleza, BR:** A new Cato PoP is now available in Fortaleza with the IP range 216.205.114.0/24.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
