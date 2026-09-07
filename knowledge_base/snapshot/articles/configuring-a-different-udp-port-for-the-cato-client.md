---
title: "Configuring a Different UDP Port for the Cato Client"
slug: "configuring-a-different-udp-port-for-the-cato-client"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/configuring-a-different-udp-port-for-the-cato-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring a Different UDP Port for the Cato Client

## Overview

By default, the Cato Client uses UDP port 443 to establish a VPN tunnel to the Cato Cloud. However, there are some situations where this port is blocked, such as airport and hotel networks. If the port is blocked, the Cato Client may not be able to connect to the VPN.

In the event that UDP 443 is blocked, it is possible to change the Port to UDP 1337.

## Windows

The Port value for the Cato Client on Windows machines are set within the registry. You will need to modify the registry keys to configure the Cato Client to use port 1337 instead of port 443.

> [!NOTE]
> - You must have admin permissions on the computer to make changes to the registry.
> - The dns_port and server_port registry keys are of type DWORD with the value set to 1337.
> - This is a permanent change to the Windows computer and survives a reboot.

**To configure the Cato Client to use UDP port 1337:**

- Add the **dns_port** and **server_port** keys to the registry with the custom port 1337 (Decimal):
  - `Computer/HKEY_LOCAL_MACHINE/SOFTWARE/CatoNetworksVPN/dns_port=1337`
  - `Computer/HKEY_LOCAL_MACHINE/SOFTWARE/CatoNetworksVPN/server_port=1337`

## MacOS

As of the macOS 4.5.1 Cato Client, you are able to change the UDP port value from 443 to 1337 using a terminal command. Please ensure that the Cato Client Application is not running before making these changes.

> [!NOTE]
> This is a permanent change to the macOS Cato Client application and will persist through a reboot.

To configure the macOS Cato Client to use UDP 1337:

1. Open a Terminal window on your macOS machine
2. Enter the command:

`defaults write com.catonetworks.mac.CatoClient connectionPort -string 1337`
3. Open the Cato Client to verify that the VPN connection can be established using the new port.

To revert the changes and restore the original port (UDP 443):

1. Open a Terminal window on your macOS machine
2. Enter the command:

`defaults write com.catonetworks.mac.CatoClient connectionPort -string 443`
3. Open the Cato Client to verify that the VPN connection can be established using the default port.
