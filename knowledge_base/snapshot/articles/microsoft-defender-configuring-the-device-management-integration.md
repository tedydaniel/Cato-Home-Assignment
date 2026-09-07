---
title: "Microsoft Defender: Configuring the Device Management Integration"
slug: "microsoft-defender-configuring-the-device-management-integration"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/microsoft-defender-configuring-the-device-management-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Defender: Configuring the Device Management Integration

This article explains how to configure the Device Management integration for Microsoft Defender.

## Overview

To enhance device intelligence, you can integrate Microsoft Defender device metadata with Cato’s device discovery for the IoT/OT Security service. Metadata from both platforms is merged, creating unified device profiles that enhance visibility and classification.

The combined view appears on the **Home > Devices > Inventory** tab and helps improve identification of both managed and unmanaged assets. With more accurate and complete device data, you can make better-informed security decisions across your network. For more information on Device Inventory, see [What is Device Inventory?](/v1/docs/what-is-device-inventory).

This integration enhances device intelligence and does not support Device Posture checks.

To configure the Device Management integration, you need to:

1. Create the Microsoft 365 Parent Connector
2. Create the Microsoft Defender Connector

An IoT/OT Security license is required for this feature.

## Configuring the Defender Integration

To configure the Defender integration, create an API app.

### Prerequisites

- You must have an IoT/OT License
- You must have one of the following Microsoft licenses:
  - Microsoft 365 E5 license
  - Microsoft 365 E3 license with E5 Compliance add-on
  - Microsoft 365 E3 license with E5 eDiscovery and Audit add-on
  - Office 365 E5 license
- To add a connector, you must have editor permission for **Integrations** (in the **Resources** section). For more information, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).

## Step 1: Create the Microsoft 365 Parent Connector

First, configure the MS Tenant integration as the parent connector. This connector can be used for all Microsoft integrations. If you have already created the parent connector, go to step 2.

**To create the MS Tenant integration:**

1. From the navigation menu, select **Resources > Integrations** and click the **Integrated Apps** tab.
2. Click **New**. The **New Connector** panel opens.
3. In the **New Connector** panel, select the **MS Tenant (Configure a new MS Tenant)** app.

![New_Microsoft_365_Connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34167864064413.png)
4. Enter the **Connector Name**.
5. Click **Authorize and Save**.

A new browser tab opens to the Microsoft 365 app.
6. In the new browser tab, authenticate to the Microsoft 365 app:
  1. Select the Microsoft account for the Microsoft 365 app.

Otherwise, there may be a Microsoft authentication error.
  2. Enter the password for the app and approve it.
  3. **Accept** the permissions to let Cato access the Microsoft 365 app.
  4. The screen shows that you have successfully applied the permissions for the app.

![Success_Connector_Permissions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34167830321309.png)

You can close the browser tab and return to the Cato Management Application.
7. The Microsoft 365 SaaS application is added to the **Integrated Apps** tab.

## Step 2: Create the Microsoft Defender Connector

After you have set up the Microsoft 365 Parent Connector, create the Defender connector.

**To create the Microsoft Defender connector:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. Select the **Microsoft Primary Tenant** that was created in Step 1.
6. (Optional) Add a description.
7. Click **Save**.

The CMA connects to the vendor.
8. Click **Authorize**.

![image-20250826-133358.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34167869541149.png)

A Microsoft permissions screen will appear.
9. Review the requested permissions and click **Accept**.
10. The app is visible on the **Integrated Apps** table with a **Connected** status.
