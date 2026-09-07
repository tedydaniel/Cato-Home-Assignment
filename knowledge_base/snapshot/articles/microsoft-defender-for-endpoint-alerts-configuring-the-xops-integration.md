---
title: "Microsoft Defender for Endpoint Alerts: Configuring the XOps Integration"
slug: "microsoft-defender-for-endpoint-alerts-configuring-the-xops-integration"
updated: 2026-09-01T12:10:47Z
published: 2026-09-01T12:10:47Z
canonical: "knowledge.catonetworks.com/microsoft-defender-for-endpoint-alerts-configuring-the-xops-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Defender for Endpoint Alerts: Configuring the XOps Integration

This article discusses integrating data from Microsoft Defender for Endpoint to generate stories that you can review in the Cato Stories Workbench.

## Overview of Endpoint Alert Stories

Using the Microsoft API, you can integrate alert data from Microsoft Defender for Endpoint to generate stories for endpoint devices. The endpoint stories help you get a more complete picture of potential threats in your network.

The Cato Endpoint Alerts engine creates a story by correlating data from Defender [Alerts](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/review-alerts?view=o365-worldwide) related to the same Defender Incident. Endpoint Alert stories include all relevant evidence for the Alerts detected by Defender. The Stories Workbench shows the endpoint stories together with the other story types, and you can sort and filter the stories to focus on the Endpoint Alert stories.

To integrate Defender for Endpoint alert data with Cato XOps, you need to first set up API connectors for Microsoft 365 and for Defender for Endpoint. After creating the connectors, the Endpoint Alert engine retrieves and analyzes the alert data from Defender for Endpoint.

For more information on reviewing XOps stories, including data from Microsoft Defender, see [Drilling-Down and Analyzing XOps Security Stories](/v1/docs/drilling-down-and-analyzing-xops-security-stories)

### 

### High Level Overview of Integrating Endpoint Alert Stories

This is a high level description of the workflow for integrating and reviewing Defender for Endpoint stories in the Stories Workbench:

1. Create the Microsoft 365 parent connector.
2. Create the Defender for Endpoint connector.
3. Review the Endpoint Alert stories in the Stories Workbench.

### Known Limitations

- The settings in the **Story Actions** panel are not configurable for Endpoint Alert stories. All fields related to the actions appear as N/A. For more about the **Story Actions** panel, see below.
- Microsoft Endpoint Alert stories for shared devices include in the story all users logged in to the device, while the relevant Defender for Endpoint Alert may show only one user.
- To add a connector, you must have editor permission for **Integrations** (in the **Resources** section). For more information, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).

## Understanding Microsoft Endpoint Alert Stories

The Microsoft Endpoint Alert producer generates stories based on the integration. This section explains the information available in the Overview tab of the story drill-down page.

![Defender for Endpoint Story updated.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36323980028829.png)

These are the story Overview widgets:

