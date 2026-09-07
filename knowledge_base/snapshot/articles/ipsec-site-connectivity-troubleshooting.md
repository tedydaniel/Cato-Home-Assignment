---
title: "IPsec Site Connectivity Troubleshooting"
slug: "ipsec-site-connectivity-troubleshooting"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/ipsec-site-connectivity-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# IPsec Site Connectivity Troubleshooting

## Overview

Connectivity is paramount for access to the WAN via the Cato cloud for networks behind an IPsec. The lack of connectivity of an IPsec site can disrupt business functions. This playbook looks to guide troubleshooting in this scenario.

## Symptoms

A failure in IPsec connectivity can be determined in the following ways. An administrator may note the following symptoms:

- IPsec Site is disconnected in CMA
- History of instability in the connection
- Poor performance for traffic traversing the IPsec connection

## Possible Causes

The following are possible causes that you can identify while troubleshooting.

- Peer Connectivity
  - This includes the ability for the peers to reach each other consistently over L3 underlay.
- IPsec configuration mismatch
  - Transform sets or authentication mismatches can cause tunnels not to form at all or to fail before a rekey can be completed
- Underlay performance
  - IPsec relies on a stable underlay connection for satisfactory performance inside the tunnel.

> [!NOTE]
> Note:
> 
> For accounts with IPsec sites, if the external IPs of an RPF rule overlaps with the IP addresses of an IPsec site, make sure that the rule excludes the IPsec tunnel ports UDP/500 and UDP/4500.

## Troubleshooting the Issue

Steps to troubleshoot the symptoms an Administrator may encounter are listed below. These steps are intended to identify possible causes for the issues faced. The resolution steps will be highlighted later in the playbook.

### Troubleshooting Disconnected or Unstable IPSec Site in CMA

#### Gathering Information from Events

Using the **Home** > **Events page** in CMA, an administrator can quickly get a history of connectivity events for IPsec sites within an account. Events can be filtered down into relevant events by selecting the 'Sites connectivity status' preset or by filtering for Event type 'Connectivity' and Sub-type 'Disconnected'. You can further filter for the name of the site in question with the 'Source site' field or else use the Tunnel protocol value 'IPSEC' to filter for all IPsec sites.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17506145984157.png)

Viewing the timestamp of the relevant disconnection event from the site in question can help focus the investigation. Were any wider networking events or local power events known to occur at this time stamp? Are there any [audit trail](https://support.catonetworks.com/hc/en-us/articles/4413273463953-Using-the-Admin-Audit-Trail) changes preceding this that may be correlated?

If no disconnect event is found and the tunnel is still reported as unstable, it is possible that the issue occurs at the time of a rekey process due to mismatching parameters between Cato and the remote peer. Continue with the steps below for further analysis.

#### Viewing Site IPsec Connection History

> [!NOTE]
> IMPORTANT:
> 
> If this file isn't available in CMA (file not found), it means that Phase 1 (or IKE_SA in IKEv2) hasn't been negotiated with the remote peer. Confirm that IKE and Authentication parameters match between the two peers.

The timeline available in **Network > Site > Site Configuration > IPsec** is essential for troubleshooting disconnected IPsec sites.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17605960511517.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17605907441309.png)

The CSV provided by the Timeline button will give a history of relevant tunnel logs. These logs can provide clear indications of the issues that may be causing the lack of connectivity in the IPsec connection. Common examples of indicative messages are below:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18475198129821.png)

Messages suggesting traffic selectors do not match are evidence of a configuration mismatch between the peers' phase 2 settings, specifically regarding the subnets that will be available on each side of the IPsec peering. If you see errors suggesting this is the case, navigate to [Resolving IPsec configuration mismatch](/v1/docs/ipsec-site-connectivity-troubleshooting#resolving-ipsec-configuration-mismatch).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18096417937309.png)

