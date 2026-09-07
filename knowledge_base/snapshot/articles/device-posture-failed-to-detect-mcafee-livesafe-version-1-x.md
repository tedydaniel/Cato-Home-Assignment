---
title: "Device Posture Failed to Detect McAfee Livesafe Version 1.x"
slug: "device-posture-failed-to-detect-mcafee-livesafe-version-1-x"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/device-posture-failed-to-detect-mcafee-livesafe-version-1-x"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Device Posture Failed to Detect McAfee Livesafe Version 1.x

## Issue

A device posture policy was configured to match McAfee LiveSafe version 1.x. However, despite the Windows device having McAfee LiveSafe version 1.x installed, the policy match failed, causing the user connection to be unsuccessful.

## Environment

- This affects McAfee LiveSafe installed on Windows
- McAfee LiveSafe is running on version 1.x

## Troubleshooting

- All Windows users had McAfee LiveSafe version 1.x installed on their devices.
- The following Device Check was configured to match the application and used in the Device Posture Profile, which is, in turn, applied in the policy for Windows users connecting to Cato. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21489044310941.png)
- When users try to connect, the connection fails. In the events, the block rule points to the device posture.

## Solution

If the McAfee LiveSafe version is 1.x as follows, despite having the McAfee LiveSafe on the UI, this will only be matched when the "**McAfee**" is selected under Product.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21489044313501.png)

The following Device Check rule needs to be configured instead.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21489044315037.png)

The reason is that McAfee LiveSafe version 1.x has similar functionality, registry, and files as the McAfee product. This version is not identified as a different product. Hence, it uses the same signature as the **McAfee** product.
