---
title: "Configuring the Client Connectivity Policy"
slug: "configuring-the-client-connectivity-policy"
updated: 2026-08-17T06:25:01Z
published: 2026-08-17T06:25:01Z
canonical: "knowledge.catonetworks.com/configuring-the-client-connectivity-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring the Client Connectivity Policy

This article discusses how to configure rules for the Client Connectivity Policy as part of implementing and enforcing Zero Trust Network Access (ZTNA) in your Cato account.

For more information, see [What is the Client Connectivity Policy?](/v1/docs/what-is-the-client-connectivity-policy).

## Overview

Use the Client Connectivity Policy to apply the requirements of your ZTNA policy that the Cato Client performs on devices for users, such as: Device Postures and Checks, confidence level, device OS, and more. If the device fails to comply with the policy that was set for the profile, then the user can't connect to the Cato Cloud.

For example, you can only allow remote users to access internal resources when they are compliant with the Device Posture policies. This can improve your confidence in the devices that are connected to your internal resources.

You can also use the Client Connectivity Policy to provide users with secured remote Internet access after one time authentication. For more information, see [Remote Internet Security with One Time Authentication](/v1/docs/remote-internet-security-with-one-time-authentication).

### Understanding Actions

The **Action** defines the level of access provided to the user. The Actions are:

- **Allow WAN and Internet:** The user has secured Internet access and can access the private network (WAN) **Note:** This option provides permission for a user to access the private network (WAN). A user's access to the private network (WAN) is dependent on rules in the [WAN Firewall](/v1/docs/managing-the-wan-firewall-policy).
- **Allow Internet only:** The user only has secured Internet access and cannot access the private network (WAN)

This Action also includes the option to **Terminate active WAN sessions**. This option applies when a remote user was previously allowed WAN access under one rule, but their circumstances change, and they now match only a rule that allows Internet access. In this case, you can choose whether to terminate the remote user’s existing WAN sessions.

For example, a remote user is granted WAN access based on their confidence level. If that condition later changes, such as when the token expires, the remote user is no longer allowed to access the WAN. This setting determines whether their current WAN sessions are disconnected. This option does not apply in Office Mode. **Note:** This option provides permission for a user to access the Internet. A user's access to the Internet is dependent on rules in the [Internet Firewall](/v1/docs/managing-the-internet-firewall-policy).
- **Block WAN and Internet:** The user is blocked from accessing the Internet and WAN

Existing WAN sessions are always terminated once a user meets a rule with this action.

### Prerequisites

Device Checks are supported for Windows and macOS Clients. For more information about the requirements for each check, see [Creating Device Posture Profiles and Device Checks](/v1/docs/creating-device-posture-profiles-and-device-checks).

## Preparing to Implement Client Connectivity Policy

The goal of the policy is to only trust devices that match the policy. Therefore, define rules that block all non-trusted devices so they are NOT allowed to connect to the network.

Before you enable the Client Connectivity Policy, make sure that you decide what the behavior is for users with unsupported Clients and operating systems. Do you want to allow these users to connect to your account? For example, users with Linux Clients or Windows Client v4.7 and earlier.

### Supported Connectivity Policy Features

- Configuring checks for a variety of Anti-Malware and endpoint Firewall vendors, to make sure that the relevant software is installed and running to allow remote access with the Client.
- We recommend that you do not enable Always-On connectivity with Real-Time Checks, because if a device fails to meet the policy requirements, the Client may abruptly disconnect from the network. This can provide a bad user experience for the user.

You can review the list of supported vendors and versions for Real-Time Checks [here](/v1/docs/creating-device-posture-profiles-and-device-checks).
- The Connectivity Policy is an ordered policy, therefore, you can add users to multiple profiles or rules. However, the first matching rule is applied to the user.

### Client Connectivity Policy and Always-On Policy in the Office

This section discusses using the Client Connectivity Policy when you are enforcing the Always-On policy behind a site and require users to authenticate even when they are in the office.

