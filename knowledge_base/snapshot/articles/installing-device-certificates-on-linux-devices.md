---
title: "Installing Device Certificates on Linux Devices"
slug: "installing-device-certificates-on-linux-devices"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/installing-device-certificates-on-linux-devices"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Installing Device Certificates on Linux Devices

This article explains how to install device certificates used for device checks on Linux devices.

## Overview

To install device certificates on your Linux Device, first create the certificate and then install it on the device.

### Prerequisites

- You must have administrator permissions for the Linux computer
- The certificate file must be in a PFX (p12) format, including its private key
- The certificate issuer must match the signing certificate that is uploaded in the ​[Access > Client Access> Signing Certificates​​](/v1/docs/managing-signing-certificates-for-remote-access) page in the Cato Management Application
- Certificates have a maximum allowed size of 2048 bytes. Certificates larger than this size will be ignored

### Installing and Configuring the Certificate

1. Step 1: Create the device certificate
2. Step 2: Install the certificate with the following command:

`cato-sdp import-cert &lt;certificate path&gt;/&lt;certificate&gt;.p12`

### Creating a Device Certificate

This section is an example of commands to create an OpenSSL certificate that the Client accesses for Device Authentication. You can use other tools to create the certificate.

You must have your own signing certificate before you create the device certificate.

```plaintext
openssl genrsa -out <name>.key 2048

openssl req -new -key <name>.key -out <name>.csr

sudo openssl x509 -req -in <name>.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out <name>.crt -days 500 -sha256

openssl pkcs12 -export -out <name>.p12 -inkey <name>.key -in <name>.crt
```

In the example above, there is NO password added to the `openssl pcks12` command.

### Enabling the Device Certificate on the Client

This is required on Linux Client versions below v5.1

Copy the certificate and the file with the private key to the Linux device. When you run the Client, add the `-cert` argument. For more about arguments for the Linux Client, see [Installing and Running the Linux Client (v5.1 and above)](/v1/docs/getting-started-with-the-linux-client)

**To enable the device certificate on the Linux Client:**

1. Copy the device certificate and the private key file (**<name>.p12**) to a director that the Client has permissions to access.
2. When you run the Client, add this argument: **-cert <path to the p12 file>**.
