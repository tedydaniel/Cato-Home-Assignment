---
title: "Managing Signing Certificates for Remote Access"
slug: "managing-signing-certificates-for-remote-access"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/managing-signing-certificates-for-remote-access"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Signing Certificates for Remote Access

## Overview

Cato lets you enforce certificate-based authentication, ensuring that only trusted devices can connect to your network without relying solely on user credentials. Use the signing certificates in access policies to manage network access based on whether the certificate is installed on the device. For example, you can create a [certificate Device Check](/v1/docs/creating-device-posture-profiles-and-device-checks) that enforces device posture with the [Client Connectivity Policy](/v1/docs/what-is-the-client-connectivity-policy). The Signing Certificates page shows key certificate details and lets you add new certificates.

For more information about installing certificates, see the articles in [Distributing and Installing Device Certificates](/v1/docs/distributing-and-installing-device-certificates).

### Prerequisites

- The certificate that you upload to the CMA must meet the following requirements:
  - Certificate file is PEM format (base 64-encoded) with the extension **.pem**, such as: **sign_cert.pem**
  - X.509 format
  - Use RSA encryption
- The certificate that you install on the device must include:
  - Include both the public and private key
  - Match the certificate chain of the uploaded certificate
  - (Windows devices) Install the certificate in the Local Machine Personal Certificate Store
  - (macOS devices) Make sure that the Cato Client is permitted to access the private key of the certificate

## Upload Signing Certificates to the CMA

Upload signing certificates in the CMA to use them in access policies for your account.

If the uploaded certificate is invalid or expired, devices may be blocked from accessing the network based on your policy settings.

![signing_cert.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29595742245405.png)

**To upload a new signing certificate:**

1. From the navigation menu, select **Access > Client Access**.
2. In the Signing Certificates section, click **New**.
3. Enter the **Name** and click **Upload Certificate**.
4. Select the certificate file and upload it to the CMA.
5. **(Optional)** Click **Show Details** to view certificate metadata.

## Handling Expired Certificates

If a public key has expired, the PoP allows the connection only if the authority signed the device certificate before it expired.

- The red icon on the right side of the certificate indicates an expired certificate
- The yellow warning icon indicates that a certificate is about to expire within the next 30 days

Cato generates alerts for an expiring public key:

- 30 days before the public key is going to expire
- On the expiration date for the certificate

For the device certificates, Cato doesn’t allow a Client to connect with an expired certificate. If a user tries to connect with an expired device certificate, the Client notifies the PoP that the certificate has expired, and the connection is blocked.

The PoP verifies that the certificate is valid and then permits the connection for Clients.

The [Event page](/v1/docs/analyzing-events-in-your-network) shows these events with the certificate expiration date.

### Analyzing Certificate Events

The Events screen (**Home > Events**) helps you monitor the events for expired certificates. When the Cato Client successfully connects with a device certificate, Cato generates an event with the following information:

- Client Cert Name – the device certificate name used for the connection
- Client Cert Expires – the expiration date of the device certificate

For failed connection events, the failure reason is described in the event message. Connection failures can be caused by a bad issuer or an expired certificate.
