---
title: "Working with the Site Preview Pane"
slug: "working-with-the-site-preview-pane"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/working-with-the-site-preview-pane"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with the Site Preview Pane

This article explains the fields and statuses available in the Site Preview pane.

## Understanding the Site Preview Pane

When you click on a site in the Topology page, a panel opens and shows details about the site. The information includes the site status, sockets, which ports are available and what are their statues, and more.

![site-preview-pane.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275685913885.png)

- ![configuration_blue.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275669441821.png) - Configure. Drop-down menu with shortcut to Site Configuration pages for this site.
- ![monitoring_blue.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275645908637.png) - Monitor. Drop-down menu with shortcut to Site Monitoring pages for this site.
- **Site Type** - Site connects to the Cato Cloud using a Socket, IPsec, vSocket, and so on.
- **Country** - Setting where the site is physically located (or licensed).
- **Connected PoP** - PoP in the Cato Cloud that the site is connected to.
- **Site Overview**
  - **Site Status** - If the site is **Connected** or **Disconnected** to the Cato Cloud.

In addition, you can hover over the Socket Status to see the Socket's uptime (supported for Socket v21 and later). This can help you understand if a Site Down issue is related to power outages.

![Socket-physical-status.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275686141213.png)
  - **Last Connected** - The time stamp when the site connected to the PoP .
  - **HA Status** - For Socket HA configurations, shows **Ready** or **Not-Ready**. Use the tooltip to show the details of the HA status.
- **Site Sockets** (for Socket and vSocket site types).
  - **Primary** and **Secondary** - Links for the primary and secondary (for HA) Sockets.

The warning icon ![warning.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275638319645.png) for the Secondary Socket indicates that one of the ports isn't connected.

Click a link to show the following details for the link:
  - **Socket Ver** - Cato firmware version installed on the Socket
  - **Socket WebUI** - Click to open a new browser tab and log in to the Socket WebUI.
  - **Destination** - Cato, LAN, Alt-WAN, and so on.
  - **ISP** - Name of the ISP the link is using.
  - **ISP IP** - IP address the ISP allocates to the link.
  - **Bandwidth** - Configured upstream and downstream bandwidth for the link.
  - **Status** - If the link is **Up & Connected** to the Cato Cloud, **Up & Disconnected** the link is up, but the Socket is disconnected to the Cato Cloud, or the link is **Down & Disconnected**. For more information, see [Socket Port Statuses](/v1/docs/working-with-the-site-preview-pane#socket-port-statuses), below.
  - **Distance (ms)** - Round trip time between the site and the PoP
  - **Recent Connections** - Click **View Log** to open the [Recent Connections data](/v1/docs/monitoring-a-site-with-a-snapshot) in a pop-up window
- **IPsec Details** (for IPsec IKEv1 and IKEv2 sites)
  - **PoP** - PoP in the Cato Cloud that the site is connected to
  - **Site IP** - Public IP address of the site
  - **ISP** - Name of the ISP for the active link
  - **Distance (ms)** - Round trip time between the site and the PoP
  - **Recent Connections** - Click **View Log** to open the [Recent Connections data](/v1/docs/monitoring-a-site-with-a-snapshot) in a pop-up window

## Socket Port Statuses

> [!NOTE]
> Note:
> 
> This is an Early Availability (EA) feature that is only available for limited release. For more information, contact your Cato Networks representative or send an email to [ea@catonetworks.com](mailto:ea@catonetworks.com).

You can view the status for each port in the Socket page for a site. In addition, you can hover over each port and get more detailed information about the status. For example, if a port is showing a status of **Up and Disconnected**, you can hover and see if the problem is that the tunnel is down or an IP address has not been allocated.

### Port Statuses

Each port provides the following information:

- Color indicator for the port status:

![socket_status.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275638381853.png)
  - Green - Port status is Up and Connected
  - Yellow - Port status is Up and Disconnected
  - Red - Port status is Down
- Additional information about the status when you hover over the port:

| Item | Description |
| --- | --- |
| Port is (not) connected | Indicates if there is a physical connection to the port |
| IP is (not) allocated | Indicates if the WAN interface has an IP address **Note:** Supported from Socket v21 and later. |
| Internet is (not) connected | Indicates if there is a connection to the Internet **Note:** Supported from Socket v21 and later. |
| Tunnel is (not) connected | Indicates if a connection has been established with the Cato Cloud |

For X1600 LTE Sockets, the following additional statuses are available for each SIM:

| Item | Description |
| --- | --- |
| Signal Strength | Indicates the quality of the signal |
| APN | Indicates the name and connection status to the cellular provider |
| Roaming Enabled | Indicates if the roaming function is enabled |
| SIM is (not) Detected | Indicates if a connection has been established with the Cato Cloud |
