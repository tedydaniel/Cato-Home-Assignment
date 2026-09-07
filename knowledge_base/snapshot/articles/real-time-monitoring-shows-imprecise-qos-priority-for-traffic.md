---
title: "Real-Time Monitoring Shows Imprecise QoS Priority for Traffic"
slug: "real-time-monitoring-shows-imprecise-qos-priority-for-traffic"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/real-time-monitoring-shows-imprecise-qos-priority-for-traffic"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Real-Time Monitoring Shows Imprecise QoS Priority for Traffic

## Question

Why can traffic be seen in the QoS Real-time Monitoring, under Site Monitoring -> Real Time -> QOS for the selected site, that does not match the expected priority configuration?

For example, traffic that is assigned with QOS priority P30 in the Bandwidth Management window, appears in the Real-time QOS tab as priority P10.

## Answer

Cato evaluates the network profile per network flow and assigns the priority after the application finalization. The first packets in a flow, before is identified, are assigned with the default priority. This priority is the highest QoS priority that is used in your network rulebase and is used when showing traffic in the **Real-Time -> QOS** site monitoring window. For example, if the highest priority used by a rule is P10, then the unfinalized flows are assigned with priority P10. Only after Cato inspects and determine the application, the flow is assigned with the configured priority based on your BW Management profiles in the rulebase.

**Notes**:

- Unfinalized flows remain with QoS priority P10
- Blocked flows are assigned QoS priority P255
- The amount of the unfinalized traffic is minimal, with flows being finalized after a few packets at most.
- Lower priority profiles in the Bandwidth Management window (**Network > Bandwidth Management**) that aren't assigned to a network rule are ignored for the purposes of deciding the default priority.

## References

For more information on QoS and Bandwidth Management please view the following documentation:

[https://support.catonetworks.com/hc/en-us/articles/4413280501905-Analyzing-QoS-and-Bandwidth-Management-for-a-Site-Priority-Analyzer-](/v1/docs/analyzing-qos-and-bandwidth-management-for-a-site-priority-analyzer)

For more information on Real-time monitoring, please view the following video demonstration:

https://support.catonetworks.com/hc/en-us/articles/9048657044509-How-to-use-Real-Time-Monitoring
