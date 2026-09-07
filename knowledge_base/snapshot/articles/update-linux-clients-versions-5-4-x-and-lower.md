---
title: "Update Linux Clients Versions 5.4.x and Lower"
slug: "update-linux-clients-versions-5-4-x-and-lower"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/update-linux-clients-versions-5-4-x-and-lower"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Linux Clients Versions 5.4.x and Lower

We are letting you know of a security vulnerability ([CVE-2025-7012](/v1/docs/cve-2025-7012-linux-sdp-client-local-privilege-escalation)) that was recently identified and impacts Cato Linux Clients with versions lower than 5.4.x. This vulnerability can let attackers who have access to the Linux Client on the device escalate their privileges. We released a new version of the Cato Linux Client version 5.5 that includes a security patch that fixes this vulnerability.

We see that there are ZTNA (SDP) users in your account with Linux devices that used Linux Clients with versions v5.4 and lower within the past 30 days and are potentially vulnerable to attacks. We strongly recommend that you make sure that all Linux Clients are upgraded to Linux Client version v5.5 to protect against the vulnerability. You can download the latest Linux Client version from the [Cato Client download portal](https://clientdownload.catonetworks.com/).

To the best of our knowledge, none of these issues has been exploited in the wild.

## What Changes Do I Need to Make?

Use the [Access Overview Dashboard](/v1/docs/using-the-access-overview-page) to identify users who have a Linux Client with versions v5.4 and lower, and make sure that they upgrade to at least Linux Client version v5.5 to receive the most recent security patches and enhancements.

## What is the Impact to the Account?

If you don’t upgrade to Linux Client v5.5 or higher, devices with older Linux Client versions are vulnerable to malicious attacks related to CVE-2025-7012.

To the best of our knowledge, none of these issues has been exploited in the wild.

## Who Do I Talk to If I Have Questions?

If you have questions or encounter issues, please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).
