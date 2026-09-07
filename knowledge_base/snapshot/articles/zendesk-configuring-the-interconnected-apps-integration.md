---
title: "Zendesk: Configuring the Interconnected Apps Integration"
slug: "zendesk-configuring-the-interconnected-apps-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/zendesk-configuring-the-interconnected-apps-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Zendesk: Configuring the Interconnected Apps Integration

This article explains how to configure the Interconnected Apps integration for Zendesk.

## Overview

Interconnected Apps provides you with visibility into third-party plugins connected to sanctioned SaaS applications. To provide Cato with visibility of data within an app, you need to set up an integration with the required application. For more information, see [Viewing and Analyzing Interconnected Apps](/v1/docs/viewing-and-analyzing-interconnected-apps).

To configure the Interconnected Apps integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the Cato Management Application (CMA)

A CASB license is required for Interconnected Apps. For more about purchasing a CASB license, please contact your Cato representative.

### Benefits of Connecting Zendesk

After creating this connector, you can gain visibility into:

- **App Inventory** All OAuth apps authorized by users, including local custom apps and Zendesk Marketplace apps
- **Permission Analysis**: Scopes classified into standard categories (Collaboration and Communication, Basic Profile and Presence, Directory and App Mgmt, Security and Compliance, etc.) with risk levels
- **User Mapping**: Which users authorized which apps, with full user details (name, email)

## Configuring the Zendesk Integration

To configure the Zendesk integration, create an API token.

This connector uses the same credentials as the [Zendesk App Activity connector](/v1/docs/zendesk-configuring-the-app-activities-integration) (same tenant URL, admin email, and API token). No additional setup is required if the Activity connector is already configured.

### Prerequisites

- You must have purchased the Zendesk Enterprise plan.

### Step 1: Configure the Integration in the Zendesk Admin Center

In the Zendesk Admin Center, identify the API Token to enter into the CMA.

**To configure the Zendesk integration:**

1. In the Admin Center, navigate to **Apps and Integrations > Zendesk API**.
2. Click **Add API Token**.
3. Copy and save the API token value.

The Token value cannot be viewed again. Ensure you save the Token value before you leave the page.

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
  - **Tenant URL**: The URL of your Zendesk tenant (`https://&lt;your_tenant&gt;.zendesk.com`0
  - **Admin Email**: The email address of a Zendesk user with the Admin role
  - **API Token**: The token generated in step 1
7. Click **Save**.
8. The app is visible on the **Integrated Apps** table with a **Connected** status.

After connecting your APIs, you can track the interconnected apps on the **Plugins** page. Data may take a few minutes to appear.
