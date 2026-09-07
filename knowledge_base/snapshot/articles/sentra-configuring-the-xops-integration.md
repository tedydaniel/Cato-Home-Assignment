---
title: "Sentra: Configuring the XOps Integration"
slug: "sentra-configuring-the-xops-integration"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/sentra-configuring-the-xops-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sentra: Configuring the XOps Integration

This article discusses how to expand data security coverage by integrating data from Sentra to enrich stories that you can review in the Cato Stories Workbench.

## Overview

By integrating data from Sentra into the XOps platform, you can extend visibility into where sensitive data resides across cloud, SaaS, and data stores. This helps reduce data exposure risks by adding data-centric context to XOps detections and stories.

With the Sentra integration, the XOps platform detects exposed or misconfigured data stores, excessive access permissions, and violations involving regulated or critical data. This creates a unified risk view that combines data security posture with network, endpoint, and cloud signals.

Attackers often target sensitive data by exploiting misconfigurations or overly permissive access to data repositories. Once sensitive data is exposed, it can be exfiltrated directly or used to escalate attacks across the environment. The Sentra integration enables the XOps platform to correlate data exposure risks with other security events, providing the context needed to detect high-impact incidents early.

When a data misconfiguration or exposure is identified, you can mitigate the risk by configuring Cato DLP rules to restrict access to the affected data. This reduces the attack surface by limiting data movement and preventing unauthorized exfiltration while remediation is performed.

To integrate data from Sentra into XOps, you need to create an API connector for the Sentra application. After creating the connector, the XOps engine retrieves and analyzes the detection data from Sentra.

## Understanding Stories Created by the Integration

Stories generated from the integration are processed by the Generic Incident producer. The table below explains the widgets in these stories.

![Sentra_story_drilldown.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35652283386909.png)

| Name | Description |
| --- | --- |
| Summary widget | A summary of basic information about the story, including the: - Criticality of the threat - Summary of the story details - Severity of the threat as determined by an analyst - Verdict for the threat as determined by an analyst |
| Details | A summary explanation of the story and metadata. |
| Timeline | A timeline of events or actions taken in the story. |
| Entities | The entities where the stories occurred. These could be Users, Sites, Data stores, applications, etc. |
| Evidence | Supporting evidence to explain why an XOps story was generated. |
| Raw Data | Dynamic table containing the raw events that generated the story. |

## Configuring the Sentra Connector

To create the connector between Cato and your Sentra tenant, you need to:

1. Configure the integration in the Sentra console.
2. Create the API connector in the CMA.

### Prerequisites

- A Sentra DSPM (Data Security Posture Management) license for API access
- Administrator permissions to create API keys

### Step 1: Configuring the Integration in the Sentra Console

In the Sentra console, create an API key.

**To configure the integration:**

1. Log in to the Sentra console (https://app.sentra.io) with an account that has Administrator permissions.
2. From the Sentra console navigation menu, select **Settings > API Keys**.
3. Click **Create API Key**. and configure the key:
  - **Name** - Enter a name for the integration
  - **Expiration** - Select an expiration period. The maximum available option is recommended to reduce rotation overhead.
  - **Role** - Select a role that includes Alert read permissions (for example, **Viewer**).
  - Click **Create API Key**. The key is created and shown only once.
4. Copy and save the API key so it can be entered in the CMA. The key is required for authentication and can't be retrieved later.

**Note:** Store the key securely. The API key can't be retrieved after initial generation.

### Step 2: Create the API Connector in the CMA

After you have created the API client, add the details in the CMA.

**To configure the Sentra connector in the CMA:**

1. From the navigation menu, select **Resources > Integrations**.
2. On the **Integrated Apps** tab, click **New**. The **New Integration** panel opens.
3. Select the **SaaS Application** you want to add.
4. Enter the details created during step 1.
5. Click **Save**.
6. The app is visible on the **Integrated Apps** table with a **Connected** status.

## Viewing the Stories Workbench Page

Once you have created the connector, stories will be visible in the Stories Workbench.

**To view the Stories Workbench page:**

- From the navigation menu, click **Home > Stories Workbench**.

For information about the columns in the Stories Workbench, see [Understanding the Stories Columns](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench)

For more information on reviewing XOps stories, see [Drilling-Down and Analyzing XOps Security Stories](/v1/docs/drilling-down-and-analyzing-xops-security-stories)
