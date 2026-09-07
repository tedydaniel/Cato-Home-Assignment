---
title: "Fixing TLS inspection Issues for Claude Code"
slug: "fixing-tls-inspection-issues-for-claude-code"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/fixing-tls-inspection-issues-for-claude-code"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Fixing TLS inspection Issues for Claude Code

## Issue

When [Cato TLS Inspection is enabled](/v1/docs/configuring-tls-inspection-policy-for-the-account), Cato presents its own root/intermediate certificate as the issuer for inspected TLS sessions, enabling decryption and security. Most enterprise applications rely on the operating system or browser trust store, so once the Cato Root Certificate is installed there, they continue to work transparently.

However, some developer tools, including Claude Code, use certificate pinning or their own TLS implementation (for example, Node.js/OpenSSL) rather than relying solely on the OS trust store. As a result, they may reject the Cato-issued certificate even though the operating system trusts it, causing TLS errors (e.g., SELF_SIGNED_CERT_IN_CHAIN) during traffic inspection.

## Environment

- TLS Inspection is enabled for the account, even if Claude is bypassed.
- The Cato root certificate is installed and trusted in the OS trust store

## Troubleshooting

- Confirm the issue is limited to Claude Code or similar dev tools, not a general network problem
- Add the Cato root certificate using the app’s custom CA mechanism

## Solution

### Prerequisites

- **Cato Root Certificate (PEM format)** - You can download the certificate from here - [https://clientdownload.catonetworks.com/public/certificates/CatoNetworksTrustedRootCA.cer](https://clientdownload.catonetworks.com/public/certificates/CatoNetworksTrustedRootCA.cer)
- **Certificate file path** - Ensure the certificate is saved to a location on your local filesystem that is accessible and readable by the user account running the application.

### Instructions

Claude Code [supports custom Certificate Authorities via environment variables](https://code.claude.com/docs/en/network-config#custom-ca-certificates).

Use the `NODE_EXTRA_CA_CERTS` environment variable to direct Claude Code’s Node-based TLS stack to the Cato root certificate file. Ensure it is set globally and persistently so it works every time the user uses Claude Desktop, Claude CLI, or a Claude Code IDE extension.

### Verification

- Restart Claude Code after setting the environment variable
- Attempt a Claude Code operation that previously failed
- If it succeeds without TLS errors while TLS Inspection remains enabled, the configuration is correct

### Support Escalation Criteria

- The `NODE_EXTRA_CA_CERTS` variable is correctly configured and points to a valid PEM file, but Claude Code continues to fail with TLS handshake errors.
- The environment requires a combination of mutual TLS (mTLS) and proxy authentication that goes beyond standard environment variable configuration.
- Assistance is needed with deploying or enforcing environment variable settings across multiple users or machines at an organizational level.
