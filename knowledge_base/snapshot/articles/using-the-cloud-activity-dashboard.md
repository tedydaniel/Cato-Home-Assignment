---
title: "Using the Cloud Activity Dashboard"
slug: "using-the-cloud-activity-dashboard"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/using-the-cloud-activity-dashboard"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Cloud Activity Dashboard

This article explains how to use the Cloud Activity Dashboard to monitor activities within SaaS applications.

## Overview

The Cloud Activity Dashboard provides centralized and comprehensive visibility of user activities in the SaaS applications used in your ecosystem. The dashboard contains data from multiple features to combine sanctioned and unsanctioned apps that are monitored both in-line and out-of-band. This enables you to detect any anomalies, ensure compliance, and streamline incident response across from a single dashboard.

The Cloud Activity Dashboard lets you monitor:

- User activity in shadow IT and sanctioned apps
  - Based on in line traffic inspection from your Application Control policy, you can view the activities taken by each user
  - This data is only displayed in the Cloud Activity Dashboard if Application Control and TLS inspection are enabled
  - For more information, see [Cloud Access Security Broker (CASB)](/v1/docs/application-control-casb)
- Every activity from unmanaged and managed users
  - Based on API integration with sanctioned apps
  - For more information, see [What is App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities)
- Sign ins to sanctioned applications
  - Based on users signing into an application with SSO and an API integration with your identity provider
  - Supported for Entra ID
  - For more information, see [Configuring the Microsoft Entra ID (Azure AD) Connector](/v1/docs/configuring-the-microsoft-entra-id-azure-ad-connector) and [Configuring the Microsoft Entra ID Protection Connector for Sign-In Anomaly Data](/v1/docs/configuring-the-microsoft-entra-id-protection-connector-for-sign-in-anomaly-data)

> [!NOTE]
> Note:
> 
> Some widgets in the dashboard require [App Control](/v1/docs/managing-the-application-control-policy) to be enabled with a rule that monitors all cloud activities across all cloud applications.

### Understanding General Components of the Cloud Activity Dashboard

The widgets within the **Audit Activities** section contain two components to help you identify usage trends:

- **Inline / APIs Toggle:** This toggle switches the data between apps monitored in-line and apps monitored by API.
- **Growth/Decline Indicator:** If a specific metric has changed by more than 100% over the defined period, an arrow appears next to the metric. If there has been an increase, there is a red arrow pointing up. If there is a decrease, there is a green arrow pointing down. By hovering over the metric, you can view the exact percentage change.
- **Activities Categories:** The activities taken in an app are grouped into Activity Categories in the dashboard. This lets you track, filter, and visualize SaaS activity, to manage and investigate user behavior efficiently. For more information, see [What is Application Control via API with Audit Activities?](/v1/docs/what-is-application-control-via-api-with-app-activities).

### Use Cases

These are examples of insights you can gain from the Cloud Activity Dashboard widgets:

- **Suspicious Downloads:** Detect large or unusual data downloads. For example, a specific employee downloading significantly more data than normal, which could indicate data exfiltration or insider threats.
- **Permission Changes:** Track and review instances where a user's permissions are altered, helping to identify unauthorized access or privilege escalations.

## Getting Started with the Cloud Activities Dashboard

The Cloud Activity Dashboard is split into three sections:

- **Overview:** A high-level summary of the number of apps used in your ecosystem
- **Audit Activities:** A summary of actions taken, the apps involved, and the users who performed them for both in-line and out-of-band apps.
- **SSO Sign-Ins:** Visibility for SSO sign-in events in your organization's Microsoft Entra ID tenant

These tables explain the widgets in the Cloud Activities Dashboard.

### Understanding the Overview Section

This table explains the widgets in the Overview section:

![Overview1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24479766797853.png)

| Name | Description |
| --- | --- |
| Apps Monitored Inline | The number of apps monitored by Cato CASB Solution. This value isn't impacted when you change the time range or a filter. |
| Apps Monitored via API | The number of apps monitored by API. This value isn't impacted when you change the time range or a filter. |
| Unsanctioned | The number of unsanctioned apps used in your account. This value isn't impacted when you change the time range or a filter. |
| Accessed Outside of Cato | Number of Apps accessed outside of Cato (like in Cloud Applications – appear only when EntraID is configured). |

