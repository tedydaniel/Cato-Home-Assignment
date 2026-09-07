---
title: "How to Check if Traffic is Blocked by the WAN Firewall"
slug: "how-to-check-if-traffic-is-blocked-by-the-wan-firewall"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/how-to-check-if-traffic-is-blocked-by-the-wan-firewall"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Check if Traffic is Blocked by the WAN Firewall

## Question

There are connectivity issues for the WAN traffic in my account, for example there are issues connecting to other sites or remote resources in my organization. How can I check that the WAN firewall isn’t blocking the WAN traffic?

## Answer

These are the recommended steps to troubleshoot and see if the WAN firewall is blocking traffic and is related to the connectivity issues.

Step 1 - Review WAN firewall block events

1. Review the block events in **Home > Events**:
  1. Select the **WAN firewall** preset. ![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12143612900381.png)
  2. In the **action** field select **Block**. ![mceclip1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12143646880029.png)
2. If you find a block event that is possibly related to the connectivity issue, create a firewall rule above the block rule that allows the traffic.
3. If the connectivity problem persists, continue to step 2.

Step 2 - Review the WAN firewall policy

If you know the specific network details of the relevant traffic, such as source, destination, or protocol, check if the traffic matches a WAN firewall rule. It might be necessary to fine tune the rule and make sure that the firewall allows the specific application (or other network detail).

Step 3 - Check if the traffic is blocked by the implicit block rule

The final rule of the WAN firewall is an implicit block rule, and blocks all traffic that doesn't match one of the firewall rules. This implicit rule doesn't generate events when it blocks traffic.

Add a new rule ANY ANY block at the bottom of the WAN firewall rule and enable tracking for the rule to help identify the source of the blocked traffic. This rule is the same functionality as the implicit rule, but generates block events. Generate traffic and then review the block events.
