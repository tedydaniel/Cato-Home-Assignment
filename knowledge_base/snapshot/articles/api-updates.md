---
title: "Cato API Changelog"
slug: "cato-api-changelog"
updated: 2026-08-10T09:30:08Z
published: 2026-08-10T09:30:08Z
canonical: "knowledge.catonetworks.com/cato-api-changelog"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato API Changelog

This article is a platform for notifications on recent and planned changes to the Cato GraphQL API schema. It contains news and updates highlighting new capabilities, such as newly released APIs and automation tools.

For information about changes that might require you to update your API client, see [Cato API Potentially Breaking Changes and EoL](/v1/docs/cato-api-potentially-breaking-changes-and-eol).

The API terms used in this article are explained in [What is the Cato API](/v1/docs/what-is-the-cato-api).

For any customers using the Cato API, we recommend that you click **Follow** to automatically receive email notifications for updates to this article about changes to the API.

For more information about the APIs, see the [Cato Networks GraphQL API Reference](https://api.catonetworks.com/documentation/).

## News and Updates

#### Additional User Actions

**Change:** Updated API

**Feature Title:** Simplified user administration through external workflows and identity management systems

The API supports enabling users (`enableUser`) and disabling users (`disableUser`).

#### Improved Analytics for Grouped AppStats API Results - Jun 21, 2026

**Change:** Updated API

**Feature Title:** Improved Analytics for Grouped AppStats and Events API Results

When querying AppStats or Events API data and grouping by a dimension, such as country or device type, you can choose to display records with no value for that dimension as an empty group. This helps ensure consistent totals in API queries and shows previously hidden data in CMA dashboards and reports.

- New query-level boolean parameter: `IncludeEmptyDimension`, no impact to existing API scripts
- Applies to API queries and data shown in the CMA

#### Added Fields for appStats API for DEM Customers - Apr 19, 2026

**Change:** Updated API

**Feature Title:** Updates to appStats API for application experience metrics

The following new fields for the appStats API are available for application experience metrics to enable programmatic access to user, host, and application performance data:

- `experience_score_level` - Aggregated experience score indicator
- `ttfb` - Time to first byte, measures server responsiveness
- `tls_latency` - Time for establishing TLS connection
- `tcp_latency` - TCP connection setup time
- `http_latency` - End-to-end HTTP request latency
- `http_error_rate` - Rate of HTTP errors observed

**Note:** These fields are available only for customers with a DEM license.

#### Added Mutation APIs for Webhooks, Mailing Lists, and Subscription Groups - Mar 29, 2026

**Change:** New API

**Feature Title:** API support for managing webhooks, mailing lists, and subscription groups

- Use the following APIs to assign, replace, update, and remove site licenses via API for single and pooled licenses

For details on the notification management in the CMA, refer to the [Notifications](/v1/docs/notifications) KB articles
  - 
    - Manage webhook integrations using `createWebhook`, `updateWebhook`, `deleteWebhook`, `webhook`, `webhookList`, and `testWebhook`
    - Manage mailing lists using `createMailingList`, `updateMailingList`, `deleteMailingList`, `mailingList`, and `mailingListList`
    - Combine webhooks and mailing lists into 'subscription groups using' `createSubscriptionGroup`, `updateSubscriptionGroup`, `deleteSubscriptionGroup`, `subscriptionGroup`, and `subscriptionGroupList`

## Previous API News and Updates

#### Updates to Split Tunnel Policy APIs - Jan 18, 2026

**Change:** Updated API

**Feature Title:** Updates to SplitTunnelPolicyMutations

- The following APIs have been changed to more accurately align with the feature behavior in the Cato Management Application.
  - **These changes apply to all of the mutations for the Split Tunnel policy:**
    - `Exclude` - changed to RouteAllToCatoExcept
    - `Include` - changed to RouteOnlySelected
    - `Coverage` - changed to ConnectionMode
    - `dnsExclusion` - changed to dnsSuffix

These APIs are currently available as Beta.

#### Added Mutation APIs for Site Bandwidth Licenses - Aug 11, 2025

**Change:** New API

**Feature Title:** API support for managing site bandwidth licenses

- Use the following APIs to assign, replace, update, and remove site licenses via API for single and pooled licenses
  - **Mutation APIs:**
    - `assignSiteBwLicense` - assigns a license to a site
    - `updateSiteBwLicense` - for pooled licenses, updates the bandwidth for a site
    - `replaceSiteBwLicense` - replaces the site license with no downtime
    - `removeSiteBwLicense` - removes a license from a site

These APIs are currently available as Beta.

#### Added Query APIs for App Catalog and DLP Content Types - May 19, 2025

**Change:** New API

**Feature Title:** API support for querying App Catalog and DLP Content Types

- App Catalog - Query the data for apps, including Compliance, Security, and CASB Activities:
  - `catalogApplicationList` - All apps and data
  - `catalogApplication` - Single app
- DLP Content - Query the types of content for the DLP Data Inline Protection rule
  - `contentTypeGroupList`

These APIs are currently available as Beta.

#### Added Mutation API for HA Secondary vSocket - Mar 2, 2025

**Change:** New API

**Feature Title:** API support for secondary vSocket for HA configurations

- Use the [following APIs](https://api.catonetworks.com/documentation/#mutation-sites.addBgpPeer) to set story verdicts, change status, and add comments
  - **Mutation APIs:**
    - `addSecondaryAwsVSocketInput` For AWS vSocket with HA configuration, add a secondary vSocket
    - `AddSecondaryAzureVSocketInput` For AWS vSocket with HA configuration, add a secondary vSocket

These APIs are currently available as Beta.

#### Added XDR Mutation API - Jan 12, 2025

**Change:** New API

**Feature Title:** API support for XDR stories and comments

- Use the [following APIs](https://api.catonetworks.com/documentation/#mutation-xdr.addStoryComment) to set story verdicts, change status, and add comments
  - **Mutation APIs:**
    - `addStoryComment` Post comments that help track the story investigation
    - `analystFeedback` Manage Story Actions, such as the story Verdict, Type, and Classification.
    - `deleteStoryComment` Delete a previously posted comment using the comment ID

This API is currently available as Beta.

#### Last-Mile Bandwidth Supports Kbps - Jan 12, 2025

**Change:** Enhancement for APIs

**Feature Title:** Set site bandwidth values that include one decimal point (e.g. 1.5 Mbps) for more granular accuracy

- Use the [following APIs](https://api.catonetworks.com/documentation/#mutation-sites.addSocketSite) to set story verdicts, change status, and add comments
  - **Impacted types for APIs:**
    - `LastMileBwInput`
    - `InterfaceInfo`
    - `SocketInterfaceBandwidthInput`

These API types are currently available as Beta.

#### Changes to accountSnapshot and accountMetrics for IPsec IKEv2 Sites - Jan 12, 2025

**Change:** Update of `Primary` value to `Primary 1`

**Feature Title:** API Support for IPsec IKEv2 sites

The value retrieved from the `InterfaceId` field in the accountSnapshot and accountMetrics queries are changing as of the gradual release of support for Active/Active configurations on Jan 12, 2025.

| Old Value | New Value | Notes |
| --- | --- | --- |
| Primary | Primary1 | This change lets us support more than one primary tunnel |

#### New BGP Peering API - Dec 23, 2024

**Change:** New API

**Feature Title:** API Support for BGP Peering

- Use the following APIs to simplify the [configuring](https://api.catonetworks.com/documentation/#mutation-sites.addBgpPeer) and [monitoring](https://api.catonetworks.com/documentation/#query-site.bgpPeer) BGP peers for sites
  - **Mutation APIs:**
    - `addBgpPeer` Add a new BGP peer to a site
    - `updateBgpPeer` Update settings for an existing BGP peer configuration
    - `removeBgpPeer` Delete a BGP peer configuration for a site
  - **Query APIs:**
    - `bgpPeer` Retrieve information about a specific BGP peer
    - `siteBgpStatus` Show the current BGP status, including session details and route information

This API is currently available as Beta.
