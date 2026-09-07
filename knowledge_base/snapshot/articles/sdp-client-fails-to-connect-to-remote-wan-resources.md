---
title: "SDP Client Fails to Connect to Remote WAN Resources"
slug: "sdp-client-fails-to-connect-to-remote-wan-resources"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/sdp-client-fails-to-connect-to-remote-wan-resources"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SDP Client Fails to Connect to Remote WAN Resources

## Issue

The SDP Client is unable to connect to remote WAN resources via Cato, such as network drives. Connection attempts either time out or fail to reach the destination (e.g., ping fails).

## Root Cause

This issue is typically caused by **overlapping subnets** between the SDP Client's local (home) network and the remote site hosting the WAN resources. Most home routers use default IP ranges like **192.168.0.0/24**, **192.168.1.0/24**, or **10.0.0.0/24.** If the remote network is configured with the same range, the client may misroute traffic locally instead of through the Cato tunnel, resulting in failed connections.

## Troubleshooting

1. Compare the client’s local subnet with the subnet of the remote resources. If they overlap, the issue is likely related to routing conflicts.
2. For Windows Clients (v5.3 and higher), use the [**LAN Access**](/v1/docs/routing-with-the-cato-client-split-tunnel-policy) feature to block access to the local LAN. This forces all traffic, including LAN-routed traffic, through the secure Cato tunnel, avoiding conflicts with local resources.
3. SDP Clients in other OSs, such as macOS and Linux, do not support the LAN Access block feature. Instead, configure a **Split Tunnel** policy in CMA to explicitly direct traffic through the tunnel:
  - Define the necessary remote subnet(s) as [IP Ranges](/v1/docs/using-ip-ranges-in-policies) in CMA (e.g., name the range *Home-LAN*).
  - Add a second IP Range as a *default route* (0.0.0.0/0) to ensure all traffic can be tunneled.
  - Apply these IP Ranges under the “Exceptions” section of a **Split Tunnel** policy that is set to *“Route all traffic Out-of-Tunnel”*. Specify the applicable OS platforms in the policy. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28036676131997.png)
  - In some cases, you may need to define /32 IP ranges for individual remote hosts if only specific systems are affected.

### Best Practice Recommendations

- If possible, configure the corporate or branch office network to use less common IP ranges, minimizing the risk of conflicts with home LANs.
- Alternatively, instruct users to change their home router’s DHCP settings to assign a less typical IP range.

By identifying and resolving subnet overlap issues, you can significantly improve the reliability and consistency of remote WAN access via the SDP Client. For additional help with internal resource access issues, see [Access to Internal Resources Troubleshooting](/v1/docs/access-to-internal-resources-troubleshooting).
