---
title: "Zoom: Configuring the Device Management Integration"
slug: "zoom-configuring-the-device-management-integration"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/zoom-configuring-the-device-management-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Zoom: Configuring the Device Management Integration

This article explains how to configure the Device Inventory integration for Zoom.

## Overview

To enhance device intelligence, you can integrate Zoom device data, for example details of the operating system version, with Cato's device discovery for the IoT/OT Security service. Data from both platforms is merged, creating unified device profiles that enhance visibility and classification.

The combined view appears on the **Home > Devices > Inventory** tab and helps improve identification of both managed and unmanaged assets. With more accurate and complete device data, you can make better-informed security decisions across your network. For more information on Device Inventory, see [What is Device Inventory?](/v1/docs/what-is-device-inventory).

To configure the Device Management integration, you need to:

- Configure the integration in Zoom
- Create the API connector in the CMA

An IoT/OT Security license is required for this feature.

## Configuring the Zoom Integration

To create the Zoom integration, create a Server OAuth App in the Zoom App marketplace.

### Prerequisites

- You must have a Zoom Business plan or a higher plan that includes the Zoom Quality of Service Subscription (QSS)
- These Scopes (Permission) are provided:
  - dashboard:read:list_meetings:admin - View meetings metrics
  - dashboard:read:list_meeting_participants_qos:admin - View meeting participants' quality of service
  - user:read:user:admin - View a user
- Zoom users must have individual accounts (for example, not a generic business account)
- To add a connector, you must have editor permission for **Integrations** (in the **Resources** section). For more information, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).

### Step 1: Configure the Integration in the Zoom App Marketplace

In the Zoom App Marketplace, identify the **Account ID**, **Client ID**, and **Client Secret** to enter into the CMA.

**To configure the Zoom integration:**

1. Log in to the [Zoom App Marketplace](https://marketplace.zoom.us/).
2. Click **Develop > Build App**.
3. Select **Server to Server OAuth App** and click **Create**.

![Zoom.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33409884913821.png)
4. Choose a name for the app.
5. On the **App Credentials** page, copy and save the **Account ID**, **Client ID**, and **Client Secret**, so they can be added into the CMA.
6. On the **Information** page, add the required information.
7. On the **Scopes** page, click **Add Scopes** and add these scopes:
  - dashboard:read:list_meetings:admin - View meetings metrics
  - dashboard:read:list_meeting_participants_qos:admin - View meeting participants' quality of service
  - user:read:user:admin - View a user
8. On the **Activation** page, click **Activate your app**.

### Step 2: Create the API Connector in the CMA

After you have set up an integration, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Integrated Apps** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop down select **Device Management**.
6. Add the details created during step one.
7. Click **Save**.
8. The app is visible on the **Integrated Apps** table with a **Connected** status.
