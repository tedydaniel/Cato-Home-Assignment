---
title: "Asymmetric Routing over Cato and MPLS"
slug: "asymmetric-routing-over-cato-and-mpls"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/asymmetric-routing-over-cato-and-mpls"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Asymmetric Routing over Cato and MPLS

Asymmetric routing over Cato and MPLS is when sending traffic from a source to a destination over the MPLS and the traffic returns over the Cato Cloud. This article describes the limitations of using this deployment.

## The Challenge

Is it possible to use an asymmetric routing over Cato Cloud and MPLS where the outgoing traffic flow goes through MPLS and the incoming traffic through Cato Cloud? Does Cato support asymmetric routing? What about the 3-way handshake messages?

![asymmetricTrafic.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248178881949.png)

## The Solution

You can use asymmetric routing where the outgoing traffic is sent over the MPLS link and the incoming traffic is sent over the Cato Cloud. However, there are several limitations to consider when working with asymmetric traffic:

- The traffic reaches the destination, but features that are based on the application level are not applied, these features are: networking rules, security rules, WAN acceleration and QoS.
  - These features require the ability to detect the type of application (Layer 7) and this isn’t supported, because only half of the traffic is passing through the Cato Cloud. The 3-way handshake is only partially over the Cato Cloud and is detected as **Open Mode.** The **Open Mode** is a connection mode that the Cato Cloud is not aware of the beginning of the connection. The Cato Cloud detects that traffic in the middle of the connection.

- These features are based on the Cato Cloud acting as a proxy aren’t supported for asymmetric traffic. The proxy requires stateful and active traffic management, which isn’t possible with asymmetric traffic.
- Asymmetric traffic can cause out-of-order packets delivery.
- The asymmetric traffic is only supported for WAN traffic, but not for Internet traffic.

> [!NOTE]
> Note:
> 
> Due to all of these limitations, Cato Networks doesn't officially support asymmetric routing.
