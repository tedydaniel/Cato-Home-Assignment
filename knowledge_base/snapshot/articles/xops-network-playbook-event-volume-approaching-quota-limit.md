---
title: "XOps Network Playbook - Event Volume Approaching Quota Limit"
slug: "xops-network-playbook-event-volume-approaching-quota-limit"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-event-volume-approaching-quota-limit"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - Event Volume Approaching Quota Limit

This playbook describes steps to resolve an issue when the amount of events your account is generating may be approaching the licensed limit.

## Overview

Cato XOps predicts when your account is likely to exceed the event quota limit, letting you to take proactive steps before events are dropped or visibility is impacted. This playbook helps you identify the main sources of event generation and reduce unnecessary events to stay within the quota.

Use this playbook when you receive an **Event Volume Approaching Quota Limit** story from XOps.

![Event_Quota_story.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35977825941533.png)

## Step 1 - Review the Story Details

In the XOps story drill-down page, review the **Details** and **Forecast** sections:

- Review the Forecast graph to understand when the quota is expected to be reached
- Note the relevant subtypes and timeframe for the increase
- Examine the Forecast graph and confirm that the predicted event count is approaching the quota threshold

This information helps you focus your investigation on the relevant time window and event types.

## Step 2 - Identify Top Event Sources

Use the [Events](/v1/docs/analyzing-events-in-your-network) page to identify which policies or rules generate the highest number of events.

1. From the navigation menu, select **Home > Events**.
2. Set the time range to match the timeframe from the story.
3. Analyze event distribution:
  - Expand the **Rule** field to identify rules generating the most events
  - Expand other relevant fields (for example, **Subtype**, **Source IP**) to identify patterns

These are some examples of items you might want to focus on:

- Firewall rules with high event volume
- IPS or other security engines generating repetitive events
- Traffic patterns that trigger excessive logging

## Step 3 - Optimize Event Generation

If you identify rules or policies generating excessive events, review whether event tracking is required.

These are some examples of possible optimizations:

- Disable unnecessary **Track > Event** settings for high-volume rules
- Reduce logging for expected or repetitive traffic
- Adjust policies that generate excessive events without operational value

For example use cases of reducing event generation, see [Quota Exceeded in Cato](/v1/docs/quota-exceeded-in-cato).

## Step 4 - Review Event Quota Capacity

Event quotas depend on your DPA agreement. You can review your DPA version in the **Account > License** page. For more about the event limits for each DPA version, see [Cato Cloud Thresholds and Limits](/v1/docs/cato-cloud-thresholds-and-limits).

If you need to increase your capacity, contact your Cato representative about licensing additional data units.

## Raising Cases to Cato Support

If following this playbook has not resolved an issue, submit a [Support ticket](/v1/docs/submitting-a-support-ticket). To get the most helpful response to a request, an administrator should provide the results of the troubleshooting steps taken.
