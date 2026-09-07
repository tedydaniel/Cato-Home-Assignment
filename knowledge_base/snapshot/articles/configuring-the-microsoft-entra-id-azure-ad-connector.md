---
title: "Configuring the Microsoft Entra ID (Azure AD) Sign-In Activities Connector"
slug: "configuring-the-microsoft-entra-id-azure-ad-connector"
updated: 2026-08-27T13:46:40Z
published: 2026-08-27T13:46:40Z
canonical: "knowledge.catonetworks.com/configuring-the-microsoft-entra-id-azure-ad-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring the Microsoft Entra ID (Azure AD) Sign-In Activities Connector

This article explains how to configure the Microsoft Entra ID (formerly Azure AD) connector to integrate data about Entra ID sign-ins with Cato events and the Cloud Activities Dashboard.

> [!NOTE]
> Note:
> 
> Microsoft recently changed the name of Azure AD to Entra ID. All mentions of Azure AD in Cato documentation refer to Entra ID.

## Overview of the Microsoft Connectors

To configure Cato's Microsoft Azure AD connector to fetch sign-in data, first you need to configure the Microsoft 365 connector as the parent app to give read permissions for the Azure AD connector. The parent app only has permissions to manage the Microsoft connectors. After configuring the Microsoft 365 connector, you can configure an Azure AD connector to retrieve the sign-in data.

If you want to import sign-in data from different sub-organizations within your organization, create a separate Microsoft 365 connector for each relevant Azure tenant, and then configure an Azure ID connector for each tenant.

### Prerequisites

- A Microsoft 365 E3 license or better, or a standalone Entra ID P1 or P2 plan is required.
- The Microsoft 365 connector requires an admin with the global admin role to give permissions to Cato's Azure AD connector.

### Required Permissions for the Microsoft Azure AD Connector

To let the Azure AD connector retrieve the sign-in data for your account, the connector gives Cato the following permissions and actions with Microsoft 365:

- Connect to the Microsoft APIs and read all Microsoft Azure AD (Entra ID) data for an organization.
- Sign in and read user profile.

## Configuring the Microsoft Connectors

To configure the Entra ID integration, you need to:

1. Create the MS Tenant Integration (if you do not have this already configured)
2. Create the API connector in the CMA

### Step 1: Configuring the MS Tenant Integration

First, configure the MS Tenant integration as the parent connector. This connector can be used for all Microsoft integrations. If you have already created the parent connector, go to step 2.

**To create the Microsoft 365 parent connector:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated Apps** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **New Connector** panel, select the **Microsoft 365 (New Tenant)** app.

![New_Microsoft_365_Connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30488165116573.png)
4. Enter the **Connector Name**.
5. Click **Authorize and Save**.

A new browser tab opens to the Microsoft 365 app.
6. In the new browser tab, authenticate to the Microsoft 365 app:
  1. Select the Microsoft account for the Microsoft 365 app.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions to let Cato access the Microsoft 365 app.
  4. The screen shows that you have successfully applied the permissions for the app.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30488165141277.png)

You can close the browser tab and return to the Cato Management Application.
7. The Microsoft 365 SaaS application is added to the **Integrated Apps** tab.

![Azure_AD_Connector_Settings.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30488132028829.png)

### Step 2: Configuring the Entra ID Connector

After you have created the MS Tenant integration, you can create the Entra ID connector.

> [!NOTE]
> Note:
> 
> When you create an API connector for a Microsoft 365 app, the connector creates an authentication certificate that is valid for 3 months, and renews the certificate 7 days before expiration.

**To configure the Microsoft Azure AD connector:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated Apps** tab.
2. Click **New**. The **New Connector** panel opens.
3. From the **Saas Application** drop-down menu, select **Microsoft** **Entra ID.**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(198).png)
4. Select **Sign In Activities**.
5. In the **Auth** drop-down, choose **Consent Microsoft**
6. Add a **Name** and **Description** for the connector.
7. In the **Parent ID** drop-down, select the **Microsoft Primary Tenant** that was created in Step 1.
8. Click **Save**.

The CMA connects to the vendor
9. Click **Authorize**.

A Microsoft permissions screen will appear.
10. Review the requested permissions and click **Accept.**

The app is visible on the **Integrated Apps** table with a **Connected** status.

### Understanding the Connector Status

The **Status** column on the Connectors Settings page shows the status of the connection between the Microsoft app and your Cato account. These are the explanations of the statuses:

- **Connected** - Your account is connected to the app and it is working correctly.
- **Pending user consent** - Permissions have not been granted to let Cato access the Microsoft 365 app. To resolve this issue, refresh the browser. If **Status** changes to **Connected**, the issue is resolved, if **Status** doesn't change, delete and recreate the connector.
- **Error** - There is a connectivity, permissions, or other issue with the Microsoft connector. Delete and recreate the connector.

## Cato Event and API Fields for Azure AD Sign-Ins

These are the relevant fields for Azure AD sign-in events of sub-type **Application Sign-in**.

The [eventsFeed](https://api.catonetworks.com/documentation/#query-eventsFeed) query of the Cato API shows data for Azure AD sign-ins in these fields for eventFieldName type, you can see descriptions of the fields: [here](https://api.catonetworks.com/documentation/#definition-EventFieldName).

| API enum Value | Event Field |
| --- | --- |
| is_compliant | Is Compliant |
| is_managed | Is Managed |
| vendor_event_id | Vendor Event Id |
| tenant_id | Tenant Id |
| tenant_name | Tenant Name |
| sign_in_event_types | Sign In Types |
| risk_level | Risk Level |
| client_class | Client Class |
