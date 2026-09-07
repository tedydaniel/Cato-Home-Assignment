---
title: "Configuring Intune MDM Compliance Checks for Device Posture"
slug: "configuring-intune-mdm-compliance-checks-for-device-posture"
updated: 2026-09-03T12:48:10Z
published: 2026-09-03T12:48:10Z
canonical: "knowledge.catonetworks.com/configuring-intune-mdm-compliance-checks-for-device-posture"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Intune MDM Compliance Checks for Device Posture

> [!NOTE]
> **Note:**
> 
> Please contact [feature-releases@catonetworks.com](mailto:feature-releases@catonetworks.com) for more information about enabling and using this feature.

Device Posture checks let you evaluate the security state of a device before allowing access to network resources or applications. You can use these checks in access policies to enforce conditional access based on attributes such as Client status, operating system, or security configuration.

With support for Microsoft Intune MDM compliance states, Cato expands its Device Posture capabilities. You can incorporate Intune compliance signals into your posture evaluation and enforce access based on your organization’s MDM policy. This lets you apply zero-trust principles to managed devices and ensure that only devices meeting your Intune compliance requirements can access protected resources.

## Prerequisites

- [Microsoft Intune integration](/v1/docs/microsoft-intune-configuring-the-device-management-integration) is configured in your account
- You have appropriate permissions in the Cato Management Application (CMA) to configure Device Posture

## Supported Operating Systems

Intune MDM compliance checks are supported for devices running these operating systems:

- Windows
- macOS
  - Not supported on macOS devices that are communicating with more than one NIC
- Linux

## Use Case

Your organization uses Microsoft Intune to manage corporate devices. As the admin, you want to apply policies in the CMA that ensure that only devices marked as compliant in Intune can access sensitive internal applications, such as finance or HR systems, connect remotely with the Cato Client, and more. You also want to block devices that are explicitly marked as non-compliant, or are in an unknown or misconfigured state.

In the Resources > Device Posture page, you configure a Device Posture Check for MDM Compliance with the following behavior:

- Compliant devices are allowed to access protected applications through ZTNA policies
- Devices in Conflict, Error, Grace Period, or Config Manager states are ignored, and access is not permitted unless other rules apply

This lets you enforce conditional access policies that are dynamically tied to the device’s compliance state in Intune, and ensures only trusted, compliant devices can connect to your resources.

## Creating a New Device Posture Check for Intune Compliance

Create a device posture check based on Microsoft Intune compliance. Once you create the check, it can be applied to new or existing [posture profiles](/v1/docs/creating-device-posture-profiles-and-device-checks).

**To configure an Intune-based MDM Compliance check:**

1. In the CMA, go to **Resources > Device Posture** and in the **Device Checks** tab, click **New**.
2. In the **General** section, provide information such as the **Name** and **Description** of this rule.
  - Set the **Vendor Type** to **3rd party vendors**.
  - Set the **Device Check Type** to **MDM Compliance**.
3. In the **Vendor** section:
  - Set the **Vendor Name** to **Intune**.
  - Under **Compliance States**, determine which Intune statuses you want to evaluate.

The statuses that you select are considered Passed when detected.
4. Configure **Additional Settings**:
  - **Bypass unrecognized devices** – Allow access if device cannot be identified
5. Click **Save**.
