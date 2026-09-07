---
title: "Synk: Configuring the SaaS Anomalies Connector"
slug: "synk-configuring-the-saas-anomalies-connector"
updated: 2026-06-22T09:24:33Z
published: 2026-06-22T09:24:33Z
canonical: "knowledge.catonetworks.com/synk-configuring-the-saas-anomalies-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Synk: Configuring the SaaS Anomalies Connector

This article explains how to configure the SaaS Anomalies connector for Synk.

## Overview

The Snyk connector lets you monitor security alerts from your Snyk environment in Cato. This includes posture issues and vulnerabilities detected in your projects and infrastructure. By integrating Snyk with Cato, you gain centralized visibility into these alerts for easier monitoring and investigation. This helps you respond more quickly and maintain stronger security oversight across your environment.

To configure the SaaS Anomalies integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

## Configuring the Synk Integration

To configure the Synk integration, create an API key and your Group ID.

### Prerequisites

- A Synk Enterprise plan

### Step 1: Configure the Integration in the Synk Application

Create an API key and your Group ID in the Synk application.

**To configure the Synk integration:**

1. Log into the Synk application.
2. From the left side bar, choose the Group you would like to integrate, then click **Settings**.
3. Select **Member roles > Create new Role**.
4. In the **Create new role** dialog box, add a name and description and set the Role Type to **Group**.
5. Click **Create role**.
6. Provide the following permissions:
  - Group Level Permissions:
    - Group Management: View groups
    - Organization Management: View Organizations
    - Audit Log Management: View Audit Logs
    - Issue Management: View Issues
  - Organization Level Permissions:
    - Organization Management: View Organizations
    - Audit Log Management: View Audit Logs
    - Collection Management: View Collections
    - Container Image Management: View container images
    - Entitlement Management: View entitlements
    - Integration Management: View integrations
    - Project Management: View projects
    - Project Management: View project history
    - Project Management: View Jira issues
    - Ignore Management: View Ignores
    - Service Account Management: View service accounts
    - Snyk Apps Management: View Apps
    - Snyk Cloud Management: View environments
    - User Management: View users
    - Snyk Learn Assignments Management: View organization assignments
7. Navigate to **Service Accounts > Create Service Account**, select the role you created and check the API Key (no expiry) checkbox.
8. In the dialog box, copy and save the API key so it can be entered into the CMA.
9. Navigate to the Group settings, under General copy and paste the **Group ID** so it can be entered into the CMA.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop down select **SaaS Anomalies**.
6. Add the details created during step one.
7. Click **Save**.
8. The app is visible on the **Integrated Apps** table with a **Connected** status.
