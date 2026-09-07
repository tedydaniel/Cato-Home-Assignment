---
title: "Last Mile Monitoring Probes and Connectivity"
slug: "last-mile-monitoring-probes-and-connectivity"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/last-mile-monitoring-probes-and-connectivity"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Last Mile Monitoring Probes and Connectivity

This article offers an overview of using probes to help measure last-mile connectivity and quality for sites.

## Overview

Cato's Last Mile Monitoring Probes feature lets you monitor the quality of the last-mile ISP link. You can also monitor the reachability and availability of business-critical applications and the quality of your Internet connection. The Cato Cloud sends ICMP packets over your various transport types to domains or IP addresses that you define. This helps you identify if there is a connectivity problem, such as latency or packet loss.

By default, this feature measures the quality for the ISP links to these destinations: facebook.com, google.com, and amazon.com. However, you also have the option to configure custom websites for Internet and for WAN traffic.

### Probes

Cato supports sending different probes to various URLs or IP addresses to monitor the performance of your last mile for different sites. Each probe measures latency and packet loss.

You can assign up to 5 probes for each rule.

Once you configure your probes, you can apply them to your sites using the policy.

**​Note:**​ Sometimes the destination ​**amazon.com**​ doesn't respond to a Last Mile Monitoring probe, instead you can use ​**www.amazon.com**​​.

## Enabling the Last Mile Monitoring Probes Policy

The Last Mile Monitoring Probes policy lets you control which probes are sent to which destinations.

**To enable or disable the Last Mile Monitoring Probes policy**

1. From the navigation menu, select **Network > Last Mile Monitoring Probes**.
2. Toggle the **Last Mile Monitoring Probes Policy** slider above the rule base to enable or disable the policy

## Configuring the Last Mile Monitoring Probe Policy

The Last Mile Monitoring policy is comprised of two stages:

- Defining probes
- Creating rules for when the different probes are used

### Define a Probe

By default, you have predefined probes to several destinations, some in China and others globally. You can define additional probes for use in your policy. The rules are order-based, meaning, once a rule is matched, it is applied to the site.

While you can configure as many probes as you would like, you can implement only 5 per rule.

![LMM_probes.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247995090333.png)

**To define a probe:**

1. From the navigation menu, select **Network > Last Mile Monitoring Probes**.
2. On the **Probes** page, click **New**.
3. Enter a descriptive **Name** for the probe and complete the following information:
  - Destination - the URL or IP address to send the probe to
  - Probe Interval - how often probes are sent. The default is 60 seconds
4. Configure if you want to **Send on last resort** links. Take into account that last resort links are often more expensive
5. Click **Apply**

### Configure a Last Mile Monitoring Policy Rule

By default, you have 2 predefined rules - one for all sites and another for sites in China to meet the requirements for Internet traffic in the region.

You can configure additional rules in the policy. You must assign at least one probe to each rule, and no more than 5 probes.

The rules are order-based, meaning, once a rule is matched, it is applied to the site or user and all following rules are ignored.

![LMM_Policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247964812957.png)

**To configure a rule:**

1. From the navigation menu, select **Network > Last Mile Monitoring Probes**.
2. On the **Policy** page, click **New**.
3. Enter a descriptive **Name** for the rule and complete the following information:
  - Rule Order
4. Select the **Source** with at least one of the following items:
  - Site - a specific site or sites
  - Country - all sites whose origin is the selected country or countries
  - System Group - Select the All Sites system group
5. Under **Configuration**, select the probes to which to apply this rule.
6. Click **Apply** and then click **Save**.
