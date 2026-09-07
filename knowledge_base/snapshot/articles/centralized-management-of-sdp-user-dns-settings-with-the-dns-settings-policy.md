---
title: "Centralized Management of SDP User DNS Settings with the DNS Settings Policy"
slug: "centralized-management-of-sdp-user-dns-settings-with-the-dns-settings-policy"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/centralized-management-of-sdp-user-dns-settings-with-the-dns-settings-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Centralized Management of SDP User DNS Settings with the DNS Settings Policy

This article explains how to manage the DNS settings of the SDP users in your account.

## Overview

By default, Cato Networks provides DNS service for your account and acts as your DNS server. You can use the Cato Management Application to configure Cato to resolve private DNS servers.

When the DNS servers are configured for the entire account, the DNS server in the Cato Cloud attempts to resolve every DNS query sent over the Cato network. If the DNS query is not resolved, then Cato Cloud uses authoritative DNS to resolve the query. As a best practice, we recommend that you configure two different DNS servers to offer the best security, performance, and redundancy.

For more information about DNS settings for the entire account, see [Configuring DNS Settings](/v1/docs/configuring-dns-settings).

In addition to the default account DNS settings, the DNS Settings Policy lets you define different DNS settings for SDP users or groups. The DNS settings are applied from an ordered rulebase.

### Use Case

A company has Product Managers who are members of both the **Product** user group and the **R&D** user group. Product Managers are required to use the account level DNS settings, while R&D engineers need access to specific DNS servers.

The company creates the following rules within the DNS Setting policies:

![Example_DNS_Policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218253780637.png)

- **Product Managers** - this rule contains the Product user group and assigns the account DNS settings
- **R&D** - this rule contains the R&D user group and has manually configured DNS settings

The DNS Settings policy rule for the Product Managers is higher than the R&D rule. The Product Managers first match the Product rule and receive the account DNS settings.

### Known Limitations

DNS Forwarding is not supported if you override Account Level DNS settings

## Defining SDP User DNS Settings

The **DNS Setting Policy** provides you with a central location to manage the DNS settings across your account. You can apply the account level DNS settings or define different DNS settings for SDP users, User groups, or operating systems. If a SDP user or device does not match any rule, the account DNS settings are applied by an implicit rule.

For more information about configuring DNS with Cato, see [Best Practices for DNS and Your Cato Account](/v1/docs/best-practices-for-dns-and-your-cato-account).

### Working with the Ordered DNS Settings Policy

The **DNS Settings Policy** is an ordered rulebase that sequentially checks if a SDP user and/or operating system match the rules defined in the policy. Once a SDP user or device matches a rule, the DNS settings defined in the rule are applied. Rules that are listed in the policy after the matching rule are not applied. If a SDP user or device does not match any rule, the account DNS settings are applied by an implicit rule.

You can apply the account DNS settings within a rule. This lets you apply the account DNS settings to SDP users or operating systems and create additional lower ranked rules.

### Using SDP User DNS Settings in Office Mode

An SDP user with DNS settings defined in the **DNS Settings Policy** that connects to the Cato Cloud in an office that is behind a Cato Socket or IPsec site, receives the DNS settings for the site.

For configurations where the private DNS server is located on the local LAN, then the static DNS entry and the connectivity over the local LAN means that the users are always identified as being connected with office mode. If the site (and the users in Office Mode) are not connected to the Cato Cloud but are connected to the Internet, because the users have connectivity to the private DNS server, the Client won’t be able to connect to the Cato Cloud.

For more information about Office Mode, see [Configuring Office Mode](/v1/docs/configuring-office-mode).

### Using the DNS Settings Policy with DNS Forwarding

DNS Forwarding rules forward any DNS queries with the specified domain names to resolve with a private DNS server. To use DNS Forwarding, make sure that the DNS queries transit the Cato Cloud and are resolved by a ​[trusted DNS server​](/v1/docs/using-trusted-dns-servers).

For more information about DNS Forwarding rules, see [Defining DNS Forwarding Rules](/v1/docs/defining-dns-forwarding-rules).

### Configuring the DNS Settings Policy

Use the DNS Settings Policy to manage your DNS settings.

![DNS_Policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218259675549.png)

**To configure the DNS settings policy:**

1. From the navigation menu, click **Access > DNS settings Policy**.
2. Click **New**.

The **New DNS Settings Policy Rule** panel opens.
3. Enter a **Name** for the rule.
4. Define the **Users & Groups**, **Platforms**, and **DNS Settings**.
5. Click **Apply**.
6. Repeat steps 2-5 for each rule in the DNS Policy.
7. Enable the **DNS Settings Policy** and then click **Save**.

The slider is green when the rule is enabled, and gray when the rule is disabled.
