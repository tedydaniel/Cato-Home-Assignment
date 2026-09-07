---
title: "Updated Instructions for Upcoming Expiring TLS Certificate"
slug: "updated-instructions-for-upcoming-expiring-tls-certificate"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/updated-instructions-for-upcoming-expiring-tls-certificate"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Updated Instructions for Upcoming Expiring TLS Certificate

The default Cato certificate used by the TLS Inspection policy and Threat Prevention engines was issued in 2015 and has expired.

If TLS Inspection is not enabled for your account, no action is required.

If TLS Inspection is enabled, to ensure uninterrupted service, please complete the following steps in your Cato Management Application before the expiration date:

1. Complete the [required prerequisites](https://support.catonetworks.com/hc/en-us/articles/22781778613149-FAQ-for-the-New-Default-Cato-Certificate-for-TLS-Inspection) on every device in scope for the TLS inspection policy.
2. Activate the new Cato Certificate or upload a new valid custom certificate to the [Security > Certificate Management page](/v1/docs/managing-certificates-for-tls-inspection).

After **October 29, 2025**, customers who did not activate a new certificate will experience the following issues:

- TLS Inspection will not function properly.
- Threat Prevention services will be unable to inspect TLS-encrypted traffic.
- Users may encounter difficulties accessing HTTPS resources.

For detailed instructions, please refer to the [New Default Cato Certificate FAQ guide](https://support.catonetworks.com/hc/en-us/articles/22781778613149-FAQ-for-the-New-Default-Cato-Certificate-for-TLS-Inspection). If you have any questions or need assistance, our support team is available to help.
