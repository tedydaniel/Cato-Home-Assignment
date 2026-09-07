---
title: "Configuring a Site-Level NAT Policy"
slug: "configuring-a-site-level-nat-policy"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/configuring-a-site-level-nat-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring a Site-Level NAT Policy

This article discusses how to use the NAT policy to manage and prioritize traffic for sites in your account.

## Overview

There are many challenges facing organizations that want to translate their network traffic while still maintaining accessibility to all of their relevant resources. Especially when you need to communicate between private networks that might work with the same private IP ranges. In addition, you might have resources whose structure or topology you don’t want to expose, in which case, you can use NAT to make the traffic appear as if it comes from a certain IP address.

Alternatively, you might need to offer remote access to internal services such as web or file servers. You can provide one public IP address that is then converted to a different internal IP address or addresses.

Cato lets you create a site-specific NAT policy to match specific source and destination IPs, and apply both source and destination NAT (SNAT and DNAT, respectively) for outgoing traffic (from the Cato Cloud towards the site).

![Site-NAT-Architecture.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247993158301.png)

The NAT policy is applied to incoming traffic (from the PoP) to the site on which the policy is configured:

- Traffic from the Internet (ie. RPF)
- Traffic from a different Cato site (ie. WAN traffic)

### Enhanced NAT with Port Address Translation (PAT)

Cato’s NAT implementation goes beyond basic IP address translation by incorporating by default Port Address Translation (PAT), enabling many-to-one NAT functionality. This allows up to 65,536 concurrent sessions per translated IP address by assigning unique source port numbers to each session. As a result, multiple original IP hosts can simultaneously initiate connections through a single translated IP, while maintaining session uniqueness.

This granular control is essential for efficiently handling scenarios such as:

- Access to multiple internal services exposed through a single IP
- High-density user environments, where thousands of sessions must be mapped without exhausting IP address resources

By leveraging PAT, Cato ensures scalable, collision-free connectivity and seamless application performance even under heavy traffic loads.

## NAT Policy Use Cases

The following section presents two example use cases for SNAT and DNAT. The example below shows the rulebase for these use cases.

![Site-NAT-Policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247976859165.png)

### SNAT Use Case

In this scenario, you have a group of IT admins connected via an SDP Client. They need to access a resource belonging to a 3rd party, for example, a ticketing system, located behind an IPsec site elsewhere in the company.

The third party requires you to communicate using a specific IP address, e.g. 192.151.100.10. The original source IP (that belongs to the IT admins group) will be blocked from communicating.

To solve this, you can create a NAT policy rule for connections whose original source IP is the admins in a specific group. When trying to access the ticketing system, you apply Source NAT on the admin IP address to translate to 192.151.100.10, which ensures that the IT admin can communicate with the 3rd party server.

### DNAT Use Case

In this scenario, you have multiple hosts from different groups sending traffic to one IP address. These machines all send their packets to a single network address, e.g. 203.0.113.96.

To make sure that you maintain optimal performance across your network, you can create several DNAT rules to direct traffic to different servers based on the source IP address and the traffic type:

- Traffic from VLAN1 to 203.0.113.96 is sent to 10.10.10.5
- Traffic from Finance to 203.0.113.96, is sent to 10.10.10.25
- Traffic from Procurement to 203.0.113.96, is sent to 10.10.10.65

This enables you to add more machines to the respective groups without having to change your configuration, while also efficiently managing traffic to a single IP address.

## Working with the NAT Rulebase

The NAT policy uses ordered rules. A packet arrives and is checked against the rules. Once a rule is matched, an action is applied and none of the other rules are processed.

For example, if a connection matches rule #3, the action is applied to the connection and all the sequential rules are ignored. If a connection doesn’t match any rule, it is processed with the original data.

## Configuring the NAT Policy

This section explains how to define rules for NAT and the objects, ports, and services that you can configure.

### Defining NAT Rules

Create a NAT rule and configure the settings for the rule to manage routing for the LAN traffic.

NAT policy rules are applied to a site within approximately one minute.

For customers who use the legacy configuration of the Socket LAN IP as the Translated Source IP, we do not recommend this configuration.

**To define a NAT rule:**

1. From the navigation menu, click **Network > Sites** and select the site.

> [!NOTE]
> Note:
> 
> If you do not see NAT policy in your menu and would like to enable it, contact your account representative or Customer Support.
2. From the navigation menu, click **Site Configuration > NAT**.
3. Click **New**. The **Add NAT Rule** panel opens.
4. From the **General** section, configure the following settings for the rule:
  - Enter the **Name** for the rule.
  - Enable or disable the rule using the slide (green is enabled, grey is disabled).
  - Configure the **Rule Order**. Define a higher number for more specific rules and a lower number for less specific rules.
5. Configure the **Original Source IP** settings.
  - Select IP Range or Any.

IP range can be a single IP address or a range of addresses. You can create multiple entries.
6. Configure the **Original Destination IP and Port/Protocol** settings:
  - Under **Destination IP**, select IP range or Any.

IP range can be a single IP address or a range of addresses. You can create multiple entries.
  - Under **Destination Port/Protocol**, define the protocol and port using the format protocol/port:

For example, TCP/80, UDP/53, TCP/443
7. Under NAT Action, determine whether to change the source or destination NAT. You can change both the source and destination, but you can't keep both original addresses.
8. Click **Apply**, and then click **Save**.

The rule is added to the table.
