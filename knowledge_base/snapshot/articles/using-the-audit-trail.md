---
title: "Using the Audit Trail"
slug: "using-the-audit-trail"
updated: 2026-09-02T09:36:42Z
published: 2026-09-02T09:36:42Z
canonical: "knowledge.catonetworks.com/using-the-audit-trail"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Audit Trail

The **Audit Trail** provides a chronological log of configuration changes made to your account, whether by administrators or an API. The log contains entries for additions, deletions, and edits of items such as rules, configuration settings, and more.

Audit Trail events are available as standalone content or together with Cato events.

- Access detailed Audit Trail events from:
  - The dedicated Audit Trail page in the CMA
  - The dedicated Audit Trail API, [auditFeed](/v1/docs/cato-api-auditfeed)
- Get contextual clarity by viewing configuration changes in a single stream together with network events, security events, and CMA admin logins. Summarised Audit Trail events are a subtype (`Event Type = System` and `Sub-type = Audit`) of events and are available however you consume those:
  - The Events page in the CMA
  - The [eventsFeed API](/v1/docs/cato-api-eventsfeed-large-scale-event-monitoring)
  - [Events integrations](/v1/docs/getting-started-with-event-integrations) for your cloud storage account, your SIEM, or other connected platforms

## Showing the Audit Trail Page

![admin_trail.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25896270853149.jpeg)

In the **Audit Trail** page, you can see information about actions taken by administrators during a specific time period. You can use the search bar to filter the Audit Trail by modules, types, administrators, and actions.

For some policies, such as the Internet Firewall and WAN Firewall, you can view the value of a field before and after it was changed.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35322530203677.png)

**Note:** Sometimes policy changes may take several minutes until the change is recorded in the Audit Trail, but this doesn't necessarily reflect an actual propagation delay.

**To show the Audit Trail for CMA admins:**

- From the navigation menu, click **Account > Audit Trail**.

## Filtering and Sorting the Audit Trail

You can filter the Audit Trail page by using the time range filter, selecting a Custom Preset filter, manually creating a filter, or using a natural language search. The Audit Trail page supports showing data for the previous 12 months, and you can view up to 3 months of items at one time. The Audit Trail is not part of Cato's Data Lake.

For more information, see the following articles:

- [Using Natural Language Search](/v1/docs/using-natural-language-search)
- [Filtering Data on a Page](/v1/docs/filtering-data-on-a-page)
- [Setting the Time Range Filter](/v1/docs/setting-the-time-range-filter)
