---
title: "Adding Device Conditions to Firewall Rules"
slug: "adding-device-conditions-to-firewall-rules"
updated: 2026-06-22T09:26:42Z
published: 2026-06-22T09:26:42Z
canonical: "knowledge.catonetworks.com/adding-device-conditions-to-firewall-rules"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding Device Conditions to Firewall Rules

This article discusses how to add conditions for device criteria to the WAN and Internet firewall rulebases for enhanced security and protection.

## Overview

The **Device** setting for the WAN and Internet firewall rules gives you the ability to expand the scope of your firewall security policy to include conditional access based on attributes of the actual device of an end-user or other devices communicating on your network, such as IoT/OT. You can specify the access requirements for devices on the network. For example:

- WAN firewall -
  - Specify the source of the rule to only apply to devices that meet the pre-defined posture or based on geo-location
  - Allow access to a business-critical OT device only for specific users
- Internet firewall -
  - Define rules for a SaaS application that limit access based on the device settings and location
  - Block Internet access for IP cameras on the network

By default, the device settings do not impact traffic because they are set to Any Any and automatically match all traffic.

For more information about the Cato WAN and Internet firewall, see the Knowledge Base articles in [Cato Firewalls](/v1/docs/cato-firewalls).

### Prerequisites

- Before you can add a Device Profile to the **Device** settings for a rule, you must create and configure the [Device Profile](/v1/docs/creating-device-posture-profiles-and-device-checks)
- To see which Device Checks are supported for Client OS and version, see [Creating Device Posture Profiles and Device Checks](/v1/docs/creating-device-posture-profiles-and-device-checks)
- Rules that use Device Profiles are applied only when the Cato Client is installed on the device and used as an identity agent, both remotely and when located behind a Socket.

For more information, see [Using Cato Identity Agents for User Awareness (EA Authentication without a ZTNA License)](/v1/docs/using-cato-identity-agents-for-user-awareness).

**Note:** Licensed Clients automatically are used as identity agents.

## Configuring the Device Settings

These are the **Device** settings that you can add to a firewall rule:

- **Device Attributes** - Attributes of devices as identified by the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine
- **Platforms** - Device operating system (OS)
- **Countries** - Source country for the connection based on the physical location of the device (according to the IP address geo-location)
- **Device Posture Profiles** - Device Profiles (configured in Access > Device Posture)
- **Origin of the Connection** - The geolocation of the device. You can configure the rule based on whether the device is connecting behind a Side or remotely via the Client, Browser Extension, or Enterprise Browser (each remote connection option can be selected separately).
- **User Attributes**: The [Risk Level](/v1/docs/understanding-the-user-risk-level) and [Confidence Level](/v1/docs/remote-internet-security-with-one-time-authentication) of the user logged into the device.

When you configure multiple conditions for a rule, they have an AND relationship, the rule is matched only if traffic matches the criteria defined in all of the items.

Within a condition (a single cell), the items have an OR relationship. For example, a rule that has the **Platforms** condition of **Windows**, and **macOS**, matches all Windows or macOS devices.

This is an example of a rule where the traffic must meet all of these **Device** conditions: **Windows** devices, located in **India**, that meet the requirements of **Device Posture Profile 1**.

![FW_Device_Conditions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26957302299933.png)

### Adding Device Attribute Requirements

![Device_FW_Criteria.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26957320543389.png)

Use the **Device Attributes** condition to define rules for devices that were detected on the network by the Device Inventory engine. You can use the following attributes in a firewall rule: **Category**, **Type**, **Model**, **OS**, **Manufacturer**, **OS Version**.

Select a **Device Attributes Type**, then select the **values** from the dropdown list. The list is automatically populated with values of devices detected on the network. You can select multiple **Device Attribute Types** in a rule, and the attributes have an AND relationship between them. For example, if you select **OS** as **Windows** and **Manufacturer** as **Dell**, the condition applies only to Dell devices with a Windows operating system.

However, when you select multiple values within a **Device Attribute Type**, there is an OR relationship between them. For example, if you select **Manufacturer** with the values of **Dell** and **HP**, the condition will match for either Dell or HP devices.

A separate Device Inventory license is required for Device Inventory pages and features. For more about purchasing a license, please contact your Cato representative.

### Adding Platform Requirements

The **Platforms** condition for a firewall rule lets you define the device operating systems that match the rule. For example, for a specific network segment, only allow access to Windows, macOS, or Linux devices.

