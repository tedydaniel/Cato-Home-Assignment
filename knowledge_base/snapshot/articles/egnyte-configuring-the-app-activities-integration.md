---
title: "Egnyte: Configuring the App Activities Integration"
slug: "egnyte-configuring-the-app-activities-integration"
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/egnyte-configuring-the-app-activities-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Egnyte: Configuring the App Activities Integration

This article explains how to configure the App Activities integration for Egnyte.

## Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

## Configuring the Egnyte Integration

To configure the Egnyte integration, use the Service Account user in your Egnyte account.

### Prerequisites

You must have purchased one of these licenses:

- Business
- Enterprise Lite
- Enterprise Platform

#### Step 1: Configure the Integration in your Egnyte Account

In you Egnyte account, identify the Key and Secret to enter into the CMA.

**To configure the Egnyte integration:**

1. In your Egnyte account, navigate to **Settings > Users & Groups**.
2. Click **Add new account**.
3. Select **Service Account > Administrator**.
4. Enter the credentials you want to use.

Copy and save the user name and password so they can be added into the CMA.
5. In a new browser window, go to [https://developers.egnyte.com](https://developers.egnyte.com) to create a developer account.
6. Click **Sign In** then **Create an account**.
7. Fill in your details to create an account.
8. In the developer account, navigate to **Get API Key > Application**.
9. Click **Create a New Application**.
10. Fill in the details.

The Egnyte domain you will use for testing is your Egnyte domain.
11. Select **Issue a new key for Egnyte Connect API** and unselect **Issue a new key for Egnyte Protect** if it’s selected.
12. Copy and save the **Key** and the **Secret** so they can be added into the CMA.
13. Click **Register Application**.

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

#### Sources

- **<tenant_domain>/puboauth/token** - Login
- **<tenant_domain>/pubapi/v2/audit/stream** - Audit

#### Known Limitations

- All different activities (Actions) are fetched.
