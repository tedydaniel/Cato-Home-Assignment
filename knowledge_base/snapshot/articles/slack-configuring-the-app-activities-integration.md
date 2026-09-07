---
title: "Slack: Configuring the App Activities Integration"
slug: "slack-configuring-the-app-activities-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/slack-configuring-the-app-activities-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack: Configuring the App Activities Integration

This article explains how to configure the App Activities integration for Slack

## Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

### Benefits of Connecting Slack

After creating this connector, you can view and monitor activity in your Slack environment, for example:

- File upload
- Channel modifications
- New 3rd-party app integrations
- Private message forwarding

This helps you identify and respond to suspicious activity, and you can receive alerts for these activities:

- Anomalous activity based on actor attributes (email, IP, etc…)
- Malicious file uploads

## Configuring the Slack Integration

To configure the Slack integration, create an app.

### Prerequisites

- Slack Enterprise Grid license

### Step 1: Configure the Integration in your Slack Tenant

In the Slack API Portal, identify the OAuth Token to enter into the CMA.

**To configure the Slack integration:**

1. In the [Slack API Portal](https://api.slack.com/apps), click **Create an App**.

The **Create an app** dialog box opens.
2. Select **From scratch**.

![From_Sctrach.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31593196209053.png)
3. Add a name for the app and select the workspace you would like to integrate with Cato.

![Name.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31593163441693.png)
4. Click **Create App**.
5. Navigate to **OAuth & Permissions**.
6. In the **Scopes Section**, click on **Add an OAuth Scope** add the following scopes as **User Token Scopes**:

![Scopes.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31593147972893.png)
  - users:read
  - users:read.email
  - Auditlogs:read
7. In the **OAuth Tokens** section, click **Install to <workspace>**.
8. Click **Allow**.
9. Copy and save the **User OAuth Token** so it can be added to the CMA.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Integrated Apps** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop down select **App Activities**.
6. Add the details created during step one.
7. Click **Save**.
8. The app is visible on the **Integrated Apps** table with a **Connected** status.

After connecting your APIs, you can track the App activities in the [Cloud Activities dashboard](/v1/docs/using-the-cloud-activity-dashboard). Data may take a few minutes to appear.
