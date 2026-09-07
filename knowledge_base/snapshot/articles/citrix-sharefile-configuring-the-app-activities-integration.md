---
title: "Citrix ShareFile: Configuring the App Activities Integration"
slug: "citrix-sharefile-configuring-the-app-activities-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/citrix-sharefile-configuring-the-app-activities-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Citrix ShareFile: Configuring the App Activities Integration

This article explains how to configure the App Activities integration for Citrix ShareFile.

## Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the Cato Management Application (CMA)

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

## Configuring the ShareFile Integration

In your ShareFile account, identify the Client ID and Client Secret.

### Step 1: Configure the Integration in your ShareFile Account

**To configure the ShareFile integration:**

1. Log in to your ShareFile account (https://api.sharefile.com/).
2. Click **Get an API Key / Request OAuth Key**.
3. Add the following details:
  - Application Name: Choose a name
  - Application Description: Add a description
  - Redirect URI: `https://cc.catonetworks.com/redirect/cas/appconnector/callback`
  - Contact / Company: Add your contact details
4. Click **Generate API Key**.
5. Copy and save the **Client ID** and **Client Secret** so they can be entered into the CMA.

#### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop down select **App Activities**.
6. Add the details created during step one.
7. Click **Save**.
8. The app is visible on the **Integrated Apps** table with a **Connected** status.

After connecting your APIs, you can track the App activities in the [Cloud Activities dashboard](/v1/docs/using-the-cloud-activity-dashboard). Data may take a few minutes to appear.
