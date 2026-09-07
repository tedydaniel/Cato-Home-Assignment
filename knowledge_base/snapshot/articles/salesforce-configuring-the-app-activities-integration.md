---
title: "Salesforce: Configuring the App Activities Integration"
slug: "salesforce-configuring-the-app-activities-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/salesforce-configuring-the-app-activities-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Salesforce: Configuring the App Activities Integration

This article explains how to configure the App Activities integration for Salesforce.

## Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

## Configuring the Salesforce Integration

To configure the Salesforce integration, create a connected app.

### Prerequisites

- License for Salesforce Shield or Event Monitoring
- These permissions are provided:
  - View Event Log Files
  - Run Reports
  - View Dashboards in Public Folders
  - View Reports in Public FoldersPassword Never Expires
  - API Enabled
  - API User Only

### Step 1: Configure the Integration in your Salesforce Tenant

In your Salesforce tenant, identify the Consumer Key and Consumer Secret to enter into the CMA.

**To configure the Salesforce integration:**

1. In your Salesforce tenant, from Setup, in the Quick Find box, enter App Manager, and then select **App Manager**.
2. Click **New Connected App**.
3. Enter a name, contact email ID and phone number.
4. Select **Enable OAuth Settings**.
5. In Selected OAuth Scopes, select these options:

![SF_CASB.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28478711923741.png)
  - **Access the identity URL service**
  - **Manage user data via APIs**
  - **Perform requests at any time**
6. Click **Save**.

The Connected App is created.
7. On the details page of the Connected App, click **Manage Consumer Details**.

Copy and save the **Consumer Key** and **Consumer Secret** so they can be added into the CMA.
8. In the Quick Find box, search for **Permission Sets** and click **Permission Sets**.
9. Click **New**.
10. Add a **Label** and **API name** then save the new permission set.
11. Enable all the permissions listed above.
12. Click **Manage Assignments** then **Add Assignment** and add the user to be used for the connector.

**Note:** When you configure the Salesforce integration in the CMA, the **User Name** and **Password** are the credentials of the admin created for the integration.

#### Step 2: Create the API Connector in the CMA

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

### Known Limitations

- All activities (Event Types in SalesForce) are fetched

### Sources

- **ListEventLogFile** - Querying event log file paths
- **DownloadEventLogFile** - Querying log files
- **DownloadEventLogFile** - Querying log files
- **DocumentInfo** - Querying Document enrichments
- **UserInfo** - Querying User enrichments
- **GroupInfo** - Querying Group enrichments
- **AssetInfo** - Querying Asset enrichments
