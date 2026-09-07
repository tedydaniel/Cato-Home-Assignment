---
title: "What is PQC for TLS Inspection"
slug: "what-is-pqc-for-tls-inspection"
updated: 2026-06-22T09:27:06Z
published: 2026-06-22T09:27:06Z
canonical: "knowledge.catonetworks.com/what-is-pqc-for-tls-inspection"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is PQC for TLS Inspection

> [!NOTE]
> Note:
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

## Overview

Post-Quantum Cryptography (PQC) visibility and enforcement for TLS Inspection enhances your ability to monitor, inspect, and control the cryptographic algorithms used in TLS connections across your environment.

When enabled, TLS Inspection logs post-quantum–related parameters exchanged during the TLS handshake, including key exchange and digital signature algorithms for both client and server connections. In the TLS Inspection policy, you can choose to enforce PQC or Hybrid-PQC key exchange algorithms on a per-rule basis, providing granular control over cryptographic behavior.

These capabilities strengthen control over encrypted traffic, improve crypto-agility, and proactively future-proof the platform by supporting quantum-resistant cryptography before quantum threats become practical.

### Why PQC Matters

Traditional public-key cryptography (such as RSA and elliptic-curve–based key exchange) is designed to resist classical computing attacks. However, large-scale quantum computers are expected to break these algorithms using quantum techniques such as Shor’s algorithm.

Even before quantum computers become practical, adversaries can capture encrypted traffic today and store it for future decryption. This is known as a Store-Now, Decrypt-Later (SNDL) attack.

By introducing PQC visibility and enforcement within TLS Inspection, organizations can:

- Monitor the adoption of quantum-resistant algorithms across inspected TLS traffic
- Enforce the use of PQC or Hybrid-PQC encryption where required
- Reduce exposure to SNDL interception risks
- Advance their transition to a quantum-ready security architecture

For more information, please see these blog posts:

- [The Post-Quantum Journey Begins](https://www.catonetworks.com/blog/the-post-quantum-journey-begins/)
- [When Quantum Turns Encryption Into a Time Problem](https://www.catonetworks.com/blog/the-post-quantum-journey-begins/)

## Configuring PQC for TLS Inspection

PQC configuration is managed within each TLS Inspection rule. By default, PQC is disabled. You can enable and configure PQC behavior separately for both the client side and the server side of the inspected connection. For more information about TLS inspection, see [Configuring TLS Inspection Policy for the Account](/v1/docs/configuring-tls-inspection-policy-for-the-account).

> [!NOTE]
> Note:
> 
> PQC configuration requires TLS version 1.3 and a rule with an **Inspect** action.

- **Standard (Recommended):** Enables validated PQC and Hybrid-PQC key exchange algorithms to provide strong security with broad interoperability.
- **Advanced:** Enables validated PQC-only key exchange algorithms, allowing stricter enforcement of quantum-resistant cryptography

![PQC.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34309563208605.png)

**To configure PQC:**

1. From the navigation menu, click **Security > TLS Inspection**.
2. In a TLS inspection rule configure the **Client** and **Server** settings to meet your requirements.
3. Click **Save** and then **Publish**
