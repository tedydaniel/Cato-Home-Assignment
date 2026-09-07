---
title: "Creating Physical App Connectors"
slug: "creating-physical-app-connectors"
updated: 2026-08-23T13:51:30Z
published: 2026-08-23T13:51:30Z
canonical: "knowledge.catonetworks.com/creating-physical-app-connectors"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Physical App Connectors

> [!NOTE]
> Note:
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

## Overview

You can deploy a physical App Connector to provide secure access to private applications in a physical data center or branch environment. The physical App Connector establishes an outbound connection to Cato, and once connected, you assign it in the CMA and associate it with the relevant app connector group.

Unlike a virtual App Connector, a physical App Connector does not require a serial number to be entered during a cloud deployment template. Instead, after the device is connected to the network and communicates with Cato, the CMA detects the new device and prompts you to identify and assign it.

### Supported Socket Models

- All x1500 Socket models support deploying a physical App Connector Other Socket models (such as X1600 and X1700) are not currently supported for physical App Connectors

## Understanding the Physical App Connector Workflow

The following is a high-level workflow for deploying a physical app connector:

- You create the App Connector object in the CMA
- Physically connect the device to the network
- Assign the device to a connector
- Assign apps to the connector

## Create a Physical App Connector

When you create an App Connector, you can choose the behavior for connecting to a preferred PoP in the Cato Cloud:

- Disabled - the App Connector automatically connects to the best available PoP (default)
- Enabled - Select the PoPs to which the connector attempts to connect to
  - Restrict an App Connector to only connect to the Preferred PoP Locations that you configure. In this case, the connector doesn't connect to a non-preferred PoP location despite any connectivity or performance issues that it is experiencing. When you use this option, you must define a primary and secondary PoP location for the App Connector.

Once the App Connector is created in the CMA, copy the serial number, as you will need to provide it when deploying the App Connector in your cloud environment.

![physical-app-connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35809709319581.png)

**To create a physical app connector**

1. From the navigation menu, click **Access > App Connector**, and then click **New**.
2. Enter the information in the **General** section, such as **Connector** **Name** and **Country**.
3. Under **Type**, click **Physical**.
4. In the **Connector Group** section, select an existing App Connector group from the list or enter a name to create a new group.
5. Under **Preferred PoPs**, select the behavior
  1. **Disabled** - the App Connector tries to connect to the best available PoP
  2. **Enabled** - Select the **Primary** and **Secondary** PoP locations that the connector tries to connect to
  3. **Enabled** and **Only connect to the preferred PoPs** - Only connect to the **Primary** or **Secondary** PoP location
6. Click **Apply**.

## Connect your Device to the Network

For information about connecting your device to the network, refer to the relevant [deployment guides](/v1/docs/cato-socket-deployment-guides-and-data-sheets).

## Assign the Device to a Connector

Once the device connects to the Cato Cloud, you can assign it to the app connector you created [above](/v1/docs/creating-physical-app-connectors#create-a-physical-app-connector) from the Notifications panel.

![assign-app-connector.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35809671573533.png)

**To assign a device to a connector**

1. Click the notification icon ![notification.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35809663444253.png).
2. In the **Notifications** panel, click **Activate New Socket**.
3. Under **Assign to**, click **App Connector**.
4. Under **Site**, select the app connector you created [above](/v1/docs/creating-physical-app-connectors#create-a-physical-app-connector).
5. Click **Ok**.

## Assign Apps to the Connector

You assign apps to your connectors either from the Private Apps page or from App Connectors page, using the **Assign App** link.
