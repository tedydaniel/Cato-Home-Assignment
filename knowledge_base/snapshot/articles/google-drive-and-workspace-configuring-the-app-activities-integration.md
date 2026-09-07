---
title: "Google Drive and Workspace: Configuring the App Activities Integration"
slug: "google-drive-and-workspace-configuring-the-app-activities-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/google-drive-and-workspace-configuring-the-app-activities-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Drive and Workspace: Configuring the App Activities Integration

This article explains how to configure the App Activities integration for Google Drive and Workspace.

## Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

### Understanding the Google Workspace Integration

Connecting your Google Workspace account to Cato enables visibility into:

- **User Login Activity**: Track successful and failed login attempts across all Google Workspace services (e.g., Gmail, Drive, Docs, Sheets, Calendar).
- **Third-party App Authorizations (OAuth Events)**: Monitor when users sign in to third-party applications using Google Sign-In or grant external apps access to Workspace data. This includes token issuance, scopes granted (e.g., Drive read/write), and token revocations.

### Benefits of Connecting Google Drive

After creating this connector, you can view and monitor activity in your Google Drive. For example:

- File uploads/downloads
- Sharing files
- Permission changes

You also gain access to various audit logs in your Google environment, for example:

- Logins success/failure
- App access authorization
- Account modification

This helps you identify and respond to suspicious activity, and you can receive alerts for these activities:

- Suspicious logins
- Risky sensitive actions
- Password leaks

## Configuring the Google Drive and Workspace Integration

To configure the Google Drive and Workspace integration, create a new project.

### Prerequisites

- You must have purchased a Google Cloud Enterprise license

> [!NOTE]
> Note:
> 
> From May 2026, the Google Drive and Workspace connector can collect additional security event data from the Google Alert Center. This includes data such as suspicious logins, leaked passwords, and sensitive admin actions.
> 
> If you created this connector before May 2026, you need to enable the Google Workspace Alert Center API (steps 7 and 8) and ensure all scopes listed in step 22 are added.

### Step 1: Configure the Integration in the Google Cloud Console

In the Google Cloud Console, create a Service account private key to enter into the CMA.

**To configure the Google Drive and Workspace integration:**

1. In your [Google Cloud Console](https://console.cloud.google.com/), click **Select a Project**.
2. Click **New project**.

![Google1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28478697230621.png)
3. Choose a **Name** and **Location** and click **Create**.
4. Navigate to **APIs & Services > Library**.
5. Search for Admin SDK.

![Google_2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28478697252637.png)
6. Click on **Admin SDK API** and click **Enable**.

![Google3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28478676772381.png)
7. Search for Google Workspace Alert Center API.
8. Click on **Google Workspace Alert Center API** and click **Enable**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35976758120477.png)
9. Navigate to **IAM & Admin > Service Accounts**.
10. Select the project you created in step two, and click **Create service account**.
11. Add a **Service account ID** and click **Create and continue**.
12. In the **Select a role** drop down, choose **Audit Manager Admin** (you can search for this role).

![Google4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28478697312157.png)
13. Click **Done**.
14. Click on the service account you created and navigate to the **Keys** tab,
15. Click **Add key > Create new key**.
16. Choose the JSON key type and click **Create**.

A JSON file containing the private key is downloaded.
17. Copy and save the **Private key** so it can be added to the CMA.
18. In the [Google Admin console](https://admin.google.com/), navigate to **Security > Access and Data Control > API control**.
19. Under **Domain wide delegation**, select **Manage Domain Wide Delegation**.
20. Click **Add new**.
21. Add the **Client ID** of the Service Account. You can find this in the Service Account page.
22. Add these scopes:
  1. `https://www.googleapis.com/auth/admin.reports.audit.readonly`
  2. `https://www.googleapis.com/auth/admin.directory.user.readonly`
  3. `https://www.googleapis.com/auth/admin.directory.user.security`
  4. `https://www.googleapis.com/auth/apps.alerts`
23. Click **Authorize**.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.

**Note:** Enter the **Private Key** in JSON format.
5. In the **Capability** drop down select **App Activities**.
6. Add the details created during step one.

**Note**: The JSON and admin email address are the details necessary for the connector creation. The admin email field should include the email of a user with the Super Admin role.
7. Click **Save**.
8. The app is visible on the **Integrated Apps** table with a **Connected** status.

After connecting your APIs, you can track the App activities in the [Cloud Activities dashboard](/v1/docs/using-the-cloud-activity-dashboard). Data may take a few minutes to appear.

### Sources

- **Audit Logs Drive** - Activities/drive endpoint to query Google Drive audit logs
- **Audit Logs Login** - Activities/Login endpoint to query Google native logins audit logs
- **Audit Logs Third Party (Token)** - Activities/token endpoint to query Google third_party logins audit logs

### Known Limitations

- All events are currently fetched in the Drive and Login endpoints

In the third party logins, only events describing the login itself are fetched
