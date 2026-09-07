---
title: "Priority Analyzer Shows Imprecise QoS Priority for Traffic"
slug: "priority-analyzer-shows-imprecise-qos-priority-for-traffic"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/priority-analyzer-shows-imprecise-qos-priority-for-traffic"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Priority Analyzer Shows Imprecise QoS Priority for Traffic

## The Problem

The Priority Analyzer in the Cato Management Application (**Network** > **Sites** > **siteName** > **Priority Analyzer**) shows traffic measurements that don’t match the configured network policy. For example, traffic that is assigned with QoS priority P30 in the BW Management window, appears in the Priority Analyzer as priority P10.

## The Reason

Cato evaluates the network profile per network flow and assigns the priority after the application finalization. The first packets are before the flow is identified and are assigned with the default priority. This priority is the highest QoS priority that is used in your network rulebase and is used when showing traffic in the **Priority Analyzer** window. For example, if the highest priority used by a rule is P10, then the unfinalized flows are assigned with priority P10. Only after Cato inspects and determine the application, the flow is assigned with the configured priority based on your BW Management profiles in the rulebase.

**Notes**:

- Unfinalized flows remain with QoS priority P10
- Blocked flows are assigned QoS priority P255
- The amount of the unfinalized traffic is minimal
- Lower profiles in the BW Management window (**Network > Bandwidth Management**) that aren't assigned to a network rule are ignored
