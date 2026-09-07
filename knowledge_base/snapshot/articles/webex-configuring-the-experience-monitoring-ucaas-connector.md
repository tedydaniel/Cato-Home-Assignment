---
title: "Webex: Configuring the Experience Monitoring UCaaS Connector"
slug: "webex-configuring-the-experience-monitoring-ucaas-connector"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/webex-configuring-the-experience-monitoring-ucaas-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Webex: Configuring the Experience Monitoring UCaaS Connector

This article explains how to configure the Experience Monitoring Integration for Webex.

## Overview

Experience Monitoring provides enhanced context, such as packet loss or tunnel age, to give you the information you need to determine if the issues are related to your ISP, the Cato Cloud, or other sources.

You can also configure a connector with UCaaS applications to display application-specific metrics in the CMA to monitor the user experience when using the application.

To configure the Experience Monitoring UCaaS Connector, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A DEM license is required to display Application-Specific Metrics. For more about purchasing a DEM license, please contact your Cato representative.

## Configuring the Webex Experience Monitoring Integration

To configure the Webex integration, create a Client ID and Client Secret to be entered into the CMA.

### Prerequisites

- You must have a Webex Enterprise license

### Step 1: Configure the Integration in the Webex Developer Portal

In the Webex Developer Portal, create the required information to be added into the CMA.

**To configure the Webex Integration:**

1. Sign in to the Webex Developer Portal `https://developer.webex.com/my-apps`.
2. Click **Create New App**.
3. In the **Integration** box, select **Create an Integration**.

![image-20250803-131515.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35976693330461.png)
4. Choose an **Integration Name** and add an **Icon** and **App Hub Description**.
5. In the **Redirect URI(s)** field, enter:

`https://cc.catonetworks.com/redirect/cas/appconnector/callback`
6. Under **OAuth Scopes,** add the following:
  - `analytics:read_all`
  - `meeting:admin_schedule_read`
  - `meeting:schedules_read`
7. Click **Add Integration**.
8. On the integrations overview page, copy and save the **Client ID** and **Client Secret** so they can be entered into the CMA.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To add create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**. The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop down select **Experience Monitoring**.
6. Add the details created during step one.
7. Click **Save**.
8. In the Webex login window, log in with your Webex credentials.
9. Click **Accept**. (This page is only displayed if this is the first Webex connector you have created with Cato)

![image-20250826-123213.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35976710219933.png)
