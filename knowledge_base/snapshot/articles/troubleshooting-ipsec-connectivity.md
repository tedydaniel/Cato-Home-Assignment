---
title: "Troubleshooting IPsec Connectivity"
slug: "troubleshooting-ipsec-connectivity"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/troubleshooting-ipsec-connectivity"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting IPsec Connectivity

## Overview

There are many different factors that can cause an IPSec tunnel to fail, such as incorrect configuration, misconfigured routing, or potential hardware issues. This article describes different tools that you can use to investigate and discover the root cause of tunnel connectivity issues and then remediate them.

## Troubleshooting IPSec Tunnels in the Cato Management Application

The IPsec section for the site contains the tools that you can use to troubleshoot connectivity issues for the site, including:

- Timeline connection log
- Traffic capture (PCAP)
- Connection Status
- Reset tunnel

These tools are available for IPSec site types (IKEv1, IKEv2) and can be used for both the primary and secondary tunnels.

**Note**: Troubleshooting tools are not supported for IPSec IKEv1 FW-init.

To show the IPsec section, go to **Site Configuration > IPSec**.

### Timeline Connection Log

| ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36481184013725.png) |
| --- |

The Timeline Connection Log is a record of recent events and provides the end user “history” of the tunnel state which may be helpful during an investigation.

When you download the Timeline, you receive two CSV files (Active and Archive timelines) with chronological logs for IPSec negotiation changes.

This readable format allows you to easily identify when changes occurred and their cause.

| ![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247858781213(1).png) |
| --- |

**Note**: The timeline logs appear in UTC timezone for ease of use.

To download the timeline logs, expand the **Primary** or **Secondary** section for the IPsec site and click **Timeline**.

#### Timeline Logging Limitations

- Maximum log records for an active timeline file - 100
- Maximum log records for an archive timeline file - 300
- If the tunnel is down, only the archive timeline file is available.

### Traffic Capture (PCAP)

A packet capture provides low-level analysis of what’s happening over the tunnel. This is useful for deeper investigations. The Cato Management Application lets you download a PCAP from the relevant Cato PoP used for the IPSec connection.

| ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36481197205789.png) |
| --- |

Two PCAP files (Active and Archive PCAPs) are downloaded. The files include descriptions for each packet traversing the tunnel alongside Protocol, Port, Message types and more.

![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247858994717(1).png)

#### Traffic Capture Limitations

- The PCAP timeframe appears according to your local host machine settings.
- If the tunnel is down, only the archive PCAP file is available.
- IKEv1 maximum packet size:
  - Active PCAP - 512 packets
  - Archive PCAP - 1024 packets
- IKEV2 maximum packet size:
  - Active PCAP - 256 packets
  - Archive PCAP - 1024 packets

### Connection Status

The Connection Status tool presents a state summary of your IPSec site. When you click the **Connection Status** button, the last available snapshot of data is grabbed and displayed on the screen.

If the site is disconnected, connection status is **not** fetched.

| ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36481197205917.png) |
| --- |

| ![image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247831360797(1).png) |
| --- |

The connection status includes the following summary fields for each IPSec tunnel:

- Site name
- Account name
- Local address
- Peer address
- Last IKE SA established
- Last ESP SA established
- Init message parameters (Protocol, DH Group, Encryption algorithm, Encryption key length, PRF algorithm, Integrity algorithm)
- Auth message parameters (Protocol, DH Group, Encryption algorithm, Encryption key length, Integrity algorithm)
- Connection IKE SAs (SPI Initiator, SPI Responder, Local port, Peer port, Current stage, timestamp)
- IKE Connection Algorithms (DH length, PRF algorithm, Integrity algorithm, Cipher algorithm, GCM encryption)
- Flags
- Connection ESP SAs (SPI Initiator, SPI Responder, timestamp, IKE SPI data, Incoming and outgoing data packets)
- ESP Connection Algorithms (DH length, Integrity algorithm, Cipher algorithm, GCM encryption)
- Flags

