---
title: "Preparing to Install the Cato Client"
slug: "preparing-to-install-the-cato-client"
tags: ["Access", "Best Practices", "Clients"]
status: "update"
updated: 2026-09-06T10:26:05Z
published: 2026-09-06T10:26:05Z
canonical: "knowledge.catonetworks.com/preparing-to-install-the-cato-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Preparing to Install the Cato Client

The Cato Client is proprietary software that extends Cato's network and security capabilities to remote users in any location. This article lists the prerequisites and explains how to install the Client.

## Overview

The Cato Client can identify and authenticate users, enforce your network rules, and inspect remote traffic based on security policies. To ensure your users benefit from these features, the Cato Client must be installed on their device. Before you install the Client on any device, ensure that the prerequisites are met and the required processes and URLs are added to the allowlists of your security software. You can then download the Client and install it on an individual device or distribute it with an MDM.

After you install the Client on a device, you can configure features and policies to meet your requirements. Users can authenticate and securely connect to your network. For more information on the Client Connection process, see [Understanding the Cato Client Connection Flow](/v1/docs/understanding-the-cato-client-connection-flow).

## Prerequisites for Installing the Cato Client

Before the Client is installed on a device, ensure the following prerequisites are met:

- Install the Client on a device running a [supported operating system](/v1/docs/preparing-to-install-the-cato-client#h_01KE98NZQF4MVB80AZTEDBMY7D).
- IP routing should be disabled before installing the Cato Client and enabled after the installation completes.
- The Cato CA certificate is installed on the device or computer
  - For Windows Clients, the Cato certificate is automatically added to the Windows certificate store and supports the Chrome and Edge browsers

You can manually install the Cato certificate for other browsers (such as Firefox), or use an MDM to install it with the browser, see [Installing the Cato Certificate on Windows Devices](/v1/docs/installing-the-cato-certificate-on-windows-devices)
  - For macOS Clients, for organizations that use an MDM, the Cato certificate is automatically installed as part of the CA keychain

Otherwise, the SDP user manually installs the Cato certificate. For more information, see [Installing the Cato Certificate on macOS Devices](/v1/docs/installing-the-cato-certificate-on-macos-devices).
  - For iOS and Android Clients, the SDP user manually installs the Client or use an MDM to install the certificate with the Client. For more information, see [Installing the Cato Certificate on iOS Devices](/v1/docs/installing-the-cato-certificate-on-ios-devices) or [Installing the Cato Certificate on Android Devices](/v1/docs/installing-the-cato-certificate-on-android-devices).
  - The Cato certificate and Client installation files can be downloaded from:
    - The [Client download portal](https://clientdownload.catonetworks.com/) in CER format
    - The **Security > Certificate Management** page in PEM and DER format
- Internet browser requirements:
  - Use an Internet browser that supports SSL (such as Chrome or Edge)
  - For external authentication, make sure that a default browser is configured in the device OS settings
- A PPPoE connection is not used. PPPoE is not supported
- For iOS, Android, and Linux Clients, we recommend that you disable IPv6 on all physical adapters
  - IPv6 is supported for [Last Mile Connections](/v1/docs/cato-client-last-mile-support-for-ipv6) on Windows Client v5.11 and higher and macOS Client v5.7 and higher
- Make sure that the IP addresses for PoPs in the Cato Cloud are allowlisted on any firewalls or similar devices

For a list of the PoP IP ranges, see: [Production PoP Guide](/v1/docs/production-pop-guide)
- The Client uses cipher suites to establish a DTLS handshake with the Cato Cloud. Ensure the device uses one of the [cipher suites that Cato supports](%%LINK:115005910469%%).
- On Windows devices, IP forwarding is disabled. For more information, see [IP Routing Prevents Windows Client Authentication](/v1/docs/ip-routing-prevents-windows-client-authentication)
- On macOS devices:
  - Full Disk Access permission
  - No other enterprise VPN is running on the device
- If Bandwidth Management is used in your account, we recommend that you give the IP address 10.254.254.1 at least the same priority as any other address you have added
- To receive user notifications, notifications must be enabled on the device. For more information, see [Creating the Data Control Policy](/v1/docs/creating-the-data-control-policy) and [Managing the Application Control Policy](/v1/docs/managing-the-application-control-policy)
- Review the Known Limitations of the Client version. For more information, see [Summary of Cato Client Releases](/v1/docs/summary-of-cato-client-releases)

### Allowlisting Processes and URLs for the Cato Client

For more information about processes and URLs to allowlist for all security endpoint software and solutions, see [Allowlisting Processes and URLs for the Cato Client](/v1/docs/allowlisting-processes-and-urls-for-the-cato-client).

## Minimum Supported Device Operating Systems

The following sections show the operating systems on which you install the Cato Client.

**Notes:**

- Any Client version that is not listed as supported is considered [End of Support](/v1/docs/end-of-support-eos-policy-for-cato-clients)
- The Client does not support operating systems that vendors have declared EoL (End of Life)
- Android EoL is based on the date from which Google no longer provides security updates or patches for a version
- New device OS versions are not supported automatically for all Cato Client versions. Official support begins only after Cato announces which Client versions have been validated and are supported on the new OS version

### Microsoft Windows

The following table shows which Microsoft Windows versions support which versions of the Cato Client. For instructions on installing the Cato Client for Windows, see [Installing the Windows Client](/v1/docs/installing-the-cato-client).

From October 1, 2026, Windows Clients v5.17 and lower will be End of Support. We recommend that you update devices to the newest Client version to ensure continued support and security protections.

| **Operating System** | **Minimum Supported Client Version** |
| --- | --- |
| Windows 11 | v5.11 and higher |
| Windows 10 32-bit Windows 10 64-bit | v5.11 and higher |
| Windows 8.1 32-bit Windows 8.1 64-bit | v5.11 and higher |
| Windows Server 2016 Windows Server 2019 Windows Server 2022 Windows Server 2025 | v5.10 and higher |

### macOS

The following table shows which macOS versions support which versions of the Cato Client. For instructions on installing the Cato Client for macOS, see [Installing the macOS Client](/v1/docs/installing-the-cato-client).

**Notes:**

- From November 7, 2026, the Cato macOS Client will not be supported on devices running macOS v13.3 (Ventura) and lower. To ensure continued support for the Cato Client, upgrade devices running these macOS versions before November 7, 2026.
- From October 1, 2026, macOS Clients v5.10.0 and lower will be End of Support. We recommend that you update devices to the newest Client version to ensure continued support and security protections.

| **Operating System** | **Cato Client Version** |
| --- | --- |
| macOS Tahoe (version 26) | v5.10.4 and higher |
| macOS Sequoia (version 15) | v5.8 and higher |
| macOS Sonoma (version 14) | v5.8 - v6.0.1 |
| macOS (Ventura) software version 13.3 | v5.7 - v5.10.4 |
| macOS (Monterey) software version 12 | 5.7 - v5.8 |
| macOS (Big Sur) software version 11 | v5.6 |

### iOS and iPadOS

The following table shows which iOS versions support which versions of the Cato Client. For instructions on installing the Cato Client for iOS, see [Installing the iOS and Android Clients](/v1/docs/installing-the-cato-client).

**Note:** From October 1, 2026, iOS and iPad OS Clients v5.6.0 and lower will be End of Support. We recommend that you update devices to the newest Client version to ensure continued support and security protections.

| **Operating System** | **Cato Client Version** |
| --- | --- |
| iOS 17.0 and higher | v5.9 and higher |
| iOS 16.0 and higher | v5.2 - v5.8.2 |
| iPadOS 15.0 and higher | v5.2 and higher |

### Android and Chromebook

The following table shows which Android and Chromebook versions support which versions of the Cato Client. For instructions on installing the Cato Client for iOS, see [Installing the iOS and Android Clients](/v1/docs/installing-the-cato-client).

**Note:** From October 1, 2026, Android and Chromebook Clients v5.2.1 and lower will be End of Support. We recommend that you update devices to the newest Client version to ensure continued support and security protections.

| **Operating System** | **Cato Client Version** |
| --- | --- |
| Android version 8.1 and higher | v5.2 and higher |
| Chromebook (all versions) | v5.2 and higher |

### Linux

The following table shows which Linux flavors and versions support which versions of the Cato Client. For instructions on installing the Cato Client for Linux, see [Installing the Linux Client](/v1/docs/installing-the-cato-client).

Linux Clients are supported for 64-bit OS (X86_64 and ARM64)

**Note:** From October 1, 2026, Linux Clients v5.5 and lower will be End of Support. We recommend that you update devices to the newest Client version to ensure continued support and security protections.

| **Operating System** | **Cato Client Version** |
| --- | --- |
| Ubuntu v18 and higher (There is a different Client for each Ubuntu OS version) | v5.2 and higher |
| CentOS v9 and higher | v5.2 and higher |
| Fedora v36 and higher | v5.2 and higher |
| Debian v11 and higher | v5.2 and higher |
| Mint v20.3 and higher | v5.2 and higher |
| RHEL v8.0 and higher | v5.2 and higher |
| Any systems running glibc 2.31 and higher | v5.2 and higher |

## Understanding the Next Steps After Installing the Client

Once the Client is installed on a device, you can configure features and policies to meet your secure remote access requirements. The Client enforces the features configured in the Cato Management Application. This lets you simply manage and enforce your requirements and ensure the protection of your network.

### Understanding Key Client Features and Policies

Here are some key features we recommend you enable. For more information about all the Client features, see the [Access documentation](/v1/docs/access).

- **User Awareness:** [Identify](/v1/docs/using-cato-identity-agents-for-user-awareness) the user signed into the device at any point in time to control user access, and monitor user activity
- **Client Connectivity Policy:** To check the [posture](/v1/docs/configuring-the-client-connectivity-policy) of devices before they connect to the network
- **Always-On Policy:** To ensure all traffic [always](/v1/docs/protecting-users-with-always-on-security) goes through the Cato Cloud and Cato security engines inspect the traffic to ensure it complies with your security policies

#### Analyzing Client Events

You view and analyze data from users connecting with the Client from the [Remote User Dashboard](/v1/docs/using-the-access-overview-page).
