---
title: "Configuring BFD for BGP Neighbors"
slug: "configuring-bfd-for-bgp-neighbors"
updated: 2026-06-21T12:38:54Z
published: 2026-06-21T12:38:54Z
canonical: "knowledge.catonetworks.com/configuring-bfd-for-bgp-neighbors"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring BFD for BGP Neighbors

This article explains how to configure Bidirectional Forwarding Detection (BFD) for BGP neighbors for sites in your account.

## Overview

Bidirectional Forwarding Detection (BFD) lets you significantly reduce BGP failover times by detecting path failures faster than standard BGP timers. Enabling BFD on sites that use BGP helps maintain high availability and minimizes downtime during routing changes.

Cato supports BFD for BGP neighbors on IPsec and Cloud Interconnect sites. BFD is implemented according to RFCs 5880, 5881, and 5882. BFD in passive mode is supported for all sites (including Sockets and vSockets).

When BFD detects a failure, it signals the BGP peer to immediately tear down the session and trigger failover to the secondary path. Without BFD, BGP relies on the default hold timer (60 seconds), which delays convergence and recovery.

Cato supports single-hop and multi-hop BFD for BGP peers on IPsec and Cloud Interconnect sites. Multi-hop BFD gives you more flexibility for BGP deployments where the BGP peers are not directly connected and the BFD session operates across one or more intermediate hops. For multi-hop BFD sessions, Cato uses UDP port 4784 and does not require BFD packets to arrive with a TTL value of 255, allowing the session to operate across routed paths. This helps improve routing resilience in more complex network topologies.

### Use Case

**Speeding up BGP convergence for an IPsec site** - BFD can quickly detect connection issues and trigger the routing protocol to move to an alternative failover path for Cato sites. For example, BGP convergence for IPsec sites can take up to 60 seconds without BFD. After BFD is configured for a site, the default detection time is approximately 5 seconds.

### Known Limitations

- The acceptable settings for BFD time interval (transmit and receive) is between 100 and 1800 milliseconds.

**Note:** The transmit and receive intervals should fall within the range of 2 to 20 packets in order to work optimally.
- BFD Asynchronous Mode is supported by default (Echo Mode, Demand Mode, and BFD authentication mechanisms aren't supported).

## Understanding BFD for BGP Enabled Sites

> [!NOTE]
> Note:
> 
> Cato supports BFD in the asynchronous mode.

To establish a BFD session, enable and configure BFD in the Cato Management Application, as well as on the remote peer. When the BFD session is established, BFD timers are negotiated, and BFD peers initiate exchange of control packets at the agreed-upon interval settings (BFD is initiated by Cato by default if there is at least one BFD-enabled active peer).

The effective detection time of a BFD session is determined by the local detection multiplier, the minimum receive interval, and the minimum transmit interval for BFD packets. The formula for calculating detection time is as follows:

- ![BFD_Formula.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247938849309.png)

> [!NOTE]
> Note:
> 
> If different BFD profiles exist, only the profile with the lowest detection time is used.

### Using BFD for Cloud Interconnect Sites

Using BFD for Cloud Interconnect Sites is considered a best practice. Setting the BFD transmit and receive intervals has a significant impact on network conditions, intervals that are too small can cause network instability, and intervals that are too large can reduce BFD effectiveness.

The default BFD values (500 ms transmit, 500 ms receive, and a multiplier of 3) are generally optimal for BFD performance over L2 connections, but you can adjust these settings according to your site type if needed.

Each cloud provider defines a different default value. For example, AWS defines the default value for Direct Connect BFD to be 300 ms and a multiplier of 3.

### Using BFD for IPsec Sites

Using BFD for IPSec sites can dramatically improve the convergence time and the stability of your network. However, it's important to note that IPsec tunnels are internet-based connections with latency around 10-20 ms.

Therefore, too small a detection time can cause network instability, and intervals that are too large can reduce BFD effectiveness.

The default BFD values (1000 ms transmit, 1000 ms receive, and a multiplier of 5) are generally optimal for BFD performance over an internet connection, but you can adjust these settings according to your site type if needed.

> [!NOTE]
> Note:
> 
> Make sure that you have the vendor documentation for specific default values and instructions for configuring BFD.

Also, after you modify the BFD timers, make sure to disable and then enable the BFD session for the timers to be implemented. If you do not reset the BFD session, your changes are ignored.

## Configuring BFD for a site

This section explains how to define BFD settings for existing BGP peers or configure BFD for a new BGP peer.

For more about creating a new BGP neighbor, see [Defining BGP Neighbors](/v1/docs/preparing-to-implement-bgp-neighbors-with-cato).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/BFD settings multi-hop.png)

**To configure BFD settings for a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Settings > BGP**.
3. Click **New** to create a new BGP peer or edit an existing one. The **Edit BGP Neighbor** panel opens.
4. In the **Additional Settings** section, select **Enable BFD** and configure these settings:.
  1. **BFD Mode** - Select single-hop or multi-hop BFD for the site.
  2. **Transmit interval** - The interval at which BFD control packets are sent over the network.
  3. **Receive interval** - The minimum accepted interval at which BFD control packets are received over the network from the neighbor.
  4. **Multiplier** - The BFD detection time when changes in transmit and receive intervals occur.
5. Click **Apply**, and then click **Save**.

## Monitoring BFD connectivity for a site

You can monitor the status of BFD for your BGP neighbors and their events as follows:

- BFD Status - You can see the BFD status as part of the BGP settings in **Site Configuration > BGP** and click the **Show BGP Status** button. The **BFD Status** is Up or Down. **​​Note:**​​ Clicking **Show BGP Status** for Socket and vSocket sites shows the data for BFD in passive mode.

![BFD_status.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247907610269.png)
- BFD Events - In **Monitoring > Events**, you can inspect dedicated BFD events by filtering event type **Routing**, and sub-type **BFD Session**.

![BFD_Events.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247939155101.png)

You can also view the **BGP Disconnected Error Code** field, for cases when the BFD session tears down the BGP session with the **CeaseBfdDown** reason.
