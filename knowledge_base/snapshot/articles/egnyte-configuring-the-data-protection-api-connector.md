---
title: "Egnyte: Configuring the Data Protection API Connector"
slug: "egnyte-configuring-the-data-protection-api-connector"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/egnyte-configuring-the-data-protection-api-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Egnyte: Configuring the Data Protection API Connector

## Overview

The Data Protection API provides out-of-band visibility and control for sanctioned cloud apps. To provide Data Protection with access to an app, you need to set up an integration with the required application. For more information, see [What is the Data Protection API?](/v1/docs/what-is-the-data-protection-api).

To configure the Data Protection API integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A SaaS Security API license is required.

## Configuring the Egnyte Integration

To configure the Egnyte integration, use the Service Account user in your Egnyte account.

### Prerequisites

You must have purchased one of these licenses:

- Business
- Enterprise Lite
- Enterprise Platform

### Step 1: Configure the Integration in your Egnyte Account

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

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop down select Data And Threat Protection.
6. Add the details created during step one.
7. Click **Save**.
8. The app is visible on the **Integrated Apps** table with a **Connected** status.

## Adding Egnyte Rules to the Data Protection Policy

The Data Protection policy can monitor and manage the files and folders that your users upload with Egnyte.

### Understanding Egnyte Actions

When you create a Data Protection rule, you can define different actions to monitor or remediate the policy violations when the rule is matched. Each action automatically generates an event, and you can also choose to receive an email notification. For more about Data Protection API events, see [Analyzing Data Protection API Events](/v1/docs/egnyte-configuring-the-data-protection-api-connector#analyzing-data-protection-api-events).

These are the actions you can set for the Data Protection engine to perform when a rule is matched:

- **Monitor**: Detects and logs matching activity without enforcing any change, providing visibility for auditing and analysis.
- **Remove Share**: Automatically revokes sharing links or access to prevent external or unauthorized file access

### Configuring Egnyte Rules

Use the Data Protection page to add the SaaS application rules in your Data Protection policy.

Create a Data Protection rule to define the traffic that is scanned by Data Protection API. Create separate rules for each SaaS app connector, and then define the criteria which determines which traffic is scanned.

![EgnyteDPAPI.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33981421907997.png)

**To configure rules:**

1. From the navigation pane, select **Security > App & Data API Protection** and select or expand **Data Protection**.
2. Click **New**. The **New Rule** panel opens.
3. In **Application Connector**, select the Egnyte app.
4. Configure the required settings for the rule (see below for more information).
5. Select an **Action**.
6. **(Optional)** Define the tracking options for the rules to generate email notifications.

For more information about events and email notifications, see [Account Level Alerts and System Notifications](/v1/docs/account-level-alerts-and-system-notifications).
7. Click **Save**. The rule is added to the Data Protection policy.

### Understanding the Egnyte Rules

Each rule can be defined according to the following criteria:

- **Sharing Options**: Controls how files and folders can be shared, including link settings, access levels, and expiration rules
- **File Attributes**: Describes file metadata such as name, size, type, owner, and timestamps used for identification and policy decisions
- **Content Profile**: Analyzes file contents to classify data types, sensitivity, or patterns for security and compliance enforcement

## Analyzing Data Protection API Events

The Home > Events page shows all the Data Protection API events for your account. The powerful search tools let you drill-down and identify the few events that contain the relevant data that you need.

Data Protection API events can be identified by the following fields:

- Event Type - Security
- Sub-Type - SaaS Security API Data Protection

You can learn more about using the Events page [here](/v1/docs/analyzing-events-in-your-network).

### Explaining the Data Protection API Events Fields

| Field Name | Description |
| --- | --- |
| Connector Name | Name for the connector that is defined for the rule |
| Connector Type | SaaS app that is defined for this connector |
| DLP Profile | DLP Content Profile that generated this event |
| File Name | Name of the attached file |
| File Size | Size of the attached file |
| File Type | File type for the attached file |
| Matched Data Types | Data Types in the Content Profile that matched the rule |
| Collaborators | Email addresses of the users that received the file |
| Rule | Name of the rule in the Data Protection policy |
| Owner | File owner |
| Severity | Severity defined for the rule |
| Sharing Scope | Sharing Options for the Dropbox attachment |
