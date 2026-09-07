---
title: "Working with BGP Filtering"
slug: "working-with-bgp-filtering"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/working-with-bgp-filtering"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with BGP Filtering

This article explains how to determine which BGP routes to accept or block using BGP filtering.

## Overview

BGP Ingress Route Filters let you control which routes are accepted or dropped when received from a BGP neighbor traversing traffic to the Cato cloud. This is important for maintaining network stability, security, and performance.

BGP filtering can be used to gradually migrate your environment to Cato by limiting the routes that you are accepting. In addition, you can use BGP filtering to block routes that are known to be used by malicious actors.

Cato supports the following methods for BGP filtering:

- Access Control Lists
  - Exact match
  - Exact and Inclusive
- Communities

> [!NOTE]
> Notes:
> 
> - BGP filtering is available for all site types (Socket sites require Socket v21.1 and higher)
> - Editing BGP filters triggers an immediate BGP session reset
> - BGP Inbound Filters support up to 500 different CIDRs

### Exact Match

You can use Exact match to filter incoming BGP routes based on the source network CIDR.

![bgp-filtering_exact.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27469679486365.png)

For example, you can create a rule that only accepts routes from an exact subnet, e.g. 192.168.1.0/24. The filter will only accept routes that are an exact match, but won't accept routes from subnets like 192.168.1.0/30.

### Exact and Inclusive

Similar to Exact, you can use prefix lists to accept routes that are included not only in the exact CIDR you define, but also its subnets.

![bgp-filtering_inclusive.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27469749584285.png)

For example, you can create a rule that accepts routes from a subnet, e.g. 192.168.1.0/24, but also includes subnets from the /24 to /27 range. The filter accepts routes that are an exact match and also routes from the subnets 192.168.1.0/25 or 192.168.1.0/27.

### Communities

BGP communities are used to tag routes with an attribute, which gives you more control over routing policies. While the community attribute is optional, when used, it lets you group routes and create filtering policies based on these groupings.

![bgp-filtering_community.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27469733430301.png)

For example, create a rule that blocks all routes with the community tag 123. Make sure to tag the BGP routes themselves with the community attribute.

### Use Case - Gradually Migrate your Environment

Company ABC is currently migrating its environment to the Cato Cloud. As part of that migration, it wants to gradually introduce advertised routes to specific peers without causing disruptions.

Using both community-based filtering and ACLs, ABC can build a rulebase that accepts or blocks routes based on predetermined criteria, and then adjust those rules as the situation calls for change.

## Configuring BGP for a site

This section explains how to define BGP filtering settings when defining a BGP peer. For full instructions about defining a BGP peer, see [Configuring BGP Neighbors for a Cato Socket](/v1/docs/configuring-bgp-neighbors-for-a-cato-socket).

**To configure BGP filtering settings for a site:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Settings > BGP**.
3. Click **New** to create a new BGP peer or edit an existing one. The **Edit BGP Neighbor** panel opens.
4. In the **Policy** section, under **Accept** determine whether to filter routes and how:
  - **Drop all** - All BGP routes are dropped, meaning no filtering is applied
  - **Accept all** - All BGP routes are accepted, meaning no filtering is applied
  - **Accept List** - Create a rulebase for which routes to accept. Any routes that are not specified are dropped.
  - **Drop List** - Create a rulebase for which routes to drop. Any routes that are not specified, are accepted.
5. If you selected **Accept List** or **Drop List**, click **New** to define which routes to accept or drop, respectively.
  1. Determine the **Match** criteria
  2. Select the **Condition**

If you select **Routes**, the condition can be either **Exact** or **Exact and Inclusive**. If you select Communities, the condition is only **Exact**.
  3. Under **Values**, select **Global** or **Custom**.
    - Global IP Range - a global object that was created in your [IP ranges](/v1/docs/using-ip-ranges-in-policies)
    - Custom IP Range - Define the CIDR that only apply to the specific rule
  4. (Optional) If you selected the Exact and Inclusive condition, you can define **Greater than and equal to** and **Less than and equal to** values to include as subnets.
  5. (Optional) Click **Add Exceptions** to exclude a route from the Accept or Drop action.
6. Click **Apply**, and then click **Save**.
