---
title: "Installing the Cato Certificate on iOS Devices"
slug: "installing-the-cato-certificate-on-ios-devices"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/installing-the-cato-certificate-on-ios-devices"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Installing the Cato Certificate on iOS Devices

This article explains how to install the Cato Certificate on an iOS device.

## Overview

When using the Cato SDP Client, we recommend that you install the Cato CA certificate on the device to provide the best security and user experience. In addition, depending on the settings for your organization, the Cato certificate is required to connect to the network.

System admins can download the Cato certificate and use a Device Management system to distribute and install it on iOS devices with no action required by the end-user. If necessary, end-users can download and manually install the Cato certificate as a trusted certificate for the iOS device.

## Installing the Cato Certificate

To install the Cato Certificate, first download the certificate and then install it on your device.

**To install the Cato certificate on an iOS device:**

1. Using the Safari browser, download the Cato certificate from the [Client download portal.](https://clientdownload.catonetworks.com/)

**Note:** For successful certificate installation, the user must download the certificate using the device's default Safari browser.

![iOS_Cert.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218308042269.png)
2. On the iOS device, navigate to **Settings > General > VPN & Device Management** and click on the **Cato Networks CA** downloaded profile.
3. Click **Install**.

![Install.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218291866781.png)
4. Enter your passcode and click **Install**.
5. Navigate to **Settings > General > About > Certificate Trust Settings** and enable full trust for root certificate for Cato Networks CA.

![Trust_Settings.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218278581661.png)

The Cato certificate is installed on your device.
