---
title: "Bypassing the Cato Cloud (Account Level Policy)"
slug: "bypassing-the-cato-cloud-account-level-policy"
updated: 2026-07-19T11:06:59Z
published: 2026-07-19T11:06:59Z
canonical: "knowledge.catonetworks.com/bypassing-the-cato-cloud-account-level-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bypassing the Cato Cloud (Account Level Policy)

**Note:** Cato is automatically migrating eligible site-level Socket bypass policies to the account-level Socket bypass policy. For more information, see the [FAQ](/v1/docs/bypassing-the-cato-cloud-account-level-policy#faq-automatic-migration-from-sitelevel-policy) below.

## Overview

The Bypass policy lets you define bypass rules for Internet traffic that will directly egress to the Internet instead of being routed to the Cato Cloud. This is an account-level policy that applies globally across all Socket sites in your account. The PoPs in the Cato Cloud don't inspect bypassed Internet traffic or apply security policies. In addition, app or category-based traffic rules enforced in the Cato Cloud are not applied. The Socket continues to apply Bandwidth Profiles and QoS to bypassed traffic in the upstream direction. QoS is not applied in the downstream direction because the PoPs are bypassed.

Bypassed Internet traffic is sent over a Socket WAN interface. An internal Socket mechanism generates a score for each WAN interface, which is calculated each second based on a set of parameters, such as packet loss, jitter, latency, and congestion.

The default behavior is for the Socket to automatically choose the WAN port for the bypass traffic based on the best score. The Socket can select different WAN ports for different flows.

> [!TIP]
> Important:
> 
> - Bypassing Internet traffic is only supported for accounts with all Socket and vSocket sites running Socket v26.0.23517 and higher
> - Bypassed traffic is not included as site traffic for the site bandwidth license

![Bypass_Policy_Account_Level.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33239523031965.png)

### Use Case - Bypassing Windows Update Traffic

Windows Update traffic can consume significant bandwidth and does not always require inspection by the Cato Cloud. To optimize performance, admins configure a Bypass rule with the **Windows Update** predefined application configured as the destination. Windows devices then download updates directly from Microsoft over the local Internet connection

### Prerequisites

- Supported for Socket and vSocket sites with Socket v26.0.23517 and higher

## How the Account Level Bypass Works

### Bypass Rules Based on Predefined Applications

To make it easier to configure application traffic in Socket sites to egress directly to the Internet, you can define rules using predefined applications that include all the relevant destination IP addresses for the application. Cato maintains these predefined applications so that when the application's IP addresses are updated, your policy automatically applies to the new IP addresses. For example, instead of having to configure and keep track of all the public IPs for Zoom, you can simply select the **Zoom** predefined application, and Cato ensures that the correct destinations are bypassed.

### Bypass Rules Based on FQDNs, Domains, and Custom Applications

You can create bypass rules based on FQDNs, domains, and custom applications for granular control over which Internet destinations egress directly from the Socket. By matching traffic on DNS-based identifiers instead of individual IP addresses, you avoid manually tracking changing IP ranges and reduce ongoing maintenance. [Custom applications](/v1/docs/working-with-custom-apps) let you group multiple FQDNs, domains, or IP ranges into a single reusable object, making your policy easier to manage, more readable, and consistent across rules.

### How the Bypass Policy Relates to the Cato Firewall Policies

Traffic that matches a Bypass policy rule is not enforced by Cato firewall policies. Since bypassed traffic is not sent to the Cato Cloud, Internet Firewall, and WAN Firewall rules are not applied to it. Although both the Bypass policy and the Socket Next Gen LAN Firewall are enforced locally on the Socket, they serve different purposes and apply to different types of traffic. The Socket Next Gen LAN Firewall controls east-west traffic and segmentation within the site, while the Bypass policy applies only to traffic that egresses directly to the Internet.

### Policy Revisions and Concurrent Editing by Multiple Admins

The Bypass policy lets different admins edit the policy in parallel. Each admin can edit rules and save the changes to the rulebase in their own private revision, and then publish them to the account policy (the published revision). For more information on how to manage policy revisions, see [Working with Policy Revisions](/v1/docs/working-with-policy-revisions).

## Defining Bypass Rules

Create a bypass rule and configure the settings for the rule to manage which traffic egresses directly to the Internet.

**Preferred Socket Port**

By default, the Socket automatically selects the WAN interface with the best score. Optionally, you can set a **Preferred Socket Port** (for example, **WAN2**). If the WAN scores are similar, the Socket prefers the selected WAN interface (as long as it has connectivity). If it loses connectivity, the Socket selects a different WAN role.

For more about **Source** and **Destination** items for a rule, see [Reference for Rule Objects](/v1/docs/reference-for-rule-objects).

![Bypass_Policy_Account_Level_new_rule.png](https://support.catonetworks.com/hc/article_attachments/33239513326877)

**To define a bypass rule for Internet traffic:**

1. From the navigation menu, select **Network > Bypass**.
2. Click **New** and then from the dropdown select **New Rule**.
3. Enter the **Name** for the rule.
4. Enable or disable the rule using the slider (green is enabled, grey is disabled).
5. Configure the **Position** for the rule in the rulebase.
6. Expand the **Site** section and select the Socket sites and/or groups that the rule applies to. The default value is **Any**.
7. Expand the **Source** section and select one or more objects for the traffic source for this rule.

When there is more than one **Source** object in a rule, there is an OR relationship between them. The default value is **Any**.
8. Expand the **Destination** section and select one or more traffic destinations for this rule.

When there is more than one **Destination** object in a rule, there is an OR relationship between them. The default value is **Any**.
9. Expand the **Service/Port** section and define the simple and/or custom services the rule applies to:

When there is more than one **Service/Port** object in a rule, there is an OR relationship between them. The default value is **Any**.
  - For a **Simple Service**, select the service from the dropdown menu
  - For a **Custom Service**, enter the protocol and port in the format protocol/port. For example, **TCP/80** for a single port, **TCP/80-88** for a port range
10. Expand the Actions section and define the **Preferred Socket Port** and **Tracking** settings.
  - **(Optional)** In **Preferred Socket Port**, select the WAN port the Socket will use as the preferred WAN port for the bypass traffic. When **Automatic** is selected, the Socket determines the optimal port for the Bypass traffic.
  - **(Optional)** Select the **Event** option for the rule to generate events when it is matched by traffic.
11. Click **Save** to save the changes.

The changes are saved to your unpublished revision and are available for editing until they are published or discarded.

## Customizing the Flow Timeout

For Socket and vSocket sites, the default flow timeout is 60 seconds. After this time, there is an idle timeout for the traffic flow, and the Socket closes the bypassed flow.

You can use the Socket WebUI to customize the flow timeout. However, this custom setting is not persistent, and if the Socket reboots, including upgrading to a new version, then it reverts to the default flow timeout of 60 seconds. To permanently configure a custom flow timeout, please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).

**To customize the bypass flow timeout:**

1. Log in to the Socket WebUI:
  1. From the navigation menu, select **Network > Sites**, and select the site.
  2. From the navigation menu, select **Site Configuration > Socket**.
  3. From the **Actions** menu of the socket, select **Socket WebUI**.
2. From the **Cloud Connection Settings** tab, in the **Flow timeout (for bypass flows only)** section, enter the new timeout value.
3. Click **Update**.

## Known Limitations

- FQDN-based bypass relies on DNS-to-IP correlation, which can be imprecise when services are hosted behind CDNs. If multiple hostnames resolve to the same shared CDN IP, this may result in false positive matches to a rule, and traffic for other hostnames may be unintentionally bypassed.

## FAQ: Automatic Migration from Site-Level Policy

Cato automatically migrates eligible site-level Socket bypass policies to the account-level Socket bypass policy.

### Which sites are eligible for automatic migration?

Sites running Socket version 26 or later are eligible for automatic migration.

### Are sites running earlier Socket versions migrated automatically?

No. Sites running Socket versions earlier than version 26 are not eligible for automatic migration.

### What happens to the site-level bypass policy after migration?

After an account migrates to the account-level Socket bypass policy, the site-level bypass policy is deprecated.

### Do admins need to take action?

No action is required for eligible sites. Cato automatically migrates the eligible site-level bypass policies to the account-level policy.

## Article Changelog

| Date | Description |
| --- | --- |
| July 19, 2026 | Minimum Socket version for Account-Level Socket Bypass feature is v26.0.23517 |
