---
title: "Restricting Access to SaaS Application Tenants"
slug: "restricting-access-to-saas-application-tenants"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/restricting-access-to-saas-application-tenants"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Restricting Access to SaaS Application Tenants

This article provides an overview of how to address security concerns in multi-tenant SaaS apps by restricting access to specified tenants.

## Overview

The increase in use of SaaS applications for business and personal use creates a challenge of uncontrolled multi-tenant access. Without visibility and control, users may connect to unsanctioned tenants, resulting in potential security risks, for example:

- Data exfiltration: As sensitive information is uploaded to unmanaged environments
- Compliance violations: Due to storage in unauthorized locations
- Loss of governance: Users can access unsanctioned SaaS apps

Tenant restrictions address these challenges by defining which SaaS app tenants users are allowed to or are blocked from accessing or controlling the actions within the app. They can be used to ensure only approved users can access organizational SaaS tenants, and block access to unapproved users or tenants, for example, personal email accounts. This can help you meet compliance requirements and reduce the risk of data loss.

Cato provides multiple methods of enforcing tenant restrictions:

- **Tenant Awareness**: Within Application Control rules, define specific actions that are allowed or blocked per tenant and user to centrally manage tenant-aware policies across your environment. For example, blocking downloading documents from Google Drive.
- **Tenant Restriction Policy**: Controls user traffic headed to SaaS apps by changing the header fields in HTTP client requests. For example, blocking access to personal Google Drive tenants.

### Use Case - Preventing Data Leakage

A company uses Google Drive as its corporate cloud storage solution and understands its employees have personal accounts.

To prevent accidental or intentional uploads of sensitive data to personal accounts, without disrupting legitimate business activity, the company wants to allow uploads and downloads only to its corporate Google Drive tenant while blocking these activities in personal tenants.

The IT team creates an Application Control rules that allow the upload and download actions within their corporate tenant and block the upload and download action in other tenants.

## Tenant Awareness

You can granularly control user activity across SaaS apps by defining specific actions, tenants, and users in an Application Control rule. The **Application Context** predicate lets you define the specific tenants the rule applies to. Event are created when a user takes an action that matches an Application control rule. For more information about viewing events, see [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network)

For more information on creating Application Control rules, see [Managing the Application Control Policy](/v1/docs/managing-the-application-control-policy).

### Supported Applications

To identify the supported apps and actions, in the [App Catalogue,](/v1/docs/using-the-app-catalog) in the search field, search for the word **Tenant**. Expand each app to identify supported actions.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31197103667613.png)

### Login Action Control

![Login_Action_Control.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31179882081053.png)

Using the **Login** activity in Application Control rules, you can defines the users that are able to log in to or are blocked from a specified app. For example, you can define users that are able to log in to Facebook, while block all other users.

To use this method to enforce tenant restrictions:

1. Create a rule that allows the Login action when the username matches specific criteria
2. Create a lower priority rule that blocks the Login action for the app when the username matches specific criteria

Users who were logged in to the app before the rule was applied are not forced to log out. This method is available for apps that support the Login action.

For more information on creating Application Control rules, see [Managing the Application Control Policy](/v1/docs/managing-the-application-control-policy).

## Tenant Restriction Policy (Application Based)

The Tenant Restriction policy lets you create rules to limit which tenants users can access for the apps allowed in your network. This helps you secure your network by preventing access to tenants besides your organization's tenant. For example, you can stop users from accessing their personal email account or file sharing account to help prevent leakage of sensitive data.

For more information, see [Managing Tenant Restrictions for SaaS Apps (Tenant Restrictions Policy)](/v1/docs/managing-tenant-restrictions-for-saas-apps-tenant-restrictions-policy).
