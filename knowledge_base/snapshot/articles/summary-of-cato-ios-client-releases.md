---
title: "Summary of Cato iOS Client Releases"
slug: "summary-of-cato-ios-client-releases"
updated: 2026-08-30T12:42:08Z
published: 2026-08-30T12:42:08Z
canonical: "knowledge.catonetworks.com/summary-of-cato-ios-client-releases"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Summary of Cato iOS Client Releases

This article summarizes the features and enhancements of iOS Clients according to the specific version.

In addition, it also lists the known limitations.

The iOS Client can be downloaded from the App Store (for iOS and iPadOS).

For more information about the requirements to implement Cato's remote access in your organization, see [Preparing to Install the Cato Client](/v1/docs/preparing-to-install-the-cato-client).

## iOS Clients

This section summarizes the features and enhancements of iOS Clients.

### iOS Client v5.9

During the week of Aug. 30, 2026, the iOS Client version 5.9 will be available for download from the App Store. This version includes:

- Improved certificate validation process for DTLS tunnel connections
- Prevent installation of the Client on unsupported versions. This includes any iOS version before iOS 17.

#### Resolved Issues v5.9

| ID | Description | Severity |
| --- | --- | --- |
| 196379 | Fixed an issue where canceling external-browser authentication could leave the Client stuck in the authentication process and prevent reopening the identity provider. | High |
| 196178 | Fixed an issue where the Client could remain in **Temporary Disconnect** after the bypass period ended instead of reconnecting automatically. | Medium |

### iOS Client v5.8.2

During the week of May 17, 2026, the iOS Client version 5.8.2 will be available for download from the App Store. This version includes:

#### Resolved Issues v5.8.2

| ID | Description | Severity |
| --- | --- | --- |
| 173903 | Fixed an issue that caused reduced connectivity if Always-On was enabled. | High |
| 169534 | Fixed an issue that prevented the device's default browser from being used for authentication. | High |

### iOS Client v5.8

During the week of March 8, 2026, the iOS Client version 5.8 will be available for download from the App Store. This version includes:

#### Resolved Issues v5.8

| ID | Description | Severity |
| --- | --- | --- |
| 163561 | Fixed a connectivity issue when using in-flight Wi-Fi | Critical |
| 164795 | Fixed an issue where websites could not be accessed when the client was connected after coming back from sleep | High |

### iOS Client v5.7

During the week of January 25, 2026, the iOS Client version 5.7 will be available for download from the App Store. This version includes:

- Support for iOS 26

#### Resolved Issues v5.7

| ID | Description | Severity |
| --- | --- | --- |
| 160069 | Fixed an issue of no device connectivity after device wakes from lock when the Client is in Always-On | Critical |
| 147326 | Fixed an issue where the Client in Always-On reconnection failed after device sleep | Critical |
| 156904 | Fixed an issue of long connection time of an Always-On client after device lock | Critical |
| 155923 | Fixed an issue where MFA was prompted before the client was connected in Always-On mode | Critical |
| 156255 | Fixed an issue of missing WhatsApp notifications while the device was locked and the Client is in Always-On | High |

### iOS Client v5.6.4

During the week of November 16, 2025, the iOS Client version 5.6.4 will be available for download from the App Store. This version includes:

#### Resolved Issues v5.6.4

| ID | Description | Severity |
| --- | --- | --- |
| 152918 | Fixed an issue where the Client could get stuck after exiting sleep mode. | Critical |

### iOS Client v5.6.2

During the week of October 19, 2025, the iOS Client version 5.6.2 will be available for download from the App Store. This version includes:

#### Resolved Issues v5.6.2

| ID | Description | Severity |
| --- | --- | --- |
| 147005 | Fixed an issue where the Client could get stuck after exiting sleep mode. Issue persisted until 5.6.4 | High |

### iOS Client v5.6

From July 21, 2025, the iOS Client version 5.6 will be available for download from the App Store. This version includes the following:

- New Features
- Fixed Bugs
- Known Limitations

#### New Features

iOS Client version 5.6 includes the following new features:

- Support for [Internet recovery](/v1/docs/protecting-users-with-always-on-security) when a connection to Cato can’t be established.
- Support for [user-controlled](/v1/docs/protecting-users-with-always-on-security) Always-on Bypass.
- Updated the Client embedded browser to Chromium version 135.0.220.
- Additional performance enhancements

