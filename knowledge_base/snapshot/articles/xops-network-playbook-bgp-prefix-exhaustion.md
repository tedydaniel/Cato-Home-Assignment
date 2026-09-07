---
title: "XOps Network Playbook - BGP Prefix Exhaustion"
slug: "xops-network-playbook-bgp-prefix-exhaustion"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-bgp-prefix-exhaustion"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - BGP Prefix Exhaustion

This playbook describes steps to resolve issues when a BGP route limit is reached.

## Overview

This playbook explains how to identify when the BGP route limit has been reached and outlines the steps you can take to reduce the number of routes being advertised to Cato.

## Symptoms

- BGP Session reset or flap
- Inconsistent routing
- Intermittent blackholing

## Step 1 - Verify the Route Limit reached

The following are the different ways that a Cato Management Application admin can verify that the route limit was reached.

### Using the Story Drill-down

- Go to the **Stories Workbench** page and set the producer to **Account Operations**, including the filter 'Indication **In** BGP Prefix Exhaustion**'.** Adjust the time frame as necessary. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33161924759965.png)
- Verify that a story was created as shown below. ![story-bgp-ex.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33161900262045.jpeg)
- Click on the story to drill down into the details. It provides information on the story status, an incident timeline ![bgp-prefix-story.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33161900264477.jpeg)

### Check BGP Status

Go to the relevant site BGP tab, click on **Show BGP Status** and select **Raw Status**. in the pop window search for the routes_count field and confirm the number of routes has reached the limit of 1024 routes. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33161924766365.png)

## Step 2 - Reduce the number of advertised routes

To Reduce the number of routes advertised to Cato, you can apply the following options:

- **Advertise Aggregated (Summarized) Routes -** Summarizing your internal prefixes can significantly reduce the total number of routes sent to Cato.
- **Apply Route Filtering -** Filter out infrastructure, transit, or any non‑WAN‑relevant prefixes so only necessary routes are advertised. Please review [Working with BGP Filtering](/v1/docs/working-with-bgp-filtering) article for possible filtering options.

If these steps cannot be implemented, or if they were applied but the number of advertised routes still exceeds **1024**, please contact **Cato Support** for further assistance.

## Raising Cases to Cato Support

If following this playbook has not resolved an issue, submit a [Support ticket](/v1/docs/submitting-a-support-ticket). To get the most helpful response to a request, an administrator should provide the results of the troubleshooting steps taken.
