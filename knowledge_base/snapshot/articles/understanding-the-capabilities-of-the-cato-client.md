---
title: "Understanding the Capabilities of the Cato Client"
slug: "understanding-the-capabilities-of-the-cato-client"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/understanding-the-capabilities-of-the-cato-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding the Capabilities of the Cato Client

The Cato Client contains a suite of features to secure your network, devices, and identify and support your users. This article explains the capabilities of the Cato Client and explains why it is recommended to install it on all devices so it can be used by all users. For more information on how to install, prerequisites, sign in, and use the Cato Client, see [Getting Started with the Cato Client](/v1/docs/getting-started-with-the-cato-client).

## Overview

You can easily install the Cato Client on a device to provide a range of capabilities to benefit users connecting remotely or behind a site. As well as supporting universal ZTNA functionality, the Client provides additional benefits, for example, device posture endpoint protection, User Engagement, and Digital experience monitoring.

The capabilities of the Client can be grouped into these key capabilities:

1. Identification and Authentication
2. Device Posture
3. Secured Remote Access (requires a ZTNA license)
4. Secured Internet Access (requires a ZTNA license)
5. Digital Experience (requires a DEM license)
6. User Engagement

![The_Client.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35418990561949.png)

Some of these features, such as secure remote and Internet access, require a ZTNA license. However, there are several features that you can use without a license, and we recommend that you install the Client on all devices in your organization.

## Identification and Authentication

The Cato Client can identify who is connecting to your network and confirm their identity from any place the user is located. By installing the Client on any device, you can identify users with or without a ZTNA license.

The Client has an [Identity Agent](/v1/docs/using-cato-identity-agents-for-user-awareness) that identifies users connecting remotely or behind a site. By installing the Client on every device within your network, you can easily identify all users and enforce policies based on identity in any location.

Confirming the identity of the users connecting to your network protects against unauthorized access.

## Device Posture

[Device Posture](/v1/docs/creating-device-posture-profiles-and-device-checks) lets you control which devices are allowed to connect to your network remotely or behind a site. The Client can run over 10 different checks to assess the conditions of the device. The Client only allows access if the conditions of the device meet your security requirements. The Client continuously checks the device posture to ensure it always complies with your requirements. This protects your network by blocking vulnerable devices.

## Secured Remote Private Access

The Client [Secured Private Access](/v1/docs/what-is-cato-private-access) based on the identity of a user, their context (for example, geographical location), and the device they are connecting with. This is enforced through various [policies](/v1/docs/client-policies) configured in the CMA. For example, with the [WAN firewall](/docs/understanding-the-capabilities-of-the-cato-client#UUID-7dc53880-9368-9ac4-7743-bfc98ebe90aehttps://support.catonetworks.com/hc/en-us/articles/4413265660305#UUID-7dc53880-9368-9ac4-7743-bfc98ebe90ae), [one-time authentication](/v1/docs/remote-internet-security-with-one-time-authentication), and [Device Posture](/v1/docs/creating-device-posture-profiles-and-device-checks), you can ensure that access to your WAN resources is granted only when users are properly authenticated, and their devices meet your security standards, implementing a true Zero Trust architecture.

## Secured Internet Access

The Client ensures that all Internet traffic flows through the Cato Cloud. Cato security engines inspect the traffic to ensure it complies with your security and access policies, for example, CASB. [The Split Tunnel Policy](/v1/docs/routing-with-the-cato-client-split-tunnel-policy) gives you granular control over which traffic goes through Cato and which bypasses it. You can ensure your users and organization are always protected by enabling the [Always-on Policy](/docs/understanding-the-capabilities-of-the-cato-client#UUID-59bfaaed-8efa-6ef2-90af-3a73ea718da1https://support.catonetworks.com/hc/en-us/articles/4417643184529#UUID-59bfaaed-8efa-6ef2-90af-3a73ea718da1). This enhances Internet security by defining rules for when users or User groups always connect to the Cato Cloud.

## Digital Experience Monitoring

The Client supports Synthetic Monitoring, which lets you monitor the reachability and individual user experience for business-critical applications. [Experience Monitoring](/v1/docs/what-is-cato-experience-monitoring) lets you combine the existing Network Analytics with app and user analytics to provide a holistic view of issues that your users are experiencing.

## User Engagement

The Client notifies users when they are attempting to perform an action that the [Data Control](/v1/docs/creating-the-data-control-policy) or [Application Control](/v1/docs/creating-the-data-control-policy) polices block. This provides a better experience for users because they understand why they can't access an app or resource.
