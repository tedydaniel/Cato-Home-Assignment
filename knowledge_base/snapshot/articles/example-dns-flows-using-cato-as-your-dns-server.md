---
title: "Example DNS Flows Using Cato as your DNS Server"
slug: "example-dns-flows-using-cato-as-your-dns-server"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/example-dns-flows-using-cato-as-your-dns-server"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Example DNS Flows Using Cato as your DNS Server

This article provides examples of DNS flows when using Cato as your DNS server.

## Sample Diagrams of DNS Flows

This section shows several DNS flow examples. Each one explains how Cato's DNS service works in a different configuration.

### Using Cato as a DNS Server

The following diagram shows an example of an account that uses the Cato DNS server (10.254.254.1). The same flow applies to any trusted DNS server.

1. A host requests to resolve a public domain (abc.com).
2. The Cato PoP intercepts the DNS query and checks for the destination IP address. The PoP performs DNS inspection, checks for DNS forwarding rules and for local DNS records in the cache.
3. No matching DNS records are identified in the cache.
4. The PoP then forwards the DNS query to a trusted DNS server and performs SNAT.
5. When the trusted DNS server sends back the response, the PoP translates back the source and destination IP addresses and forwards the response to the originating host.

The PoP also stores the DNS response in the cache.

| ![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30151554712733.png) |
| --- |

### Using Untrusted DNS Server

The following diagram shows an example of using an untrusted DNS server (IP address: 208.67.222.222 - OpenDNS).

1. The PoP forwards the DNS query "as-is" to the destination (abc.com) over the Internet.
2. The PoP applies the DNS Protection policy and DNS caching.
3. The PoP performs NAT on the source IP address (with the PoP public IP address).

The PoP doesn't perform DNS inspection or DNS forwarding rules.

![mceclip1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30151565241117.png)

### Using DNS Forwarding Rules

The following diagram shows an example of a DNS query to Cato's DNS service (10.254.254.1) when DNS forwarding rules are applied (*.local.org).

1. The PoP inspects the DNS query, and checks for forwarding rules.
2. The PoP redirects the DNS query to the remote DNS server (192.168.5.5).

The PoP doesn't cache DNS responses from a forwarding DNS server.

If the host and the DNS server are in the same site, the source IP of these packets is 10.254.254.1

| ![mceclip2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30151568548253.png) |
| --- |

### Using Untrusted Private DNS Server

The following diagram shows an example of using an untrusted private DNS server (192.168.5.5).

1. The PoP forwards the DNS query to the destination "as-is" over the WAN.
2. The PoP applies the DNS Protection policy and DNS caching.
3. The PoP doesn't perform DNS inspection and DNS forwarding rules aren't applied.

**Note**: The DNS response still populates the dname field used by the Internet Firewall and Network Rules. This means that the response could be inspected and blocked by Cato.

| ![mceclip3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30151541613469.png) |
| --- |

### Using Cato as the DNS Server with a DNS Relay

The following diagrams show an example of using Cato as the DNS server when you have configured an exception in the Split Tunnel policy for the local DNS server.

Once there is an exception, the DNS-relay service is automatically implemented to facilitate the proper resolution. The DNS-relay service has been added by Cato to manage DNS requests and determine if the request needs to go through the Cato DNS or the local DNS.

#### Local Domain Query

This section shows the flow when you send a DNS request for a local domain, which is sent to the local DNS server.

1. A host requests to resolve a local domain (*.local.org).
2. The DNS-relay intercepts the request and redirects it to the local DNS Server (192.168.5.5), which resides in the same site as the host. The DNS-relay uses the same ip as the host (as it is only a component in it, and doesn't have another physical interface).
3. The local DNS Server sends back the response to the originating host.
4. The dns-relay intercepts the response and redirect it to the originating host.

![local-dns-flow.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30151550473373.png)

#### Public Domain Query

This section shows the flow when you send a DNS request for a public domain through the Cato DNS server.

1. A host requests to resolve a public domain, for example, cnn.com.
2. The dns-relay intercepts the request and redirects it to the Cato DNS server (10.254.254.1). The dns-relay uses the same IP address as the host (as it is only a component in it, and doesn't have another physical interface).
3. The PoP then forwards the DNS query to a trusted DNS server and performs SNAT.
4. The trusted DNS server sends the response to the PoP.
5. When the trusted DNS server sends back the response, the PoP translates the source and destination IP addresses and forwards the response to the originating host.
6. The DNS-relay intercepts the response and redirect it to the originating host

![Cato-DNS-Relay.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30151580380829.png)
