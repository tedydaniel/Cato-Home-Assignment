---
title: "SDP client fails to connect due to netsh crashes with Windows 11"
slug: "sdp-client-fails-to-connect-due-to-netsh-crashes-with-windows-11"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/sdp-client-fails-to-connect-due-to-netsh-crashes-with-windows-11"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SDP client fails to connect due to netsh crashes with Windows 11

## Overview

[netsh.exe on Windows 11 will fail](https://answers.microsoft.com/en-us/windows/forum/all/netsh-failing-in-windows-11-version-10022621674/c421d0ea-4746-45f4-a1d2-69f51bc7e164) to run and crash if Windows Update **KB2693643** (Remote Server Administration Tools for Windows 10) is installed.

Since the Windows SDP client requires netsh.exe to operate, this causes the SDP client to get stuck in the Connecting or Authenticating states.

## Troubleshooting

1. In the Event Viewer > Windows Logs > Application, search for netsh.exe crashes with Event ID 1000 or 1001. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10755940027293.png)
2. Verify that Windows Update KB2693643 (Remote Server Administration Tools for Windows 10) is installed under **Settings > Update & Security > Windows Update > Update History**.

You can also check for the update using the PowerShell command

`Get-Hotfix | findstr /i "2693643"`

If the update does exist, the output will be shown similarly in the example below.

`PS C:\Users\UserX&gt; Get-Hotfix | findstr /i "2693643"` `Example-PC&nbsp; Update&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; KB2693643&nbsp; &nbsp; Example-CATO-PC\cato&nbsp;&nbsp;&nbsp; 1/9/2023 12:00:00 AM`

If the update doesn't exist, the command will return nothing.

## Solution

The solution would be to uninstall Windows Update KB2693643. This update causes netsh.exe, which the Windows SDP client requires to update network configuration during the connection, to crash on Windows 11.

You can uninstall the update from **Settings > Update & Security > Windows Update > Update History > Uninstall Updates** or by running the following Powershell command: `wusa /uninstall /kb:2693643`

## Additional Notes

- Starting with **Windows SDP Client version 5.15**, the client no longer depends solely on `netsh.exe`. Instead, it first attempts to use Windows APIs to update network configurations, reducing the risk of encountering this issue.
- If you need to install **Remote Server Administration Tools (RSAT)** after removing this update, refer to the official Microsoft documentation: [Install RSAT on Windows 11](https://learn.microsoft.com/en-us/troubleshoot/windows-server/system-management-components/remote-server-administration-tools)
