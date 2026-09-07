---
title: "Box: Configuring the App Activities Integration"
slug: "box-configuring-the-app-activities-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/box-configuring-the-app-activities-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Box: Configuring the App Activities Integration

This article explains how to configure the App Activities integration for Box

## Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

## Configuring the Box Integration

To configure the Box integration create a Platform App.

### Prerequisites

- You must have purchased the Box Enterprise license

### Step 1: Configure the Integration in the Box Developer Center

In the Box Developer Center, identify the Enterprise ID and Client ID to enter into the CMA.

**To configure the Box integration:**

1. Login to the Box Developer Center (`https://&lt;your_tenant&gt;.app.box.com/developers/console`)
2. On the **My Platform Apps** page, click **Create Platform App**

![Box1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28529524444445.png)
3. Click **Custom App**.
4. Add a name for the app
5. In the **Purpose** field, select **Integration** and in the **Category** field, select **Security & Compliance** and click **Next**.
6. Select **Server Authentication (Client Credentials Grant)** and click **Create App**.

![Box2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28529524531741.png)
7. On the **General Settings** page, copy the **Enterprise ID** so it can be added into the CMA.
8. On the **Configuration** page:
  - Click **Fetch Client Secret**. Copy the **Client Secret** and the **Client ID** so they can be added into the CMA.

**Note:** Two Factor Authentication must be enabled for the Client Secret to be displayed.
  - Select **App + Enterprise Access**

![3f751e35-1734-4996-a6ae-aefff7de3ffe.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28529541557021.png)
9. On the **Authorization** page, click **Review and Submit**.
10. The Box account admin receives an email from which approval for the integration needs to be approved.

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

### Sources

- Login - using the OAuth endpoint
- Events - Querying the Events endpoint with the admin_logs stream_type

### Known Limitations

- All events are currently fetched
