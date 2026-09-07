---
title: "What is the Socket Next Gen LAN Firewall"
slug: "what-is-the-socket-next-gen-lan-firewall"
updated: 2026-07-27T12:12:27Z
published: 2026-07-27T12:12:27Z
canonical: "knowledge.catonetworks.com/what-is-the-socket-next-gen-lan-firewall"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is the Socket Next Gen LAN Firewall

## Overview

By default, LAN traffic behind a site is sent over the WAN to the PoP for traffic inspection. This means that for hosts behind the same site, the traffic is sent over the last-mile to the PoP, and then sent back to the same site. You can also use the Socket as a LAN firewall to segment the traffic locally, without needing a third-party firewall appliance.

The Socket Next Gen LAN Firewall lets you apply Layer 2 through Layer 7 (application layer) policy controls to east-west traffic while routing and segmenting the traffic behind the site. Routing the traffic locally also ensures that critical environments such as OT and IoT can continue to operate over the local network, even if the Internet connection is down.

The LAN Firewall is an account-level policy that lets you configure rules to apply corporate-wide policies across multiple sites, without manually configuring each site. For more information about configuring Next Gen LAN Firewall rules, see [Managing the Socket Next Gen LAN Firewall Policy](/v1/docs/managing-the-socket-next-gen-lan-firewall-policy).

