---
title: "Product Update - December 2, 2024"
slug: "product-update-december-2-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-december-2-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - December 2, 2024

- **New Rule-Based Policy to Manage Allocating IPs for Clients:** The [IP Allocation policy](/v1/docs/ip-allocation-policy-for-remote-users) lets you manage the IP ranges that are assigned to Clients when the device connects to the Cato Cloud. The new policy introduces several improvements, including:
  - Ability to modify the policy in parallel by [multiple admins](/v1/docs/working-with-policy-revisions)
  - An ordered rulebase to dynamically assign IP ranges to Clients
  - [API support](https://api.catonetworks.com/documentation/#mutation-container.ipAddressRange.addValues) for managing the IP Allocation policy
  - Click [here](https://academy.catonetworks.com/dynamic-ip-allocation-policy-for-remote-users) to watch a video recording of this feature

- **Off Cloud CMA Enhancements:**
  - **Improved Visibility for WAN Off Cloud Traffic:** We added a new status that indicates if off cloud traffic is enabled for WAN links in the [Site Configuration > Socket page](/v1/docs/working-with-socket-sites)
  - **View Real-Time Status for Off Cloud Tunnels:** The Off Cloud page shows which Socket sites have established off cloud tunnels with other sites, so you can review [WAN resiliency](/v1/docs/socket-site-resiliency-with-wan-recovery) for your account