### Understanding the Audit Activities Section

This table explains the widgets in the **Audit Activities** section:

| Name | Description |
| --- | --- |
| Activities Over Time | Frequency each Activity Category has occurred during the time range and filter. |
| Users | Frequency each user has completed an activity. |
| Activities Distribution | Distribution each activity has occurred as a percentage of total activities. |
| Applications | Frequency an activity has occurred in each application. |
| Files | Files that have been uploaded or downloaded. |

### Understanding the SaaS Anomalies Section

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36144411072797.png)

The SaaS Anomalies section contains two widgets, The **SaaS Findings**, displays the number of SaaS Anomalies events by their title or Severity. The Applications widget displays the applications the SaaS Anomalies were detected in.

### Understanding the SSO Sign Ins Section

This table explains the widgets in the **SSO Sign In** Section:

![SSO_section.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24479805734173.png)

| Name | Description |
| --- | --- |
| Sanctioned Apps Sign-In Activity | Shows SSO sign-in information for all of your organization's sanctioned SaaS apps that use SSO. You can click in the row of an app to show the Events page pre-filtered for sign-in events for the app. These are the widget columns: - **# Sign-in** - Total number of sign-ins for the app, including successful and failed sign-ins - **# Outside Cato** - Indicates users who authenticated to an app directly over the public Internet and not via the Cato Cloud. App traffic over the public internet isn't protected by the Cato Cloud Security services. - **# Failed Sign-in** - Number of failed sign-in attempts for the app - **# Tenants** - Number of Entra ID tenants associated with the sign-ins to this app. This number can include tenants external to your organization if you have configured [External ID cross-tenant access](https://learn.microsoft.com/en-us/entra/external-id/cross-tenant-access-overview), and a sign-in was performed from a source outside your organization. - Hover the mouse over the number of tenants and then hover over the tooltip to show the tenant IDs as they appear in sign-in events for the app. You can use the tenant ID to filter the Events page to show events for that tenant. If a sign-in was performed from a source outside your organization, you can use the tenant ID to view details about the external source in the associated event Click in the row of an app to show the Events page pre-filtered for sign-in events for the app |
| Activity Categories by Countries | Shows the following information for sign-ins from each country: - **# Sign-in** - Total number of sign-ins for the country, including successful and failed sign-ins - **# Failed Sign-in** - Number of failed sign-in attempts for the country |
| Top Users With Failed Sign-in | A list of users with the most failed sign-ins for a single app, with the name of the app and number of failed sign-ins. |
| Top Sign-ins Outside of Cato | A list of users with the most sign-ins for a single app outside of, with the name of the app and number of failed sign-ins. |
| Top Sign-in Anomalies | A list of users with the most sign-in anomalies. |
| Sign-in Activity Over Time | Graphs the total and failed sign-ins on a timeline - Hover the mouse on the graph to show the sign-in details for a point on the timeline - Click a toggle button to show or hide a graph - Click and drag to zoom-in on: - Time of sign-ins - Number of sign-ins |
| Anomalies | Anomalous sign-ins in your Entra ID tenant that may indicate malicious activity. Anomaly types include: Atypical travel, Anomalous token, Suspicious browser, Unfamiliar sign-in properties, Malicious IP address, Suspicious inbox manipulation rules, Password spray, Impossible travel, New country, Activity from anonymous IP address, Suspicious inbox forwarding, Mass access to sensitive files, Verified threat actor IP, Additional risk detected, Anonymous IP address, Admin confirmed user compromised, Microsoft Entra threat intelligence. |
| Sign-in Break Down by OSs | Shows number of app sign-ins performed on each operating system. Hover the mouse over a chart section to show the number of sign-ins for that operating system and its percentage of total sign-ins. |
| Sign-in Break Down by Browser | Shows number of app sign-ins performed on each browser. Hover the mouse over a chart section to show the number of sign-ins for that browser and its percentage of total sign-ins. |
