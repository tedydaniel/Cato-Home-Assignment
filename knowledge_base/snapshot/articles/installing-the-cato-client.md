---
title: "Installing the Cato Client"
slug: "installing-the-cato-client"
updated: 2026-07-26T14:01:12Z
published: 2026-07-26T14:01:12Z
canonical: "knowledge.catonetworks.com/installing-the-cato-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Installing the Cato Client

This article provides information about installing the Cato Client on the various supported operating systems.

## Installing the Cato Client

The Client can be installed on any supported device. For troubleshooting information, see [Troubleshooting Scenarios for Issues with the Cato Client](/v1/docs/troubleshooting-scenarios-for-issues-with-the-cato-client).

### Installing the Windows Client

The Windows Client can be downloaded from the and installed on individual devices by following the installation wizard. You can also download the Client from the [Client Rollout page](/v1/docs/managing-the-rollout-of-client-versions-client-upgrade-policy) and distribute the Client with an MDM. For more information, see [Downloading the Cato Client](/v1/docs/downloading-the-cato-client).

> [!NOTE]
> Note:
> 
> The Cato Client uses Windows location services to identify various items on the network, for example, the WiFi network name. If you do not want to provide Cato with this information, change the settings for the location services using [these](https://support.microsoft.com/en-us/windows/windows-location-service-and-privacy-3a8eee0a-5b0b-dc07-eede-2a5ca1c49088) instructions.

Use one of the following options to install the Windows Client:

- Run the EXE from the File Explorer
- Run the EXE file using the command line: ***<setup_file.exe>***
  - In Windows Client versions below 5.5, for silent installation use the command line: ***<setup_file.exe> /s /x /v"/qn****"*
  - In Windows Client version 5.5 and above, for silent installation, use the command line: **<setup_file.exe> /s**
- Run the MSI file using the command line: ***msiexec /i <setup_file.msi****>*

**Note**: /j is not supported
  - The MSI installation requires MS .NET framework version 4.6.2 or higher installed
  - Run the MSI command line as an administrator

In the installation wizard, there is the option to create a desktop shortcut for the Client. You can prevent users selecting this option with the command line:

**msiexec /i <setup_file.msi>CATO_FORCE_DISABLE_DESKTOP_SHORTCUT=1 /qn**

For more information, see [Common Registry Keys for the Windows Client](/v1/docs/common-registry-keys-for-the-windows-client).

#### Automatically Launching Windows Client after Initial Installation (Client v5.6 and Higher)

To make it easier for users to authenticate to their new device, you can define the Windows registry key to enable the Client to automatically open after the initial installation. Afterwards, the Client behaves according to the settings for your account.

After the registry is changed, the Client automatically opens for the next Windows user that logs in to the device.

**To configure the Windows registry to automatically launch the Client:**

1. Go to this location in the registry: **HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN**
2. Define this value:
  - LaunchAuthPageOnStartup=1 (DWORD)

For a full list of installation parameters, see [Deploy Cato Client with Intune (Windows)](/v1/docs/deploy-cato-client-with-intune-windows).

### Installing the macOS Client

The macOS Client can be downloaded from the and installed on individual devices by following the installation wizard. You can also download the Client from the [Client Rollout page](/v1/docs/managing-the-rollout-of-client-versions-client-upgrade-policy) and distribute the Client with an MDM. For more information, see [Downloading the Cato Client](/v1/docs/downloading-the-cato-client).

To install the macOS Client, run the PKG file from Finder.

### Installing the Linux Client

For more information about installing the Linux Client, see [Installing and Running the Linux Client](/v1/docs/getting-started-with-the-linux-client)

### Installing the iOS and Android Clients

The iOS and Android Clients can be downloaded from the relevant app store and installed on individual devices or distributed with an MDM.
