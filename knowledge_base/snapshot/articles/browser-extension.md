---
title: "What is the Cato Browser Extension"
slug: "what-is-the-cato-browser-extension"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/what-is-the-cato-browser-extension"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is the Cato Browser Extension

This article explains the Cato Browser Extension, how to configure it, and how your users can implement it.

## Overview

Oftentimes, organizations have to work with unmanaged devices that are used by third-party vendors and contractors. These devices can present a challenge as a potential attack vector to your network because they don't necessarily follow the organizational security policy. The Cato Browser Extension lets you provide secure access to SaaS applications for unmanaged devices without giving them direct access to any of your internal resources.

Users install the extension in their browser, and when they enable it, traffic is routed to the forward proxy located on the PoP, processed by the security engines, and from there, to the relevant SaaS application.

> [!NOTE]
> Note:
> 
> The extension is installed on a specific Chrome browser profile and routes traffic through Cato once the extension is connected to the Cato Cloud.

Cato also lets you force your users to connect to the extension whenever they wish to use their unmanaged devices. They can create a rule in the conditional access policies for their IdP or Saas providers that traffic is only accepted if it originates in the Cato Cloud.

![Browser_Extension_-SaaS__1_.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33250915535901.png)

### Use Case

ABC Company has several SaaS apps it works with, for example Figma and Office365, and wants to ensure that all connections to those apps are secure and authorized. They have several contractors that need to access these resources.

The IT department tells the contractors to install the Browser Extension on their unmanaged devices. Then, they create dedicated rules in the Client Connectivity Policy to allow the contractors to access the required resources.

In addition, when they are connected via the Browser Extension, the Cato Cloud inspects the traffic to protect against malicious activities.
