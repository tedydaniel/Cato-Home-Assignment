---
title: "Integrating Cato with an Alt. WAN Network"
slug: "integrating-cato-with-an-alt-wan-network"
updated: 2026-07-20T08:15:45Z
published: 2026-07-20T08:15:45Z
canonical: "knowledge.catonetworks.com/integrating-cato-with-an-alt-wan-network"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating Cato with an Alt. WAN Network

## Overview of Alt. WAN

Customers can use Cato Sockets to completely integrate existing MPLS networks with Cato. The Sockets provide advanced networking capabilities to manage the WAN traffic between your sites over the Cato Cloud and the MPLS network.

The Socket sends the Alternative WAN traffic to the MPLS PE (Provider Edge) router, which then forwards the traffic over the MPLS core to the destination. The MPLS provider is responsible for transferring the data and allowing a direct connection between the network nodes.

The following diagram shows a sample site-to-site deployment of two Cato Sockets connecting over an MPLS network:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Alt WAN Network Overview.png)

> [!NOTE]
> Note:
> 
> The Alt. WAN tunnel uses UDP port 20049 to send traffic.

## Integrating Cato with the Alt. WAN Network

When you integrate Alt. WAN traffic in a site with a Cato Socket, you must apply the following settings:

1. Configure the Socket WAN interface to only manage Alt. WAN traffic. When you configure the Alt. WAN interface, the interface is used for only Alt. WAN transport.
2. Create or edit network rules to manage the traffic via the Alt. WAN link.

### Explaining Alt. WAN and Alt. WAN Layer-2 Destinations

Cato distinguishes between two types of Alt. WAN networks, Sockets on the same (Layer-2) or different (Layer-3) subnets. Use the Cato Management Application to select the correct Alt. WAN network and link destination for the Socket. The only difference between the Alt. WAN Layer-2 and Alt. WAN Layer-3 options, is the source IP address that the Socket uses for transport.

**Alternative WAN (Layer-2)**

When you need Socket sites to be on the same network subnet, set the link destination to **Alternative WAN (Layer-2)**. The Socket uses the source IP address and the Gateway IP address in the Alt. WAN link settings to route the traffic to the destination.

**Sockets in High Availability Connected to Alt. WAN Network**

In Socket HA mode, both primary and secondary Sockets use a single logical MAC address. The logical MAC address is defined by a fixed value followed by the Alt. WAN network interface ID.

Use the following requirements for HA Sockets in Alt. WAN configuration:

1. Both primary and secondary Sockets on the same site must be connected with the same network interfaces to the Alt. WAN network

2. The HA Sockets in different sites must be connected to the Alt. WAN network, using different network interfaces

For example:

- On site1: the primary and secondary Sockets are connected to network interface #2 (MAC address AA-BB-CC-DD-EE-02)
- On site2: the primary and secondary Sockets are connected to network interface #3 (MAC address AA-BB-CC-DD-EE-03)

> [!NOTE]
> Note:
> 
> The number of HA sites that can be connected to the same MPLS network is limited to the number of network interfaces in the Socket.

In case you want to change this behavior, please contact customer support.

**Alternative WAN (Alt. WAN Layer-3)**

When you need to provide WAN connectivity for Sockets that are in different networks, use the **Alternative WAN (Alt. WAN Layer-3)** destination option for the link. The Socket uses the Gateway IP address of LAN 01 native range (**Network > Sites > {Site Name} > Site Configuration > Networks**) as the source IP address to route the traffic to the destination.

### Sample for Alt. WAN

After you configure the Socket for the Alt. WAN traffic, create network rules to designate the traffic types that use this link. The following example shows a network rule that provides Alt. WAN redundancy for WAN VoIP video traffic. If the Cato Cloud isn’t available, then the traffic falls back to the MPLS network over the Alt. WAN link.

![alt_wan_transport.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24270302120861.png)

This WAN network rule is only for the VoIP Video category, and is from Any source to Any destination. Configure the **Transport** options to define the fallback behavior: the primary transport option is the Cato Cloud and the secondary is the Alt. WAN link.

## How it Works - Sending Alt. WAN Traffic

The Cato Socket fully supports sending WAN traffic over the Alt. WAN links for a site. Let's take a deeper look at how Sockets send Alt. WAN traffic.

When a Socket connects to the private MPLS network, it creates a UDP based encrypted tunnel to transfer the data between the Sockets. Then the MPLS edge router identifies the Socket connection and adds the Socket IP address to its routing table, using the VRFs (Virtual Routing and Forwarding).

The Socket encapsulates the traffic by adding proprietary headers to the packets. These headers help to measure the quality metrics for the traffic and contain the Socket source and destination IP addresses. These headers are integrated probes that monitor the reachability and the link quality (packet loss, latency, and jitter).

## Deploying New Sockets and Sending Alt. WAN Traffic

For situations where you are deploying a new Socket on a site and other sites in your network aren't provisioned with Sockets, the new Socket can't communicate with the other sites. The Socket Gradual Deployment feature lets the new Socket send unknown WAN traffic over the MPLS network.

When this feature is enabled, the Socket enters deployment mode and assumes that any RFC1918 network space (that's not explicitly part of a Cato site) exists in the Alt. WAN network space. When packets with an unknown private destination IP addresses arrive to the Socket LAN1 link, the Socket sends these packets over the Alt. WAN link. The packets arrive to the MPLS edge router, which then routes the traffic over the MPLS network toward the destination.

To enable Socket Gradual Deployment for a site in your account, contact Cato Support.

## Analyzing Alt. WAN Traffic

The Cato Management Application provides multiple analytics capabilities to monitor and analyze the Alt. WAN traffic in your site.

### Monitoring Real Time Alt. WAN Traffic

The Real-Time analytics window shows the statistics of transport and QoS. Select the Alt. WAN transport to see the real time statistics of the Alt. WAN link in your site. For more about real time analytics, see [Analyzing Data for a Site in Real-Time](/docs/integrating-cato-with-an-alt-wan-network#).

### Analyzing Alt. WAN Traffic with Priority Analyzer

The Priority Analyzer window allows you to analyze the QoS and PBR data. It provides a better visibility of the bandwidth usage over the different network links, including the Alt. WAN. For more about the priority analyzer, see [Analyzing QoS and BW Management for a Site](/docs/integrating-cato-with-an-alt-wan-network#).
