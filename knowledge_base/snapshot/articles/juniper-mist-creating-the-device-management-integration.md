---
title: "Juniper Mist: Creating the Device Management Integration"
slug: "juniper-mist-creating-the-device-management-integration"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/juniper-mist-creating-the-device-management-integration"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Juniper Mist: Creating the Device Management Integration

This article explains how to configure the Device Inventory integration for Juniper Mist.

## Overview

Cato DEM integrates with Juniper Mist providing bi-directional communication with the Mist Controller, utilized for Device Security and Experience Monitoring. This enables seamless visibility into network and device performance across your environment. This connector brings Mist events, telemetry, and IoT inventory data directly into the Cato platform, streamlining troubleshooting and device management. Gain faster insights, reduce mean time to resolution, and improve digital experience for all connected users and devices.

To configure the integration, you need to:

- Configure the integration in Mist Cloud
- Create the API connector in the CMA

## Configuring the Juniper Mist Integration

To create the Juniper Mist integration, create the required information in Mist Cloud portal.

### Prerequisites

- Your account has permissions to manage API tokens

### Step 1: Configure the Integration in Mist Cloud

In Mist Cloud, create an API Token to enter into the CMA.

**To configure the Juniper Mist integration:**

1. Sign in to the [Mist Cloud](https://manage.mist.com/) portal.
2. Click on the Account icon and select **My Account**.

Note: For organization-level tokens, go to Organization > Admin > Settings.
3. In the **API Token** section, click **Create Token**.
4. Enter a name for the token and click **Generate**.
5. Copy and save the token so it can be entered into the CMA.
6. Click **Done**.

#### Additional Information

This information is also required to configure the Juniper Mist integration:

- API Base URL
- Organization ID

For more information, see the [Juniper documentation](https://www.juniper.net/documentation/us/en/software/mist/automation-integration/topics/topic-map/api-endpoint-url-global-regions.html)

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
