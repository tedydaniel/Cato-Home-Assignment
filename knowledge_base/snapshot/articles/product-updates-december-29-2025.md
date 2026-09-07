---
title: "Product Updates - December 29, 2025"
slug: "product-updates-december-29-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-december-29-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - December 29, 2025

## New Features & Enhancements

- **ILMM Webhooks Now Use Zendesk Token Authentication:** To align with [Zendesk's deprecation](https://support.zendesk.com/hc/en-us/articles/8843683464346-Important-update-Password-access-for-APIs-will-soon-be-removed) of password-based API access, we are updating ILMM webhook configurations to use Zendesk token-based authentication.
  - Impacts ILMM customers only

## In Case You Missed It

Take a look at this previously released feature:

- **AI-Driven Insights Improve your Security Posture**: [Autonomous Policies](/v1/docs/understanding-cato-autonomous-policies) use AI-driven insights to continuously analyze real network behavior and help optimize security policies. The engine identifies opportunities to tighten, clean up, or refine policies so they better align with actual usage based on Cato’s visibility of network data. This strengthens your security posture while reducing manual effort for SOC teams who spend less time reviewing rules manually and more time focusing on real security risk.
  - AI-driven insights are available in the [Internet](/v1/docs/what-is-the-cato-internet-firewall) and [WAN](/v1/docs/what-is-the-cato-wan-firewall) Firewalls, [Remote Port Forwarding](/v1/docs/configuring-remote-port-forwarding-for-the-account), and [TLS Inspection](/v1/docs/using-the-tls-inspection-configuration-wizard) Policies
- **Access Policies Based on Public Source IP**: Enable location-aware access control and compliance with IP-based ACLs by using the public ISP IP address of remote users for Access policies.
  - The [IP Allocation Policy](/v1/docs/ip-allocation-policy-for-remote-users) lets you dynamically assign IP addresses to remote users based on where they connect from
  - In the [Client Connectivity Policy](/v1/docs/what-is-the-client-connectivity-policy), you can use public ISP IP ranges as a condition to allow or block access to resources