The account-level Socket Next Gen LAN Firewall policy also supports sub-policies and role-based access control (RBAC), so you can delegate management of specific rules to different admins while keeping centralized control over the rest of the policy. Learn more [here](/v1/docs/managing-the-socket-next-gen-lan-firewall-policy#using-subpolicies-and-rbac-for-the-lan-firewall-policy).

For information about Next Gen LAN Firewall throughput for different Socket types, see [Cato Cloud Thresholds and Limits](/v1/docs/cato-cloud-thresholds-and-limits).

### Use Case

Example Corp has 200 global branches that use the same LAN network design. This includes VLAN ID 10 for servers, and VLAN ID 20 for business-critical OT devices. The network team decides to route traffic between these VLANs locally, which enables the OT devices and servers to continue communicating even if there is an ISP outage. Additionally, they only want to allow specific protocols between the VLANs.

The network team creates a LAN Network rule with the **Site** configured as a **Group** object containing the 200 relevant sites, and the **Transport** configured as **LAN** to route the traffic locally. Then they create a LAN Firewall rule under the LAN Network rule, with VLAN 10 and VLAN 20 configured as **Source** and **Destination**, and **Direction** as **Both**. Under **Service/Port**, they configure the protocols they want to allow, and the **Action** is configured as **Allow**.

This single LAN Firewall rule applies the policy to each one of the 200 local networks, without having to configure separate rules for all the sites.

For information about Next Gen LAN Firewall throughput for different Socket types, see this [article](/v1/docs/cato-cloud-thresholds-and-limits#supported-throughput-for-cato-sites).

### Prerequisites

- The Socket Next Gen LAN Firewall is available only for accounts that don't have a current site-level LAN Firewall policy configured. In the future, Cato will convert the current site-level LAN Firewall policies to the Socket Next Gen LAN Firewall policy
- Supported from Socket v22 and higher and now to the Use Case

## Fundamental Concepts

This section explains basic concepts for understanding the role and capabilities of the Layer 7 LAN firewall.

### Types of Traffic

To understand the role of the LAN Firewall and its relationship to other Cato policies, it’s important to understand that Cato identifies traffic as one of three different types: LAN, WAN, or Internet. Understanding the distinctions and characteristics of these types of traffic is crucial for optimal policy planning and utilization of the different Cato firewall policies. For more information, see [Getting Started with the Cato Firewalls](https://support.catonetworks.com/document/preview/154485#UUID-822c0508-fe02-a6ff-ae39-1c13a029fefd).

### WAN vs. LAN traffic within the Same Site

Traffic between hosts within the same site can be handled as either LAN traffic (routed by the Socket and not sent to the PoP), or WAN traffic (sent to the PoP and then back to the site), depending on your configuration. The default behavior for the Socket is to route all traffic to the PoP for inspection and the PoP blocks or allows the traffic. However, traffic that matches the LAN Firewall policy is routed locally and not sent to the PoP.

When traffic from a host in the LAN reaches the Socket, the Socket checks to see if the traffic matches a rule in the LAN firewall policy.

- If it matches a rule, the Socket routes the traffic to the local destination without sending it to the PoP.
- If the traffic doesn't match a LAN firewall rule, it is sent to the PoP for handling by the WAN or Internet firewall.

For more information about defining LAN traffic, see below, [The LAN Firewall Policy](/v1/docs/what-is-the-socket-next-gen-lan-firewall#the-lan-firewall-policy).

The following is a state machine diagram showing how the Socket LAN Firewall handles traffic from a host on the local network.

![LAN_FW_State_Machine.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34989852869917.png)

### Layer 7 vs Layer 2-4 Firewall Rules

The LAN firewall supports Layers 2 through 4 and Layer 7 (application layer) inspection, enabling you to control traffic based on applications, services, and specific content within applications. By default, sites support Layer 2-4 functionality, and you define in the policy which sites are also enabled with Layer 7 capabilities. This section describes the difference between Layer 2-4 and Layer 7 firewalling.

Layer 2-4 firewalls filter traffic based on basic criteria such as IP addresses, ports, and transport-layer protocols like TCP or UDP. For these criteria, the Socket firewall can decide to allow or block the traffic based on the first packet. While effective for basic traffic control, this approach doesn’t analyze the actual data being transmitted within the packets.

Layer 7 (Application Layer) firewalls inspect the packet payload to identify specific applications, domains, or protocols. For example, a Layer 7 firewall can distinguish between SMBv1 and SMBv3 traffic or identify the specific application generating the traffic (such as Office 365). This deeper inspection allows for more granular policy enforcement and improved control over local network traffic. However, because Layer 7 inspection requires analyzing additional packets to determine the application data (e.g. extracting a domain name in HTTP traffic), and greater Socket resources than Layer 4 processing. This should be taken into consideration when planning your corporate LAN firewall policy and deciding which sites to enable with Layer 7 capabilities.

When you enable a site with Layer 7 capabilities, the Socket performs deep packet inspection on traffic, whether or not a LAN Firewall rule is configured, as long as there is traffic defined to use LAN transport (see below, [The LAN Firewall Policy](/v1/docs/what-is-the-socket-next-gen-lan-firewall#the-lan-firewall-policy)). This means that Layer 7 data appears in events for the site traffic, including fields such as Application, App Risk, and Custom App.

## The LAN Firewall Policy

The Socket applies the LAN firewall policy by first determining a routing decision for the LAN traffic - whether to send the traffic to the PoP or to route it locally. Secondly, the LAN firewall rules are applied to determine if the traffic is blocked or allowed.

To implement this, the LAN firewall policy includes LAN Network and LAN Firewall rules. The LAN Network rules define how the Socket routes the traffic, locally over the LAN, or as WAN traffic sent to a PoP. Once a LAN Network rule is matched and defines the **Transport** as **LAN**, the related LAN Firewall rules determine whether the traffic is allowed or blocked, and the Socket enforces the rule. If traffic doesn’t match any LAN Network rule, it is treated as WAN traffic and sent to the PoP.

LAN Firewall rules are linked to a single LAN Network rule, ensuring that firewall actions are specific to the traffic defined by that LAN Network rule.

The following sections describe the characteristics for LAN Network and LAN Firewall rules.

![LAN_Firewall.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34989852942493.png)

### LAN Network Rules

LAN Network rules control which transport (LAN or WAN) is used to route traffic between various network hosts or segments. This is a global policy configured for the entire account, and not per specific sites. This means each rule can be configured to apply to multiple sites in the account. For example, if you set up multiple sites using the same VLAN configuration, you can create a single rule that applies to the VLANs in each site defined in the rule.

LAN Network rules make Layer 4 routing decisions and don't use Layer 7 functionality. For example, you can define Network rules with conditions for sites, VLANs, or specific protocols, but you can’t make a condition based on the application.

A LAN Network rule can be a parent to multiple LAN Firewall rules under it. There is a default ANY-ANY Block rule configured as the last rule under a LAN Network rule. Therefore, if traffic matches a LAN Network rule, but doesn't match a LAN Firewall rule, it is blocked.

### LAN Firewall Rules

LAN Firewall rules allow or block specific types of traffic, and track these events for monitoring and compliance purposes. Each LAN Firewall rule is directly linked to a specific parent LAN Network rule and is limited to the source and destination scope of the parent rule. LAN Firewall rules support up to Layer 4 segmentation by default, including segmentation based on MAC addresses. Additionally, for sites configured for Layer 7 functionality, the LAN Firewall rules can include intelligent traffic filtering based on applications, domains, and other Layer 7 conditions.

There is a default LAN Firewall ANY-ANY Block rule configured as the last rule under each LAN Network rule. Therefore, if traffic matches a LAN Network rule, but doesn't match a LAN Firewall rule, it is blocked. This implicit behavior enforces a true zero-trust approach to on-premises segmentation by ensuring that only explicitly allowed traffic can traverse the local network.

### Sub-Policies

A LAN Firewall policy is made up of a main policy and any number of sub-policies. Any rules that are not inside a sub-policy belong to the main policy when you define admin permissions.

- Each sub-policy is anchored by a scoping rule in the main policy. The scoping rule is a LAN Network rule whose conditions (for example, Source Site = Paris) define when the rules in the sub-policy are applied to the traffic.
- A sub-policy contains its own ordered LAN Network rules and LAN Firewall rules. The action of the first matching rule is applied to the traffic.
- Each sub-policy is treated as a separate entity for RBAC, so you can give different admins **View** or **Edit** access to different sub-policies.
- By default, an optional ANY ANY cleanup rule is added at the end of the sub-policy, using the Block action to match the default behavior of the LAN Firewall policy. This cleanup rule is only applied to traffic that matches the scoping rule for the sub-policy and doesn’t match any other rule in that sub-policy.
- You can add sections for rules inside a sub-policy.
- Sub-policies cannot contain other sub-policies (no nesting).
- You cannot move rules or sections between sub-policies, or between a sub-policy and the main policy
- An admin with access to a sub-policy can see its scoping rule even if they don’t have access to the main policy.
- Rule numbers stay consistent across the entire policy, even when some admins cannot view certain sub-policies. As a result, admins without view permissions for specific sub-policies may see gaps in the rule numbering.

**Note:** Rules inside a sub-policy that have ANY conditions are only applied to the traffic that also matches the scoping rule of the sub-policy. That means a rule with ANY ANY Block does not impact traffic that does NOT match the scoping rule.

**Example:** A company with regional network teams can create a sub-policy per region, scoped by source site, so that each regional admin manages only the LAN Firewall rules for their own sites and cannot change rules that belong to other regions or to the main policy.

### Publishing Changes

The LAN Firewall policy has a single **Publish** action that covers the main policy and all of its sub-policies:

- The number of pending changes is shown as a single counter across the main policy and all sub-policies.
- Publishing commits all pending changes across the policy in one revision, including changes made by other admins in sub-policies that you don’t have access to.
- An admin who has **Edit** access to only some sub-policies can still edit and publish their allowed changes.

### Understanding the Hit Count

The hit count helps you identify unused rules that can be removed from a policy, and optimize rule configuration to better match the required traffic scope. The hit count for a rule is based on the number of events generated by the rule. If a rule does not generate events, the hit count is zero.

The hit count contains two numbers:

- The approximate number of events generated by each rule in the policy
- How often the rule is hit relative to other rules (ranked by percentile)

These values are updated once every 24 hours and are based on the past 14 days of traffic.

You can quickly identify the rules with the highest and lowest hit count, based on the color of the status bar. This color reflects how often the rule is hit relative to other rules:

- Blue: 0 - 24th percentile
- Green: 25th - 49th percentile
- Orange: 50th - 74th percentile
- Red: 75th -100th percentile

#### Resetting and Refreshing the Hit Counter

![Reset.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34989786843805.png)

The hit count values are updated automatically every 24 hours and are based on the past 14 days of traffic. From the three dots at the end of each rule, you can reset or refresh the hit count for up-to-date visibility. This lets you accurately measure rule effectiveness and immediately validate rule activity.

- Resetting the hit counter for a specific rule returns the hit count to 0
- Refreshing the hit counter updates the hit count on demand for all policy rules
