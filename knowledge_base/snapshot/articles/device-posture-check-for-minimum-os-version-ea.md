---
title: "Device Posture Check for Minimum OS Version (EA)"
slug: "device-posture-check-for-minimum-os-version-ea"
updated: 2026-09-06T06:46:16Z
published: 2026-09-06T06:46:16Z
canonical: "knowledge.catonetworks.com/device-posture-check-for-minimum-os-version-ea"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Device Posture Check for Minimum OS Version (EA)

**Note:** This is an Early Availability (EA) feature that is only available for limited release. For more information, contact your Cato Networks representative or send an email to [ea@catonetworks.com](mailto:ea@catonetworks.com).

## Overview

Device Posture Profile and Checks let you enforce compliance requirements for remote users before they are allowed to connect to the Network. You can use them in the Client Connectivity Policy and Internet and WAN firewall to define the specific device requirements.

For more information, see [Creating Device Posture Profiles and Device Checks](/v1/docs/creating-device-posture-profiles-and-device-checks).

## Working with OS Version Checks

This check is supported on:

- Windows devices with Client version 6.8.2 or higher
- macOS devices with Client version 6.1 or higher
- iOS devices with Client version 5.9 or higher
- Android devices with Client v5.6 or higher

You can define a minimum OS version, with the option to specify a minor version.

Select Pass device check for unrecognized OS version to allow devices to pass the check when their OS version cannot be identified.

This check includes an OR operator. This lets you create one check for multiple OS versions.

When creating a check for Windows:

- Windows 10 and Windows 11 are considered separate products
- If you create a rule with a higher than operator, the rule applies to the minor version of that product. For example, if you create a rule to apply to versions of Windows 10 higher than 21H2, the rule does not apply to Windows 11.