### Adding Country Requirements

The **Countries** condition lets you define the source of the traffic that matches the rule based on the IP geo-location of the device. For example, restrict access to a site for a branch office, so that only devices that are located in the same country as the office are allowed to connect.

### Adding Device Profile Requirements

The **Profiles** condition lets you restrict the rule to only match devices that meet the requirements of the Device Profile. This condition is based on the Device Posture feature, which checks if the device meets the posture requirements. For example, only devices that have the newest Anti-Malware software version meet the posture requirements.

The Device Profiles are currently not supported on all Client versions, for more information see [Creating Device Posture Profiles and Device Checks](/v1/docs/creating-device-posture-profiles-and-device-checks).

#### Working with Unsupported Cato Clients

The firewall can only determine if a Client matches the Device Check for supported Clients. For each Device Check, you can define the behavior for unsupported Clients that match the other requirements firewall rule (Source, App/Category, and so on):

- Skip the Device Check, and apply the firewall action to the unsupported Clients
- Apply the Device Check, and the Client doesn't match the firewall rule and the action isn't applied

The following table explains the behavior for unsupported Clients when the connection matches all the other settings of the firewall rule. The behavior depends on whether the **Skip this check for unsupported SDP Client version** option is enabled or cleared (disabled) in the Device Check.

| Unsupported Clients | Firewall Rule Action | Client Behavior |
| --- | --- | --- |
| Skip check (Enabled) | Block | Unsupported Clients automatically skip the Device Check and are blocked (they can't connect) |
| Allow | Unsupported Clients automatically skip the Device Check and are allowed (they can connect) |
| Apply Check (Disabled) | Block | Unsupported Clients fail to match the Device Check, the firewall skips this rule (doesn't apply the block action to the connection) |
| Allow | Unsupported Clients fail to match the Device Check, the firewall skips this rule (doesn't apply the allow action to the connection) |

### Adding Device Origin Requirements

The **Origin of the Connection** condition lets you define the geo-location of the device that matches the rule. For example, allow access to sensitive information behind a site, but not when working remotely.

### Adding User Attribute Requirements

The **User Attribute** condition lets you define criteria based on a user's risk score or confidence level. For example, allow access to SalesForce only when the user Confidence Level is High.

Using the Confidence Level attribute lets you enforce a requirement for a higher level of authentication (step-up authentication) when accessing sensitive resources. When blocking access, you can [apply a custom template](/v1/docs/creating-user-notification-templates) informing the user why they were blocked and they need to do to gain access.

### Configuring the Device Conditions in a Rule

You can configure the device criteria settings in a new or existing firewall rule.

**To configure the Device conditions for a firewall rule:**

1. From the **Security** section in the navigation pane, select **Internet Firewall** or **WAN Firewall**.
2. Click **New** to create a new rule, or click the Edit icon ![edit.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26957337543453.png) in the **Criteria** column for an existing rule.
3. In the **Criteria** section, configure the **Device Attributes**, **Platforms**, **Countries**, and **Profiles** that are required to match this rule.
4. Click **Apply**.

The Criteria conditions are configured for the rule.

### Sample Firewall Rules with Device Conditions

This is an example of a WAN firewall rule that allows traffic in both directions for all SDP users that match all of the following Device conditions: using a Windows OS device, physically located in South Korea, and matches the requirements of the **Test Policy** Device Profile.

![WAN_FW_Device_Rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26957670548125.png)

This is an example of an Internet firewall rule that is an exception to the rule that blocks the Social category. The exception allows traffic that matches the following Device conditions: using a Windows or macOS device and physically located in the United States.

![Int_FW_Device_Conditions.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26957320730653.png)

### Sample Firewall Rules with User Attributes

This is an example of an Internet firewall rule that blocks traffic to Salesforce for all users with a Confidence Level of Low.

![low-confidence-fw-rule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34309720924573.png)

When a user is blocked, they are presented with a [dedicated block page](/v1/docs/creating-user-notification-templates) informing them what they need to do to get access to SalesForce.

![low-confidence-client-notification.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34309696660765.png)

## Best Practices for Implementing Firewall Device Conditions

- Add Device Posture **Profiles** to rules with the allow action
- Define the Device Profile with the minimum requirements to allow devices to connect (devices that don't meet these requirements are blocked)
