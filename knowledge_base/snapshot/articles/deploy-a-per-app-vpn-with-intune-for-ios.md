---
title: "Deploy a Per App VPN with Intune for iOS"
slug: "deploy-a-per-app-vpn-with-intune-for-ios"
updated: 2026-07-05T06:54:02Z
published: 2026-07-05T06:54:02Z
canonical: "knowledge.catonetworks.com/deploy-a-per-app-vpn-with-intune-for-ios"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy a Per App VPN with Intune for iOS

This article discusses how to configure Azure Intune to deploy a per-app VPN for your account.

## Overview

Per-App VPN on iOS lets you selectively tunnel only specific enterprise applications through the Cato Cloud while allowing personal apps and internet traffic to bypass the VPN profile.

With per-app VPN behavior, you can isolate sensitive traffic such as corporate email, SaaS applications, and internal services. At the same time, personal apps such as social media, streaming, and general browsing continue to use the device’s regular network. This reduces bandwidth and latency overhead, improves user privacy, and simplifies compliance

### Prerequisites

- Ensure that Microsoft Intune company portal app is installed on the devices where you want to install the per-app VPN profile
- Supported for iOS Client v5.8 and higher

### Notes

- Office Mode is not compatible with a per-app VPN
- Split tunnel configurations are not applied when working with a per-app VPN as the tunneling determinations are made in the VPN profile
- Bypassing the Cato Cloud is not supported when working with a per-app VPN as the tunneling determinations are made in the VPN profile

### Use Case

ABC Company allows employees to use personal iPhones to access company resources such as Salesforce, Microsoft Teams, and more. However, the IT team needs to ensure that all enterprise traffic is routed through the Cato Cloud, while personal browsing and apps remain outside the VPN tunnel.

To enforce this, the team deploys a Per-App VPN configuration using Microsoft Intune. They define a VPN profile that includes only the corporate apps, and assign the profile to user groups with enrolled iOS devices. As a result, work apps automatically connect to the Cato Cloud, while personal apps such as Instagram, WhatsApp, or Safari are accessed directly through the mobile connection.

### High-Level Workflow For Deploying a Per App VPN

This is an overview of the workflow to implement a per app VPN for iOS Clients in your account.

1. Configure the VPN profile settings
2. Add the users and groups to whom the VPN profile applies
3. Configure the apps that must go through the VPN tunnel and the apps that are excluded from the VPN tunnel
4. Distribute the VPN profile

## Configure a Per-App VPN for iOS

Use the Microsoft Intune Admin Center to configure a per-app VPN for iOS.

![ios-per-app-config.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34696051008797.png)

**To configure the per-app VPN:**

1. From the navigation menu, select **Devices > iOS/iPadOS** and under Manage Devices, click **Configuration**.
2. Click **Create > New Policy** and enter the following:
  - Under **Profile type**, select **Templates**
  - Under **Template name**, select **VPN** provide a descriptive name, and click **Next**.
3. In the Configuration settings page, enter the following:
  - Under **Connection type**, select Custom VPN
  - Enter a descriptive name for the connection name, for example, Cato Per-App VPN
  - In the **VPN server address** field, enter `vpn.catonetworks.net`
  - Under **the Authentication method**, select **Username and password**.
  - Under **Split tunneling**, click **Disable**.
  - In the **VPN identifier** field, enter `CatoNetworks.CatoVPN`
  - Enter the custom VPN attribute:
    - **Key** - SingleSignOn
    - **Value** - True
4. Under **Automatic VPN** settings, in the **Type of automatic VPN** field, select **Per-app VPN**.
5. Under **Provider Type**, select **packet-tunnel**.
6. Under **Safari URLs that will trigger this VPN**, enter the following:
  - catonetworks.com
  - sso.ias.catonetworks.com
7. Under **Excluded Domains**, enter `push.apple.com`
8. Click **Next** and continue below to add users and groups.

## Define the Users and Groups for the Per-App VPN

You can define which apps are tunneled through the per-app VPN, and which can go outside of the VPN tunnel. If the app that you want to tunnel is already installed on the device, you must uninstall and reinstall the app after applying the per-app VPN profile.

![ios-per-app-groups.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34696057839773.png)

**To add users and groups to the per-app VPN:**

1. In the Assignments page, click **Add groups**
2. Select the groups you want to add and click **Select**.
3. (Optional) Within the group you selected, you can also select excluded groups to whom the per-app VPN will not apply.
4. Click **Next** and **Create**.

## Configure Apps for the VPN Profile

![ios-per-app-apps.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34696040426013.png)

**Configure the apps that must use the VPN profile:**

1. From the navigation menu, select **Apps** and under Manage apps by platform, click **iOS/iPadOS**.
2. Click **Create** to add a new app or select an app from the existing list.

You must include at least the Cato Client as an app that uses the profile.
3. In the Assignments page, select the same groups as above for whom the apps are available, and click **Select**.
4. In the VPN column, click **None** and in the Edit assignment page, under **App settings > VPN** select the per app VPN you created above.
5. Click **Next** and **Create**.

## Deploy the Custom VPN Profile on End User Devices

The following section provides information about how your end users can apply the per-app vpn profile on their devices. When they access an app that is defined as requiring the VPN tunnel, the Cato Client automatically connects.

**To deploy the per-app VPN**

1. From the Azure Intune company portal app, click **Begin setup**.
2. Authenticate to your company portal.
3. When prompted to download the management profile, click **Allow**.
4. After the profile is downloaded, click **Continue**.
5. Follow the instructions to install the profile:
  1. Go to the Settings app on your device
  2. Under **VPN and Device Management**, click **Install**.

After you complete the profile installation, return to the Azure Intune company portal.
6. In the company portal, when prompted, select **Yes, I installed the profile** and then click **Continue**.
7. For each app that requires the per-app VPN, you will be prompted to allow the app to be managed. Click **Manage**.

If you don't allow the app to be managed, you won't be able to access the resource.

When the process has completed successfully, in the Cato Client you will see in the Statistics page that Per-App VPN is set to **Yes**.
