---
title: "Upcoming Deprecation of Denmark Localized IP Range in Stockholm PoP on Dec. 8, 2024"
slug: "upcoming-deprecation-denmark-localized-ip-range-stockholm-pop-dec-8-2024"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/upcoming-deprecation-denmark-localized-ip-range-stockholm-pop-dec-8-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upcoming Deprecation of Denmark Localized IP Range in Stockholm PoP on Dec. 8, 2024

Some settings in your account use Cato IP addresses that are localized for Denmark and serviced through the Stockholm PoP. As of Dec 8, 2024, this geo-localized IP range will be deprecated and no longer available. Over two years ago, we improved the Cato Cloud platform with a PoP located in Copenhagen, Denmark. You can use Copenhagen PoP IPs to achieve the same geo-localized experience for Denmark with improved performance. To avoid any potential service disruptions, you need to change the relevant Network Rules and site settings to stop using the Denmark localized IP range (209.206.17.128/25) and use a different IP range.

These configurations are impacted by the upcoming deprecation of the Denmark localized IP range (209.206.17.128/25) in the Stockholm PoP:

- Network Rules
- IPsec sites - the **Public IP** for the Primary and/or Secondary tunnel
- Remote Port Forwarding rules - the **External IP**

Use the [IP Allocation page](/v1/docs/allocating-ip-addresses-for-the-account), to assign an IP from the Copenhagen PoP to your account.

## What Geo-Localized IPs are Being Deprecated?

This is the geo-localized IP range being deprecated as of Dec. 8, 2024:

| **IP Location** | **IP Range** | **Serviced Through** |
| --- | --- | --- |
| Denmark | 209.206.17.128 - 209.206.17.254 | Stockholm |

## What Changes Do I Need to Make to the Network Rules?

Update the rules in the [Network Rules policy](/v1/docs/configuring-network-rules) (Network > Network Rules), so that they use IP addresses associated with the Copenhagen PoP.

## What Changes Do I Need to Make to the IPsec Sites?

Edit the [**Public IP**](/v1/docs/configuring-ipsec-ikev2-sites) for the **Primary** and **Secondary** tunnel for the [IPsec site](/v1/docs/ipsec-sites) (Network > Sites > {site name} > Site Configuration > IPsec), and use IP addresses associated with the Copenhagen PoP.

## What Changes Do I Need to Make to the Remote Port Forwarding Rules?

For rules in the [Remote Port Forwarding policy](/v1/docs/configuring-remote-port-forwarding-for-the-account) (Network > Remote Port Forwarding) that define the **External IP** as an address that belongs to the impacted Stockholm range, edit the rules to use an IP in the Copenhagen PoP. For more information about Cato IP ranges, see the [Production PoP Guide](/v1/docs/production-pop-guide).

## What Happens If I Don’t Make these Changes?

After Dec 8, 2024, if any of the settings above are configured to use the Denmark localized IP range in the Stockholm PoP, then there can be connectivity and service issues for traffic relevant to the Network Rules, IPsec sites, or Remote Port Forwarding rules.

## Who Do I Talk to If I Have Questions?

Please contact your authorized Cato representative.

## Who Do I Talk to If I Have Technical Issues?

Please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).
