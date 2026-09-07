---
title: "XOps Network Playbook - HA Status Is Not Ready"
slug: "xops-network-playbook-ha-status-is-not-ready"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-ha-status-is-not-ready"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - HA Status Is Not Ready

## Overview

This playbook describes steps to resolve issues when the "Socket HA Status is Not Ready" status is seen on your HA site.

For sites with Socket High Availability (HA) configurations, there can be scenarios where the site status is Not Ready for HA. This means that the redundancy and failover mechanisms in place will not function as expected, resulting in possible issues if the primary Socket needs to fail over to the secondary Socket.

Below are some scenarios that you can use to help identify and resolve issues related to the Socket HA status is Not Ready:

- Socket is disconnected from Cato
- Incompatible Socket versions (Socket HA)
- Socket HA keepalive failure

## Step 1 - Verifying that HA Status is Not Ready

This section discusses different Cato tools that you can use to verify that the Socket in an HA configuration is down or disconnected from the Cato Cloud.

- When the Cato Cloud identifies one of the Sockets in the Socket HA setup is down, stories are generated in the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19329056134685.png)
- To verify, navigate the affected Site to Network > Site > Site Configuration > Socket. The example below shows that the Compatible Version is not ready and that each Socket is running a different major version. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19329022088861.png)

## Step 2 - Troubleshooting HA Status Issues

Please follow our playbook for [Socket HA Status Troubleshooting](/v1/docs/socket-ha-status-troubleshooting).

## Raising cases to Cato Support

If following this playbook has not resolved an issue, submit a [Support ticket](/v1/docs/submitting-a-support-ticket). To get the most helpful response to a request, an administrator should provide the results of the troubleshooting steps taken.
