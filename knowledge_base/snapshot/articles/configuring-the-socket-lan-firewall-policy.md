---
title: "Configuring the Socket LAN Firewall Policy"
slug: "configuring-the-socket-lan-firewall-policy"
updated: 2026-07-27T11:35:35Z
published: 2026-07-27T11:35:35Z
canonical: "knowledge.catonetworks.com/configuring-the-socket-lan-firewall-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring the Socket LAN Firewall Policy

> [!NOTE]
> Note:
> 
> **Upcoming Automatic Migration of Site LAN Firewall Rules to Account-Level Policy**
> 
> We recently released the [Socket Next Gen LAN Firewall](/v1/docs/what-is-the-socket-next-gen-lan-firewall) that provides account-level configurations and Layer 7 enforcement. Starting July 1, 2025, we will migrate existing site-level LAN firewall rules to the account-level policy.
> 
> - Each site-level rule will automatically be configured in the new policy as a Network rule to specify the routing, and a Firewall rule to allow or block the traffic
> - The rules for each site will be added as a separate section in the rulebase
> - The migration is a seamless, automatic process and no service disruption is anticipated
> - If you're interested in migrating your policy before July 1, please contact [ea@catonetworks.com](mailto:ea@catonetworks.com)

## Overview

The default behavior for the Socket is to forward all WAN and Internet traffic to the PoP for security inspection. This includes LAN traffic between adjacent network segments within a site (e.g. VLANs). In some scenarios, you may want to override the default behavior and configure the Socket in a site to allow or block communication between two network segments or hosts, directly on the Socket, without sending the traffic to the Cato PoP. With the LAN Firewall policy, you can configure rules for allowing or blocking LAN traffic directly on the Socket. Optionally, you can enable tracking (events) for each rule.

**Note:** The LAN Firewall is an enhancement to the Local Routing policy. For more information see below [Prerequisites for Using The LAN Firewall](/v1/docs/configuring-the-socket-lan-firewall-policy#prerequisites-for-using-the-lan-firewall) and [Upgrading the Local Routing Policy to the LAN Firewall](/v1/docs/upgrading-the-local-routing-policy-to-the-lan-firewall).

## Understanding the LAN Firewall

The LAN Firewall allows you to block or allow certain types of traffic at the Socket level, by creating policies according to your needs.

The following diagram below shows a LAN Firewall rule that allows traffic from LAN1 to LAN2.

| ![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247905661725.png) |
| --- |

This diagram shows a LAN Firewall rule that blocks traffic blocks traffic from LAN1 to LAN2.

| ![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247937280413.png) |
| --- |

### Using the LAN Firewall - Sample Rulebase

The following is a LAN Firewall configuration rulebase sample. Each rule is explained below:

| ![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247923234589.png) |
| --- |

Rule **1** - 'Block guest' - This rule prevents hosts who are using the '**Guest-Wifi**' network from accessing **any** other hosts or internal resources in the site while tracking these events. The hosts can still access the internet.

Rule **2** - 'Allow file share' - This rule allows only hosts connected to the '**Corp-Users**' network to connect to servers in the '**File-Servers**' local network over **HTTPS** or **SMB (TCP/445)**. Each flow is tracked in the events. With this allow locally policy, tunnel overhead for SMB and HTTPS between the networks is decreased since traffic is managed locally on the site and does not traverse the tunnel.

Rule **3** - 'Allow CCTV server' - This rule allows hosts from the '**IOT-Cameras**' network to connect to the '**IOT-File-Servers**' network over **HTTPS** only. Each flow is tracked in the events.

Implicit behavior - **Any** other host traffic that is **not** defined in the rulebase will be sent to the Cato PoP for inspection before reaching back to '**File-Servers**'. For example, any traffic from '**Corp-Users**' to '**File-Servers**' over **TCP/21 (FTP**) will not match the sample rulebase and trigger the default behavior (send traffic to Cato PoP).

### Working with the LAN Firewall Rulebase

The LAN firewall policy is processed in an order from the first to the last configured rule. Once a rule is matched, an action is applied. **Else, traffic is sent to the Cato PoP by default**.

Rules at the top of the rulebase have a higher priority because they are applied to connections before the rules lower down in the rulebase. For example, if a connection matches on rule #3, the action is applied to the connection, and the firewall stops inspecting it. The firewall does not continue to apply rules #4 and below to the connection. You can increase the efficiency of the LAN firewall and give a high priority to rules that match the largest number of connections.

### Throughput for the LAN Firewall

The following table represents supported throughput over the LAN Firewall for each Socket model.

**Note:** The values represented below are based on Socket v19.0 uni-dimensional tests in a lab environment.

| Socket Model | TCP BW | UDP BW |
| --- | --- | --- |
| X1500 | up to 1Gb/sec | up to 2Gb/sec |
| X1600 | up to 8Gb/sec | up to 8.5Gb/sec |
| X1700 | up to 10Gb/sec | up to 12Gb/sec |

## Prerequisites for Using The LAN Firewall

The LAN Firewall is an enhancement of the existing Local Routing policy. This feature is enabled **per site**.

Make sure that all Sockets in the site are running Socket version 18.0 or higher.

### Upgrading the Local Routing Rules to the LAN Firewall

- If there are no Local Routing rules configured for the site, you can immediately upgrade it to the LAN Firewall policy
- If there are Local Routing rules configured for the site, migrate the Local Routing rules to the LAN firewall, see [Upgrading the Local Routing Policy to the LAN Firewall](/v1/docs/upgrading-the-local-routing-policy-to-the-lan-firewall)
- After you upgrade to the LAN Firewall, enable the feature (**LAN Firewall Enabled** toggle on the top right of the screen).

When this feature is disabled, all traffic is sent to the PoP.

## Configuring the LAN Firewall

This section explains how to define rules for the LAN Firewall and the objects, ports, and services that you can configure.

### Defining a LAN Firewall Rule

Create a new LAN Firewall rule and configure the settings for the rule to manage routing for the LAN traffic. Use the **Add Rule Below** option to easily add a rule to the correct place in the rulebase.

> [!NOTE]
> Note:
> 
> Applying the new configuration to the Socket may take up to a minute.

**To define a LAN Firewall rule:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > LAN Firewall**.
3. Click **New**. The **Add Rule** panel opens.
4. In the **General** section:
  1. Enter a **Name** for the new rule.
  2. By default, the rule is **Enabled**. You can disable the rule using the **Enabled** toggle.
  3. Under **Direction**, select **To** to enable traffic in one direction only, or **Both** to enable bidirectional traffic.
  4. Choose the **Rule Order**. We recommend that you define a high rule order for **more specific** rules and low rule order for **less specific** rules.

**Note**: Please see the "Working with The LAN Firewall Rulebase" section for more on rule order configuration.

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247912661405.png)
5. Expand the **Source** and **Destination** sections, define the traffic source and destination entities for this rule.
6. Expand the Service/Port section, select the protocols that the rule applies to.
  1. If selected **Port/Protocol**, define the relevant port and protocol as you wish in the "Protocol/Port" format (i.e. TCP/80-88, UDP/53, ICMP etc.)
  2. If selected **Simple Service**, select the relevant Layer 4 services as predicated.

