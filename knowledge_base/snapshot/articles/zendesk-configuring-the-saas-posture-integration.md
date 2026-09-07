---
title: "Zendesk: Configuring the SaaS Posture Integration"
slug: "zendesk-configuring-the-saas-posture-integration"
updated: 2026-07-06T12:11:17Z
published: 2026-07-06T12:11:17Z
canonical: "knowledge.catonetworks.com/zendesk-configuring-the-saas-posture-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Zendesk: Configuring the SaaS Posture Integration

## Overview

## Overview

SaaS Posture integrations provide visibility into the configuration and security posture of your connected SaaS applications. Cato continuously reviews the application settings and compares them to the recommended posture defined by Cato’s research team. This helps identify misconfigurations that can increase risk, such as authentication settings, third-party integrations, and data-sharing controls.

Posture data appears in the Applications dashboard, where you can view posture scores and the highest-severity findings across connected applications. You can review each posture check from the Posture page, including the issue details, status, and remediation action required to pass the check.

For more information, see [Reviewing the Security Posture of Your SaaS Applications.](https://knowledge.catonetworks.com/v1/docs/understanding-the-security-posture-of-your-saas-applications)

To configure the SaaS Posture integration, you need to:

1. Configure the required settings in the SaaS application
2. Create the API connector in the CMA

A CASB license is required for SaaS Posture integrations.

## Configuring the Zendesk Integration

To configure the Zendesk integration, create an API token.

#### Prerequisites

- You must have purchased the Zendesk Enterprise plan.

#### Step 1: Configure the Integration in the Zendesk Admin Center

In the Zendesk Admin Center, identify the API Token to enter into the CMA.

**To configure the Zendesk integration:**

1. In the Admin Center, navigate to **Apps and integrations > API configuration** and check the **Allow API token access** check box.
2. Click **Save**.
3. Navigate to **Apps and integrations > API tokens** and click **Add API token**.
4. Add a **Description** and click **Save**.
5. Copy and save the **Token** so it can be entered into the CMA.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations.**
2. Click the **Configured Integrations** tab.
3. Click **New**. The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop-down, select **SaaS Posture**.
6. Add the details created during step one.
  - **Instance URL**: Your Zendesk subdomain URL, e.g., `https://&lt;yourcompany&gt;.zendesk.com`
  - **Username**: The admin email address used to sign in (e.g., `admin@yourcompany.com`)
  - **Password:** The token generated in step one.
7. Click **Save**.

The app is visible on the **Integrated Apps** table with a **Connected** status.
