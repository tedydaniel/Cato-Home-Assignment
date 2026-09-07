---
title: "Defining DNS Forwarding Rules"
slug: "defining-dns-forwarding-rules"
updated: 2026-07-21T07:55:44Z
published: 2026-07-21T07:55:44Z
canonical: "knowledge.catonetworks.com/defining-dns-forwarding-rules"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Defining DNS Forwarding Rules

## Overview

You can configure DNS Forwarding rules to forward any DNS queries with the specified domain names to resolve with a private DNS server (instead of Cato's DNS server). For example, sometimes mobile users need to connect directly to the Cato Cloud instead of going through one of your internal servers or sites.

In the case of multiple DNS Forwarding rules for the same domain, Cato prioritizes the most specific rule. In the example below, the domain **s1.example.local** is prioritized over **example.local**.

![dns-forward.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28135184559133.png)

If multiple IP addresses for the DNS forwarding servers are configured, the DNS request is sent to all the DNS servers defined in the rule. The first response received is used to resolve the query.

### Notes for Using DNS Forwarding with Cato

- You can use DNS forwarding either with Cato's default DNS server or trusted DNS servers such as 8.8.8.8, 1.1.1.1, and 9.9.9.9. For more about trusted DNS servers, see [Using Trusted DNS Servers](/v1/docs/using-trusted-dns-servers).
- DNS Forwarding can be applied to both external and internal IP addresses and domains.
- DNS Forwarding can process requests over either UDP or TCP.
- The PoP doesn't store DNS forwarding requests in the cache.
- DoH (DNS over HTTPS) and DoT (DNS over TLS) aren't supported.
- For accounts that use a [custom system range](/v1/docs/working-with-the-cato-system-range):
  - If the DNS query is forwarded to a DNS server on the same site as the host, the PoP translates (NAT) the request and uses x.y.z.1 as the source IP
  - Hosts send DNS queries to x.y.z.3 (the custom system range address that replaces the default range 10.254.254.1)

## Defining DNS Forwarding for the Account

**To define a DNS Forwarding rule:**

1. From the navigation menu, click **Network > DNS Settings**.
2. Click the **DNS Forwarding** tab.
3. Click **New** to add a DNS Forwarding rule. The **Add** panel opens.
4. Enter the **Domain** for the traffic that matches this DNS Forwarding rule.

You can enter one domain per rule.
5. In the **IPs** section, enter the IP address for the DNS server for this rule. Each rule supports up to six DNS servers.
6. Click **Apply**. The rule is added to the DNS Forwarding rulebase.
7. Click **Save**.

## Defining Reverse DNS Forwarding Rules

A reverse DNS request translates an IP address into a domain name. Reverse DNS forwarding allows all reverse DNS queries to be forwarded to a central DNS server that handles reverse lookups, simplifying administration.

A reverse DNS forwarding rule is identified by a backward IP address with the suffix **in-addr.arpa**. The IP portion indicates the octets of an IP address you want to query the hostname for.

> [!NOTE]
> Note:
> 
> When configuring reverse DNS forwarding rules, especially those that cover large or non-specific reverse zones, make sure that the DNS servers you forward requests to can properly resolve or process the reverse lookup queries they receive.

![DNS_reverse.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28135181105181.png)

**To define a reverse DNS forwarding rule:**

1. From the navigation menu, click **Network > DNS Settings > DNS Forwarding**.
2. Click **New**. The Add Rule panel opens.
3. Enter the backward **Domain** for the traffic that matches this DNS Forwarding rule, followed by **in-addr.arpa**.
4. Enter the IP address for the DNS server for this rule. Each rule supports up to six DNS servers.
5. Click **Apply**, and then click **Save**.