The predefined services list is based on the RFC definition of each service.
7. NAT section:

| ![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247953812381.png) |
| --- |
  1. **Enable NAT** - Optionally, enable NAT on the outgoing interface. This translates all originating IPs to one NAT IP.
8. In the Actions section:

**Note:** If traffic does not match any of the rules, the default action is **Send to PoP**.
  1. **Allow locally** - This action allows matching local traffic between the Socket LAN networks.
  2. **Block locally** - This action blocks matching traffic locally between the Socket LAN networks.
9. In the Actions section under **Track**:
  1. Optionally, enable the **Event** checkbox. When matched, an event is generated for this rule.
10. Click **Apply**, and then click **Save**.

### NAT and LAN Firewall Rules

There are scenarios that require using NAT between the LAN networks within a site, this can be between two (or more) directly connected networks, or between routed networks (static routes or BGP routes).

1. NAT is configurable only in the **To** direction.
2. After you save the configuration for the rule, the Cato Management Application automatically calculates the **Outbound Network** and **Outbound IP** for the rule.

### LAN Firewall Source and Destination Objects

The following source and destination objects can be defined:

- **Global Range** - Native range for the LAN interface of a site.
- **Host** - Hosts and servers defined in the site.
- **Interface Subnet** - VLAN, routed, or direct ranges, or a secondary AWS vSocket native range.
- **Network Interface** - Subnets and network ranges defined for the LAN interfaces of a site.
- **Any** - Any source or destination **within the site.**

### LAN Firewall Services and Ports

The following is a predefined list of available services:

| **Service** | **Port** | **Protocol** |
| --- | --- | --- |
| RDP | 3389 | TCP |
| MYSQL | 3306 | TCP |
| HTTP | 80 | TCP |
| HTTPS | 443 | TCP |
| SSH | 22 | TCP |
| SMTP | 25 | TCP |
| DNS TCP | 53 | TCP |
| DNS UDP | 53 | UDP |

## Monitoring and Events

You can optionally enable event tracking for each defined rule in the LAN Firewall.

> [!NOTE]
> Note:
> 
> LAN firewall traffic will not be visible in app and network analytics dashboards.

The events appear under **Site Monitoring > Events**.

- **Event Type** - Security
- **Sub-Type** - LAN Firewall

**To filter for LAN Firewall events:**

1. Go to **Home** > **Events**.
2. Click on **Filter** and select the relevant field, operator, and value.
  1. **Field** - Multiple fields can be selected as a filter. For example, we may opt to filter for "Source site" or "Sub-Type" (LAN Firewall)
  2. **Operator** - Choose to include or exclude specific values (**Is**, **Is not**) or multiple values (**In**, **Not in**), for example "Source site" with operator "**In**" allows to select multiple source sites as values.
  3. **Value** - The value for the field.
3. Click **Add filter**.

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247954003485.png)

In the following example, you can see the details for a LAN Firewall event.

- **Action** - Block or Monitor. (Traffic was blocked or allowed locally by the LAN Firewall)
- **Configured Host Name** - Additional host information on the source IP, if available.
- **Sub-Type** - LAN Firewall. All events generated by the LAN Firewall will have this sub-type.
- **Rule** - The defined rule name which generated this event.

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247923694493.png)

Unlike the WAN or Internet Firewall, where events are generated by the Cato PoP, LAN Firewall events are generated on the Socket itself. These events are sent over the site tunnel to be stored in the Cato Management Application.

All flow traffic over the tunnel is prioritized before LAN Firewall events, which have a default QoS priority of 255 and may generate additional overhead.

Cato recommends tracking high priority LAN Firewall rules only in order to avoid additional overhead over the tunnel.
