---
title: "Understanding Full Path URL for App Control vs Internet Firewall"
slug: "understanding-full-path-url-for-app-control-vs-internet-firewall"
updated: 2026-07-23T07:52:21Z
published: 2026-07-23T07:52:21Z
canonical: "knowledge.catonetworks.com/understanding-full-path-url-for-app-control-vs-internet-firewall"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding Full Path URL for App Control vs Internet Firewall

This article discusses how the different security engines in the Cato Cloud handle data for the full path URL within a traffic flow.

## Overview

HTTP requests are handled differently by the Firewall engine that is used for the Internet Firewall policy and the App Control engine that is used for the Application Control policy. The Cato platform includes multiple security engines that simultaneously analyze and process traffic flows, and it can be difficult to understand how data, such as the full path URL, is extracted from a specific flow and logged in an event.

For more information about the Cato security engines, see [Understanding Packet Flow with Cato SPACE Architecture](/v1/docs/understanding-packet-flow-with-cato-space-architecture).

## Analyzing HTTP Requests for App Control vs Firewall Engine

The URL is an attribute that often changes with each HTTP request within a traffic flow. Firewall engines are designed to balance security and performance and don't inspect every HTTP request that occurs within a flow. This means that the full path URL data for Internet firewall events can be misleading. The PoP makes a best effort to enrich events with additional data, and it's possible that Internet Firewall events will contain the full path URL data.

On the other hand, the App Control engine examines every HTTP request with a session and logs the full path URL data. For customers that are using the CASB service, App Security traffic events will contain the full path URL data for relevant cloud apps, because the App Control engine extracted that data.

The main difference between the App Control engine and the Firewall engine is the frequency at which HTTP requests are inspected:

- App Control engine:
  - For Application Control policies (CASB), inspects every HTTP request with a traffic flow
  - Logs **Full Path URL** field for events
- Firewall engine:
  - For Internet Firewall policies, inspects the first HTTP request within a traffic flow
  - Inconsistent behavior for logging **Full Path URL** field for events

**Best Practice:** If you want to consistently log the full path URL data in events, use the [Application Control policy](/v1/docs/managing-the-application-control-policy) to log events for the relevant traffic with the following settings:

- 
  - **For applications with granular activities:**
    - Application - Any Cloud Application (or a specific app)
    - Criteria - Any Granular Activity
  - **For applications without granular activities:** "Any Granular Activity" won't match any traffic. To log full path URL data for these apps, create a separate rule with no criteria defined:
    - Application - Any Cloud Application (or a specific app)
    - Criteria - *(leave blank)*

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(80).png)
