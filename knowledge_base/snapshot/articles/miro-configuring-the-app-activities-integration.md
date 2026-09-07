---
title: "Miro: Configuring the App Activities Integration"
slug: "miro-configuring-the-app-activities-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/miro-configuring-the-app-activities-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Miro: Configuring the App Activities Integration

This article explains how to configure the App Activities integration for Miro.

## Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

## Configuring the Miro Integration

To configure the Make integration, create a Client ID and Client Secret.

### Prerequisites

- You must has a Miro Enterprise license

### Step 1: Configure the Integration in the Miro Developer Portal

In the Miro Developer Portal, create the required information to be added to the CMA.

**To configure the integration in the Miro portal:**

1. Sign into the Miro Developer Portal (`https://developers.miro.com/`).
2. In the left hand menu, navigate. to **Your Apps**.
3. Click **Create new app**.
4. Choose an **App name** and select the correct developer team from the drop down.

**Note**: Do not check the **Expire user authorization token** checkbox.
5. In the app settings, navigate to **Redirect URI for OAuth2.0**.
6. In the **Redirect URI for OAuth2.0** field, add:

![image-20260204-154511.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34971832556445.png)
  - `https://cc.catonetworks.com/redirect/cas/appconnector/callback`
7. Click **Add**.
8. Select these permissions:
  - boards:read
  - identity:read
  - team:read
  - auditlogs:read
  - organizations:read
  - organizations:teams:read
  - projects:read
9. In the app settings, copy and save the **Client ID** and **Client Secret** so they can be entered into the CMA.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop down select **App Activities**.
6. Add the details created during step one.
7. Click **Authorize**.
8. In the Miro authorization window, select your team from the dropdown, review the permissions and click **Add**.
9. The app is visible on the **Integrated Apps** table with a **Connected** status.

After connecting your APIs, you can track the App activities in the [Cloud Activities dashboard](/v1/docs/using-the-cloud-activity-dashboard). Data may take a few minutes to appear.
