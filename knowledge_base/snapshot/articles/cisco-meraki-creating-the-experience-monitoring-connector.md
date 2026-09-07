---
title: "Cisco Meraki: Creating the Experience Monitoring Connector"
slug: "cisco-meraki-creating-the-experience-monitoring-connector"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/cisco-meraki-creating-the-experience-monitoring-connector"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cisco Meraki: Creating the Experience Monitoring Connector

This article explains how to configure the Experience Monitoring integration for Cisco Meraki.

## Overview

The Cisco Meraki integration provides bi-directional communication utilized for Experience Monitoring. This enables seamless visibility into network and device performance across your environment. This connector brings events, telemetry, and IoT inventory data directly into the Cato platform, streamlining troubleshooting and device management. Gain faster insights, reduce mean time to resolution, and improve digital experience for all connected users and devices.

To configure this integration, you need to:

- Configure the integration in your Meraki Dashboard
- Create the API connector in the Cato Management Application (CMA)

## Configuring the Cisco Meraki Integration

To create the Cisco Meraki integration, create the required information in the Meraki Dashboard.

### Prerequisites

- A Cisco Meraki Dashboard account with
  - Read-only access at the organization level
  - API access enabled (you can enable is by navigating to **Organization > Settings > Dashboard API access**)

### Step 1: Configuring the Integration in the Meraki Dashboard

In the Meraki Dashboard, create an API key to be entered into the CMA.

**To configure the Meraki Integration:**

1. Log in to the [Meraki Dashboard](https://dashboard.meraki.com/).
2. Navigate to **Organization > Settings**.
3. Under the **Dashboard API access** section, enable **Enable access to the Cisco Meraki Dashboard API**.
4. Click **Save**.
5. Navigate to **Organization > API & Webhooks**.
6. On the **API keys and access tab**, click **Generate new API key**.
7. Copy and save the API key so it can be entered into the CMA.

**Note:** The API key inherits the permissions of the admin account that generated it.

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
