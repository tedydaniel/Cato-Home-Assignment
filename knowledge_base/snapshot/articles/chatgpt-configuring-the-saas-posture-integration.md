---
title: "ChatGPT: Configuring the SaaS Posture Integration"
slug: "chatgpt-configuring-the-saas-posture-integration"
updated: 2026-09-03T12:09:46Z
published: 2026-09-03T12:09:46Z
canonical: "knowledge.catonetworks.com/chatgpt-configuring-the-saas-posture-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ChatGPT: Configuring the SaaS Posture Integration

## Overview

SaaS Posture integrations provide visibility into the configuration and security posture of your connected SaaS applications. Cato continuously reviews the application settings and compares them to the recommended posture defined by Cato’s research team. This helps identify misconfigurations that can increase risk, such as authentication settings, third-party integrations, and data-sharing controls.

Posture data appears in the Applications dashboard, where you can view posture scores and the highest-severity findings across connected applications. You can review each posture check from the Posture page, including the issue details, status, and remediation action required to pass the check.

For more information, see [Reviewing the Security Posture of Your SaaS Applications.](https://knowledge.catonetworks.com/v1/docs/understanding-the-security-posture-of-your-saas-applications)

To configure the SaaS Posture integration, you need to:

1. Configure the required settings in the SaaS application
2. Create the API connector in the CMA

A CASB license is required for SaaS Posture integrations.

## Configuring the ChatGPT Integration

To configure the ChatGPT integration, create a new secret key.

### Prerequisites

- You must have purchased the ChatGPT Enterprise license

### Step 1: Configure the Integrations in the Open AI Platform Center

In the Open AI Platform Center, identify the information to enter into the CMA.

**To configure the ChatGPT Admin API Key:**

1. Log into your [Open AI Platform Center](https://platform.openai.com/).
2. In your Open AI Platform Center, navigate to **Settings > Data Controls**.
3. On the **Data retention** tab, Enable Audit logging and click **Save**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(39).png)
4. Navigate to **Settings > Organization > Admin Keys**.
5. Click **Create new Admin key**.
6. (Optional) Enter a name for the Admin key and update the Project and click **Create Admin key**.
7. Copy the key so it can be entered into the CMA. This should be entered into the **Access Token** field.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(40).png)

**To create a compliance API key**

The Compliance API provides additional posture checks for custom GPTs and workspace-level projects.

  1. In your [Open AI Platform Center](https://platform.openai.com/), navigate to **Identity & Access > Credentials > Admin Keys**.
  2. Click **Create new admin key**.
  3. Add the following details:

    - Name: Choose a name for the key
    - Workspace: Select the ChatGPT Enterprise workspace for Cato to monitor
    - Expiration: Never
    - Permissions: Select All
  4. Click **Submit**.
  5. Copy the secret key so it can be entered into the CMA.

**To identify your workspace ID:**

  1. Navigate to the [OpenAI Platform API settings](https://platform.openai.com/settings/organization/general).
  2. Verify it matches the Workspace ID of the ChatGPT workspace at [https://chatgpt.com/admin/settings.](https://chatgpt.com/admin/settings.) If the Workspace IDs do not match, contact [support@openai.com](mailto:support@openai.com) to resolve the issue before proceeding.
  3. Copy and save the Workspace ID so it can be entered into the CMA.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

The app is visible on the **Integrated Apps** table with a **Connected** status.
  1. From the navigation menu, click **Resources > Integrations.**
  2. Click the **Configured Integrations** tab.
  3. Click **New**. The **New Integration** panel opens.
  4. Select the **SaaS Application** you want to add.
  5. In the **Capability** drop-down, select **SaaS Posture**.
  6. Add the details created during step one.
    - **Access Token:** The API key you created in step 1
    - **Admin Token:** The API key created in step 2
    - **Workspace ID:** Your ChatGPT Enterprise workspace ID identified above
  7. Click **Save**.
