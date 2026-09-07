---
title: "XOps Network Playbook - BGP Session Disconnected"
slug: "xops-network-playbook-bgp-session-disconnected"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-bgp-session-disconnected"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - BGP Session Disconnected

This playbook describes steps to resolve issues when a BGP session disconnects for a site.

## Overview

When a BGP session is disconnected, the connection between two BGP routers is terminated and can disrupt the exchange of routing information. The impact of the disconnected session can vary depending on the network's redundancy and failover mechanisms. In scenarios where alternate paths exist, the impact may be minimal. However, in less resilient setups, disconnections can lead to temporary routing issues and service disruptions.

For more information on BGP, please see [Using BGP in the Cato Cloud.](/v1/docs/using-bgp-in-the-cato-cloud)

There are different ways to discover that a BGP session has disconnected for a site:

- Go to the **Stories Workbench** page and use the **Network XDR** preset to find the **BGP session disconnected** stories.

![bgpwprkbench.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19330565429661.png)

The story provides information about the incident timeline, current Socket status, and more.
- A Routing event, with the BGP Session sub-Type with the action **Disconnected**
  - Use the **BGP peers disconnected** preset filter and adjust the time frame if necessary

- BGP email notification
  - When email notifications are enabled for a [BGP peer](/v1/docs/preparing-to-implement-bgp-neighbors-with-cato), emails are sent to the mailing list (can include non-admins)

When responding to Site Operations stories it is important to approach the problem by first verifying the problem is ongoing, then troubleshooting the problem and finally verifying the problem is resolved.

## Step 1 - Verifying that the BGP Session is Disconnected

This section discusses different Cato tools that you can use to verify that the BGP session for a site is disconnected, and what might be the root cause.

### Showing the BGP Status

Use the Cato Management Application to show the real-time status of the BGP session. In the BGP page for the site (Network > Sites > {site name} > Site Configuration > BGP), click **Show BGP Status**.

This is an example of the status for a disconnected BGP session:

![bgpstatus.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19330599344029.png)

### Showing BGP routes

Use the Cato Management Application to view the account routing table (Monitoring > Routing Table). You can filter for the site name in question.

The below example shows that no DYNAMIC routes are included in the route table, implying no routes are being learnt from BGP peers:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19330599348125.png)

### Verifying the BGP Disconnected Status for Cloud Interconnect Sites

For Cloud Interconnect sites, BGP is used for connectivity between the cloud environment underlay and the PoPs.

- In the Cloud Interconnect page for the site (Network > Sites > {site name} > Site Configuration > Cloud Interconnect), click **Test Connectivity** to show the BGP status of the underlay
- In the Sites page, review the status of the site

## Step 2 - Troubleshooting the BGP Disconnected Status

This section discusses tools within Cato that can be used to follow a structured troubleshooting approach to this kind of incident. These steps should be followed generally in order but the results of these checks may determine what the next step might be.

### Clarify BGP Session Disconnection Reason

The Cato Management Application's Events page (Home > Events) can be used to clarify the reason the BGP session disconnected.

Using the preset **BGP peers disconnected** you can see a history of all disconnected BGP sessions within your selected timeframe. These events also have an associated BGP Disconnect Error Code, which can clarify the reason for the disconnection:

![bgpdisconnreason.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19330599355165.png)

### Ensure No Changes Have Proceeded This Incident

Review changes in the [Audit Trail page](/v1/docs/using-the-audit-trail) for the Cato Management Application, and see if there is a configuration that is related to this issue. If a configuration change directly preceded this incident, consider reverting it and confirming what the configuration should be.

### Verify the BGP Configuration Is Correct

Use the Cato Management Application to show the real-time status of the BGP session. In the BGP page for the site (Network > Sites > {site name} > Site Configuration > BGP), click **Show BGP Status,** and then **Raw Status**. This detailed status also lists the configuration parameters. These should be checked to ensure the correct configuration is being applied.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19330599359773.png)

### Soft Resetting the Configuration

Once you verify the standby BGP neighbor is disconnected, you can change one of the [BGP neighbors](/v1/docs/preparing-to-implement-bgp-neighbors-with-cato) and click **Save**. This pushes a new configuration which can resolve the issue. Then restore the original settings and save the original configuration.

### Check that BGP Protocol Traffic is Bi-directional Between Peers

In order for a BGP session to establish and function there must be bi-directional traffic on BGP TCP port 179. Using Cato packet captures the bi-directionality of this traffic can be investigated and verified.

For socket sites, take a packet capture (PCAP) on the Socket LAN interface (the port used for BGP traffic). For more information, see [How to Take a Packet Capture on a Socket](/v1/docs/how-to-capture-traffic-on-a-socket).

- Filter the PCAP for port 179. If the traffic is bi-directional ensure the TCP 3-way handshake is completing successfully.
- If the handshake is being completed successfully but the session is still not established it is likely that an error is being reported by one of the peers. These errors should be visible on the packet capture. Errors reported should be BGP standard errors and thus can be further examined by checking BGP error documentation.
- If the traffic is only one way, sourced from the socket but not returned by the peer, continue to the next section to investigate layer 3 reachability.

For IPSEC sites, please refer to packet capture steps highlighted in the [IPsec Site Connectivity Troubleshooting](/v1/docs/ipsec-site-connectivity-troubleshooting) Playbook.

### Check Layer 3 Reachability to Peer

Use the [Known Hosts](/v1/docs/showing-known-hosts-for-a-site) page for the site to review the most recent time there was activity for a host. This provides more information about the timing of connectivity issues and the BGP session.

#### Pinging the BGP peer to test reachability

For socket sites you can use the Socket WebUI to ping the BGP peer from the LAN interface, make sure that the BGP peer allows ICMP traffic. For more information, see [Using the Socket WebUI Tools](/v1/docs/using-the-socket-webui-tools).

- From the Socket WebUI, ping the host with these settings:
  - **Route via** - LAN
  - **Hostname/IP** - IP address of the BGP peer
  - Fails - The BGP router is not reachable, the issue isn't related to the Cato Cloud
  - Succeeds - There is an issue between the PoP and the BGP router

These are example conclusions based on the ping results:

For BGP over IPSEC sites you can follow the procedure outlined in [Troubleshooting IPsec Connectivity](/v1/docs/troubleshooting-ipsec-connectivity) in order to get packet captures. A valid source for the ping is any host across the WAN that should be able to reach the BGP peer's address via ICMP.

## Step 3 - Verifying that the BGP Disconnected Status is resolved

### Showing the BGP Session Established Event

After the BGP neighbor is connected to the site, a BGP Session event is generated with the Action **Established**. In the Events page, you can manually configure the event filter for **Action** IS **Established** to show the event.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19330565462685.png)

### Testing the BGP Status

The real-time status of the BGP session shows the routing status and information. In the BGP page for the site (Network > Sites > {site name} > Site Configuration > BGP), click **Show BGP Status**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19330565471773.png)

### Ensuring all prefixes received

Use the Cato Management Application to view the account routing table (Monitoring > Routing Table). You can filter for the site name in question.

The below example shows that the expected DYNAMIC route is included in the route table, implying that intended routes are being learned from BGP peer:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19330565486237.png)

## Raising Cases with Cato Support

If after following this playbook you are unable to rectify the issue, you may want to raise a ticket with Cato Support. When doing this, for the speediest resolution it is important that you include all insight gathered through following the above steps.

Please see [Submitting a Support Ticket](/v1/docs/submitting-a-support-ticket)
