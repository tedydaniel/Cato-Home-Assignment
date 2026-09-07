---
title: "Salesforce: Configuring the Interconnected Apps Integration"
slug: "salesforce-configuring-the-interconnected-apps-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/salesforce-configuring-the-interconnected-apps-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Salesforce: Configuring the Interconnected Apps Integration

This article explains how to configure the Interconnected Apps integration for Salesforce.

## Overview

Interconnected Apps provides you with visibility into third-party plugins connected to sanctioned SaaS applications. To provide Cato with visibility of data within an app, you need to set up an integration with the required application. For more information, see [Viewing and Analyzing Interconnected Apps](/v1/docs/viewing-and-analyzing-interconnected-apps).

To configure the Interconnected Apps integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the Cato Management Application (CMA)

A CASB license is required for Interconnected Apps. For more about purchasing a CASB license, please contact your Cato representative.

## Configuring the Salesforce Integration

To configure the Salesforce integration, create the required configurations in your Salesforce account, then configure the connector within the CMA.

### Step 1: Configure the Integration in your Salesforce Account

To configure the Salesforce integration, create a user, assign it the required permission, and create an external client app.

**To create a user for the integration:**

1. Login to your Salesforce account (`&lt;your_tenant&gt;.lightning.force.com`)
2. Click on the gear icon and click **Setup**.
3. Search for **Users**
4. Click **New User**
5. Add the required details, with these configurations:
  - **User License**: Salesforce
  - **Profile**: Standard User
6. Click **Save**.

**To assign the user the required permissions:**

1. In your Salesforce account, search for **Permission Sets**.
2. Click **New**.
3. Enter the required fields and click **Save**.
4. Click **Edit**, and add these permissions:
  - API Enabled
  - API Only User
  - Customize Application
  - Manage Connected Apps
  - Manage Custom Permissions
  - Password Never Expires
  - Run Reports
  - View all External Client Apps
  - View Dashboards in Public Folders
  - View Developer Name
  - View Event Log Files
  - View Reports in Public Folders
  - View Roles and Role Hierarchy
  - View Setup and Configuration
  - Modify Metadata Through Metadata API Functions
5. Click **Save**.
6. Click **Manage Assignments > Add Assignment** and choose the user created above.

**To create the external client app:**

1. In your Salesforce account, search for **External Client App Manager**.
2. Click New External Client App.
3. Enter the required fields, with this configuration:
  - **Distribution State**: Local
4. Select **API (Enable OAuth Settings)** and check the **Enable Oauth** checkbox.
5. Under **App Settings** and these configurations:
  - **Callback URl** :`https://cc.catonetworks.com/redirect/cas/salesforce/callback`
  - **OAuth Scopes**:
    - Manage user data via APIs (api)
    - Perform requests at any time (refresh_token, offline_access)
    - Access Analytics REST API resources (wave_api)
  - **Flow Enablement**: Check the **Enable Client Credentials Flow** checkbox
6. Click **Create**.
7. In the app’s page, navigate to **Policies** and click **Edit**.
8. Under **OAuth Policies > Plugin Policies > Permitted Users**, select **Admin approved users are pre-authorized**.
9. Under **App Policies > Select Permission Sets** select the permission set you created
10. Under **OAuth Flows and External Client App Enhancements** select the **Enable Client Credentials Flow** checkbox.
11. Under **Run As (Username)** add the email of the integration user.
12. Click **Save**.
13. In the app’s page, navigate to **Settings > OAuth Settings > App Settings**.
14. Click **Consumer Key and Secret** copy and save the **Key** and **Secret** to enter into the CMA.

Note: You may need to authenticate to view the **Key** and **Secret**.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop down select **Third Party Apps**.
6. Add the details created during step one.
7. Click **Save**.
8. The app is visible on the **Integrated Apps** table with a **Connected** status.

After connecting your APIs, you can track the interconnected apps on the **Plugins** page. Data may take a few minutes to appear.
