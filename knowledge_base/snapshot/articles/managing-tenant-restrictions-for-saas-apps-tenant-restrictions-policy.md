---
title: "Managing Tenant Restrictions for SaaS Apps (Tenant Restrictions Policy)"
slug: "managing-tenant-restrictions-for-saas-apps-tenant-restrictions-policy"
updated: 2026-07-20T12:30:27Z
published: 2026-07-20T12:30:27Z
canonical: "knowledge.catonetworks.com/managing-tenant-restrictions-for-saas-apps-tenant-restrictions-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Tenant Restrictions for SaaS Apps (Tenant Restrictions Policy)

This article explains how to control access to SaaS apps tenants with the Tenant Restriction policy. For an overview of how Tenant Restriction rules control access using header injections, see [Restricting Access to SaaS Application Tenants](/v1/docs/restricting-access-to-saas-application-tenants).

## Overview

The Tenant Restriction policy lets you create rules to limit which tenants users can access for the apps allowed in your network. This helps you secure your network by preventing access to tenants besides your organization's tenant. For example, you can stop users from accessing their personal email account or file sharing account to help prevent leakage of sensitive data.

The Tenant Restriction rulebase controls user traffic headed to SaaS apps by changing the header fields in HTTP client requests. When traffic matches a rule, Cato acts as a proxy and injects the HTTP headers you defined for that rule. The third-party app receives the headers you specified, and then enforces your organization's tenant access policy for that app.

You can configure granular Tenant Restriction rules that apply to specific user groups, sites, or other sources. Granular rules can help you gradually implement tenant restrictions and avoid potential usability issues. You can also create rules that bypass tenant restrictions for specified sources.

### Policy Revisions and Concurrent Editing by Multiple Admins

The Tenant Restriction policy lets different admins edit the policy in parallel. Each admin can edit rules and save the changes to the rulebase in their own private revision, and then publish them to the account policy (the published revision). For more information on how to manage policy revisions, see [Working with Policy Revisions](/v1/docs/working-with-policy-revisions).

### Prerequisites

- For Tenant Restriction rules, you must enable TLS Inspection and define the TLS Inspection policy to inspect the traffic that matches the rule.
- The Tenant Restriction feature is included in the CASB license. For more about purchasing the CASB license, please contact your Cato representative.

## Enabling the Tenant Restriction Policy

Enable the Tenant Restriction policy to create rules that control access to SaaS apps tenants.

**To enable or disable the Tenant Restriction policy:**

1. From the navigation menu, select **Security > App & Data Inline**.
2. Select the **Tenant Restriction** tab.
3. Click the slider to enable (green) or disable (gray) the **Tenant Restriction** policy for the account.

## Adding Tenant Restriction Rules

When you add a rule to the Tenant Restriction policy, configure each section in the rule that is required to define the tenant access for that app.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31556465303709.png)

### Creating Tenant Restriction Rules

Create a new Tenant Restriction rule and configure the rule's settings to implement tenant control for your organization. The **Injected Headers** fields can contain only the following characters:

- **Header Name** - **a**-**z**, **A**-**Z**, **0**-**9**, and special characters: **_** and **-**
- **Header Value** - **a**-**z**, **A**-**Z**, **0**-**9**, and special characters: **_ :;.,\/"'?!(){}[]@<>=-+*#$&`|~^&**

![Tenant_control_nonpolicy_new_rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27468567339165.png)

**To create a new Tenant Restriction rule:**

1. From the navigation menu, select **Security > App & Data Inline**.
2. Select the **Tenant Restriction** tab.
3. Click **New**. The **New Rule** panel opens.
4. Enter a **Name** for the rule.
5. Configure the **Position** for the rule in the rulebase.
6. Expand **Source** and select the source type.
  - Select the type (for example: Host, Network Interface, IP, Any). The default value is **Any**.
  - When needed, select a specific object from the drop-down list for that type.
7. Select a SaaS **Application** from the drop-down menu.
8. Define each **Header Name** and **Header Value** for the configured application (see below for more information).
9. Select the **Action** for this rule. The options are **Inject Headers** and **Bypass**.
10. **(Optional)** Configure the **Time** options that define when this rule is enabled.
11. Click **Save**.

The changes are saved to your unpublished revision, and are available for editing until they are published or discarded.

## Adding Custom Headers for SaaS App

The **Header Name** and **Header Value** fields define the app and the action the Tenant Restriction Policy enforces. These fields are specific to each app. Below are examples of required fields for commonly used apps. To ensure you have the latest information, we recommend checking the apps's documentation.

### ChatGPT

ChatGPT requires the following header and value to enforce tenant restrictions. For more information, see the [OpenAI documentation](https://help.openai.com/en/articles/20001323-corporate-network-controls-in-chatgpt-enterprise).

| Header | Header Value |
| --- | --- |
| `Chatgpt-Allowed-Workspace-Id` | `OpenAI Workspace ID (UUID)` |

### Claude

Claude requires the following header and value to enforce tenant restrictions. For more information, see the [Claude documentation](https://support.claude.com/en/articles/13198485-enforce-network-level-access-control-with-tenant-restrictions).

| Header Name | Header Value |
| --- | --- |
| `anthropic-allowed-org-ids` | `Your organization's team ID` |

### Microsoft 365

Microsoft 365 requires two headers to enforce tenant restrictions. Add the following two rules in this order. For more information, see the [Microsoft documentation](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/tenant-restrictions).

| Header Name | Header Value |
| --- | --- |
| `Sec-Restrict-Tenant-Access-Policy` | `restrict-msa` |
| `Restrict-Access-To-Tenants` or `Restrict-Access-Context` | Your organization's domain, for example `bbbbcccc-1111-dddd-2222-eeee3333ffff` |

For example:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(75).png)

### Slack

Slack requires two headers to enforce tenant restrictions. For more information, see the [Slack documentation](https://slack.com/help/articles/360024821873-Approve-Slack-workspaces-for-your-network).

| Header Name | Header Value |
| --- | --- |
| `X-Slack-Allowed-Workspaces-Requester`, `X-Slack-Allowed-Workspaces` | Your organization's workspace ID |

### Google Suite

Add the following header and value to enforce tenant restrictions. For more information, see the [Google documentation](https://support.google.com/a/answer/1668854).

| Header Name | Header Value |
| --- | --- |
| `X-GooGApps-Allowed-Domains` | Your organization's domain |

For example:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(76).png)

### Dropbox

Add the following header and value to enforce tenant restrictions. For more information, see the [Dropbox documentation](https://help.dropbox.com/security/network-control).

| Header Name | Header Value |
| --- | --- |
| `X-Dropbox-allowed-Team-Ids` | Your organization's team ID |
