---
title: "Cursor: Configuring the SaaS Posture Integration"
slug: "cursor-configuring-the-saas-posture-integration"
status: "update"
updated: 2026-09-03T11:57:13Z
published: 2026-09-03T11:57:13Z
canonical: "knowledge.catonetworks.com/cursor-configuring-the-saas-posture-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cursor: Configuring the SaaS Posture Integration

## Overview

SaaS Posture integrations provide visibility into the configuration and security posture of your connected SaaS applications. Cato continuously reviews the application settings and compares them to the recommended posture defined by Cato’s research team. This helps identify misconfigurations that can increase risk, such as authentication settings, third-party integrations, and data-sharing controls.

Posture data appears in the Applications dashboard, where you can view posture scores and the highest-severity findings across connected applications. You can review each posture check from the Posture page, including the issue details, status, and remediation action required to pass the check.

For more information, see [Reviewing the Security Posture of Your SaaS Applications.](https://knowledge.catonetworks.com/v1/docs/understanding-the-security-posture-of-your-saas-applications)

To configure the SaaS Posture integration, you need to:

1. Configure the required settings in the SaaS application
2. Create the API connector in the CMA

A CASB license is required for SaaS Posture integrations.

## Configuring the Cursor Integration

To configure the Cursor integration, create an API Key.

### Prerequisites

- A Cursor Team or Enterprise (Business) plan
- An account with Owner (admin) access

### Step 1: Configure the Integration in the Cursor Dashboard

In the Cursor dashboard, create the API Key. **To configure the Cursor integration:**

1. In the [Cursor dashboard](https://cursor.com/dashboard), sign in as a team admin (Owner).
2. Navigate to **Settings > Cursor Admin API Keys**.
3. Click **New API Key**.
4. Give the key a descriptive name.
5. Copy and save the key so it can be entered into the CMA.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations.**
2. Click the **Configured Integrations** tab.
3. Click **New**. The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop-down, select **SaaS Posture**.
6. In **Tenant Name**, enter a recognizable name for your Cursor organization. This value is used to identify the tenant in SaaSs Posture findings.
7. Add the details created during step one.
  - **API Key**: The key you created in step 1.
8. Click **Save**.

The app is visible on the **Integrated Apps** table with a **Connected** status.

### Known Limitations

- **Inactivity is derived from 90 days of daily usage data.** If the full 90-day window cannot be retrieved (e.g., the team is younger than 90 days, or a usage page errors), the **No Inactive Licensed Users** check reports no signal instead of a false positive.
- **Spend and usage are optional enrichment.** If /teams/spend or /teams/daily-usage-data is unavailable, the **User Spend Limits Configured**, **Client Version Up to Date**, and **No Inactive Licensed Users** checks show no verdict for the affected members rather than a failure.
