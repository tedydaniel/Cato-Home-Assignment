---
title: "Activating New Cato Cert for Accounts with Cato Block Page and TLSi Disabled"
slug: "activating-new-cato-cert-for-accounts-with-cato-block-page-and-tlsi-disabled"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/activating-new-cato-cert-for-accounts-with-cato-block-page-and-tlsi-disabled"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Activating New Cato Cert for Accounts with Cato Block Page and TLSi Disabled

As was [announced,](/v1/docs/product-update-november-11-2024) the default Cato certificate used in your account expires in October 2025, and a new certificate is available. This certificate ensures the [Cato block page](/v1/docs/certificate-warnings-with-blocked-https-websites) is displayed if a user tries to access a blocked website.

From July 27, 2025, we will start deploying the new default Cato certificate as the default certificate for the Cato block page. To ensure your users continue to receive the Cato block page and not the browser block page, the new certificate needs to be:

- Enabled for your account
  - Cato will automatically enable the certificate on your behalf over the next few weeks
- Distributed to your devices

Devices without the new certificate may not receive the Cato block page after July 27, 2025.

## What Action Do I Need to Take?

Cato will enable the new certificate on your behalf. You need to ensure the new certificate is distributed to any device you want the Cato block page to be displayed on.

## How Do I Distribute the Certificate to Devices?

The new certificate is already installed on devices using the Windows Client version 5.11 and higher or macOS Client version 5.7 and higher. No additional action is needed for these devices.

If you have devices with lower Client versions, other operating systems, or without a Client installed, you need to distribute the new certificate with an MDM or install it manually. You can download the new certificate from the **Security > Certificate Management** page.

You can view the Client version used on all devices in your account from the [Access > Access Overview](/v1/docs/using-the-access-overview-page) page.

## What is the Impact to the Account?

Starting from July 27, 2025, a user who does not have the new certificate installed on their device may receive the browser block page instead of the Cato block page when trying to access a blocked website.

This change in user experience may result in users not understanding why access has been blocked.