### Resetting the IPSec Tunnel

You can trigger the connected PoP to reset the IPSec tunnel with the remote peer address. Resetting the tunnel may help to re-establish the connection for the site.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36481184016029.png)

To reset the IPsec tunnel, expand the **Primary** or **Secondary** section for the IPsec site and click **Reset Tunnel**.

#### Reset Limitations

- IKEv1 tunnels - Resetting is instant.
- IKEv2 tunnels - Resetting may take up to two minutes to re-establish connectivity.
- BGP failover may take place if high availability is configured.
- In case a tunnel is FW-initiated (Initiated by the remote peer), you need to make sure the tunnel is re-established on the remote peer side (When the tunnel is down, the reset button is disabled).

## Common IPSec Troubleshooting Practices

The following section includes a common steps to consider when you are investigating issues with an IPSec tunnel.

**Note:** These steps are not related to packet loss issues.

1. Check for recent status page health changes - If the PoP is experiencing issues, this can impact the IPSec tunnel (each tunnel is connected to one Cato PoP location). You can monitor Cato PoPs health in the [status page](https://status.catonetworks.com/).

If the remote peer is a cloud vendor such as Azure or AWS, you can also check their status pages.
2. Collect remote IPSec firewall configuration.
  - Who is set to initiate the tunnel?
  - Does the IPSec configuration on the remote firewall match the IPSec configuration on the Cato Management Application? (i.e. do IKE message parameters match?)
  - Review **Connection Status** in the Cato Management Application.
  - Is NAT-T enabled on the remote IPSec firewall?
3. Collect logs and PCAPs on the remote IPSec firewall and timeline and PCAPs on the Cato Management Application.
  - Review logs for any irregularities, do remote firewall timestamps correlate with Events and timeline logs downloaded from Cato?
  - Review PCAPs for packet-by-packet communication.
4. Review traffic selectors - Is the tunnel policy-based or route-based?
5. Review general site configuration in the Cato Management Application:
  - Is this a High Availability setup? If yes, what is the BGP status?
  - Is there a PSK mismatch? (PSK is supported up to 64 characters)
6. Reset the tunnel in the Cato Management Application.
7. **Contact your account representative or open a ticket to Cato Support.**

## Timeline Log Failure Connectivity Messages

This section contains a list of failure messages in the IPSec timeline logs.

**IKEv1:**

| "No supported p1 transform" |
| --- |
| "The chosen P1 transform is XXX and it doesn't match the current configuration" - p1 mismatch |
| "No supported p2 transform" |
| "The chosen phase 2 transform is XXX and it doesn't match the current configuration" |
| "The chosen phase 2 transform is XXX and it doesn't match the current AWS configuration template" - in case AWS is in use |
| "Unable to find a suitable peer for this connection - using random, expect errors" |
| "Configuration mismatch: FW is trying to connect without local subnets while the site is configured with subnets" |
| "FW is trying to connect to a cato init site with local subnet <> but the site's <site_id> local is with 0.0.0.0/0" |
| "Local subnet " <subnet details> " isn't configured in site" |

**IKEv2:**

| *IKEV2_CONN_CLOSE_REASON__UNKNOWN* = 0 |
| --- |
| *IKEV2_CONN_CLOSE_REASON__TIMEOUT* = 1 |
| *IKEV2_CONN_CLOSE_REASON__CONFIG_MISMATCH* = 2 |
| *IKEV2_CONN_CLOSE_REASON__CONFIG_CHANGED* = 3 |
| *IKEV2_CONN_CLOSE_REASON__SITE_REMOVED* = 4 |
| *IKEV2_CONN_CLOSE_REASON__NO_PEER_PROPOSAL_SELECTED* = 5 |
| *IKEV2_CONN_CLOSE_REASON__USER_REQUEST* = 6 |
| *IKEV2_CONN_CLOSE_REASON__TUNNEL_CREATION_FAILURE* = 7 |
