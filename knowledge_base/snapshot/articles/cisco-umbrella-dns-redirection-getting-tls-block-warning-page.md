---
title: "Cisco Umbrella DNS Redirection Getting TLS Block/Warning Page"
slug: "cisco-umbrella-dns-redirection-getting-tls-block-warning-page"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/cisco-umbrella-dns-redirection-getting-tls-block-warning-page"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cisco Umbrella DNS Redirection Getting TLS Block/Warning Page

## Issue

Cisco Umbrella provides endpoint security by redirecting DNS requests to its global network of servers.

If Cato's TLS inspection is enabled in the account and the 'Untrusted Server Certificates' option is set to Block or Warning, websites that require redirection by Cisco Umbrella (due to a Cisco security action) will receive a Cato Block/Warning page.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/11388933390621.png)

## Environment

- TLS inspection is enabled
- The 'Untrusted Server Certificates' option is set to Block or Warning.

## Troubleshooting

- Find the related TLS events for the blocked website. The TLS Certificate Error field will show 'Unable to get local issuer certificate'.
- If the destination IP shown in the event is within IP ranges 146.112.0.0/16, 155.190.0.0/16, and 151.186.0.0/16, that indicates that DNS redirection by Cisco Umbrella has taken place.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/11389584332445.png)
- The redirection will trigger a Cato TLS error led by a Cato blocking/warning page because the website's certificate issuer (Cisco Umbrella Root CA) is not trusted by Cato. The certificate chain below is presented to the end-user when bypassing Cato.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/11389362229789.png)

## Solution

Cisco Umbrella's IP ranges must be bypassed from Cato TLS inspection. When doing so, Cato will not block the Umbrella redirection due to a failed certificate check.

As per [Cisco's website](https://support.umbrella.com/hc/en-us/articles/360059292052-Additional-Egress-IP-Address-Range), the IP ranges used by the Umbrella service are 146.112.0.0/16, 155.190.0.0/16, and 151.186.0.0/16.

For information on how to bypass TLS inspection, see [Using Rules that Bypass TLS Traffic](/v1/docs/configuring-tls-inspection-policy-for-the-account).
