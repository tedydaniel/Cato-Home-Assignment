---
title: "Make: Configuring the App Activities Integration"
slug: "make-configuring-the-app-activities-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/make-configuring-the-app-activities-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Make: Configuring the App Activities Integration

This article explains how to configure the App Activities integration for Make.

## Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

## Configuring the Make Integration

To configure the Make integration, create a **Token**, **Organization Name** and **Zone Domain**.

### Prerequisites

- You must have an Enterprise License

### Step 1: Configure the Integration in the Make Portal

In the Make portal, create the required information to be added to the CMA.

**To configure the integration in the Make portal:**

1. Sign into you Make account.
2. Click your avatar at the bottom-left corner of the page, and select **Profile**.
3. On the **API/MCP Access** tab, click **Add Token**.
4. Select these configurations:

![image-20250805-084226.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31660971511453.png)
  - **Type**: API Token
  - **Scope**:
    - organizations:read
    - admin:read
    - scenarios:read
    - connections:read
    - hooks:read
    - keys:read
    - teams:read
    - functions:read
    - ai-agents:read
  - **Label**: Create your one label
5. Click **Save**.
6. Copy and save the generated **API Token** so it can be entered into the CMA.
7. From the navigation bar, click **Organization**.
8. On the **Variables** tab copy and save the **Organization Name** and **Zone Domain** so they can be entered into the CMA.

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
