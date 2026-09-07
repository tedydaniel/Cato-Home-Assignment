---
title: "GitHub: Configuring the Interconnected Apps Integration"
slug: "github-configuring-the-interconnected-apps-integration"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/github-configuring-the-interconnected-apps-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# GitHub: Configuring the Interconnected Apps Integration

This article explains how to configure the Interconnected Apps integration for GitHub.

## Overview

Interconnected Apps provides you with visibility into third-party plugins connected to sanctioned SaaS applications. To provide Cato with visibility of data within an app, you need to set up an integration with the required application. For more information, see [Viewing and Analyzing Interconnected Apps](%%LINK:33492823254813%%).

To configure the Interconnected Apps integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the Cato Management Application (CMA)

A CASB license is required for Interconnected Apps. For more about purchasing a CASB license, please contact your Cato representative.

### Benefits of the GitHub Integration

After creating this connector, you can view detailed information about apps connected to your GitHub environment through Cato, including permissions and usage data (users, last used date).

## Configuring the GitHub Integration

To configure the GitHub integration, generate the required information and enter it in the CMA

### Prerequisites

- GitHub Enterprise license

### Step 1: Configure the Integration in the GitHub Developer Center

In the GitHub Developer Center, identify the access token to enter into the CMA.

**To configure the GitHub integration:**

1. In the GitHub Developer Center, navigate to **Personal access tokens > Tokens (classic)**.
2. Click **Generate new token > Generate new token (classic)**.
3. Set the token expiration date. We recommend setting the expiration date to the maximum allowable period of 1 year.
4. Add these scopes:
  - Audit_log:
    - read:audit_log
  - Org:
    - read:org
5. Click **Generate token** and authorize your organization.
6. Copy and save the **Access Token** so it can be entered into the CMA.
7. Click **Configure SSO** and authorize your organizations
8. Navigate to **Settings > Enterprises**.
9. Click on the name of your enterprise. The login page of your enterprise is displayed.
10. Copy and save the last segment of the URL so it can be added into the CMA. For example, in the URL `https://github.com/enterprises/cato`, copy and save `cato`.

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
