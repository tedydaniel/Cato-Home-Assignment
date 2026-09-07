---
title: "Deploying and Upgrading macOS Clients with an MDM"
slug: "deploying-and-upgrading-macos-clients-with-an-mdm"
updated: 2026-08-17T05:22:34Z
published: 2026-08-17T05:22:34Z
canonical: "knowledge.catonetworks.com/deploying-and-upgrading-macos-clients-with-an-mdm"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploying and Upgrading macOS Clients with an MDM

This article discusses how to configure a Mobile Device Management (MDM) to deploy and update macOS Clients for SDP users in your account.

This feature is supported for macOS Client v5.0 and higher.

## Overview

Starting with macOS Client v5.0, you can configure the Cato Management Application to use an MDM to manage the deployment and updates for macOS Clients in your organization. All Client updates are controlled using the MDM and end users don't receive notifications of new Client versions.

### High-Level Workflow of Managed Deployments and Upgrades for macOS Clients

This is an overview of the workflow to implement an MDM solution for macOS Clients in your account.

1. From the navigation menu, click **Access > Client Rollout**.
2. Click the **Upgrade Policy** tab.
3. For the macOS Client, choose **Managed by Admin**.
4. Import the macOS package.
5. Configure the MDM to create a policy that allows the DMG extension and VPN profiles for end users.

Otherwise, end users need to manually approve and allow the above items in macOS.
6. In the MDM, distribute the new macOS Client version to the end users in your account.

## Importing the macOS Package

To use the Managed Upgrade for the macOS Client in your account, first you need to import the package to the MDM.

### Sample JAMF Procedure to Import the macOS Package

1. From the navigation menu, select **Settings > Computer Management**.
2. Select **Packages** and click **New**.
3. Enter the **Display Name**.
4. Click **Choose File** and select the macOS Client package.
5. Click **Save**.

The macOS Client package is imported to JAMF.

## Automatically Allowing macOS Permissions for the Client with the MDM

Starting with the macOS Client v5.0, the following permissions are required to install the Client on a macOS host:

- Allow the Cato Client to create a VPN profile
- Allow system extensions for the Cato Client

You can configure the MDM to automatically allow these permissions for end user as part of the installation process for the new Client version. Otherwise, the end user must manually configure the macOS settings as part of the installation process.

### Allowing Permissions for the VPN Profile

In the MDM, create a VPN Payload that contains the settings to automatically set macOS to allow permissions for the Cato Client VPN profile. When the Client is installed, the VPN Profile permissions are set correctly, and macOS doesn't request that the end user manually configure them.

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

#### Sample JAMF Procedure to Set Permissions for the VPN Settings

Create the new profile and then configure the VPN settings for that profile.

1. Create the profile for the macOS Client:
  1. From the navigation pane, select **Computers > Configuration Profiles**.
  2. Click **New** and create a new profile for the Cato Client.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/general(1).png)
2. Edit the **VPN** settings to allow the VPN permissions for the profile (based on the data in the table above):
  1. In **Configuration Profiles**, edit the profile you created in the previous step and select **VPN**.
  2. Enter the settings for the **VPN Type**, **Connection Type**, **Identifier, Server**, **Account**, and **Provider Bundle Identifier**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/01_vpn.png)
  3. Configure the settings for the **User Authentication**, **Provider Type**, and **Provider Designated Requirement**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/02_vpn.png)

### Allowing System Extensions

In the MDM, configure the policy to allow the system extensions that are used by the macOS Client. When the Client is installed, the system extension permissions are set correctly, and macOS doesn't request the end user to manually configure them.

| Setting | Value |
| --- | --- |
| Display Name | CatoClient System Extension |
| System Extension Types | Allowed System Extensions |
| Team Identifier | CKGSB8CH43 |
| Allowed System Extensions | - com.catonetworks.mac.CatoClient - com.catonetworks.mac.CatoClient.CatoClientSysExtension |

#### Sample JAMF Procedure to Set Permissions for the System Extensions

Edit the **System Extensions** settings to allow the system permissions for the profile (based on the data in the table above).

1. Select **Allow users to approve system extensions**.
2. Enter the **Display Name**.
3. Select the **System Extension Types**.
4. Enter the **Team Identifier**.
5. Make sure that the values for the **Approved System Extensions** are correct.
6. Save the changes to the macOS Client profile.

## Distributing the macOS Client

In the MDM, select the users and groups that are receiving the Cato VPN profile. Then create a new policy with the macOS package and push the policy to the users.

### Suppressing the EULA Screen during Deployment

Starting with macOS v5.10.6, you can deploy a silent installation that suppresses the EULA screen.

**To suppress the EULA screen during deployment:**

1. Open the profile file in a text editor.
2. In the PayloadContent section of the file, under mcx_preference_settings, include the following:

```plaintext
<dict>
      <key>suppressEULAScreen</key>
      <integer>1</integer>
</dict>
```
3. Save the file.

A sample profile for JAMF is attached to this page.

### Sample JAMF Procedure to Distribute the macOS Client

1. In **Computers > Configuration Profiles**, select the group or specific users that are receiving the Cato VPN profile.
2. Create a new policy and add the macOS package to it.
  1. In **Computers > Policy**, create a new policy.
  2. From the **General** section, configure these settings:
    1. Enter the **Display Name.**
    2. Configure the other policy settings based on the requirements for your organization.
  3. In the **Packages** section, add the macOS Client package.
3. Click **Save**. The profile is ready to distribute the Client to the macOS devices.

## Known Limitations

- If you upgrade the Client with an MDM, pop-ups are sometimes displayed requesting permission to allow the installation of system extensions and the VPN configuration.

To prevent this issue, you can first distribute the permissions for the DMG extension and the VPN payload, then distribute the Clients to the macOS hosts.

## Attachments

- [EULASuppress.mobileconfig](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/EULASuppress.mobileconfig)
- [sample_profile.mobileconfig](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/sample_profile.mobileconfig)
