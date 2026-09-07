---
title: "Troubleshooting Issues Related to Local SMTP Servers"
slug: "troubleshooting-issues-related-to-local-smtp-servers"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/troubleshooting-issues-related-to-local-smtp-servers"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Issues Related to Local SMTP Servers

Email servers that are hosted locally, send emails to a hosted email service or directly to the Internet. If there is an issue where emails aren't delivered, or occasionally bounce back with an error. This article explains Cato best practices for SMTP traffic and troubleshooting steps.

## Best Practices for Local SMTP Servers

## Internet Firewall Allows SMTP

We recommend configuring the Internet firewall to allow access to SMTP traffic. For more information, see [How to allow SMB/SMTP outbound traffic (or any other service).](/v1/docs/how-to-allow-smb-smtp-outbound-traffic-and-other-services)

## Egress Rule for SMTP

[Allocate an IP](/v1/docs/allocating-ip-addresses-for-the-account) address from Cato’s IP pool and configure an [egress rule](/v1/docs/how-to-configure-a-network-rule-to-egress-traffic) for the SMTP traffic. We recommend this configuration because it limits personnel who can send email traffic from your assigned IP addresses, this will ensure no blacklist shall happen.

## Troubleshooting Local SMTP Servers

These are some suggestions to help troubleshoot issues related to email delivery with internal email servers.

## Reviewing Email Logs for Blacklisting the Cato IPs

If your email is not being delivered, you need to determine why the email is getting blocked. The log messages for emails can indicate the reason for the email failure. In some instances, the delivery failure can be triggered by a third-party IP reputation service (for example, Spamhaus) used by the destination SMTP host.

- These reputation services provide a lookup service that indicates whether the IP address of the SMTP sender is considered to be trustworthy. In most cases, you will simply find Cato IPs located within Spamhaus' Policy Block List (PBL) which indicates that any SMTP traffic coming from these IPs should require SMTP authentication before allowing email to be accepted. This is expected behavior and does not indicate any kind of reputation issue with Cato IP ranges.
- IPs should ONLY be removed from the PBL if the intent is to run an **outbound mail server** on that PBL-listed IP, in this case, the Cato IP address. For more information, visit [Spamhaus PBL](https://www.spamhaus.org/faq/section/Spamhaus%20PBL).
- To confirm the backlisting by the reputation service, visit the specific website and check if the Cato IP address is listed there. For example, Spamhaus has an [online IP reputation checker](https://check.spamhaus.org/) for this purpose.
- If the Cato egress IP address is listed on any of the blacklists, you can request from the service to remove the IP address. Most websites like Spamhaus will have a simple online form that can be submitted to have the IP removed.

## Verifying DNS PTR Record

Verify the egress IP for the SMTP traffic has a DNS PTR record (reverse DNS) associated with it. If the egress IP address does not have a DNS PTR record, contact Cato [Support](https://support.catonetworks.com/hc/en-us/requests/new).

> [!NOTE]
> Note:
> 
> PTR records aren't supported for IP addresses allocated in China PoPs.

## Verifying SPF Records

Verify if any SPF records exist for the email domain. An SPF record is a way to advertise which IP addresses are allowed to send an email for a given domain. Other SMTP servers can reference the record and if they receive traffic from an IP not on that list, they might reject the email.
