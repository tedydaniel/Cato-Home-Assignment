---
title: "Google Workspace: Configuring the Interconnected Apps Integration"
slug: "google-workspace-configuring-the-interconnected-apps-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/google-workspace-configuring-the-interconnected-apps-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Workspace: Configuring the Interconnected Apps Integration

This article explains how to configure the Interconnected Apps integration for Google Workspace.

## Overview

Interconnected Apps provides you with visibility into third-party plugins connected to sanctioned SaaS applications. To provide Cato with visibility of data within an app, you need to set up an integration with the required application. For more information, see [Viewing and Analyzing Interconnected Apps](/v1/docs/viewing-and-analyzing-interconnected-apps).

To configure the Interconnected Apps integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the Cato Management Application (CMA)

A CASB license is required for Interconnected Apps. For more about purchasing a CASB license, please contact your Cato representative.

### Benefits of Connecting Google Workspace

After creating this connector, you can gain visibility into:

- **App inventory**: See all OAuth apps authorized by users in your organization
- **Permission analysis**: Understand what permissions (scopes) each app has been granted, classified as LOW / MEDIUM / HIGH
- **User mapping**: Know which users authorized apps
- **Risk assessment**: Identify high-risk applications with broad permissions (e.g., full Drive access, email read/write)

## Configuring the Google Workspace Integration

To configure the Google Workspace integration, create a new project.

### Prerequisites

- You must have purchased a Google Cloud Enterprise license

### Step 1: Configure the Integration in the Google Cloud Console

In the Google Cloud Console, create a Service account private key to enter into the CMA.

**To configure the Google Workspace integration:**

1. In your [Google Cloud Console](https://console.cloud.google.com/), click **Select a Project**.
2. Click **New project**.

![Google1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35485388738205.png)
3. Choose a **Name** and **Location** and click **Create**.
4. Navigate to **APIs & Services > Library**.
5. Search for Admin SDK.

![Google_2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35485415969053.png)
6. Click on **Admin SDK API** and click **Enable**.

![Google3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35485380160285.png)
7. Navigate to **IAM & Admin > Service Accounts**.
8. Select the project you created in step two, and click **Create service account**.
9. Add a **Service account ID** and click **Create and continue**.
10. Click **Done**. (No role is required for this connector)
11. Click on the service account you created and navigate to the **Keys** tab,
12. Click **Add key > Create new key**.
13. Choose the JSON key type and click **Create**.

A JSON file containing the private key is downloaded.
14. Copy and save the **Private key** so it can be added to the CMA.
15. In the [Google Admin console](https://admin.google.com/), navigate to **Security > Access and Data Control > API control**.
16. Under **Domain wide delegation**, select **Manage Domain Wide Delegation**.
17. Click **Add new**.
18. Add the **Client ID** of the Service Account. You can find this in the Service Account page.
19. Add these scopes:
  1. `https://www.googleapis.com/auth/admin.directory.user.readonly`
  2. `https://www.googleapis.com/auth/admin.directory.user.security`
20. Click **Authorize**.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop down select **Third Party Apps**.
6. Add the details created during step one.
7. Click **Save**.
8. The app is visible on the **Integrated Apps** table with a **Connected** status.

After connecting your APIs, you can track the interconnected apps on the **Plugins** page. Data may take a few minutes to appear.
