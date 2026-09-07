---
title: "CrowdStrike: Configuring the XOps Integration"
slug: "crowdstrike-configuring-the-xops-integration"
updated: 2026-07-23T12:45:07Z
published: 2026-07-23T12:45:07Z
canonical: "knowledge.catonetworks.com/crowdstrike-configuring-the-xops-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CrowdStrike: Configuring the XOps Integration

This article discusses integrating data from CrowdStrike EDR to generate stories that you can review in the Cato Stories Workbench.

## Overview

Using an API connector, you can integrate data from CrowdStrike detections to generate stories for endpoint devices. The endpoint stories help you get a more complete picture of potential threats in your network.

A story is created in the CMA by correlating CrowdStrike detections based on the Incident ID. These stories include all relevant evidence for the detection identified by CrowdStrike. The Stories Workbench shows the endpoint stories together with the other story types, and you can sort and filter the stories to focus on the Endpoint incidents.

CrowdStrike stories are created in near real-time after the original alert is generated.

To integrate CrowdStrike EndPoint Detection data with Cato XOps, you need to set up the API connectors for CrowdStrike. After creating the connector, the Endpoint Detection engine retrieves and analyzes the detection data from CrowdStrike.

For more information on reviewing XOps stories, including data from CrowdStrike, see [Drilling-Down and Analyzing XOps Security Stories](/v1/docs/drilling-down-and-analyzing-xops-security-stories).

### Prerequisites

- To view Cato XOps stories for CrowdStrike detections, an XOps, or MDR license is required. Events are generated without a license
- A Falcon Insight (EDR) license is required
- To add a connector, you must have editor permission for **Integrations** (in the **Resources** section). For more information, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).

## Configuring the CrowdStrike Connector

To create the connector between Cato and your CrowdStrike tenant, you need to:

1. Create the API Client in the Falcon Crowdstrike platform
2. Create the API connector in the CMA

### Step 1: Create the API Client in the Falcon CrowdStrike Platform

In the Falcon CrowdStrike platform, create the API Client.

**To create the API Client:**

1. In your Falcon CrowdStrike platform, navigate to **Support and resources > API clients and keys**.

![CS_nav.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27314531321501.png)
2. Click **Create API client**.
3. Add a **Client name** and **Description**, and **Read** access for these scopes:
  - Alerts
  - Incidents
  - Threatgraph
4. Save the **Client ID**, **Secret**, and **Base URL** so they can be added in the CMA.

#### Step 2: Create the API Connector in the CMA

After you have created the API client, add the details in the CMA.

![CS1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27314531387933.png)

**To configure the CrowdStrike Connector in the CMA:**

1. From the navigation menu, select **Resources > Integrations**.
2. On the **Integrated Apps** tab, click **New**. The **New Integration** panel opens.
3. From the **SaaS Application** drop-down menu, select CrowdStrike.
4. Enter a **Name**, **Description** (optional), and the **Base URL**, **Application ID**, and **Client Secret Value** from step 1.
5. (Optional) Choose to track errors in the integration by creating an event.
6. Click **Save**.

#### Understanding the Connector Status

The Status column on the Connectors Settings page shows the status of the connection between the CrowdStrike app and your Cato account. These are the explanations of the statuses:

- **Connected** - Your account is connected to the app and working correctly
- **Pending user consent** - Permissions have not been granted to let Cato access the CrowdStrike app. To resolve this issue, refresh the browser. If **Status** changes to **Connected**, the issue is resolved, if **Status** doesn't change, delete and recreate the connector.
- **Error** - There is a connectivity, permissions, license, or other issue with the connector. Delete and recreate the connector.

### Viewing the Stories Workbench Page

Once you have created the connector, stories will be visible in the Stories Workbench.

**To view the Stories Workbench page:**

- From the navigation menu, click **Home > Stories Workbench**.

For information about the columns in the Stories Workbench, see [Understanding the Stories Columns](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench)

For more information on reviewing XOps stories, see [Drilling-Down and Analyzing XOps Security Stories](/v1/docs/drilling-down-and-analyzing-xops-security-stories)
