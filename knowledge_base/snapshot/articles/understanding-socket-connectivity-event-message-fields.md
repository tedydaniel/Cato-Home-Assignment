---
title: "Understanding Socket Connectivity Event Message Fields"
slug: "understanding-socket-connectivity-event-message-fields"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/understanding-socket-connectivity-event-message-fields"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding Socket Connectivity Event Message Fields

This article explains the cause for a specific Connectivity event message, and, when possible, how to remediate them.

## Overview

A Socket can have multiple tunnels to a PoP, and each tunnel can have one of two connectivity statuses, connected or disconnected. When a tunnel either disconnects or connects to the Cato PoP, a Connectivity event is generated. These often come in a pair of Disconnected and Connected events.

When the tunnel is disconnected for less than 2.5 minutes, a single Reconnected event is generated instead of the Disconnected (and Connected) events. For more information, see [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network) and [Explaining the Event Fields](/v1/docs/understanding-event-fields).

## Understanding Reconnected Events

Sometimes, Cato is able to identify the reason behind the Reconnected event. The reason is displayed in the event message field within the event to help you understand the root cause behind the event, and possibly remediate the issue to prevent it from happening again. This information is also available through the [accountSnapshot Cato API](https://api.catonetworks.com/documentation/#definition-AccountSnapshot), using the tunnelConnectionReason field.

The following table lists the event messages displayed within the Reconnected event Sub-Type, and their descriptions. The event code can be found at the end of each Event message.

> [!NOTE]
> Note:
> 
> If there are multiple occurrences of the same event, open a ticket with Customer Support to further investigate the issue.

| Event Code | Event Message | Description |
| --- | --- | --- |
| 1 | Reconnected to preferred PoP to optimize performance | When all active tunnels of a Socket site do not meet the connection SLA parameter, the tunnels are moved to the next best PoP. After the pre-configured interval (default is 60 minutes), the tunnels attempt to reconnect to the preferred PoP. This is the PoP that is closest to the source and provides the best performance. |
| 2 | Reconnected due to an unknown reason | An error occurred in the Cato Cloud, which caused the Socket to reconnect to the PoP. |
| 3 | Performance issue detected, reconnected to a different service node in the Cato Cloud | A performance issue was detected. The site reconnected to a different service node in the Cato Cloud to improve performance. |
| 4 | Reconnected due to a PoP service node maintenance | Due to maintenance on the PoP service node, the Socket reconnected to the next best available service node. |
| 5 | Reconnected due to Socket restart | The Socket reconnected to the Cato Cloud due to a manual or automatic restart. |
| 7 | Reconnected to a different Cato Cloud service node due to an administrative change | The Socket reconnected to a different PoP service node due to a change in the Socket configuration. |
| 8 | Reconnected due to a PoP service node related issue | An error occurred in the PoP service node, which caused the Socket to reconnect to the PoP. |
| 9 | Reconnected after WAN port was physically disconnected | The Socket reconnected to the service node after the cable was temporarily disconnected on the WAN port. |
| 10 | Reconnected due to Socket Internet connectivity issue | The Socket reconnected to the service node after an Internet connectivity issue was detected. |
| 11 | Reconnected following a user-initiated reconnection action | The Socket reconnected after a user-triggered reconnect. |
| 12 | Reconnected due to a PoP service node related issue | The Socket reconnected due to a temporary issue with the PoP. |
| 14 | Reconnected due to Socket connectivity issue to the Cato Cloud | The Socket reconnected to the service node because of WAN connectivity problems. |
| 15 | Reconnected due to Socket connectivity issue to the Cato Cloud | The Socket reconnected to the service node after a temporary connectivity issue to the Cato Cloud. |
| 16 | Reconnected due to a PoP service node firmware update | Due to maintenance on the PoP service node, the Socket reconnected to the next best available service node. |
| 17 | Secondary Socket reconnected to same PoP service node as the primary Socket | The secondary HA Socket reconnected to the same service node as the primary Socket. |
| 18 | Performance issue detected, reconnected to different service node in the Cato Cloud | All active tunnels of a Socket site didn’t meet the connectivity SLA. The Socket reconnected to a different service node PoP to resolve the performance issue. |
| 19 | Performance issue detected, reconnected to different service node in the Cato Cloud | A performance issue was detected. The site reconnected to a different service node in the Cato Cloud to improve performance. |
| 20 | Site reconnected to different service node in the Cato Cloud | The site reconnected to a different service node in the Cato Cloud to improve performance. |
