---
title: "Slack: Configuring the Interconnected Apps Integration"
slug: "slack-configuring-the-interconnected-apps-integration"
status: "update"
updated: 2026-09-03T11:58:30Z
published: 2026-09-03T11:58:30Z
canonical: "knowledge.catonetworks.com/slack-configuring-the-interconnected-apps-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack: Configuring the Interconnected Apps Integration

This article explains how to configure the Interconnected Apps integration for Slack.

## Overview

Interconnected Apps provides you with visibility into third-party plugins connected to sanctioned SaaS applications. To provide Cato with visibility of data within an app, you need to set up an integration with the required application. For more information, see [Viewing and Analyzing Interconnected Apps](%%LINK:33492823254813%%).

To configure the Interconnected Apps integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the Cato Management Application (CMA)

A CASB license is required for Interconnected Apps. For more about purchasing a CASB license, please contact your Cato representative.

## Configuring the Slack Integration

To configure the Slack integration, create an app.

### Prerequisites

- Slack Enterprise Grid license

### Step 1: Configure the Integration in your Slack Tenant

In the Slack API Portal, identify the OAuth Token to enter into the CMA.

**Note**: The same token can be used for both the [Slack integration](/v1/docs/slack-configuring-the-app-activities-integration) configured for App Activities, and the Slack Interconnected Apps Integration. If you already configured Slack Activities, add the `admin.apps:read` scope to your existing app (see Step 6 for more information) and reinstall it to update the token permissions. If you do not have the Slack integration configured for App Activities, begin from Step 1.

**To configure the Slack integration:**

1. In the [Slack API Portal](https://api.slack.com/apps), click **Create an App**.

The **Create an app** dialog box opens.
2. Select **From scratch**.

![From_Sctrach.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33643842377629(1).png)
3. Add a name for the app and select the workspace you would like to integrate with Cato.

![Name.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33643826115485(1).png)
4. Click **Create App**.
5. Navigate to **OAuth & Permissions**.
6. In the **Scopes Section**>**User token scopes**, click **Add an OAuth Scope**, and add the following scopes as **User Token Scopes**:
  - admin
  - admin.apps:read
  - admin.teams:read
  - auditlogs:read
  - users:read
  - users:read.email
7. In the **OAuth Tokens** section, click **Install to <workspace>**.
8. Click **Allow**.
9. Copy and save the **User OAuth Token** so it can be added to the CMA.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop-down select **Third Party Apps**.
6. Add the details created during step one.
7. Click **Save**.
8. The app is visible on the **Integrated Apps** table with a **Connected** status.

After connecting your APIs, you can track the interconnected apps on the **Plugins** page. Data may take a few minutes to appear.

**Note**: The same token can be used for both Slack Activities and Slack Third Party Apps connectors. If you already configured Slack Activities, simply add the `admin.apps:read` and `admin.teams:read` scopes to your existing app and reinstall it to update the token permissions.
