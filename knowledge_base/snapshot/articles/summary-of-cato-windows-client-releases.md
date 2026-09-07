---
title: "Summary of Cato Windows Client Releases"
slug: "summary-of-cato-windows-client-releases"
status: "update"
updated: 2026-09-03T10:57:44Z
published: 2026-09-03T10:57:44Z
canonical: "knowledge.catonetworks.com/summary-of-cato-windows-client-releases"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Summary of Cato Windows Client Releases

This article summarizes the features and enhancements of the Windows Client.

In addition, it also lists the known limitations.

Admins and users can easily download the Client from the [Client download portal](https://clientdownload.catonetworks.com/) without requiring authentication.

For more information about the requirements to implement Cato's remote access in your organization, see [Preparing to Install the Cato Client](/v1/docs/preparing-to-install-the-cato-client).

## Windows Client v6.12.6

During the week of Aug. 16, 2026, we will begin rolling out the Windows Client version 6.12.6. This version contains:

- Improved certificate validation process for DTLS tunnel connections

### Resolved Issues

| ID | Description | Severity |
| --- | --- | --- |
| 202424 | Fixed an issue where the Windows VPN service could crash during shutdown | High |
| 200699 | We fixed an issue that caused all internet access to be blocked after manually disconnecting the Windows Client when both Always-On and Trusted/Managed Network were configured. | Medium |

## Windows Client v6.12

During the week of July 26, 2026, we will begin rolling out the Windows Client version 6.12. This version includes:

- **Additional Installation Parameters**: The Windows MSI supports [installation parameters](/v1/docs/deploy-cato-client-with-intune-windows) that previously required setting registry keys, simplifying automated deployments.
- **Updated OPSWAT OESIS Framework**: We updated the [OPSWAT OESIS framework](https://www.opswat.com/products/endpoint-security-sdk/device-compliance) used by the Client to version 4.3.6344

### Resolved Issues v6.12

| ID | Description | Severity |
| --- | --- | --- |
| 194104 | Fixed an issue that could cause the Client to become stuck during automatic upgrade | Medium |
| 195747 | Fixed an issue with Always-On reconnection after a bypass expired | Medium |
| 184142 | Fixed an issue where Digital Experience Monitoring (DEM) displayed incorrect Sent and Received packet counts for MTR probes | Medium |

## Windows Client v6.8.3

During the week of June 14, 2026, we will begin rolling out the Windows Client version 6.8.3. This version includes:

- Client Management now runs on a separate service to better support resiliency
  - To ensure this service runs correctly, add **coresvc.exe** to your [security allowlist](/v1/docs/allowlisting-processes-and-urls-for-the-cato-client)
- Improved the process for how the Client identifies the optimal PoP to connect to
- Support multiple NICs when using Intune MDM compliance checks for device posture

### Resolved Issues v6.8.3

| ID | Description | Severity |
| --- | --- | --- |
| 181368 | Fixed an issue that caused the Experience Monitoring service to crash. | Critical |
| 179748 | Fixed an issue that caused devices with an EPP installed to fail an Anti-Malware device posture check | Critical |
| 167866 | Fixed an issue that prevented DNS resolution behind IPv6 networks | High |
| 176352 | Fixed an issue where DNS relay was not updated when a 3rd party VPN (for example, Global Protect) connects | High |
| 175865 | Fixed an issue that prevented end users from disabling Office Mode | Medium |

## Windows Client v6.4

During the week of May 3, 2026, we will begin rolling out the Windows Client version 6.4. This version includes:

### Resolved Issues v6.4

| ID | Description | Severity |
| --- | --- | --- |
| 173364 | Fixed an issue where the Client did not reconnect after a disconnection when Always-On is enabled. | High |
| 142788 | Fixed an issue that caused the Client to disconnect after switching networks on devices running Windows 11. | High |
| 169470 | Fixed an issue where users were prompted to reauthenticate after their session expired, even if Private Access was disabled. | Medium |
| 174502 | Fixed an issue where Device Posture updates were delayed and did not match the correct rules. | Medium |
| 174234 | Fixed an issue that prevented Experience Monitoring data being collected if the Client disconnected. | Medium |

## Windows Client v6.2

During the week of March 22, 2026, we will begin rolling out the Windows Client version 6.2. This version includes:

- Improved co-existence with 3rd party products

### Resolved Issues v6.2

| ID | Description | Severity |
| --- | --- | --- |
| 168485 | Fixed an issue where, after an upgrade, the connection duration could be reported inaccurately with an inflated value. | Critical |
| 167355 | Improved reliability of User Awareness for users connected in Office Mode. | Critical |
| 167095 | Fixed an issue where, after successful authentication, the client could incorrectly return to the login screen. | Critical |
| 164574 | Fixed an issue where connectivity could be disrupted when transitioning from Wi-Fi to a wired network. | Critical |
| 163611 | Fixed an issue where Device Check validation did not correctly handle processes with multiple signature thumbprints. | Critical |
| 148414 | Fixed an issue where Always-On reconnection could fail after switching Windows session users. | High |
| 162709 | Fixed an issue where users were incorrectly prompted to authenticate with a Microsoft account as the first authentication step. | High |

## Windows Client v6.0

During the week of February 22, 2026, we will begin rolling out the Windows Client version 6.0. This version includes:

- Monitoring [WiFi signal strength](/v1/docs/experience-monitoring-in-the-cato-client) locally can indicate if a poor connection is identified (no license required)
- Support for ARM architecture
- Optimized the Cato Client for improved throughput
- Resolved CVE-2025-15040 (vulnerability in the embedded Chromium browser)
- **Note:** Automatic upgrade isn't available for some unsupported legacy Client versions. You need to uninstall the old version and then install the new one

### Resolved Issues v6.0

| ID | Description | Severity |
| --- | --- | --- |
| 160357 | Fixed an issue that caused the Client to crash when Cisco AnyConnect was also running on the device | Critical |
| 159274 | Fixed a connectivity issue when connecting to a Trusted Network | High |
| 162961 | Fixed an issue that caused slow connection time | High |
| 162380 | Fixed an issue where the Client could not detect a captive portal | Medium |
| 160499 | Fixed an issue that caused authentication to fail with battery saving was enabled | Medium |

### Known Limitation

- The Running Processes Device posture check cannot be performed on several executables that block the Cato API. For example: n6agent.exe, MsSense.exe, QualysAgent.exe, and SentinelAgent.exe

## Windows Client v5.21

During the week of December 14, 2025, we will begin rolling out the Windows Client version 5.21. This version includes:

- Improvements to the look and feel of the Client tray icon
- Resolved issues

### Resolved Issues v5.21

| ID | Description | Severity | Impacted Versions |
| --- | --- | --- | --- |
| 153314 | Fixed an issue that prevented manual PoP selection whenever the Connect on Boot checkbox was selected. | High | 5.18 and higher |
| 155308 | Fixed an issue that triggered an MFA prompt even when the user was already connected in Office Mode. | High | 5.8 and higher |
| 154819 | Fixed an issue where the client established a tunnel connection even while on a Trusted Network. | High | 5.18 and higher |
| 113963 | Fixed an issue where, under certain network conditions, office-based users were misclassified as external users, preventing Office Mode from engaging. | High | 5.12 and higher |
| 162961 | Fixed an issue where office networks could not be accurately identified | High | 5.12 and higher |
| 159274 | Fixed connectivity issues when the Client was connected to a trusted network | High | 5.12 and higher |

## Windows Client v5.20

During the week of November 10, 2025, we will begin rolling out the Windows Client version 5.20. This version includes the following resolved issues:

### Resolved Issues v5.20

| ID | Description | Severity | Impacted Versions |
| --- | --- | --- | --- |
| 140490 | Fixed an issue to improve the accuracy of the HTTPS probe for DEM. | High | 5.15 and higher |
| 139438 | Fixed an issue in which unrelated IPs were allocated to our WinTUN device. | High | 5.15 and higher |
| 143363 | Fixed an issue where automatic reconnection for clients using Always-On failed after the machine resumed from sleep state. | High | 5.16 and higher |

## Windows Client v5.18

During the week of October 19, 2025, we will begin rolling out the Windows Client version 5.18. This version includes the following resolved issues:

### Resolved Issues v5.18

| ID | Description | Severity | Impacted Versions |
| --- | --- | --- | --- |
| 111721 | Fixed an issue where Windows clients behind a Socket in Office Mode with Always-On intermittently failed to report the configured Device Posture Profile. | Critical | 5.12 and higher |
| 148024 | Fixed a stability issue causing occasional client crashes under specific runtime conditions. | Critical | 5.17 |
| 147493 | Fixed a reauthentication issue. | Critical | 5.16 and higher |
| 143835 | Fixed intermittent failures in device posture evaluation during the first sign-in. | Critical | 5.16 and higher |
| 143205 | Fixed a mismatch between Windows Defender ATP status and Client Connectivity Policy (CCP) evaluation when the client operated behind an office socket. | Critical | 5.17 |
| 143249 | Fixed an issue where the client could not be installed on 32-bit sytems running Windows 10. | High | 5.16 and higher |
| 146936 | Fixed an issue where the client failed to reauthenticate using an embedded browser. | High | 5.16 and higher |
| 142952 | Fixed an issue where the client was opening normally instead of minimized. | High |  |

## Windows Client v5.17

During the week of August 31, 2025, we will begin rolling out the Windows Client version 5.17. This version includes:

- [Resolved Issues](/docs/summary-of-cato-windows-client-releases#UUID-8dca8579-666e-3316-2caa-4a55d4345f26_section-idm2747298649572623) and Known Limitations

### Resolved Issues v5.17

| ID | Description | Severity | Impacted Versions |
| --- | --- | --- | --- |
| 113963 | Some users could not enter office mode for the first few minutes after connecting through a site | High | 5.11, 5.12 |
| 119921 | Some Clients were not communicating with Cato Cloud for a few minutes after the client network or power source changed | High | 5.13 |
| 128685 | Client UI misaligned for Korean users | Medium | 5.14 |

### Known Limitations v5.17

No known limitations for Windows Client v5.17.

## Windows Client v5.16

During the week of July 1, 2025, we are starting the rollout of Windows Client version 5.16. This version:

- [Resolved Issues](/docs/summary-of-cato-windows-client-releases#UUID-8dca8579-666e-3316-2caa-4a55d4345f26_section-idm2747298649572623) and Known Limitations
- Security update:
  - Updates the Client embedded browser to Chromium version 135.0.220
- Additional bug fixes and enhancements

### Resolved Issues v5.16

| ID | Description | Severity | Impacted Versions |
| --- | --- | --- | --- |
| 136449 | Users sometimes received a fatal exception error, causing the Client to stop working. This occurred after users rebooted their computers. | Critical | 5.15, 5.14 |
| 136300 | When Always-On and PreLogin were enabled on Windows endpoints, devices retained full Internet connectivity even while the Cato Client was in Limited Access mode. This occurred during the authentication process, specifically before MFA was completed. Users were able to access the Internet after dismissing the MFA prompt and before initiating a full VPN connection. | Critical | 5.15, 5.14 |
| 131251 | Improved the connection time after detecting if users are on a trusted or untrusted network. | Critical | 5.14 |
| 136943 | Users sometimes received the following error message: `Cato Client Server is not running. Please contact your administrator` This caused the Client to stop working. | High | 5.15, 5.14 |
| 130451 | Connection Failed error messages appeared even after the Client was connected. | High | 5.15 |

### Known Limitations v5.16

No known limitations for Windows Client v5.16.

## Windows Client v5.15

During the week of May 19, 2025, we are starting the rollout of Windows Client version 5.15. This version contains:

- **Advanced Device Posture Collection:** To improve performance when connecting, Device Posture is now collected continuously, even before connecting. After connecting, the Client continues to collect the Device Posture to ensure it remains up-to-date.
- [Resolved Issues](/docs/summary-of-cato-windows-client-releases#UUID-8dca8579-666e-3316-2caa-4a55d4345f26_N1752043129218) and [known limitations](/docs/summary-of-cato-windows-client-releases#UUID-8dca8579-666e-3316-2caa-4a55d4345f26_section-idm273493032652620)
- Additional bug fixes and enhancements

### Resolved Issues v5.15

| ID | Description | Severity |
| --- | --- | --- |
| 104446 | When there was an error with the embedded browser, the page was stuck with a blank white page. | Critical |
| 119923 | When the client received a token with user ID that is different from the stored user ID, it didn't update the token, which caused the authentication process to fail. | Critical |
| 122274 | When uploading a file while connected to the Windows Client, the Client would reconnect. | High |

### Known Limitations v5.15

| ID | Description | Severity |
| --- | --- | --- |
| 136943 | Users on Cato Client for Windows v5.15 and v5.14 might receive the following error: `Cato Client Server is not running. Please contact your administrator` This error causes the Client to stop working. | High |
| 136449 | Users on Cato Client for Windows v5.15 and v5.14 might experience a fatal exception error, causing the Client to stop working. This occurs after users reboot their computers. | Critical |
| 136300 | When Always-On and PreLogin are enabled on Windows endpoints, devices retain full Internet connectivity even while the Cato Client is in Limited Access mode. This occurs during the authentication process—specifically, before MFA is completed. Users are able to access the Internet after dismissing the MFA prompt and before initiating a full VPN connection. | Critical |

## Windows Client v5.14

During the week of March 17, 2025, we are starting the rollout of Windows Client version 5.14. This version contains bug fixes and enhancements.

In addition, Windows Client 5.14 installs a driver to support Anti-Tampering. This driver is not loaded unless you enable Anti-Tampering. For more information, see [Working with Anti-Tampering for the Cato Client (EA)](/v1/docs/working-with-anti-tampering-for-the-cato-client).

### Known Limitations v5.14

| ID | Description | Severity |
| --- | --- | --- |
| 136943 | Users on Cato Client for Windows v5.15 and v5.14 might receive the following error: `Cato Client Server is not running. Please contact your administrator` This caused the Client to stop working. | High |
| 136449 | Users on Cato Client for Windows v5.15 and v5.14 might experience a fatal exception error, causing the Client to stop working. This occurred after users rebooted their computers. | Critical |
| 136300 | When Always-On and PreLogin are enabled on Windows endpoints, devices retain full Internet connectivity even while the Cato Client is in Limited Access mode. This occurs during the authentication process—specifically, before MFA is completed. Users are able to access the Internet after dismissing the MFA prompt and before initiating a full VPN connection. | Critical |

## Windows Client v5.13

From January 5, 2025 we started the rollout of Windows Client version 5.13. This version contains:

- The following [DEM enhancements](/v1/docs/experience-monitoring) are now supported with this version:
  - **Underlay Performance Monitoring in Socket Last Mile**: Identify and diagnose out-of-tunnel issues that could impact last-mile performance
  - **Use Multiple Devices**: DEM hardware metrics are now grouped by device name, helping you easily understand the performance of each device when there are multiple devices for the same user
  - **Support for Different LAN Gateways**: LAN gateway probes are now grouped by LAN gateway IP, letting you easily understand the performance of each LAN gateway when different gateways are present at different timeframes
- Bug fixes and enhancements

## Windows Client v5.12

From November 3, 2024, we started the rollout of Windows Client version 5.12. This version contains:

- Bug fixes and enhancements, including:
  - Enabling the Always-On policy with the [registry key](/v1/docs/protecting-users-with-always-on-security) blocked access to Microsoft Self-Service Password Reset from the lock screen

## Windows Client v5.11.9

From August 16, 2024, we started the rollout of Windows Client version 5.11.9. This version contains:

- **Bug Fix:**
  - Resolved a connectivity issue impacting topologies that include a misconfigured DNS setting on the device network adapter set with an IPv6 address that does not respond

## Windows Client v5.11

From July 14, 2024, we started the rollout of Windows Client version 5.11. This version contains:

- **IPv6 Support for Last Mile Connection:** Users can connect remotely over ISPs that provide last-mile [IPv6-only](/v1/docs/cato-client-last-mile-support-for-ipv6) connections. Both IPv6 and IPv4 connections are now supported.
- **Authenticating with Windows Credentials Supported on Azure Hybrid AD Joined Devices:** Users on Azure Hybrid AD Joined Devices can authenticate [with their Windows credentials](/v1/docs/authenticate-users-automatically-with-windows-credentials) for an improved user experience. You can configure the Client to launch, add a user, authenticate, and connect without any user action. Azure AD with MFA is now also supported.
- **New Cato Root Certificate:** We added a new root certificate that is automatically installed on the device with the Cato Client.
  - The new certificate is called **Cato Networks Root CA** and expires in March 2034.
  - The previous certificate is from 2015 and is called **Cato Networks CA**. It will expire in Oct 2025.
- **Bug Fix:**
  - If a login attempt failed, in some cases users were unable to connect to the network

## Windows Client v5.10.34

From June 6th, 2024, we started the rollout of Windows Client version 5.10.34. This version contains an important security update and bug fixes. For details of the updates, see these articles:

- [Security Vulnerabilities in the Cato Client](%%LINK:19353019271325%%)
- [CVE-2024-6978 Windows SDP Client: Local root certificates can be installed by low-privileged users](/v1/docs/cve-2024-6978-windows-sdp-client-local-root-certificates-installed)
- [CVE-2024-6977 Windows SDP Client: Sensitive data in trace logs can lead to account takeover](/v1/docs/cve-2024-6977-windows-sdp-client-sensitive-data-trace-logs-account-takeover)
- [CVE-2024-6974 Windows SDP Client: Local Privilege Escalation via self-upgrade](/v1/docs/cve-2024-6974-windows-sdp-client-local-privilege-escalation-via-self-upgrade)
- [CVE-2024-6975 Windows SDP Client: Local Privilege Escalation via openssl configuration file](/v1/docs/cve-2024-6975-windows-sdp-client-local-privilege-escalation-openssl)
- [CVE-2024-6973 Windows SDP Client: Remote Code Execution via crafted URLs](/v1/docs/cve-2024-6973-windows-sdp-client-remote-code-execution-via-crafted-urls)

## Windows Client v5.10.26

From March 31st, 2024, we started the rollout of Windows Client version 5.10.26. This version contains bug fixes including:

- Anti-Malware Device Checks could not validate Microsoft Defender for Endpoint (Defender ATP) real-time protection

## Windows Client v5.10

From February 12th 2024, we started the rollout of Windows Client v5.10. This version contains:

- **User Notifications for CASB and DLP**: The device displays a notification to the user when their activity is blocked by App Control or Data Control rules. This educates the user about which app was blocked and why.
- Improved Client messages for failed upgrades and token expiration
- Stability enhancements, including Pre-login mode
- Bug fixes

## Known Limitations for Windows Client v5.2 and Higher

This section lists known limitations that apply to all the Windows Clients version 5.2 and higher.

- For deployments with a third-party proxy, Internet Explorer is not supported as the default browser.
  - Configure a different default browser on the device.

## Known Limitations for Windows Client v5.0 and Higher

This section lists known limitations that apply to all the Windows Clients version 5.0 and higher.

- This Client version uses the 85.255.31.1 IP address as part of the infrastructure to support Single Sign-On (SSO)
  - Make sure that this IP address is NOT blocked by any third-party anti-malware software
- For accounts that use Azure Conditional Access, please set the **Browser Authentication** to **External Browser** (Access > Client Access > Authentication) For more information about Browser Authentication, see [Configuring the Authentication Policy for Cato Clients](/v1/docs/configuring-the-authentication-policy-for-cato-clients)
- Set **Browser Authentication** to internal **In-Client Browser** to authenticate to OneLogin
- For OneLogin SSO, we recommend that you use the internal in-Client browser. When Browser Authentication is set to External Browser, if the browser window or tab is closed, the end-user can't authenticate to OneLogin
- Windows 8.1 OS is only supported when all the newest Microsoft updates and patches are installed
- Automatic Upgrade for Windows Servers is currently not supported
- Automatic Upgrade for the Windows Client version 5.0 is disabled for hosts that use the Windows Server operating system and the Trusted Browsing feature on the Windows Server blocks the Client from authenticating
  - Solution: To use Windows Client v5.0 on a Windows Server you can use one of the following solutions and then install or upgrade the new Client version:
    - Allowlist the domains for your IdP for Trusted Browsing
    - Disable the Trusted Browsing feature
- In some cases, for Windows devices with the Intel Killer Wireless NICs, after the Client connects to the network all traffic is blocked
  - Workaround: Disable the Killer Network Service on the Windows device, and then use the Cato Client to connect to the network
- When using TAP virtual adapter, the MAC address of the Cato virtual adapter in the Client is randomly generated and isn’t guaranteed to be unique across the Clients in your network. Sometimes the MAC address isn’t shown for the virtual adapter.
  - When the MAC address is required, we recommend that you use the MAC address of the physical device instead of the Client virtual adapter.
- If you change the default installation folder, during a Client upgrade or if you delete the Client, other files within the directory are deleted. If you add items to the default installation folder (C:\Program Files\Cato Networks\) they are deleted during a Client upgrade or if you delete the Client.
- If IP routing is enabled on the device, the Client cannot authenticate.
  - Workaround: Disable IP routing on Windows. For more information, see [IP Routing Prevents Windows Client Authentication](/v1/docs/ip-routing-prevents-windows-client-authentication).
