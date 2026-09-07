---
title: "Distributing Device Certificates to Windows Devices With Certutil"
slug: "distributing-device-certificates-to-windows-devices-with-certutil"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/distributing-device-certificates-to-windows-devices-with-certutil"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Distributing Device Certificates to Windows Devices With Certutil

This article explains how to distribute device certificates used for device checks to Windows Devices using the Certutil.exe command-line program.

## Overview

You can distribute your corporate self-signed certificates to Windows devices in your network using the Certutil.exe command-line program. This streamlines the distribution of device certificates across devices so you can centrally control certificate deployment, ensuring robust security measures are consistently enforced.

### Prerequisites

- You must have administrator permissions for the Windows computer
- The certificate file must be in a PFX (p12) format, including its private key
- The certificate ‘issuer’ must match the signing certificate that is uploaded in the Cato Management Application
- You must install the certificate into the certificate manager of the device
- You must know the password protecting the key (required to install the certificate)
- Certificates have a maximum allowed size of 2048 bytes. Certificates larger than this size will be ignored

## Installing the Device Certificate

There are several ways to install a certificate on a Windows device. The following example shows how to install a certificate using the Certutil command line program.

**To import a certificate with Certutil:**

1. Open the command prompt as administrator (elevated) and use the certutil.exe:

certutil -csp "Microsoft Software Key Storage Provider" -importpfx My <path-to-p12-file> NoExport
2. After you run this command, you are prompted for the password of the p12 file.
3. Enter the certificate file password. Alternatively, you can pass the password on the command line with the -p option.

The following command is an example of the certutil with the password parameter:

certutil -csp KSP -p &lt;secret&gt; -importpfx My <path-to-p12-file> NoExport

**Notes:**

- The NoExport option prohibits export of the private key
- KSP is an alias for Microsoft Software Key Storage Provider
- The -csp option is used to specify where the private key is stored. Although it is optional, we recommend that you explicitly specify the provider as the default

### Verifying the Certificate Installation

You can confirm that the certificate is successfully installed on the device with certutil:

**certutil -store My**

This command lists the machine certificate information. If the certificate was successfully installed then it appears in this list.

Now, you can connect to the Cato Cloud with a device certificate.

When the Client successfully connects to the Cato Cloud, it saves the device certificate that was last used in the registry for future connections. This helps to reduce the connection time.
