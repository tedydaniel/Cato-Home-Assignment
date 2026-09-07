---
title: "Deploy the Cato Client with Intune (macOS)"
slug: "deploy-the-cato-client-with-intune-macos"
updated: 2026-09-01T14:05:40Z
published: 2026-09-01T14:05:40Z
canonical: "knowledge.catonetworks.com/deploy-the-cato-client-with-intune-macos"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy the Cato Client with Intune (macOS)

This article discusses how to configure Azure Intune to deploy and update macOS Clients for SDP users in your account.

## Overview

You can configure the Cato Management Application to use an MDM to manage the deployment and updates for macOS Clients in your organization. All Client updates are controlled using the MDM and end users don't receive notifications of new Client versions from Cato.

### High Level Workflow of Managed Deployments and Upgrades for macOS Clients

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/download_macos_package.png)

1. From the navigation menu, click **Access > Client Rollout**.
2. Click the **Upgrade Policy** tab.
3. For the macOS Client, choose **Managed by Admin**.
4. From the **Client Rollout** tab, download the macOS package.
5. Import the macOS package to Intune.
6. Configure Azure Intune to create a policy that allows the DMG extension and VPN profiles for end users.

Otherwise, end users need to manually approve and allow the above items in macOS.
7. In Azure Intune, distribute the new macOS Client version to the end users in your account.

## Importing the macOS Package

Use the Microsoft Intune Admin Center to add the Client package you want to distribute.

**Import the macOS package to Intune**

1. From the navigation menu, select **Apps > macOS**.
2. Click **Add** and under **App type**, select **macOS app (PKG)**.
3. Click **Select** and select the Cato Client package you want to upload. You will have to provide the following information:
  - Name
  - Description
  - Publisher Name
4. Under **Category**, select the **Business** and **Computer management** checkboxes, respectively.
5. Click **Next** and in the Program page, click **Next** again.
6. In the Requirements page, select the **minimum required macOS operating system** as required for the Cato Client version you are deploying.
7. In the Detection rules page, make sure you set **Ignore app version** to **No**, and click **Next**.
8. On the Assignments page, determine who will receive this package (for example, All Users), and click **Next**.
9. Click **Create**.

The macOS Client package is imported to Intune and is available in the Apps page for macOS packages.

## Automatically Allowing macOS Permissions for the Client with Intune

You can configure Intune to automatically allow these permissions for the end user as part of the installation process for the new Client version. Otherwise, the end user must manually configure the macOS settings as part of the installation process.

The following permissions are required to install the Client on a macOS host:

- Allow the Cato Client to create a VPN profile
- Allow system extensions for the Cato Client
  - There are separate system extensions for Anti-Tamper and DNS Relay features (currently in EA)

**Note:** The Early Availability (EA) features are only available for limited release. For more information, contact your Cato Networks representative or send an email to [ea@catonetworks.com](mailto:ea@catonetworks.com).

### Deploy a Custom VPN Profile

**To create a custom VPN profile:**

1. Download the custom profile attached to this article, or create your [own custom profile](/v1/docs/deploy-the-cato-client-with-intune-macos#creating-a-custom-vpn-profile).
2. From the Microsoft Intune Admin Center, navigate to **Devices > macOS > Configuration** to create a policy for the macOS Client
3. Click **Create** and select **New Policy**. (based on the data in the table above):
  1. In **Create a profile**, under **Profile type**, select **Custom**.
  2. Click **Create**.
4. In the Basics page, enter a **Name** and optional **Description** for the profile, and click **Next**.
5. In the Configuration settings page, enter the following:
  1. Provide a descriptive name for the custom profile
  2. Under Configuration profile file, upload the custom profile you downloaded above
  3. Click **Next**
6. In the Assignments page, click **Add all devices** and click **Next**.
7. Click **Create**.

### Creating a Custom VPN Profile

This article comes with a preconfigured, customized VPN profile that you can upload to Intune. If you want to create a custom VPN profile, you will need to download the [Apple Configurator tool](https://support.apple.com/apple-configurator), and create a profile using the information in the table, below.

| Setting | Value |
| --- | --- |
| Connection Name | Cato Networks VPN |
| Connection Type | Custom SSL (from the drop-down menu) |
| Identifier | com.catonetworks.mac.CatoClient |
| Server | vpn.catonetworks.net |
| Account | CatoClientVPN |
| Provider Bundle Identifier | com.catonetworks.mac.CatoClient.CatoClientSysExtension |
| User Authentication | 1. Choose the **Password** option. 2. Clear the **Send all traffic through VPN** option. |
| Provider Type | Packet Tunnel |
| Provider Designated Requirement | anchor apple generic and identifier "com.catonetworks.mac.CatoClient" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = CKGSB8CH43) |

#### Create a Profile for Deploying the macOS Package

When allowing system extensions for the Cato Client, there are separate system extensions for Anti-Tamper and DNS Relay features. If you don’t add them to the profile, then the device user is shown a pop-up message requesting permission to allow the extension.

**Create the new profile and then configure the VPN settings for that profile.**

1. From the Microsoft Intune Admin Center, navigate to **Devices > macOS > Configuration** to create a policy for the macOS Client:
2. Click **Create** and select **New Policy**. (based on the data in the table above):
  1. In **Create a profile**, under **Profile type** select **Settings catalog**.
  2. Click **Create**.
3. In the Basics page, enter a **Name** and **Description** for the profile, and click **Next**.
4. In the Configuration settings page, click **Add settings**.
  1. Using the Search box, enter **managed login items** and verify that the **Rules** setting is selected
  2. Using the Search box, enter **system extensions** and verify that **Allowed System Extensions** is selected
  3. Using the Search box, enter **notifications** and under User Experience > Notifications, verify that **Notification Settings** is selected
  4. Close the **Add settings** pane.
5. In the Configuration page, under Rules, click **Edit ins**.
  1. In the **Comment** field, enter an optional comment describing the instance
  2. In the **Rule Value** field, enter the following value from the allowed system extensions:

com.catonetworks.mac.CatoClient
  3. Click **Save**.
6. In the Configuration page, under Allowed System Extensions, click **Edit instance**.
  1. Enter the values listed in the Allowed System Extensions below:
    - `com.catonetworks.mac.CatoClient`
    - `com.catonetworks.mac.CatoClient.CatoClientSysExtension`
    - `com.catonetworks.mac.CatoClient.CatoDNSRelaySysExtension` **Note:** This extension is mandatory for DNS Relay
    - `com.catonetworks.mac.CatoClient.ProtectionSysExtension` **Note:** This extension is mandatory for Anti-Tampering
  2. Under Team Identifier, enter the value: **CKGSB8CH43**
  3. Click **Save**
7. In the Configuration page, under Notification Settings, click **Edit instance**.
  1. Under **Bundle Identifier**, enter **com.catonetworks.mac.CatoClient**
  2. Verify that **Critical Alert Enabled** is set to **True**
  3. Click **Save**
8. Click **Next**, and on the Scope tags page, click **Next** again.
9. In the Assignments page, determine who should receive this package, for example, click **Add all devices** or select a specific group of users, and click **Next**.
10. Click **Create**.

[sample_profile.mobileconfig](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/sample_profile(1).mobileconfig)
