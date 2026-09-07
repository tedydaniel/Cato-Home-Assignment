---
title: "How the Cato Cloud Protects against DNS Tunneling"
slug: "how-the-cato-cloud-protects-against-dns-tunneling"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/how-the-cato-cloud-protects-against-dns-tunneling"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How the Cato Cloud Protects against DNS Tunneling

Domain Name System (DNS) Tunneling is a common method for hackers to exploit the DNS service for malicious purposes, such as exfiltrating sensitive organization data or infiltrating malware. This article explains how the IPS engine in the Cato Cloud protects your network from the DNS tunneling malware attacks.

When you configure the [IPS policy to block traffic](/v1/docs/configuring-the-ips-policy), this also enables the Cato Cloud's protections against DNS Tunneling attacks for your account.

## Detecting DNS Tunneling

The Cato Cloud analyzes DNS requests and identifies potential DNS Tunneling attacks based on these properties:

1. Packet size – The length of the requests may indicate anomalous communication over DNS. Large DNS packets are anomalous and indicate a potential attack.
2. Record type – Resource records (RR) that map domains to IP addresses (such as A and AAAA records) are most common in DNS protocol usage but are restricted to a short response length. When exchanging data over DNS, usage of RR may vary to allow more data to be transported and can indicate an attack.
3. Unique ratio – DNS queries and responses that carry encoded information are likely to be unique. When there is a high level of unique subdomains in a query, this can indicate an attack.

## Blocking DNS Tunneling

To protect customers from DNS tunneling related to malicious hackers, Cato uses machine learning algorithms to detect anomalies over all outbound DNS queries. The DNS traffic between each site connected to the Cato Cloud and each unique domain is analyzed offline over a time period of 24 hours. Domains with a low reputation that receive frequent anomalous DNS queries are automatically signed in the following day. Then the IPS policy for all accounts is able to block the relevant DNS traffic for these domains.

Furthermore, Cato prevents data exfiltration over DNS tunneling using a set of heuristics that trigger IPS to block the traffic. These heuristics have been tested over multiple DNS tunneling tools and techniques. This real-time prevention is achieved even without knowing the threat actor or the domain name, and complements Cato’s machine learning algorithms.

### Reviewing Events for Blocked DNS Tunneling Attacks

You can review Security events in **Home > Events** and find any DNS Tunneling attacks in your account that IPS blocked. The IPS events are labeled with the threat type **DNS Tunneling**.

![DNS_Tunneling_Event.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303168680861.png)

## Cato Blocked a DNS Tunneling Attack - Now What?

If you find block events for DNS Tunneling, here are some suggested next steps:

1. Isolate the infected hosts from the network (in both the WAN and Internet firewalls).
2. Remediate the hosts with anti-malware and endpoint protection software.
