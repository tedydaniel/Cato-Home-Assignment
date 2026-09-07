---
title: "Implementing QoS using Microsoft Teams and Cato"
slug: "implementing-qos-using-microsoft-teams-and-cato"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/implementing-qos-using-microsoft-teams-and-cato"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Implementing QoS using Microsoft Teams and Cato

This article discusses how to implement Quality of Service (QoS) with the Microsoft Teams app and your Cato account.

## Issue

By default you can't distinguish between these traffic types in Microsoft Teams apps: voice, video, and screen share. Cato combines them into a single app, **Skype and MS Teams**, so it's not possible to define QoS for each traffic type separately.

## Solution

In Microsoft Teams, assign different DSCP markings for each traffic type and use a Group Policy Object (GPO) to make sure that the QoS policy is applied to all operating systems and Cato Clients.

The Cato Management Application has different applications for Skype and Teams based on the DSCP marking, for example: Skype Voice (DSCP = 46).

See Microsoft documentation for more information about [best practices for QoS and Teams](https://docs.microsoft.com/en-us/microsoftteams/qos-in-teams).

### Adding DSCP Markers in Microsoft Teams

Microsoft recommends that you use a combination of DSCP markings at the endpoint and port-based ACLs on routers, if possible. Using a GPO to catch the majority of clients, and also using port-based DSCP tagging will ensure that mobile, Mac, and other clients will still get QoS treatment (at least partially).

You can implement QoS by using a Group Policy Object (GPO) to direct Client devices to insert a DSCP marker in the IP packet header to identify it as particular type of traffic (for example, voice). Routers and other network devices can be configured to recognize this and put the traffic in a separate, higher-priority queue.

This is a sample QoS configuration for traffic types in Teams:

![Teams_DSCP_TrafficType.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248171290909.png)

### Adding the MS Teams and Skype Applications to Network Rules

In the Network Rules screen (**Networking > Network Rules**) edit the Applications for a rule and add the Skype application for the specific traffic type. The following screenshot shows the different Skype applications that you can add to a network rules:

![NetworkRule_DSCP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248194776093.png)

This is an example of a network rule that applies the same QoS priority to **Skype Screenshare (DSCP = 24)** and **Skype Video (DSCP = 36)**:

![NetworkRule_SkypeApp.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248163081245.png)

#### Sample Analytics of QoS for Microsoft Teams

This section shows an example of the Application analytics for a site.

This is an example of the Microsoft Teams traffic before adding DSCP markers:

![AppAnalytics_Before.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248163202589.png)

After adding the DSCP markers, you can see the analytics for each traffic type:

![AppAnalytics_After.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248187953309.png)
