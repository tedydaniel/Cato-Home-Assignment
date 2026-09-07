---
title: "Wiz: Configuring the XOps Integration"
slug: "wiz-configuring-the-xops-integration"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/wiz-configuring-the-xops-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Wiz: Configuring the XOps Integration

This article discusses integrating data from Wiz to generate stories that you can review in the Cato Stories Workbench.

## Overview

By integrating data from Wiz into the XOps platform, you can extend visibility and detection capabilities beyond your corporate network and endpoints. This reduces attack risks in cloud-native architectures, where new attack surfaces emerge.

With the Wiz integration, the XOps platform identifies and manages risks unique to cloud environments. This includes detecting insecure configurations, vulnerable applications, and exposed credentials. This creates a unified risk view that bridges on-premises and cloud assets under a single security framework.

Adversaries can exploit vulnerabilities in cloud infrastructure, for example misconfigured storage buckets or exposed APIs, to establish initial access. From there, they can pivot into the corporate network. The Wiz integration enables the XOps platform to detect cross-environment attacks early, providing the visibility and context needed to prevent lateral movement between cloud and on-premises systems.

To integrate Wiz data with XOps , you need to set up the API connectors for Wiz. After creating the connector, the XOps engine retrieves and analyzes the detection data from Wiz.

For more information on reviewing XOps stories, see [Drilling-Down and Analyzing XOps Security Stories](/v1/docs/drilling-down-and-analyzing-xops-security-stories).

### Understanding Stories Generated with the Wiz Connector

Stories generated from Wiz issues are processed by the Cloud Detection and Response producer in near real time. They are generated based on:

- Wiz source modules: Wiz Cloud and Wiz Defend
- Detection Types: Threat Detection, Cloud Configuration, and Graph Control
- Imported Data: Overview, Events Table, and Primary Resource from the Wiz issue

### Use Case - Login Failed for a from a Non-Organizational IP Address

![Wix_UC.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33409867777821.png)

Company XYZ manages its cloud environment through Google Workspace, where several users hold highly privileged roles with broad administrative access. However, the company faces visibility challenges when login attempts occur from outside its organizational network, especially when those attempts fail. Without proper detection, these events could indicate credential theft or brute-force attacks targeting critical accounts.

The company integrates XOps with their Wiz account. When Wiz detects a failed login attempt alert, XOps automatically ingests the data, enriches it with Cato’s identity and network context, and creates a correlated story highlighting the suspicious activity.

From the XOps story, the company can:

- Verify whether the failed login was legitimate or malicious
- Investigate the IP’s origin, geolocation, and reputation using correlated Cato network insights
- Identify whether similar attempts were made against other privileged users

By combining Wiz’s cloud intelligence with Cato’s contextual analytics, Company XYZ gains visibility into failed authentication attempts that could signal compromise attempts against administrative accounts. This proactive approach helps reduce investigation time, prevents credential-based attacks, and strengthens the organization’s overall identity security posture.

### Prerequisites

- You must have a Wiz Defend license
- To view Cato XOps stories for wiz issues, an XOps, or MDR license is required. The connector can be configured, and events generated without a license
- To add a connector, you must have editor permission for **Integrations** (in the **Resources** section). For more information, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).

## Configuring the Wiz Connector

To create the connector between Cato and your Wiz tenant, you need to:

1. Configure the integration in the Wiz App
2. Create the API connector in the CMA

### Step 1: Configure the Integration in the Wiz App

In the Wiz App, identify the Client ID and Client Secret.

**To configure the integration:**

1. In the [Wiz App](https://app.wiz.io/), navigate to **Settings > Access Management > Service Accounts**.
2. Click **Add Service Account**.

![Wiz.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33409849557533.png)
3. In the **Type** dropdown, select **Custom Integration (GraphQL API)**.
4. Add these API scopes:
  - read:security_scans
  - read:issues
  - read:controls
  - read:cloud_events_cloud
  - read:cloud_events_sensor
  - read:threat_issues
5. Copy and save the **Client ID** and **Client Secret** so they can be added to the CMA.
6. Click on your initials and select **Tenant Info**.
7. Copy and save the **API Endpoint URL** and **Authentication URL** so they can be added to the CMA.

### Step 2: Create the API Connector in the CMA

After you have created the API client, add the details in the CMA.

**To configure the Wiz connector in the CMA:**

1. From the navigation menu, select **Resources > Integrations**.
2. On the **Integrated Apps** tab, click **New**. The **New Integration** panel opens.
3. Select the **SaaS Application** you want to add.
4. Add the details created during step one.
5. Click **Save**.
6. The app is visible on the **Integrated Apps** table with a **Connected** status.

### Sources

- GraphQL endpoint
  - IssuesTable - Querying the Issues endpoint.

### Known Limitations

- All issues are currently fetched
- Stories cannot be muted
- Wiz Events data is not included in the XOps stories

## Viewing the Stories Workbench Page

Once you have created the connector, stories will be visible in the Stories Workbench.

**To view the Stories Workbench page:**

- From the navigation menu, click **Home > Stories Workbench**.

For information about the columns in the Stories Workbench, see [Understanding the Stories Columns](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench)

For more information on reviewing XOps stories, see [Drilling-Down and Analyzing XOps Security Stories](/v1/docs/drilling-down-and-analyzing-xops-security-stories)
