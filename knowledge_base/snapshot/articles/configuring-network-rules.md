---
title: "Configuring Network Rules"
slug: "configuring-network-rules"
updated: 2026-08-13T07:20:24Z
published: 2026-08-13T07:20:24Z
canonical: "knowledge.catonetworks.com/configuring-network-rules"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Network Rules

## Overview

Network rules let you steer and prioritize traffic across your WAN and Internet connections, giving you fine-grained control over performance, routing, and link usage. By creating rules based on application, source, and destination, you can ensure critical traffic receives the right QoS, optimize for latency or packet loss, and select the best transport paths. Use the Network Rules page to define rule order, apply acceleration settings, and configure advanced routing behaviors that align with your business and technical requirements.

For more about network rules and Cato, see [What are Network Rules?](/v1/docs/what-are-network-rules).

### Working with Multiple Objects in a Single Rule

The **Source**, **App/Category**, and **Destination** columns form an AND relationship: the rule is triggered only if traffic matches the criteria defined in all three columns.

When there are multiple items within one column, there is an OR relationship: the rule is applied if traffic matches the criteria defined for any of the items. For example, a rule that defines **App/Category** with **Service** for **TCP** and for **UDP**, this rule matches TCP or UDP traffic.

### Policy Revisions and Concurrent Editing by Multiple Admins

The Network Rules page lets different admins edit the policy in parallel. Each admin can edit rules and save the changes to the rulebase in their own private revision and then publish them to the account policy (the published revision). For more information on how to manage policy revisions, see [Working with Policy Revisions](/v1/docs/working-with-policy-revisions).

## Enabling the Network Rule Policy

Control whether the Network Rule policy is enforced by using the **Network Rules Enabled** toggle in the Network Rules page. When the policy is enabled, the configured rules are applied to route and prioritize traffic in your account. Disabling the policy immediately stops the enforcement of these rules.

**To enable the Network Rules policy:**

1. From the navigation menu, click **Network > Network Rules**.
2. Click the toggle next to **Network Rules Disabled**.
3. Click **Continue** in the confirmation window. The toggle is green when the policy is enabled.

## Creating a Network Rule

To apply custom traffic steering or QoS to specific WAN or Internet traffic flows, create a network rule that defines the traffic and how it should be handled. Network Rules is an ordered policy, and they are evaluated according to their order. Create a new rule in the correct position, such as before or after an existing rule.

When configuring the **Source**, you define which traffic the rule applies to. You can select from a variety of global objects, such as IP ranges, application categories, or user groups, to match the relevant traffic.

Each rule includes the following configuration options:

