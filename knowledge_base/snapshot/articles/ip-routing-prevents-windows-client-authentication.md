---
title: "IP Routing Prevents Windows Client Authentication"
slug: "ip-routing-prevents-windows-client-authentication"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/ip-routing-prevents-windows-client-authentication"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# IP Routing Prevents Windows Client Authentication

## Issue

When IP routing is enabled on Windows, authentication of the SDP client will fail.

![authenticating.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13482213157021.jpeg)

## Troubleshooting

## Determine If IP Routing Is Enabled:

To determine whether IP routing is enabled on your Windows device, execute the 'ipconfig /all' command.

![ipconfig.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13482213159709.jpeg)

If the IP routing is enabled, the SDP client will not be able to connect. The reason is because when IP Routing is enabled, it interferes with the SDP Client authentication process. The authentication service **only accepts** requests with a source IP the client received on establishing the unauthenticated tunnel (169.254.255.253), otherwise authentication requests are ignored.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13527045848989.png)

With the IP Routing feature disabled, the source IP used is determined by the authentication service destination IP. The operating system will find in the routing table which interface has route to the authentication service destination IP. SDP Client then adds a route to the authentication service IP via the Cato tunnel interface, so it takes the correct source IP of Cato tunnel interface.

On the other hand, if IP Routing is enabled, Windows can choose a source IP from other interface (for e.g., the WiFi interface), so the authentication requests were ignored

## Solution

Disable IP routing on Windows so that the SDP client will use the IP address of the CatoNetworks adapter for authentication. To do that, choose one of the two options -

**Option 1 -**

1. Open the Windows Registry Editor by pressing Win + R, typing "regedit," and pressing Enter.
2. Navigate to the following registry key:

`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters `
  - If the "IPEnableRouter" value doesn't exist, you can assume IP routing is already disabled.
  - If the "IPEnableRouter" value exists and is set to "1," it means IP routing is enabled. To disable it, right-click on "IPEnableRouter," select "Modify," and change the value to "0."

In the right pane, look for a DWORD value named "IPEnableRouter."
3. Close the Registry Editor.

![registry.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13526893018397.jpeg)

After making this change and rebooting Windows, IP routing should be disabled.

**Option 2 -**

1. Open the Windows Services by pressing Win + R, typing "services.msc," and pressing Enter.
2. Scroll down and press on "Routing and Remote Access."![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/14533586681373.png)
3. Pressing on the "Stop" button at the top on the Services window (Or Right-clicking on the service) will give you the option to disable it.
