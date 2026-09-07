---
title: "Atlassian (Jira and Confluence): Configuring the App Activities Integration"
slug: "atlassian-jira-and-confluence-configuring-the-app-activities-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/atlassian-jira-and-confluence-configuring-the-app-activities-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Atlassian (Jira and Confluence): Configuring the App Activities Integration

This article explains how to configure the App Activities integration for Atlassian products Confluence and Jira.

## Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

The supported Atlassian products are:

- Confluence
- Jira

## Configuring the Atlassian Integration

To configure the Atlassian integration, create an API key.

### Prerequisites

- You must have purchased the Atlassian Enterprise license

### Step 1: Configuration the Integration in the Atlassian Admin Console

In the Admin Console, identify the Organization ID and API ket to enter into the CMA.

**To configure the Atlassian integration:**

1. Log into your [Atlassian Admin Console](https://admin.atlassian.com/).
2. Navigate to **Settings > API keys**.
3. Click **Create an API key**.
4. Choose a name for the API key and select the expiration date.

We recommend extending the expiration date to the maximum of one year.
5. Click **Create**.
6. Copy and save the **Organization ID** and **API key**.

**Note:** These values cannot be viewed again. Ensure you save them before you leave the page.

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

- **Audit** - Querying actions log files.

### Known Limitations

- All activities (called Actions in Atlassian) are fetched
