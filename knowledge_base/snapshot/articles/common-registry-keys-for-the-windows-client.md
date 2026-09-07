---
title: "Common Registry Keys for the Windows Client"
slug: "common-registry-keys-for-the-windows-client"
updated: 2026-06-22T09:24:17Z
published: 2026-06-22T09:24:17Z
canonical: "knowledge.catonetworks.com/common-registry-keys-for-the-windows-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Common Registry Keys for the Windows Client

This article summarizes Windows registry keys and registry paths that are commonly used for deploying, managing, and troubleshooting the Cato Windows Client. It consolidates the registry locations, their purpose, and the related configuration or administrative action. The registry keys are used for remote access as well as User Awareness.

| Registry Path/Key | Type | Purpose/Context | Value or Action | Additional Resources |
| --- | --- | --- | --- | --- |
| `HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN\dns_port` | Value | Configure the Windows Client to use UDP 1337 instead of UDP 443 | `DWORD = 1337` | [Configure DNS Port](/v1/docs/configuring-a-different-udp-port-for-the-cato-client) |
| `HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN\server_port` | Value | Configure the Windows Client to use UDP 1337 instead of UDP 443 | `DWORD = 1337` | [Configure UDP Port](/v1/docs/configuring-a-different-udp-port-for-the-cato-client) |
| `HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN\SubdomainForSeamlessAuth` | Value | Define the Cato SSO subdomain for seamless authentication with Windows credentials | `String = &lt;your account name&gt;` | [Subdomain for Seamless Authentication](/v1/docs/authenticate-users-automatically-with-windows-credentials) |
| `HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN\LaunchAuthPageOnStartup` | Value | Automatically launch the Client after initial installation for the next Windows user who logs in | `DWORD = 1` | [Automatically Launch the Client](/v1/docs/authenticate-users-automatically-with-windows-credentials) |
| `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\` | Registry path | Find the installed Windows Client uninstall entry | Search for `Cato Client` under this path | [Uninstall Client using MsiExec](/v1/docs/how-to-uninstall-the-windows-client-using-msiexec-exe) |
| `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\&lt;Cato Client key&gt;\UninstallString` | Value | Retrieve the uninstall command for the Windows Client | Copy the `UninstallString` value data | [Uninstall Client using MsiExec](/v1/docs/how-to-uninstall-the-windows-client-using-msiexec-exe) |
| `HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN\SeamlessAuthAllowUI` | Value | Permits the use of additional manual authentication methods such as MFA | `DWORD = 1` | [Authenticate Users Automatically with Windows Credentials](/v1/docs/authenticate-users-automatically-with-windows-credentials) |
| `HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN\ConnectOnBoot` | Value | Configure Cato Client to connect every time the device boots | `DWORD = 1` | [Connect On Boot](/v1/docs/authenticate-users-automatically-with-windows-credentials) |
| `HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN\InitialAlwaysOn` | Value | Force Always-On to be enabled on new client installations | `DWORD = 1` | [Initial Always On](/v1/docs/protecting-users-with-always-on-security) |
| `HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN\PreLogin` | Value | Enable Pre-login for a specific device | `DWORD = 1` | [Enable Pre-Login](/v1/docs/using-windows-pre-login-and-the-sdp-client) |
| `HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN\GREMode` | Value | Enable the GRE tunnel for shared hosts | `DWORD = 1` | [GRE Mode for Shared Hosts](/v1/docs/user-awareness-for-shared-hosts) |
| `HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN\LastUser\UpgradeMode` | Value | Indicates which upgrade mode is configured on the device | `DWORD = 0-2` | [Upgrade Mode](/v1/docs/sdp-client-silently-upgraded-even-though-policy-was-changed-to-managed-upgrade) |
