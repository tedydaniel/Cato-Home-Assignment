---
title: "Workday: Configuring the App Activities Integration"
slug: "workday-configuring-the-app-activities-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/workday-configuring-the-app-activities-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Workday: Configuring the App Activities Integration

This article explains how to configure the App Activities integration for Workday.

## Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

### Prerequisites

- Admin user in Workday

### Benefits of Connecting Workday

After creating this connector, you can view and monitor activity in your Workday environment, for example:

- Successful and failed login attempts (Password, SAML, SSO, OAuth)
- Suspicious sign-on patterns (unusual IPs, times, auth methods)

## Configuring the Workday Integration

To create the Workday integration, register an API Client for Integrations.

### Step 1: Configure the Integration in your Workday Account

Three steps are required to configure the integration in your Workday account.

#### Create an Integration System User

This user is used for authentication with the Workday API.

**To create an integration system user**

1. Login to your Workday account
2. In the search bar, search for and select **Create Integration System User**.
3. Enter the following details:

![WD1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34695180048797.png)
  - **User Name:** Choose a user name
  - **New Password:** Enter a password and re-enter it in New Password Verify
  - Check **Do Not Allow UI Sessions for enhanced security** check box
4. Click **OK**, then **Done**

#### Configure Permissions for the Integration System User

To configure the required permissions for the new integration system user, create an integration system security group, add domain security policies, and activate pending security policy changes.

**To create an integration system security group:**

1. In your Workday account, in the search bar, search for and select **Create Security Group**.
2. Enter the following:

![WD2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34695156549917.png)
  - **Type of Tenanted Security Group**: Integration System Security Group (Unconstrained)
  - **Name**: Choose a name
3. Click **OK**, then **Done**

**To add domain security policies to the security group:**

1. In your Workday account, in the search bar, search for and select **Maintain Permissions for Security Group**.
2. Set **Operation** to **Maintain** and select the security group created above.
3. Click **OK**.
4. In the **Domain Security Policy Permissions** table, add the following rows:

**View required policy permissions**

| Access | Domain Security Policy |
| --- | --- |
| Get Only | Manage: Organization Integration |
| Get Only | User-Based Security Group Administration |
| View Only | Workday Accounts |
| Get Only | Special OX Web Services |
| Get Only | Integration Security |
| View Only | Integration Security |
| View Only | Security Configuration |
| Get Only | Security Configuration |
| View Only | Security Administration |
| View Only | Security Activation |
| View Only | Purge Person Data |
| Get Only | Integration Configure |
| Get Only | Workday Account Monitoring |
| View Only | Workday Account Monitoring |
| Get Only | System Auditing |
| View Only | System Auditing |
| Get Only | Former Worker Storage |
| Get Only | Worker Data: Public Worker Reports |
| Get Only | Workday Accounts |
| Get Only | Worker Data: Current Staffing Information |
| View Only | Worker Data: Current Staffing Information |
| View Only | Manage: All Custom Reports |
| Get Only | Manage: All Custom Reports |
| Get Only | Security Activation |
| Get Only | Workday Query Language |
| View Only | Workday Query Language |
| Get Only | Business Process Administration |
| View Only | Business Process Administration |
| Get Only | Worker Data: Staffing |
| View Only | Worker Data: Staffing |
| Get Only | Worker Data: Worker ID |
| View Only | Worker Data: Worker ID |
| Get Only | Indexed Data Source: Workers |
| View Only | Indexed Data Source: Workers |
| Get Only | Person Data: Work Contact Information |
| View Only | Person Data: Work Contact Information |
| View Only | Worker Data: Public Worker Reports |
5. Click **OK**, then **Done**

**Activate Pending Security Policy Changes:**

1. In your Workday account, in the search bar, search for and select **Activate Pending Security Policy Changes**.
2. Enter a comment and click **OK**.
3. Check the **Confirm** checkbox and click **OK**.

#### Register an API Client for Integrations

1. In your Workday account, in the search bar, search for and select **Register API Client for Integrations**.
2. Enter the following:

![WD3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34695200338461.png)
  - **Client Name**: Enter a name
  - Check the **Non-Expiring Refresh Tokens** checkbox
  - Under **Scope (Functional Areas)**, select: Integration, Organizations and Roles, Implementation, Staffing, Tenant Non-Configurable, System
3. Click **OK**.
4. Copy and save the **Client ID** and **Client Secret** so they can be entered into the CMA.

**Note:** The secret is only visible on this page and cannot be recovered later
5. Click the three-dots next to the API client name and navigate to **API Client > Manage Refresh Tokens for Integrations**.
6. For **Workday Account**, select the integration system user created above and click **OK**.
7. Select **Generate New Refresh Token** and click **OK**.
8. Copy and save the **Refresh Token** value so it can be entered into the CMA.
9. Search for and select **View API Clients**.
10. Copy and save the **Workday REST API Endpoint** and **Token Endpoint** so they can be entered into the CMA.

### Step 2: Create the API Connector in the CMA

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
