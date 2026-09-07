---
title: "Microsoft Teams: Configuring the Experience Monitoring UCaaS Connector"
slug: "microsoft-teams-configuring-the-experience-monitoring-ucaas-connector"
updated: 2026-07-20T12:58:38Z
published: 2026-07-20T12:58:38Z
canonical: "knowledge.catonetworks.com/microsoft-teams-configuring-the-experience-monitoring-ucaas-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Teams: Configuring the Experience Monitoring UCaaS Connector

This article explains how to configure the Experience Monitoring Integration for Microsoft Teams.

## Overview

Experience Monitoring provides enhanced context, such as packet loss or tunnel age, to give you the information you need to determine if the issues are related to your ISP, the Cato Cloud, or other sources.

You can also configure a connector with UCaaS applications to display application-specific metrics in the CMA to monitor the user experience when using the application.

To configure the Experience Monitoring UCaaS Connector, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A DEM license is required to display Application-Specific Metrics. For more about purchasing a DEM license, please contact your Cato representative.

## Configuring the Microsoft Teams Experience Monitoring Integration

To configure the integration, create an API app.

### Prerequisites

- You must have purchased a Microsoft 365 E3 license
- This permission is provided:
  - CallRecords.Read.All
- You have admin permissions for your Microsoft Entra admin center

#### Step 1: Create the Microsoft 365 Parent Connector

First, configure the MS Tenant integration as the parent connector. This connector can be used for all Microsoft integrations. If you have already created the parent connector, go to step 2.

**To create the MS Tenant integration:**

1. From the navigation menu, select **Resources > Integrations** and click the **Configured Integrations** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **New Connector** panel, select the **MS Tenant (Configure a new MS Tenant)** app.

![New_Microsoft_365_Connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35420003421981.png)
4. Enter the **Connector Name**.
5. Click **Authorize and Save**.

A new browser tab opens to the Microsoft 365 app.
6. In the new browser tab, authenticate to the Microsoft 365 app:
  1. Select the Microsoft account for the Microsoft 365 app.

Otherwise, there may be a Microsoft authentication error.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions to let Cato access the Microsoft 365 app.
  4. The screen shows that you have successfully applied the permissions for the app.

You can close the browser tab and return to the Cato Management Application.
7. The Microsoft 365 SaaS application is added to the **Integrated Apps** tab.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the Microsoft 365 parent connector:**

1. From the navigation menu, select **Resources > Integrations** and click the **Configured Integrations** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **New Connector** panel, select the **Microsoft Teams** app.

![New_Microsoft_365_Connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35420003421981.png)
4. In the **Auth** drop-down, select the **Microsoft Primary Tenant** that was created in Step 1.
5. (Optional) Add a description.
6. Select a **Parent ID**.
7. Click **Save**. The CMA connects to the vendor
8. Click **Authorize**.
9. A Microsoft permissions screen will appear.
10. Review the requested permissions and click **Accept.**

## Sources

- Login: OAuth2 endpoint
- Listing the calls: callRecords endpoint
- GET to the calls Quality of Service information from the callRecords endpoint

## Known Limitations

- All meetings are fetched
- There is a 30 minute delay in displaying Teams data
