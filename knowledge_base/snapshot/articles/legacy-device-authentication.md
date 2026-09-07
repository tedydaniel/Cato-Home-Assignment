---
title: "LEGACY - Device Authentication"
slug: "legacy-device-authentication"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/legacy-device-authentication"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# LEGACY - Device Authentication

This feature is not available for accounts created after April 14, 2024. To control certified corporate devices, use the enhanced functionality of the [Client Connectivity Policy.](/v1/docs/configuring-the-client-connectivity-policy)

For more information, see [Managing Signing Certificates for Remote Access](/v1/docs/managing-signing-certificates-for-remote-access).

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

## Filtering Events with Predefined Filters

The Events screen provides two event filter presets to help you monitor Device Authentication:

1. Client certificate about to expire
2. Client authentication issue

**1. The Client certificate about to expire filter**

You can select this preset to show all the successful connection events that are related to a device certificate that is about to expire within the next 30 days.

**Note**: Cato doesn’t generate a separate event for certificates that are about to expire.

The following screenshot shows a sample of the Event Discovery window when the **Client certificate about to expire** is applied:

![04_expired.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29595759497629.png)

**2. The SDP authentication issue filter**

This preset is not specifically for connecting with device certificate-based authentication, it shows all the failed connection events.

The following screenshot shows a sample of the Event screen when the **SDP authentication issue** filter is applied:

![05_ED.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29595729741085.png)
