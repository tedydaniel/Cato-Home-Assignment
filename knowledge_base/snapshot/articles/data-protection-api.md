---
title: "What is the Data Protection API?"
slug: "what-is-the-data-protection-api"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/what-is-the-data-protection-api"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is the Data Protection API?

This article provides an overview and background information about Cato's out-of-band Data Protection API service to monitor and control traffic to sanctioned SaaS cloud apps.

> [!NOTE]
> Note:
> 
> Please contact [SaaSecAPI@catonetworks.com](mailto:SaaSecAPI@catonetworks.com) or your official Cato reseller for more information about using the Data Protection API policy.

## Overview of Data Protection API

Data Protection API provides out-of-band visibility and control for sanctioned cloud apps. Other security features (such as CASB) can only control and monitor traffic that goes over the Cato Cloud. Data Protection API gives the ability to also monitor and react to traffic from remote users that connect directly to the cloud apps. This applies even when they are not using the SDP Client to send traffic over the Cato Cloud.

Data Protection API inspects the content of a connection without using TLS Inspection. This is especially beneficial to accounts that don't have TLS Inspection enabled. However, even for accounts that are using TLS Inspection, some cloud apps can't be inspected due to issues related to certificate pinning. Data Protection API compliments Cato's inline CASB and DLP solutions to provide the best security coverage.

For some apps you can create Threat Protection rules for the connector to provide out-of-band Anti-Malware protection by scanning files and attachments for malware and viruses using the Anti-Malware and Next Gen Anti-Malware engines that are enabled for your account. The Data Protection API engine scans the connector traffic and applies the action and tracking options that you configure for the rule.

### Prerequisites

- To add a connector, you must have editor permission for **Integrations** (in the **Resources** section) and **App & Data API Protection** (in the **App & Data Control** section). For more information, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).

## Implementing Data Protection API in Your Account

This is a high-level overview of the steps to implement Data Protection API .

1. Create the connectors for the relevant cloud apps.

For Microsoft apps, it is necessary to create a Microsoft 365 parent connector and then a child connector for each app.
2. Create (or review) the DLP Content Profile that defines the sensitive data that Data Protection API is scanning for (see [Creating DLP Content Profiles](/v1/docs/creating-dlp-content-profiles)).
3. Create the rules for the Data Protection policy.

## Supported Data Protection API Connectors

Cato supports a wide range of applications and continuously expands the list. To view the complete list of supported applications, see [Data Protection API](/v1/docs/data-protection-api).

## Known Limitations for Data Protection API

These are limitations that apply to any connector used in the Data Protection policy. For limitations related to specific SaaS apps, see below [Known Limitations for Specific Connectors](/v1/docs/what-is-the-data-protection-api#known-limitations-for-specific-connectors).

- Can’t edit Data Protection API connectors.

Workaround - delete the connector and create a new connector with the required settings.
- It may take up to 15 minutes for file changes to be detected.
- For Anti-malware scans, allowlisting with file hash isn’t supported.
- Changes to permissions for folders and directories are not scanned.
- Actions for groups (such as file sharing with a group) are not scanned.
- Maximum supported file size for DLP and Anti-Malware scans is 500MB.
- For DLP and Anti-Malware scans, Data Protection API only supports file types supported by the Cato DLP and Anti-Malware engines.
- When Data Protection API rules are created, deleted, or edited, the changes are tracked in the Audit Trail without showing details relating to the rule content
- .log file extensions are not supported
- Binary files are not supported for the GitHub connector.

### Known Limitations for Specific Connectors

These are limitations for the specific Data Protection API connectors.

- Azure
  - New users that are added after the connector is created are not scanned.

Workaround - create a new rule for the connector, or disable and then re-enable the Data Protection API policy.
- Box
  - New users that are added after the connector is created are not scanned.

Workaround - create a new rule for the connector, or disable and then re-enable the Data Protection API policy.
  - New files added to the root folder can take up to 24 hours before they are scanned and before rule actions are applied to them. Files in sub-folders are scanned immediately after they are uploaded.
  - Only 1 connector per tenant is supported. (Microsoft and Google connectors support multiple connectors per tenant)
- Exchange
  - For rules that scan email activity, the event can also include an attached file (even if the file does not match the policy).
- Google Drive
  - Only commercial accounts are supported for the Google Drive connector.
- OneDrive
  - When there are SharePoint and OneDrive connectors for the same resource, each connector creates a separate event for the same action.
  - One Drive can take up to 5 minutes to indicate a change in a file, which can cause delays in event generation.
- SharePoint
  - Only the **Documents** directory is scanned.
  - When there are SharePoint and OneDrive connectors for the same resource, each connector creates a separate event for the same action.
- Slack
  - Only 1 connector per tenant is supported. (Microsoft and Google connectors support multiple connectors per tenant)
  - Only public and shared channels are supported.
