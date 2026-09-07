---
title: "GitHub: Configuring the App Activities Integration"
slug: "github-configuring-the-app-activities-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/github-configuring-the-app-activities-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# GitHub: Configuring the App Activities Integration

This article explains how to configure the App Activities integration for GitHub.

## Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

### Benefits of Connecting GitHub

After creating this connector, you can view and monitor activity in your GitHub environment. For example,

- User logins
- Cloning of repositories
- Commits
- Pull requests
- Modification of repos/organization settings
- Alerts of code/vulnerability scans

This helps you identify and respond to suspicious activity, and you can receive alerts for these activities:

- Code security scans
- Vulnerability (Dependabot) scans
- Secret scans

## Configuring the GitHub Integration

To configure the GitHub integration, create a new Personal access token.

### Prerequisites

- You must have purchased a GitHub Enterprise license
- These scopes (permissions) are provided:
  - **User** - read:user
  - **Audit_log** - read:audit_log
  - **Org** - read:org
  - **Enterprise** - read:enterprise
  - **Repository** - security_events:read

> [!NOTE]
> Note:
> 
> From March 2026, the GitHub connector can collect security events for auditing and cross-platform correlation. If you created this connector before March 2026, you need to regenerate the access token, with the additional `security_events:read` scope and add the new token into the CMA.
> 
> To regenerate the access token, in the GitHub Developer Center, select the existing token used for the Cato integration. Click **Regenerate token**, and under the Repository section, ensure the `security_events:read` is selected. Click **Regenerate token** to apply the changes. Follow Step 2 below to add the new token to the CMA.

### Step 1: Configure the Integration in the GitHub Developer Center

In the GitHub Developer Center, identify the access token to enter into the CMA.

**To configure the GitHub integration:**

1. In the GitHub Developer Center, navigate to **Personal access tokens > Tokens (classic)**.
2. Click **Generate new token**.
3. Set the token expiration date.

We recommend setting the expiration date to the maximum allowable period of 1 year.
4. Add the scopes listed above.
5. Click **Generate token**.
6. Copy and save the new access token so they can be added into the CMA.
7. Navigate to **Settings > Enterprises**.
8. Click on the name of your enterprise.

The login page of your enterprise is displayed.
9. Copy and save the last segment of the URL so it can be added into the CMA. For example, in the URL `https://github.com/enterprises/cato`, copy and save `cato`.

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
7. Click **Save**.
8. The app is visible on the **Integrated Apps** table with a **Connected** status.

After connecting your APIs, you can track the App activities in the [Cloud Activities dashboard](/v1/docs/using-the-cloud-activity-dashboard). Data may take a few minutes to appear.

### Known Limitation

- All events are fetched

### Sources

- **Enterprise Audit Log Endpoint** - Querying the Events endpoint
- **GraphQL and Users Endpoint** - Querying about GitHub users.
