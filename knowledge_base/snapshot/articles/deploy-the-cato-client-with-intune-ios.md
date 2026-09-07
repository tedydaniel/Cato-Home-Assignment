---
title: "Deploy the Cato Client with Intune (iOS)"
slug: "deploy-the-cato-client-with-intune-ios"
updated: 2026-06-22T09:24:33Z
published: 2026-06-22T09:24:33Z
canonical: "knowledge.catonetworks.com/deploy-the-cato-client-with-intune-ios"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy the Cato Client with Intune (iOS)

This article discusses how to configure Azure Intune to deploy and update iOS Clients for SDP users in your account.

This feature is supported for iOS Client v5.0 and higher.

## Overview

Starting with iOS Client v5.0, you can configure the Cato Management Application to use an MDM to manage the deployment and updates for iOS Clients in your organization. All Client updates are uploaded to the App Store, and end users don't receive notifications of new Client versions.

### High-Level Workflow of Managed Deployments and Upgrades for iOS Clients

This is an overview of the workflow to implement an MDM solution for iOS Clients in your account.

1. Contact your support representative to get the latest iOS package.
2. Import the iOS package to Azure Intune.
3. Configure Azure Intune to create a policy that allows the PKG extension and VPN profiles for end users.

Otherwise, end users need to manually approve and allow the above items in iOS.
4. In Azure Intune, distribute the new iOS Client version to the end users in your account.

## Importing the iOS App

Use the Microsoft Intune Admin Center to add the Client app you want to distribute.

**Install the iOS app from Intune**

1. From the navigation menu, select **Apps > iOS/iPadOS**.
2. Click **Create** and under **App type**, select **iOS store app**.
3. Click **Select**.
4. Click **Search the App Store** and enter Cato Client
5. Click **Cato Client** and click **Select**
6. Click **Next** and in the Assignments page, determine who will receive this package (for example, All Users), and click **Next**.
7. Click **Create**.

## Automatically Allowing iOS Permissions for the Client with Intune

Starting with the iOS Client v5.0, the following permissions are required to install the Client on an iOS host:

- Allow the Cato Client to create a VPN profile
- Allow Cato Client notifications

You can configure Intune to automatically allow these permissions for end users as part of the installation process for the new Client version. Otherwise, the end user must manually configure the iOS settings as part of the installation process.

### Creating a Custom VPN Profile

This article comes with a preconfigured, customized VPN profile that you can upload to Intune. If you want to create a custom VPN profile, you will need to download the [Apple Configurator tool](https://support.apple.com/apple-configurator), and create a profile using the information in the table, below.

| Setting | Value |
| --- | --- |
| Connection Name | Cato Networks VPN |
| Connection Type | Custom SSL (from the drop-down menu) |
| Identifier | CatoNetworks.CatoVPN |
| Server | vpn.catonetworks.net |
| Account | CatoClientVPN |
| Provider Bundle Identifier | CatoNetworks.CatoVPN.CatoVPNNEExtenstion |
| Provider Designated Requirement | Leave this field empty |
| User Authentication | 1. Choose the **Password** option. 2. Clear the **Send all traffic through VPN** option. |
| Provider Type | Packet Tunnel |

#### Adding a Certificate for Device Posture

If you have a device posture certificate for authentication, do the following:

> [!NOTE]
> Available from Client iOS v5.6 and later.

1. On the Apple Configurator tool select Certificates.
2. Click the + icon.
3. Select your certificate and enter the certificate password (if required)
4. Under the VPN section, select **Certificate** in the **User Authentication** drop-down menu.
5. Select your certificate.

#### Allows Users to Temporarily Disable Always-On

By default, the profile provide by Cato includes protection preventing users from disabling Always-On for the Cato Client.

If you want to enable users to disable Always-On, you can remove lines 44-54 in the attached profile.

> [!NOTE]
> This option is available for iOS version 16 and later.

### Deploy a Custom VPN Profile

**Create a custom VPN profile.**

1. Download the custom profile attached to this article, or create your [own custom profile](/v1/docs/deploy-the-cato-client-with-intune-ios#creating-a-custom-vpn-profile).
2. From the Microsoft Intune Admin Center, navigate to **Devices > iOS/iPadOS > Configuration** to create a policy for the iOS Client
3. Click **Create** and select **New Policy**.
  1. In **Create a profile**, under **Profile type** select **Custom**.
  2. Click **Create**.
4. In the Basics page, enter a **Name** and optional **Description** for the profile, and click **Next**.
5. In the Configuration settings page, enter the following:
  1. Provide a descriptive name for the custom profile
  2. Under Configuration profile file, upload the custom profile you downloaded above
  3. Click **Next**
6. In the Assignments page, click **Add all devices** and click **Next**.
7. Click **Create**.

### Create a Profile for Deploying the iOS Settings

**Create the new profile and then configure the VPN settings for that profile.**

1. From the Microsoft Intune Admin Center, navigate to **Devices > iOS > Configuration** to create a policy for the iOS Client:
2. Click **Create** and select **New Policy**:
  1. In **Create a profile**, under **Profile type** select **Settings catalog**.
  2. Click **Create**.
3. In the Basics page, enter a **Name** and **Description** for the profile, and click **Next**.
4. In the Configuration settings page, click **Add settings**.
  1. Using the Search box, enter **notifications** and under User Experience > Notifications that **Notification Settings** is selected
  2. Close the Add settings pane
5. In the Configuration page, under Notification Settings, click **Edit instance**.
  1. In the **Bundle Identifier**, enter CatoNetworks.CatoVPN
  2. Verify that **Critical Alert Enabled** is set to **True**
  3. Click **Save** and then **Next**.
6. On the Scope tags page, click **Next** again.
7. In the Assignments page, determine who should receive this package, for example, click **Add all devices** or select a specific group of users, and click **Next**.
8. Click **Create**.

[sample_profile_ios.mobileconfig](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/sample_profile_ios.mobileconfig)
