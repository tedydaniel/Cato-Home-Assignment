---
title: "Installing the Cato Certificate on macOS Devices"
slug: "installing-the-cato-certificate-on-macos-devices"
updated: 2026-08-03T10:33:26Z
published: 2026-08-03T10:33:26Z
canonical: "knowledge.catonetworks.com/installing-the-cato-certificate-on-macos-devices"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Installing the Cato Certificate on macOS Devices

When using the Cato SDP Client, we recommend that you install the Cato CA certificate on the device to provide the best security and user experience. In addition, depending on the settings for your organization, the Cato certificate is required to connect to the network.

## Overview

To ensure secure connectivity and optimal performance with the Cato Client on macOS devices, users should install the Cato CA certificate as a trusted certificate.

System admins can download the Cato certificate and use a Device Management system to distribute and install it on macOS devices with no action required by the end-user. If necessary, end-users can download and manually install the Cato certificate as a trusted certificate for the macOS device.

## Installing the Cato Certificate

Follow these steps to install the Cato certificate as a trusted certificate on the macOS device.

> [!NOTE]
> Note:
> 
> For versions higher than the macOS Client v5.5, the Cato certificate is automatically installed when the Cato Client is installed.

**To install the Cato certificate:**

1. Download the Cato certificate from the [Client download portal](https://clientdownload.catonetworks.com/).
2. Open the **Keychain Access** screen, and select **File > Import Items**.
3. Select the certificate file you downloaded in step 1 and click **Open**.

If necessary, enter the user name and password to allow modifying the system keychain.

![01_import_cert.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27700863600157.png)
4. If the Cato certificate is not trusted, perform these steps:
  1. Select the **Cato Networks CA** certificate and select **File > Get Info**.
  2. Expand the **Trust** section, and in **When using this certificate**, select **Always Trust**.

![02_keychain_cert.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27700848439325.png)
  3. Close the **Cato Networks CA** window.

If necessary, enter the user name and password to allow modifying the system keychain.
5. The Cato certificate is installed on the device.

![03_trusted_cert.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27700838839709.png)
