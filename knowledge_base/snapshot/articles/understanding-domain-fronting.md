---
title: "Understanding Domain Fronting"
slug: "understanding-domain-fronting"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/understanding-domain-fronting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding Domain Fronting

This article explains how Cato automatically blocks domain fronting by continuously reevaluating the true hostname across DNS, TLS, and HTTP inspection stages. This ensures that disguised Command-and-Control (CnC) traffic is immediately detected and blocked.

## Overview

Domain fronting is a technique used by threat actors to disguise malicious traffic as legitimate communication. It exploits how HTTPS and Content Delivery Networks (CDNs) process domain names. During a standard HTTPS connection, two domain identifiers are visible at different stages:

- **SNI (Server Name Indication)**: Sent in plaintext during the TLS handshake, indicating the intended hostname the client intends to connect to
- **Host Header**: Sent later within the encrypted HTTP request, specifying the actual domain being accessed

With domain fronting, attackers deliberately mismatch these two fields, for example, using a benign domain in the SNI (e.g., example.com) and a malicious one in the Host header (e.g., malicious-cnc.com). This allows Command-and-Control (CnC) traffic to appear as if it’s destined for a legitimate service, often hidden behind major cloud or CDN providers.

## How Cato Blocks Domain Fronting

Unlike other solutions that require special rules or updates to handle domain fronting, Cato’s architecture inherently detects and blocks domain fronting attempts. It does this by continuously reevaluating the true identity of a flow as more information becomes available (for more information, see [Understanding Packet Flow with Cato SPACE Architecture](/v1/docs/understanding-packet-flow-with-cato-space-architecture) , which explains this dynamic reevaluation process).

### Unified Host Name Evaluation

Cato uses a concept called the unified host name, a dynamically updated identifier that represents the true destination of a flow. This identifier is refined at each inspection stage:

1. During the DNS resolution phase, Cato identifies the DNAME, the domain associated with the destination IP
2. During the TLS handshake, Cato observes the Server Name Indication (SNI), which shows the hostname the client is trying to reach
3. After TLS inspection, once the encrypted traffic is decrypted, Cato can see the HTTP Host header, revealing the actual domain being accessed

Cato re-evaluates the unified host name at each of these stages. If the Host header domain conflicts with or differs from the original SNI, Cato treats it as new intelligence and triggers reevaluation across both the Firewall (FW) and Intrusion Prevention System (IPS) engines.

This means that both products are effectively re-applied with the new hostname context. If the newly revealed host is malicious (i.e., configured to be blocked by the Firewall or included in a blocking IPS signature), Cato blocks it immediately, even though the original SNI and destination IP appeared benign.

This layered inspection ensures that CnC channels attempting to hide behind trusted domains are blocked as soon as the true destination is exposed.

## Testing Domain Fronting Protection

To validate Cato’s protection against domain fronting, you can reproduce the detection process yourself:

1. **Create a Firewall Rule**: Ensure you have a Firewall rule configured to block anonymizers (or create one if not already present).
2. **Send a Test Request**: Run the following curl command:

`curl -v https://example.com -H 'Host: expressvpn.com'`

The command is blocked by the Firewall
3. **Verify the Block**: In the CMA, check the Events page under Firewall rule hits to confirm the block. In the event attributes, the **Destination IP** field is the examplee.com IP address, while the **Domain Name** field is updated with the domain that last appeared in the HTTP Host header: expressvpn.com.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31712021492637.png)

Optional: You can also capture the traffic in Wireshark (if sent in plaintext rather than HTTPS) to visualize the Host header and confirm the block event.

After applying the configuration, you can verify the behavior by running the following command: `curl -v https://chatgpt.com -H 'Host: echo.free.beeceptor.com'`

These steps provide a transparent way to observe how Cato neutralizes domain fronting attempts through its post-inspection reevaluation process.

### Example Capture

Below is an example Wireshark capture showing the DNS and HTTP flows from the test:

![Domain_Forwarding1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31711683898397.png)

It shows a DNS query to examplee.com, followed by an HTTP request where the Host header points to expressvpn.com. The HTTP response returns 403 Forbidden, confirming that Cato successfully blocked the domain-fronted request.

Domain fronting is a technique used to hide malicious communication behind legitimate domains. While some solutions struggle to identify traffic that hides behind legitimate domains, Cato’s architecture, with unified hostname reevaluation and dual-engine revalidation, inherently blocks these attempts. By continuously updating the SNI, Host header, and IP information across inspection stages, Cato ensures that CnC channels masquerading behind trusted domains never make it through.
