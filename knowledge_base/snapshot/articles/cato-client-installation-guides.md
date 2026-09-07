---
title: "Getting Started with the Windows Client"
slug: "getting-started-with-the-windows-client"
updated: 2026-09-01T11:01:31Z
published: 2026-09-01T11:01:31Z
canonical: "knowledge.catonetworks.com/getting-started-with-the-windows-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with the Windows Client

## Overview

The Cato Client is proprietary endpoint software that delivers secure access, advanced security enforcement, and monitoring capabilities. Downloading, installing, and connecting the Client is a simple process that enables you to quickly begin using its features and realizing value.

Depending on how your organization has configured the remote access policies and Client settings, the behavior and available features may vary. Some options described in this article might not apply to your specific installation.

**Note:** Before installing the Windows Client, review the Prerequisites (especially the minimum device operating system) listed in [Preparing to Install the Cato Client](/v1/docs/preparing-to-install-the-cato-client).

### Why Use the Cato Client?

The Client runs in the background on the device and contains a suite of features to secure your network and devices, and identify and support your users.

The capabilities of the Client can be grouped into six key capabilities:

1. Identification and Authentication
2. Device Posture
3. Secured Remote Access (requires a ZTNA license)
4. Secured Internet Access (requires a ZTNA license)
5. Digital Experience (requires a DEM license)
6. User Engagement

For more information, see [Understanding the Capabilities of the Cato Client](/v1/docs/understanding-the-capabilities-of-the-cato-client).

## How to Download, Install, and Connect with the Client

The Client may have been automatically installed on your device, which means you can use the instructions below to add a user and connect. If the Client was not installed, you can download and install it following the steps below:

### Downloading the Windows Client

**To download the Windows Client from the Cato website:**

1. From a browser, open the [Client download portal](https://clientdownload.catonetworks.com/) and select the **Windows** tab.
2. Click **Download**. The installation file is saved to your device.

### Installing the Windows Client

**To install the Windows Client on your device:**

1. Open the Windows Client installation file that you downloaded in the previous section and follow the steps in the installation wizard.
2. After you install the Client, open **Cato VPN Client** from the desktop.

![Client_Windows_Default.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30175666338333(1).png)

The Client can also be installed with the command line. For more information, see [Installing the Cato Client](/v1/docs/installing-the-cato-client).

### Adding a New User

You can add more than one user to the Client. To add a new user, on the **User** tab, click **Add User** and sign in with your email and password (and MFA) or SSO

### Signing into the Client

Once you have installed the Client, sign in to connect to the network. You can sign in with your email address and password (and MFA method) or with SSO.

#### Signing in with Email and Password (and MFA)

In the Client, click the **Connect** button and enter your email address. You will then be sent an email that explains how to create your password.

Once you have created your password, you can sign in to the Client and connect to the network.

**Note:** You may have received the email with an explanation of how to create your password before you click **Connect**.

#### Signing in with SSO

In the Client, click the **Connect** button and enter your email address. You can then choose to sign in with your SSO credentials.

### Connecting to your Network

Once the Client is installed and a user is added, you can connect to your network with the Client.

![Client_Windows_Default.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30175666338333(1).png)

**To connect to your network:**

1. Open the Client.
2. Click the connect button.

### Connecting to a Specific PoP

By default, the Client automatically connects to the optimal PoP based on geolocation and connectivity metrics. For more information on the Client connection process, see [Preparing to Install the Cato Client](/v1/docs/preparing-to-install-the-cato-client).

You can override this process by manually entering the IP address of a specific PoP you want the Client to connect to. To view the IP addresses of Cato's PoPs, see [Production PoP Guide](/v1/docs/production-pop-guide).

![Windows_manual2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30175679823389(1).png)

**To select the PoP the Client connects to:**

1. From the navigation menu in the Client, click **Users**.
2. Enter the IP address of the PoP you want the Client to connect to.

The Client connects to the manually selected PoP.

### Understanding Connectivity Statuses

You can view the Client connectivity status in the Client or using the Windows tray icon. The symbols for each connectivity status are:

| Symbol | Description |
| --- | --- |
| ![Connected.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33890798526365(1).png) | The Client is connected. |
| ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/warning.png) | The Client is connected but has a warning. |
| ![Error.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33890722363165(1).png) | The Client is connected but has an error. |
| ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/disconnected.png) | The Client is disconnected. |
| ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/disconnected_error.png) | The Client is disconnected due to an error. |
| ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/bypass.png) | The Client is bypassing the Cato Cloud. For more information, see [Protecting Users with Always-On Security](/v1/docs/protecting-users-with-always-on-security) |

## Understanding Authentication Errors

Based on the configuration of the [Client Connectivity policy](/v1/docs/what-is-the-client-connectivity-policy), the Client checks that your device has the required software or updates installed before it allows you to connect to the network. For example, the Client checks if you have up-to-date antivirus software installed. Only secure and compliant devices are allowed to connect. If the device doesn't comply with the Client Connectivity policy, the Client is blocked, and there is a notification with more details.

### How Do I Know if a Device Isn't Compliant?

If your device doesn’t meet the security policy, the Client doesn't connect and shows a message explaining the issue. Common reasons include:

- Out-of-date antivirus software version
- An unsupported operating system
- Need to update the Client to a newer version

Click **Details** in the message to see what failed.

![DevicePosture_ClientError.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30175688253213(1).png)
