---
title: "Configuring Remote Port Forwarding for the Account"
slug: "configuring-remote-port-forwarding-for-the-account"
status: "update"
updated: 2026-09-06T10:29:16Z
published: 2026-09-06T10:29:16Z
canonical: "knowledge.catonetworks.com/configuring-remote-port-forwarding-for-the-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Remote Port Forwarding for the Account

Remote Port Forwarding (RPF) lets you direct an inbound connection from the Internet through the Cato Cloud to an internal LAN host. The connection then benefits from the different Cato security services.

> [!NOTE]
> **Note:** RPF isn't supported for PoPs that are located in China. You can't choose an Allocated IP for these Chinese PoPs.

## Overview of Remote Port Forwarding with Cato

You can control inbound access control to RPF resources using either an allow-list approach or a block-list approach:

- Allow List – blocks all sources (IP addresses and ranges) and only ALLOWS sources that are specifically configured
- Block List - allows all sources (IP addresses and ranges) and only BLOCKS sources that are specifically configured

The block list approach is recommended for situations where you need to control access to Internet-facing RPF resources and the allowed sources are not known or defined. This approach provides an option to configure a list of blocked sources via the Cato Management Application or an API. The block list may be based on customer-maintained block-lists, private security feeds, specific geo records, and indicators from 3rd party systems.

> [!NOTE]
> **Note:** The Cato IPS service protects inbound RPF traffic, however TLS inspection isn't performed on inbound traffic. This means that IPS can’t inspect content for the encrypted traffic, but IPS inspects traffic based on reputation checks (such as scanners, portsweepers, known C&Cs, and so on).

### Anti-Spoofing Protections in the Cato Firewall

One of the basic functionalities of an NGFW is to protect against anti-spoofing attacks. The security engines in the Cato Cloud implicitly drop any connection where the source IP is outside the scope of the configured entity (such as site, network range, device, or user). This blocks anti-spoofing attacks and prevents violations of the configured logical topology.

### Policy Revisions and Concurrent Editing by Multiple Admins

The Remote Port Forwarding policy lets different admins edit the policy in parallel. Each admin can edit rules and save the changes to the rulebase in their own private revision, and then publish them to the account policy (the published revision). For more information on how to manage policy revisions, see [Working with Policy Revisions](/v1/docs/working-with-policy-revisions).

### Understanding the Autonomous Insights

![RPF_auto.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27286731779869(1).png)

The Remote Port Forwarding Insights are a list of [best practices](/v1/docs/reviewing-posture-checks-for-your-account) that evaluate your Remote Port Forwarding policy and show how they comply with Cato’s recommendations. Following these recommendations optimizes your firewall configurations and improves security posture.

There are two types of insights:

- Star icon (powered by AI): Enabled rules in your Remote Port Forwarding policy are automatically analyzed by Artificial Intelligence (AI) to detect issues, for example, rules that can be discarded or modified such as:
  - **Expired Rule** or **Rule with Future Expiration Date:** Rules created to address a specific need and have a desirable cutoff date that has already passed or that has not yet been reached or cannot be proven/evaluated.
  - **Temporary Rule:** Introduced as a short-term solution to address an immediate need. These rules are mostly created to function temporarily while a proper or permanent solution is being deployed or developed.
  - **Testing Rule:** Rules explicitly created for validating, debugging, or experimenting with a specific feature or scenario.
- **Configuration-based:** The configurations and settings in your Remote Port Forwarding policy are to ensure they follow best practices.

### Working with the Remote Port Forwarding Configuration Wizard

The Remote Port Forwarding Wizard autonomously reviews your policy using these checks and insights. When a check fails, you can review and update your policy directly in the Wizard without editing individual rules. This helps you stay secure while simplifying policy management. For more information, see [Using the Configuration Wizard](/v1/docs/using-the-configuration-wizard).

## Enabling Remote Port Forwarding

**To enable Remote Port Forwarding:**

1. From the navigation menu, click **Security > Remote Port Forwarding**.
2. Click the **Disabled** slider. The slider is green to indicate that RPF is enabled.
3. Click **Save**. RPF is now enabled for the account.

## Defining Remote Port Forwarding Rules

The **External IP** for an RPF rule is a Cato allocated IP address. For more information, see [Allocating IP Addresses for the Account](/v1/docs/allocating-ip-addresses-for-the-account). For internal applications, use the Internal IP and port in the rule.

When you define an RPF rule, there are different options for the **Allowed Remote IPs** setting:

- Enter a specific IP address or an IP range in one of these formats:

You can also paste a comma separated list with multiple IP addresses and ranges, for example: 10.1.1.1, 10.2.1.1-10.2.1.105
  - Range of IP addresses - 192.0.2.10-192.0.2.20
  - Subnet (CIDR) - 192.0.2.0/24
- Enable tracking and notifications.

If your network requires mapping from multiple external ports to a single internal port, it is possible to configure this by creating multiple RPF rules.

The mapping for the external to internal ports is specific one-to-one mapping based on the order of the **External** and **Internal Port Range**. For example, the External Port Range 5000-5005 is mapped to the Internal Port Range 6103-6108. This means that external port 5000 is mapped to internal port 6103, external port 5001 is mapped to internal port 6104, and so on.

![RemotePortForwarding.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27286767493533(1).png)

> [!NOTE]
> **Note:** For accounts with IPsec sites, if the external IPs of an RPF rule overlaps with the IP addresses of an IPsec site, make sure that the rule excludes the IPsec tunnel ports UDP/500 and UDP/4500.

**To define a Remote Port Forwarding rule:**

1. From the navigation menu, click **Security > Remote Port Forwarding**.

The Remote Port Forwarding page opens to your existing unpublished revision, or to the newest published revision.
2. Click **New**. The **Add Rule** panel opens.
3. Enter the **Name** for the rule.
4. **(Optional)** Select **Forward ICMP** to enable forwarding ICMP messages for this rule.
5. Select the **Allowed Protocols** for the rule.
6. Select the protocols you want to allow for this rule.
7. In the **External** section, define the Cato allocated **External IP** and **External Port Range** for the ports monitored by the PoP.
8. In the **Internal** section, enter the **Internal IP** address to which the traffic is forwarded and the **Internal Port range**.
9. In the **Remote IPs** section, select if this rule is an **Allow List** or **Block List**.
  1. To define the only traffic that is ALLOWED to connect to the host:
    1. Select **Allow List**.
    2. Select the **Traffic Sources** based on the **IP Range**, **Subnet,** or **Country**. These are the IP addresses and ranges that are allowed to perform RPF to the host.
    3. Click ![add.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27286731883421(1).png) (Add) to add more allowed remote IPs.
  2. To allow all traffic to this host, and define sources that are BLOCKED and can't connect to it:
    1. Select **Block List**.
    2. Select the **Traffic Sources** based on the **IP Range**, **Subnet,** or **Country**. These are the IP addresses and ranges that are blocked and can't perform RPF to the host.
    3. Click ![add.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27286731883421(1).png) (Add) to add more blocked remote IPs.
10. **(Optional)** Define email notifications, for the traffic that matches the rule. For more information, see [Account Level Alerts and System Notifications](/v1/docs/account-level-alerts-and-system-notifications).
11. Click **Apply**. The rule is added.
12. Click **Save**.

The changes are saved to your unpublished revision and are available for editing until they are published or discarded.
