---
title: "Working with App Connectors"
slug: "working-with-app-connectors"
updated: 2026-07-09T12:59:19Z
published: 2026-07-09T12:59:19Z
canonical: "knowledge.catonetworks.com/working-with-app-connectors"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with App Connectors

> [!NOTE]
> Note:
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

App Connectors provide secure connectivity between Cato and private applications hosted in data centers or cloud environments. You use the App Connectors page to view and manage the connectors that expose private applications to authorized users, as well as assign apps to the connectors in your account.

The page provides visibility into the version and connectivity status of each connector, and serves as the starting point for creating and managing App Connectors. From this page, you can create new connectors, assign private applications to them, and review their connection to the Cato Cloud.

![app-connectors-main.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35809663306013(2).png)

## Understanding the App Connectors Overview

The App Connectors Overview provides high-level information about all of the connectors in your account, and includes the following widgets:

- Connectivity Status – the total number of connectors and their statuses (connected or, disconnected, degraded, and disabled)
- Model – shows the distribution of connector types in your account (e.g., X1500, AWS, etc.)
- Socket versions – shows the distribution of the Socket versions running on the app connectors. This widget presents information for both physical and virtual app connectors
- App Connector Groups - the total number of app connector groups and the number of apps assigned to each group

## Reviewing App Connector Data

You can use the App Connector page to manage the app connectors in your account, and it summarizes a variety of real-time information about the connectors. In addition, you can add connectors and edit or delete existing connectors.

These are the default columns that are shown:

- Name - name of the connector
- Connectivity Status - Connected or Disconnected
- Group - to which app connector group the connector belongs
- Model - the model of the connector, e.g., GCP or X1500.
- Serial Number - the serial number of the connector. For virtual connectors, this number must be provided when configuring the connector in the relevant cloud provider.
- Country - in which country the connector resides.
- Connected PoP - shows the name of the PoP to which it's connected. If the connector is disconnected, the field will show the name of the last connected PoP. If the connector was never connected before to a PoP, the field remains empty
- Private Apps - names of the apps accessible through this connector

You can also use the **Group by** drop-down to see which connectors are in which Connector Group and which apps are covered by the different groups.

## Limitations

- QoS is not applied to app connector traffic. You can't define a bandwidth profile and Network Rules for the traffic, and it is assigned the lowest network priority.
- For Socket v26, currently, apps not located/available in the LAN subnet are not supported via App Connector.
