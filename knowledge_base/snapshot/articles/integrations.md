---
title: "Using the Integrations Page"
slug: "using-the-integrations-page"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/using-the-integrations-page"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Integrations Page

This article discusses how to use the Integrations page to get information about supported third-party integrations and to manage API connectors for SaaS application integrations.

## Overview of the Integrations Page

The Integrations page shows a catalog of all third-party integrations supported by Cato, and also provides a unified interface to manage the API connectors for your account's SaaS application integrations. The catalog organizes the integrations according to the different use cases, such as IdP integrations for SSO, cloud storage services for events, SaaS Security API integrations, SIEM integrations, and more. The catalog also links to the relevant Cato Management Application configuration page and documentation for the integration.

## Getting Started with the Integrations Page

![Integrations_-_Catalog.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31734957505309.png)

**To show the Integrations Page:**

- From the navigation menu, click **Resources > Integrations**.

## Working with API Connectors for SaaS Applications

Create and edit API connectors for different SaaS application integrations.

![Integrations_-_Connectors.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31734981326749.png)

**To create or edit an API connector for a SaaS application:**

1. From the navigation menu, click **Resources > Integrations**.
2. Select the **Data Protection API** tab.
3. Click the connector to edit, or click **New** to create a new connector.

For further details about creating a connector, see the relevant [documentation](/v1/docs/data-protection-api) for the connector you want to create.

## Understanding Integrated APIs

![Integrations3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31734950123037.png)

The **Integrated APIs** tab is the central location for displaying your integrated SaaS apps, the integration status, and the capabilities enabled for each app. App integrated for different capabilities are all displayed on this tab. For example, a Zoom connector for [Experience Monitoring](/v1/docs/experience-monitoring) and a Salesforce connector for [Application Control](/v1/docs/application-control-via-api-with-app-activities) are both displayed on this tab.

You can create a new connector by clicking **New**. See the relevant documentation for more information on how to configure connectors for each capability.

## Using the MS Tenant

The MS Tenant acts as a parent connector for most Microsoft Apps. When adding an integration with a Microsoft app, the first step to configure the integration is to create the parent connector. You only need to configure this connector once, and it can then be used for all Microsoft apps.

**To create the MS Tenant integration:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated Apps** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **New Connector** panel, select the **MS Tenant (Configure a new MS Tenant)** app.

![New_Microsoft_365_Connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31734998133533.png)
4. Enter the **Connector Name**.
5. Click **Authorize and Save**.

A new browser tab opens to the Microsoft 365 app.
6. In the new browser tab, authenticate to the Microsoft 365 app:
  1. Select the Microsoft account for the Microsoft 365 app.

Otherwise, there may be a Microsoft authentication error.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions to let Cato access the Microsoft 365 app.
  4. The screen shows that you have successfully applied the permissions for the app.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31734957737117.png)

You can close the browser tab and return to the Cato Management Application.
7. The Microsoft 365 SaaS application is added to the **Integrated Apps** tab.
