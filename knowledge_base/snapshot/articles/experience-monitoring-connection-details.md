---
title: "Experience Monitoring Connection Details"
slug: "experience-monitoring-connection-details"
updated: 2026-07-28T07:45:31Z
published: 2026-07-28T07:45:31Z
canonical: "knowledge.catonetworks.com/experience-monitoring-connection-details"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Experience Monitoring Connection Details

This article explains how accounts with a DEM license can use Connection Details to better understand digital experience for their sites and users.

## Overview

Experience Monitoring lets you track the digital experience of your users as they interact with their applications and services. You receive an overall Application Experience score for your experience, which can help you identify problems or trends in your network. For more information, see [What is Cato Experience Monitoring](/v1/docs/what-is-cato-experience-monitoring).

![DEM-overall.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275701191837.png)

In addition, for accounts with a DEM license, Cato provides tools that give you additional insight into the user and site experience. Connection Details helps you break down the network path into logical nodes and highlight possible problem indicators.

When you drill down into the Users (remote or behind a site), the User Experience graph shows you when the user was connected (a solid line) and when the user was not connected (a dotted line).

- When you click on an area of the graph in which the user was connected, the Connection Details section below provides you with a visualized breakdown of the different points of the flows for a site and user.
- Depending on the type of site, and the location of the user, you see different nodes. For example, for a user working remotely, you can view information about the user's device, Wi-Fi, LAN gateway, tunnel, and application experience.

> [!NOTE]
> Note:
> 
> To see the User Device, Wi-Fi, and LAN Gateway nodes, the user's device must be connected to the Cato Client both when working remotely and behind a Socket.

![path-analysis-user.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275691394717.png)

Whereas for a host without the Cato Client you will see information only for the Internet, tunnel and application.

![path-analysis-socket.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275692330397.png)

For information about the different Experience Monitoring widgets, see [Using the Experience Monitoring Page](/v1/docs/using-the-experience-monitoring-page).

### Use Case

A user from ABC company calls the IT helpdesk complaining that the company's messaging system is responding poorly.

When looking at the overall Application Score for the messaging system, the helpdesk engineer doesn't see any global issue with the application. However, when looking at the User Connection Details, they see that the Wi-Fi node is colored yellow.

![path-analysis-usecase.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275674468765.png)

Hovering over the Device node, they see that while the experience is Fair, the Signal Strength is very weak. This helps the helpdesk engineer understand that the problem probably lies in a local problem in the user's home Wi-Fi setup and not a problem in the network or messaging application.

> [!NOTE]
> Notes:
> 
> - Scores are based on successful TCP flows. Blocked traffic is not taken into account.
> - Traffic sent using the Bypass feature does not provide HTTP/s Latency and Error Rate metrics

## Node Scoring

Each node is scored for its individual experience based on metrics for that node. When looking at the Connection Details you can immediately get an indication of the score for each node based on its color (green, yellow, and red). Each node is scored individually and doesn't affect the score of other nodes.

In addition, when you hover over a node, you can view the average metrics for that node. To see the full metrics, click on the node to view the relevant widgets.

The following table provides information about which nodes are available, the metrics used to calculate the score, and how the score is calculated. For information about Application Experience Scoring, see [What is Cato Experience Monitoring](/v1/docs/what-is-cato-experience-monitoring).

> [!NOTE]
> Notes:
> 
> - Device, Wi-Fi, and LAN Gateway data is supported for Windows Client v5.11 and macOS Client v.5.7
> - The Cato Client uses Windows location services to identify various items on the network, for example, the WiFi network name. If you do not want to provide Cato with this information, change the settings for the location services using ​​[these​​ instructions](https://support.microsoft.com/en-us/windows/windows-location-service-and-privacy-3a8eee0a-5b0b-dc07-eede-2a5ca1c49088).

Depending on the connection type, you will see different nodes on the Connection Details.

| Node | Metrics | How it's scored | Connection Type |
| --- | --- | --- | --- |
| Client Device | The Client Device score is based on the following metrics, as shown in the widgets: - CPU Score - Good - CPU in use is less than 70% - Fair - CPU in use is between 70-90% - Poor - CPU in use is greater than 90% - Memory Score - Good - Memory used is below 60% - Fair - Memory used is between 60-80% - Poor - Memory used is greater than 80% | The score displayed for the node is based on the poorest result between the two metrics. For example, if the CPU Score is Good, but the Memory Score is Fair, the node score is Fair. | - Remote User - User behind Socket site using Cato Client - User behind an IPsec site using Cato Client - User behind Cloud Interconnect site using Cato Client |
| Wi-Fi | The Wi-Fi node score is calculated based on the Signal Strength metric, as shown in the widgets. - Good - signal strength -67 dBm or higher - Fair - signal strength between -67 dBm and -80 dBm - Poor - signal strength -80 dBm or lower | The score displayed for the node is based on the score for the Signal Strength metric | - Remote User - User behind Socket site using Cato Client - User behind an IPsec site using Cato Client - User behind Cloud Interconnect site using Cato Client |
| LAN Gateway | The score for the LAN Gateway is based on the following metrics, as shown in the widgets: - LAN Gateway Packet Loss - Good - less than 1% packet loss. - Fair - between 1-5% packet loss. - Poor - more than 5% packet loss. - LAN Gateway Distance - Good - below 10 ms. - Fair - between 10-50 ms. - Poor - exceeding 50 ms | The score displayed for the node is based on the poorest result between the two metrics. For example, if LAN Gateway Distance is Good and LAN Gateway Packet Loss is Poor, the node score is Poor. | - Remote User - User behind Socket site using Cato Client - User behind an IPsec site using Cato Client - User behind Cloud Interconnect site using Cato Client |
| Last Mile | The score for the Last Mile node is based on the following metrics, as shown in the widgets: - Tunnel Upstream Packet Loss - Good - less than 1% packet loss. - Fair - between 1-5% packet loss. - Poor - more than 5% packet loss. - Tunnel Downstream Packet Loss - Good - less than 1% packet loss. - Fair - between 1-5% packet loss. - Poor - more than 5% packet loss. - Tunnel Distance - Good - below 20 ms. - Fair - between 20-100 ms. - Poor - exceeding 100 ms In addition, there is also a Tunnel Age widget that is not calculated in the score. | The score displayed for the node is based on the poorest result between the two metrics. For example, if the Tunnel Packet Loss is Good, and Tunnel Distance is Poor, the node score is Poor. | - Remote User - Socket site - IPsec site - Host behind Socket site not using Cato Client - Host behind an IPsec site not using Cato Client - User behind Socket site using Cato Client - User behind IPsec site using Cato Client |
| Application | The [application score](/v1/docs/what-is-cato-experience-monitoring#application-experience-scoring) is based on the current application score and any applied filters. |  | All connection types |
| Socket | The Socket performance score is based on the average Socket CPU usage (CPU Load) for the site over the configured time range. - CPU Load - Good - CPU in use is less than 70% - Fair - CPU in use is between 70-90% - Poor - CPU in use is greater than 90% | The score is calculated based on the poorest-performing core of the site's primary Socket. | - Socket site - Host behind Socket site not using Cato Client - Host behind an IPsec site not using Cato Client |
