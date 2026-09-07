---
title: "Cato Read-Only API Notification – New Internal Cato ID for SDP Users"
slug: "cato-read-only-api-notification-new-internal-cato-id-for-sdp-users"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/cato-read-only-api-notification-new-internal-cato-id-for-sdp-users"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Read-Only API Notification – New Internal Cato ID for SDP Users

## Overview

SDP users are assigned an internal Cato ID as part of the Cato Management Application and Cato’s APIs. To support upcoming features and enhancements, Cato is creating new internal IDs for SDP users.

Starting on June 4, 2023, we are assigning a new internal ID to each SDP user. It’s possible that these new IDs will have an impact on API scripts and queries for SDP users that are hard-coded for the previous IDs.

We recommend that you review the API scripts and make sure that they aren’t hard-coded to use the existing internal ID for SDP users.

## What Changes Do We Need to Make?

Review the scripts and settings for Cato’s API queries and make sure that they are not using the internal ID for SDP users.

Customers that created long term SDP user analytics with the entityLookup and/or accountSnapshot APIs might use the SDP user IDs. Customers that use the eventsFeed API are not impacted.

## What Is the Impact to My Account?

After June 4, 2023, dashboards or historical analytics that are hard-coded for the previous internal IDs for SDP users may experience issues or might not behave as expected.

These are the API types that are changing:

- [AccountMetrics](https://api.catonetworks.com/documentation/#definition-AccountMetrics) (id)
- [AccountSnapshot](https://api.catonetworks.com/documentation/#definition-AccountSnapshot) (id)
- [AppStatsFieldName](https://api.catonetworks.com/documentation/#definition-AppStatsFieldName) (src_site_id & dest_site_id)
- [Entity](https://api.catonetworks.com/documentation/#definition-Entity) (id)
  - Type = vpnUser
- [EventFieldName](https://api.catonetworks.com/documentation/#definition-EventFieldName) (src_site_id & src_or_dest_site_id)

## Who Do I Talk to If I Have Questions?

Please contact [Support](https://support.catonetworks.com/hc/en-us/requests/new).
