---
title: "Summary of Cato Android Client Releases"
slug: "summary-of-cato-android-client-releases"
updated: 2026-08-30T13:15:20Z
published: 2026-08-30T13:15:20Z
canonical: "knowledge.catonetworks.com/summary-of-cato-android-client-releases"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Summary of Cato Android Client Releases

This article summarizes the features and enhancements of supported Android Client versions.

In addition, it also lists the known limitations.

Admins and users can easily download the Client from the [Client download portal](https://clientdownload.catonetworks.com/) without requiring authentication.

For more information about the requirements to implement Cato's remote access in your organization, see [Preparing to Install the Cato Client](/v1/docs/preparing-to-install-the-cato-client).

## Android SDP Clients

This section summarizes the features and enhancements of the Android Client.

### Android Client v5.6.2

Android Client v5.6.2 will be uploaded to the Google Play Store during the week of Aug. 30, 2026. This version includes:

- Improved certificate validation process for DTLS tunnel connections

### Android Client v5.6.1

Android Client version 5.6.1 will be uploaded to the Google Play Store during the week of July 19, 2026. This version includes:

### Bug Fixes

| ID | Description | Severity |
| --- | --- | --- |
| 195331 | Fixed an issue that could disconnect the Client and prevent automatic reconnection until the app was manually restarted. | High |

### Android Client v5.6

Android Client version 5.6 will be uploaded to the Google Play Store during the week of June 21, 2026. This version includes:

- The End-User License Agreement (EULA) is displayed the first time the Client launches (for a newly installed Client and an upgrade)
  - MDM administrators can suppress this for managed deployments
  - After upgrading, users with Always-On enabled must accept the EULA for the Client to connect
- A minimum Android OS version can be enforced in a Device Posture check
- To ensure stable Always-On connectivity, the Client displays an in-app message when Android Battery Optimization is enabled to advise users to disable it
- Security fixes and stability improvements

### Bug Fixes

| ID | Description | Severity |
| --- | --- | --- |
| 184168 | Improved connectivity stability when re-authenticating after switching between Wi-Fi and mobile data | Medium |

### Android Client v5.5.1

Android Client version 5.5.1 will be uploaded to the Google Play Store during the week of May 17, 2026. This version includes:

#### Bug Fixes

| ID | Description | Severity |
| --- | --- | --- |
| 179227 / 178601 | Fixed multiple issues where the Client was stuck in a Connecting state | Critical |

### Android Client v5.5

Android Client version 5.5 will be uploaded to the Google Play Store during the week of April 5, 2026. This version includes:

- Users can select which browser to use for authentication when Identity Provider servers only accept requests from specific browsers. This option is available on the **Settings** tab.

#### Bug Fixes

Android Client v5.5 includes the following bug fixes:

| ID | Description | Severity |
| --- | --- | --- |
| 172675 | Fixed a routing issue that could connect Clients to a non-optimal PoP | Critical |
| 173486 | Fixed an issue where users were stuck in connecting | Critical |
| 173019 | Resolved a reconnection issue when switching from cellular to Wi-Fi, improving client recovery and session continuity | High |
| 168502 | Fixed a crash during authentication that could prevent users from completing sign-in | Medium |

### Android Client v5.4

Android Client version 5.4 will be uploaded to the Google Play Store during the week of February 15, 2026. This version includes:

#### Bug Fixes

Android Client v5.3 includes the following bug fixes:

| ID | Description | Severity |
| --- | --- | --- |
| 114155 | Fixed various issues that caused the Client to crash or get stuck during connection, disconnection, authentication, or network switching | High |
| 164098 | Fixed an issue that caused an error when connecting to Android Auto | High |
| 155953 | Enhanced error messages to be clearer and more actionable, improved telemetry with richer timestamp data for better troubleshooting, and fixed an issue where client log uploads failed when using specific certificates. | Medium |
| 114930 | Resolved multiple Chromebook-specific issues that caused client crashes, blank or white screens, unclear error messages, and authentication or reauthentication failures | Low |
| 115402 | Fixed issues that caused reauthentication or reconnection failures after session expiration, authentication changes, or user and network switches. Also resolved an issue that prevented adding Azure users to the Client | Low |

### Android Client v5.3

Android Client version 5.3 will be uploaded to the Google Play Store during the week of November 30, 2025. This version includes:

#### Bug Fixes

Android Client v5.3 includes the following bug fix:

| ID | Description | Severity |
| --- | --- | --- |
| 154363 | Fixed an issue where the Client could get stuck after exiting sleep mode. | Critical |

### Android Client v5.2.1

Android Client version 5.2.1 was uploaded to the Google Play Store on September 28, 2025. This version includes:

- **Enhanced Client PoP Selection:** We improved the PoP selection process to better consider multiple factors, including geography and availability. The Client now more accurately selects the best PoP to connect to

#### Bug Fixes

Android Client v5.2.1 includes the following bug fixes:

| ID | Description | Severity |
| --- | --- | --- |
| 140040 | Fixed an issue causing the Client to sometimes get stuck and require rebooting the Android device. | Critical |
| 149283 | Fixed an issue causing Clients to get stuck when reconnecting in some environments. | Critical |
| 129711 | Fixed an issue in some environments, causing the Client to require manual reauthentication after unlocking the device if this was done after a prolonged device lock. | High |
| 116201 | Fixed an issue causing the Client to sometimes fail to automatically reconnect when switching from WiFi to 4G. | Medium |
| 91599 | Fixed an issue in which the Device Name information was missing in events for Android devices. | Low |

### Android Client v5.0.2

Android Client version 5.0.2 was uploaded to the Google Play Store on November 13th, 2022, and includes:

- Bug fixes and enhancements

## Known Limitations for Android Client v5.0:

This section lists known limitations that apply to all the Android Clients version 5.0.

- For Split Tunnel - only Include Mode is supported for Android devices v12.x and lower. Exclude Mode is supported for Android OS devices v13.0 and higher.
- When the Android Client uses a Bypass Code, events are not generated. Events are still generated for other Client OS.
