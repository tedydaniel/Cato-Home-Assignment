---
title: "FAQs - Upgrading to macOS Client v5.10 (Aug 2025)"
slug: "faqs-upgrading-to-macos-client-v5-10-aug-2025"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/faqs-upgrading-to-macos-client-v5-10-aug-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# FAQs - Upgrading to macOS Client v5.10 (Aug 2025)

**Does macOS support remote internet security with one-time authentication?**

Remote internet security with one-time authentication is supported in the macOS Client starting from version 5.10, which is planned to be released in August 2025.

**What impact will upgrading to macOS Client v5.10 have on my users?**

These are the changes that may impact your users when upgrading to macOS Client v5.10:

- The macOS Client has new indications showing users if they have **Secured Internet Access** and **Secured Private Access** to your WAN.
- Once you upgrade to macOS Client v5.10, existing rules in your Client Connectivity policy that require **low** confidence and allow Internet access will apply to macOS Client v5.10 users. This means after a one-time authentication, those macOS users would always have Internet access.

For example, in the following policy, macOS Client v5.9 Client users would match rule 1, but macOS Client v5.10 users would also match rule 3 even if their session token has expired.

![image__12_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29648921992477.png)

**What changes do I need to make to support users upgrading to macOS Client v5.10?**

If you were using this capability for your users with the Windows client, we recommend that you carefully review your Client Connectivity policy to verify that your rules reflect your business requirements.

Look for rules with the following properties:

- Confidence is set to **low**
- Device is set to **any**
- Action is set to **allow Internet** access

Rules that are set for **Windows** devices are not impacted by upgrading to macOS Client v5.10.

If you’d like to allow macOS users to maintain secure Internet access after their initial authentication (even if their token expires), you can update your Client Connectivity Policy rules to take advantage of this new capability.

**What are the changes to the macOS v5.10 client?**

We added the following fields to the home screen indicating the user's connection status:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29650634374813.jpeg)
