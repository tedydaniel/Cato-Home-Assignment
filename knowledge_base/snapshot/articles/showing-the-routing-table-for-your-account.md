---
title: "Showing The Routing Table for Your Account"
slug: "showing-the-routing-table-for-your-account"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/showing-the-routing-table-for-your-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Showing The Routing Table for Your Account

This article discusses how to use the Routing Table screen to analyze the routing information for your account.

By default, the Routing Table screen shows all active and inactive routes for the account. Active routes have the best route metrics and are used for traffic forwarding, while inactive routes have less preferred metrics. For example, in a site with two BGP neighbors, the same routes are learned from both neighbors. The route with the preferred BGP metric appears as active, while the routes with a less preferred metric appear as inactive. If the primary BGP neighbor goes down, the inactive route becomes active and is used for traffic forwarding.

You can search for specific routes, subnets, site names, and SDP Users according to their IP address or name. The table is dynamically filtered as you enter the search string. You can filter the routes as follows:

- **Queried PoP** - All the Cato PoPs that are serving the account have similar routing information.
  - **Automatic** option – Routing information is queried from a random PoP
  - Manually select a specific PoP that the routing information is queried
- **Sites/SDP Users** – Select to show routes for sites, SDP Users, or for both (by default, only routes for sites are shown)

**To show the routing table:**

1. From the navigation pane, click **Network > Routing Table**.

The **Routing Table** screen opens.

![routing_table.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32021723153565(1).png)
2. To only display active routes, click the **Show all routes** slider ![toggle.png](https://support.catonetworks.com/hc/article_attachments/32021768184861).

The slider is gray when this option is disabled.

## Understanding the Routing Table Fields

This section explains the columns and fields in the Routing Table screen.

- Name – Name of the route’s origin site or SDP User.
- IP/Subnet - Host IP address or subnet CIDR notation.
- Next Hop – The next hop device IP address for this route.
  - Routes with no next hop appear as **Directly Connected**.
- Routing Type – A dynamic or a static route.
  - Static – A route that is defined statically in the CMA
  - Dynamic – A route learned from a peer device (BGP). This route is not defined in the CMA.
- Origin PoP – The connected Cato PoP that the route originates from.
- Route Last Update - The last time the route entry was updated in the local PoP routing table. This timestamp may change due to internal route processing or synchronization and does not necessarily indicate a BGP update, route flap, tunnel event, or customer configuration change.
- Details – Additional metric information for a route (if metric is displayed as **0** there is no available information for it).
  - Tunnel metric – Tunnel priority (lower value is preferred)
  - Weight – Configured BGP peer priority (lower value is preferred)
  - AS Length – AS Path length for this route (if available)
  - Metric Discriminatory – MED attribute received by external router (if available)
- Additional BGP Information – Additional information for dynamic routes (if available).
  - AS Path – Route AS Path sequence
  - Origin AS – Origin AS type for this route
  - Communities – Received BGP communities for the route
