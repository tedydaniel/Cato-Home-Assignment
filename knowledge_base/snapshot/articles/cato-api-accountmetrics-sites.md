---
title: "Cato API - AccountMetrics > Sites"
slug: "cato-api-accountmetrics-sites"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/cato-api-accountmetrics-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato API - AccountMetrics > Sites

## AccountMetrics > Sites

The SiteMetrics field contains data related to one or more sites in the account. You can also specify data for VPN users with their IDs.

## SiteMetrics Fields

The SiteMetrics field contains data for sites and their links. Use the IDs argument to specify which sites are included in the query.

These are the details for the SiteMetrics fields for a query:

- id - site or VPN user ID or array of IDs
- interfaceMetric - analytics that are returned for the links for a site (array with nested queries and fields)
- metrics - traffic metrics and data for sites (array with nested fields)
- name - site names
- SiteInfo - shows general information about the site (array with nested fields)

## ID

Shows the unique internal ID for the site or VPN user.

## Interfaces

The InterfaceMetrics field shows link data for a site. For more about InterfaceMetrics see [Cato API - AccountMetrics > Sites > Interfaces](/v1/docs/cato-api-accountmetrics-sites-interfaces).

## Metrics (Site)

The SiteMetrics field shows the traffic analytics for the site. These are the site data that you can see:

- duration - total amount of time for the site data
- granularity - duration in seconds for a single metrics bucket
- bytesDownstream - total downstream traffic (from the Cato Cloud to the site)
- bytesUpstream - total upstream traffic (from the site to the Cato Cloud)
- bytesTotal - total traffic for the site
- lostDownstream - number of packets lost for downstream traffic
- lostDownstreamPcnt - percent of packet loss for downstream traffic
- lostUpstream - number of packets lost for upstream traffic
- lostUpstreamPcnt - percent of packet loss for upstream traffic
- packetsDownstream - total downstream packets
- packetsUpstream - total upstream packets
- jitterUptstream - jitter for upstream traffic (difference in time delay in milliseconds (ms) between data packets)
- jitterDownstream - jitter for downstream traffic (difference in time delay in milliseconds (ms) between data packets)
- packetsDiscardedDownstream - total packets discarded for downstream traffic
- packetsDiscardedUpstream - total packets discarded for upstream traffic
- RTT - round-trip time from the site to the Cato Cloud

toRate Argument

When the boolean argument toRate is set to **true**, then the data is returned as per second. When the argument is set to false, then the query returns the data over the entire time period.

The toRate argument only applies to types with data in bytes, it doesn't apply to rtt, health, and so on.

## Name

Name of the site or VPN user in the Cato Management Application.

## Info

The SiteInfo fields show data about sites similar to the **Site > General** window in the Cato Management Application. For more about SiteInfo, see [Cato API - AccountMetrics > Sites > SiteInfo](/v1/docs/cato-api-accountmetrics-sites-siteinfo).

## SiteMetrics siteIDs Argument

Enter the site and VPN users IDs for the data that the query returns. If you leave the siteIDs argument blank, the query returns all the sites and VPN users in the account.

The ids argument, is a legacy argument and is no longer necessary.
