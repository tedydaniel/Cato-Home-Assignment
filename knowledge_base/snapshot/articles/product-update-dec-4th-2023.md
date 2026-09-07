---
title: "Product Update - Dec. 4th, 2023"
slug: "product-update-dec-4th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-dec-4th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Dec. 4th, 2023

## New Features & Enhancements

- **Always-On Enhancements:** Over the next few weeks, we are introducing new features that ensure Always-On can be used while maintaining business continuity:
  - **New Bypass Mode for Always-On**: Users can temporarily access the Internet without waiting for admin approval. Users provide a reason in the Client and Always-On can be [temporarily bypassed](/v1/docs/protecting-users-with-always-on-security) and the Client can disconnect.
    - The duration of the bypass can be configured by administrators
    - Supported from Windows Client version 5.9
  - **Always-On Recovery Mode:** Users can [access the Internet](/v1/docs/protecting-users-with-always-on-security) if a connection to the Cato Cloud is unavailable. For example, if a Captive Portal prevents the Client connecting to Cato Cloud, users can still access the Internet, bypassing Cato security.
    - Supported from Windows Client version 5.9
- **New Dropbox Connector for SaaS Security API:** You can now [monitor your Dropbox tenants](/v1/docs/dropbox-configuring-the-data-protection-api-connector) for the transfer of sensitive data, compliance violations, and malicious files. For example, identify when files containing credit card details are shared outside your organization.

## PoP Announcements

- The following IP ranges are now available in these PoP locations:
  - **Hong Kong, HK:** 202.75.242.0/24
  - **Las Vegas, NV:** 216.205.118.0/24​​
  - **Manchester, UK:** 216.252.178.0/24
- The following IP ranges will be available soon in these PoP locations:
  - **Ashburn, VA:** 150.195.206.0/24
  - **Osaka, JP:** 150.195.212.0/24
  - **Tokyo, JP:** 150.195.217.0/24
  - **Casablanca, MA:** 150.195.215.0/24

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
