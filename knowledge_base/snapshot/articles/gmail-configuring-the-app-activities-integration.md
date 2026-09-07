---
title: "Gmail: Configuring the App Activities Integration"
slug: "gmail-configuring-the-app-activities-integration"
updated: 2026-08-10T10:16:39Z
published: 2026-08-10T10:16:39Z
canonical: "knowledge.catonetworks.com/gmail-configuring-the-app-activities-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Gmail: Configuring the App Activities Integration

This article explains how to configure the App Activities integration for Gmail.

## Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

### Benefits of Connecting Gmail

After creating this connector, you can view and monitor activity in your Gmail tenant, for example:

- Mail Sharing (Send / Forward / Auto-Forward)
- Mail Labeling (Spam / Archive)
- Attachments / Links attached
- Item permissions change

## Configuring the Gmail Integration

To configure the Gmail integration, create a new project.

### Prerequisites

- You must have purchased a Google Cloud Enterprise license

### Step 1: Configure the Integration in the Google Cloud Console

In the Google Cloud Console, create a Service account private key to enter into the CMA.

**To configure the Gmail integration:**

1. In your [Google Cloud Console](https://console.cloud.google.com/), click **Select a Project**.
2. Click **New project**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(145).png)
3. Choose a **Name** and **Location** and click **Create**.
4. Navigate to **APIs & Services > Library**.
5. Search for Admin SDK.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(146).png)
6. Click on **Admin SDK API** and click **Enable**.
7. Search for Gmail API.
8. Click on **Gmail API** and click **Enable.**
9. Navigate to **IAM & Admin > Service Accounts**.
10. Select the project you created in step two, and click **Create service account**.
11. Add a **Service account ID** and click **Create and continue**.
12. In the **Select a role** drop down, choose **Audit Manager Admin** (you can search for this role).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(147).png)
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
22. Add this scope:
  - `https://www.googleapis.com/auth/admin.reports.audit.readonly admin.directory.user.readonly`
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