| Name | Description |
| --- | --- |
| Summary widget | The bar at the top of the page shows a summary of basic information about the story, including the: - Criticality of the threat - Summary of the story details - Severity of the threat as determined by an analyst - Verdict for the threat as determined by an analyst |
| Timeline | A timeline of events or actions taken in the story. |
| Details | Basic information for the story. - Click the **Incident URL** link to view the Incident in Microsoft Defender. |
| Entities | The entities involved in the incident. These could be Users, Devices, Sites, Data stores, applications, etc. A story can include alerts for multiple users and devices. |
| Alerts | Shows details for the Alerts related to the Defender Incident. - Expand an Alert to show a chronological process tree for the Evidences related to the Alert, including processes, files, and registry values - Click an item in the process tree to drill-down further and show granular data about the Evidence These are the columns in the table: - An **Alert Name** that describes the suspicious activity - **Criticality** - Overall risk score for the Alert as calculated by Cato's machine learning risk analysis algorithm (values are from 1 - 10) - The **Local IP** and **External IP** of the device involved in the Alert. - **Vendor User Name** - The user account Microsoft Defender associated with the alert - **Device Name** - Name of the device involved in the Alert - **OS** - Operating system of the device involved in the Alert - **Vendor Domain Name -** The Windows, AD, or local domain associated with the user account in the alert - **Alert ID** - The ID number for the Alert - **MITRE Techniques** - MITRE ATT&CK® techniques identified for the threat For more about the MITRE ATT&CK® framework, see [Using the MITRE ATT&CK® Dashboard](/v1/docs/using-the-mitre-att-ck-dashboard). - **Status** - Shows whether the Alert is **New** or was already **Resolved** - **First Activity Date** - Date of initial suspicious activity detected for the Alert - **Last Activity Date** - Date of most recent suspicious activity detected for the Alert - **Threat Name** - Name of malware detected. For example: Trojan:Win32/Startpage - **Description & Recommended Actions** - Click **View** for a brief Alert description and recommended steps for investigating and mitigating the threat |
| Evidences | Aggregates details for all the **Processes**, **Files**, **Registry** values, and **Network** parameters identified in the evidence for the various story Alerts. Some of the columns in the **Evidences** table are shared by all the types of Evidences, and some are specific per type. These are the columns that appear for all types of Evidences: - **Verdict** - Verdict generated by Defender for the piece of evidence (**Malicious**, **Suspicious**, or **No threats found**) - **Remediation Status** - Shows whether the threat was remediated - **Created** - Date and time when the event was recorded These are the specific columns for each type of Evidence: - **Processes:** - **Process Name** - Name of the executable file for the process - **Process ID** - Windows-assigned ID number for the process - **Process Command Line** - Arguments that were passed to the process in Windows. This can reveal important context about the execution of a suspicious process - **File Path** - Location on the endpoint device of the executable file for the process - **Files:** - **File Path** - Location of the file on the endpoint device - **File Name** - Name of the file including extension - **File Size** - Size of the file in bytes, kilobytes, or megabytes - **Registry:** - Registry key **Name** - **Registry Value Type** - Format of the data stored in the registry value - **Registry Value** - The value of the registry entry - **Network:** - Shows network data for the flow that generated the alert, such as the **Destination IP**, **Destination Port**, DNS and HTTP data, and the **URL** accessed |

## Overview of the Microsoft Connectors

To configure Cato's Microsoft Defender connector to fetch alert data, first you need to configure the Microsoft 365 connector as the parent app to give read permissions for the Defender connector. The parent app only has permissions to manage the Microsoft connectors. After configuring the Microsoft 365 connector, you can configure a Defender connector to retrieve the alert data.

If you want to import alert data from different sub-organizations within your organization, create a separate Microsoft 365 connector for each relevant Azure tenant, and then configure a Defender connector for each tenant.

### Prerequisites

- One of these Microsoft Licenses:
  - Microsoft Defender for Endpoint Plan 2
  - Microsoft 365 E5 (or higher) or Microsoft 365 E5 Security
  - Microsoft 365 A5 (Education) or Microsoft 365 G5 (Government)
  - Windows 11 Enterprise E5
- The Microsoft 365 connector requires an admin with the global admin role to give permissions to Cato's Defender connector

### Required Permissions for the Microsoft Defender Connector

To let the Defender connector retrieve the alert data from your Microsoft 365 account, the connector gives Cato the following permissions and actions with Microsoft 365:

- Connect to the Microsoft APIs and read all Defender for Endpoint data for an organization
- Sign in and read user profile

## Configuring the Microsoft Connectors

Configure a parent Microsoft 365 connector and then define a Defender connector for the Microsoft 365 account.

If your organization already configured a Microsoft 365 parent connector for another feature, such as a [Saas Security API](/v1/docs/what-is-the-data-protection-api) policy for Microsoft apps, or for importing [MIP labels](/v1/docs/using-mip-sensitivity-labels-in-your-cato-dlp-policy) to your DLP policy, you only need to configure a Defender connector.

### Configuring the Microsoft 365 Connector

Use the Cato Management Application to create the Microsoft 365 SaaS application connector for the relevant Azure tenant. You must have the correct credentials to authenticate to Microsoft 365 to add the connector to your Cato account.

