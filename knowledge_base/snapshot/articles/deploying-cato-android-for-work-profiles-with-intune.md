---
title: "Deploying Cato Android for Work Profiles with Intune"
slug: "deploying-cato-android-for-work-profiles-with-intune"
updated: 2026-08-02T14:58:13Z
published: 2026-08-02T14:58:13Z
canonical: "knowledge.catonetworks.com/deploying-cato-android-for-work-profiles-with-intune"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploying Cato Android for Work Profiles with Intune

This article explains how to use Microsoft Intune to deploy the Cato Client for Android work profiles and route only work application traffic through the Cato Cloud.

## Overview

Cato lets you protect traffic for managed work applications on Android devices without routing traffic for the entire device through the tunnel. This is especially useful for organizations that permit BYOD, and they want to secure corporate apps and data while personal apps bypass the Cato tunnel.

Create an Android work profile with Microsoft Intune and enforce secure connectivity for apps included in that profile. Business apps such as corporate email, SaaS applications, and internal services send traffic through the Cato Cloud, while personal apps continue to use the device's regular network connection.

Microsoft Intune doesn't support native per-app traffic enforcement for custom providers on Android. Instead, this solution uses an Android work profile together with Always-On VPN and Lockdown mode.

To prevent users from bypassing this design through the personal profile, we recommend configuring access controls in your IdP or SaaS applications, so they only accept connections that originate from the Cato Cloud. This helps ensure that managed work apps remain accessible only when traffic is routed through Cato.

For more information, see [Deploying Cato Client with Android (Intune)](/v1/docs/deploy-the-cato-client-with-intune-android).

## Prerequisites

- Supported for Cato Client for Android v5.5 and higher
- Always-On VPN and Lockdown mode must be enabled for the work profile

### Use Case

ABC Company allows employees to use personal Android devices to access company resources such as Salesforce, Microsoft Teams, and internal web apps. However, the IT team wants to make sure that only enterprise traffic is routed through the Cato Cloud, while personal browsing and personal apps remain outside the tunnel.

To enforce this, the team deploys the Cato Client with an Android work profile using Microsoft Intune. They assign the relevant apps to the work profile and configure the profile to enforce Always-On VPN and Lockdown mode. As a result, work apps automatically send traffic through the Cato Cloud, while personal apps such as Instagram, WhatsApp, and personal browsing continue to use the device's direct network connection.

## How the Android Work Profile Solution Works

Microsoft Intune lets you isolate managed work apps inside an Android work profile and enforce secure connectivity for all apps in that profile. Enforce tunnel usage for all apps in the work profile with these Android restrictions:

- **Always-On VPN** starts the Cato Client automatically when the device boots. To establish connectivity automatically, you must also enable the Always-On policy in the Cato Management Application.
- **Lockdown mode** blocks all network traffic in the work profile unless it is routed through the tunnel.

These settings work together to enforce continuous connectivity for work-profile apps. Always-On VPN starts the Client automatically and helps prevent users from disconnecting it. Lockdown mode enforces fail-closed behavior, so work-profile traffic is blocked unless the Client is connected to the Cato Cloud.

For Android devices, enabling Always-On VPN alone doesn't block traffic for situations where the Client can't establish a tunnel to the Cato Cloud. Without Lockdown mode, traffic from work-profile apps can bypass the tunnel and access the network directly. Together, these restrictions ensure that all applications inside the work profile communicate only through the Cato Cloud.

### Expected Behavior

- The Android work profile determines which apps use the Cato tunnel.
- Apps in the work profile send traffic through the tunnel.
- Apps in the personal profile continue to use the device's regular network connection.
- Traffic enforcement is applied at the Android OS level for the work profile.
- Split Tunnel isn't supported in this deployment. If you use the Split Tunnel policy in the Cato Management Application to route traffic, that traffic is typically dropped by the Client.
- Lockdown mode enforces fail-closed behavior for the work profile, so the work profile app traffic is only allowed when it is routed through the Cato tunnel.
- Temporary bypass isn't supported because traffic outside the tunnel is blocked by Lockdown mode.

## Configuring Intune for Android Work Profile Traffic Routing

Intune uses these policy types for this deployment:

- An Android Enterprise device restrictions policy to enforce Always-On VPN and Lockdown mode for the work profile.
- A managed devices app configuration policy for the Cato Client to apply the required app settings for the deployment.

**To configure the Intune policy:**

1. In the Intune admin center, navigate to **Devices** and select **Android**.
2. Under **Configuration**, click **Create > New policy**.
3. Select **Android Enterprise** and **Templates**, then choose **Device restrictions**.
  - Select either **Fully managed** or **Personally owned work profile**, depending on the device type. ![1-createProfile.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36226754858653.png)
4. Enter a name for the policy.
5. Open the **Connectivity** section and configure the following settings:
  - Enable **Always-On VPN**.
  - Set **VPN client** to **Custom**.
  - Under **Package ID**, enter `com.catonetworks.vpnclient`.
  - Enable **Lockdown mode**.

![2-deviceRestrictions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36226770677789.png)
6. Assign the policy to the relevant Intune user or device groups.
7. Save the policy.
8. Configure the settings for the managed devices app configuration, navigate to **Apps > Manage apps > Android Configuration**.
9. Click **Create** and select **Managed devices**.
10. In the **Basics** page, configure these settings:
  - Name of the configuration.
  - **Platform** - Android Enterprise.
  - **Profile Type** - select the relevant profile for your deployment.
  - **Targeted app** - Cato Client. ![3-createApp.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36226754860957.png)
11. Click **OK** and then click **Next**.
12. In the **Settings** page, in the **Configuration settings format**, select **Use configuration designer**.
13. Click **Add**, and select the **Always-On VPN** and **Per-App VPN** keys.

![4-appSettings.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36226754861341.png)
14. Click **OK** and then set the **Configuration value** to **True** for each key. ![5-config.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36226754861597.png)
15. Click **Next** and assign the policy to the relevant Intune user or device groups.
16. Save the policy.

## Adding Apps to the Per-App VPN Profile

Traffic enforcement is applied at the Android work profile level. Any application installed in the work profile is automatically forced to send traffic through the Client.

You control which apps are included in the VPN by controlling which apps are assigned to the Android work profile in Intune.

**To add apps to the work profile:**

1. In the Intune admin center, go to **Apps**.
2. Select **Android** and choose the relevant app type, such as **Android Enterprise**.
3. Add or select the application you want to ensure is accessed via the VPN.
4. In the app assignment settings, assign the app to the same user or device groups that use the Android work profile.

## Known Limitations

- While in Office Mode, the Client doesn’t route traffic through the tunnel. So for deployments with Lockdown Mode enabled, when the Client is behind a site, it enters Office Mode and blocks all internet traffic.
  - Workaround - use the `per_app_vpn=true` flag to disable Office Mode, and keep all traffic in the site tunnel
