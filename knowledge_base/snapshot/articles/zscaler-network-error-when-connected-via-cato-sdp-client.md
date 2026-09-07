---
title: "Zscaler Network Error When Connected Via Cato SDP Client"
slug: "zscaler-network-error-when-connected-via-cato-sdp-client"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/zscaler-network-error-when-connected-via-cato-sdp-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Zscaler Network Error When Connected Via Cato SDP Client

## Issue

The Zscaler Client Connector encounters a connection failure when used in conjunction with the Cato SDP Client, displaying an error message stating "No network interface can be detected."

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/14207569466525.png)

## Environment

- Cato SDP Client connected to the Cato Cloud.
- Zscaler Client Connector App version 4.1.

## Reason

The connection failure is attributed to a compatibility issue between the Cato SDP client and Zscaler Client Connector App version 4.1.

When the Cato SDP client is connected, it assigns a 169.254.x.x IP address (defaulting to 169.254.254.1) as the default gateway address to route traffic via the tunnel. However, when the Zscaler Client Connector 4.1 and above detects the use of a link-local IP address as the next hop, it blocks the Zscaler connection.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/14231079544861.png)

From zScaler Client logs, the error looks like this:

```plaintext
2023-08-14 16:54:44.117118(+0530)[11896:11880] ERR Default Interface Gateway is: 169.254.254.1
```

This issue will persist even if the Zscaler Cloud public IP is bypassed from the Cato tunnel (split tunnel).

## Solution

The issue has been resolved in Zscaler version 4.2 or later.
