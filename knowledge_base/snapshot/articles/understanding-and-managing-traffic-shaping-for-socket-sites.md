---
title: "Understanding and Managing Traffic Shaping for Socket Sites"
slug: "understanding-and-managing-traffic-shaping-for-socket-sites"
updated: 2026-08-13T12:17:12Z
published: 2026-08-13T12:17:12Z
canonical: "knowledge.catonetworks.com/understanding-and-managing-traffic-shaping-for-socket-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding and Managing Traffic Shaping for Socket Sites

This article explains how Cato shapes traffic for Socket sites and how to configure and monitor the capacity that applies to each site. The shaping behavior depends on the account license model.

> **Note:** This article applies to Socket sites using Socket v25 and higher.

## Overview

Cato shapes Socket site traffic according to the bandwidth capacity that applies to the site. Upstream traffic from the site is shaped by the Socket. Downstream traffic to the site is shaped by the PoP.

The account license model impacts how the site capacity is determined:

- [Enforcement Model](/v1/docs/managing-site-bandwidth-in-licenses) - Cato uses the assigned site license to shape site traffic
- [Bursting Model](/v1/docs/jan-2027-license-bursting-model) - Cato uses the configured site bandwidth limit or the configured last-mile bandwidth to shape site traffic, depending on how the site is configured

To understand which license model your account uses, see [Identifying your License Model](/v1/docs/identifying-your-license-model).

Bandwidth Management policies define how traffic is prioritized within the applicable site capacity. WAN interface limits can apply additional limits for traffic that uses a specific WAN interface.

### Understanding the Traffic Processing Order

Cato applies traffic shaping in two stages. First, Cato shapes traffic according to the capacity that applies to the site. Then, Cato applies any configured WAN interface limits for traffic that uses a specific interface.

1. Site capacity shaping - Cato first applies the shaping limit for the site. Bandwidth Management priority policies are applied within this site capacity.
2. WAN interface shaping - After site capacity shaping, Cato applies any configured WAN interface Bandwidth Management limits. These limits can further restrict traffic that leaves through a specific WAN interface.

## Traffic Shaping for the Enforcement Model

For accounts that use the Enforcement Model, Cato shapes Socket site traffic according to the assigned site license. The site license defines the bandwidth capacity for the site, and Cato distributes that capacity across the site WAN links.

For example, if a site has a 100 Mbps license, Cato uses 100 Mbps as the site capacity for traffic shaping. The capacity applies as a site total and is not a separate 100 Mbps limit for each WAN link.

For information about assigning or updating site licenses, see [Managing Site Bandwidth](https://knowledge.catonetworks.com/docs/managing-site-bandwidth-in-licenses).

## Traffic Shaping for the Bursting Model

For accounts that use the Bursting Model, most sites do not require an assigned site license. You configure the shaping limit in the site settings in the Cato Management Application (**Network > Sites >** [site name] **>** **Site Configuration > General**, under **Site Bandwidth Limits**).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Shaping - last mile bandwidth setting toggle 2.png)

The **Limit Last Mile Bandwidth** setting controls how Cato calculates the site capacity:

- When enabled, Cato shapes traffic according to the configured upstream and downstream limits
- When disabled, Cato shapes traffic according to the total configured last-mile bandwidth for the site WAN links. Disabling **Limit Last Mile Bandwidth** does not remove traffic shaping. Cato still uses the configured last-mile bandwidth as the site capacity.

The maximum upstream value cannot exceed the total configured upstream last-mile bandwidth across the site WAN links. Similarly, the maximum downstream value cannot exceed the total configured downstream last-mile bandwidth across the site WAN links.

> **Notes:**
> 
> - Changing site bandwidth limits or last-mile bandwidth can cause the site to reconnect. The CMA shows a warning when a change can impact connectivity.
> - In the Bursting Model, sites without assigned licenses can exceed committed limits and may incur additional charges.

For more information, see [Jan 2027 License Bursting Model](https://knowledge.catonetworks.com/docs/jan-2027-license-bursting-model) and [Identifying your License Model](https://knowledge.catonetworks.com/docs/identifying-your-license-model).

## Traffic Shaping for Standalone Countries

Standalone countries include China, Vietnam, and Morocco. Sites in these countries require an assigned site license, including for accounts that use the Bursting Model.

For sites in standalone countries:

- The **Limit Last Mile Bandwidth** setting is always enabled. You can’t disable this setting.
- The configured bandwidth limit cannot exceed the assigned site license.

## Configuration Guidelines for Bandwidth Management

Bandwidth Management settings define how Cato allocates the available site capacity between traffic priorities and WAN interfaces. Configure these limits in relation to the site capacity, otherwise traffic can be discarded or prioritized in a way that doesn’t match the intended policy.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Shaping - bandwidth edit panel.png)

Use these guidelines to avoid unexpected discarded traffic or unintended priority behavior:

- For percentage-based limits, do not configure a total above 100%
- For absolute values, do not configure a total above the applicable site capacity
- Avoid configuring absolute values for limits on the account-level when sites have different capacities. Try to use percentages instead.
- If you use absolute value limits, use site-level Bandwidth Management settings when different sites require different absolute limits

The applicable site capacity depends on the license model:

- For the Enforcement Model, use the assigned site license
- For the Bursting Model, use the configured **Site Bandwidth Limits** or last-mile bandwidth
- For standalone countries, use the assigned site license

If the sum of absolute priority limits is higher than the site capacity, traffic can be assigned to priorities in a way that does not match the intended allocation. For example, assigning 20 Mbps to one priority on a 10 Mbps site can prevent other priorities from receiving the expected bandwidth.

## Monitoring Site Throughput and Capacity

Use the CMA to monitor throughput, site capacity, and discarded traffic for Socket sites.

### Sites Page

The Sites page shows the **Licensed Capacity** that applies to each site. Use the capacity value to understand the site’s shaping limit and compare it with actual throughput in the Network Analytics page.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Shaping - sites page.png)

### Network Analytics

The [Network Analytics](/v1/docs/showing-the-site-network-analytics) page shows site throughput compared to the applicable site capacity. The top bar shows the licensed capacity for the site, and the throughput graphs show a dotted bandwidth limit line.

Throughput graphs show traffic that entered the tunnel after shaping. Because the graphs show traffic after shaping, sustained throughput is not expected to remain above the limit line.

The bandwidth limit line includes a 20% grace allowance above the site capacity. For example, for a 10 Mbps capacity, the dotted line appears at 12 Mbps.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Shaping - network analytics throughput.png)

## Reviewing Discarded Traffic

The Network Analytics page displays graphs that show traffic that Cato discarded before it entered the tunnel. Discarded traffic can indicate that traffic reached the applicable shaping limit.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/shaping - discards.png)

If you see discarded traffic, review these settings:

- Assigned site license for the Enforcement Model
- Site bandwidth limits for the Bursting Model
- Last-mile bandwidth configuration
- Bandwidth Management priority policies
- WAN interface Bandwidth Management limits

## Related Articles

- [Managing Site Bandwidth](https://knowledge.catonetworks.com/docs/managing-site-bandwidth-in-licenses)
- [Working with Cato License Types](https://knowledge.catonetworks.com/docs/working-with-cato-license-types)
- [Jan 2027 License Bursting Model](https://knowledge.catonetworks.com/docs/jan-2027-license-bursting-model)
- [Identifying your License Model](https://knowledge.catonetworks.com/docs/identifying-your-license-model)
- [Showing the Site Network Analytics](/v1/docs/showing-the-site-network-analytics)
