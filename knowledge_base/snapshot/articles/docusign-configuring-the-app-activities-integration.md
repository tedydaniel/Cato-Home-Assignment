---
title: "Docusign: Configuring the App Activities Integration"
slug: "docusign-configuring-the-app-activities-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/docusign-configuring-the-app-activities-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Docusign: Configuring the App Activities Integration

This article explains how to configure the App Activities integration for Docusign.

## Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

### Prerequisites

- DocuSign Monitor Add-on in your DocuSign organization
- DocuSign plans for both CLM and eSignature

## Benefits of Connecting Docusign

After creating this connector, you can view and monitor activity in your Docusign environment. For example:

- User logins (successful & failed)
- Document creation
- Document sent for signature
- Envelope completed
- Envelope declined
- Account settings changes
- User account changes
- Organization configuration changes

## Configuring the Docusign Integration

To configure the Docusign integration, create an application in the DocuSign admin portal.

### Step 1: Configure the Integration in the Docusign Admin Portal

In the Docusign admin portal, configure a user and application.

#### Creating a User

The first step in configuring the integration is to create a user with the required roles.

**To create a user:**

1. In the [Docusign Admin Portal](https://apps.docusign.com/admin/users) create a user. For more information, see the [Docusign documentation](https://support.docusign.com/s/document-item?language=en_US&amp;bundleId=pik1583277475390&amp;topicId=jpz1583277424305.html&amp;_LANG=enus).
2. Assign the user the Organization Administrator or Security Reports Administrator role.
3. On the User's page, copy and save the **User ID** so that it can be entered into the CMA.

#### Configure an Application

The next step is to create an Integration key and Private key.

**To configure an application:**

1. In the [Docusign Admin Portal](https://apps.docusign.com/admin/apps-and-keys), navigate **Settings > Integrations > Apps and Keys**.
2. Click **Add App and Integration Key**.

![image__73_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33893067649181.png)
3. Add the following:
  - App Name: Choose a name for the app
  - Integration Type: Third-party integration key

![image__74_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33893060805789.png)
  - Redirect URIs: https://cc.catonetworks.com/redirect/cas/appconnector/callback

![image__75_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33893105981469.png)
  - Allowed HTTP Methods: Check GET and POST

![image__76_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33893106052125.png)
4. Copy and save the **Integration Key** so it can be entered into the CMA.
5. In the **Service Integration** section, click **Generate RSA**. Copy and save the **Private Key** so it can be entered into the CMA.

**Note**: This is only displayed once.
6. Click **Save**.

#### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop down select **App Activities**.
6. Add the details created during step one.
7. If you are integrating with a development environment, check the **Is Dev Environment** box, if you are integrating with a production environment, leave this box unchecked.
8. Click **Save**.

The Docusign consent flow opens.
9. Grant consent for these scopes:
  - signature
  - impersonation
  - user_read
10. The app is visible on the **Integrated Apps** table with a **Connected** status.

After connecting your APIs, you can track the App activities in the [Cloud Activities dashboard](/v1/docs/using-the-cloud-activity-dashboard). Data may take a few minutes to appear.
