---
title: "XOps Network Playbook - Link Down"
slug: "xops-network-playbook-link-down"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-link-down"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - Link Down

This playbook describes steps to resolve Partially Disconnected alerts that are triggered when your site is still up, but one of the WAN links is currently down.

## Overview

This playbook is designed to walk you through a story in which your site is still online with the Cato Cloud, but one of the WAN links is disconnected or offline.

It applies to either of these scenarios

- A Socket WAN link is down
- An IPsec WAN link is down

## A Socket Link is Down

The following section should be used to resolve a scenario where a Socket link is down. There are two scenarios where a link is considered down:

- The port is up, but the tunnel is disconnected
- The port is down

For an IPSec configuration, see [below](/v1/docs/xops-network-playbook-link-down#an-ipsec-link-is-down).

### Step 1 - Verifying that the Socket Link is Down

There are multiple ways to discover that a Link Down issue has occurred:

- A story in the Stories Workbench.
  - Use the **Network Operations** preset filter and adjust the time frame if necessary. The story provides information about the investigation, such as if the port is down or up, access to the Socket WebUI, and more.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19343449206045.png)

- Connectivity events, with the Disconnected or Passive Disconnected sub-type
- A port is showing as down ![socket_port-status.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/15935917969437.png)

### Step 2 - Troubleshooting the Socket Link Down Status

Please follow our playbook for [Socket Site Tunnel Connectivity Troubleshooting](/v1/docs/socket-site-tunnel-connectivity-troubleshooting).

## An IPSec Link is Down

The following section should be used to resolve a scenario where an IPSec link is down.

### Step 1 - Verifying that the IPSec Link is Down

There are multiple ways to start your investigation when you suspect that an IPSec link is down.

- A story in the Stories Workbench.
  - Use the **Network Operations** preset filter and adjust the time frame if necessary.
- Connectivity events, with the Disconnected or Passive Disconnected sub-type.
- A site is showing as disconnected.
- Connectivity Status button in Network > Sites > IPsec ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19377627936157.png)

### Step 2 - Troubleshooting the IPSec Link Down Status

Please follow our playbook for [IPsec Site Connectivity Troubleshooting](/v1/docs/ipsec-site-connectivity-troubleshooting).

## Raising a Ticket with Support

If after following this playbook you are unable to rectify the issue, you may want to raise a ticket with Cato Support. When doing this, for the speediest resolution it is important that you include all insight gathered through following the above steps.

Please see [Submitting a Support Ticket](/v1/docs/submitting-a-support-ticket)
