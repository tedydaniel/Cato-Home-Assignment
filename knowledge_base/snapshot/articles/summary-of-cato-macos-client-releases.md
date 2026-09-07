---
title: "Summary of Cato macOS Client Releases"
slug: "summary-of-cato-macos-client-releases"
updated: 2026-08-30T12:36:55Z
published: 2026-08-30T12:36:55Z
canonical: "knowledge.catonetworks.com/summary-of-cato-macos-client-releases"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Summary of Cato macOS Client Releases

This article summarizes features, enhancements, and bug fixes for macOS Clients.

In addition, it also lists the known limitations.

Admins and users can easily download the Client from the [Client download portal](https://clientdownload.catonetworks.com/) without requiring authentication.

For more information about the requirements to implement Cato's remote access in your organization, see [Preparing to Install the Cato Client](/v1/docs/preparing-to-install-the-cato-client).

## macOS Client v6.1

Starting Aug. 30, 2026, we are rolling out macOS Client version 6.1. This version contains:

### Enhancements:

- Improved certificate validation process for DTLS tunnel connections
- Prevent installation of the Client on unsupported versions. This includes any macOS version before macOS 14 (Sonoma).
- Automatic reconnection through a better network interface if one becomes available

### Bug Fixes

| ID | Description | Severity |
| --- | --- | --- |
| 206226 | Fixed an issue where the Client could crash when retrieving the active user | Critical |
| 191891 | Fixed an issue where users could connect to invalid PoPs | Critical |
| 198931 | Fixed an issue where the Client did not connect after startup when Always-On was enabled | Critical |

## macOS Client v6.0.1

Starting June 29, 2026, we are rolling out macOS Client version 6.0.1. This version contains:

| ID | Description | Severity |
| --- | --- | --- |
| 180049 | Fixed an issue where the Client could crash when DEM is in use | Critical |
| 88259 | Fixed an issue where access could be denied due to an unexpected Device Posture detection failure | Critical |
| 177500 | Fixed an issue where Client was unable to detect Iru, formerly Kandji, for Device Posture checks | High |

## macOS Client 5.13.1

Starting June 21, we are rolling out macOS Client version 5.13.1.

- macOS Client v5.13.1 (build 11418) includes a security patch

### Bug Fixes

macOS Client v5.13.1 includes the following bug fix:

| ID | Description | Severity |
| --- | --- | --- |
| 182301 | Fixed an issue with the installation process | Critical |

## macOS Client v5.13

Starting May 3, 2026, we are rolling out macOS Client version 5.13. This version includes:

- The tray icon highlights whether the Client has secure Private access, secure Internet access, or both
- Quicker detection of WiFi network changes

### Bug Fixes

macOS Client v5.13 includes the following bug fixes:

| ID | Description | Severity |
| --- | --- | --- |
| 176907 | Fixed an issue where the Client could crash with a SIGTRAP error when the device entered sleep mode | Critical |
| 128683 | Fixed an issue where the macOS Client could become unresponsive during authentication when using an external browser | Critical |
| 162721 | Fixed an issue where the Client Connectivity policy did not function as expected when device posture checks for registry keys were in use. | Critical |
| 167767 | Fixed an issue that caused increased battery consumption during Client operation | High |
| 172284 | Fix an issue of intermittent disconnections related to DNS resolution flow | High |
| 174502 | Fixed an issue where Device Posture updates were delayed and did not match the correct rules | High |

## macOS Client v5.11

Starting February 15, 2026, we are rolling out macOS Client version 5.11. This version includes:

- Bug fixes
- Known limitation

### Bug Fixes

macOS Client v5.11 includes the following bug fixes:

| ID | Description | Severity |
| --- | --- | --- |
| 154781 | Fixed an issue where connection establishment was stuck in authentication when private access expired during sleep and in other scenarios. | Critical |
| 143420 | Fixed an issue where Device Posture checks based on Admin selection only did not take effect when the client was behind a socket (on site). | Critical |
| 122465 | Fixed an issue where user re-authentication was not working with the embedded browser. | Critical |
| 155183 | Fixed an issue where the device posture checks for anti malware was not able to detect Symantec Endpoint Protection | High |
| 148819 | Fixed an issue of client crash related to Always On configuration change. | High |
| 129065 | Fixed an issue where the Client crashed during large files transfers | High |
| 140636 | Fixed an issue where the user name or host names was missing in events for remote users | Medium |

#### Known Limitations

- In some cases, when a user tries to authenticate with SSO after a private access session expires, an empty webpage briefly appears.

## macOS Client v5.10.6

Starting November 2, 2025, we are rolling out macOS Client version 5.10.6. This version includes:

- Support for a fully silent installation, including EULA suppression
- Stability improvements
- Security updates
- Bug fixes

### Bug Fixes

macOS Client v5.10.6 includes the following bug fixes:

| ID | Description | Severity |
| --- | --- | --- |
| 143943 | Fixed an issue where SDP remote users not behind a socket would be erroneously identified as being on an office network. | Critical |
| 148645 | Fixed an issue where the clients were not sending DEM data when connected through office mode. | High |
| 143501 | Fixed an issue where Clients that connected to a different PoP during maintenance continued to connect to that PoP even after the maintenance was completed. | Critical |

## macOS Client v5.10.5

Starting October 5, 2025, we are rolling out macOS Client version 5.10.5. This version includes:

- Support for macOS Tahoe 26.
- Stability improvements
- Security updates
- Bug fixes

### Bug Fixes

macOS Client v5.10.5 includes the following bug fixes:

| ID | Description | Severity |
| --- | --- | --- |
| 144198 | User reauthentication was not working for customers using the embedded browser | Critical |

### Known Limitations

There are no known limitations for macOS Client 5.10.5.

## macOS Client v5.10

Starting August 18, 2025, we are rolling out macOS Client version 5.10. This version includes:

- Support for [remote internet security with one-time authentication](/v1/docs/remote-internet-security-with-one-time-authentication). This enables users to always have connectivity and protection with minimal interaction with the Client. Previously supported only for the Windows client. To see if this impacts your users, read our [FAQ](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings).
- An updated user interface that now includes more connectivity details

![macOS_client_510_UI.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35807952484637.png)
- Performance enhancements and bug fixes

### Known Limitations

There are no known limitations for macOS Client 5.10.

## macOS Client v5.9

Starting June 22, 2025, we are rolling out macOS Client version 5.9. This version includes:

- Prevent installation of the Client on unsupported versions. This includes any macOS version prior to macOS 13.3 (Ventura).
- Bug fixes and known limitations

### Bug Fixes

macOS Client v5.9 includes the following bug fixes:

| ID | Description | Severity |
| --- | --- | --- |
| 119486 | After users disconnected the Client, sometimes the Client failed to authenticate and connect again. | Critical |
| 121753 | When connecting in Office Mode, the Client took a long time to detect Office Mode and connect. | Critical |
| 119825 | Device Posture for certificates allowed connections for new Client versions, even when there was an invalid certificate. | High |

### Known Limitations

macOS Client v5.9 has the following known limitations:

| ID | Description | Severity |
| --- | --- | --- |
| 129474 | **Duplicate Browser Window for External Browser Authentication:** For Clients that use the external browser, when adding a new user with MFA, the Client occasionally opens a duplicate browser window. After entering credentials, users would then need to click Open Browser again to complete the MFA process. | High |
| 107091 | **Occasional Issues with Sending Logs:** In certain cases, the Client fails to **Send Logs** and instead shows an error message. The logs aren’t shared with Support. **Workaround:** Save logs locally with **Save to Device** and then send the log file to Support. | Low |

## macOS Client v5.8

Starting March 24, 2025, we are rolling out macOS Client version 5.8.5. This version includes:

- Support for the following [DEM enhancements](/docs/summary-of-cato-macos-client-releases#UUID-aba51f26-99bc-9966-ac93-bc6445672b14):
  - **Underlay Performance Monitoring in Socket Last Mile:** Identify and diagnose out-of-tunnel issues that could impact last-mile performance
  - **Group Multiple Devices:** DEM hardware metrics are now grouped by device name, helping you easily understand the performance of each device when there are multiple devices for the same user
  - **Support for Different LAN Gateways:** LAN gateway probes are now grouped by LAN gateway IP, letting you easily understand the performance of each LAN gateway when different gateways are present at different timeframes
- **Record Client Issues**: An additional troubleshooting tool that lets users [record](/v1/docs/recording-issues-using-the-cato-client) and then reproduce an issue that occurred with the Client. The traffic capture and log files can be uploaded to Support for further analysis.
  - This feature and the existing ability to send logs to Support are available on the new Support tab in the Client
- **Updated OPSWAT OESIS Framework**: We updated the OPSWAT OESIS framework used by the Client to version 4.3.3685
- Critical bug fixes for Device Posture to support macOS v15.2 (Sequoia)
  - Cato discovered issues when using earlier versions of the macOS Client on Sequoia while using Device Posture
    - Upgrade your macOS Client to v5.8.5 before upgrading your device to Sequoia
    - If you have already upgraded your OS version to macOS Sequoia, contact Customer Support to get the Client v5.8.5 release
- macOS Client v5.8 includes a security patch that fixes [CVE-2025-3886](https://www.cve.org/CVERecord?id=CVE-2025-3886)
- Bug fixes and enhancements

## macOS Client v5.7

From July 14, 2024, we are starting the rollout of macOS Client version 5.7. This version contains:

- **IPv6 Support for Last Mile Connection:** Users can connect remotely over ISPs that provide last-mile [IPv6-only](/v1/docs/cato-client-last-mile-support-for-ipv6) connections. Both IPv6 and IPv4 connections are now supported.
- **User Notifications for CASB and DLP:** The device displays a notification to the user when their activity is blocked by [App Control](/v1/docs/managing-the-application-control-policy) or [Data Control](/v1/docs/creating-the-data-control-policy) rules. This educates the user about which app was blocked and why.
- **End User Feedback:** To help us continually improve our remote access, users can now provide [feedback](/v1/docs/providing-cato-with-remote-user-feedback) to Cato from within the Client.
  - Every few months, users are prompted to give a rating and comments
  - Users can also manually provide feedback at any time
- **End of Support for Big Sur:** Devices running Big Sur (macOS 11) are no longer supported by the macOS Client
- **New Cato Root Certificate:** We added a new root certificate that is automatically installed on the device with the Cato Client.
  - The new certificate is called **Cato Networks Root CA** and expires in March 2034.
  - The previous certificate is from 2015 and is called **Cato Networks CA**. It will expire in Oct 2025.
- **Bug fix:**
  - If a login attempt failed, in some cases users were unable to connect to the network

## macOS Client v5.6

The gradual rollout of macOS Client version 5.6 started on the week of Apr. 15th, 2024. This version contains:

- **Device Posture Check for Disk Encryption**: You can now include a check for Disk Encryption within your [Device Posture Profiles](/v1/docs/creating-device-posture-profiles-and-device-checks). The Device Posture Profile can be included in your Client Connectivity and Security policies
- **Updated Client Tray Icon**: We improved how the Client’s tray icon indicates a connected or disconnected status
- **New Indication of System Notification Status**: On the Settings page, we added the status of System Notifications and improved the messaging to highlight their importance
- Bug fixes and stability improvements

## Known Limitations for macOS Client 5.7

This section lists known limitations that apply to all the macOS Client version 5.7:

As a result of these limitations, we do not recommend installing macOS Sequoia (version 15) on devices running Client version 5.7 and lower.

- On macOS Sequoia (version 15), on the **Settings** page of the Client, if you click **Download logs**, the logs are not downloaded
- On macOS Sequoia (version 15), after connecting and minimizing the Client, it cannot be opened

## Known Limitations for macOS Client v5.5

This section lists known limitations that apply to all the macOS Clients version 5.5 and higher.

- On devices running macOS Sonoma (v14), start minimized is not supported. If Always-On is enabled the Client opens after the device boots.

## Known Limitations for macOS Client 5.4

This section lists known limitations that apply to all the macOS Clients version 5. and higher.

- If you downgrade the Client to v5.3, it may become unresponsive. To resolve this issue, restart the Client from the Application folder or Launchpad.
- If you downgrade the Client to v5.3, users other than the last connected user are removed
- With Always-On enabled, after a device wakes up or connects to a network, if Zoom is installed on the device, the Zoom app may open a pop up with a connection error. To resolve this issue, restart Zoom.
- If you manually install the VPN Profile and have Device Certificate checks included in the Device Posture Profile, a pop up is displayed requesting the keychain password.
- If you upgrade the Client with an MDM, pop ups are sometimes displayed requesting permission to allow the installation of system extensions and the VPN configuration.

To prevent this issue, you can first distribute the permissions for DMG extension and the VPN payload, then distribute the Clients to the macOS hosts.
- Connecting to Cato is only supported from within the Client. Connecting from **System Preferences > Network** (or from macOS Ventura **System Settings > VPN**) on the device is not supported.

## Known Limitations for macOS Client v5.3

This section lists known limitations that apply to all the macOS Clients version 5.3 and higher.

- After a device wakes up from sleep, the Client may accidentally show a message that the upgrade failed. No action is required, a few minutes after closing the message the Client automatically attempts to upgrade again.
- SDP users cannot disable office mode.

## Known Limitations for macOS Client v5.0 and Higher

This section lists known limitations that apply to all macOS Clients version 5.0 and higher.

- When a macOS device enters sleep mode, the Cato Client may disconnect from the VPN after a few minutes of inactivity. This behavior affects background connectivity and may interrupt services that rely on persistent VPN access.
  - This can impact apps, such as if the macOS device receives an incoming Microsoft Teams call while the device is in sleep mode and the Cato Client is disconnected. The Teams call may disconnect when the Client automatically reconnects to the network.
- This Client version uses the 85.255.31.1 IP address as part of the infrastructure to support Single Sign-On (SSO)
  - Make sure that this IP address is NOT blocked by any third-party anti-malware software
- For accounts that use Azure Conditional Access, please set the **Browser Authentication** to **External Browser** (Access > Client Access > Authentication) For more information about Browser Authentication, see [Configuring the Authentication Policy for Cato Clients](/v1/docs/configuring-the-authentication-policy-for-cato-clients)
- For macOS devices with the Symantec Web Security Service (WSS) agent installed, we do not currently support installing the WSS agent and the macOS Client on the same device
- Uploading a local split-tunnel file to the Client is not supported. You can use the global split-tunnel settings in the Cato Management Application
- For OneLogin SSO, we recommend that you use the internal in-Client browser. When Browser Authentication is set to External Browser, if the browser window or tab is closed, the end-user can't authenticate to OneLogin
- In some cases, this version might experience problems with these configurations:
  - Azure Conditional Access
  - Proxy configuration
  - For accounts that use a third-party proxy, make sure to whitelist the following items (for both HTTP and HTTPS):
    - IP address - 85.255.31.1
    - URL - sso.ias.catonetworks.com
