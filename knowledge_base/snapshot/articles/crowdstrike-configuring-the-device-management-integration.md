---
title: "CrowdStrike: Configuring the Device Management Integration"
slug: "crowdstrike-configuring-the-device-management-integration"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/crowdstrike-configuring-the-device-management-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CrowdStrike: Configuring the Device Management Integration

This article explains how to configure the Device Inventory integration for CrowdStrike

## Overview

To enhance device intelligence, you can integrate CrowdStrike device data with Cato's device discovery for the IoT/OT Security service. Data from both platforms is merged, creating unified device profiles that enhance visibility and classification.

The combined view appears on the **Home > Devices > Inventory** tab and helps improve identification of both managed and unmanaged assets. With more accurate and complete device data, you can make better-informed security decisions across your network. For more information on Device Inventory, see [What is Device Inventory?](/v1/docs/what-is-device-inventory).

To configure the Device Management integration, you need to:

1. Create the API Client in the Falcon Crowdstrike platform
2. Create the API connector in the CMA

An IoT/OT Security license is required for this feature.

## Configuring the CrowdStrike Connector

In the Falcon CrowdStrike platform, create the API Client and enter it into the CMA.

### Prerequisites

- You must have a CrowdStrike Falcon Discover license
- To add a connector, you must have editor permission for **Integrations** (in the **Resources** section). For more information, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).

### Step 1: Create the API Client in the Falcon CrowdStrike Platform

In the Falcon CrowdStrike platform, create the API Client.

**To create the API Client:**

1. In your Falcon CrowdStrike platform, navigate to **Support and resources > API clients and keys**.

![CS_nav.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30344535059229.png)
2. Click **Create API client**.
3. Add a **Client name** and **Description**, and **Read** access for these scopes:

**Note:** You must have a CrowdStrike Falcon Discover license
  - Assets![CS__1_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33409916312861.png)
4. Save the **Client ID**, **Secret**, and **Base URL** so they can be added in the CMA.

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
