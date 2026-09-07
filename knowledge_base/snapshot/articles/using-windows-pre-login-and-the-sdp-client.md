---
title: "Using Windows Pre Login and the Client"
slug: "using-windows-pre-login-and-the-sdp-client"
updated: 2026-07-26T14:10:54Z
published: 2026-07-26T14:10:54Z
canonical: "knowledge.catonetworks.com/using-windows-pre-login-and-the-sdp-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Windows Pre Login and the Client

This article explains how to configure the Pre Login settings to provide initial authentication to securely access networks and resources.

## Overview of Pre Login

Pre Login is an essential component of Zero Trust Network Architecture (ZTNA). It provides access to devices based on their Device Authentication and before the user is authenticated. The granular Pre Login policy defines a limited access policy of Allowed Destinations that are applied to trusted devices.

Cato's Pre Login feature addresses the problem of the initial authentication for a device, a common example is that a new device is sent to a new remote user. The device needs to connect to the company’s Active Directory (AD) to complete the user authentication. However, since this is a new device, there are no Windows users credentials on it, and unauthenticated users aren’t allowed to connect to the AD.

Cato’s solution is based on pre-deploying a trusted certificate and the Cato Client on the device. This establishes enough trust to let the device connect to the Pre Login resources that you configure. Then the user can securely authenticate to the device.

### Cato's Pre Login Solution

As soon as the device can connect to the public Internet (such as, WiFi in the user’s house), or if a Windows users signs out, the Cato Pre Login feature lets the device connect to the Pre Login resources.

During this Pre Login stage, the device pulls its IP address from the default range of IP addresses. You should ensure that your system is configured to work with the default range.

The Windows device is pre-configured with the Cato Client, a trusted certificate, and the Windows registry is configured with the account name. The Client then connects to the relevant resources, for example, connect to the AD and the user then authenticates the device. Once the Windows device successfully authenticates to the Cato Cloud, Windows user credentials are saved to the device, and in the future it can authenticate and connect to the AD as required.

Once the user is authenticated, if they match a rule for a static or dynamic IP address, they will draw their address from that range.

### Windows Device Prerequisites

Windows devices that meet all of these prerequisites can use Cato's Pre Login feature.

- Cato SDP Client requirements:
  - Supported from Window Client v5.4 and higher
  - Client is installed on the device
- Certificate requirements:
  - Upload a private signing certificate (not the Cato certificate) to the Cato Management Application (**Access > Client Access > Signing certificates**)

For more information about uploading certificates, see [this article](/v1/docs/managing-signing-certificates-for-remote-access).
  - Install a signed device certificate on the Windows device
- Configure the Windows registry for the Client on the device **Computer\HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN**:
  - Enable Pre Login for this device

**PreLogin (DWORD)**, value data **1**
  - Configure the account name as it appears in the Cato Management Application

**Subdomain (String)**, value data <account subdomain>

For example, the account name **SampleCo** has the full domain: **sampleco.via.catonetworks.com** where sampleco is the <account subdomain>

You can show the [subdomain for your account](/v1/docs/configuring-sso-and-the-subdomain-for-the-account) in Access > Single Sign-On
  - After the Client successfully performs the initial authentication to the Cato Cloud, the registry is automatically updated
  - (Optional) If you are configuring Always-On out-of-the-box, define the following key:

**InitialAlwaysOn (DWORD)**, value data **1**
  - This can also be configured using installation parameters, for more information, see [Deploy Cato Client with Intune (Windows)](/v1/docs/deploy-cato-client-with-intune-windows)

### Requirements for Allowed Destinations

- For accounts that use a private DNS server (including internal AD servers), configure these settings:
  - The private DNS server is defined as an **Allowed Destination**

DNS servers defined for the account are automatically included as an **Allowed Destination**
  - [DNS Forwarding](/v1/docs/defining-dns-forwarding-rules) is enabled, and configured for the private DNS server
  - By default, the Cato Client sets the DNS server as 10.254.254.1

If your account uses a custom service range, the IP address for DNS is x.y.z.3
- SDP Clients that are configured with Always-On, are only allowed to connect to:
  - WAN - Resources defined in Allowed Destinations
  - Internet - Authenticate the user with the IdP
- SDP Clients without the Always-On settings (including new devices), are allowed to connect to:
  - WAN - Resources defined in Allowed Destinations
  - Internet - Windows device can connect to any resource in the Internet
- For security reasons, we recommend that you define the smallest IP range for an **Allowed Destination**

### Pre Login with Connect on Boot

If Pre Login and [Connect on Boot](/v1/docs/protecting-users-with-always-on-security) are both enabled, after the device boots the Client enters Pre Login state. Once a user signs into the device the Client attempts to authenticate the user. For more information, see [Understanding the Cato Client Connection Flow](/v1/docs/understanding-the-cato-client-connection-flow).

## Sample Pre Login Use-cases

- Challenge - A brand new Windows device is sent to an employee at their house. The corporate AD is behind a Cato site, so the new user can't connect to it.
  - Solution - The device meets the Pre login prerequisites above. The user turns on the computer, it is allowed to connect to the AD, and the user authenticates to the AD and is allowed to connect to the network.

## Configuring Pre Login Settings in the Cato Management Application

Use the Pre login screen to define the resources in the **Allowed Destinations** that the pre-configured Windows devices can connect to. When the Client on the device attempts to connect to the Cato Cloud, the device is recognized as a Pre login device.

The Cato Cloud allows the device to connect to the resources that are configured as an **Allowed Destination**, and the WAN and Internal firewall rules are not applied to this connection. In addition, the Device Posture requirements are not applied to the Pre Login traffic. The Cato Cloud only allows traffic that is related to the Pre Login process.

An **Allowed Destination** can be a IP address, IP range, or a host (which is defined for a specific site). Pre Login supports up to 48 Allowed Destinations.

![Prelogin.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25210430131357.png)

**To configure your account to support Pre Login:**

1. From the navigation menu, click **Access > Client Access**.
2. Expand the **Pre Login** section.
3. Select **Enable Pre Login**.
4. From the drop down menu, select the Host, IP address, or IP range for each **Allowed Destination**.

**Note:** For security reasons, do not use the IP range 0.0.0.0 - 255.255.255.255 as an **Allowed Destination**.
5. Click **Save**.
