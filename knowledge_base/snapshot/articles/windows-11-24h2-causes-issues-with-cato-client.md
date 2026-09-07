---
title: "Windows 11 24H2 Causes Issues with Cato Client"
slug: "windows-11-24h2-causes-issues-with-cato-client"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/windows-11-24h2-causes-issues-with-cato-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Windows 11 24H2 Causes Issues with Cato Client

## Overview

Upgrading to Windows 11 version 24H2 may introduce compatibility issues that affect the functionality of the Cato SDP Client and services running over the Cato Cloud. This article outlines the challenges you might face and provides possible solutions to address them.

## Environment

These issues can occur under the following conditions:

- Windows 11 version 24H2 (build 10.0.26100)
- Cato SDP Client

## Recommendations

- Before upgrading to Windows 11 version 24H2, verify compatibility with your essential applications.
- Stay informed about software updates from your applications that address compatibility with Windows 11 24H2.
- If this article does not address your issue, contact your IT support team or the respective software vendor for further assistance.

## Troubleshooting

In Windows, the OS version can be found in Windows settings, **System > About**. It can also be found in the CLI by running *system info*.

After upgrading to Windows 11 version 24H2, you may encounter the following issues:

### Cato Client Installation Failure

**Challenge**

The Cato Client installer fails, displaying error code **1603** with the message: *“Cato Client setup wizard ended prematurely because of an error.”*

**Root Cause**

Conflicts with local security software often trigger the failure.

**Solution**

- Check whether security software is running on the PC. For example, Cortex XDR.
- Temporarily disable the software or disable its underlying protection features.
- Attempt to reinstall the Cato Client.

### Citrix Workspace Fails to Start

**Challenge**

Citrix Workspace fails to launch, displaying the error: *“Unable to start.”*

**Root Cause**

The Windows upgrade enables **Adaptive Transport**, causing Citrix Workspace to use UDP/443 for server communication, which conflicts with certain configurations.

**Solution**

- Disable the Adaptive Transport feature, as explained in this [Citrix article](https://support.citrix.com/s/article/CTX220732-how-to-configure-hdx-enlightened-data-transport-protocol?language=en_US).
- Relaunch the application to ensure the changes take effect.

### Cato Client Uses Windows Location Services

**Challenge**

When opening Cato Client, Windows shows the following warning message: "Location has been turned off".

**Root Cause**

Cato Client uses **Windows location services** to identify various network items, such as the WiFi network name. Windows 11 24H2 now warns you when location services are disabled globally or for the application.

**Solution**

- To prevent the warning message, you may enable location services using [these instructions](https://support.microsoft.com/en-us/windows/windows-location-service-and-privacy-3a8eee0a-5b0b-dc07-eede-2a5ca1c49088).
