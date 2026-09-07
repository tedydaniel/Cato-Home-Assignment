---
title: "XOps Network Playbook - LAN IP Conflict"
slug: "xops-network-playbook-lan-ip-conflict"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-lan-ip-conflict"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - LAN IP Conflict

This playbook describes steps to resolve issues when an IP conflict is detected.

## Overview

This playbook guides you through resolving IP conflicts that can occur due to DHCP misconfiguration, when multiple DHCP servers are active on the same network, or when static host reservations overlap with DHCP pool assignments.

## Symptoms

- Frequent disconnections
- ARP table flapping
- DHCP Lease Errors

## Step 1 - Verify the Duplicate IP event occurred

- There are multiple ways to discover that a Duplicate IP event has occurred:
  - In the Stories Workbench page, use the Network Operations preset and adjust the time frame if required. ![LANIPConflict.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32030617636125(2).png)
  - Browse to the events section and filter for connectivity events with sub-type IP Conflict. adjust the time frame if needed.

## Step 2 - Verify the DHCP Source and Overlapping

- Browse to **Network > Site > Known Hosts** and search for the devices by IP or MAC address to confirm whether the IP was assigned from the Cato Socket or another router.
  - If the IP was assigned by Cato, go to the **Networks** section and, in the **DHCP Settings** column, verify that DHCP pools are defined correctly and that they do not overlap with static hosts configured for the site.
  - If Cato DHCP is not used, check the remote router’s DHCP configuration for possible overlaps and adjust the settings if required.

## Step 3 - Resolve IP Conflict

- Locate conflicting hosts using the site’s **Known Hosts** page. Alternatively, run the `arp -a` command in the device’s command prompt to find the MAC address of conflicting hosts.
- Release the IP directly from one of the hosts using the following commands:
  - **Windows:** In the command line, run `ipconfig /release` followed by `ipconfig /renew`.
  - **macOS:** Go to **System Settings > Network > Interface Details > TCP/IP,** and click **Renew DHCP Lease**.
  - **Linux/macOS (terminal):** Run `dhclient -r` followed by `dhclient`.

## Step 4 - Renew DHCP Lease

- If the previous step did not resolve the issue, remove the relevant host entry from the site’s **Static Host Reservations** and adjust the configured DHCP lease time for the account or site.
- The lease will then be automatically reassigned on the next request.

## Raising a Ticket with Support

- If after following this playbook you are unable to rectify the issue, you may want to raise a ticket with Cato Support. When doing this, for the speediest resolution it is important that you include all insight gathered through following the above steps.

Please see [Submitting a Support Ticket](/v1/docs/submitting-a-support-ticket)
