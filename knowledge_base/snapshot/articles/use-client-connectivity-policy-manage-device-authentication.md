---
title: "Use the Client Connectivity Policy to Manage your Device Authentication Requirements"
slug: "use-client-connectivity-policy-manage-device-authentication"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/use-client-connectivity-policy-manage-device-authentication"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Use the Client Connectivity Policy to Manage your Device Authentication Requirements

The [Client Connectivity Policy](/v1/docs/what-is-the-client-connectivity-policy) lets you centrally manage rules that define device posture requirements for any device connecting to your network with the Cato Client. This includes checking the operating system running on the device, checking for an approved Device Certificate, and many additional checks.

Due to the enhanced functionality and protection of the Client Connectivity Policy, starting June 1st, 2024, Cato will automatically create rules in the Client Connectivity Policy that match your current [Device Authentication](/v1/docs/legacy-device-authentication) configurations.

Any operating systems that Device Authentication blocked from accessing the network will be blocked by an automatically created Client Connectivity Policy rule. This applies to both global account configurations and configurations for specific users.

For more information on how to manage your Client Connectivity Policy, see [Configuring the Client Connectivity Policy](/v1/docs/configuring-the-client-connectivity-policy).

## What are the Changes to My Account?

After November 30, 2024, the Device Authentication page will no longer be available in the Cato Management Application. All device posture requirements for your account should be managed using the enhanced Client Connectivity Policy. Cato will automatically update the Client Connectivity Policy to match your Device Authentication configurations. The new Client Connectivity Policy rule ensures that any operating systems blocked by Device Authentication cannot access the network. Device certificates can still be managed from the **Access > Client Access** page. For more information, see [Controlling Certified Corporate Devices.](/v1/docs/legacy-device-authentication)

## What is the Impact on the Account?

There is no impact on remote access in your account. Cato will automatically update your account and ensure your current device posture configurations remain the same.

## Who Do I Talk to If I Have Questions?

Please contact your Cato account representative or Support.
