---
title: "Users Are Getting \"Your connection is Not Secure\" Message While Browsing Websites"
slug: "users-are-getting-your-connection-is-not-secure-message-while-browsing-websites"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/users-are-getting-your-connection-is-not-secure-message-while-browsing-websites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Users Are Getting "Your connection is Not Secure" Message While Browsing Websites

## Issue

When connections go through Cato, users are encountering the 'Your connection is not secure' message while browsing websites.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/360010067538.png)

## Environment

Users hit into this issue when their connections are going through Cato cloud.

## Troubleshooting

This error message appears if the Cato certificate isn't installed on the computer or device. The certificate is used to show the Cato **block** or **prompt** page, and also for TLS inspection (when enabled). Refer to [How-to-Verify-if-Cato-or-Custom-Root-Certificate-is-Installed](/v1/docs/how-to-verify-if-cato-or-custom-root-certificate-is-installed) on how to validate whether the Cato certificate is installed on the computer.

Please note that if a private certificate is activated as shown below, you should install the private CA instead.

![customcert.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13642193781661.jpeg)

## Solution

To ensure that the returned certificate is trusted and prevent the occurrence of this message, please proceed with installing the certificate on your device. To install a certificate into the Trusted Root Certification Authorities store in Windows, follow [Installing-the-Root-Certificate-for-TLS-Inspection](/v1/docs/installing-the-cato-certificate-on-windows-devices).
