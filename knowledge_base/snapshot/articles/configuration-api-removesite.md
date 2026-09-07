---
title: "Configuration API - removeSite"
slug: "configuration-api-removesite"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/configuration-api-removesite"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration API - removeSite

We strongly recommend that before you start using the Cato API, please review the [Support Policy for the Cato API](/v1/docs/support-policy-for-the-cato-api).

## Overview of removeSite

Use the removeSite API to delete any type of site from your account.

## Locating the siteID for a Site

The site ID isn't shown in the Cato Management Application, you can locate the site ID:

- Using the entityLookup API query (see [Cato API - EntityLookup](/v1/docs/cato-api-entitylookup)), use the `type` with the value **site**

You can also use the `search` parameter with the value as the name of the site, and the query returns the site ID
- Number in the URL for the Cato Management Application, when you selected a site (Network > Sites > {site name}). For example, the site ID is 12345 for the following URL: https://cc.catonetworks.com/#/26/sites/12345/networkAnalytics

## removeSite

Use the `removeStaticHost` API to delete a site in your account. You only need to use the `siteId` with this API.