The above messages also indicate a configuration mismatch, this time with the auth payloads. Of course, the PSK needs to match these payloads for the connection to be successful. If these are evident in any connection attempt, navigate to [Resolving IPsec configuration mismatch](/v1/docs/ipsec-site-connectivity-troubleshooting#resolving-ipsec-configuration-mismatch).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18475169969053.png)

The above timeline displays an attempted connection with a configured peer, which received no response. It can be seen in this timeline that no interaction with the peer occurred, and the SA was closed due to inactivity. This is typically the case when there is no L3 reachability to the remote peer. In these instances, view the [Resolving Peer Connectivity](/v1/docs/ipsec-site-connectivity-troubleshooting#resolving-peer-connectivity).

A complete list of possible timeline error messages for IKEv1 and IKEv2 can be found [here](/v1/docs/troubleshooting-ipsec-connectivity).

#### Using Packet Captures to Troubleshoot

> [!NOTE]
> Note:
> 
> when taking packet captures, the PoP IP you have configured for the tunnel will be abstracted behind a 10.x.y.z internal IP.

Also, in the **Network > Site > Site Configuration > IPsec** page is the packet capture tool. This will help provide packet traces of the control traffic between the peers. The issues highlighted above are also represented in these packet captures.

**TS_UNACCEPTABLE**

For mismatching subnets within a transform set, informational packets will advise of an error. In this IKEv2 example, the informational message TS_UNACCEPTABLE is symptomatic of a mismatch in configuration within the transform set. To fix this issue, navigate to [Resolving IPsec configuration mismatch](/v1/docs/ipsec-site-connectivity-troubleshooting#resolving-ipsec-configuration-mismatch).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18096541780253.png)

**NO_PROPOSAL_CHOSEN**

For mismatching parameters within the security association, either peer will include an error within the payload. In this IKEv2 example, the error NO-PROPOSAL-CHOSEN clearly indicates that one of the algorithms or DH groups configured in CMA do not match the configuration of the remote peer. This can occur during the initial establishment of the tunnel or the rekey process.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18475198132893.png)

**AUTHENTICATION_FAILED**

The capture below shows another IKEv2 example, this time one in which the PSK used for authentication did not match:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18475198133533.png)

**One-Way Packets**

Packet captures can also help to identify connectivity issues at the IP level with peers. In the example below, the packet capture only shows one-way, outgoing traffic, suggesting that the peer is unreachable. If a troubleshooting administrator sees an unreachable peer, navigate to [Resolving Peer Connectivity](/v1/docs/ipsec-site-connectivity-troubleshooting#resolving-peer-connectivity).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18096541772829.png)

In any of the above instances or other indicators of configuration mismatch between peers in IKEv1 or IKEv2, navigate to [Resolving IPsec configuration mismatch](/v1/docs/ipsec-site-connectivity-troubleshooting#resolving-ipsec-configuration-mismatch).

### Troubleshooting poor performance over VPN

If poor performance is seen over the VPN, this typically takes the form of packet loss, high latency or frequent disconnections.

Packet loss will be seen on traffic going through the tunnel through the applications it is affecting and can be confirmed by testing with ICMP probes from one host to another via the IPsec connection.

Latency and tunnel disconnections will also be evident in application performance and can also be determined via the **Network > Site Monitoring > Network Analytics** page for the site in question.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18111755392669.png)

If performance issues are identified, navigate to [Resolving Underlay Performance](/v1/docs/ipsec-site-connectivity-troubleshooting#resolving-underlay-performance).

#### Packet Drops in Azure IPSec

When configuring IPSec with Azure, tunnel throughput and packets per second (PPS) are determined by the VPN gateway's SKU and the encryption algorithms employed. For instance, according to [Microsoft’s documentation](https://learn.microsoft.com/en-us/azure/vpn-gateway/about-gateway-skus#performance), the VpnGw3 Generation2 gateway, when using GCMAES256, can handle up to 140,000 packets per second (PPS). ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22181147805469.png)

If traffic exceeds these thresholds, Azure will automatically drop the excess packets, which can cause noticeable performance degradation. One common symptom is a reduction in throughput, which may appear in CMA's Network Analytics as a drop in traffic volume. However, a more precise way to diagnose this is by monitoring VPN gateway metrics directly within the Azure portal, which provides real-time insights into tunnel throughput and PPS values for the affected VPN connection.

To mitigate this issue, you may consider upgrading to a higher IPSec SKU or deploying an [Azure vSocket](/v1/docs/deploying-azure-vsockets-from-the-marketplace), both of which can enhance your VPN tunnel's capacity and prevent packet drops due to traffic overload.

## Resolving Discovered Issues

### Resolving Peer Connectivity

For scenarios in which the IPsec peer is not sending packets to the PoP, shown via timeline entries or packet captures, please make sure that the remote peer is configured to connect to the same IP address as has been allocated to the tunnel in CMA.

If this configuration is confirmed, ensure the remote peer can traverse connections bounded by NAT by responding to traffic on port 4500 as well as port 500. NAT-T (NAT Traversal) should be enabled on the remote peer.

If the remote peer device is configured to respond to ICMP requests over the internet, you can also test its general reachability by testing ICMP requests to the device's public IP.

Check for recent status page health changes - If the PoP is experiencing issues, this can impact the IPsec tunnel (each tunnel is connected to one Cato PoP location). You can monitor Cato PoP health on the [status page](https://status.catonetworks.com/).

If the remote peer is a cloud vendor such as Azure or AWS, you can also check their status pages.

If the peer device is still unreachable for this IPsec connection, reach out to the administrator to ensure it is publicly accessible for IPsec connections.

### Resolving IPsec configuration mismatch

Ensure that the peer configuration for the transform set matches the configuration on the **Site > IPsec** page.

To configure the Cato side of the peering to match a specific transform set from the peer, edit the configuration as described in the linked documentation for [IKEv1](/v1/docs/configuring-ipsec-ikev1-sites) and [IKEv2](/v1/docs/configuring-ipsec-ikev2-sites).

IP ranges (selectors) on both sides of the tunnel must match. In CMA, ensure that the IP ranges are configured as follows:

- **Local IP Ranges (Peer Side):** Navigate to **Site Configuration > Networks** and define the subnets located behind the IPsec peer (e.g., firewall or router).
- **Remote IP Ranges (Cato Side):** Navigate to **Site Configuration > IPSec > Routing** and define the local IP rangesallowed to traverse the tunnel (typically networks from other sites). If this field is not configured, the tunnel is considered a route-based VPN with implicit selectors 0.0.0.0 <> 0.0.0.0.

Some vendors require all subnets included in the transform set to be included in only a single transform set message. If this is the case for a peer, an admin should utilise the advanced configuration option 'IKEv2 Send Single TS per payload' under **Site > Advanced Configuration**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18117471201693.png)

### Resolving Underlay Performance

The focus for resolving underlay performance is to isolate the performance against the remote peer.

Test the remote peer's ability to ping public web servers like 8.8.8.8. If the delay or packet loss is consistent with the tunnel's, the conclusion can be made that the issue exists within the remote peer's environment.

## Raising cases to Cato Support

Submit a Support ticket with the results of the above troubleshooting steps. Please include the following information in the ticket:

- Relevant timeline entries with timestamps
- Relevant packet captures
- Confirmation of matching transform sets, including subnet associations and auth/encryption parameters
