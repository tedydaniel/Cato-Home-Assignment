---
title: "Product Update - February 13th, 2023"
slug: "product-update-february-13th-2023"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-february-13th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - February 13th, 2023

## New Features & Enhancements

- **Site Configuration API:** You can use the GraphQL [configuration API](/v1/docs/cato-configuration-api-reference-guide)to provision new sites and edit existing ones, including settings such as network ranges, hosts, and so on. For example, customers can automate large-scale site deployment using pre-defined scripts.
  - You can use [Postman to easily modify example scripts](/v1/docs/using-the-cato-site-creation-api-with-postman)for the configuration APIs
- **RBAC for Cato Management Application Admins:** The new [Role Based Access Control (RBAC) feature](/v1/docs/managing-admin-roles-using-rbac) increases security for Cato Management Application admins, and lets you use admin roles to restrict permissions for specific screens. For example, use the predefined Security role to restrict access to only those screens that are related to security features.
- **RBAC for Cato Resellers:** Cato resellers can use [predefined or custom admin roles](https://support.catonetworks.com/hc/en-us/articles/9087001774365)to manage access for the reseller and managed accounts.
  - Use roles to restrict admin permissions only for the reseller account
  - Roles can be applied to admins for multiple managed accounts
  - Customize roles and access according to the unique requirements for accounts
- **New SDP Users Dashboard Provides Better Visibility:** We are releasing a [new dashboard](/v1/docs/using-the-access-overview-page) that visualizes data for SDP user access in your account. For example, there are widgets that show the number of concurrent SDP users connected, trend of connected users over time, users for each Client OS and version, and more.
- **Email Notifications for BGP Neighbor Status Change**: You can now configure email notifications to inform admins of BGP neighbor status changes. Notifications are sent when the status changes from Established to Down and vice versa.
- **IPS Email Notifications Include More Threat Data:** We enriched the IPS email notifications with additional data to help you understand threats, including:
  - Threat Type
  - Threat Name
  - Application Category
- **Cato Management Application Enhancements:**
  - New support for Japanese localization
  - New type of [Cato API keys](/v1/docs/generating-api-keys-for-the-cato-api) that supports configuration API calls and queries

## Knowledge Base Updates

- [Cato Configuration API - Reference Guide](/v1/docs/cato-configuration-api-reference-guide)
- [Configuring Roles and Permissions for Admins](/v1/docs/managing-admin-roles-using-rbac)
- [Configuring Roles and Permissions for Reseller Admins](https://support.catonetworks.com/hc/en-us/articles/9087001774365)
- [What is SaaS Security API](/v1/docs/what-is-the-data-protection-api)
