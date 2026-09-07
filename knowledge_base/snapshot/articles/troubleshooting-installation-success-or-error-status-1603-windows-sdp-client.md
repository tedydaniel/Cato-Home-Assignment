---
title: "Troubleshooting the \"Installation success or error status: 1603\" When Installing the Windows SDP Client"
slug: "troubleshooting-installation-success-or-error-status-1603-windows-sdp-client"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/troubleshooting-installation-success-or-error-status-1603-windows-sdp-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting the "Installation success or error status: 1603" When Installing the Windows SDP Client

## Issue

The Windows Cato Client installation fails and shows the following screen:

![](https://support.catonetworks.com/attachments/token/GhlIlBbplHxa5coJcbFMXV5ST/?name=image.png)

## Solution

1. Open the Windows Installer log and check for the error code.
2. If the error code displayed is "1603", this indicates that there was a general Windows installer issue that could be related to permissions.
3. If you are using MSIEXEC for the client installation, do not use the "/j" option. The "/j" option will change the installer to an advertised package. For details on the option, refer to [Microsoft MSIEXEC Options](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/msiexec). Refer to [Upgrading-Cato-Windows-Client](https://support.catonetworks.com/hc/en-us/articles/360006643118-Upgrading-Cato-Windows-Client) for instructions on how to install/upgrade a client using MSIEXEC.
4. Further information regarding the 1603 error code is available in [this article](https://docs.microsoft.com/en-us/troubleshoot/windows-server/application-management/msi-installation-error-1603) provided directly by Microsoft.

If you are experiencing any additional error codes when installing the Cato Client, please contact Cato Support for further assistance.
