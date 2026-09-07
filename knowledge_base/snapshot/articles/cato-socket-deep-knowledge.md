---
title: "Cato Socket: Deep Knowledge"
slug: "cato-socket-deep-knowledge"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/cato-socket-deep-knowledge"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Socket: Deep Knowledge

## Overview of How the Cato Socket Sends Traffic

The Cato Socket is a SD-WAN device that connects sites to the Cato Cloud and manages traffic routing, quality of service, and traffic priorities. The Socket has three layers of decision making before sending traffic over encrypted tunnel to the Cloud. This article discusses the Socket three decision layers:

Part 1: The Socket interfaces and precedence

Part 2: PBR and Network rules within the Socket

Part 3: The Socket Traffic prioritization and QoS

All of these items are relevant for both types of Sockets: X1500 and X1700.

The following diagram shows the traffic flow within the Socket and to the Cato Cloud.

| ![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248007128861.png) |
| --- |

## Part 1: The Socket Interfaces and Precedence

Each of your sites has different connectivity options (DIA, MPLS, LTE, etc.). This article explains links configuration and options to get the most optimal bandwidth management with load balancing and redundancy.

Cato supports these deployment options:

- Active/active
- Active/passive
- Working with more than two links

For more information on Cato Socket interfaces and precedence options, see [Part 1 The Socket Interfaces and Precedence](/v1/docs/part-1-the-socket-interfaces-and-precedence).

Setting the Socket interfaces, defines which links are available to transport the traffic. On top of that, you can use Cato’s network rules to select the routing options for any type of traffic.

## Part 2: Network Rules within the Socket

Routing traffic over the best link allows you to optimize any type of traffic. The network rules are in an ordered rulebase that gives you the flexibility to route traffic over links and transports for each traffic type.

These are the categories of network rules:

- Internet rules - control and route outbound traffic to the public Internet
- WAN rules - control and route traffic between datacenters, sites or users in the account

For more information on Cato network rules, see [Part 2 PBR and Network Rules within the Socket](/v1/docs/part-2-pbr-and-network-rules-within-the-socket).

For each network rule, you can choose the QoS priority for that specific type of traffic.

## Part 3: The Socket Traffic Prioritization and QoS

Cato Networks’ QoS helps you to prioritize the traffic and improve the bandwidth usage in your network. Create QoS bandwidth profiles for your account and then you can easily assign the profile to network rules. The same proprietary Cato QoS engine is used both in the Socket and the PoP to manage the traffic end to end.

For more information on Cato bandwidth management and QoS, see [Part 3 The Socket Traffic Prioritization and QoS](/v1/docs/part-3-the-socket-traffic-prioritization-and-qos)
