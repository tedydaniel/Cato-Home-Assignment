---
title: "Dropbox: Configuring the App Activities Integration"
slug: "dropbox-configuring-the-app-activities-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/dropbox-configuring-the-app-activities-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dropbox: Configuring the App Activities Integration

This article explains how to configure the App Activities integration for Dropbox.

## Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Log in to your Dropbox account
2. Create the API connector in the CMA

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

## Configuring the Dropbox Integration

To configure the Dropbox integration, log in to your Dropbox account and create the connector in the CMA.

### Prerequisites

### Step 1: Log in to Dropbox

Log in to the Dropbox account you would like to integrate to Cato.

#### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. In a new tab, open the CMA and from the navigation menu, click **Resources > Integrations**.
2. Click the **Integrated Apps** tab.
3. Click **New**.

The **New Integration** panel opens.
4. In the **SaaS Application** dropdown, select **Dropbox**.
5. Add a **Name** and **Description**.
6. (Optional) Chose to track errors with the integration.
7. Click **Save**. The CMA connects to Dropbox.

![Dropbox2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28478652097565.png)
8. Click **Authorize**.

![Dropbox3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28478652123677.png)
9. Grant permissions to Cato Networks.
10. The app is visible on the **Integrated Apps** table with a **Connected** status.

After connecting your APIs, you can track the App activities in the [Cloud Activities dashboard](/v1/docs/using-the-cloud-activity-dashboard). Data may take a few minutes to appear.
