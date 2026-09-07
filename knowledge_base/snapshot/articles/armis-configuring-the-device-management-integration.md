---
title: "Armis: Configuring the Device Management Integration"
slug: "armis-configuring-the-device-management-integration"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/armis-configuring-the-device-management-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Armis: Configuring the Device Management Integration

This article explains how to configure the Device Inventory integration for Armis.

## Overview

To enhance device intelligence, you can integrate Armis device data with Cato’s device discovery for the IoT/OT Security service. Data from both platforms is merged, creating unified device profiles that enhance visibility and classification.

Armis is an agentless security platform that provides comprehensive visibility and intelligence about all connected devices, managed, unmanaged, IoT, and OT across your environment. Integrating Armis data enhances device inventory accuracy by continuously identifying and classifying assets, helping security teams maintain a real-time, unified view of their network.

The combined view appears on the **Home > Devices > Inventory** tab and helps improve identification of both managed and unmanaged assets. With more accurate and complete device data, you can make better-informed security decisions across your network. For more information on Device Inventory, see [What is Device Inventory?](/v1/docs/what-is-device-inventory).

To configure the Device Management integration, you need to:

- Configure the integration within Armis
- Create the API connector in the CMA

### Prerequisites

- To add a connector, you must have editor permission for **Integrations** (in the **Resources** section). For more information, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).

## Configuring the Armis Integration

To configure the Armis integration, create an API Secret Key.

### Step 1: Configure the Integration in the Armis Management Console

In the Armis management console, create an API Secret Key.

**To configure the Armis integration:**

1. Login into your Armis management console (`https://&lt;tenant&gt;.armis.com`)

**Note:** You must have permissions to manage APIs.
2. Navigate to `https://&lt;tenant&gt;.armis.com/settings/api-management`.
3. Click **Create**.
4. Copy and save the API Secret Key so it can be added in the CMA.

#### Step 2: Create the API Connector in the CMA

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
