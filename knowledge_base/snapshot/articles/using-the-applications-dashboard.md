---
title: "Using the Applications Dashboard"
slug: "using-the-applications-dashboard"
updated: 2026-06-28T10:27:41Z
published: 2026-06-28T10:27:41Z
canonical: "knowledge.catonetworks.com/using-the-applications-dashboard"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Applications Dashboard

This article explains how to use the Applications Dashboard to monitor how apps are used in your environment to understand usage and detect risky or unsanctioned apps.

## Overview

The Applications Dashboard provides centralized visibility into your organization's application usage. The dashboard shows which applications are being accessed, by whom, and whether they are sanctioned or unsanctioned. It also highlights usage patterns, user behavior, and associated risks to help you identify shadow IT and detect potentially risky applications.

With this visibility, IT and security teams can better understand app usage, strengthen policy enforcement, and plan more effective CASB and DLP rules. You can also update the sanctioned or unsanctioned status of an app directly from the dashboard, giving you greater control and enabling faster incident response.

By combining visibility with control, the Applications Dashboard helps reduce risk, ensure compliance, and protect sensitive data while still allowing employees to work with the tools they need.

A CASB license is required for the Apps Overview Dashboard. For more information about purchasing a CASB license, please contact your Cato representative.

### Use Case - Identifying Unsanctioned App Usage

The security team at company ABC needs to manage the growing number of SaaS and cloud apps used by employees. They have a sanctioned apps list and policies to enforce its usage. However, they lack full visibility into which apps are being accessed across the organization. This gap creates risk, as shadow IT and unsanctioned tools may expose sensitive data or bypass security controls.

To mitigate this risk and identify shadow IT and high-risk tools, the security team reviews the:

- **Top Applications widget** to see which cloud apps are used most frequently, including unsanctioned or risky apps
- **Risk Level widget** to highlight applications that pose security or compliance risks and prioritize which ones to address
- **Sanctioned Status** within the Top Applications widget to track which apps align with company policy and which should be restricted or blocked.

The security team identifies a number of risky applications that are mistakenly classified as unsanctioned. To reduce risk they sanction the risky applications within the Applications Dashboard.

## Getting Started with the Applications Dashboard

To access the Application Dashboard, navigate to **Security > Applications**.

The Application Dashboard is split into two tabs:

- **Overview**: This tab is split into 3 sections:
  - **Summary**: A high-level overview of the apps used in your ecosystem and the categories they are in
  - **Overview**: Gain visibility into apps used in your environment, their generated events, user activity, and actions taken
  - **Data Protection**: Insights into data policy violations and the users and files involved (A DLP license is required for this section)
- **Activities:** Centralized and comprehensive visibility of user activities in the SaaS applications used in your ecosystem. For more information, see [Using the Applications Activities Dashboard](/v1/docs/using-the-applications-activities-dashboard).
- **Inventory**: This tab lists all the apps used in your environment and provides high-level information about the app

## Understanding the Overview Tab

The **Overview** tab provides configurable widgets that analyze app usage in your environment

### Understanding the Summary Section

This table explains the widgets in the Summary section.

![OverviewApps1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32184046058781(1).png)

| Name | Description |
| --- | --- |
| Apps | How many apps are used. You can also view how many apps are used in your environment that can be integrated with Cato. For more information, see [App Control & Data Protection](/v1/docs/app-control-data-protection). |
| Classification | Number of sanctioned and unsanctioned apps used. |
| Risky Apps | Number of risky GenAI applications being used. You can change the risk score of an app for your account. For more information, see [Using the App Catalog](/v1/docs/using-the-app-catalog) . |
| Users | Number of users using GenAI apps. |

### 

### Understanding the Usage Flow Sankey Diagram

For increased visibility of how SaaS applications are used in your network, the a sankey diagram to visualize application usage flow in your network.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36318225382429.png)

### Understanding the Overview Section

This table explains the widgets in the **Overview** section. All widgets in this section can be filtered by the Number of Apps, Number of Users, or Usage.

![Overvierw_Apps_3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32184031158941(1).png)

| Name | Description |
| --- | --- |
| App Classification | Number of sanctioned and unsanctioned apps used. |
| App Risk | Number of apps being used slit by risk score. |
| TLS Inspection | Number of apps inspected by TLS. |
| App Categories | Number of apps split by category. |
| Users | Users with the highest network usage of apps. |
| Events by Action | Breakdown of the action Cato has taken on events generated by apps. |
| Activities Over Time | Most frequent user activities on apps over time. You can see the exact number of activities by clicking on the graph. This helps you detect anomalies in users activities. |
| Top Applications | Most frequently used applications. Clicking on an app opens the **App Quick View** draw which provides more detailed information about the app including Security & Compliance information, and the Throughput through the app. Click on the **Classification** to change the security status of the app directly from this draw. |

### 

### Understanding the Attack Surface Section

The Attack Surface section displays a summary of data gathered from SaaS Posture Connectors. For more information, see [Reviewing the Security Posture of Your SaaS Applications (SSPM)](/v1/docs/understanding-the-security-posture-of-your-saas-applications).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(26).png)

| Name | Description |
| --- | --- |
| SaaS Security Posture | The percentage of available checks that have passed. |
| Top 10 SaaS Posture Checks | The ten most severe SaaS posture checks that failed. |
| SaaS Posture Applications | SaaS applications available for posture monitoring. Connected applications display their number of failed checks, unconnected applications display a link to connect them. |

### Understanding the Data Protection Section

This table explains the widgets in the **Data Protection** section.

A DLP license is required to view this section. For more information about purchasing a DLP license, please contact your Cato representative.

| Name | Description |
| --- | --- |
| Violations by Data Type | Proportion of each data types involved in violations and the Top 4 apps with the most data violations. |
| Data Policy Violations Over Time | The amount of data policy violations over time. |
| Top Users Sharing Sensitive Data | List of the users who most frequently violate data policy. |
| Policy Violations | List of DLP rules that were most frequently violated. |
| File Uploads | List of the latest files uploaded to GenAI applications. |

## Understanding the Inventory Tab

For a high-level view, the **Inventory** tab provides a list of all the apps used in your environment, how they are used and their risk score and security status.

![Inventorty_tab.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32184054559773(1).png)

Clicking on an app opens the **App Quick View** draw which provides more detailed information about the app including Security & Compliance information, and the Throughput through the app. Click on the **Classification** to change the security status of the app directly from this draw.