#### Fixed Bugs

iOS Client version 5.6 includes the following bug fixes:

| ID | Description | Severity |
| --- | --- | --- |
| 126489 | Fixed an issue where the Client could get stuck on “Authenticating” after the first unlock following a device reboot, especially when connected to 4G/LTE. | High |
| 123838 | Fixed an issue where the Client occasionally entered a “Disconnecting” state after the device was unlocked from sleep. This caused a temporary loss of Internet connectivity for all apps until the Client reconnected. | High |
| 122679 | Fixed an issue where the Client experienced delays of several seconds when reconnecting after the device was unlocked from sleep or when using the Disconnect/Connect button. | High |
| 115153 122421 | Fixed an issue where SSO authentication with EntraID failed due to a missing device identifier, resulting in the error: `device identifier: not available` | High |
| 124624 | Fixed an issue where iOS devices managed via an MDM created a duplicate VPN profile when a certificate check was added to the device posture configuration. This second profile overrode the Always-On setting, allowing users to disconnect manually. T | Medium |

#### Known Limitations

iOS Client version 5.6 does not have any known limitations.

### iOS Client v5.5

From February 23, 2025, the iOS Client version 5.5 will gradually be available for download from the App Store. The version can currently be downloaded [here](https://testflight.apple.com/join/ob2m1ra0).

- **Improved detection of Office Network:** For users with iOS connecting behind a site, we have improved the way the Client identifies that it should enter Office Mode.
- **Idle mode enhancements:** The following improvements were made for Idle mode:
  - Improved connection time when returning from Idle mode
  - For organizations using the Always On feature, improved the notifications process from Apple notification service (APNS). This feature will be available over the coming weeks
- Bug fixes and stability improvements, including:
  - If detection of Captive Portal is blocked by a network rule, the Client continues to try and reconnect
  - Removed user notification for certificate check when not required
- Supported from iOS v16.x and higher.

### iOS Client v5.4

From September 29, 2024, the iOS Client version 5.4 will gradually be available for download from the App Store. The version contains:

- **IPv6 Support for Last Mile Connections:** Users can connect remotely over ISPs that provide last mile [IPv6-only](/v1/docs/cato-client-last-mile-support-for-ipv6) connections. Both IPv6 and IPv4 connections are now supported.
- **User Notifications for CASB and DLP:** The device displays a notification to the user when their activity is blocked by [App Control](/v1/docs/managing-the-application-control-policy) or [Data Control](/v1/docs/creating-the-data-control-policy) rules. This educates the user about which app was blocked and why.
- Bug fixes and stability improvements

### iOS Client v5.3

From April 30th, 2024, the iOS Client version 5.3 will gradually be available for download from the App Store. This version contains:

- **New Device Posture Check for Device Certificates Provides Increased Security**: You can now include a check for Device Certificates within your [Device Posture Profiles](/v1/docs/creating-device-posture-profiles-and-device-checks). The Device Posture Profile can be included in your Client Connectivity and Security policies
- **Increased Visibility of Connection Data**: The Statistics page in the Client now displays the status of the Split Tunnel Policy and the Proxy Configuration Policy
- Bug fixes and enhancements

### iOS Client v5.2.1

The iOS Client version 5.2.1 will gradually be available for download from the App Store from Feb 4th, 2024. This version contains bug fixes and enhancements including:

- Reduced the time it takes for the Client to connect
- Resolved an issue where the connection time stopped even if the Client was connected to the Cato Cloud

### iOS Client v5.1.1

The iOS Client version 5.1.1 was available in the iOS App Store from June 12th, 2023. This version contains bug fixes and enhancements including:

- Resolved an issue where some SDP users couldn’t upload large files when the Client was connected to the Cato Cloud

## Known Limitations for iOS Clients v5.0

This section lists known limitations that apply to all iOS Clients version 5.0 and higher.

- When a phone enters sleep mode, the Cato Client may disconnect from the VPN after a few minutes of inactivity. This behavior affects background connectivity and may interrupt services that rely on persistent VPN access.
  - This can impact apps, such as if the phone receives an incoming Microsoft Teams call while the phone is in sleep mode and the Cato Client is disconnected. The Teams call may disconnect when the Client automatically reconnects to the network.
- For accounts that use Device Authentication with a certificate, when the iOS device recovers from sleep mode, you need to open the Client (doesn't include Always On)
