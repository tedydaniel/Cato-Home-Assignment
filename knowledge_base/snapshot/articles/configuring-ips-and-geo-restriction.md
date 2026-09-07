---
title: "Configuring IPS and Geo Restriction"
slug: "configuring-ips-and-geo-restriction"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/configuring-ips-and-geo-restriction"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring IPS and Geo Restriction

## Overview of Cato's IPS Policy

Cato's IPS service is comprised of several layers of security including:

- Behavioral Signatures: Protecting against deviation from normal, expected behavior of the system or the user. Normal behavior is identified using Cato Networks' big data analytics and deep visibility across many traffic flows over the Cato Cloud.
- Reputation Analysis: Protecting against inbound / outbound communication with compromised or malicious resources.
- Known Vulnerabilities: Protecting against known CVEs, rapidly adapting to incorporate new ones.
- Anti-Bot: Protecting against outbound traffic to C&C servers based on reputation feeds, and network behavioral analysis.
- Network Behavioral Analysis: Protecting against inbound / outbound network scans.
- Protocol Validation: Protecting against invalid packet (conformance to the protocol wise), reducing attack surface from exploits using anomalous traffic.
- Geo Restriction: Enforce a custom geo-restriction policy to block inbound, outbound, or all traffic to specific countries.

## Cato's IPS and Geo Restriction

This section is an example of creating IPS policy to block WAN and Inbound traffic. It also contains a geo-restriction policy to block traffic for Iran and North Korea.

**Note:** If you want to block traffic from a country, but allow a specific FQDN, use the Internet Firewall. For more information, see [Recommendations for Internet and WAN Firewall Policies](/v1/docs/recommendations-for-internet-and-wan-firewall-policies).

### Defining the IPS Protection Policy

For WAN, Inbound, and Outbound traffic, you can define the actions for the IPS engine and the relevant email notifications. It is possible that the matching traffic is a false-positive and is actually legitimate traffic.

These are the available actions:

- **Block** - Blocks the traffic and it doesn't continue to its destination. When applicable, redirects the user to a dedicated blocking web page. An event is generated for the Events screen (Home > Events).
- **Monitor** - The traffic is allowed to continue to the destination and an event is generated for the Events screen (Home > Events).

![IPS_Policy_getting_started.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275594973213.png)

**To configure actions for the IPS policy:**

1. From the navigation menu, click **Security > IPS**.
2. In the IPS page, click the **Protection Policy** tab.
3. Click the slider ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275611161629.png) to enable the IPS policy.

The toggle is green ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275611161629.png) when enabled.
4. In the **Protection Policy** section, configure the following settings for each **Protection Scope**:
  1. For WAN traffic, IPS blocks matched protections and generates an email notification:
    1. Click **WAN Traffic**.

The **Edit** panel opens.
    2. In **Action**, from the drop-down menu select **Block**.
    3. In **Track**, select **Email Notification**.
    4. Click **Apply**.
  2. For Inbound Internet traffic, IPS blocks matched protections and generates an email notification:
    1. Click **Inbound Traffic**.

The **Edit** panel opens.
    2. In **Action**, from the drop-down menu select **Block**.
    3. In **Track**, select **Email Notification**.
    4. Click **Apply**.
  3. For Outbound Internet traffic, IPS monitors matched protections and doesn't generate an email notification:
    1. Click **Outbound Traffic**.

The **Edit** panel opens.
    2. In **Action**, from the drop-down menu select **Monitor**.
    3. In **Track**, make sure that **Email Notification** is cleared.
    4. Click **Apply**.
5. Click **Save**. The IPS policy settings are saved for the account.

### Managing Geo Restriction Rules

You can define Geo restriction rules for IPS. Geo restriction rules for IPS are based on the IP address geolocation and not on the domain. You can define the rule to apply to inbound, outbound, or both directions of traffic.

> [!NOTE]
> Note:
> 
> If you configure a Geo Restriction rule for inbound traffic, this applies also to RPF resources. However, IPS Geo Restriction rules are not applied to traffic from Cato SDP Clients. To block Client connections from specific regions, you can configure rules in the Client Connectivity Policy.

![IPS_Geo_Restriction.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275579504925.png)

**To define a Geo restriction rule:**

1. From the navigation menu, click **Security > IPS**.
2. In the IPS page, click the **Geo Restriction** tab or expand the section.
3. Click **New**.

The **Add** panel opens.
4. Enter the **Name** for the rule, and in **Direction**, select **Both Directions** to configure the rule to apply to all traffic.
5. In the **Countries** section, add **Iran** and **Korea, Democratic People's Republic of** (North Korea).
6. In **Action**, select **Block** to block all traffic to and from Iran and North Korea.
7. In **Track** select **Event** and **Email Notification**, to have the maximum visibility for traffic to and from Iran and North Korea.
8. Click **Apply** and then click **Save**.
