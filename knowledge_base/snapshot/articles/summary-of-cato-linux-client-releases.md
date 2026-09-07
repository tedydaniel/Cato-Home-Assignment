---
title: "Summary of Cato Linux Client Releases"
slug: "summary-of-cato-linux-client-releases"
status: "update"
updated: 2026-09-06T10:25:19Z
published: 2026-09-06T10:25:19Z
canonical: "knowledge.catonetworks.com/summary-of-cato-linux-client-releases"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Summary of Cato Linux Client Releases

This article summarizes features and enhancements of Linux Clients.

In addition, it also lists the known limitations.

Admins and users can easily download the Client from the [Client download portal](https://clientdownload.catonetworks.com/) without requiring authentication.

For more information about the requirements to implement Cato's remote access in your organization, see [Preparing to Install the Cato Client](/v1/docs/preparing-to-install-the-cato-client).

## Linux Clients

This section summarizes the features and enhancements of Linux Clients:

### Linux Client v5.8.2

Starting Sept 6, 2026, we are rolling out Linux Client version 5.8.2. This version contains the following:

- Improved certificate validation process for DTLS tunnel connections
- Support for ARM64 architecture, expanding compatibility to ARM-based Linux devices and servers.
- Stability improvements, security updates, and bug fixes

#### Resolved Issues v5.8.2

| ID | Description | Severity |
| --- | --- | --- |
| 188257 | Resolved an issue where importing a device certificate on the Linux Client failed when a relative file path was used with the `cato-sdp import-cert` command. | High |

### Linux Client v5.7

Starting April 26, 2026, we are rolling out Linux Client version 5.7. This version contains the following:

| ID | Description | Severity |
| --- | --- | --- |
| 172898 | Fixed an issue where authentication could time out and prevent the browser sign-in window from opening | Critical |
| 160220 | Fixed an issue that impacted the stability of the Cato Client, related to daemon responsiveness and connection failures | High |
| 177067 | Fixed an issue that could cause intermittent disconnections due to client crashes | High |

### Linux Client v5.6

Starting February 15, 2026, we are rolling out Linux Client version 5.6. This version contains the following:

- Client installation package certificate updated

#### Resolved Issues v5.6

| ID | Description | Severity |
| --- | --- | --- |
| 156571 | Fixed an issue where using the --no-office-mode flag could return a (null) error and prevent the client from connecting when placed behind a socket | Medium |

### Linux Client v5.5

Starting July 13, 2025, we are rolling out Linux Client version 5.5. This version contains the following:

- New features
- Resolved issues
- Security update
  - Security patch for a vulnerability (CVE-2025-7012) impacting Linux Clients v5.4 and lower

Linux Client v5.5 is supported from Ubuntu v20 and higher

#### New Features

Linux Client v5.5 includes the following new features:

- Advanced Device Posture Collection - To improve performance when connecting, Device Posture is now collected continuously, even before connecting, to ensure Device Posture stays up-to-date

#### Resolved Issues v5.5

| ID | Description | Severity | Impacted Versions |
| --- | --- | --- | --- |
| 131555 | Resolved a crash on Fedora distributions caused by an earlier version of the OPSWAT library. | High | 5.4 |
| 119825 | Device Posture for certificates allowed connections for new Client versions, even when there was an invalid certificate. | High | 5.4 |

### Linux Client v5.4

From March 17, 2025, we started the rollout of Linux Client version 5.4. This version contains bug fixes and enhancements.

### Linux Client v5.3

From November 10, 2024, we started the rollout of Linux Client version 5.3. This version contains:

- **Device Checks Applied Behind a Site**: To enforce device compliance requirements behind a site, [Device Posture Profiles](/v1/docs/creating-device-posture-profiles-and-device-checks) are applied to devices behind a Socket.
- **Updated OPSWAT OESIS Framework**: We updated the [OPSWAT OESIS framework](https://www.opswat.com/products/endpoint-security-sdk/device-compliance) used by the Client to version 4.3.3404.
- Bug fixes and enhancements, including:
  - In some cases, the Identity Agent did not correctly identify users

### Linux Client v5.2.1.1

From June 6th, 2024, we started the rollout of Linux Client version 5.2.1.1. This version contains an important security update and bug fixes. For details of these updates, see these articles:

- [Security Vulnerabilities in the Cato Client](https://support.catonetworks.com/hc/en-us/articles/19353019271325-Security-Vulnerabilities-in-the-Cato-Client)
- [CVE-2024-6978 Windows SDP Client: Local root certificates can be installed by low-privileged users](/v1/docs/cve-2024-6978-windows-sdp-client-local-root-certificates-installed)
- [CVE-2024-6977 Windows SDP Client: Sensitive data in trace logs can lead to account takeover](/v1/docs/cve-2024-6977-windows-sdp-client-sensitive-data-trace-logs-account-takeover)
- [CVE-2024-6974 Windows SDP Client: Local Privilege Escalation via self-upgrade](/v1/docs/cve-2024-6974-windows-sdp-client-local-privilege-escalation-via-self-upgrade)
- [CVE-2024-6975 Windows SDP Client: Local Privilege Escalation via openssl configuration file](/v1/docs/cve-2024-6975-windows-sdp-client-local-privilege-escalation-openssl)
- [CVE-2024-6973 Windows SDP Client: Remote Code Execution via crafted URLs](/v1/docs/cve-2024-6973-windows-sdp-client-remote-code-execution-via-crafted-urls)

### Linux Client v5.2

From, Jan 22nd, 2024, we started the rollout of Linux Client version 5.2. This version contains:

- **Connect on Boot:** The Client connects to the Cato Cloud automatically, without any user interaction, after the device boots
- **User Authentication is No Longer Required Behind a Site**: To simplify the user experience for users behind a site, the Client can connect automatically in Office Mode without users manually authenticating. There is no impact on Security and User Awareness polices
- Bug fixes and enhancements, including:
  - Improved process for prioritizing which PoP the Client connects to
  - Faster time to reconnect when the Client changes from an out of office network to an office network
