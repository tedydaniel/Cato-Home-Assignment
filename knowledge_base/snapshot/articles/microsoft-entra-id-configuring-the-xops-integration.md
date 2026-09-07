---
title: "Microsoft Entra ID: Configuring the XOps Integration"
slug: "microsoft-entra-id-configuring-the-xops-integration"
updated: 2026-07-23T12:44:32Z
published: 2026-07-23T12:44:32Z
canonical: "knowledge.catonetworks.com/microsoft-entra-id-configuring-the-xops-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Entra ID: Configuring the XOps Integration

This article discusses how you can use the Stories Workbench to review XOps stories for sign-in anomalies detected in Microsoft Entra ID Protection alerts.

## Overview

Microsoft Entra ID Protection helps organizations detect identity-based risks for their Entra ID tenant, such as anomalous sign-ins that may indicate malicious activity. Using the Microsoft API, you can integrate alert data from Microsoft Entra ID Protection to generate Cato XOps stories. This lets analysts include data from risky sign-ins within the broader context of XOps investigations. The Cato Entra Identity Alert engine creates a story by correlating data from Entra ID Protection alerts that occurred for the same user within a 24-hour period. The Stories Workbench shows the Entra Identity Alert stories together with the other story types, and you can sort and filter the stories to focus on the Entra Identity Alert stories.

You can also enrich Entra Identity Alert stories by integrating sign-in event data from Microsoft Entra ID. This provides context of the user's usual sign-in behavior which can be compared with the anomalous alert data provided by Entra ID Protection.

For more information on reviewing XOps stories, including data from Microsoft Entra ID, see [Drilling-Down and Analyzing XOps Security Stories](/v1/docs/drilling-down-and-analyzing-xops-security-stories)

### Prerequisites

- XOps stories for Microsoft Entra ID Protection alerts require configuring the Microsoft Entra ID Protection connector. For more about configuring the connector including the required Microsoft licenses and permissions, see [Configuring the Microsoft Entra ID Protection Connector for Sign-In Anomaly Data](/v1/docs/configuring-the-microsoft-entra-id-protection-connector-for-sign-in-anomaly-data).
- For sign-in event data in the **Sign-In Events** and **Sign-In Events on the User** widgets, configuring the Microsoft Entra ID connector is required. For more about configuring the connector including the required Microsoft license and permissions, see [Configuring the Microsoft Entra ID (Azure AD) Connector](/v1/docs/configuring-the-microsoft-entra-id-azure-ad-connector).
- To add a connector, you must have editor permission for **Integrations** (in the **Resources** section). For more information, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).

> [!NOTE]
> Notes:
> 
> - If you configure only the Microsoft Entra ID Protection connector, Entra Identity stories are generated, however the **Sign-In Events** and **Sign-In Events on the User** widgets show no data.
> - If you configure only the Microsoft Entra ID connector, no Entra Identity stories are generated.

#### Understanding the Connector Status

The Status column on the Connectors Settings page shows the status of the connection between the CrowdStrike app and your Cato account. These are the explanations of the statuses:

- **Connected** - Your account is connected to the app and working correctly
- **Pending user consent** - Permissions have not been granted to let Cato access the CrowdStrike app. To resolve this issue, refresh the browser. If **Status** changes to **Connected**, the issue is resolved, if **Status** doesn't change, delete and recreate the connector.
- **Error** - There is a connectivity, permissions, license, or other issue with the connector. Delete and recreate the connector.

## Viewing the Stories Workbench Page

Once you have created the connector, stories will be visible in the Stories Workbench.

**To view the Stories Workbench page:**

- From the navigation menu, click **Home > Stories Workbench**.

For information about the columns in the Stories Workbench see [Understanding the Stories Columns](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench)

For more information on reviewing XOps stories, see [Drilling-Down and Analyzing XOps Security Stories](/v1/docs/drilling-down-and-analyzing-xops-security-stories)
