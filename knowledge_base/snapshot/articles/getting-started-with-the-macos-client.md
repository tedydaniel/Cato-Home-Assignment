---
title: "Getting Started with the macOS Client"
slug: "getting-started-with-the-macos-client"
updated: 2026-09-07T14:04:25Z
published: 2026-09-07T14:04:25Z
canonical: "knowledge.catonetworks.com/getting-started-with-the-macos-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with the macOS Client

## Overview

The Cato Client is proprietary endpoint software that delivers secure access, advanced security enforcement, and monitoring capabilities. Downloading, installing, and connecting the Client is a simple process that enables you to quickly begin using its features and realizing value.

Depending on how your organization has configured the remote access policies and Client settings, the behavior and available features may vary. Some options described in this article might not apply to your specific installation.

### Why Use the Cato Client?

The Client runs in the background on the device and contains a suite of features to secure your network, devices and identify and support your users.

The capabilities of the Client can be grouped into six key capabilities:

1. Identification and Authentication
2. Device Posture
3. Secured Remote Access (requires a ZTNA license)
4. Secured Internet Access (requires a ZTNA license)
5. Digital Experience (requires a DEM license)
6. User Engagement

For more information, see [Understanding the Capabilities of the Cato Client](/v1/docs/understanding-the-capabilities-of-the-cato-client).

### Prerequisites

- System level notifications must be enabled on the device to authenticate using the browser within the Client ([Embedded browser)](/v1/docs/configuring-the-authentication-policy-for-cato-clients).
- The Client is Allowed in the background (This is enabled in **Settings > General > Login Items**)
- The Client requires Full Disk Access permissions for Device Posture checks and collecting logs.
- Review the Prerequisites (especially the minimum device operating system) listed in [Preparing to Install the Cato Client](/v1/docs/preparing-to-install-the-cato-client).

## How to Download, Install, and Connect with the Client

The Client may have been automatically installed on your device which means you can use the instructions below to add a user and connect. If the Client was not installed, you can download and install it following the steps below:

## Downloading the macOS Client

You can download the macOS Client onto your device from the Client Portal.

**To download the macOS Client from the Cato website:**

1. From a browser, open the [Client download portal](https://clientdownload.catonetworks.com/), and select the **macOS** tab.
2. Click **Download**. The installation file is saved to your device.

## Installing the macOS Client

Once you download the Client, you can install it on your macOS device.

**To install the macOS Client on your device:**

1. Open the macOS Client installation file.
2. Follow the steps in the installation wizard.
3. When the **Installer** pop up is displayed, enter the device password.

![Installer.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33890811301149(1).png)
4. In the **System Extension Blocked** pop up, click **Open System Setting**.

![System_Extension_Blocked.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33890811375645(1).png)
  1. **For macOS versions Sequoia (15.0) and above:**

> [!NOTE]
> ​​Note​​:
> 
> You may be asked to allow the Client to find devices on local networks. This is not required for normal operation of the Client.
    1. In the **General** section, navigate to **Login Items & Extension**.
    2. Under the **Extensions** section, click **Network Extensions** i symbol.

![Login_Items_and_Extenstions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33890799072797(1).png)
    3. In the **Network Extensions** pop up, turn the Cato Client toggle on.

![PoP_up.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33890722805533(1).png)
    4. Click **Done**.
  2. **For macOS versions Ventura (13.0) and above:**
    1. In the **Privacy & Security** section, click **Allow**.

![Privacy___Security1__1_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33890773266717(1).png)
    2. Enter the device **Username** and **Password** and click **Unlock**.

![Privacy___Security.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33890799248925(1).png)
    3. Close the **Privacy & Security** window.
5. The Client requests your permission to add a new VPN configuration, click **Allow**.

![Allow_VPN.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33890811711901(1).png)

The Client is installed on your device.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/macOS_AddUser.png)

## Adding a New User

You can add more than one user to the Client. To add a new user, on the **User** tab, click **Add User** and sign in with your email and password (and MFA) or SSO

## Signing into the Client

Once you have installed the Client, sign in to connect to the network. You can sign in with your email address and password (and MFA method) or with SSO.

### Signing in with Email and Password (and MFA)

In the Client, click the **Connect** button and enter your email address. You will then be sent an email that explains how to create your password.

Once you have created your password you can sign into the Client and connect to the network.

> [!NOTE]
> Note:
> 
> You may have received the email the with an explanation on how to create your password before you click **Connect**.

### Signing in with SSO

In the Client, click the **Connect** button and enter your email address. You can then choose to sign in with your SSO credentials.

## Connecting to the Network

After you have added a User to the Client, you can connect to the network.

**To connect to the network:**

- From the **Home** page of the Client, click the **Connect** button in the middle of the shield.

The Client connects to the network.

> [!NOTE]
> Note:
> 
> This is the only supported method of connecting to the network. Connecting from **System Preferences > Network** on the device is not supported.

## Connecting to a Specific PoP

By default, the Client automatically connects to the optimal PoP based on geolocation and connectivity metrics. For more information on the Client connection process, see [Preparing to Install the Cato Client](/v1/docs/preparing-to-install-the-cato-client).

You can override this process by manually entering the IP address of a specific PoP you want the Client to connect to. To view the IP addresses of Cato's PoPs, see [Production PoP Guide](/v1/docs/production-pop-guide).

![Manual_macOS.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33890766532253(1).png)

**To select the PoP the Client connects to:**

1. From the navigation menu in the Client, click **Users**.
2. Enable **PoP Server IP**.
3. Enter the IP address of the PoP you want the Client to connect to.

The Client connects to the manually selected PoP.

## Understanding Connectivity Statuses

You can view the Client connectivity status in the Client or using the tray icon. The symbols for each connectivity status are:

| Symbol | Description |
| --- | --- |
| ![Connected_macos.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33890756689181(1).png) | The Client is connected. |
| ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Warningmacos1.png) | The Client is connected but has a warning. |
| ![errormacos.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33890755642013(1).png) | The Client is connected but has an error. |
| ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Disconnected.png) | The Client is disconnected. |
| ![Disconnected_error.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33890755735709(1).png) | The Client is disconnected due to an error. |
| ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Bypass4.png) | The Client is bypassing the Cato Cloud. For more information, see [Protecting Users with Always-On Security](/v1/docs/protecting-users-with-always-on-security) |

## Understanding Authentication Errors

Based on the configuration of the [Client Connectivity policy](/v1/docs/what-is-the-client-connectivity-policy) the Client checks your device has the required software or updates installed before it allows you to connect to the network. For example, the Client checks if you have an up-to-date antivirus software installed. Only secure and compliant devices are allowed to connect. If the device doesn't comply with the Client Connectivity policy, the Client is blocked, and there is a notification with more details.

### How Do I Know if a Device Isn't Compliant?

If your device doesn’t meet the security policy, the Client doesn't connect and shows a message explaining the issue. Common reasons include:

- Out-of-date antivirus software version
- An unsupported operating system
- Need to update the Client to a newer version

Click **Details** in the message to see what failed.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Client_imag.png)
