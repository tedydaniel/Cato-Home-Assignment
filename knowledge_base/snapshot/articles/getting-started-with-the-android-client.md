---
title: "Getting Started with the Android Client"
slug: "getting-started-with-the-android-client"
updated: 2026-06-21T10:52:52Z
published: 2026-06-21T10:52:52Z
canonical: "knowledge.catonetworks.com/getting-started-with-the-android-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with the Android Client

This article explains how to install the Android Client on your device and connect to the Cato Cloud.

## Overview

The Cato Client is proprietary endpoint software that delivers secure access, advanced security enforcement, and monitoring capabilities. Downloading, installing, and connecting the Client is a simple process that enables you to quickly begin using its features and realizing value.

To connect to your network using the Android Client, you need to:

- Step 1: Install the Android Client from the Google Play Store.
- Step 2: Open the Client and sign in to connect to the network.

**Note:** Before installing the Android Client, review the Prerequisites (especially the minimum device operating system) listed in [Preparing to Install the Cato Client](/v1/docs/preparing-to-install-the-cato-client).

## Step 1: Installing the Android Client

**To install the Android Client on your device:**

1. Install the Cato Client app from the Google Play Store.
2. After you install the Client, click **Open**.
3. The Client requests your permission to add a new VPN configuration, click **OK**.

The Client is installed on your device.

![Client_Android_Default.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218263540765.jpg)

## Step 2: Signing into the Client

Once you have installed the Client, sign in to connect to the network. You can sign in with your email address and password (and MFA method) or with SSO.

### Approving the End User License Agreement (EULA)

The first time you open the Client, the EULA is displayed. You need to review and approve the EULA before you can sign into the Client.

### Signing in with Email and Password (and MFA)

In the Client, click the **Connect** button and enter your email address. You will then be sent an email that explains how to create your password.

Once you have created your password you can sign into the Client and connect to the network.

> [!NOTE]
> Note:
> 
> You may have received the email the with an explanation on how to create your password before you click **Connect**.

### Signing in with SSO

In the Client, click the **Connect** button and enter your email address. You can then choose to sign in with your SSO credentials.

Disabling Battery Optimization

Your devices battery optimization functionality can impact the stability of the connectivity of the Client especially with Always-On. When prompted, it is best practice to disable battery optimization for the Client.

### 

## Connecting to a Specific PoP

By default, the Client automatically connects to the optimal PoP based on geolocation and connectivity metrics. For more information on the Client connection process, see [Installing the Cato Client](/v1/docs/preparing-to-install-the-cato-client).

You can override this process by manually entering the IP address of a specific PoP you want the Client to connect to. To view the IP addresses of Cato's PoPs, see [Production PoP Guide](/v1/docs/production-pop-guide).

![Android_PoP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218323073949(1).png)

**To select the PoP the Client connects to:**

1. From the navigation menu in the Client, select **Settings**.
2. Select **Manual PoP**.
3. Enter the IP address of the PoP you want the Client to connect to.
4. Select **OK**.

The Client connects to the manually selected PoP.
