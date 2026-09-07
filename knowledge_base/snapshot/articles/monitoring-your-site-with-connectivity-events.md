---
title: "Monitoring Your Site with Connectivity Events"
slug: "monitoring-your-site-with-connectivity-events"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/monitoring-your-site-with-connectivity-events"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitoring Your Site with Connectivity Events

This article discusses the different connectivity events in Cato, how they are triggered, and what you can do with the information in the events.

## Overview of Connectivity Events

The Cato Management Application (CMA) creates events for different things that happen in the Cato platform. Among the different event types are Connectivity events. Whenever there is a change in the connectivity status, an event is generated with the information about the change, the link or site that was affected, and more.

### Example Diagram of a Connectivity Event Caused by a Disconnect

In this example, one of the interfaces disconnects as shown in the following image:

![diagram.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30317776748317.png)

In this scenario, a Disconnected event for WAN1 would be created. If you have Link Health Rules configured to send a communication when a Disconnected event occurs, an alert would be sent according to the rule settings, such as an email or webhook. For more information, see [Enabling Connectivity Alerts](/v1/docs/monitoring-your-site-with-connectivity-events#enabling-connectivity-alerts).

### Sites with Multiple Links

Active links are links configured with "Active" precedence, and Passive links are links configured with precedence of "passive" or "last resort". For more information, see [Part 1: The Socket Interfaces and Precedence](/v1/docs/part-1-the-socket-interfaces-and-precedence).

### Overview of Connectivity Event Types

The following list describes the types of connectivity events for Socket sites:

- **Connected**: This event is generated after a tunnel is connected to the PoP for 30 seconds, and the link role is Active (precedence 1). If the Socket connects with 2 different interfaces, 2 Connected alerts are generated. If the Socket connects to a different PoP during this time frame, it will generate a **Changed PoP** event instead of a **Connected** event. If the Socket connects within 2.5 minutes of a disconnection, it will generate a **Reconnected** event instead of a **Connected** event.
- **Disconnected**: Generated if the link role is Active (precedence 1), and the tunnel to the PoP is disconnected for more than 2 ½ minutes.
- **Changed PoP**: Generated when the PoP to which a site was connected changes.
- **Reconnected**: Generated when the Active tunnel changes from disconnect to connect. This will only be generated after being connected for 30 seconds. Reconnect events do not send email notifications based on [Link Health rules](/v1/docs/working-with-link-health-rules).
- **Passive Reconnect**: Generated when the Passive or Last Resort link changes from disconnect to connect. This will only be generated after being connected for 30 seconds.
- **Failover**: Generated when there is a failover between two WAN links. In case the active link is down, there is a failover to the passive link and the passive link becomes active.

This alert is only relevant for Socket v8.0 and earlier.
- **Socket Failover**: Generated when the secondary Socket's role changes to primary. For more details on Socket failover, see [What is Socket HA](/v1/docs/what-is-socket-ha).
- **Passive Disconnected**: Generated when the WAN link role is either Passive (precedence 2) or Last Resort (precedence 3), and the link has been disconnected for more than 2.5 minutes. It is relevant for deployments with at least 2 interfaces with different precedence.
- **Passive Connected**: Generated when the WAN link role is either Passive (precedence 2) or Last Resort (precedence 3), and has just connected for at least 30 seconds. It is relevant for deployments with at least 2 interfaces with different precedence.
- **LAN Port DIsconnected**: Generated when the port is down for 5 seconds.
- **LAN Port Connected**: Generated when the port is up for 5 seconds after a disconnected event.
- **Alt. WAN Disconnected**: Generated when the Alt. WAN link is down for 5 seconds.
- **Alt. WAN Connected**: Generated when the Alt. WAN link is up for 5 seconds after a disconnected event.
- **HA Not Ready**: Generated in the following scenarios:
  - When there is a failover in an HA configuration and the original secondary Socket reports as primary, and the original primary Socket is disconnected
  - When both Sockets in an HA configuration report as the primary Socket for 30 seconds
- **HA Ready**: Generated when one Socket in an HA configuration reports as the primary Socket, and the other reports as secondary, for 30 seconds following an HA Not Ready event.

### Enabling Connectivity Alerts

We recommend that you create a Connectivity Health Rule, In the Cato Management Application so that you start getting the connectivity alerts.

For more about creating Health Rules, see [Working with Link Health Rules](/v1/docs/working-with-link-health-rules).

Whenever there is a change in the connectivity status, an event is generated and if it matches the Health Rule, an alert is sent to the recipients.

For more information about notifications, see the relevant article for Subscription Groups, Mailing Lists, and Alert Integrations in the [Alerts](/v1/docs/notifications) section.

You can see the events in the CMA in **Home > Events**.

### Example of a Connectivity Event

The following example shows a Passive Connected event that indicates that the Secondary or Last Resort link is connected.

![connectivity-event_passiveConnected.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30317736824989.png)

This indicates that if the Active link disconnects, the secondary link will be available to maintain connectivity.
