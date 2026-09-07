---
title: "macOS Ventura and iOS Users Unable to Reach Internal Resources Via Cato"
slug: "macos-ventura-and-ios-users-unable-to-reach-internal-resources-via-cato"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/macos-ventura-and-ios-users-unable-to-reach-internal-resources-via-cato"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# macOS Ventura and iOS Users Unable to Reach Internal Resources Via Cato

## Issue

On macOS Ventura and iOS devices, users aren't able to reach internal resources when connected to Cato

## Environment

- macOS Ventura 13.0 or later
- iPhone iOS 16 or later
- Cato SDP Client regardless of the version
- DNS forwarding configured for internal domains

## Reason

If Cato DNS settings applied to SDP users are default (empty fields), Cato will push to the client the following DNS information:

- Primary DNS server **10.254.254.1**
- Secondary DNS server **8.8.8.8**

Based on Cato's tests, when the account is configured as above or using a known public DNS server (such as 8.8.8.8 or 1.1.1.1), macOS/iOS are likely to prefer **DoH** (DNS over HTTPS) or **DoT** (DNS over TLS) for name resolution toward the configured public DNS server. Cato currently does not support DoH/DoT.

Once macOS/iOS sees a DNS server that is compliant with DoH/DoT, it will ignore any other DNS server, including Cato's DNS Server IP. Further information can be found in this [Apple discussion](https://discussions.apple.com/thread/254321365).

Since Cato PoPs **don't support** [DNS forwarding](/v1/docs/defining-dns-forwarding-rules) for DoH/DoT packets, DNS forwarding fails, the user can't reach internal resources, or the retrieved DNS results aren't the expected ones.

The preferred DNS servers on the machine can be identified by running ***scutil --dns*** in the terminal. The following output shows that macOS prefers 8.8.8.8 as the primary DNS server.

```plaintext
MacBook-Air-2:~ xx$ scutil --dns 
DNS configuration

resolver #1
nameserver[0] : 8.8.8.8
nameserver[1] : 10.254.254.1
if_index : 24 (utun8)
flags : Supplemental, Request A records
reach : 0x00000003 (Reachable,Transient Connection)
order : 101200
```

Be aware that when DNS settings between entities conflict, the entity closest to the host (from host > site > group > account) takes precedence. For more information, see [Configuring DNS Settings](/v1/docs/configuring-dns-settings)

## Solution

This is a known issue that Apple is actively working on. The following workarounds can be implemented at Cato:

1. Block **DoH (DNS over HTTPS)** and **DNS over TLS** in a [Firewall rule](/v1/docs/managing-the-internet-firewall-policy) to prevent these protocols from being reachable via Cato. This will force macOS/iOS to switch to Cato's default DNS server, 10.254.254.1, over UDP-based DNS, allowing DNS forwarding.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10977982005917.png)
2. Set **10.254.254.1 as the only DNS server EXPLICITLY in CMA**. This will prevent 8.8.8.8 (or any other DoH/DoT-supported DNS server) from being set as the machine's primary DNS and will force ALL DNS queries to be handled by Cato.

The DNS server can be set globally or per group, preferably the pre-configured 'All SDP Users' user group. For more information, see [Centralized Management of SDP User DNS Settings](/v1/docs/centralized-management-of-sdp-user-dns-settings-with-the-dns-settings-policy)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17169345631901.png)
