---
title: "What is PQC for the Cato Client"
slug: "what-is-pqc-for-the-cato-client"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/what-is-pqc-for-the-cato-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is PQC for the Cato Client

> [!NOTE]
> Note:
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

## Overview

Post-Quantum Cryptography (PQC) for the Cato Client enhances the cryptographic handshake between the Client and Cato Points of Presence (PoPs) to protect remote access traffic against future quantum-computing threats.

When enabled for the entire account, the Client uses a post-quantum key exchange mechanism during tunnel establishment with the Cato Cloud. This strengthens the security of all traffic between the Client and the PoP and helps protect sensitive data against sophisticated attacks.

### Why PQC Matters

Traditional public-key cryptography (such as RSA and elliptic-curve–based key exchange) is designed to resist classical computing attacks. However, large-scale quantum computers are expected to break these algorithms using quantum techniques such as Shor’s algorithm.

Even before quantum computers become practical, adversaries can capture encrypted traffic today and store it for future decryption. This is known as a Store-Now, Decrypt-Later (SNDL) attack.

By introducing post-quantum key exchange between the Client and the Cato Cloud, organizations can:

- Protect long-lived or sensitive data from future quantum threats
- Reduce exposure to SNDL-style interception risks
- Begin transitioning to a quantum-ready security architecture

For more information, see this [Cato blog](https://www.catonetworks.com/blog/the-post-quantum-journey-begins/).

### Prerequisites

- PQC for Clients is supported on Windows Client v6.0 and higher

## PQC and Cato Remote Access Architecture

When you enable Post-Quantum Cryptography (PQC) for Clients in your account, the platform upgrades the cryptographic handshake used to establish the secure tunnel between the Client and the nearest Cato PoP.

The change occurs during tunnel establishment:

1. **Client tunnel initiation:** The Client connects to the optimal PoP based on Cato’s global backbone routing and site proximity.
2. **Post-quantum key exchange negotiation:** During the handshake phase, the Client and the PoP use a post-quantum resistant key exchange mechanism instead of relying solely on classical public-key methods.

This protects the session establishment process against future quantum decryption capabilities.
3. **Session key derivation and enforcement:** The derived session keys are then used to encrypt all traffic flowing between the Client and the PoP.

Once enabled, PQC applies to all traffic transmitted through the Client tunnel, without requiring application changes, user interaction, or policy modifications.

**Note:** Post-quantum key exchange requires larger keys and additional computation compared to classical cryptography. As a result, after enabling PQC, you may experience significant performance degradation for remote users.
