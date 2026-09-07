---
title: "SentinelOne EDR: Configuring the XOps Integration"
slug: "sentinelone-edr-configuring-the-xops-integration"
updated: 2026-07-23T12:44:49Z
published: 2026-07-23T12:44:49Z
canonical: "knowledge.catonetworks.com/sentinelone-edr-configuring-the-xops-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SentinelOne EDR: Configuring the XOps Integration

This article discusses integrating data from SentinelOne EDR to generate stories that you can review in the Cato Stories Workbench.

## Overview

Using an API connector, you can integrate incident data from SentinelOne EDR to generate stories for endpoint devices. The endpoint stories help you get a more complete picture of potential threats in your network.

A story is created in the CMA by correlating data from SentinelOne EDR incidents based on the Agent UUID (Device ID) and the threat file Hash within 90 days. These stories include all relevant evidence for the incidents detected by SentinelOne. The Stories Workbench shows the endpoint stories together with the other story types, and you can sort and filter the stories to focus on the Endpoint incidents.

SentinelOne stories are created in near real-time after the original alert is generated.

To integrate SentinelOne EDR incident data with Cato XOps, you need to set up the API connectors for SentinelOne EDR. After creating the connector, the Endpoint Incident engine retrieves and analyzes the Incident data from SentinelOne EDR.

For more information on reviewing XOps stories, including data from SentinelOne, see [Drilling-Down and Analyzing XOps Security Stories](/v1/docs/drilling-down-and-analyzing-xops-security-stories)

### Prerequisites

- You must have a SentinelOne Enterprise license, including the Singularity Data Lake
- To view Cato XOps stories for SentinelOne EDR incidents, an XOps, or MDR license is required. Events are generated without a license
- To add a connector, you must have editor permission for **Integrations** (in the **Resources** section). For more information, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).

## Configuring the SentinelOne EDR Connector

To create the connector between Cato and your SentinelOne tenant, you need to:

1. Create the API token in the SentinelOne console
2. Create the API connector in the CMA

You must have the correct credentials to authenticate to SentinelOne.

### Step 1: Create the API Token in the SentinelOne Console

In the SentinelOne console, create the API token to enter into the CMA.

**To create the API token:**

1. In your SentinelOne console tenant, in the side menu, navigate to **Settings > Choose Users**.
2. On the **Service Users** tab, click **Actions > Create New Service User**.

![New_Service_User.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27591497030429.png)
3. Add a **Name** and **Expiration date** for the Service User. We recommend setting the expiration date to at least one year.

**Note:** The Token must be renewed once it has expired.
4. Click **Next**.
5. Choose the **Account** level and check the box of the relevant account.

![Scope.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27591509163421.png)
6. Click **Create User**. You may be required to enter your MFA code.
7. Copy and save the API token so it can be added to the CMA.

### Step 2: Create the API Connector in the CMA

After you have an API Token, add the details in the CMA.

![S1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27315293048093.png)

**To configure the SentinelOne EDR Connector in the CMA:**

1. From the navigation menu, select **Resources > Integrations**.
2. On the **Integrated Apps** tab, click **New**. The **New Integration** panel opens.
3. From the **SaaS Application** drop-down menu, select SentinelOne.
4. Enter a **Name**, **Description** (optional), **Tenant URL** (the domain of your tenant), and **API Token**.

**Note:** Include https:// in the tenant URL. For example, https://<YOUR_TENANT>.sentinelone.net
5. (Optional) Choose to track errors in the integration by creating an event.
6. Click **Save**.

## Understanding the Connector Status

The **Status** column on the Connectors Settings page shows the status of the connection between the SentinelOne app and your Cato account. These are the explanations of the statuses:

- **Connected** - Your account is connected to the app and working correctly
- **Pending user consent** - Permissions have not been granted to let Cato access the SentinelOne app. To resolve this issue, refresh the browser. If **Status** changes to **Connected**, the issue is resolved, if **Status** doesn't change, delete and recreate the connector.
- **Error** - There is a connectivity, permissions, license, or other issue with the connector. Delete and recreate the connector.

## Viewing the Stories Workbench Page

Once you have created the connector, stories will be visible in the Stories Workbench.

**To view the Stories Workbench page:**

- From the navigation menu, click **Home > Stories Workbench**.

For information about the columns in the Stories Workbench, see [Understanding the Stories Columns](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench)

For more information on reviewing XOps stories, see [Drilling-Down and Analyzing XOps Security Stories](/v1/docs/drilling-down-and-analyzing-xops-security-stories)
