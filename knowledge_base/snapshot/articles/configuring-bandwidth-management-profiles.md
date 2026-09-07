---
title: "Configuring Bandwidth Management Profiles"
slug: "configuring-bandwidth-management-profiles"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/configuring-bandwidth-management-profiles"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Bandwidth Management Profiles

This article details how to create and manage Bandwidth Management profiles in the Cato Management Application (CMA) to help manage and prioritize traffic in your network.

## Overview of Bandwidth Management Profiles

Bandwidth Management profiles define how you measure and control network traffic based on profiles to manage and prioritize upstream/downstream bandwidth according to a fixed speed or a percentage of the total bandwidth. By default, these profiles are applied at the account level rather than per site. The Bandwidth Management table includes predefined profiles that can be edited as needed. Additional profiles can be added and configured for greater granularity.

Bandwidth Management profiles are for site traffic and don't apply to traffic for remote users with the Cato Client.

**Note:** To help make sure that network rules are configured correctly, rules in the **Bandwidth Management** screen are for the entire account. You can also create profiles for specific sites and interfaces that override the global settings.

### QoS Settings

Each profile lets you set the traffic priority and bandwidth limits, which control the QoS based on traffic classes.

#### Priority

Priority sets the relative weight or importance given to each Bandwidth Management Profile.

Each profile is given a Priority number ranging from **2** to **254** that determines the relative priority of the traffic, as defined by the networking rule. Lower priority profiles (for example, P200 and higher) are generally reserved for lower priority traffic, such as backup data.

#### Limits

The **Limit** setting defines the maximum throughput that the QoS engine allows for this priority. By default, the **Limit** value is set to **No limit**. Other options include **Always limit** and **Limit only when line is congested**.

### Class of Traffic

The **Class of Traffic** column shows the names of the network rules assigned to each traffic priority.

## Understanding the Bandwidth Option: Limit Only When the Line is Congested

If you select the **Limit only when the line is congested** option for a bandwidth policy, the Cato Cloud always optimizes and maximizes the usage of your links capacity.

- If there is no contention for capacity, throttling is not applied.
- If there is contention for capacity, throttling is applied to the extent required by the policies that you defined.

For example, if P30 is limited to 30%, that means only 30% of the link is allocated to lower priority traffic. Ensuring that higher priority traffic can use the remaining 70% of the link.

The bucket granularity in the CMA is 5 seconds. If you are monitoring traffic with the [Priority Analyzer](/v1/docs/analyzing-qos-and-bandwidth-management-for-a-site-priority-analyzer), congestion doesn’t need to last the full 5 seconds for the page to display a red indicator. This may be misleading, as you could assume that **Limit only when the line is congested** was fully active during the entire bucket, even if congestion occurred for only 1 second.

The following examples show contention for capacity:

**Scenario A:**

In this scenario, Cato throttles the bandwidth for network rules using P20 (even though it is currently under the limit) to accommodate traffic in network rules using P10, which is not limited.

| Policy | Bandwidth Limits | Current Bandwidth Usage |
| --- | --- | --- |
| P10 | None | 80% |
| P20 | 50% | 40% |
| P30 | 20% | 0% |
| Total Potential Bandwidth Usage: | 120% |

**Scenario B:**

In this scenario, the total bandwidth limit is more than 100%, and Cato throttles traffic dynamically as required to maximize high-priority traffic.

| Policy | Bandwidth Limits |
| --- | --- |
| P10 | 20% |
| P20 | 30% |
| P30 | 40% |
| P40 | 20% |
| Default | N/A |
| Total Bandwidth Limits: | 110% |

## Creating a New Bandwidth Management Profile

QoS profiles and network rules can be configured globally (account level), and tailored with as much granularity as required (for example, at site level). When you limit the bandwidth for a site, it is applied to all the links in the site. For example, if you set a profile for 5 Mbps, for sites that have 2 or more active links, each link is limited to 5 Mbps.

Cato recommends using the **%** unit of measurement for Bandwidth Management Profiles at the account level. If you need to configure profiles for specific sites or interfaces, we recommend that you use **Mbps** at the site level, see [Overriding Bandwidth Management Profiles for a Site](/v1/docs/overriding-bandwidth-management-profiles-for-a-site). If you enter upstream/downstream values that are greater than the actual connection speed of your ISP's link, the Cato Socket QoS engine will be ineffective.

![bandwidthmanagement.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28249657715101(1).png)

After you define your **Bandwidth Management** profiles, apply them to Network Rules (see [Configuring Network Rules](/v1/docs/configuring-network-rules)).

**To create a Bandwidth Management Profile for your account:**

1. From the navigation menu, click **Network > Bandwidth Management**.
2. Click **New**. The **Add** panel opens.
3. Configure the **Bandwidth Management** profile:
  - **Priority**: Enter a value between 2 to 254.
  - **Limits**: Select if and how to limit the bandwidth for this priority as follows:
    - **No Limit** - don't force any bandwidth limits.

**Note:** Selecting **No Limit**, can potentially starve traffic with lower priorities.
    - **Always Limit** - Always enforce the limit according to the **Upload/Download values** defined below.
    - **Limit only when line is congested** - Enforce the limit (according to the upload/download values defined below) only during times when the line is congested.

**Note:** When the setting **Limit only when line is congested** is applied to traffic when the line is congested, the traffic throughput may exceed the limit if there is available bandwidth. This is due to the Socket using a best effort algorithm to utilize the entire bandwidth of the link without exceeding the total bandwidth limit. For more about the Socket traffic shaping algorithms and the best effort iteration of transmission, see [Part 3: The Socket Traffic Prioritization and QoS](/v1/docs/part-3-the-socket-traffic-prioritization-and-qos).
  - **Upload Limit** and **Download Limit**: Enter the limit and select percentage (**%**) or bandwidth (**Mbps**).
4. Click **Apply**. The new profile is added to the **Bandwidth Management** table in the order defined by the configured priority.
5. Click **Save**. The new profile is saved.

## Editing a Bandwidth Management Profile

**To edit a Bandwidth Management profile:**

1. From the navigation menu, click **Network** > **Bandwidth Management**.
2. Click on the profile to edit. The **Edit Bandwidth** panel opens.
3. Edit the value(s) as needed.
4. Click **Apply**. The changes are updated.
5. Click **Save**. The changes are saved.

## Limitation

QoS is not applied to app connector traffic. You can't define a bandwidth profile and Network Rules for the traffic, and it is assigned the lowest network priority.
