---
title: "CMA - Technical Guidelines"
slug: "cma-technical-guidelines"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/cma-technical-guidelines"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CMA - Technical Guidelines

This article provides essential technical guidelines and administrative requirements to help you effectively manage and secure your Cato Management Application (CMA).

## Entity Limits per Account

You can create a range of entities in the CMA to meet the requirements of your organization. These are the maximum number of entities that you can create for the relevant item (entire account, site, or group).

| Description | Maximum Limit |
| --- | --- |
| Groups (Resources > Groups) | 140,000 |
| Members per Group (Resources > Group > {group name} > Members) | 50,000 |
| Hosts per Site (Network > Sites > {site name} > Site Configuration > Static Host Reservations) | 3,500 |
| Network Ranges per Socket LAN Interface (Network > Sites > {site name} > Site Configuration > Networks) | 1000 |
| Local Routing Rules per Site (Network > Sites > {site name} > Site Configuration > Local Routing) | 100 |
| Rules per Policy | 10,000 |
| Elements per Rule Elements are the total number of items defined for a rule. For example, a rule with 100 users and 10 sites has 110 elements and 2 predicates (user and site). | 2,000 |

## Account Name Requirements

These are the requirements for account names in the CMA:

- Maximum of 56 characters
- ASCII characters and digits are supported
- Quotation marks are not supported (ie. `"example-account"` is an invalid account name)

## Recommended Browsers and Screen Resolution

These are the recommended browser and settings for the best experience when working with the CMA:

- The optimal screen resolution for the CMA is 1920 x 1080
- Recommended browsers:
  - Chrome
  - Edge

## Session Management and Idle Timeout

If you don't manually log out of the CMA, the default behavior for the CMA is to automatically log you out after one hour of inactivity in the browser window.

When you are logged out of the CMA, settings for the [policy revisions](/v1/docs/working-with-policy-revisions) are saved for the next time that you log in.

**Screens That Are Always Active with Real-Time Data**

To help you monitor activity in your network, some of the screens in the CMA remain active with up-to-date real-time data as long as the browser is open.

These are the CMA screens that continuously refresh while the browser is open:

- Home > Topology
- Network > Site Monitoring > {Site name} > Network Analytics
- Network > Site Monitoring > {Site name} > Real Time
