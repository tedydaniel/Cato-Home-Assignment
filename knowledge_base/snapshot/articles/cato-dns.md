---
title: "What is Cato DNS?"
slug: "what-is-cato-dns"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/what-is-cato-dns"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is Cato DNS?

This article explains how DNS works with the Cato Cloud, and how you can use the Cato DNS server or trusted public DNS servers and internal DNS servers with your account

## Overview

Cato can provide DNS services for your account and act as the DNS server. When a DNS query is sent from behind a Socket, IPsec site, or the Cato Client, the PoP intercepts, inspects, and tries to resolve the query using its own DNS cache. If there is no DNS cache entry for the query, the PoP forwards the query to one of its global trusted DNS servers.

To use the Cato DNS server, no changes are required in the Cato Management Application (CMA). By default, Cato provides DNS service for your account and acts as your DNS server. Cato uses the following DNS servers:

- Primary server: 10.254.254.1 (Cato DNS server)
- Secondary server: 8.8.8.8 (Google DNS server)

These configurations are applied if no DNS servers are configured on the **DNS Settings** page.

You can configure the DNS settings so that your account uses private DNS servers. Using the Cato DNS service provides security protections and advantages. The service processes all DNS requests and generates the responses, which allows Cato to inspect the requests based on your DNS protection configuration. If required, the DNS queries are securely forwarded to trusted global DNS providers which include 8.8.8.8, 1.1.1.1, and 9.9.9.9.

> [!NOTE]
> Note:
> 
> No firewall events are generated for DNS traffic to the Cato DNS server (10.254.254.1).

You can also use the CMA to configure Cato to resolve private DNS servers.

### Trusted and Untrusted DNS Servers

Global DNS services that are verified as secure, are treated by Cato as trusted DNS servers. Other DNS providers are considered as an untrusted DNS server. The DNS behavior is different for trusted and untrusted DNS servers. For more information, see [Using Trusted DNS Servers](/v1/docs/using-trusted-dns-servers).

### DNS Settings for Remote Users

When a remote user connects to your network, your account DNS settings are applied. You can apply specific DNS settings for users or user groups using the [DNS Policy](/v1/docs/centralized-management-of-sdp-user-dns-settings-with-the-dns-settings-policy).

#### DNS Settings in Office Mode

When the Client is used in an office that is behind a Cato Socket or IPsec site, it automatically enters Office Mode. It connects to the site without using the encrypted tunnel. In this scenario, devices use the DNS settings configured in the account or site. If a user defines a local DNS server on their device, the local DNS server will be used instead.

#### Always-On Bypass Mode

The Always-On policy defines rules for when the Client always connects to the Cato Cloud. If Always-On is bypassed, devices use the local DNS settings since traffic is not routed to the Cato Cloud.

## Handling DNS Queries

When a PoP receives a DNS query from a Socket DTLS tunnel, IPsec tunnel, or Cato Client tunnel, the PoP checks the destination IP address of the query. When the query destination IP address matches a trusted DNS server, then the PoP checks if [DNS Forwarding](/v1/docs/defining-dns-forwarding-rules) is enabled for the account. Then the PoP forwards the query to the configured DNS server(s).

For accounts that don't use DNS Forwarding, the PoP tries to resolve the query using its own DNS cache. When the PoP can resolve the query, it generates a DNS response. If there is no DNS cache entry for the query, the PoP forwards the query to one of its global DNS servers, and performs the following actions:

1. The PoP modifies the query destination IP address from a trusted DNS server to the global DNS server IP address. The UDP port isn't changed.
2. The PoP performs SNAT on the source IP address of the query to its own public IP address (Cato’s public range), thus hiding the source organization.
3. When the PoP receives the DNS response from the global DNS server, it modifies the source and the destination IP addresses to the original values and forwards the response back to the source. The PoP caches the A or CNAME type responses that it receives from the global DNS servers and their TTL is enforced.

If the destination IP address for the DNS query **does not** match a trusted DNS server, and there is no internal DNS server defined, then the PoP sends this query to its destination IP address as regular WAN or Internet traffic. The query Destination IP isn't changed.

For public DNS queries, the PoP uses NAT to translate the source IP address to one of Cato’s public range IP addresses. In this case, the PoP does not perform DNS forwarding or DNS response caching.

The amount of time that DNS queries are maintained in the PoP's cache depends on the TTL from the DNS server. For example, for a DNS record with a TTL of 86400 will be cached for 24 hours.

If DNS forwarding is enabled, the PoP does not cache DNS responses.

> [!NOTE]
> Note:
> 
> Cato Networks doesn't support the following DNS types:
> 
> - DNS over TLS
> - DNS over HTTPS

### Working with Hierarchy for DNS Settings

You can configure the DNS settings on different objects in the CMA, for example: settings for the entire account, and for specific groups. When there is a conflict between these objects, the precedence is for the entity closest to the host for the user:

1. Users - closest to the host and highest precedence
2. Sites
3. Groups
4. Account - lowest precedence

In other words, if there are different DNS settings for a site and the account, the DHCP settings for the site are used because the site has higher precedence than the account.

DHCP options take precedence over and override the DNS settings for the account, group, site, or user.

### Configuring DNS Settings for the Account

You can configure the following DNS settings for the entire account:

- DNS settings and suffixes
- DNS forwarding (see [Defining DNS Forwarding Rules](/v1/docs/defining-dns-forwarding-rules))

![DNS_Relay.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33512473503901.png)

> [!NOTE]
> Note:
> 
> You can replace the Cato Cloud default servers with custom DNS servers. In this case, the following DNS records need to be added to your DNS servers to maintain service functionality:

- `vpn.catonetworks.net` - 10.254.254.5 (or the customized reserve service range x.y.z.2 IP address)
- `tunnel-api.catonetworks.com` - 10.254.254.3 (or the customized reserve service range x.y.z.7 IP address)

However, for custom DNS servers that send traffic over the Cato Cloud, you don't need to add these DNS records. The PoPs can resolve the DNS queries for the custom servers.

## Cato DNS Security Protection

Cato's IPS service includes DNS Protection that analyzes DNS requests and responses and provides protections based on reputation, behavioral signatures, and heuristics. Malicious DNS requests are blocked before there is a connection between the host and the malicious server (no TCP or UDP handshake).

Cato provides various types of DNS Protection, for example, Malicious Domains, phishing campaigns, DNS tunneling, and more. For more information, see [Customizing the DNS Protections for IPS](/v1/docs/customizing-the-dns-protections-for-ips).
