---
title: "Monitoring a Site with a Snapshot"
slug: "monitoring-a-site-with-a-snapshot"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/monitoring-a-site-with-a-snapshot"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring a Site with a Snapshot

The **Snapshot** screen shows data for the connection between the site and the Cato Cloud.

## Showing the Snapshot Screen

**To show the metrics for a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Monitoring > Snapshot**.

### Explanation of the Device Overview fields

This example and the table that follows explain the fields in the **Snapshot** window:

![Site_Snapshot_Callouts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247957278109.png)

| Item | Name | Description |
| --- | --- | --- |
| 1 | Snapshot site | Select the site that is showing metrics data |
| 2 | Device Overview | Shows information about the Sockets for the site |
| 3 | Socket data | Shows data about the Socket and ISPs for the Socket |
| 4 | Socket WebUI for Secondary Socket | Remote access to the Socket WebUI for the Secondary Socket Not shown for IPsec sites |
| 5 | Socket WebUI for Primary Socket | Remote access to the Socket WebUI for the Primary Socket Not shown for IPsec sites |
| 6 | Link State | Expand this section for data about the LAN links Not shown for IPsec sites |
| 7 | Recent Connections | Expand this section for historical data about the site connection to the Cato Cloud |

### Explanation of Snapshot fields

- **Primary** and **Secondary** - Primary or secondary Socket for this site
- **Interface** - ISP information for the link
- **Remote IP** - IP address of the PoP that the link is connected to
- **PoP** - Physical location for the Cato PoP
- **Connected** - Amount of time that the site is continuously connected to this PoP
  - Shows the reason that the Socket initiated the connection to this PoP
- **RTT** - round trip time between the site and the PoP

### Explanation of Link State Fields

The **Link State** fields show the following data about the Socket links:

- **Primary** and **Secondary** - Primary or secondary Socket for this site
- **Link** - port on the Socket
- **Status** - shows if the link is **Up** or **Down**
- **Media Connected** - **Yes** indicates that the cable is connected to the port
- **Link Speed** - Auto-negotiation, or the maximum speed configured for the link in the Socket WebUI
- **Duplex** - Auto-negotiation, or the duplex configured for the link in the Socket WebUI

### Explanation of Recent Connection Fields

- **Remote IP** - IP address of the PoP that the link is connected to
- **From** - Link that connected to the PoP
- **PoP** - Physical location for the Cato PoP
- **Duration** - Amount of time that the site is continuously connected to this PoP
- **Last Update** - Amount of time since the Socket received an update from the PoP
