---
title: "Using Captive Portal Detection with Cato Clients"
slug: "using-captive-portal-detection-with-cato-clients"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/using-captive-portal-detection-with-cato-clients"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Captive Portal Detection with Cato Clients

This article explains how to authenticate to a Captive Portal for Clients with and without Always On enabled.

## Overview

Captive Portal is a name to identify a network that requires an additional log-in to connect to the Internet. For example, a guest network at a hotel, or an airport. First the user opens the browser to authenticate to the Captive Portal and connect to the Internet, and then uses the Client to connect to the Cato Cloud.

However, for Clients with Always On enabled, you need to enable a setting in the Client before you can connect to the Internet.

## Using a Captive Portal with Always On

When Always On is enabled for the entire account or a specific SDP user, you can enable the Client to let the SDP user authenticate to the Captive Portal.

In the **Settings** menu for the Client, enable **Captive Portal Detection**.

![captivePortal.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218238212253.png)

This is the an overview of the process to authenticate to a Captive Portal when Always On is enabled:

1. The user can’t connect to the Captive Portal because there’s no Internet connection for the device.
2. The Client automatically identifies that this network uses a Captive Portal that requires authentication.
3. Always On is temporarily disabled for the Client.
4. From a browser, the user can now authenticate to the Captive Portal.
5. After the Internet connection is established, the Client automatically connects to the Cato Cloud, and Always On is enabled again.
6. The user is connected to the network for your account with Cato's encrypted tunnel.

## Supported Clients for Captive Portal

The following Client OS support Captive Portal Detection:

- Windows
  - The Captive Portal setting is disabled by default for the Windows Client in v5.6 and below
  - The Captive Portal setting is enabled by default and is removed from the **Settings** menu in v5.7 and above
- macOS
  - The Captive Portal setting is enabled by default for the macOS Client (possible that the macOS will enable the user to authenticate to the Captive Portal)
- iOS
  - The Captive Portal setting is disabled by default for the iOS Client
- Android
  - The Captive Portal setting is disabled by default for the Android Client
