---
title: "Urgent: Update NAT Rules and IPsec Sites for Beijing_DC1 by Aug 1"
slug: "urgent-update-nat-rules-and-ipsec-sites-for-beijing-dc1-by-aug-1"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/urgent-update-nat-rules-and-ipsec-sites-for-beijing-dc1-by-aug-1"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Urgent: Update NAT Rules and IPsec Sites for Beijing_DC1 by Aug 1

As part of an urgent infrastructure change initiated by one of our upstream carriers, an IP range associated with the Beijing PoP will be decommissioned on Aug 1, 2025.

To avoid service disruptions, you must update these configurations:

- [NAT-based Network Rules](/v1/docs/configuring-network-rules#h_01JZSVB952JEDD04BQVYJET9XG)
- [IPsec site tunnel settings](/v1/docs/configuring-sites-with-ipsec-connections)

**Note:** The Beijing PoP location itself remains active, so **Route via** rules are not impacted.

Failure to update configurations by August 1, 2025, will cause outages.

**Note:** For customers who require extra allocated IPs, we will temporarily assign licenses for the allocated IPs during this transition.

## What Happens if I Don’t Make these Changes?

Starting Aug 1, 2025, any NAT rule or IPsec tunnel that still uses a decommissioned IP from the Beijing_DC1 PoP will experience connectivity loss or degraded service.

Using deprecated IPs will result in outages or degraded connectivity. There is no fallback.

## What PoP Locations are Impacted?

The Beijing_DC1 PoP location underwent these changes on Aug 1, 2025:

1. Decommission the IP range 111.206.82.0/26 **(As of Aug 10, this range is no longer available)**
2. New ranges, 111.202.125.0/25 and 106.39.250.192/26, will be available for Beijing_DC1 (there is also the existing range 101.36.65.64/26)

## What Changes Do I Need to Make to the Network Rules?

Edit rules in the [Network Rules policy](/v1/docs/configuring-network-rules) (Network > Network Rules) that egress traffic via NAT using an IP address within 111.206.82.0/26 to a new IP with a valid IP for Beijing_DC1 (within 111.202.125.0/25, 106.39.250.192/26, or 101.36.65.64/26).

1. Allocate a new IP for the Beijing_DC1 PoP from 111.202.125.0/25, 106.39.250.192/26, or 101.36.65.64/26 ([Network > IP Allocation](/v1/docs/allocating-ip-addresses-for-the-account))
2. In the Network > Network Rules page, change the NAT to an IP address from the previous step.
3. In the Network > IP Allocation page, remove the previous IP (from 111.206.82.0/26 or 106.39.250.192/26) for the Beijing DC1 PoP.

**Note:** If the rule uses **Route via**, no changes are required.

## What Changes Do I Need to Make to IPsec Sites?

For [IPsec sites](/v1/docs/ipsec-sites) configured with a Public IP from the Beijing_DC1 PoP, update the **IP** for the **Primary** and **Secondary** tunnels.

1. Allocate a new IP for the Beijing DC1 PoP from 111.202.125.0/25, 106.39.250.192/26, or 101.36.65.64/26 ([Network > IP Allocation](/v1/docs/allocating-ip-addresses-for-the-account))
2. In the Site Configuration> IPsec page, change the IP address from the previous step.
3. In the Network > IP Allocation page, remove the previous IP (from 111.206.82.0/26) for the Beijing DC1 PoP.

## Questions or Need More Information?

You must urgently take action, if you need more information, please use the [Cato Knowledge AI assistant](/v1/docs/what-is-cato-s-ask-ai-agent) in the CMA to answer your questions, including configuring NAT for Network Rules and IPsec site settings.
