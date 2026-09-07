---
title: "Hub & Spoke Off-Cloud Topology for WAN Recovery"
slug: "hub-spoke-off-cloud-topology-for-wan-recovery"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/hub-spoke-off-cloud-topology-for-wan-recovery"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Hub & Spoke Off-Cloud Topology for WAN Recovery

## Overview of WAN Recovery

[WAN Recovery](/v1/docs/socket-site-resiliency-with-wan-recovery) provides resiliency if your Socket sites cannot communicate through the Cato Cloud. It uses direct VPN tunnels between Socket sites over the Internet to preserve WAN traffic if there are significant connectivity issues with the Cato Cloud. By default, each Socket maintains tunnels with other Sockets using keepalives, ensuring fast recovery and resiliency.

By default, all Socket sites (except those in China) also form a **full mesh** of Off-Cloud tunnels, continuously exchanging reachability probes with every other site. While suitable for small and medium deployments, this behavior generates unnecessary traffic and increases CPU load in large-scale environments.

Transitioning to a **hub & spoke** design reduces the number of tunnels and probes, maintaining optimal performance and efficiency.

## Should I change my account to a hub & spoke off-cloud topology?

For accounts with hundreds or thousands of Socket sites, the default full-mesh Off-Cloud topology can result in:

- **High CPU utilization and resource consumption** on Sockets (e.g., X1500 models) from maintaining numerous site-to-site tunnels and keepalives.
- **Increased bandwidth usage** from site-to-site reachability probes, which can be especially problematic for sites with limited bandwidth or cellular links.

To ensure that these types of accounts remain scalable, efficient, and stable as they grow, they should consider moving to a hub & spoke topology.

## What are the changes to the account with the hub & spoke topology?

When the Off-Cloud topology for your account is changed from full mesh to hub & spoke, we designate the data centers or headquarters as hub sites, and the other sites as spokes.

- **Hub sites** connect to all hubs and spokes
- **Spoke sites** connect only to hubs, with this routing change:
  - Spoke specific routes are not advertised to other spoke sites

This change significantly reduces the number of site-to-site tunnels and reachability probes.

## When is the topology change applied to my account?

- Changes will be implemented during pre-arranged maintenance windows with customers
- Rollouts may occur in gradual phases, beginning with a small number of sites to validate the expected behavior

## What is the impact of changing to a hub & spoke topology?

- **Expected impact:**
  - All sites will continue to communicate through the Cato Cloud, regardless of role
  - Off-Cloud WAN Recovery will continue to function between spokes and hubs, but **not between spokes**
- **Potential worst-case impact:**
  - If hubs are not configured correctly, spokes may temporarily lose Off-Cloud WAN Recovery between them
  - **Resolution:** Identify the affected site(s) and reconfigure them as hubs

## As an account admin, what do I need to do?

1. Approach your Cato account representative and let them know that you want to change to a hub & spoke topology for WAN recovery.
2. Make sure that your data centers and headquarters sites are correctly identified in the CMA.

For more information, see [Using the CMA to Add Sites](/v1/docs/using-the-cma-to-add-sites).
3. During the pre-arranged maintenance window:
  1. Be available to confirm site connectivity
  2. Report any unexpected connectivity issues immediately
4. After the change:
  1. Verify that critical applications and inter-site connections function as expected

## What is the process to roll back to a mesh topology?

A rollback is highly unlikely, but if required, the procedure is simple and easy to perform:

- We will reset the account settings to full mesh
- Rollback can be performed during the maintenance window
