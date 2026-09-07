---
title: "Microsoft Apps (Including Copilot): Configuring the App Activities Integrations"
slug: "microsoft-apps-including-copilot-configuring-the-app-activities-integrations"
updated: 2026-06-22T09:24:17Z
published: 2026-06-22T09:24:17Z
canonical: "knowledge.catonetworks.com/microsoft-apps-including-copilot-configuring-the-app-activities-integrations"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Apps (Including Copilot): Configuring the App Activities Integrations

This article explains how to configure the App Activities integration for Microsoft Apps.

The same process is required to configure the integration for all these applications.

## Overview

App Activities provides you with an API-based solution for out-of-band visibility of all activity made by any user in a connected SaaS application. To provide App Activities with visibility of data within an app, you need to set up an integration with the required application. Once you create the integration, if a field has changed or expired, you can edit it from the **Resources >Integrations > Integrated Apps** page. For more information, see [What is Application Control via API with App Activities](/v1/docs/what-is-application-control-via-api-with-app-activities).

To configure the App Activities integration, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A CASB license is required for App Activities. This license includes [app and data control](/v1/docs/what-is-the-unified-casb-solution) and App Activities via API. For more about purchasing a CASB license, please contact your Cato representative.

All activities (called Operations in Microsoft Exchange) are fetched.

### Benefits of Connecting Microsoft Apps

After creating this connector, you can view and monitor activity in your Microsoft Apps, for example:

- Office (e.g., Word, PowerPoint, Excel)
- CoPilot
- Power BI

This helps you identify and respond to suspicious activity, and you can receive alerts for these activities:

- Suspicious inbox forwarding
- Unusual volume of file deletion
- Activity from suspicious ip address
- Alerts on phishing/spam emails

### Supported Applications

This table lists the supported Microsoft applications and the connector that is required to be configured for each of them.

All four applications are configured with the same process outlined below.

| **Application** | **Connector** |
| --- | --- |
| - Microsoft 365 - All [Microsoft 365 apps](https://www.microsoft.com/en-us/microsoft-365/products-apps-services) are supported, including: - Microsoft 365 Copilot - Excel - Intune - PowerPoint - Word | Microsoft 356 Apps |
| - Entra ID | Microsoft Entra ID |
| - Exchange | Microsoft Exchange |
| - SharePoint - OneDrive for Business | Microsoft SharePoint and OneDrive Business |

## Configuring the Microsoft Apps Integration

To configure the integrations, create an API app.

### Prerequisites

- You must have one of these licenses:
  - Microsoft 365 E3
  - Microsoft 365 E3 license with E5 Compliance add-on
  - Microsoft 365 E3 license with E5 eDiscovery and Audit add-on
  - Office 365 E5 license
- You have admin permissions for your Microsoft Entra admin center
- The Office 365 Audit Log is enabled. For more information, see the [Microsoft documentation](https://learn.microsoft.com/en-us/office/office-365-management-api/troubleshooting-the-office-365-management-activity-api)
- Your Global Admin account is assigned the required administrative roles in both Microsoft Purview and Exchange, and the services are in a hydrated (fully provisioned) state. To do this:
  1. Ensure your admin account is a Global Administrator in Microsoft 365
  2. Assign the account administrative roles in both Microsoft Purview and Microsoft Exchange
  3. Sign in to the Purview and Exchange portals to trigger hydration
  4. To verify auditing is enabled and the roles have taken effect, after 60 minutes, re-run the UnifiedAuditLogIngestion command after propagation completes

### Step 1: Create the MS Tenant Integration

First, configure the MS Tenant integration as the parent connector. This connector can be used for all Microsoft integrations. If you have already created the parent connector, go to step 2.

**To create the MS Tenant integration:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated Apps** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **New Connector** panel, select the **MS Tenant (Configure a new MS Tenant)** app.

![New_Microsoft_365_Connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31557283398429(1).png)
4. Enter the **Connector Name**.
5. Click **Authorize and Save**.

A new browser tab opens to the Microsoft 365 app.
6. In the new browser tab, authenticate to the Microsoft 365 app:
  1. Select the Microsoft account for the Microsoft 365 app.

Otherwise, there may be a Microsoft authentication error.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions to let Cato access the Microsoft 365 app.
  4. The screen shows that you have successfully applied the permissions for the app.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31377643807901(1).png)

You can close the browser tab and return to the Cato Management Application.
7. The Microsoft 365 SaaS application is added to the **Integrated Apps** tab.

### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Integrated Apps** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. Select **App Activities**.
6. Select the **Microsoft Primary Tenant** that was created in Step 1.
7. (Optional) Add a description.
8. Click **Save**.

The CMA connects to the vendor
9. Click **Authorize**.

![image-20250826-133358.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31377680982429(1).png)

A Microsoft permissions screen will appear.
10. Review the requested permissions and click **Accept**.
11. The app is visible on the **Integrated Apps** table with a **Connected** status.

After connecting your APIs, you can track the App activities in the [Cloud Activities dashboard](/v1/docs/using-the-applications-activities-dashboard). Data may take a few minutes to appear.

### Sources

- **POST https://login.microsoftonline.com/{{tenant_id}}/oauth2/v2.0/token** - Login
- **GET https://manage.office.com/api/v1.0/{{tenant_id}}/activity/feed/subscriptions/list** - Confirming audit is enable
- **POST https://manage.office.com/api/v1.0/{{tenant_id}}/activity/feed/subscriptions/start?contentType={{a**udit_name}} - Enabling the audit (if required):
- **GET https://manage.office.com/api/v1.0/{{tenant_id}}/activity/feed/subscriptions/content?contentType={{audit_name}}&startTime={{start_time}}&;endTime={{end_time}}** - Listing the audit
- GET to the event URIs obtained from the previous response
