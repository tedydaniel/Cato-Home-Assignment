---
title: "Cyera: Creating the XOps Integration"
slug: "cyera-creating-the-xops-integration"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/cyera-creating-the-xops-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cyera: Creating the XOps Integration

This article discusses how to expand data security coverage by integrating data from Cyera to enrich stories that you can review in the Cato Stories Workbench.

## Overview

By integrating data from Cyera into the XOps platform, you can extend visibility into where sensitive data resides across cloud, SaaS, and data stores. This helps reduce data exposure risks by adding data-centric context to XOps detections and stories.

With the Cyera integration, the XOps platform detects exposed or misconfigured data stores, excessive access permissions, and violations involving regulated or critical data. This creates a unified risk view that combines data security posture with network, endpoint, and cloud signals.

Attackers often target sensitive data by exploiting misconfigurations or overly permissive access to data repositories. Once sensitive data is exposed, it can be exfiltrated directly or used to escalate attacks across the environment. The Cyera integration enables the XOps platform to correlate data exposure risks with other security events, providing the context needed to detect high-impact incidents early.

When a data misconfiguration or exposure is identified, you can mitigate the risk by configuring Cato DLP rules to restrict access to the affected data. This reduces the attack surface by limiting data movement and preventing unauthorized exfiltration while remediation is performed.

To integrate data from Cyera into XOps, you need to create an API connector for Cyera. After creating the connector, the XOps engine retrieves and analyzes the detection data from Cyera.

## Understanding Stories Created by the Integration

Stories generated from the integration are processed by the Generic Incident producer. The table below explains the widget in these stories.

![Cyera.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35509442567197.png)

| Name | Description |
| --- | --- |
| Summary widget | A summary of basic information about the story, including the: - Criticality of the threat - Summary of the story details - Severity of the threat as determined by an analyst - Verdict for the threat as determined by an analyst |
| Details | A summary explanation of the story and metadata. |
| Timeline | A timeline of events or actions taken in the story. |
| Entities | The entities where the stories occurred. These could be Users, Sites, Data stores, applications, etc. |
| Evidence | Supporting evidence to explain why an XOps story was generated. |
| Raw Data | Dynamic table containing the raw events that generated the story. |

## Configuring the Cyera Connector

To create the connector between Cato and your Cyera tenant, you need to:

1. Configure the integration in the Cyera console
2. Create the API connector in the CMA

### Step 1: Configuring the Integration in the Cyera Console

In the Cyera console, identify the base URL, Client ID, and Client secret.

**To configure the integration:**

1. In your Cyera console (https://<your_tenant>.cyera.io), from the profile icon, navigate to the **Integrations** and select the **Cato Networks** integration.
2. Choose the expiration timeline.
3. Click **Generate Token**.
4. Copy and save the following information so it can be entered into the CMA.

**Note:** This information is only displayed once.
  - Base URL (your Cyera API endpoint)
  - Client ID
  - Client Secret

### Step 2: Create the API Connector in the CMA

After you have created the API client, add the details in the CMA.

**To configure the Cyera connector in the CMA:**

1. From the navigation menu, select **Resources > Integrations**.
2. On the **Integrated Apps** tab, click **New**. The **New Integration** panel opens.
3. Select the **SaaS Application** you want to add.
4. Add the details created during step one.
5. Click **Save**.
6. The app is visible on the **Integrated Apps** table with a **Connected** status.

## Viewing the Stories Workbench Page

Once you have created the connector, stories will be visible in the Stories Workbench.

**To view the Stories Workbench page:**

- From the navigation menu, click **Home > Stories Workbench**.

For information about the columns in the Stories Workbench, see [Understanding the Stories Columns](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench)

For more information on reviewing XOps stories, see [Drilling-Down and Analyzing XOps Security Stories](/v1/docs/drilling-down-and-analyzing-xops-security-stories)
