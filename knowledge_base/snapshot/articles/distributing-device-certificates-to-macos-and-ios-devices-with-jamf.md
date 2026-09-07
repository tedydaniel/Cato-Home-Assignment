---
title: "Distributing Device Certificates to macOS and iOS Devices with Jamf"
slug: "distributing-device-certificates-to-macos-and-ios-devices-with-jamf"
status: "update"
updated: 2026-09-03T07:09:53Z
published: 2026-09-03T07:09:53Z
canonical: "knowledge.catonetworks.com/distributing-device-certificates-to-macos-and-ios-devices-with-jamf"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Distributing Device Certificates to macOS and iOS Devices with Jamf

This article explains how to distribute device certificates used for device checks to macOS and iOS devices using Jamf.

> [!NOTE]
> Note:
> 
> This article is based on Jamf versions up to February 2024. For troubleshooting, please contact Jamf support.

## Overview

You can distribute your corporate self-signed certificates to macOS and iOS devices in your network using Jamf as your MDM. This streamlines the distribution of device certificates across devices. By managing certificate distribution through an MDM, you can centrally control certificate deployment, ensuring robust security measures are consistently enforced.

### Prerequisites

- The device certificate is distributed before the Client is installed on a device
- You must have administrator permissions for the macOS device

**Note**: users with root permissions on the device can export the certificate and the private key, we highly recommend that IT admins will restrict it
- The certificate file must be in a PFX (p12) format
- You must know the password protecting the key (required to install the certificate)
- The certificate ‘issuer’ must match the signing certificate that is uploaded in the Cato Management Application
- Certificates have a maximum allowed size of 2048 bytes. Certificates larger than this size will be ignored

## Distributing Certificates for macOS and iOS Devices

Follow these steps to distribute device certificates to macOS and iOS devices:

> [!NOTE]
> Note:
> 
> From macOS Client v5.4 enabling the VPN payload and installing the VPN profile are not required. iOS versions still require this step.

- Step 1: Enable the certificate payload
- Step 2: Enable the VPN payload (this is only required on iOS devices and macOS Client v5.3 and below)
- Step 3: Install the VPN profile (this is only required on iOS devices and macOS Client v5.3 and below)

### Step 1: Enabling the Certificate Payload

Upload the required certificate to the new Configuration profile.

**To enable the certificate payload:**

1. From the navigation menu, select **Configuration Profiles**.
2. Click **New**.

The **New Configuration Profile** screen is displayed.
3. Select the **Certificate** tab and click **Configure**.
4. Upload the certificate and enter the Certificate Name and Password.
5. Ensure **Allow all apps access** is selected.
6. Select the **Scope** tab and define the computers or users.

### Step 2: Enabling the VPN payload (macOS v5.3 and below)

This step is only required for distributing certificates to iOS devices or macOS devices with Client version v5.3 and below.

1. Go to the **VPN** payload and enable it.
2. Configure the VPN connection using the following settings:
  - **Connection Type:** Custom SSL
  - **Identifier:**
    - For macOS: com.catonetworks.mac.CatoClient
    - For iOS: CatoNetworks.CatoVPN
  - **Server:** vpn.catonetworks.net
  - **Account:** add the account name ‘CatoClientVPN’.
  - **ProviderBundle Identifier:** **Note:** Use the identifier exactly as written below (including the misspelling of extension on the iOS identifier):
    - For macOS: com.catonetworks.mac.CatoClient.CatoClientSysExtension
    - For iOS: CatoNetworks.CatoVPN.CatoVPNNEExtenstion
  - **Provider Designated Requirement:** empty
  - **User Authentications:** Certificate
  - **Provider Type:** Packet Tunnel
  - **Credentials:** Choose the certificate from the ‘Certificates’ payload
  - **Proxy Setup:** None

3. Save the profile to a file.

### Step 3: Installing the VPN Profile (macOS v5.3 and below)

This step is only required for distributing certificates to iOS devices or macOS devices with Client version v5.3 and below.

**To install the VPN profile file:**

- On macOS devices:
  - Double click on the profile file
- On iOS device
  - Remotely send the VPN profile to your devices
