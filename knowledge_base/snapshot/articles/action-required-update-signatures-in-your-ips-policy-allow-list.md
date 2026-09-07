---
title: "Action Required: Update Signatures in your IPS Policy Allow List"
slug: "action-required-update-signatures-in-your-ips-policy-allow-list"
updated: 2026-08-10T10:37:42Z
published: 2026-08-10T10:37:42Z
canonical: "knowledge.catonetworks.com/action-required-update-signatures-in-your-ips-policy-allow-list"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Action Required: Update Signatures in your IPS Policy Allow List

**Note**: No action is required unless Cato has directly contacted you and asked you to do something. If you haven't been contacted by Cato, you can disregard this notice.

To give you more control over DNS Protection enforcement, we are adding a configurable threshold for Newly Registered Domains (NRDs). You will be able to block domains registered within the last 7, 14, 21, 30, and 60 days.

As part of this change, on July 8, 2026, we are retiring six existing NRD signatures. These signatures will be replaced by two new signatures. We identified that your IPS Policy allow list includes at least one signature that will be retired.

To prevent unintentionally blocking NRDs, update your IPS Allow List to use the new signatures by July 8, 2026.

For more information about DNS protection, see [Customizing the DNS Protections for IPS..](/v1/docs/customizing-the-dns-protections-for-ips)

## What Action do I need to Take?

Before July 8, 2026:

1. In the Cato Management Application, on the **Security > IPS > Allow List** page, identify any rule that contains one of the following retired signatures:

- cid_dns_feed_block_newly_registered_domains_1
- cid_dns_feed_block_newly_registered_domains_2
- cid_dns_feed_block_newly_registered_domains_3
- cid_ioa_block_newly_registered_domains_1
- cid_ioa_block_newly_registered_domains_2
- cid_ioa_block_newly_registered_domains_3

1. Replace the retired signature with the following new signatures:

- feed_block_newly_registered_domains_configurable_1
- cid_dns_feed_block_newly_registered_domains_configurable_1

1. Click **Save**.

For more information, see [Allowlisting IPS Signatures..](/v1/docs/allowlisting-ips-signatures)

## What Happens If I Do Not Take Action?

After July 8, 2026, IPS Allow List rules referencing the retired signatures will no longer match. As a result, domains that are currently excluded from NRD blocking may be blocked unexpectedly.

## Who Do I Talk to If I Have Questions?

Please use the [Cato Ask AI agent](https://externallink.cc.catonetworks.com/#/account/me/aiWorkspace?support) in the CMA to answer questions about your IPS Policy and creating Allow List rules.
