---
title: "Zoom: Configuring the Experience Monitoring UCaaS Connectors"
slug: "zoom-configuring-the-experience-monitoring-ucaas-connectors"
updated: 2026-06-22T09:24:33Z
published: 2026-06-22T09:24:33Z
canonical: "knowledge.catonetworks.com/zoom-configuring-the-experience-monitoring-ucaas-connectors"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Zoom: Configuring the Experience Monitoring UCaaS Connectors

This article explains how to configure the Experience Monitoring Integration for Zoom.

## Overview

Experience Monitoring provides enhanced context, such as packet loss or tunnel age, to give you the information you need to determine if the issues are related to your ISP, the Cato Cloud, or other sources.

You can also configure a connector with UCaaS applications to display application-specific metrics in the CMA to monitor the user experience when using the application.

To configure the Experience Monitoring UCaaS Connector, you need to:

1. Configure the integration within the SaaS application
2. Create the API connector in the CMA

A DEM license is required to display Application-Specific Metrics. For more about purchasing a DEM license, please contact your Cato representative.

## Configuring the Zoom Experience Monitoring Integration

To configure the integration, build an app.

### Prerequisites

- You must have a Zoom Business plan or a higher plan that includes the Zoom Quality of Service Subscription (QSS)
- These Scopes (Permission) are provided:
  - dashboard:read:list_meetings:admin - View meetings metrics
  - dashboard:read:list_meeting_participants_qos:admin - View meeting participants' quality of service
  - user:read:user:admin - View a user
  - dashboard_meetings:read:admin - Enables viewing Zoom disconnection events
- Zoom users must have individual accounts (for example, not a generic business account)

### Step 1: Configure the Integration in the Zoom App Marketplace

In the Zoom App Marketplace, create the required information to be added into the CMA.

**To configure the Zoom integration:**

1. Log in to the [Zoom App Marketplace](https://marketplace.zoom.us/).
2. Click **Develop > Build App**.
3. Select **Server to Server OAuth App** and click **Create**.

![Zoom.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30431426384669(1).png)
4. Choose a name for the app.
5. On the **App Credentials** page, copy and save the **Account ID**, **Client ID**, and **Client Secret**, so they can be added into the CMA.
6. On the **Information** page, add the required information.
7. On the **Scopes** page, click **Add Scopes** and add these scopes:
  - dashboard:read:list_meetings:admin - View meetings metrics
  - dashboard:read:list_meeting_participants_qos:admin - View meeting participants' quality of service
  - user:read:user:admin - View a user
  - dashboard_meetings:read:admin - Enables viewing Zoom disconnection events
8. On the **Activation** page, click **Activate your app**.

#### Step 2: Create the API Connector in the CMA

After you have set up an integration with the required application, add the details in the CMA.

**To add create the API connector in the CMA:**

1. From the navigation menu, click **Resources > Integrations**.
2. Click the **Integrated Apps** tab.
3. Click **New**. The **New Integration** panel opens.
4. Select the **SaaS Application** you want to add.
5. In the **Capability** drop down select **Experience Monitoring**.
6. Add the details created during step one.
7. Click **Save**.

### Sources

- Meetings metrics: Queries a list of all meetings in a specific time frame
- Participants QoS: Queries the Quality of Service information of each user in each meeting
- Users: Collects information about the users that participated in the meetings

### Known Limitations

- All meetings are fetched
