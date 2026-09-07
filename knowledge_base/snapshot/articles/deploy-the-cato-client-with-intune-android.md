---
title: "Deploy the Cato Client with Intune (Android)"
slug: "deploy-the-cato-client-with-intune-android"
updated: 2026-06-22T09:24:17Z
published: 2026-06-22T09:24:17Z
canonical: "knowledge.catonetworks.com/deploy-the-cato-client-with-intune-android"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy the Cato Client with Intune (Android)

This article explains how to use Microsoft Intune to deploy and manage the Cato Android Client for Android devices using Android Enterprise and Managed Google Play.

## Overview

You can use Microsoft Intune to centrally deploy and manage the Cato Android Client on managed Android devices. This helps you standardize Client deployment, reduce manual installation, and control app assignment through Android Enterprise and Managed Google Play.

For organizations that require continuous secure connectivity, you can use Intune to configure the Cato Android Client with an Always-On connection. For this deployment, enable lockdown mode in Intune to enforce a continuous secure connection and block network access when the Client is not connected to the Cato Cloud.

For more information, see:

- [Distributing Device Certificates to Android Devices with Microsoft Intune](/v1/docs/distributing-device-certificates-to-android-devices-with-microsoft-intune)
- [Deploying Cato Android for Work Profiles with Intune](%%LINK:36225510863773%%)

### Prerequisites

Before deploying the Cato Client, ensure the following prerequisites are met:

**Microsoft Requirements:**

- Microsoft Intune subscription
- Microsoft Entra ID (Azure AD)
- Administrator permissions in Intune

**Android Requirements:**

- Android Enterprise configured in Intune
- Managed Google Play connected to Intune
- Android devices enrolled in Intune

## High-Level Workflow of Managed Deployments

1. Link your Android Enterprise account with Microsoft Intune.
2. Import the Cato Android Client from Managed Google Play to Microsoft Intune.
3. (Optional) For Always-On configure and enable lockdown mode.
4. Assign the application to users.
5. Enroll the devices in Microsoft Intune.

## Link Android Enterprise with Intune

Before deploying Android applications, you must connect Android Enterprise and Managed Google Play to Microsoft Intune.

**To link Android Enterprise and Managed Google Play with Intune:**

1. From the navigation menu, select **Devices > Android**, and select **Enrollment**.
2. Click **Managed Google Play**.
3. Select the **I agree** checkbox and click the **Connect to Google now** button. In the pop-up window, complete the business registration steps.
4. If the registration process is successful, the status will change to **Setup** along with a green checkmark.

![1-android.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36225235503773(1).png)

## Import the Cato Android Client

Use Managed Google Play to import the Cato Android Client into Intune.

**To install the Android app from Intune:**

1. From the navigation menu, select **Apps > Android**.
2. Click **Create** and under **Category**, select **store app**.
3. Under App type, select **Managed Google Play app**.
4. Click **Select**.
5. Search for **Cato Client**, click **Select** and **Sync**.

![2-android.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36225222120861(1).png)
6. Return to Intune and allow a few minutes for sync.
7. Once the **Cato Client** app is added to the list, click the app.
8. Click **Properties,** and next to **Assignments,** click **Edit**.
9. Under the **Required** section, select the user, devices, or groups (for example, **All Users**) to which the app is to be deployed, and then click **Save**.

## Always-On and Lockdown for Android

Always-On VPN lets Android automatically connect and reconnect the Cato Client. When you enable Lockdown mode together with Always-On VPN, all network traffic is forced through the VPN tunnel, and network access is blocked when the Client is disconnected.

With Lockdown mode, if the Client can't connect to the network, then the device can't access the Internet.

![3-android.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36225235505821(1).png)

**To configure Always-On and Lockdown for Android devices:**

1. From the Microsoft Intune Admin Center, navigate to **Devices > Android > Configuration**.
2. Create a new Policy and select the **Device restrictions** template.
3. For an open work profile, go to the **Configuration settings** page.
4. Expand the **Connectivity** section and configure the following settings:
  - Enable **Always-On VPN**
  - Set **VPN client** to **Custom**
  - In **Package ID**, enter `com.catonetworks.vpnclient`
  - Optional - Enable **Lockdown mode**
5. Click **Save**.

#### Additional Optional Values

You can also configure these optional values:

- `browser_package`: For selecting the default authentication browser
  - Note: The browser package name is different to the name of the app, for example use:
    - com.android.chrome for Chrome
    - com.microsoft.emmx for Edge
- `bypass_eula`: To control if the EULA is displayed.
  - Setting the value to True does not display the EULA to end users

## Enroll Android Devices into Intune

**To create the new enrollment profile and assign it to users or user groups:**

1. From the Microsoft Intune Admin Center, navigate to **Devices > Android > Enrollment**.
2. Under **Enrolment Profiles** and select **Corporate-owned, fully managed user devices**.
3. Create a new policy, enter a **Name**, **Token Type** (Corporate-owned, fully managed), and click **Next**.
4. Select **None** or the **Microsoft Entra group** for users to be enrolled. Click **Next** and **create**.
5. Open the new policy and select **Token**. The QR code can be shared with users for enrolment during device setup. Alternatively, the Zero-touch deployment method can be used.

![4-android.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36225235506717(1).png)
