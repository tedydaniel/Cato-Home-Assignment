---
title: "Claroty: Configuring the Device Management Integration"
slug: "claroty-configuring-the-device-management-integration"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/claroty-configuring-the-device-management-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Claroty: Configuring the Device Management Integration

This article explains how to configure the Device Inventory integration for Claroty.

## Overview

To enhance device intelligence, you can integrate Claroty device data with Cato’s device discovery for the IoT/OT Security service. Data from both platforms is merged, creating unified device profiles that enhance visibility and classification.

The combined view appears on the **Home > Devices > Inventory** tab and helps improve identification of both managed and unmanaged assets. With more accurate and complete device data, you can make better-informed security decisions across your network. For more information on Device Inventory, see [What is Device Inventory?](/v1/docs/what-is-device-inventory).

To configure the Device Management integration, you need to:

- Configure the integration in Claroty
- Create the API connector in the CMA

An IoT/OT Security license is required for this feature.

### Prerequisites

- Claroty xDome license

## Configuring the Claroty Integration

To configure the Claroty integration, create the required configurations in the your Claroty xDome Console, then configure the connector within the CMA.

### Step 1: Configure the Integration in Claroty

To configure this integration, create an API Token and your Base URL.

**To configure the integration:**

1. In your Claroty xDome Console, navigate to **Settings > Admin Settings**.
2. Click **Add User** and select **API User**.
3. Enter a **Username** and **Title**.
4. In **Roles**, select **Read-Only-User**.
5. Click **Edit Site Permissions** to select sites to fetch data from.
6. Click **Create User**.
7. Click the **Generate Token** icon, select expiration, and click **Generate**.
8. Copy and save the token so it can be entered in the CMA.

**Note:** The token cannot be viewed again.
9. Identify your Base URL:
  - **US**: `https://api.claroty.com`
  - **EU**: `https://eu.api.claroty.com`

### Step 2: Create the API Connector in the CMA

After you have set up an integration, add the details in the CMA.

**To create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Configured Integrations** tab.
3. Click **New**.

The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop down select **Device Management**.
6. Add the details created during step one.
7. Click **Save**.
8. The app is visible on the **Integrated Apps** table with a **Connected** status.
