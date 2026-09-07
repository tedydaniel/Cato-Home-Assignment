---
title: "Configuring DNS Relay and Split Tunnel for macOS Clients (EA)"
slug: "configuring-dns-relay-and-split-tunnel-for-macos-clients"
updated: 2026-07-12T08:08:15Z
published: 2026-07-12T08:08:15Z
canonical: "knowledge.catonetworks.com/configuring-dns-relay-and-split-tunnel-for-macos-clients"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring DNS Relay and Split Tunnel for macOS Clients (EA)

This article explains how the macOS Cato Client uses DNS Relay and the Split Tunnel policy to route specific traffic to a destination.

## Overview

By default, the Cato Client routes all remote user traffic (including DNS) through the Cato Cloud, where it is inspected and security and networking policies are applied. However, some deployments require specific traffic to bypass the Cato Cloud and connect directly to its destination, while all other traffic continues to be secured by Cato.

For macOS Clients, DNS Relay and the Split Tunnel policy work together to implement this routing behavior. DNS Relay determines where the destination resides by resolving DNS requests, and the Split Tunnel policy determines whether the Client routes traffic through the Cato Cloud or directly to the destination.

Unlike security and networking policies that are enforced by PoPs in the Cato Cloud, these routing decisions are implemented locally by the macOS Client. For more about the Split Tunnel Policy, see this [article](/v1/docs/routing-with-the-cato-client-split-tunnel-policy).

### Understanding the Client Routing Flow

When a macOS user connects with the Cato Client, the Client evaluates traffic in two stages:

1. DNS resolution - Determines where the destination resides
2. Traffic routing - Determines whether user traffic to the resolved destination uses the Cato tunnel or goes directly to the local network

DNS traffic can be resolved by the Cato DNS server or by a local DNS server assigned to the network. Use DNS suffixes when you need specific DNS requests to be resolved by a local DNS server. After the destination is resolved, the Client routes the user traffic according to the Split Tunnel policy.

Traffic that is routed to the Cato Cloud is inspected and secured by the relevant account policies. Traffic that is routed locally bypasses the Cato tunnel and uses the local network path.

### Understanding Split Tunnel Routing Models

The Split Tunnel policy supports two routing models:

1. Route all traffic to Cato and define bypass exceptions
2. Route only defined destinations to Cato

In both models, **Destination Exclustions** can be based on:

- FQDN (app.example.com)
- IP range (192.168.1.0/24)

Use FQDNs or IP ranges when you need to control the route for user traffic to specific destinations.

### Prerequisites

To use DNS Relay and FQDN-based Split Tunnel routing for macOS Clients, make sure that:

- The macOS Client is version 6.0.1 or higher
- The Split Tunnel policy specifies DNS suffixes or FQDN-based destinations
- One-time: users allow the DNS system extension

## Sample Use Cases

### Route All Traffic to Cato with Exceptions

ABC Company requires all remote user traffic to be inspected by the Cato Cloud. However, users also need direct access to internal resources that are available on the local network. The admin configures the Split Tunnel policy to route all traffic through the Cato Cloud by default, while allowing traffic to specific destinations to bypass the tunnel.

The Split Tunnel rule is configured with these settings:

- Connection Mode: All Ports & Protocols
- Routing Policy: Route all to Cato
- DNS Exclusions: `local.com`
- Destination Exclusions: local.com (FQDN)

When a user accesses www.local.com, the macOS Client recognizes that the DNS suffix matches a DNS exclusion and resolves the request using the local DNS server. The Client then matches www.local.com as a destination exclusion and routes the traffic directly to the local network. All other traffic is routed through the Cato Cloud, where networking and security policies are applied.

### Route Only Defined Destinations to Cato

ABC Company uses a third-party security solution to inspect most Internet traffic, but wants to use the Cato Cloud to secure only Microsoft traffic. The admin configures the Split Tunnel policy so that traffic bypasses the Cato Cloud by default, and only traffic to the Microsoft FQDN is routed through the Cato Cloud.

The Split Tunnel rule is configured with these settings:

- **Connection Mode:** All Ports & Protocols
- **Routing Policy:** Route only selected to Cato
- **Destination Inclusions:** `login.microsoftonline.com` (FQDN)

When a user accesses a Microsoft resource, the macOS Client resolves the destination and routes the Microsoft traffic through the Cato Cloud, where security and networking policies are applied. Traffic to all other destinations bypasses the Cato Cloud and is routed directly to the destination.

## DNS Relay on macOS Clients

DNS Relay enables the macOS Client to make DNS and routing decisions for Split Tunnel rules that use DNS suffixes or FQDN-based destinations.

On macOS, DNS Relay is implemented as a DNS proxy extension. The extension is installed under Network Filters and Proxies when the Split Tunnel configuration requires DNS suffix or FQDN-based routing.

DNS Relay does not change the DNS server assigned to the Client interface. The Client continues to use the Cato DNS server or the DNS server configured by the DNS Settings policy. DNS Relay helps determine how DNS requests are resolved and assists with dynamic routing updates for FQDN-based destinations.

DNS Relay is only deployed when the Split Tunnel policy uses DNS suffixes or FQDN-based destinations. If the policy does not use these items, the Client does not install the DNS proxy extension.

### Confirm DNS Relay on the macOS Endpoint

You can confirm that DNS Relay is enabled on the macOS endpoint from the Client and from the macOS network settings.

In the Client, the Settings page indicates whether the **DNS System Extension** is **Allowed**. ![Client_DNS](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Client_DNS.png)

In macOS, the DNS proxy extension appears under **Network > VPN & Filters** and is enabled when the Split Tunnel configuration requires it. ![macOS_DNS](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/macOS_DNS.png)

## Configure Split Tunnel Routing for macOS Clients

Create a Split Tunnel rule for macOS Clients when you need to control how DNS requests are resolved and how user traffic is routed.

To configure Split Tunnel routing for macOS Clients:

1. From the navigation menu, select **Access > Split Tunnel Policy**
2. Create or edit a Split Tunnel rule
3. In **Platforms**, select macOS
4. Select the routing model for the rule:
  - **Route all traffic to Cato** to secure traffic by default and define exceptions
  - **Route only selected to Cato** to bypass traffic by default and define selected destinations
5. Define the DNS suffixes, FQDNs, or IP ranges for the rule
6. Click **Apply**
7. Click **Save**

The macOS Client applies the Split Tunnel policy locally on the endpoint. When the rule requires DNS suffix or FQDN-based routing, the Client installs and uses the DNS proxy extension.
