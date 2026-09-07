---
title: "Atlassian: Configuring the Interconnected Apps Integration"
slug: "atlassian-configuring-the-interconnected-apps-integration"
updated: 2026-08-10T10:20:53Z
published: 2026-08-10T10:20:53Z
canonical: "knowledge.catonetworks.com/atlassian-configuring-the-interconnected-apps-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Atlassian: Configuring the Interconnected Apps Integration

- This article explains how to configure the Interconnected Apps integration for Atlassian.

## Overview

Interconnected Apps provides you with visibility into third-party plugins connected to sanctioned SaaS applications. To provide Cato with visibility of data within an app, you need to set up an integration with the required application. For more information, see [Viewing and Analyzing Interconnected Apps](/v1/docs/viewing-and-analyzing-interconnected-apps).

To configure the Interconnected Apps integration, you need to:

  1. Configure the integration within the SaaS application
  2. Create the API connector in the Cato Management Application (CMA)

A CASB license is required for Interconnected Apps. For more about purchasing a CASB license, please contact your Cato representative.

## Configuring the Atlassian Integration

To configure the Atlassian integration, generate the required information and enter it in the CMA.

### Prerequisites

### Step 1: Configure the Integration in your Atlassian Account

In your Atlassian Account, create an API token and identify the account email and site URL.

**To configure the Atlassian integration:**

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

  1. From the navigation menu, click **Resources > Integrations**.
  2. Click the **Configured Integrations** tab.
  3. Click **New**.

The **New Integration** panel opens.
  4. Select the **SaaS Application** you want to add.
  5. In the **Capability** drop-down select **Third Party Apps**.
  6. Add the details created during step one.
  7. Click **Save**.
  8. The app is visible on the **Integrated Apps** table with a **Connected** status.

After connecting your APIs, you can track the interconnected apps on the **Plugins** page. Data may take a few minutes to appear.
  - Atlassian Enterprise license
  1. Log in to your Atlassian Account ([https://id.atlassian.com/manage-profile/security](https://id.atlassian.com/manage-profile/security)).
  2. Under **API tokens**, click **Create and manage API tokens.**
  3. Click **Create API Token**.
  4. Add a name for the API token, and choose an expiry date. **Note:** It is recommended to set the expiry date to the maximum 366 days.
  5. Click **Create**.
  6. Copy and save the API token so it can be entered into the CMA.
  7. On the **Email** tab, copy and save your account email so it can be entered into the CMA.
  8. Copy and save the URL of your organization Atlassian site (<site_name>.atlassian.net).
