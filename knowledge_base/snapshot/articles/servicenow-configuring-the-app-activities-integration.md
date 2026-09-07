---
title: "ServiceNow: Configuring the App Activities Integration"
slug: "servicenow-configuring-the-app-activities-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/servicenow-configuring-the-app-activities-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ServiceNow: Configuring the App Activities Integration

This article explains how to configure the App Activities integration for ServiceNow.

## Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

## Configuring the ServiceNow Integration

To configure the ServiceNow integration, create the required information from the ServiceNow Developer Portal.

### Prerequisites

- You must have a ServiceNow Platform License

### Step 1: Configure the Integration in the ServiceNow Developer Portal

In the ServiceNow Developer Portal, create the required information.

**To configure the ServiceNow integration:**

- Log into the ServiceNow Developer Portal (`https://&lt;your_tenant&gt;.service-now.com`).

#### Create an Application

1. In the search bar, search for and select **Application Registry**.

![SN1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29922504174237.png)
2. Create a New Integration.
3. Select **Create an OAuth API endpoint for external clients**.

![SN2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29922487260957.png)
4. Add a name for the application integration and copy and save the **Client ID** and **Client Secret** so they can be added to the CMA.

#### Create a Role

1. In the search bar, search for and select **User Administration**.
2. On the **Roles** tab, create a new role with a name you can recognize.

#### Add Access Control Lists

1. Click on the User icon and select **Elevate Role**.
2. Check **Security Admin** and select **Update**.
3. In the search bar, search for and select **System Security**.
4. In the **Access Controls (ACL)** tab, create a new Access Control List.
5. Choose these options:
  - **Name**: sys_audit
  - **Type**: Record
  - **Operation**: Read
  - **Decision Type**: Allow If
6. Press **Submit** and select the role you created in the [Create a Role](/v1/docs/servicenow-configuring-the-app-activities-integration#create-a-role) step.
7. Repeat steps 5 and 6 an additional 4 times with these values as the name:
  - sys_user_session
  - sys_data_source
  - sys_history_set
  - sys_audit_delete

#### Create a User

1. In the search bar, search for and select **User Administration**.
2. On the **Users** tab create a new user.
3. Add a name and email address and check the **Web service access only** box, and select **Submit**.

![SN3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29922504303389.png)
4. Search for and select the user you created in step 2.
5. Click **Set Password** and generate a password. Copy and **Save** the password so it can be added to the CMA.
6. On the user's page, select the **Roles** tab.

![SN4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29922537034013.png)
7. Add these roles to the Roles list:
  - The role you created in the [Create a Role](/v1/docs/servicenow-configuring-the-app-activities-integration#create-a-role) step
  - The Personalize role

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

Note: the user name is the email address of the user you created at step 16 above. The BaseURL is `https://&lt;your_tenant&gt;.service-now.com`.
7. Click **Save**.
8. The app is visible on the **Integrated Apps** table with a **Connected** status.

After connecting your APIs, you can track the App activities in the [Cloud Activities dashboard](/v1/docs/using-the-cloud-activity-dashboard). Data may take a few minutes to appear.

## Sources

- Login - using the OAuth endpoint
- sys_audit - Querying field changes
- sys_user_session - Querying login activities
- sys_audit_delete - Querying deletion activities
- sys_data_source - Querying import activities
- sys_history_set - Querying View and Edit activities

## Known Limitations

- Only tables that audit changes are queried
