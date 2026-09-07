---
title: "Using Trusted DNS Servers"
slug: "using-trusted-dns-servers"
status: "update"
updated: 2026-09-03T10:22:34Z
published: 2026-09-03T10:22:34Z
canonical: "knowledge.catonetworks.com/using-trusted-dns-servers"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Trusted DNS Servers

This article lists the DNS servers Cato considers to be trusted.

## Overview

The Global DNS services listed in this article are verified as secure and, together with the DNS servers configured for your account, are treated by Cato as trusted DNS servers. DNS servers not on this list, or not configured for your account, are considered untrusted DNS servers.

The DNS behavior is different for trusted and untrusted DNS servers. For example, only requests to trusted DNS servers are inspected by PoPs. This means that the PoP applies the logic for several DNS-related features, including [DNS Forwarding](/v1/docs/defining-dns-forwarding-rules), and sending DNS requests to multiple servers for resiliency. For untrusted DNS servers, the PoP does not apply this logic to the DNS requests.

The list of trusted servers is a global list with servers from various regions. This creates uniformity across all Cato PoPs, so you can create the DNS configurations for your account. In the Cato Cloud infrastructure, DNS queries are only resolved by the DNS servers in the same region as the PoP. If a trusted server has a performance issue, Cato may resolve DNS queries with other well-known servers not on this list. These servers are not considered trusted servers.

## Trusted DNS Servers

These are the DNS servers Cato considers to be trusted for PoP locations (excluding those countries specified below):

- 10.254.254.1 (Cato DNS server)
- 8.8.8.8
- 9.9.9.9 (doesn't support EDNS)
- 1.1.1.1

### Trusted DNS Servers for China

For sites and users connected to Cato PoPs located in China (such as Beijing and Shanghai), these are the trusted DNS servers:

- 119.29.29.29
- 223.5.5.5
- 218.30.118.6

### Trusted DNS Servers for Vietnam

For sites and users connected to the Cato PoP located in Ho Chi Minh City, Vietnam, these are the trusted DNS servers:

- 10.254.254.1 (Cato DNS server)
- 8.8.8.8
- 9.9.9.9 (doesn't support EDNS)
- 1.1.1.1
- 203.119.36.106
- 113.163.157.27

## Article Changelog

| Date | Description |
| --- | --- |
| Sept 3, 2026 | Added [Trusted DNS Servers for China](/v1/docs/using-trusted-dns-servers#tru) |
|  |  |
