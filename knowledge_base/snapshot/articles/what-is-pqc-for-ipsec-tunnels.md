---
title: "What Is PQC for IPsec Tunnels?"
slug: "what-is-pqc-for-ipsec-tunnels"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/what-is-pqc-for-ipsec-tunnels"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What Is PQC for IPsec Tunnels?

> [!NOTE]
> Note:
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

## Overview

Post-Quantum Cryptography (PQC) strengthens IPsec tunnel security by introducing quantum-resistant key exchange mechanisms. As quantum computing capabilities evolve, widely used algorithms such as RSA and Elliptic Curve Cryptography (ECC) may eventually become vulnerable. PQC helps ensure that your site-to-site WAN traffic remains protected against both current and future cryptographic threats.

Enabling PQC for IPsec sites and tunnels allows you to align your organization’s encryption strategy with long-term security and compliance requirements, without changing how your sites connect to the Cato Cloud.

### Protection Against Harvest Now, Decrypt Later Attacks

One of the primary risks associated with quantum computing is the "harvest now, decrypt later" model. In this scenario, attackers capture encrypted traffic today, store it, and wait until quantum capabilities mature enough to break classical encryption.

Even if the traffic cannot be decrypted now, sensitive information with a long retention value may be exposed in the future. PQC mitigates this risk by incorporating quantum-resistant key exchange algorithms into the IPsec negotiation process. As a result, traffic captured today remains protected even against future quantum decryption attempts.

## Operational and Security Considerations

### Long-Term Data Protection

Many organizations rely on long-lived IPsec tunnels to transport sensitive traffic between sites, data centers, and cloud environments. This traffic often includes regulated or business-critical data that must remain confidential for years or decades. By enabling PQC, you help ensure that encryption strength aligns with long-term data protection strategies and emerging security standards.

### Hybrid IKEv2 Negotiation Model

PQC for IPsec tunnels is implemented using a hybrid-first IKEv2 negotiation approach. During tunnel establishment, classical cryptography and PQC algorithms are negotiated together. This design preserves interoperability with peers that do not yet support PQC and maintains connectivity through a controlled fallback mechanism if required.

This approach allows you to introduce quantum-resistant cryptography without disrupting existing site-to-site connectivity or requiring simultaneous upgrades across all peers.

### Visibility and Migration Control

PQC support includes telemetry that provides insight into tunnel negotiation behavior. You can monitor negotiation outcomes, identify fallback scenarios, and validate successful quantum-safe negotiations. This visibility helps you determine which peers are PQC-ready and manage the migration process in a controlled and measurable way.

### Centralized Management in the CMA

PQC configuration is integrated directly into the IKEv2 and IPsec tunnel settings and is exposed through the relevant APIs and AccountSnapshot fields. This allows you to manage cryptographic settings centrally in the Cato Management Application (CMA). Adopting PQC does not introduce additional operational complexity. The configuration model remains consistent with existing IPsec management processes.

## When to Enable PQC

You should consider enabling PQC for IPsec tunnels if your organization operates critical infrastructure, manages regulated environments, or transports sensitive data with long retention requirements.

PQC is also relevant if you are proactively aligning with emerging cryptographic standards and preparing your network architecture for the post-quantum era.
