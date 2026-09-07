---
title: "Allowlisting IPS Signatures"
slug: "allowlisting-ips-signatures"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/allowlisting-ips-signatures"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Allowlisting IPS Signatures

This article discusses how to create an allowlist rule to allow traffic with a specific IPS signature to bypass the IPS inspection engine.

## Overview of IPS Allowlisting

The Cato Intrusion Prevention System (IPS) engine inspects WAN and Internet traffic for a variety of network attacks and uses different prevention techniques to protect the network. Some of the IPS protections are based on traffic signatures that define the type of potential network attack. Whenever a traffic pattern matches an IPS signature, the IPS engine applies the IPS policy action to the traffic (block, monitor, or allow).

For the IPS block action, you can use IPS allowlist rules to configure the IPS engine to ignore the matching traffic. For example, you can create an IPS allowlist rule directly from an IPS block event in the Event screen.

> [!NOTE]
> Note:
> 
> Using domain names or FQDNs in an IPS allowlist rule does not apply to all IPS protections and signatures. Instead, make sure to use IP ranges for the rule to allowlist all IPS protections.

### Network Traffic and the IPS Protection Scope

You can create rules to allowlist traffic for the IPS engine according to a specific scope of the network traffic. The traffic from the source (From) and to the destination (To) is only allowlisted according to one of these types of network traffic:

- WAN - WAN traffic between sites and hosts over the Cato Cloud
- Inbound - Traffic from the Internet to the internal customer network
- Outbound - Traffic from the internal customer network to the Internet
- Any - Any network traffic

![AllowList_Rulebase.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303136867613.png)

### Items in an IPS Allowlist Rule

The following table explains the items that you can use to define the settings for an IPS allowlist rule:

| Item | Description |
| --- | --- |
| Name | Name for the IPS allowlist rule. |
| Scope | Protection scope for the traffic that the IPS allowlist applies to. You can't edit the Scope for a rule. |
| Source | Source of the traffic for this rule. |
| Destination | Destination of the traffic for this rule. |
| Protocol/Port | Only applies to traffic that matches the specified protocol and ports. You can define a single port or range of ports for each rule. Use separate rules to define multiple ports, for example one rule for TCP port 80 and a second rule for TCP port 200. |
| Signature ID | The IPS signature that is allowlisted and any traffic that with this signature that matches this rule is allowed by the IPS engine. You can enter **Any** to configure the IPS engine to allow all traffic that matches this rule. |
| Track | When the rule is matched, an event is generated or an email notification alert is sent to the specified list. |
| ![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303166616605.png) | Options to **Enable**, **Disable** or **Delete** |

The following table shows the entities you can configure for the **Source** and **Destination** fields in Allow List rules for each IPS protection scope:

| Rule Scope | Available Entities for Source | Available Entities for Destination |
| --- | --- | --- |
| **Inbound** | **Country** **IP Range** **Remote ASN** **Subnet** **Any** | **Floating Subnet** **Group** **Host** **Interface Subnet** **IP** **Network Interface** **Site** **System Group** **User** **User Group** **SDP User** **Any** |
| **WAN** | **Floating Subnet** **Group** **Host** **Interface Subnet** **IP** **Network Interface** **Site** **System Group** **User** **User Group** **SDP User** **Any** | **Floating Subnet** **Group** **Host** **Interface Subnet** **IP** **Network Interface** **Site** **System Group** **User** **User Group** **SDP User** **Any** |
| **Outbound** | **Floating Subnet** **Group** **Host** **Interface Subnet** **IP** **Network Interface** **Site** **System Group** **User** **User Group** **SDP User** **Any** | **Country** **Domain** **FQDN** **IP Range** **Remote ASN** **Any** |

### Working with the IPS Allowlist Rulebase

The IPS allowlist rulebase contains all the rules that allowlist traffic for the IPS engine. All the matching IPS allowlist rules are applied to the traffic, this behavior is different from the ordered firewall rulebase where only the first matching rule is applied. This means that if a connection matches multiple allowlist rules, then each matching rule generates an event.

For example, a connection with a blocked IPS signature matches IPS allowlist rules 2 and 4. The connection is allowlisted and allowed by the IPS engine. The connection generates two separate events, one for rule 2 and one for rule 4.

## Creating an IPS Allowlist Rule from a Block Event

You can use Event Discovery to identify the IPS signature that is blocking traffic and then create an IPS allowlist rule from the block event. You can click the signature ID in an event to open a window that lets you configure the settings for a new IPS allowlist rule. The rule is then added to the IPS allowlist rulebase in the IPS policy (**Security > IPS**).

**To create an IPS allowlist rule from an event:**

1. From **Home > Events**, show the IPS event for the blocked traffic. This is a sample procedure to show an IPS event:
  1. From the **Select Preset** drop-down menu, select **IPS**.
  2. Locate the event for the IPS signature ID.
  3. Expand the event.
2. In **signature id**, click the link for the signature.

The **New Allow List** panel opens. The settings for the rule are based on the data for the the event.

![IPS_allow_from_event.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303150843549.png)
3. Review the settings for the IPS allowlist rule. The **Scope** matches the **traffic direction** for the event and you can't change it.
4. In the **Track** section, you can choose to generate an **Event** and **Email Notification** when this signature is allowed.
5. Click **Save**. The rule is added to the IPS allowlist rulebase.
6. To show the IPS allowlist rulebase, from the navigation menu click **Security > IPS** and select the **Allow List** tab.

## Managing IPS Allowlist Rules

Use the **IPS Allowlist** section in the **IPS Policy** screen to manually create, edit, and delete IPS allowlist rules.

### Showing the IPS Allowlist Rulebase

The IPS allowlist rulebase is in the **IPS Policy** page.

**To show the IPS allowlist rulebase:**

1. From the navigation menu, click **Security > IPS**.
2. Select the **Allow List** tab. The IPS allowlist rulebase is displayed.

### Manually Creating an IPS Allowlist Rule

You can add a new rule to the IPS allowlist rulebase and define the settings for the rule. You can't edit the scope of a rule.

The IPS Signature ID is a custom signature that Cato uses for the IPS engine. You can only see the Signature IDs in IPS events.

**Allowisting IPS Geo Restriction Traffic**

If you need to create allowlist rules for the [IPS Geo Restriction policy](/v1/docs/configuring-the-ips-policy), then you need to define an **IP Range** in the **Destination** field. If the rule is defined based on a **Domain**, the traffic doesn't bypass the IPS inspection engine. An alternative method of applying geo restrictions based on domains is with the Internet Firewall. For more information, see [Internet and WAN Firewall Policies – Best Practices](/v1/docs/recommendations-for-internet-and-wan-firewall-policies).

**To manually create an IPS allowlist rule:**

1. From the navigation menu, click **Security > IPS**.
2. Click **New**. The **New Allow List** panel opens.
3. Enter the **Name** for the rule.
4. Select the **Scope** of the rule.
5. Define the **Signature ID** for the rule, see above [Items in an IPS Allowlist Rule](/v1/docs/allowlisting-ips-signatures#items-in-an-ips-allowlist-rule).

If you set **Signature ID** to **Any**, then the IPS engine allows all matching traffic.
6. Click **Apply**. The IPS allowlist rule is added to the rulebase.
7. Click **Save**.
