---
title: "Microsoft Entra ID: Configuring the Interconnected Apps Integration"
slug: "microsoft-entra-id-configuring-the-interconnected-apps-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/microsoft-entra-id-configuring-the-interconnected-apps-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Entra ID: Configuring the Interconnected Apps Integration

This article explains how to configure the Interconnected Apps integration for Microsoft Entra ID.

## Overview

Interconnected Apps provides you with visibility into third-party plugins connected to sanctioned SaaS applications. To provide Cato with visibility of data within an app, you need to set up an integration with the required application. For more information, see [Viewing and Analyzing Interconnected Apps](https://support.catonetworks.com/hc/en-us/articles/33492823254813#UUID-fa3baffc-3dbc-89fe-16f5-934d240df58f).

To configure the Interconnected Apps integration, you need to:

1. Create a MS Tenant integration as the parent connector
2. Create the API connector for interconnected Apps

A CASB license is required for Interconnected Apps. For more about purchasing a CASB license, please contact your Cato representative.

## Configuring the Microsoft Entra ID Integration

To configure the integrations, create an API app.

### Prerequisites

- Microsoft 365 E3 License

#### Step 1: Create the MS Tenant Integration

First, configure the MS Tenant integration as the parent connector. This connector can be used for all Microsoft integrations. If you have already created the parent connector, go to step 2.

**To create the MS Tenant integration:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated Apps** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **New Connector** panel, select the **MS Tenant (Configure a new MS Tenant)** app.

![New_Microsoft_365_Connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33643818746781.png)
4. Enter the **Connector Name**.
5. Click **Authorize and Save**.

A new browser tab opens to the Microsoft 365 app.
6. In the new browser tab, authenticate to the Microsoft 365 app:
  1. Select the Microsoft account for the Microsoft 365 app.

Otherwise, there may be a Microsoft authentication error.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions to let Cato access the Microsoft 365 app.
  4. The screen shows that you have successfully applied the permissions for the app.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33643826043933.png)

You can close the browser tab and return to the Cato Management Application.
7. The Microsoft 365 SaaS application is added to the **Integrated Apps** tab.

#### Step 2: Create the API Connector for Integrated Apps

After you have set up the parent connector, add the details of the Interconnected Apps integration in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. Choose **3rd Party Apps**.

![image__70_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33643778789149.png)
6. Select the **Microsoft Primary Tenant** that was created in Step 1.
7. (Optional) Add a description.
8. Click **Save**.

The CMA connects to the vendor
9. Click **Authorize**.

![image-20250826-133358.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33643864561565.png)

A Microsoft permissions screen will appear.
10. Review the requested permissions and click **Accept**.
11. The app is visible on the **Integrated Apps** table with a **Connected** status.

After connecting your APIs, you can track the interconnected apps on the **Plugins** page. Data may take a few minutes to appear.
