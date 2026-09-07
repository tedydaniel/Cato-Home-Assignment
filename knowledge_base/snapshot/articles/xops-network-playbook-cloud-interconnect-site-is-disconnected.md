---
title: "XOps Network Playbook - Cloud Interconnect Site is Disconnected"
slug: "xops-network-playbook-cloud-interconnect-site-is-disconnected"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-cloud-interconnect-site-is-disconnected"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - Cloud Interconnect Site is Disconnected

This playbook describes steps to resolve issues when your site is completely disconnected.

## Overview

Cato continuously monitors a site's status. In specific scenarios, a site may become disconnected if all WAN links are down.

## Step 1 - Verifying that the Site is Disconnected

- Browse to Home > Stories Workbench page and use the Network Operations Preset to find the Site down stories. The preset will show stories that are currently not closed and not muted.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28046786806429.jpeg)
- Browse to Home > Events and search for Connectivity events, with the Disconnected subtype.

## Step 2- Troubleshooting the Site Disconnected Status

### The site is down due to a disconnected BGP session

- Go to Network > Sites > {site name} > Site configuration > Cloud Interconnect, and make sure the error is only present for connectivity and BGP, not for the Cloud Provider or Fabric Service Provider.
- Click on "Test Connection" and confirm that the response is "Failed."
- Proceed to the [Troubleshooting the BGP Disconnected Status](/v1/docs/xops-network-playbook-bgp-session-disconnected#step-2-troubleshooting-the-bgp-disconnected-status) section in the [BGP Session Disconnected](/v1/docs/xops-network-playbook-bgp-session-disconnected) playbook for further troubleshooting.

### The site is down due to no connectivity to the Fabric Service Provider

- In the cloud platform, verify that the configuration is correct and check the provision status. If configuration changes resulted in a shift in the BGP IPs or a new service key, proceed to apply the changes on the Cato side.

**Note:** Depending on the chosen fabric provider, some connections might include a cloud provider in the connectivity column.

## Raising cases to Cato Support

If, after following this playbook, you are still unable to resolve the issue, you may want to raise a ticket with Cato Support. When doing this, for the fastest resolution, it is essential that you include all insight gathered through following the above steps.

Please see [Submitting a Support Ticket.](/v1/docs/submitting-a-support-ticket)
