---
title: "XOps Network Playbook - PoP Reconnect to Improve Connectivity"
slug: "xops-network-playbook-pop-reconnect-to-improve-connectivity"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-pop-reconnect-to-improve-connectivity"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - PoP Reconnect to Improve Connectivity

## Overview

The socket will initiate a PoP reconnect in two specific scenarios:

1. This can occur either during routine PoP scheduled maintenance or in the rare event that it becomes unavailable.
2. When all links from the socket to the PoP fail to meet the threshold configured in [Connection SLA](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites).

## Step 1 - Starting the Site Reconnect to Improve Connectivity Investigation

Reconnected to the PoP issues can be identified through one of the following:

- Go to the **Stories Workbench** page and use the **Network XDR** preset to find the **Site reconnected to the PoP to improve connectivity** stories.

![force-reconnect-story.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/15957998324637.png)

The story provides insight about when a reconnect was initiated for a site, what the current status is, and a full timeline of the events.
- A Connectivity event that includes the following sub-event:
  - Performance issue detected, reconnected to a different service node in the Cato Cloud

![Forced_Reconnect.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/15958009939997.png)

## Step 2 - Remediation

Please follow our playbook for [Socket Site Tunnel Connectivity Troubleshooting](/v1/docs/socket-site-tunnel-connectivity-troubleshooting).

## Raising cases to Cato Support

If following this playbook has not resolved an issue, submit a [Support ticket](/v1/docs/submitting-a-support-ticket). To get the most helpful response to a request, an administrator should provide the results of the troubleshooting steps taken.
