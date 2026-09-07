---
title: "Using the App Catalog"
slug: "using-the-app-catalog"
updated: 2026-09-07T11:26:19Z
published: 2026-09-07T11:26:19Z
canonical: "knowledge.catonetworks.com/using-the-app-catalog"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the App Catalog

The App Catalog helps you evaluate cloud-based and on-premise applications based on their security posture, compliance status, and usage context. It’s integrated into the Cato Management Application (CMA), so you can make real-time, informed decisions with up-to-date app data and immediately apply them in your organization's policies and rulebases.

## Overview

The App Catalog is a dynamic resource and is continuously updated by Cato’s Security Research team. This ensures you always have access to the latest information on thousands of apps and services, including Cato-specific metadata such as risk scores and CASB activities. It contains general information, compliance, and security data, and lets you learn more about an app and decide how to use the app in your organization. All the apps and services can be used in the policies and rulebases in the CMA.

The data for each app is an automated process based on a proprietary Cato tool that is maintained by the Security Research team, which compiles these fields for every app: description, compliance, security, and risk score. For more information, see this [blog post](https://www.catonetworks.com/blog/cato-application-catalog-how-we-supercharged-application-categorization-with-ai-ml/).

## Getting Started with the App Catalog

The App Catalog provides information on thousands of apps and services, helping organizations assess usage and integrate them into policies and rulebases within the CMA.

![CloudAppsCatalog.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35513724754845.png)

**To show the App Catalog:**

- From the navigation menu, select **Resources > App Catalog**.

The App Catalog has these columns:

- **Logo** and **Name** of the app.

Apps are labeled **New** for 30 days after they are added to the catalog. You can use the **Status** drop-down menu to filter the catalog to show only new apps.
- A **Description** of the app
- Cato **Category** that the app belongs to. **Note:** Some apps have more than one Category. To apply a rule to these apps, include all their categories in the rule.
- **Risk** score for the app (Cato provides a risk score for each application between 0 (no risk) and 10 (very high risk). The risk score is calculated based on the analysis of millions of data flows. You can edit the risk score for your account. For more information, see below, [Understanding the Risk Score](/v1/docs/using-the-app-catalog#understanding-the-risk-score).
- **Sanctioned** - Shows if the app has been defined as a sanctioned app. For more about sanctioned vs. unsanctioned apps, see [Using the Applications Dashboard](/v1/docs/using-the-applications-dashboard).
- App **Type** - Cloud, on-premise, or service

### Understanding an App

Click an app to show the following additional information and options:

- Click **Add to Sanctioned Apps** to include the app in the Sanctioned Apps category for your organization's Application Control policy. You can also click ![RemoveApp.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35513741021597.png) to remove an app from the Sanctioned Apps category
- **General** information about the app and the company that created it
- **Compliance** shows which standards the app is compliant with and supports
- **Security** shows the security features that the app supports
- **Activities** - Shows the granular activities that are available for the app in [Application Control](/v1/docs/what-is-the-unified-casb-solution) rules. If there are fields that can be configured for an activity, they are listed under the activity. For example, the catalog shows that one of the activities you can add to a rule for Slack is **Add Reaction**, and that you can configure a specific **Reaction name** for the activity. For more about configuring Application Control rules, see [Managing the Application Control Policy](/v1/docs/managing-the-application-control-policy).

For more information, see [Understanding the Fields in the App Catalog](/v1/docs/understanding-the-fields-in-the-app-catalog).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/App Cat1.png)

### Viewing the App Inventory

The Inventory tab in the Applications Dashboard shows all the apps used in your environment, including how they are used, their risk score, and whether they are sanctioned or unsanctioned. This helps you move from reviewing an app in the App Catalog to understanding how the app is actually used in your account.

When you click **View App Inventory**, the Applications Dashboard opens to the Inventory tab. From there, you can easily view who is using the app and the traffic throughput.

### Understanding a Service

Expand a service to show the following additional information:

- **General** information about the service and protocols it uses
- **Standard Ports** - The common ports used by the service

## Understanding the Risk Score

Cato assigns each app a default risk score between 0 (no risk) and 10 (very high risk) to help you evaluate if the app meets the requirements of your security policy. You can also edit and override the default risk score for your account to customize the score for your organization’s security requirements.

The risk score is divided into the following risk levels:

- Low - apps with a risk score between 0 - 3
- Medium - apps with a risk score between 4 - 6
- High - apps with a risk score between 7 - 10

Risk score is used in event logs, App Analytics, and other dashboards, and for [Application Control](/v1/docs/managing-the-application-control-policy) rules that use risk score in the rule criteria.

### Use Case

The security team for Example Corp. assessed acceptable risk levels for the organization and decided to create an Application Control rule that blocks access to all cloud apps with a risk score of 5 or above. However, the company uses Anthropic AI systems for business-critical activities, and Anthropic has a default risk score of 5. After thorough research, the Example Corp. security team decides that the app entails lower risk than the default score indicates. The team edits the risk score to 2, and the app is no longer blocked by the Application Control policy.

### The Cato Risk Score

Cato uses an in-house artificial intelligence engine to analyze the relevant data and metrics and generate the risk score, including:

- General, Compliance, and Security data (shown in the App Catalog)
- Sentiment analysis (machine learning technique) based on recent news articles regarding the company
- Information about relevant software vulnerabilities and breaches
- Internal threat intelligence and domain-related information from the Cato Research Labs

For more information, see [Understanding the Fields in the App Catalog](/v1/docs/understanding-the-fields-in-the-app-catalog).

## Customizing the Risk Score

Create a custom app risk score from the relevant row in the App Catalog page. When you edit the score, it overrides the Cato-defined default risk level wherever the app risk is used in your account. After an app risk is edited, check which admin edited it and the time it was last modified by clicking the edit icon. You can also use the **Edited Risk** filter to show only the apps with edited risk scores.

![App_Catalog_Edit_Risk.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35513756274589.png)

**To edit an app risk score:**

1. From the navigation menu, select **Resources > App Catalog**.
2. In the row of the app, hover the mouse in the **Risk** column and click the edit icon. The **Edit Custom Application Risk** panel opens.
3. Under **Edit Application Risk**, enter the risk score.
4. Click **Apply**. The risk score is updated for the application and applied to all policies that use it.
