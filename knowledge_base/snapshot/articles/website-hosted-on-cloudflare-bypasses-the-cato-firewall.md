---
title: "Website Hosted on Cloudflare Bypasses the Cato Firewall"
slug: "website-hosted-on-cloudflare-bypasses-the-cato-firewall"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/website-hosted-on-cloudflare-bypasses-the-cato-firewall"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Website Hosted on Cloudflare Bypasses the Cato Firewall

## Issue

The Cato firewall fails to enforce firewall rules on websites hosted on Cloudflare. For instance, the website **research.cloudflare.com**, categorized as **Database**, is being allowed despite a firewall rule blocking this category.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22499982236573.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22499722091549.png)

The related CMA event shows a different domain name, **cloudflare-ech.com**, which doesn't match the intended site and bypasses the firewall rule. This event can be found by filtering the website's destination IP address.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22499722096413.png)

## Environment

- Firewall Rule blocking a specific category.
- No TLS Inspection enabled.

## Troubleshooting

The presence of the Domain Name **cloudflare-ech.com** in the event suggests that the Encrypted Client Hello (ECH) protocol is in use.

#### What is ECH?

As described in [Cloudflare documentation](https://developers.cloudflare.com/ssl/edge-certificates/ech/), ECH encrypts parts of the TLS Client Hello packet, including masking the Server Name Indication (SNI), which is typically used to establish a TLS session. This means that while Cato sees the connection to Cloudflare, it cannot identify the specific website. Both the browser and the website must support ECH for this to work.

#### How ECH Works

1. Public Key Distribution: Servers share a public key (within the ECH configuration) via DNS, often using secure DNS protocols like DoH (DNS over HTTPS) or DoT (DNS over TLS). However, unencrypted DNS via UDP can also be used. This key is used by the client to encrypt the Client Hello message. Below is an example of an HTTPS-type DNS reply containing the ECH configuration. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22499916309661.png)
2. Client Hello Encryption: When connecting, the client encrypts sensitive parts of the Client Hello, such as the SNI, using the server’s public key. Only the server can decrypt this information. An unencrypted outer Client Hello is also transmitted, displaying generic information such as a default SNI, which may not reveal the real target. In the example below, the default SNI is **cloudflare-ech.com** ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22499722100765.png)
3. Fallback Mechanism: If ECH is supported, the server processes the encrypted Client Hello, and the connection continues. If not, a fallback mechanism retries the connection with an unencrypted Client Hello, maintaining backward compatibility with traditional TLS 1.3 servers.

## Solution

Cato does not currently support ECH, so the following workarounds are recommended to force a fallback to unencrypted-SNI TLS connections based on your network setup:

- Block DoH, DoT, and QUIC protocols in the Internet Firewall. This will prevent the use of secure DNS protocols to exchange ECH configurations. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22499870238109.png)
- Depending on the browser, the client may fallback to UDP-based DNS to exchange ECH configurations. If so, enable [TLS inspection](/v1/docs/configuring-tls-inspection-policy-for-the-account) for the affected sites or users. ECH does not support Man-in-the-Middle (MITM) techniques, so the connection will fallback to using unencrypted SNI.
- As a last resort, block the domain **cloudflare-ech.com** in the Internet Firewall. This forces browsers to fallback to unencrypted SNI, allowing the correct firewall rule to apply. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22522099591837.png)
