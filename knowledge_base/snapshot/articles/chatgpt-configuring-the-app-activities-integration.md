---
title: "ChatGPT: Configuring the App Activities Integration"
slug: "chatgpt-configuring-the-app-activities-integration"
updated: 2026-09-03T12:13:42Z
published: 2026-09-03T12:13:42Z
canonical: "knowledge.catonetworks.com/chatgpt-configuring-the-app-activities-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ChatGPT: Configuring the App Activities Integration

This article explains how to configure the App Activities integration for ChatGPT.

### Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

The ChatGPT integration includes two connectors:

- **Audit Log Connector**: Provides visibility into admin activities regarding settings and policies
- **Conversations Connector**: Provides visibility into conversations, including uploads

## Configuring the ChatGPT Integration

To configure the ChatGPT integration, create a new secret key.

### Prerequisites

- You must have purchased the ChatGPT Enterprise license

### Step 1: Configure the Integrations in the Open AI Platform Center

In the Open AI Platform Center, identify the information to enter into the CMA.

**To configure the ChatGPT Audit Log Connector:**

1. Log into your [Open AI Platform Center](https://platform.openai.com/).
2. In your Open AI Platform Center, navigate to **Settings > Data Controls**.
3. On the **Data retention** tab, Enable Audit logging and click **Save**.

![ChatGPT1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28338258192029.png)
4. Navigate to **Settings > Organization > Admin Keys**.
5. Click **Create new Admin key**.
6. (Optional) Enter a name for the Admin key and update the Project and click **Create Admin key**.
7. Copy the key so it can be entered into the CMA. This should be entered into the **Access Token** field.

![ChatGPT3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28338288938141.png)

**To configure the ChatGPT Conversations Connector:**

1. Log into your [Open AI Platform Center](https://platform.openai.com/).
2. Navigate to **Identity & Access > Credentials > Admin Keys**.
3. Click **Create new admin key**.
4. Add the following details:
  - Name: Choose a name for the key
  - Workspace: Select the ChatGPT Enterprise workspace for Cato to monitor
  - Expiration: Never
  - Permissions: Select All
5. Click **Submit**.
6. Copy the secret key so it can be entered into the CMA.

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

### Sources

- **Audit Logs** - Use the audit_logs endpoint to query ChatGPT audit logs

### Known Limitations

- All events are currently fetched
