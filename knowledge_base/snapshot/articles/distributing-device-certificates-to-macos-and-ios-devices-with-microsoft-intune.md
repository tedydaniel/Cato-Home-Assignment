---
title: "Distributing Device Certificates to macOS and iOS Devices with Microsoft Intune"
slug: "distributing-device-certificates-to-macos-and-ios-devices-with-microsoft-intune"
updated: 2026-06-22T09:24:17Z
published: 2026-06-22T09:24:17Z
canonical: "knowledge.catonetworks.com/distributing-device-certificates-to-macos-and-ios-devices-with-microsoft-intune"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Distributing Device Certificates to macOS and iOS Devices with Microsoft Intune

This article explains how to distribute device certificates used for device checks to macOS and iOS devices using Microsoft Intune.

> [!NOTE]
> **Note**: This article is based on Intune versions up to February 2024. For troubleshooting, please contact Microsoft support.

## Overview

You can distribute your corporate self-signed certificates to macOS and iOS devices in your network using Microsoft Intune as your MDM. This streamlines the distribution of device certificates across devices. By managing certificate distribution through an MDM, you can centrally control certificate deployment, ensuring robust security measures are consistently enforced.

To distribute certificates to macOS and iOS devices using Microsoft Intune, first create a profile with the certificate in Apple Configurator and then distribute the profile with Microsoft Intune.

### Prerequisites

- The device certificate is distributed before the Client is installed on a device
- You must have administrator permissions for the macOS device

**Note**: users with root permissions on the device can export the certificate and the private key, we highly recommend that IT admins will restrict it
- The certificate file must be in a PFX (p12) format
- You must know the password protecting the key (required to install the certificate)
- The certificate ‘issuer’ must match the signing certificate that is uploaded in the Cato Management Application
- Certificates have a maximum allowed size of 2048 bytes. Certificates larger than this size will be ignored

## Distributing Device Certificates to macOS and iOS Devices with Microsoft Intune

Follow these steps to distribute device certificates to macOS and iOS devices:

- Step 1: Create an Apple Configurator profile
- Step 2: Enable the certificate payload
- Step 3: Enable the VPN payload (this is only required on iOS devices and macOS Client v5.3 and below)
- Step 4: Distribute the profile with Microsoft Intune

### Step 1: Creating an Apple Configurator Profile

If you do not have Apple Configurator, it can be downloaded from the App Store.

![Screenshot_2024-03-18_at_11_34_43.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218256880925(1).png)

**To create an Apple Configurator Profile:**

- In Apple Configurator, click **File > New Profile**.

A new configuration profile document window appears.

### Step 2: Enabling the Certificate Payload

Upload the required certificate to the new profile.

![Certificate_intune.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218265143069(1).png)

**To enable the certificate payload:**

1. In Apple Configurator, from the navigation menu, click **Certificates**.
2. Click **Configure**.
3. Choose the certificate you want to distribute.
4. (Optional) Enter the certificate Password.

### Step 3: Enabling the VPN Payload

This step is only required for distributing certificates to iOS devices or macOS devices with Client version v5.3 and below.

![VPN_intune.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218235382941(1).png)

**To enable the VPN Payload:**

1. In Apple Configurator, from the navigation menu, click **VPN**.
2. Click **Configure**.
3. Configure the following settings:
  - **Connection Name:** Choose a name for the connection
  - **Connection Type:** Custom SSL
  - **Identifier:**
    - For macOS: com.catonetworks.mac.CatoClient
    - For iOS: CatoNetworks.CatoVPN
  - **Server:** vpn.catonetworks.net
  - **Account:** Add your account name. For example: CatoNetworksAccount
    - For iOS Client v5.6 and above: set the account as CatoClientVPN
  - **ProviderBundle Identifier:**

**Note:** Use the identifier exactly as written below (including the misspelling of extension on the iOS identifier):
    - For macOS: com.catonetworks.mac.CatoClient.CatoClientSysExtension
    - For iOS: CatoNetworks.CatoVPN.CatoVPNNEExtenstion
  - **Provider Designated Requirement:** empty
  - **User Authentication:** Certificate
  - **Credential:** Select the certificate you uploaded in step 1
  - **Provider Type:** Packet Tunnel
  - **Proxy Setup:** None
4. Click **File > Save**.

### Step 4: Distributing the Profile

Use Microsoft Intune to distribute the profile you created in Apple Configurator.

![Intune.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218251413533(1).png)

**To distribute the profile:**

1. In Microsoft Intune, from the navigation menu, navigate to **Devices > iOS/iPadOS or macOS > Configuration profiles**.
2. Click **Create > New Policy**.
3. From the **Profile type** drop down, select **Templates**.
4. Select the **Custom** template and click **Create**.

A custom template is created.
5. On the **Basics** tab, choose a name for the profile and click **Next**.
6. On the **Configuration settings** tab, choose a **Custom configuration profile name**.
7. Upload the profile you created in Apple Configurator and click **Next**.
8. Configure the Scope tags and Assignments of the configuration profile.
9. Review and Create the configuration profile.
