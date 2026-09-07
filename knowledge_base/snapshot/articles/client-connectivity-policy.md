---
title: "What is the Client Connectivity Policy?"
slug: "what-is-the-client-connectivity-policy"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/what-is-the-client-connectivity-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is the Client Connectivity Policy?

This article explains how you can use the Client Connectivity Policy to ensure devices can only connect to your network when they comply with the organizational security requirements.

## Overview

Part of implementing your Zero Trust Network Access (ZTNA) corporate security policy and reducing the attack surface, is to check the posture of devices before they connect to the network. The Client Connectivity Policy lets you create the rules that define the requirements on the device. After a SDP user successfully authenticates, the Cato Client runs checks to verify the relevant conditions on the device. For example, the Client verifies that the anti-malware software is up-to-date, otherwise it doesn't connect to your network.

The Client can identify device conditions, for example:

- **Device Posture Profile:** This verifies the security posture of the device for the supported Device Checks, see below [Defining Device Posture Requirements](/v1/docs/what-is-the-client-connectivity-policy#defining-device-posture-requirements).
- **Platform:** This identifies the operating system of the device. For example, you can require that only Windows devices are allowed to connect.
- **Countries:** This identifies the physical location of the device. For example, define a list of countries that the Client doesn't connect to the network if the device is located in that county (based on IP geo-location).
- **Confidence Level:** This describes how reliable the user's authentication is. For more information, see [Remote Internet Security with One Time Authentication](/v1/docs/remote-internet-security-with-one-time-authentication).

The Client Connectivity Policy also helps administrators maintain the correct access level when the user or device context changes during a session. If the Client no longer matches the requirements for full network access, the policy can limit the session to secured Internet access or block the connection, depending on the configured rule. This helps reduce exposure from devices that become non-compliant while keeping access available when the connection still meets the organization’s security requirements.

The Client Connectivity Policy controls access for remote users, for more information about controlling access for users behind a site, see ​[Adding Device Conditions to Firewall Rules](/v1/docs/adding-device-conditions-to-firewall-rules).

### Sample Use Case

Company ABC is based in the UK and has a mix of corporate employees and third party contractors. Corporate employees use Windows devices, but the third party contractors use their own devices. To protect the network, the company wants to ensure that only devices with the following conditions are able to connect:

- The device is located in the UK
- Devices used by corporate employees have the required device certificate
- Devices used by third party contractors have anti-malware software, disk encryption and patch management software installed on the device

To ensure devices connecting to its network comply with its security requirements, the company creates the following **Client Connectivity Policy** Allow rules:

![ClientConnectivity_UseCase.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218221042589.png)

- **Rule 1 - Corporate employees:** On a device used by a corporate employee, the Client checks that the device:
  - Is a Windows device
  - Has a valid authentication token
  - Has the required certificate installed
  - Is located in the UK
- **Rule 2 - Third party contractors:** On a device used by a third party contractor, the Client checks that the device:
  - Has Anti-Malware software, disk encryption and patch management software installed
  - Has a valid authentication token
  - Is located in the UK

The Client only connects to the network if it identifies that the device complies with appropriate conditions for the corporate employee or third party contractor.

## Controlling Device Access to your Network

The Client Connectivity Policy is an ordered rule base that sequentially checks if the device conditions match the required conditions for the SDP user. Once a device matches a rule, it can connect to your network. Rules that are listed after the matching rule are not applied to the device. If a device does not match any rule, it is blocked by the final implicit rule of the policy (ANY ANY block).

For more information about defining rules for in the Client Connectivity Policy, see [Configuring the Client Connectivity Policy](/v1/docs/configuring-the-client-connectivity-policy).

### Defining Device Posture Requirements

To enforce compliance requirements for SDP users, first decide the device posture requirements for user segments in your organization. You can then use the Client Connectivity Policy to implement these requirements.

Each Client Connectivity Policy rule can contain a **Device Posture Profile**. This lets you define detailed device posture requirements (**Device Checks**) for devices in your organization. When you include multiple checks in a single profile, they have an AND relationship. For example, you can create a **Device Posture Profile** that contains Anti-Malware, Firewall and Disk Encryption checks.

You can create different checks per operating system and check for the presence of specific vendors and versions installed on a device. This lets the Client perform granular checks of devices to validate the posture.

Device Checks are supported for Windows and macOS Clients. For more information about the requirements for each check, see [Creating Device Posture Profiles and Device Checks](/v1/docs/creating-device-posture-profiles-and-device-checks).

### Defining Additional Compliance Requirements

You can prevent the Client connecting to your network based on the device's operating system and/or the location of the device. Each **Client Connectivity Policy** rule contains options to include **Platforms** and **Countries**. If the Client identifies the device is running a non-compliant operating system or located in a non-compliant location it does not connect to your network.
