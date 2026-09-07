---
title: "Creating Device Posture Profiles and Device Checks"
slug: "creating-device-posture-profiles-and-device-checks"
updated: 2026-09-02T07:30:31Z
published: 2026-09-02T07:30:31Z
canonical: "knowledge.catonetworks.com/creating-device-posture-profiles-and-device-checks"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Device Posture Profiles and Device Checks

This article discusses how to create Device Posture Profiles and Device Checks to make sure that only devices that meet the security requirements are allowed to connect to the network.

## Overview

Device Posture Profile and Checks let you enforce compliance requirements for remote users before they are allowed to connect to the Network. You can use them in the Client Connectivity Policy and Internet and WAN firewall to define the specific device requirements.

For example, you can create a Device Check for a specific Anti-Malware vendor, product, and version. The Client checks that this software is installed on the device before connecting to the network. The Client only connects to the network if it identifies that this software is installed on the device. For more information on the Client Connection flow, see [Understanding the Cato Client Connection Flow](/v1/docs/understanding-the-cato-client-connection-flow).

Various Device Checks can be configured. See the [Supported Device Checks](/v1/docs/creating-device-posture-profiles-and-device-checks#supported-device-checks) section for a list of available Device Checks and the [Working with Specific Device Checks and Features](/v1/docs/creating-device-posture-profiles-and-device-checks#working-with-specific-device-checks-and-features) section for additional information on each check.

Device Checks can be added to Device Profiles that can contain multiple checks. Device Profiles can be added to the [Client Connectivity Policy](/v1/docs/configuring-the-client-connectivity-policy) to determine which devices are allowed to connect to the network.

Device Profiles can also be used in the Internet and WAN firewall to create rules that include conditional access based on the actual device of the end-user. For more about using Device Checks in a firewall policy, see [Adding Device Conditions to Firewall Rules](/v1/docs/adding-device-conditions-to-firewall-rules). You can monitor the number of devices that have complied with each Device Posture Profile on the [Remote Users Dashboard](/v1/docs/using-the-access-overview-page).

For more information about improving the effectiveness of Device Checks, see [Client Connectivity Policy - Improved Posture Checks](/v1/docs/client-connectivity-policy-continuous-posture-checks-check-policy).

**Best Practice:** We recommend that you enable the Advanced Posture setting so the Client continuously checks the device posture. For more information, see [Client Connectivity Policy - Improved Posture Checks](/v1/docs/client-connectivity-policy-continuous-posture-checks-check-policy).

### Device Checks Behind a Socket Site

Device Posture Profiles are applied to devices connecting to your network behind a Socket. This lets you apply the same Device Posture Profiles, regardless of the device's physical location. For example, a sales executive works two days in the office and three days remotely. The Device Posture Profile is applied to their device whenever and wherever they connect to Cato.

### Supported Device Checks

These are the minimum version Client requirements for Device Checks. See [Working with Specific Device Checks and Features](/v1/docs/creating-device-posture-profiles-and-device-checks#working-with-specific-device-checks-and-features) for details about each Device Check.

| Device Check | Windows | macOS | Linux | iOS | Android |
| --- | --- | --- | --- | --- | --- |
| Anti-Malware | 5.2 | 5.2 | 5.1 |  |  |
| Firewall | 5.4 | 5.2 | 5.1 |  |  |
| Disk Encryption | 5.5 | 5.6 |  |  |  |
| Patch Management | 5.5 | 5.2 | 5.2 |  |  |
| Device Certificate | 5.5 | 5.4 | 5.1 | 5.3 | 5.0.1.115 |
| DLP | 5.9 | 5.4.3 | 5.2 |  |  |
| Cato Client Version | 5.0 | 5.0 | 5.0 |  |  |
| Running Process | 5.11 | 5.7 |  |  |  |
| Registry Keys | 5.11 |  |  |  |  |
| Property List (plist) |  | 5.7 |  |  |  |
| OS Version | 6.8.2 |  |  |  | 5.6 |
| Device Checks applied for users in an office | 5.7 | 5.8 | 5.3 |  |  |

An empty box indicates the Device Check is not supported on the Operating System.

#### Known Limitations

- After creating a Device Check, the page needs to be refreshed so that the new check can be included in a Device Profile

## Preparing to Use Device Checks

Each Device Check can include these settings:

- One Device Test Type (for example, Anti-Malware or Firewall)
- A vendor, product, and version (for all checks apart from Running Process, Registry Key, and Property List)
  - You can choose any version, a specific version, or a minimum/maximum version (greater than or lower than)

**Note:** In a Firewall device check, if you select Apple's macOS built-in firewall, the version number refers to the macOS version number
  - For Anti-Malware, Firewall, Patch Management, and DLP Device Posture checks, you can create a general Check for any supported vendor or product. For example, you can create a Check to allow access to a device with any of the supported Anti-Malware solutions installed. For a list of supported vendors and products, see the drop-down lists in the **Vendor** section of the New Device Check panel.

## Configuring Device Checks

Device Checks define the criteria a device must meet to connect to the network. After creating a Check, add it to a Device Profile to enforce the posture requirements.

| ![device_checks.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30055124906141.png) |
| --- |

**To configure a Device Check:**

1. From the navigation menu, select **Resources > Device Posture**.
2. Select the **Device Checks** tab.
3. Click **New**. The **New Device Check** panel opens.

![DeviceChecksPanel](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28713003506461.png)
4. Configure the settings for the Device Check.
5. Click **Apply** and then click **Save**.

## Configuring the Device Profiles

After creating a Device Check, you can add it to a Device Profile to be included in rules in the Client Connectivity Policy or firewall policy to enforce the posture requirements.

![DeviceProfiles](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28713033321245.png)

**To configure a Device Profile:**

1. From the navigation menu, select **Resources > Device Posture**.
2. Click the **Device Posture Profiles** tab.
3. Click **New**.

The **New Device Profile** panel opens.
4. Configure the settings for the Device Profile, and add the required **Device Checks** (that you created in the previous section).
5. Click **Apply** and then click **Save**.

### Creating a Profile with Multiple Checks

When you create a Device Profile with multiple checks, they have an AND relationship. This means that a device must meet the requirements of all the Device Checks to apply the rule action to the device.

The following example shows the Sample Device Profile, which includes these checks:

- Patch Management - Sample Patch MGMT
- Disk Encryption - Sample Disk Encryption

![Device_Profile_FW_AM.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28713026736925.png)

## Working with Specific Device Checks and Features

Important information about specific Device Checks and features are outlined in the following sections.

### Working with Device Certificate Checks

You can create Device Checks for certificates installed on the end-user device defined for your account. The check verifies that a user certificate key pair is installed on the device and has been signed and issued by one of the certificate authorities associated with your account. For the posture check to detect the certificate, it must be installed in the Local Machine Personal Certificate Store as a combined key pair user certificate.

Only RSA certificates are valid for Device Posture.

### Working with Disk Encryption Checks

You can define one or more drive paths that are encrypted (the entire root path is encrypted, for example `C:\` or `Macintosh HD`). Only software-based encryption is supported (hardware-based encryption is not supported).

> [!NOTE]
> **Note:**
> 
> If the check doesn’t pass on a MacOS device, validate whether your users have permissions to modify the default volume name. If the volume name doesn’t match the defined path, the device posture check will not pass.

For devices with multiple partitions, you can specify which partition is encrypted. When you define multiple drive paths for a device, the Check validates that all paths are encrypted.

### Working with Cato Client Version Checks

You can create Device Checks for the Client version installed on the end-user device.

- To allow an exact Client version, use the **Equals** operator
- To allow a specific Client version, use the **Equals or higher** operator

### Working with the Running Process Checks

Running Process Checks are supported on Windows and macOS devices.

#### Running Process Checks on Windows Devices

You can create a Device Check to verify that a process is running on the device, optionally validating that it is signed by a specified certificate ID. To configure this Check, you can include either the process name or the process full path and, optionally, the Signer Certificate Thumbprint.

You can identify the Signer Certificate Thumbprint within the Properties of the process. For example, for the process `CatoClient.exe` the Signer Certificate Thumbprint is `81d821c152fa98db1c950b87d435122e5a0b451d`.

![Thmprint.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28713049728797.png)

**To identify the Signer Certificate Thumbprint:**

1. Right-click on the process and select **Properties**.
2. On the **Digital Signatures** tab, select the required certificate and click **Details**.

The **Digital Signature Details** window is displayed.
3. Click **View Certificate**.
4. On the **Details** tab, click on **Thumbprint**.

The Signer Certificate Thumbprint is displayed.

**Note:** The process name and process path are not case-sensitive.

#### Running Process Checks on macOS Devices

You can create a Device Check to verify that a process is running on the device, optionally validating that it is signed by a specified Team ID. To identify the Team ID, in the terminal run the command `codesign` followed by the full process path. The Team ID is returned. For example, for the process `/Applications/CatoClient.app/Contents/MacOS/CatoClient`, the Team ID is `CKGSB8CH43`:

![macosprocess.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28713003595677.png)

Process names can contain unicode characters and are case-sensitive.

#### Known Limitations of Process Checks on macOS Devices

- Checking for Applications is not supported, the full process path must be included in the configuration

### Working with the Registry Key Checks

To create a check for a Registry Key you need to specify the:

- Full Registry Key Path
- Value Name (you can choose to check for the default value or a specific value)
- Value Data (you can choose to check for any value or a specific value)

> [!NOTE]
> Note:
> 
> Non-ASCII characters for registry keys or value names are not supported.

All data types are supported. In a Multi-string Registry Key, separate the lines with a vertical bar symbol (`|` ). The format of the data in a Binary Value or Binary Value type is the HEX representation of the first 16 bytes, for example `0102030405060708090A0B0C0D0E0F10`.

To identify the Value Name and Value Data, in the Registry Editor, double-click on the Registry Key you are checking for. In the example below the Key Value Name is `start_minimized` and the Key Value Data is `0`.

![Reg_Key.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28713049773341.png)

### Working with the Property List Checks

To create a check for a Property List file (plist) you need to specify the full file path of the plist to check for. You can configure the Check to verify that:

- A specific key exists in the plist by selecting **Any Value**
- A specific key and value exist in the plist by selecting **Specific**.

To identify the key name and value within a plist, open the file with a text editor. In the example below, the key name is `Label` and the value is `com.catonetworks.mac.CatoClient.helper`.

![plist.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28713026809245.png)

#### Supported Property List Data Types

These plist data types are supported:

- Strings
- Integers
- These nested data types:
  - String
  - Integers

#### Known Limitations of Property List Check

- The path name can only contain UTF-8 characters
- plist files located in user folders are not supported

### Working with Real-Time Protection

In the **Criteria** section, you can also choose to enable **Real time protection**, and a connected device is continuously verified that it matches the Device Check.

### Working with OS Version Checks

You can define a minimum OS version, with the option to specify a minor version, and patch number.

Select **Pass device check for unrecognized OS** version to allow devices to pass the check when their OS version cannot be identified (fail open).

This check includes an OR operator. This lets you create one check for multiple OS versions.

When creating a check for Windows:

- Windows 10 and Windows 11 are considered separate products
- If you create a rule with a higher than operator, the rule applies to the minor version and patch number of that product. For example, if you create a rule to apply to versions of Windows 10 higher than 21H2, the rule does not apply to Windows 11.

### Working with Unsupported Cato Clients

Sometimes you need to accommodate Clients in your organization that currently don't support Device Posture, and allow these Clients the access the network. When you configure a Device Check, the **Criteria** section lets you choose the behavior for Clients that don't support Device Posture.

When an unsupported Client matches the settings for a rule except for the profile, these are the behavior options:

- Skip the Device Check, and allow unsupported Clients to connect to the network
- Block unsupported Clients because they can't meet the requirements of the Device Check

We recommend that you minimize the scope and impact of Device Checks that allow unsupported Clients in your organization. The fewer unsupported Clients that are allowed, the stronger the Client Connectivity Policy is.

### Supported OPSWAT Versions per Client

The Cato Client uses the following versions of OPSWAT:

**Windows Clients**

- Windows Client v6.12.6 uses OPSWAT v4.3.6344
- Windows Client v6.12 uses OPSWAT v4.3.6344
- Windows Client v6.8.3 uses OPSWAT v4.3.5908
- Windows Client v6.4 uses OPSWAT v4.3.5908
- Windows Client v6.2 uses OPSWAT v4.3.5495
- Windows Client v6.0 uses OPSWAT v4.3.5495
- Windows Client v5.17 uses OPSWAT v4.3.4761
- Windows Client v5.16 uses OPSWAT v4.3.4582
- Windows Client v5.15 uses OPSWAT v4.3.4548
- Windows Client v5.14.5 uses OPSWAT v4.3.4373
- Windows Client v5.14 uses OPSWAT v4.3.4487
- Windows Client v5.13 uses OPSWAT v4.3.4373
- Windows Client v5.12 uses OPSWAT v4.3.4195
- Windows Client v5.11 uses OPSWAT v4.3.3896

**macOS Clients**

- macOS Client v6.0.1 uses OPSWAT v4.3.5584
- macOS Client v5.12 uses OPSWAT v4.3.4973
- macOS Client v5.11 uses OPSWAT v4.3.4702
- macOS Client v5.10 uses OPSWAT v4.3.4222
- macOS Client v5.9 uses OPSWAT v4.3.4025
- macOS Client v5.8.5 uses OPSWAT v4.3.3952
- macOS Client v5.8.0 uses OPSWAT v4.3.3952
- macOS Client v5.7 uses OPSWAT v4.3.3479
- macOS Client v5.6 uses OPSWAT v4.3.3479

**Linux Clients**

- Linux Client v5.6 uses OPSWAT v4.3.4572
- Linux Client v5.5 uses OPSWAT v4.3.3700
- Linux Client v5.4 uses OPSWAT v4.3.3558
- Linux Client v5.3 uses OPSWAT v4.3.3509
- Linux Client v5.2 uses OPSWAT v4.3.2690
- Linux Client v5.1 uses OPSWAT v4.3.2690
