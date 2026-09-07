---
title: "Monitoring Users with a Snapshot"
slug: "monitoring-users-with-a-snapshot"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/monitoring-users-with-a-snapshot"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring Users with a Snapshot

The User Snapshot screen shows real-time ISP data for a specific SDP user.

## Showing the User Snapshot Screen

The User Snapshot screen shows the IP addresses for each end of the encrypted tunnel between the Client and the PoP in the Cato Cloud. It also shows the amount of time the Client is connected.

**To show the User Snapshot screen:**

1. From the navigation menu, click **Access > Users** and select a user.
2. From the navigation menu, select **User Monitoring > Snapshot**.

The Snapshot shows you the connection status for the user, and if connected, for how long and to which PoP.

## Explanation of the Device Details Fields

The Device Details section shows information about the user's device that is connected to the network.

![User_Snapshot_-_Device_Details.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218298907933.png)

- **OS** - The OS and version of the device that the Client is installed on
- **Client** - The Client version
- **Remote IP** - The IP address of the Client
- **Internal IP** - The IP address of the PoP that the Client is connected to

## Explanation of Recent Connections Fields

The Recent Connections section shows information about the user's most recent connections between the Client and the PoP in the Cato Cloud.

- **Remote IP** - The IP address of the Client
- **From** - IP address of the user that's connected to the PoP
- **PoP** - Physical location of the PoP in the Cato Cloud
- **Duration** - Amount of time that the user is continuously connected to this PoP
- **Last Update** - Amount of time since the user received an update from the PoP
