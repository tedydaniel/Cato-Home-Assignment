---
title: "macOS SDP Client Unable to Connect with iPhone Hotspot"
slug: "macos-sdp-client-unable-to-connect-with-iphone-hotspot"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/macos-sdp-client-unable-to-connect-with-iphone-hotspot"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# macOS SDP Client Unable to Connect with iPhone Hotspot

## Issue

The macOS SDP Client fails to connect to Cato when connected to an iPhone hotspot for internet access. It shows error "Connection error. Trying to reconnect".

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19197775864733.png)

## Environment

- macOS SDP Client
- iPhone hotspot running version 17.2 and above

## Troubleshooting

As mentioned in [Installing the Cato Client](/v1/docs/preparing-to-install-the-cato-client), it is recommended that you disable IPv6 on all physical adapters, as Cato Cloud only supports IPv4. In macOS devices, this is done by changing the IPv6 configuration to 'Link-Local Only'.

On some occasions, when a Mac device connects to an iPhone hotspot, disabling IPv6 on the NIC may cause the hotspot to not provide an IPv4 address via DHCP to the Mac device, as shown in the screenshot below.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19197753342877.png)

This issue has been reported to Apple as a bug on their platform. As of May 2024, the issue has yet to be fixed. See this [Apple discussion](https://discussions.apple.com/thread/255346180?sortBy=best).

## Solution

The solution provided in the Apple discussion is to set the IPv6 configuration to 'Automatically' on the Mac device, assign an IPv4 DNS Server (for example, 8.8.8.8) to the physical adapter, and restart the iPhone hotspot. This way the SDP Client can resolve FQDN addresses that require an IPv4 IP address and successfully connect to Cato.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19197876766877.png)
