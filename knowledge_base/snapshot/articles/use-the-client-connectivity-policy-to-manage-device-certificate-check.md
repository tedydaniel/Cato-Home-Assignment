---
title: "Use the Client Connectivity Policy to Manage Device Certificate Check and Block Operating Systems"
slug: "use-the-client-connectivity-policy-to-manage-device-certificate-check"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/use-the-client-connectivity-policy-to-manage-device-certificate-check"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Use the Client Connectivity Policy to Manage Device Certificate Check and Block Operating Systems

This article answers FAQ on how to transition to the Client Connectivity Policy.

## Overview

The [Client Connectivity Policy](/v1/docs/configuring-the-client-connectivity-policy) lets you centrally manage rules that define posture requirements for any device connecting to your network with the Cato Client. This includes checking the operating system running on the device, checking for an approved Device Certificate, and many additional checks.

Due to the enhanced functionality and protection of the Client Connectivity Policy, Cato requires you to create rules in the Client Connectivity Policy to meet your device posture requirements and no longer use the Device Authentication page.

Device certificates can still be managed from the Access > Client Access page. For more information, see [Controlling Certified Corporate Devices.](/v1/docs/legacy-device-authentication)

The Device Certificate check has minimum Client version requirements. For more information, see [Creating Device Posture Profiles and Device Checks](/v1/docs/creating-device-posture-profiles-and-device-checks).

## Frequently Asked Questions

### How do I Manage Device Posture Requirements with the Client Connectivity Policy?

For more information on how to manage your Client Connectivity Policy, see [Configuring the Client Connectivity Policy](/v1/docs/configuring-the-client-connectivity-policy). Example configurations are outlined below.

#### Example 1: Blocking Devices Without Certificates

If you configured Device Authentication to require Windows devices to have a matching device certificate:

1. Create a [Device Check](/v1/docs/creating-device-posture-profiles-and-device-checks) for a Device Certificate on Windows devices
2. Create a Device Posture Profile that includes the Device Certificate Device Check
3. Create a Client Connectivity Policy rule to allow access for Windows devices that are compliant with the Device Posture Profile
4. Update the priority of the new rule to meet your requirements.

After creating the rule above, only Windows devices with the required certificate can access the network.

#### Example 2: Blocking User(s) on Specific Operating Systems

If you configured Device Authentication block a specific user on a macOS device:

1. Create a Client Connectivity Policy rule to block macOS devices and add the specific user(s)
2. Update the priority of the new rule to meet your requirements.

### What are the Changes to My Account?

After June 1st, 2024, the Device Authentication page will still be available in the Cato Management Application. It will continue to be available until you complete the transition and there will be no change in behavior for your users or account.

### What Happens if I Don't Create Client Connectivity Rules?

There will be no change in behavior for your users, but you must start managing your Device Posture requirements with the Client Connectivity Policy as soon as possible. If you need more assistance or need more time to make this change, please contact your account representative.

### Who do I Talk to If I have Questions?

If you require additional assistance or help to make this change, please contact your Cato account representative or [Support](https://support.catonetworks.com/hc/en-us/requests/new).