When the Clients are in [Office Mode](https://knowledge.catonetworks.com/docs/configuring-office-mode), the Client uses the site tunnel to send traffic to the Cato Cloud instead of establishing a client data tunnel and sending traffic tunnel-in-tunnel. In this mode, the Client establishes only a control tunnel to the Cato Cloud, while all data traffic is routed through the site's existing tunnel.

The Always-On **Require authentication in office** setting controls whether the Client must authenticate while operating in Office Mode. This setting applies only to Windows Clients. Clients running other operating systems always require authentication in the office, regardless of this setting.

- Remember that the Client Connectivity Policy will need to allow these users to connect to either the WAN or Internet, even when the device is located in the office behind a site
- If the Client enters the mode to bypass Always-On, the WAN and Internet Firewall policy for the site is applied to the user. This policy may be different than what is enforced when the user connects remotely
- Because this authentication applies only to the **control tunnel**, if authentication fails or the authentication token expires, only **Block All** rules in the Client Connectivity Policy are enforced.
  - Rules that block WAN access while allowing Internet access are not enforced in Office Mode.
  - As a result, data traffic is affected only if the Client Connectivity Policy drops the control tunnel entirely by matching a **Block All** rule.

For more information, see [Protecting Users with Always-On Security](/v1/docs/protecting-users-with-always-on-security).

## Configuring the Client Connectivity Policy and Settings

This section explains how to create the Client Connectivity Policy and add one or more profiles to each rule.

### Creating the Client Connectivity Policy

The Client Connectivity Policy is an ordered rulebase, and each rule has a scope of users that the rule applies to, including: geo-location (Countries) and device OS. When users or groups match the rule, the Cato Cloud manages the connections as follows:

- When they meet the Device Profile requirements for a rule, they are allowed to connect to your account.
- When they don't meet the Device Profile requirements for a rule, the Cato Cloud continues to inspect the posture according to the lower priority rules in the policy.
- The device for any user or group that doesn't match any rule is blocked by the final implicit rule of the policy (ANY ANY block).

**To create the rules for the Client Connectivity policy:**

1. From the navigation menu, click **Access > Client Connectivity Policy**.
2. Click **New**.

The **New Rule** panel opens.
3. Configure the scope of the rule:
  1. Define the **Users/Groups**, **Confidence Level**, **Platforms**, **Public ISP IP Range**, **Connection Origin** and **Countries** for this rule.
4. Expand the **Device Posture Profiles** section, and select the profiles for this rule.

If multiple Profiles are included in a single Policy rule, there is an implicit OR between them.

**Note**: Selecting **Any** Device Posture Profile means no Device Posture Profiles are included in the rule.
5. Select the **Action** for the rule. For more information on available actions, see [Remote Internet Security with One-Time Authentication](/v1/docs/remote-internet-security-with-one-time-authentication).
6. Click **Apply**.
7. Repeat steps 2-5 for each rule in the Client Connectivity policy.
8. Enable the **Client Connectivity Policy** and then click **Save**.

The slider is green when the rule is enabled, and gray when the rule is disabled.

### Sample Client Connectivity Policy

This section shows an example of a Client Connectivity Policy and how the rules are applied.

![ClientConnectivity Policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29832100230429.png)

1. The scope of rule 1 is the RnD groups for Africa and Europe with Windows devices.
  - When these users try to connect to the Cato Cloud, they are only allowed to connect if they meet the requirements of the **RnD Africa profile** or the **RnD Europe profile**.

Otherwise, the engine checks the user and device for rule 2.
2. The scope of rule 2 is the RnD groups for Africa and Europe with Windows devices that did NOT meet the Device Posture Profile requirements in rule 1.
  - When these users try to connect to the Cato Cloud, they match the Device Posture Profile **Any**, and are blocked. They can't connect to the Cato Cloud.
  - Rule 2 does not apply to users who are not members of the RnD groups for Africa and Europe, and these users continue with rule 3.
3. The scope of rule 3 is any user or user group with a Windows device.

When the users try to connect to the Cato Cloud, they are only allowed to connect to the Internet and not the WAN if they meet the requirements of the **Sample profile**.

Otherwise, the users are blocked by the final implicit ANY ANY Block rule.

## User Experience with Device Posture

When devices match the Device Checks, they can connect to the Cato Cloud, and the experience for the user is that the Client shows that it is **Connected**. This is the same user experience as when there is no Device Posture policy for the account.

When a device fails to match a Device Check, the Client does not connect to the Cato Cloud, and the Client shows an error message to the user. If a device fails a [periodic check](/v1/docs/creating-device-posture-profiles-and-device-checks) after the Client is connected, the Client disconnects, and the same error message is displayed.

This is an example of the error message:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/DevicePosture_ClientError.png)

Click **Details** to show the specific requirements that the device doesn't meet. An event is also generated that shows the same details.

### User Experience with Unsupported Client Versions

When you create a Client Connectivity policy for an OS, we strongly recommend that you make sure that all the Clients installed on all devices are upgraded to the [minimum supported Client version](/v1/docs/preparing-to-install-the-cato-client). For rules that don't allow access for earlier (unsupported) Client versions, this is the end-user experience:

- Windows OS - no message is shown to the user, and the Client continuously tries to connect to the encrypted tunnel
- macOS, iOS, Android, and Linux - users are shown a message that says this device is blocked from the network (for example, connecting from this OS is forbidden)

## Understanding Events for the Client Connectivity Policy

The CMA generates two types of events related to the Client Connectivity Policy:

- Whenever users or user groups comply with the requirements of a Client Connectivity Policy rule and are allowed to connect to the network.
- Whenever users or user groups are blocked from connecting to the network because they fail to meet the requirements of the Client Connectivity Policy.

The following table explains some of the event fields from an **Allow** action event:

| Field | Explanation |
| --- | --- |
| Device Posture Profile | The name of the Device Posture Profile that the device complies with. |
| Rule | The name of the Client Connectivity Policy rule that allowed the device to connect. |
| Authentication Method | The authentication method used by the user to authenticate to the Client. |

The following table explains the different Connectivity events with the **Block** action and the reason that the connection was blocked.

| Event Sub-Type | Reason for Blocking | Description of Event Message |
| --- | --- | --- |
| Client Connectivity Policy | Device fails to meet the Device Check | Shows the details of the Anti-Malware or Firewall installed on the device, and what is required for the Device Check. |
| Client Connectivity Policy | Unsupported Client | The device is connecting using a Client OS or version that is not supported, and the matching rule doesn't allow an unsupported Client to connect. |
| Client Connectivity Policy | Device fails to match any rule | The device did not match the scope of any rule in the Client Connectivity Policy. So, the connection was blocked by the final implicit rule. |
