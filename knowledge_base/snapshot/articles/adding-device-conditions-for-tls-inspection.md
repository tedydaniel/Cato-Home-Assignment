---
title: "Adding Device Conditions for TLS Inspection"
slug: "adding-device-conditions-for-tls-inspection"
updated: 2026-07-26T18:06:28Z
published: 2026-07-26T18:06:28Z
canonical: "knowledge.catonetworks.com/adding-device-conditions-for-tls-inspection"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding Device Conditions for TLS Inspection

This article discusses how to add conditions for devices to the TLS Inspection policy for granular inspection based on the actual status of the device.

## Overview of TLS Inspection Device Conditions

The **Device** setting for the TLS Inspection policy gives you the ability to expand the scope to inspect traffic based on the actual device of the SDP user. You can specify the requirements for devices that the TLS Inspection rules apply to. For example:

- Only inspect traffic for devices that based on geo-location
- Only allow devices to bypass TLS Inspection based on the specific OS

By default the **Device** settings do not impact the TLS Inspection policy, because they are set to Any Any and automatically match all traffic.

### Prerequisites

- Device Checks are supported for Windows and macOS Clients. For more information about the requirements for each check, see [Creating Device Posture Profiles and Device Checks](/v1/docs/creating-device-posture-profiles-and-device-checks).
- Before you can add a Device Profile to the **Device** settings for a rule:
  - You must create and configure the Device Profile
- Known limitation - Rules that use Device Profiles are only applied when the user is connected with the Cato Client (even if they are located behind a Socket)

## Configuring the Device Settings

These are the **Device** settings conditions that you can add to a TLS Inspection rule:

- Platforms - Device Operating System (OS)
- Countries - Source country for the connection based on the physical location of the device (according to the IP address geo-location)
- Profiles - Device Profiles (configured in Resources > Device Posture)
- Connection Origin - The geo-location of the device (Remote (Client, Browser Extension, or Cato Browser) or behind a site)

When you configure multiple conditions for a rule, they have an AND relationship, the rule is matched only if traffic matches the criteria defined in all of the items.

Within a condition (a single cell), the items have an OR relationship. For example, a rule that has the **Platforms** condition of **Windows**, and **macOS**, matches all Windows or macOS devices.

This is an example a rule where the traffic must meet all of these **Device** conditions: **Windows** devices, located in **India**, that meet the requirements of the **Sample Device Profile**.

![FW_Device_Conditions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303146818845.png)

### Adding Platform Requirements

The **Platforms** condition for a TLS Inspection rule lets you define the device OS that match the rule. For example, for a specific network segment, only allow inspect traffic for Windows, macOS, or Linux devices.

### Adding Country Requirements

The **Countries** condition lets you define the source of the traffic that matches the rule based on the IP geo-location of the device. For example, for a site that is a branch office, allow iOS and Android mobile devices to bypass TLS Inspection.

### Adding Device Profile Requirements

The **Profiles** condition lets you restrict the rule to only match devices that meet the requirements of the Device Profile. This condition is based on the Device Posture feature, which checks if the device meets the posture requirements.

> [!NOTE]
> Note:
> 
> For devices that are connected using Office Mode (or tunnel in tunnel), the TLS Inspection engine does not apply Device Posture profiles to the devices. This means that for an Inspect rule, devices using Office Mode aren't inspected, even if they do not meet the requirements of the Device Posture profile.

#### Using Device Profiles with Unsupported Cato Clients

The TLS Inspection engine can only determine if a Client matches the Device Profile for supported Clients. For each Device Check, you can define the behavior for unsupported Clients that match the other requirements in the rule:

- Skip the Device Check - apply the TLS Inspection action to the unsupported Clients
- Apply the Device Check - the action is only applied when the Client matches the rule

The following table explains the behavior for unsupported Clients when the connection matches all the other settings of the rule. The behavior depends on whether the **Skip this check for unsupported SDP Client version** option is enabled or cleared (disabled) in the Device Check.

| Unsupported Clients | TLS Inspection Rule Action | Client Behavior |
| --- | --- | --- |
| Skip check (Enabled) | Inspect | Unsupported Clients automatically skip the Device Check and the traffic is inspected |
| Bypass | Unsupported Clients automatically skip the Device Check and bypass TLS Inspection |
| Apply Check (Disabled) | Inspect | Unsupported Clients fail to match the Device Check, the TLS Inspection engine skips this rule (doesn't inspect the traffic) |
| Bypass | Unsupported Clients fail to match the Device Check, the TLS Inspection engine skips this rule (doesn't bypass inspection) |

### Adding Connection Origin Requirements

The **Connection Origin** condition lets you define the geo-location device that matches the rule. For example, allow access to sensitive information behind a site, but not when working remotely.

### Configuring the Device Conditions in a Rule

You can configure the **Device** settings in a new or existing TLS Inspection rule.

**To configure the Device conditions for a rule:**

1. From the navigation menu, click **Security > TLS Inspection**.
2. Click **New** to create a new rule, or click the Edit icon ![edit.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24303185606941.png) in the **Device** column for an existing rule.
3. In the **Device** section, configure the **Platforms**, **Countries**, **Device Posture Profiles** , and **Connection Origin** required to match this rule.
4. Click **Apply**.

The **Device** conditions are configured for the rule.
