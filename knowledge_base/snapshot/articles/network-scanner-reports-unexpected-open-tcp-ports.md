---
title: "Network Scanner Reports Unexpected Open TCP Ports"
slug: "network-scanner-reports-unexpected-open-tcp-ports"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/network-scanner-reports-unexpected-open-tcp-ports"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Network Scanner Reports Unexpected Open TCP Ports

## Issue

A network scanner has detected open TCP ports over the WAN between sites, reporting them on internal hosts that are known to be non-existent.

## Environment

- Allowed or blocked TCP connections between sites.
- TCP acceleration on SYN for WAN traffic enabled at the account or site level

## Troubleshooting

TCP connections between sites can be affected by TCP proxy, as mentioned in [Explaining the Cato TCP Acceleration and Best Practices](/v1/docs/explaining-the-cato-tcp-acceleration-and-best-practices). The behavior will depend on whether the TCP connection is allowed or blocked by the WAN Firewall and the TCP proxy mode involved.

Review [CMA events](/v1/docs/analyzing-events-in-your-network) to determine whether the TCP connection was allowed or blocked.

### Allowed TCP Connections

WAN traffic over the Cato Cloud operates with two available TCP proxy modes controlled by the **TCP Acceleration on SYN for WAN Traffic** setting in the Advanced Configuration page (more in the [Solution](/v1/docs/network-scanner-reports-unexpected-open-tcp-ports#solution) section).

#### Full WAN TCP proxy mode

This mode initiates the **TCP proxy** immediately upon receiving the first SYN packet for each connection. It enforces TCP proxy on all traffic, regardless of **acceleration** settings. As a result, even if the destination IP does not respond with SYN-ACK, the PoP completes the 3-way handshake with the network scanner. This can lead to false positives, where the scanner reports open TCP ports on non-existent hosts.

> [!NOTE]
> Note:
> 
> Port TCP/443 will always use this mode if TLS inspection is enabled for the account.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21349363093917.png)

#### Preserving original WAN TCP negotiation and delaying the TCP proxy

In this mode, the TCP proxy is delayed until after the TCP handshake with the destination IP is complete. The **TCP proxy** is not enforced regardless of **acceleration** settings.

The 3-way handshake with the scanner only occurs if the destination IP responds with a SYN-ACK.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21349474944157.png)

#### Identifying the TCP Proxy Mode

The active TCP proxy mode can be identified directly through WAN Firewall events. 'TCP Acceleration = 1' means that **Full WAN TCP Proxy** was triggered.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21326599423133.png)

Starting in November 2023, **Full WAN TCP Proxy** is the default mode for new accounts. For accounts created before this date, **Preserving original WAN TCP negotiation** is the default mode.

### Blocked TCP Connections

Blocked WAN traffic over the Cato Cloud will use the **Full WAN TCP Proxy** mode, in which the PoP completes the 3-way handshake with the network scanner, but no SYN packet is sent to the destination. This approach is used to deliver a block page to the source.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21348676189981.png)

## Solution

#### For Allowed TCP Connections

Administrators can modify the WAN TCP Proxy mode by adjusting the **TCP Acceleration on SYN for WAN Traffic** setting within the Advanced Configuration page, applicable at both the [account](/v1/docs/working-with-advanced-configuration-for-the-account) and [site](/v1/docs/advanced-configurations-for-a-site) level.

- **On** - Full WAN TCP Proxy.
- **Off/Disabled** - Preserving original WAN TCP negotiation and delaying the TCP proxy.

**Full WAN TCP Proxy** mode is recommended for optimal performance. However, administrators may choose to disable this mode as needed to avoid false positives for open TCP ports.

To prevent false positives on port **TCP/443**, ensure that **TLS inspection** is disabled. Alternatively, you can contact [Cato Support](/v1/docs/submitting-a-support-ticket) to configure the system to whitelist the network scanner's IP address, effectively preventing false positives.

#### For Blocked TCP Connections

The 3-way handshake behavior in blocked TCP connections is expected under the **Full WAN TCP Proxy** mode. However, if this behavior is problematic, you can contact [Cato Support](/v1/docs/submitting-a-support-ticket) to configure the system to **drop** the first TCP packet instead of completing the handshake with the scanner. This applies to traditional non-complex rules, as explained in [Traditional vs. NG Firewall Rules](/v1/docs/recommendations-for-internet-and-wan-firewall-policies#traditional-vs-ng-firewall-rules).
