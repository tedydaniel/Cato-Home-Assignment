---
title: "Product Update - July 15, 2024"
slug: "product-update-july-15-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-july-15-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - July 15, 2024

## New Features & Enhancements

- **Windows Client v5.11:** From July 14, 2024, we are starting the rollout of Windows Client version 5.11. This version contains:
  - **IPv6 Support for Last Mile Connection:** Users can connect remotely over ISPs that provide last-mile [IPv6-only](/v1/docs/cato-client-last-mile-support-for-ipv6) connections. Both IPv6 and IPv4 connections are now supported.
  - **Authenticating with Windows Credentials Supported on Azure Hybrid AD Joined Devices:** Users on Azure Hybrid AD Joined Devices can authenticate [with their Windows credentials](/v1/docs/authenticate-users-automatically-with-windows-credentials) for an improved user experience. You can configure the Client to launch, add a user, authenticate, and connect without any user action.
    - Azure AD with MFA is now also supported
  - **New Cato Root Certificate:** We added a new root certificate that is automatically installed on the device with the Cato Client.
    - The new certificate is called **Cato Networks Root CA** and expires in March 2034.
    - The previous certificate is from 2015 and is called **Cato Networks CA**. It will expire in Oct 2025.
  - **Bug Fix:**
    - If a login attempt failed, in some cases users were unable to connect to the network

- **macOS Client v5.7:** From July 14, 2024, we are starting the rollout of macOS Client version 5.7. This version contains:
  - **IPv6 Support for Last Mile Connection:** Users can connect remotely over ISPs that provide last-mile [IPv6-only](/v1/docs/cato-client-last-mile-support-for-ipv6) connections. Both IPv6 and IPv4 connections are now supported.
  - **User Notifications for CASB and DLP:** The device displays a notification to the user when their activity is blocked by [App Control](/v1/docs/managing-the-application-control-policy) or [Data Control](/v1/docs/creating-the-data-control-policy) rules. This educates the user about which app was blocked and why.
  - **End User Feedback**: To help us continually improve our remote access, users can now provide [feedback](/v1/docs/providing-cato-with-remote-user-feedback) to Cato from within the Client.
    - Every few months, users are prompted to give a rating and comments
    - Users can also manually provide feedback at any time
  - **End of Support for Big Sur:** Devices running Big Sur (macOS 11) are no longer supported by the macOS Client
  - **New Cato Root Certificate:** We added a new root certificate that is automatically installed on the device with the Cato Client.
    - The new certificate is called **Cato Networks Root CA** and expires in March 2034
    - The previous certificate is from 2015 and is called **Cato Networks CA**. It will expire in Oct 2025
  - **Bug Fix:**
    - If a login attempt failed, in some cases users were unable to connect to the network
- **Mute Stories Rules for XDR Anomaly Detection Stories:** The [XDR Mute Stories policy](/v1/docs/muting-xops-stories) now supports Usage Anomaly and Events Anomaly Security stories. For example, if you know that a specific user uploads unusual amounts of data on OneDrive as part of their work requirements, you can create a rule so stories won't be generated for OneDrive traffic from that user.
  - Available for XDR Pro and MDR customers

Go to the [Cato Product Roadmap](https://bit.ly/49aFEKU) in the Knowledge Base to follow the status of upcoming features and enhancements.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
