---
title: "Using IP Ranges in Policies"
slug: "using-ip-ranges-in-policies"
updated: 2026-08-11T09:17:35Z
published: 2026-08-11T09:17:35Z
canonical: "knowledge.catonetworks.com/using-ip-ranges-in-policies"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using IP Ranges in Policies

This article explains how to use **Global IP Ranges** across multiple policies.

## Overview

The **Global IP Range** entity is a global object in the Cato Management Application (CMA) that you define and then use in rules across multiple policies. For example, you can use the same range for servers in WAN Firewall, Network Rules, and other policies. If at some point you update a setting in the IP range object, these changes are automatically applied to all the relevant policies. No manual changes are required.

You can also use Custom IP Range for situations where the IP range is only used in the specific rule.

**Notes:**

- The CMA also supports [Floating Ranges](/v1/docs/creating-floating-ranges-for-an-account), which are only applied to traffic routed via BGP, and when the advertised route is an exact match to the Floating Range. IP range objects support all traffic, including BGP.
- For more information about using IP Ranges in Advanced Group objects, see [Working with CMA Advanced Groups and Groups](/v1/docs/working-with-cma-advanced-groups-and-groups).

### Creating IP Ranges

Create the **IP Ranges** and define the range of IP addresses for each object. In addition, you can provide a name and description so they can be easily identified in the policies. You can use a single IP address, range, or a CIDR block for the **IP Range**.

Then you can use the **IP Range** as a global object in one or more of these policies:

- Network Rules
- Internet Firewall
- WAN Firewall
- IPS (only in the outbound direction as the **Destination**)
- Anti-Malware
- Application Control (CASB and DLP)
- TLS Inspection
- IP Allocation
- Split Tunnel

![IP_Ranges.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24447617975325.png)

**To create an IP Range:**

1. From the navigation menu, click **Resources > IP Ranges**.
2. Click **New**. The **New IP Range** panel opens.
3. Define the settings for the IP range.
4. Click **Apply**.
5. To edit an IP range:
  1. Click the **Name** for the range. The **Edit IP Range panel** opens.
  2. Edit the settings.
  3. Click **Apply**.

### Using IP Ranges in Rules

These are the IP ranges that you can use for the relevant settings in rules, such as **Source** or **Destination**:

- Global IP Range - a global object that was created using the section above
- Custom IP Range - Define the IP addresses that only apply to the specific rule

![custom_global_ip_range.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24447602769181.png)

**To use IP Ranges in a rule:**

1. In the relevant section of the rule, select the **IP Range** item.
2. Select if the rule is using a **Global** or **Custom** range.
  - For **Global** ranges, select the IP range you are adding to the rule.
  - For **Custom** ranges, enter the IP address or range of IPs you are adding to the rule.
3. Click **Apply**.