- [Bandwidth priority](/v1/docs/configuring-network-rules#h_01KRV16WDX8VD12TM9X8HB3AKR) - Assigns a QoS priority to the traffic to ensure performance for business-critical flows during congestion
- [Acceleration and optimization](/v1/docs/configuring-network-rules#h_01KRV16WDY4ZZFPQNEAMSX1MQD) - Enables TCP acceleration and packet duplication to reduce latency and packet loss
- [Primary and Secondary Transport](/v1/docs/configuring-network-rules#h_01KRV16WDX0DDQ4TM8MQKRXV3E) - Defines the preferred transport types for routing traffic (Cato Cloud, Off-Cloud, or Alt. WAN)
- [Routing Method](/v1/docs/configuring-network-rules#h_01KRV16WDY3ST8S905ST7VP260) - Egress traffic from specific PoPs, allocate NAT IPs, or [backhaul Internet traffic](/v1/docs/configuring-internet-traffic-backhauling) through gateway sites

![NetworkRules.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32588018817693(1).png)

**To create a WAN or Internet network rule:**

1. From the navigation menu, click **Network > Network Rules**.
2. Click **New > New Rule**. The **Add Network Rule** panel opens.
3. From the **General** section, configure the following settings for the rule:
  1. Enter the **Name** for the rule.
  2. Enable or disable the rule using the slider (green is enabled, grey is disabled).
  3. Select the **Position** for the new rule.
  4. In the **Rule Type** drop-down menu, select whether this rule is for **WAN** or **Internet** traffic.
4. Expand the **Source** section and select one or more objects for the traffic source for this rule (or you can enter an IP address).
  1. Select the type (for example: Host, Network Interface, IP, IP Range, or Any). The default value is **Any**.
  2. When needed, select a specific object from the drop-down list for that type.
5. Expand the **Criteria** section and add the device conditions to the rule. For more information, see [Adding Device Conditions to Firewall Rules](/v1/docs/adding-device-conditions-to-firewall-rules). The default values are **Any**.
6. For WAN traffic rules, expand the **Destination** section and select one or more objects for the traffic destination for this rule.
7. Expand the **App/Category** section and select one or more applications for the rule.

When there is more than one App/Category object in a rule, there is an OR relationship between them. The default value is **Any**.

For a detailed explanation of each of the options in **App/Category** section, see [Reference for Rule Objects](/v1/docs/reference-for-rule-objects).
8. In the **Configuration** section, you can configure the following settings for the network rule (see explanations below):
  - **Bandwidth Priority**
  - **Primary Transport** and **Secondary Transport**
9. Click **Save**. The panel closes, and the settings are updated in the policy. The changes are saved to your unpublished revision and are available for editing until they are published or discarded.
10. Click **Publish**. A confirmation window opens, click **Publish**.

## Changing the Bandwidth Priorities (QoS) for a Rule

By default, new rules are assigned the default priority (p255), which you can change according to the QoS needs of your network.

The lower the priority number, the higher the QoS priority for the rule. For example, a rule with priority 10 has a higher QoS priority than a rule with priority 40.

For more about defining the bandwidth policies for your account, see [Configuring Bandwidth Management Profiles](/v1/docs/configuring-bandwidth-management-profiles).

**To change the bandwidth priority for a rule:**

1. From the navigation menu, click **Network > Network Rules**.
2. Click the network rule. The **Edit Network Rule** panel opens.
3. Expand the **Configuration** section.
4. In the **Bandwidth Management** section, from the **Bandwidth Priority** drop-down menu, select the QoS priority for this rule.
5. Click **Save**. The panel closes, and the settings are updated in the policy. The changes are saved to your unpublished revision and are available for editing until they are published or discarded.
6. Click **Publish**. A confirmation window opens, click **Publish**.

## Configuring the Transport and Routing Options

This section explains how to configure the transport options for a network rule and to egress traffic to a specific location or IP address.

### Customizing the Transport Options for a Rule

Network rules are configured globally. If a specific site does not have the specified transport, the Socket treats such a configuration as if it were configured for **Automatic**.

If you select explicit transports/NICs, the QoS engine monitors packet loss, jitter, and latency. If congestion occurs, packets are dropped. Selecting **Automatic** for transports, then the QoS engine monitors congestion in addition to packet loss, jitter, and latency.

Alt-WAN isn’t supported for Off-Cloud as a secondary transport. You can’t configure a network rule with Alt-WAN as the primary transport that fails over to Off-Cloud.

#### Known Limitation

For site-to-site WAN traffic, a WAN network rule can use a specific Socket interface as the primary transport only when that interface is available and configured on both Socket sites. If the selected interface exists only on one site, traffic that matches the rule can be dropped.

For example, if a rule sends traffic over WAN3 from one site, but the destination site doesn’t have a WAN3 interface, the traffic isn’t supported on that transport.

![TransportOptions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27760849914653(1).png)

- WAN rules have the following default settings:
  - **Primary Transport**: Cato
  - **Secondary Transport**: Automatic (accounting for additional transports such as MPLS, if applicable)
  - **Primary Interface Role**: Automatic
  - **Secondary Interface Role**: None (disabled as handled by the Automatic setting for Primary NIC)
  - **Route/NAT**: - (not applicable for WAN rules)
- Internet rules have the following default settings:
  - **Primary Transport**: Cato
  - **Secondary Transport**: None (don't use other transports)
  - **Primary Interface Role**: Automatic
  - **Secondary Interface Role**: None (disabled as handled by the Automatic setting for Primary NIC)
  - **Route/NAT**: None

**To customize the transport options for a network rule:**

1. From the navigation menu, click **Network > Network Rules**.
2. Click the network rule. The **Edit Network Rule** panel opens.
3. Expand the **Configuration** section.
4. Configure the transport fields as required: to route traffic via a specific transport, you can configure your primary and secondary transports.

The primary transport will be used as long as it is up and available, as determined by the Cato QoS engine. If the primary transport is not available, the secondary transport is used.
5. Configure the **Interface Role** fields (applicable only for traffic routed via Cato Cloud) as required.

To route traffic via a specific link, you can configure your primary and secondary NICs. The **Primary Interface Role** is used as long as it is up and available, as determined by the Cato QoS engine.

If the **Primary Interface Role** is not available, the **Secondary Interface Role** is used. When the **Secondary Interface Role** is set to **None**, the behavior is based on the setting for the **Primary Interface Role**:
  - **Automatic** - the Socket makes a best effort to send the traffic over the primary transport
  - Any other interface role - the Socket drops the traffic when the primary transport is not available
6. Click **Save**. The panel closes, and the settings are updated in the policy. The changes are saved to your unpublished revision and are available for editing until they are published or discarded.
7. Click **Publish**. A confirmation window opens, click **Publish**.

### Setting the Routing Method for an Internet Network Rule

You can configure an Internet Network Rule with different options to egress the traffic.

**Best Practice:** For Internet Network Rules that egress traffic (with the **NAT** or **Route via** option), we recommend that you define a specific **Source** or **App/Category** for the rule. Selecting **Any** as the **Source** or **App/Category** routes all Internet traffic and can cause unpredictable performance.

- Route via - Lets you select the egress PoP location from which the traffic is sent to the Internet.

**Note:** When egressing traffic to Tokyo, selecting one Tokyo PoP location (such as **Tokyo_DC2**), all the Tokyo PoP locations are automatically added to the Network Rule. The IP ranges are shared across the Tokyo PoP locations and ensure a seamless experience for accounts.
- NAT - Lets you egress traffic via a specific [Cato allocated IP address](/v1/docs/allocating-ip-addresses-for-the-account) and its PoP location. Traffic that matches this rule is translated to that IP and egressed via the relevant PoP. Both NAT and Route via route traffic via a specific PoP, however, NAT lets you specify the IP the traffic is translated to.
- Backhaul via - Egresses the Internet traffic via one or backhauling gateway sites

For more information, see these articles about [Internet Traffic Backhauling](/v1/docs/internet-traffic-backhauling).

**Note:** Sometimes, all the egress IPs in the Network Rule are not available, such as during the [PoP maintenance window](/v1/docs/understanding-rollout-to-the-cato-cloud), and the PoP uses a different IP address for the traffic flow. This scenario can impact user connectivity and experience. We recommend that you define multiple egress IPs for a rule to minimize the impact.

For **Route via** and **NAT**, when you configure multiple egress IPs, the traffic uses the egress IP for the PoP location that is closest to the source.

**Routing Method NAT - Preserving the Source Port**

By default, when the PoP performs NAT on the Internet traffic, it modifies the source port and source IP in the IP header. In some cases, an application requires preserving the original source port in the IP header, for example, SIP traffic. When you select the **Preserve source port** option, the PoP preserves the original source port in the translated packet IP header.

![Routing_Method_Preserve_Source_Port.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27760846568093(1).png)

**Note:** If there is more than one flow with the same source port, this creates a conflict in preserving the source port for both flows during the NAT translation. In such scenarios, the PoP preserves the source port of the first flow and allocates a random port for the later flow.

**To set the Routing Method for an Internet Network Rule:**

1. From the navigation menu, click **Network > Network Rules**.
2. Click the network rule. The **Edit Network Rule** panel opens.
3. Expand the **Configuration** section.
4. From the **Route/NAT** drop-down menu, select the routing option for traffic that matches the rule:
  - **Route Via** - to route traffic via a specific Cato Cloud PoP location, select the **Locations** which you are egressing traffic from.
  - **NAT** - to egress traffic for this rule via a specific IP via NAT, select the **Allocated IPs** that you are egressing traffic from.

**(Optional)** To use the original source port for the translated traffic, select **Preserve source port**.
5. Click **Save**. The panel closes, and the settings are updated in the policy. The changes are saved to your unpublished revision and are available for editing until they are published or discarded.
6. Click **Publish**. A confirmation window opens, click **Publish**.

### Routing with PoPs for 10Gbps Throughput

For sites that are connected to PoP locations that [support 10Gbps throughput](/v1/docs/pop-locations-supporting-10gbps), we recommend that you configure **Route Via** or **NAT** Network Rules to egress traffic via another 10Gbps PoP location. Otherwise, there can be an impact on the site throughput.

## Viewing Events for a Rule

You can show the events for a specific Network Rule using **View Rule Events**. When you select this action, the Events page opens and is pre-filtered for all events that match that rule.

**To view events for a rule:**

1. From the navigation menu, click **Network > Network Rules**.
2. On the right side, click ![more.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27760850175005(1).png) and select **View Rule Events**.

The Events page is displayed with the events for the relevant rule already filtered.

![rule-event.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32587987871517(1).png)

## Customizing the Acceleration & Optimization for a Rule

- TCP acceleration does not affect non-TCP traffic (UDP-based traffic) that is part of a network rule.
- When **Route/NAT** settings or TLS inspection is in effect, it implies that Cato enables TCP proxy on the traffic.
- The implicit network default rule for the Cato Cloud is to act as a TCP proxy. As such, if no prior rule matches the traffic, the TCP proxy is applied.
- TCP Acceleration is disabled (grayed out) for rules that use Alternative WAN as the primary or secondary transport.

For more about accelerating traffic in the Cato Cloud, see [Accelerating and Optimizing Traffic](/v1/docs/accelerating-and-optimizing-traffic).

For more about packet loss mitigation, see [Packet Loss Mitigation for Multi-Tunnel Links](/v1/docs/packet-loss-mitigation-for-multi-tunnel-links).

**To set the acceleration and optimization for a rule:**

1. From the navigation menu, click **Network > Network Rules**.
2. Click the network rule. The **Edit Network Rule** panel opens.
3. Expand the **Configuration** section.
4. Select **Active TCP Acceleration** to enable the PoP to act as a TCP proxy server for traffic that matches this rule.
5. Select **Packet Loss Mitigation**, to enable packet duplication to help mitigate the impact of packet loss for traffic that matches this rule.
6. Click **Save**. The panel closes, and the settings are updated in the policy. The changes are saved to your unpublished revision and are available for editing until they are published or discarded.
7. Click **Publish**. A confirmation window opens, click **Publish**.

## Adding an Exception

You define traffic that is an exception to the Network Rule, and the rule is not applied to that traffic. Define the traffic exception with the object (entity) for the Source, App/Category, and Destination. Exceptions with multiple objects have the same behavior as Network Rules, see above [Working with Multiple Objects in a Single Rule](/v1/docs/configuring-network-rules#h_01KRV16WDXGENTR6DCSYC3YBAG).

![NetworkRuleExceptions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27760846872093(1).png)

The example above has a network rule for any traffic that matches the VoIP Video category. There is an exception to this rule for traffic that matches BOTH of these conditions:

- Source is the **sample 1500 site**
- Application is **Skype and MS Teams**

**To add an exception to a network rule:**

1. From the navigation menu, click **Network > Network Rules**.
2. Identify the rule that you're creating an exception to, and from the end of the rule, click the more icon ![more.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27760850175005(1).png) and select **Add Exception**.
3. Define the exceptions for the section:
  1. From the drop-down menu, select the traffic type for the exception.

The example below shows adding an exception for a specific host.

![addException.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32587987971357(1).png)
  2. Select a specific object from the drop-down list for that type.
  3. Repeat the previous two steps to define additional objects for the exception.

Multiple objects in one section have an OR relationship.
4. If necessary, repeat step 3 to define exceptions for the other sections.

Objects in multiple sections have an AND relationship.
5. Click **Save**. The panel closes, and the settings are updated in the policy. The changes are saved to your unpublished revision and are available for editing until they are published or discarded.
6. Click **Publish**. A confirmation window opens, click **Publish**.

## Exporting Network Rules to a CSV File

You can generate a CSV file that contains all the data of the network rules per the rulebase of your account.

**Note:** Only CMA admins with **Editor** role have permissions to export to a CSV file. For more about configuring admin roles, see [Managing Administrators](/v1/docs/managing-admins).

**To export the Network Rule policy:**

1. From the navigation menu, click **Network > Network Rules**.
2. Click **Export**, and in the pop-up window click **OK**.
3. Select the location for the CSV file and save the file.

### Understanding the Contents of the Exported File

The top row in the exported CSV file lists the field names and options for rules in the relevant rulebase. Then the rules themselves are listed according to priority, starting with the lowest number value.

The CSV file contains the following columns:

| Item | Description |
| --- | --- |
| Priority | Rule priority within the rulebase |
| Rule Status | Rule is enabled or disabled |
| Type | Rule type is WAN or Internet |
| Name | Name of the network rule |
| Source | Traffic source for this rule |
| App/Category | Items that apply to this rule (apps, categories, services, etc.) |
| Destination | Traffic destination for this rule |
| BW Priority | The BW Management profile for this rule |
| Routing | The routing type applied for this rule (NAT, Backhauling, etc.). Relevant only for **Internet** network rules |
| Transport | The transport type for this rule (WAN interface transport, primary and secondary transport) |
| Acceleration & Optimizations | Optimization settings are enabled or disabled (TCP Acceleration and Packet Loss Mitigation) |

## Limitation

QoS is not applied to app connector traffic. You can't define a bandwidth profile and Network Rules for the traffic, and it is assigned the lowest network priority.
