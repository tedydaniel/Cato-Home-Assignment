---
title: "XOps Network Playbook - LAN Monitoring Host Unreachable"
slug: "xops-network-playbook-lan-monitoring-host-unreachable"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-lan-monitoring-host-unreachable"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - LAN Monitoring Host Unreachable

This playbook describes steps to resolve issues when LAN Monitoring is configured and the Cato Cloud can't reach a host behind a site.

## Overview

The LAN Monitoring feature lets you define hosts behind a site by their IP address, and the Fault Threshold for the host (the maximum number of consecutive failed ICMP tests). A PoP in the Cato Cloud sends ICMP tests to the host, if the host fails to respond to the specified number of ICMP tests, it is considered down, and an event is automatically generated. You can also choose to send an email notification when a host is unreachable.

When the connectivity between the host and the PoP is restored, a new event is generated that the host is reachable.

For more information, see [Working with LAN Monitoring for a Site](/v1/docs/configuring-lan-monitoring-for-a-site).

The following are the different ways that a Cato Management Application admin can verify that a monitored host has become unreachable to the monitoring PoP:

- Go to the **Stories Workbench** page and use the **Network XDR** preset to find the **LAN monitoring host unreachable** stories.

![lanmonpic.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19330623057821.png)

The story provides information on the current status of the site, an incident timeline, and more.
- LAN Monitoring event with the action **Host Unreachable**
  - Use the **LAN hosts unreachable** preset filter and adjust the time frame if necessary
- LAN Monitoring email notification
  - When email notifications are enabled for a LAN Monitoring rule, emails are sent to the mailing list (can include non-admins)

When responding to Site Operations stories it is important to approach the problem by first verifying the problem is ongoing, then troubleshooting the problem and finally verifying the problem is resolved.

## Step 1 - Verifying the Host is Unreachable

This section discusses different Cato tools that you can use to verify the reason that the host is unreachable.

### Using LAN Monitoring Events Preset

Using the LAN Monitoring preset Events filter allows us to check the last event related to the host in question. If this event is not followed by an event noting the connectivity has returned, this suggests the host is still unreachable.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19330623063581.png)

### Viewing Story for Current Status

The Story itself can also be used to determine the continuing unreachability of a host. The current status of the story is listed on the Dashboard. A story status of Open shows that this event is still on-going.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19330623068573.png)

## Step 2 - Troubleshooting the Host Connectivity

This section discusses tools within Cato that can be used to follow a structured troubleshooting approach to this kind of incident. These steps should be followed generally in order but the results of these checks may determine what the next step might be.

### Reviewing Changes in the Audit Trail

Review changes in the [Audit Trail page](/v1/docs/using-the-audit-trail) for the Cato Management Application, and see if there is a configuration that is related to this issue. If any configuration directly led to the change in host status, consider reverting the change.

### Known Hosts

The Known Hosts page in the CMA (Network > Sites > {site name} > Site Monitoring > Known Hosts) can be used to gather information on individual end points seen within a site. This information includes how long ago the last packets were seen that were sourced from that host.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19330623072925.png)

Typically a monitored hosts responding to ICMP packets as part of LAN Monitoring will always be refreshing this timer. An example like above suggests the timing of the host's reachability being lost. This may provide additional context. Does this time window match any expected maintenance windows or power events that may have affected host connectivity, or networking changes in the local environment, for instance.

### Using Socket WebUI Tools

You can use the Socket WebUI to ping the host from the LAN interface. For more information, see [Using the Socket WebUI Tools](/v1/docs/using-the-socket-webui-tools).

- From the Socket WebUI, ping the host with these settings:

If there is no response to the ping, the issue might be related to routing, or the host might be generally unreachable, powered down or not configured to respond to pings, for example.

![pingfail.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19330606808861.png)
  - **Route via** - LAN
  - **Hostname/IP** - IP address of the unreachable host
- 
  - Using the Socket WebUI tools, take a PCAP of the LAN interface while a ping to the host in question is ongoing. See if there is bi-directional ping between the socket and the host. ![arpfailcap.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19330606820253.png)The above example shows that there is no response from the socket when ARPing for the physical address of the host in question. This implies that the host is on the same local network as the socket LAN, but that the host is not responding at layer 2. For this result, verify that the host is powered on and ready to respond to ARP requests. ![icmpfailcap.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19330606827165.png)The above example shows both the socket and the PoP's original LAN Monitoring configured ICMP requests to the monitored host. Note the source address of 10.254.254.1 and the time delta (10 seconds) between ICMP LAN monitoring requests sent by the PoP. The fact that the ICMP request is sent shows that the MAC address of either the next hop or the end host is being utilised to send these requests. Verify if this MAC address suggests that the monitored host exists behind a layer 3 boundary, or is local to the socket's LAN network.
  - If the monitored host is behind a layer 3 boundary, begin investigating how the ICMP requests are handled at that hop. If the ICMP response from the host is reaching that layer 3 boundary device, it is likely a routing issue at that layer 3 boundary.
  - If the monitored host is within the socket's LAN network, it is likely the device is powered down or is otherwise not configured or able to respond to ICMP.

## Step 3 - Verifying that the Host is Reachable

After you remediate the issue with the host, verify that it is reachable and has connectivity to the Cato Cloud.

### Viewing the Host in the Known Hosts Page

From the Known Hosts page, show the host and verify that the **Last Host Activity** is showing data for the current time.

### Pinging the Host from the Socket WebUI

Use the Socket WebUI to ping the host, using the LAN interface to verify that the host has connectivity to the site.

### Reviewing the Host Reachable Event

After the connectivity between the host and the Cato Cloud is restored, a Host Reachable event is generated. You can manually configure the event filter for **Action** IS **Host Reachable** to show the event.

## Raising Cases with Cato Support

If after following this playbook you are unable to rectify the issue, you may want to raise a ticket with Cato Support. When doing this, for the speediest resolution it is important that you include all insight gathered through following the above steps.

Please see [Submitting a Support Ticket](/v1/docs/submitting-a-support-ticket)
