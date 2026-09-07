---
title: "Best Practices for DNS and Your Cato Account"
slug: "best-practices-for-dns-and-your-cato-account"
tags: ["Best Practices", "Networking"]
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/best-practices-for-dns-and-your-cato-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Best Practices for DNS and Your Cato Account

This article contains best practices and recommendations for DNS settings and configurations for your account.

## Improving Network Performance for Internal DNS Servers

For sites in different physical locations, you can achieve better performance by configuring different internal DNS servers for different sites. Alternatively, Cato’s DNS service uses Cato's global PoP locations in the Cato Cloud to provide your hosts with fast and global DNS resolution and can significantly reduce DNS latency. The PoPs store the DNS responses in the cache so that future DNS requests are served more quickly. A host that connects to the Cato Cloud and uses Cato’s DNS services, retrieves the DNS response from the PoP that it’s connected to (usually the closest PoP). Therefore, the DNS response time is very quick and reduces DNS latency.

We recommend that you use Cato’s DNS servers and gain the benefit of the global PoP locations in the Cato Cloud.

For situations that require local DNS servers, you can configure local servers that are physically close to the sites. For example, if you have a site in New York and a site in Singapore, you can use different local DNS servers for each site so that the DNS server in Singapore resolves DNS requests from the clients connected to the Singapore site only. The clients that are connected to the site in New York, don’t need to send DNS requests to the server in Singapore to resolve the query. It’s more efficient and improves the performance of your network.

For more about defining a custom DNS server for a site, see [Configuring DNS Settings](/v1/docs/configuring-dns-settings).

## Setting Primary and Secondary DNS Servers for Failover

Cato recommends that you configure two different DNS servers for redundancy. Set Cato’s default DNS server (10.254.254.1 or x.y.z3 for internal DNS queries) as the primary and a trusted public DNS server as the secondary DNS server. For more information about trusted DNS servers, see [Using Trusted DNS Servers](/v1/docs/using-trusted-dns-servers). If the primary DNS server isn't available, Cato then uses the secondary DNS server to resolve the queries. If you are using an internal DNS server, configure DNS forwarding to resolve internal domains.

> [!NOTE]
> Note:
> 
> DoH (DNS over HTTPS) or DoT (DNS over TLS) does not support DNS forwarding

For macOS users, it’s recommended to only define primary/secondary DNS servers that don’t support DoH or DoT such as 10.254.254.1 or an internal DNS server. Starting with macOS 13 Ventura, the operating system prefers DoH or DoT (not supported by Cato inspection) to resolve DNS queries, which can break Cato DNS forwarding. For more information see [macOS Ventura Users Unable to Reach Internal Resources Via Cato](/v1/docs/macos-ventura-and-ios-users-unable-to-reach-internal-resources-via-cato).

## Working with DNS for Remote Users

Remote users don’t connect through sites but directly to PoPs in the Cato Cloud. Therefore, if the DNS settings are not configured correctly, remote users can experience connectivity problems or can’t access internal resources. For example, if you configure DNS settings for the site rather than for the remote users, the remote users can’t access these internal resources in your domain. The DNS server can’t resolve DNS queries for the Clients since they aren't connected to the site. For this reason, you must configure DNS settings for the Clients to allow this connectivity.

Your account DNS settings are applied to all Sites and remote users. If you have specific DNS requirements for remote users, enable the [DNS policy](/v1/docs/centralized-management-of-sdp-user-dns-settings-with-the-dns-settings-policy).

## Protecting Internal Resources for Guests

Cato recommends that you protect your corporate assets and limit access to internal DNS servers as a best practice. For example, define that people accessing the guest network only use public DNS servers to resolve DNS queries. Create a separate VLAN for the guest network and assign this network to a group of guest users. Then, configure the DNS settings for this group with public untrusted DNS servers only. For more information about trusted networks, see [Using Trusted DNS Servers](/v1/docs/using-trusted-dns-servers).

To do this:

1. Create a guest WiFi network for Sites
2. Create a [group](/v1/docs/working-with-cma-advanced-groups-and-groups) for guest users and assign the guest networks to this group
3. Define an untrusted server for the group

## Connectivity for Remote Users with DNS Forwarding

Cato's DNS Forwarding feature lets you achieve connectivity to local domains in your network.

Remote users usually don’t connect to sites but directly to the Cato Cloud. This means that there is no DNS server to resolve DNS queries for local domains. We recommend that you use DNS Forwarding rules to forward these queries to the relevant DNS internal server. The server resolves the query and lets SDP users connect to corporate internal resources.

DNS Forwarding only applies to DNS requests that are sent to a trusted DNS server (DNS servers configured for your account are considered trusted).

You can configure custom DNS settings for Sites or [User/User groups](/v1/docs/centralized-management-of-sdp-user-dns-settings-with-the-dns-settings-policy). Custom DNS settings take priority over account-level DNS settings, including DNS Forwarding. However, if DNS Forwarding is configured to forward requests to a trusted DNS server or the DNS server configured for the account, then the account-level DNS settings are used.

**Notes:**

- For accounts that use the Cato DNS server, Cato can forward DNS queries only with the default DNS settings
- DNS Forwarding can process DNS requests over either UDP or TCP
- The PoPs don't store DNS forwarding requests in the cache

## Forwarding DNS Traffic to Cato

For Network Rules and firewall rules that are based on DNS (for example TLD, FQDN, and applications), the DNS traffic must use a DNS server that is trusted or defined for the account. Otherwise, these DNS-based rules aren’t applied to the traffic.

If you have an internal DNS server, you must [forward the DNS queries](/v1/docs/defining-dns-forwarding-rules) from a Cato-trusted DNS server (including Cato DNS) to the internal DNS server.

If you have a Network Rule for off-cloud traffic, make sure that it doesn't include DNS, so the DNS query is sent to a Cato-trusted DNS server.
