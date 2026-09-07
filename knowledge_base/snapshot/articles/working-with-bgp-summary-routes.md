---
title: "Working with BGP Summary Routes"
slug: "working-with-bgp-summary-routes"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/working-with-bgp-summary-routes"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with BGP Summary Routes

This article explains BGP summary routes and the configuration settings, for Socket, IPsec, and Cloud Interconnect sites.

## Overview

BGP summary routes reduce the size of BGP routing tables and improve network scalability. They are commonly used to simplify routing information exchange between AS. By advertising a summary route instead of multiple unique routes, BGP peers can simplify their forwarding decisions and minimize the computational resources required for route lookup. Summary routes can enhance BGP synchronization by reducing the exchange of large amounts of routing information.

You can optionally add BGP communities to your summary routes to create specific routing policies for the included routes.

### Prerequisites for Using BGP Summary Routes

- For Socket sites, BGP summary routes are supported on Sockets v19.x and higher
- The CIDR range for a BGP summary route must be between /8 and /30

## Understanding BGP Summary Routes

BGP summary routes help to reduce BGP overhead and routing table size by minimizing the number of advertised BGP entries over the network. A summary route is advertised as long as at least one of its more specific routes exists in the Socket or PoP's routing table. If this condition is not met, the summary route is withdrawn.

The example below shows the difference between a site in which route prefixes are advertised with or without BGP route summarization.

**Without summary routes:** When the Socket advertises route prefixes to its neighbor via BGP, it is configured to advertise **All Routes** - Meaning five unique route prefixes are advertised.

![BGP_without_Summary.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25085191591325.jpeg)

**With summary routes:** The Socket advertises a single Summary Route to its neighbor via BGP. The summary routes aggregate all five unique routes and advertise them as a single route prefix.

![BGP_with_Summary.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25085191736605.jpeg)

### BGP Summary Routes Use Cases

- **Overcoming hardcoded limitations for a number of received BGP routes** - Some Cloud Providers impose limitations on the amount of route prefixes they can receive. AWS, Microsoft Azure, and other cloud providers limit the number of route prefixes in their environment. For example, the Azure limit is to receive only up to 1000 routes. A BGP summary route can be used to overcome this limitation by minimizing the total amount of advertised route prefixes.
- **Network BGP routing simplification** - BGP summary routes can reduce BGP overhead where many routes are advertised across large networks. Replacing many unique route prefix advertisements with a summary route also allows for a simplification of the routes in your account for better management and monitoring of BGP traffic.

## Configuring BGP Summary Routes

Configure BGP summary routes to existing BGP peers or create new BGP peers.

This section explains how to edit existing BGP neighbors and add a summary route. For more about creating a new BGP neighbor, see [Defining BGP Neighbors](/v1/docs/preparing-to-implement-bgp-neighbors-with-cato).

These are the limits for BGP summary routes, you can configure up to:

- 256 summary routes per BGP peer
- 5 communities per summary route

> [!NOTE]
> Note:
> 
> Modifying the BGP advertisement configuration, such as BGP summary routes, causes a hard BGP peer reset which can impact end user experience.

**Advertising BGP Summary Routes**

For configurations where you are only advertising BGP summary routes (**Summary routes** is the only option selected for the BGP neighbor), the Cato SDP user range is not advertised by default. The default Cato system IP range 10.254.254.0/24 (or custom system range) is also advertised.

You can manually configure the BGP neighbor to include this IP range as a summary route:

- SDP user IP range: 10.41.0.0/16 (or custom SDP user range)

![Edit_BGP_Summary_Route.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25085191865501.png)

**To configure BGP Summary Routes for a BGP neighbor:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Settings > BGP**.
3. Click **New** to create a new BGP peer or edit an existing one. The **Edit BGP Neighbor** panel opens.
4. In the **Policy** section, select **Summary routes**. The Summary Route table opens.

**Note:** We recommend that you do not select both **All routes** or **Summary routes**. Selecting both options will advertise both the configured summary routes and all the unique routes over the network. This will cause BGP to advertise an excessive number of routes and reduce the efficiency of summary routes.
5. Click **New** and add BGP Summary Routes in CIDR notation.
  1. (**Optional**) Click the ![Add_Icon_CMA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25085191957789.png) icon and **Add** to define BGP communities for a summary route. BGP communities have to be in a format of **ASN:community** 1-65535:1-65535. For more information, see [Cato Reserved BGP Communities](/v1/docs/cato-reserved-bgp-communities).
6. Click **Apply**.

## Monitoring BGP Summary Routes

You can monitor and verify the status of your BGP Summary Routes with any of the following options:

- **Show BGP Status** - You can select this option in **Site Configuration** > **BGP** to show the status of BGP for your site and its current advertisements over the network.
- **Cato Management Applications Events** - Inspect BGP related events. You can see the different types of BGP events in [Defining BGP Neighbors](/v1/docs/preparing-to-implement-bgp-neighbors-with-cato).
- **Routing Table** - All routes, including dynamic summary routes, are visible in the Routing Table. The routing table includes information on summary route IPs such as the source site, last route update, AS path, and more.
