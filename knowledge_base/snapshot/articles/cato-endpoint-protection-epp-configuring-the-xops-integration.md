---
title: "Cato Endpoint Protection (EPP): Configuring the XOps Integration"
slug: "cato-endpoint-protection-epp-configuring-the-xops-integration"
updated: 2026-07-23T12:43:50Z
published: 2026-07-23T12:43:50Z
canonical: "knowledge.catonetworks.com/cato-endpoint-protection-epp-configuring-the-xops-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Endpoint Protection (EPP): Configuring the XOps Integration

This article discusses how you can use the Stories Workbench to review XOps stories for Cato EPP alerts.

## Overview of Cato Endpoint Alert Stories

The Cato EPP solution integrates with Cato XOps to generate stories for endpoint devices. The endpoint stories help you get a more complete picture of potential threats in your network, and you can conduct investigations in a unified XOps platform extending into both the network and the endpoint.

The Cato Endpoint Alert engine creates a story by correlating data from all Cato EPP alerts that occurred on the same device within a 24-hour period. Cato Endpoint Alert stories include all relevant evidence detected by Cato EPP. The Stories Workbench shows the Cato EPP stories together with the other story types, and you can sort and filter the stories to focus on the Cato Endpoint Alert stories.

For more information on reviewing XOps stories, including data from Microsoft Cato EPP, see [Drilling-Down and Analyzing XOps Security Stories](/v1/docs/drilling-down-and-analyzing-xops-security-stories)

### Known Limitations

- If the Cato EPP agent is disconnected from the Internet for over 8 hours, it's possible that XOps stories won't be created for some EPP events from that period. However, the EPP agent continues to detect and block threats, and the events will be available in the Events page.
- Cato EPP XOps stores can take up to 4 hours to be visible on the Events page

### Prerequisites

- To add a connector, you must have editor permission for **Integrations** (in the **Resources** section). For more information, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).

## Showing the Stories Workbench Page

![Detection_Response_Workbench_Endpoint.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33409901577885.png)

Once you have created the connector, stories will be visible in the Stories Workbench.

**To view the Stories Workbench page:**

- From the navigation menu, click **Home > Stories Workbench**.

For information about the columns in the Stories Workbench see [Understanding the Stories Columns](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench).

### Understanding the Connector Status

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

### Showing the Cato Endpoint Alert Stories

You can group and filter the stories according to the **Cato Endpoint Alert** story type to quickly find stories for endpoint devices. For more about grouping and filtering stories, see [Reviewing Detection & Response XOps Stories in the Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench).
