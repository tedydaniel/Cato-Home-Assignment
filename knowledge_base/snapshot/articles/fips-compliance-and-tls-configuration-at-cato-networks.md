---
title: "FIPS Compliance and TLS Configuration at Cato Networks"
slug: "fips-compliance-and-tls-configuration-at-cato-networks"
updated: 2026-06-22T09:27:06Z
published: 2026-06-22T09:27:06Z
canonical: "knowledge.catonetworks.com/fips-compliance-and-tls-configuration-at-cato-networks"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# FIPS Compliance and TLS Configuration at Cato Networks

This is an unofficial draft of FIPS compliance and TLS versions and cipher suites.

## Overview

This article explains how Cato Networks relates to Federal Information Processing Standards (FIPS) compliance. It also discusses how customizing the TLS Version and Cipher Suite compatibility level in the TLS Inspection Policy feature relates to the FIPS 140-2 and 140-3 encryption requirements.

For reference, see the [Mozilla Server Side TLS wiki](https://wiki.mozilla.org/Security/Server_Side_TLS), which provides compatibility levels (Modern, Intermediate, and Legacy) and their associated cipher configurations.

## Enforcing TLS Versions and Ciphers in the TLS Inspection Policy

Cato Networks is not FIPS-compliant. However, you can use the TLS Inspection Policy to enforce specific TLS versions and the compatibility level of cipher suites to be more consistent with FIPS guidelines. For more information, see [Configuring TLS Inspection Policy for the Account](/v1/docs/configuring-tls-inspection-policy-for-the-account).

To enforce specific TLS versions and compatibility levels in your account, configure the **TLS Inspection Policy** using the options in the **TLS Version and Cipher Suites** for the rule **Action**.

![TLS_inspect.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28357339768093.png)

## Recommendations for FIPS Compatibility Levels

The Mozilla compatibility levels provide guidance on which ciphers are recommended for FIPS alignment. The following compatibility profiles can help you configure the TLS Inspection Policy accordingly:

- Use the Modern or Intermediate compatibility profiles, based on your organization's FIPS alignment and compatibility needs
- Use the Intermediate compatibility profile to include a broader set of FIPS-approved ciphers
- Avoid using the Legacy profile, as it includes many outdated and non-compliant ciphers

### Modern Compatibility

- TLS 1.3
  - Approved for FIPS 140-2/140-3:
    - `TLS_AES_128_GCM_SHA256`
    - `TLS_AES_256_GCM_SHA384`
  - Not Approved:
    - `TLS_CHACHA20_POLY1305_SHA256` (rarely used)
- TLS 1.2
  - No TLS 1.2 ciphers in the Modern set are FIPS-approved.

**Recommendation:** You can set TLS Inspection Policy to enforce **TLS 1.3** as the minimum TLS version, and the **Modern** cipher suite. This can help you align more closely with FIPS-recommended cryptographic practices.

### Intermediate Compatibility

- TLS 1.3
  - Same compatibility as in Modern
- TLS 1.2
  - FIPS-Approved Ciphers:
    - `ECDHE-ECDSA-AES128-GCM-SHA256`
    - `ECDHE-RSA-AES128-GCM-SHA256`
    - `ECDHE-ECDSA-AES256-GCM-SHA384`
    - `ECDHE-RSA-AES256-GCM-SHA384`
    - `DHE-RSA-AES128-GCM-SHA256`
    - `DHE-RSA-AES256-GCM-SHA384`
  - Not Approved:
    - `ECDHE-ECDSA-CHACHA20-POLY1305`
    - `ECDHE-RSA-CHACHA20-POLY1305`
    - `DHE-RSA-CHACHA20-POLY1305`

**Recommendation:** If your organization requires FIPS alignment and broader client compatibility than the Modern profile allows, configure the TLS Inspection Policy with **TLS 1.2** as the minimum TLS version using the **Intermediate** compatibility level. This policy includes several FIPS-approved options, but it also contains non-approved ciphers.

### Legacy Compatibility

Not recommended for FIPS-related enforcement because it includes outdated and non-approved ciphers.

## Known Limitations

- Cato Networks is not FIPS 140-2 or 140-3 certified
- This configuration does not replace formal compliance or validation requirements
- You cannot disable or block individual TLS ciphers