![Endpoint_Connectors.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28977871348893.png)

**To configure the Microsoft 365 parent endpoint connector:**

1. From the navigation menu, select **Security > Connectors**, and select the **Connectors Settings** tab.
2. Click **New**. The **New Connector** panel opens.
3. From the **SaaS Application** drop-down menu, select the **Microsoft 365** app.

![MIP_New_Connector_MS365.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28977857009053.png)
4. Enter a unique **Connector Name**.
5. Click **Authorize and Save**.

A new browser tab opens to the Microsoft 365 app.
6. In the new browser tab, authenticate to the Microsoft 365 app:
  1. Select the Microsoft account for the Microsoft 365 app.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions to let Cato access the Microsoft 365 app.

![MIP_Labels_Parent_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28977843872285.png)
  4. The screen shows that you have successfully applied the permissions for the app.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28977859279773.png)

You can close the browser tab and return to the Cato Management Application.
7. The Microsoft 365 SaaS application is added to the **Connectors Settings** page.

![Endpoint_Connectors_-_MS_365.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28977840986909.png)

It can take Microsoft Azure several seconds to process the request, so if the **Status** shows **Pending user consent**, refresh the browser.

### Configuring the Microsoft Defender for Endpoint Connector

Use the Cato Management Application to create the Microsoft Defender for Endpoint SaaS application connector for the Azure tenant with the alert data you want to use. You must have the correct credentials to authenticate to Microsoft 365 to add the connector to your Cato account.

> [!NOTE]
> Note:
> 
> When you create an API connector for a Microsoft 365 app, the connector creates an authentication certificate that is valid for 3 months, and renews the certificate 7 days before expiration.

**To configure the Microsoft Defender connector:**

1. From the navigation menu, select **Security > Connectors**, and select the **Connectors Settings** tab.
2. Click **New**. The **New Connector** panel opens.
3. From the **Saas Application** drop-down menu, select the **Microsoft Defender** app.

![Defender_Connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28977843937693.png)
4. From the **Connector Tenant** drop-down menu, select the parent Microsoft 365 connector for the tenant with the alert data you want to use.
5. Enter a unique **Connector Name** for the Defender connector.
6. Click **Save**.
7. After the connector is successfully created, click **Authorize**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(201).png)

A new browser tab opens to the Microsoft 365 app.
8. In the new browser tab, authenticate to the Microsoft 365 app:
  1. Select the Microsoft account for the Microsoft 365 app.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions to let Cato access the Microsoft 365 app.
  4. The screen shows that you have successfully applied the permissions for the app.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28977859279773.png)

You can close the browser tab and return to the Cato Management Application.
9. The Microsoft Defender SaaS application is added to the **Connectors Settings** page.

![Endpoint_Connectors.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28977871348893.png)

It can take Microsoft Azure several seconds to process the request, so if the **Status** shows **Pending user consent**, refresh the browser.

### Understanding the Connector Status

The **Status** column on the Connectors Settings page shows the status of the connection between the Microsoft app and your Cato account. These are the explanations of the statuses:

- **Connected** - Your account is connected to the app and it is working correctly
- **Pending user consent** - Permissions have not been granted to let Cato access the Microsoft 365 app. To resolve this issue, refresh the browser. If **Status** changes to **Connected**, the issue is resolved, if **Status** doesn't change, delete and recreate the connector.
- **Error** - There is a connectivity, permissions, or other issue with the Microsoft connector. Delete and recreate the connector.

## Viewing the Stories Workbench Page

Once you have created the connector, stories will be visible in the Stories Workbench.

**To view the Stories Workbench page:**

- From the navigation menu, click **Home > Stories Workbench**.

For information about the columns in the Stories Workbench, see [Understanding the Stories Columns](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench)

For more information on reviewing XOps stories, including data from Microsoft Defender, see [Drilling-Down and Analyzing XOps Security Stories](/v1/docs/drilling-down-and-analyzing-xops-security-stories)
