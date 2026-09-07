---
title: "Settings That Can be Modified by Cato Support"
slug: "settings-that-can-be-modified-by-cato-support"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/settings-that-can-be-modified-by-cato-support"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Settings That Can be Modified by Cato Support

There are many advanced settings that can be modified on an account or site level by Cato Support. Many of these settings are not visible in the Cato Management Application or the Socket, so please contact us if you would like any of these settings applied.

## Application

| **Setting** | **Description** | **Default Value** |
| --- | --- | --- |
| Application Finalization | Increases the time that Cato waits before finalizing application identification. | 2000 milliseconds |
| Force Fragmentation | Forces fragmentation of packets even if the DF bit is set. Each app that requires fragmentation must be defined. | Disabled |

## IPsec

| **Setting** | **Description** | **Default Value** |
| --- | --- | --- |
| Dangling SAs | Force Cato to rekey phase 2 following a phase 1 rekey. | If phase 2 is not expired, use the existing SAs. |

## Networking

| **Setting** | **Description** | **Default Value** |
| --- | --- | --- |
| Cato Service Range | Change the subnet reserved by Cato for system traffic. | 10.254.254.0/24 |
| ICMP Keep Alive | Generate an ICMP keep alive through a tunnel. | Disabled |
| Max Flows per Host | Changes the maximum number of flows that a single IP can open at once. | 20,000 |
| Max Hosts per Tunnel | Changes the maximum number of hosts per tunnel | 10,000 |

## Security

| **Setting** | **Description** | **Default Value** |
| --- | --- | --- |
| Whitelist IP | Prevent any client IP address from being blocked by any Cato security policy. Useful for vulnerability scans. | Disabled |
| Whitelist IPS signature | Whitelist specific threats from IPS for the whole account | Disabled |

## Socket

| **Setting** | **Description** | **Default Value** |
| --- | --- | --- |
| Bypass Flow Timeout | Change the flow timeout for bypassed traffic on the Socket. Can also be adjusted in the Socket Web UI under Cato Connection Settings, but it will be reset back to default following a reboot or tunnel disconnect. | 60 seconds |
| GUI Access from Internet | Allows access to the Socket GUI from the Internet, such as through Remote Port Forwarding. | Access to the Socket GUI from the internet is blocked. |
| HA | Change HA failover behavior depending on whether the Socket has internet access or a tunnel established to a PoP. Also sets the grace time for failover. | If a Socket loses internet access, failover will occur in 10 seconds. If the Socket has internet access but no tunnel established to a PoP, failover will not occur. |
| MTU | Change the Socket's WAN interface MTU. | MTU is set using PTMUD from the PoP to the Socket. |
| Preferred IP | Change the PoP preferred IP for a Socket. This can also be done in the Socket Web UI under Cato Connection Settings. | Dynamic |

## User Awareness (UA)

| **Setting** | **Description** | **Default Value** |
| --- | --- | --- |
| Event IDs | Excludes a Windows Event ID generated on a Domain Controller from triggering an IP mapping for a user. | Event IDs 4768, 4769, 4770, 4624, 5145, 5140 |
| Windows UA | Enables UA for other operating systems other than Windows. | Windows only |

## SDP Client

| **Setting** | **Description** | **Default Value** |
| --- | --- | --- |
| MFA Prompt Grace Time | When "Always Prompt" is enabled for MFA authentication, this setting determines how long a Client will not be prompted for an MFA code on future reconnects following a successful connection. | 5 minutes |
| SSO Expiration Period | Change the SSO cookie expiration period. This setting determines when a VPN user authenticating with SSO will need to re-enter credentials. | 30 days |
| Blocklist of OS for SDP Client | Identify the Client OS type, and if it appears in the account blocklist - fail the connection process | Disabled |
| Cato Client behind Socket | Detects if a Cato Client is behind a socket or not. If a socket was detected, the Socket tunnel will take precedence over the client tunnel | Enabled |
