---
title: "Salesforce: Configuring the SaaS Posture Integration"
slug: "salesforce-configuring-the-saas-posture-integration"
updated: 2026-07-06T12:10:33Z
published: 2026-07-06T12:10:33Z
canonical: "knowledge.catonetworks.com/salesforce-configuring-the-saas-posture-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Salesforce: Configuring the SaaS Posture Integration

## Overview

## Overview

SaaS Posture integrations provide visibility into the configuration and security posture of your connected SaaS applications. Cato continuously reviews the application settings and compares them to the recommended posture defined by Cato’s research team. This helps identify misconfigurations that can increase risk, such as authentication settings, third-party integrations, and data-sharing controls.

Posture data appears in the Applications dashboard, where you can view posture scores and the highest-severity findings across connected applications. You can review each posture check from the Posture page, including the issue details, status, and remediation action required to pass the check.

For more information, see [Reviewing the Security Posture of Your SaaS Applications.](https://knowledge.catonetworks.com/v1/docs/understanding-the-security-posture-of-your-saas-applications)

To configure the SaaS Posture integration, you need to:

1. Configure the required settings in the SaaS application
2. Create the API connector in the CMA

A CASB license is required for SaaS Posture integrations.

## Configuring the Salesforce Integration

To configure the Salesforce integration, create a connected app.

### Prerequisites

- You must enable API access in your Salesforce account

### Step 1: Configure the Integration in your Salesforce Tenant

In your Salesforce tenant, identify the Consumer Key and Consumer Secret to enter into the CMA.

**To configure the Salesforce integration:**

Complete the following steps to configure the Salesforce integration:

**Create an Integration User and assign the required permission set:**

1. In your Salesforce tenant, open **Setup** by clicking on the gear icon in the top right of the screen.
2. Search for **Users** and open the **Users** page
3. Click **New User** and add these details:
  - **User License:** Salesforce
  - **Profile:** Standard User
4. Click **Save**.
5. In the **Setup** search, search for **Permission Sets** and click **New.**
6. Add a label and click **Save**.
7. Open **System Permissions**, click **Edit**, and enable these permissions:
  - API Enabled
  - API Only Users
  - View Setup and Configuration
  - Customize Application
  - View all External Client Apps
8. Under **Object Settings**, great **Read** access for:
  - Allowed Email Domain
  - Email Services Function
9. Navigate to **Manage Assignments > Add Assignment**, select the integration user from Step 3, and assign.

**Create a new external client app:**

1. In your Salesforce tenant, open **Setup** by clicking on the gear icon in the top right of the screen.
2. Search for **External Client App Manager**.
3. Click **New External Client App**.
4. In the **Basic Information** section, add these details:
  - **External Client App Name:** `Cato SaaS Posture`
  - **Contact Email:** An admin email address (Salesforce sends identity-verification codes here)
  - **Distribution State:** Local
5. Expand the **API (Enable OAuth Settings)** section and configure:
  - **Enable OAuth:** Check the checkbox
  - **Callback URL:** `https://cc.catonetworks.com/redirect/cas/salesforce/callback`
  - **Selected OAuth Scopes:** Select Manage user data via APIs (api)
6. Click **Create**.

**Retrieve the Consumer Key and Consumer Secret:**

1. On the External Client App detail page of the app you created, open the **Settings** tab.
2. Expand **OAuth Settings** and click **Manage Consumer Details**.
3. Complete the verification steps
4. Copy and save the **Consumer Key** and **Consumer Secret** so they can be entered into the CMA.

**Identify the Base URL:**

1. Navigate to **Setup > Company Settings > My Domain** and copy and save the **Current My Domain URL** field so it can be entered into the CMA.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations.**
2. Click the **Configured Integrations** tab.
3. Click **New**. The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop-down select **SaaS Posture**.
6. Add the details created during step one.
  - **Base URL:** My Domain URL
  - **Client ID:** Consumer Key
  - **Client Secret:** Consumer Secret
7. Click **Save**.

The app is visible on the **Integrated Apps** table with a **Connected** status.
