---
title: "Getting Started with Cato Certificates"
slug: "getting-started-with-cato-certificates"
updated: 2026-09-02T04:55:58Z
published: 2026-09-02T04:55:58Z
canonical: "knowledge.catonetworks.com/getting-started-with-cato-certificates"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with Cato Certificates

This article explains the different certificates used by Cato Networks and their purposes.

## Overview

Cato uses two distinct digital certificate types: the TLS Inspection Certificate and the Cato Client Device Certificate. They address different security controls and are deployed independently. Together, they help you inspect encrypted traffic and verify that endpoint devices meet your organization’s trust requirements.

## Certificate Comparison

| Certificate | Primary Purpose | Deployment and Outcome |
| --- | --- | --- |
| Cato TLS Inspection Certificate | Lets Cato decrypt, inspect, and re-encrypt HTTPS sessions for security controls such as DLP, Anti-Malware, and application control. | Install the Cato default Root CA during Cato Client installation, or upload and distribute a custom root CA. Endpoints trust inspected HTTPS sessions without browser certificate warnings. |
| Cato Client Device Certificate | Enables certificate-based authentication so Cato can identify trusted endpoint devices and apply Zero Trust access controls. | Upload a Signing Certificate to the Cato Management Application (CMA) and deploy device certificates to endpoints with MDM or automation. Cato can validate devices, apply posture checks, and enforce Client Connectivity policies. |

## Cato TLS Inspection Certificate

Use this certificate when you need Cato to inspect encrypted HTTPS traffic. The certificate establishes Cato as a trusted intermediary for TLS inspection.

### How It Works

- Cato decrypts encrypted HTTPS traffic, applies the configured security controls, and re-encrypts the session.
- The endpoint must trust the Cato Root CA to prevent browser certificate warnings.
- You can use the Cato default Root CA or upload your organization’s custom root CA to the CMA.

### Example Use Case

An organization enforces TLS inspection for web traffic to support DLP and Anti-Malware scanning. The admin uploads a custom root CA to the CMA and distributes it with MDM. Users can then browse HTTPS sites while Cato inspects the traffic without certificate warnings.

## Cato Client Device Certificate

Use this certificate to require device-based authentication for Cato Client connectivity. It helps restrict network access to endpoints that your organization trusts.

### How It Works

- The organization uploads a Signing Certificate to the CMA so Cato can verify endpoint certificates.
- A trusted certificate authority issues device certificates, which are deployed to endpoints using MDM or automation.
- After validation, Cato can apply posture checks and Client Connectivity policies to the endpoint.

### Example Use Case

An organization permits Cato Client connectivity only from company-issued laptops. After device certificate validation is enabled in the Client Connectivity Policy, a personal device without the required certificate cannot connect, even when the user has valid credentials.

## Key Distinction

TLS Inspection Certificates establish trust for inspected HTTPS sessions. Client Device Certificates establish trust in the endpoint itself. They are not interchangeable, and each must be deployed for its intended control.
