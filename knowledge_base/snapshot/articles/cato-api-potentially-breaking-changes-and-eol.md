---
title: "Cato API Potentially Breaking Changes and EoL"
slug: "cato-api-potentially-breaking-changes-and-eol"
updated: 2026-08-12T08:45:04Z
published: 2026-08-12T08:45:04Z
canonical: "knowledge.catonetworks.com/cato-api-potentially-breaking-changes-and-eol"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato API Potentially Breaking Changes and EoL

This article is a platform for notifications on potentially breaking changes and end-of-life (EoL) announcements for the Cato GraphQL API schema and contains information that might require you to update the API client.

The API terms used in this article are explained in [What is the Cato API](/v1/docs/what-is-the-cato-api).

For any customers using the Cato API, we recommend that you click **Follow** to automatically receive email notifications for updates to this article about breaking changes to the API. You can also see more information about new and updated APIs in the [Cato API Changelog](/v1/docs/cato-api-changelog).

For more information about the APIs, see the [Cato Networks GraphQL API Reference](https://api.catonetworks.com/documentation/).

## Potentially Breaking Changes

### 2026-08-30 - Stricter schema type validation

From August 30, 2026, we're enforcing stricter type validation across the API to align with the documented schema. API calls that pass a value in a format that doesn't match the field's documented type could be affected, depending on the endpoint.

- **What's changing:** Parameters must match their schema-defined type exactly. For example, `Int` fields will only accept integer values — string input such as `"5"` will no longer be accepted. This isn't limited to Int fields — any parameter passed in a format that doesn't match its documented type could be affected.
- **What you should do before August 30, 2026:**
  - Review your API calls for values passed in a format that doesn't match the documented schema type (e.g., numeric values passed as strings).
  - Update any misaligned calls.

### 2026-06-21 - API ID fields: Type change from Long/Integer to String

Currently, Cato's API gateway may return ID fields as either a String or a Long (integer). As part of an upcoming infrastructure update, all ID fields will consistently be returned as Strings.

- **What's changing:** API responses that previously returned ID fields as a numeric Long values (for example, `1000000002`) will now always return them as Strings (for example, `"1000000002"`).
- **Who is affected:** API clients that handle ID fields strictly as Long/integer types may break when this change is rolled out.
- **What you should do before June 21, 2026:** Update your API client code to accept both Long and String types for ID fields. This will ensure a smooth transition and prevent disruptions when the change takes effect.

### 2025-08-10 - Change to email Field in addAdmin and updateAdmin APIs

On Aug 10, 2025, the `email` field in the addAdmin and updateAdmin APIs became optional (nullable). This change supports upcoming infrastructure to support granular API access control that includes scripts and automations using service principals.

- Current and future human CMA admins must always include an `email` value
- Queries that return only human admins are unaffected.
- Some clients may need to handle null values in response payloads, such as addAdminPayload

This is not typically a breaking change, but it may impact clients that assume `email` is always present. Review your integration to avoid issues.

### 2025-04-27 - eventsFeed Query API Supports Fetching the Most Recent Events

The eventsFeed API uses a marker to enable iteratively pulling the events feed. The Marker field shows an identifier that indicates the start of a new iteration to fetch events. The API reads events from the queue based on the unique Marker field, and provides the next marker location in the response. If there are no new events in the queue, then the Marker field is empty

An alternative events consumption model is to use the direct no-code integration, see [Integrating Cato Events with AWS S3](/v1/docs/integrating-cato-events-with-aws-s3) and [Integrating Cato Events with Azure Storage Account](%%LINK:13539822366493%%).

**What did we change?**

- Previously, when the marker was not specified, the API returned the oldest available marker. This required consuming the entire event queue before reaching the most recent events.
- Starting from April 27, 2025, if no marker is specified, the API returns the most recent marker. This allows the API to pull the most recent events directly.

**Is it a breaking change?**

- There is no impact for most use cases of the eventsFeed API. There is no change when the Marker field is used for a query, and the events feed consumption logic is the same.
- If you have a dedicated logic to consume the queue to reach the recent events, this logic is no longer required.
  - Now, if no input marker is specified, the API provides the most recent marker. Calling the API with this marker fetches the most recent events
  - The API response contains a marker that points to the most recent (top of the queue) location
  - The corresponding scripts and automated processes should be updated

### 2025-02-09 - Change for XDR API, limit=0 No Longer Supported

We changed the functionality of the `limit` field so that `limit=0` is no longer supported because this isn’t considered a best practice. To ensure continued smooth operation, you need to update any scripts or queries that rely on this parameter. Instead, you can set a limit between 1-2000, which the API fully supports.

If you need to retrieve all stories, we recommend using a pagination approach.

## Upcoming End-of-Life Announcements

## Previous End-of-Life Announcements

### 2026-03-18 - EoL for SecondarySocketSerial Field

The `secondary_socket_serial` event field in the `EventFieldName` API is currently marked as Deprecated and reached end-of-life (EoL) on March 18, 2026.

Recommended alternative field: `socket_serial`

### 2025-06-30 - EoL for LastMileBwInput, InterfaceInfo, and SocketInterfaceBandwidthInput Types

The following [fields and types](https://api.catonetworks.com/documentation/#definition-LastMileBwInput) in the `LastMileBWInput` API are currently marked as Deprecated and reached end-of-life (EoL) on June 30, 2025.

Please use the recommended fields and types instead.

| Deprecated Type | Recommended Type |
| --- | --- |
| downstream | downstreamMbpsPrecision |
| upstream | upstreamMbpsPrecision |

The following [fields and types](https://api.catonetworks.com/documentation/#definition-InterfaceInfo) in the `InterfaceInfo` API are currently marked as Deprecated and reached end-of-life (EoL) on June 30, 2025.

Please use the recommended fields and types instead.

| Deprecated Type | Recommended Type |
| --- | --- |
| downstreamBandwidth | downstreamBandwidthMbpsPrecision |
| upstreamBandwidth | upstreamBandwidthMbpsPrecision |

The following [fields and types](https://api.catonetworks.com/documentation/#definition-SocketInterfaceWanInput) in the `SocketInterfaceBandwidthInput` API are currently marked as Deprecated and reached end-of-life (EoL) on June 30, 2025.

Please use the recommended fields and types instead.

| Deprecated Type | Recommended Type |
| --- | --- |
| downstreamBandwidth | downstreamBandwidthMbpsPrecision |
| upstreamBandwidth | upstreamBandwidthMbpsPrecision |

### 2025-06-08 - EoL for EventFieldName Field in FieldNameInput

- The `auditFeed` query API accepts a list of filters using the `AuditFieldFilterInput` type. Each filter includes a `fieldName` defined by the type `FieldNameInput`, which currently includes two input fields: `AuditFieldName` and `EventFieldName`.
- However, only `AuditFieldName` is a valid and supported input field. To improve schema clarity and avoid confusion, the `EventFieldName` field was removed from the schema on June 8, 2025.
- Update all scripts and queries that use `auditFeed` filters to only use the `AuditFieldName` input field.

### 2025-05-01 - EoL for EventFieldName Types

The following [fields and types](https://api.catonetworks.com/documentation/#definition-EventFieldName) in the `EventFieldName` API are currently marked as Deprecated and reached end-of-life (EoL) on May 1, 2025.

Please use the recommended fields and types instead.

| Deprecated Type | Recommended Type |
| --- | --- |
| application | application_id/application_name |
| custom_categories | custom_category_id/custom_category_name |
| custom_category | custom_category_id/custom_category_name |
| dest_site | dest_site_id/dest_site_name |
| device_posture_profiles | device_posture_profile |
| internalId | event_id |
| rule | rule_name |
| src_site | src_site_id/src_site_name |

### 2025-04-15 - EoL for bgp_peer_description

The bgp_peer_description field in the `EventFieldName` API was marked as Deprecated and is end-of-life (EoL) as of April 15, 2025.

### 2025-03-01 - EoL for EventFieldName Types

The following [fields and types](https://api.catonetworks.com/documentation/#definition-EventFieldName) in the `EventFieldName` API were marked as Deprecated and are end-of-life (EoL) as of March 1, 2025.

Please use the recommended fields and types instead.

| Deprecated Type | Recommended Type |
| --- | --- |
| parent_pid | src_process_parent_pid |
| pid | src_pid |
| process_path | src_process_path |

### 2025-02-23 - EoL for StoryDrillDownFilter value Field

The following [field](https://api.catonetworks.com/documentation/#definition-StoryDrillDownFilter) in the `StoryDrillDownFilter` Beta API was marked as Deprecated and is end-of-life (EoL) as of Feb 23, 2025.

Please use the recommended fields and types instead.

| Deprecated Type | Recommended Type |
| --- | --- |
| value | values |

### 2025-02-11 - EoL for Some SubTypes of Cato Event Data

Following the [announcement](/v1/docs/upcoming-eol-for-some-subtypes-of-cato-event-data) of EoL for some SubType values used in the event consumption APIs related to the Cato Clients, the rollout is paused for accounts that use the Ireland CMA location (cc.catonetworks.com) for the following fields:

| Deprecated Type | Recommended Type |
| --- | --- |
| Reconnected | Connected or Disconnected |
| Changed PoP | Connected or Disconnected (The PoP name is returned in the lastPopName field.) |

- For more information, see [CMA - Technical Guidelines](/v1/docs/cma-technical-guidelines)

### 2025-01-02 - EoL for Event SubTypes

The following fields and types related to the Cato Client were marked as Deprecated and are end-of-life (EoL) as of January 2, 2025.

Please use the recommended fields and types instead.

| Deprecated Type | Recommended Type | Notes |
| --- | --- | --- |
| VPN Never-Off-Bypass | Always-On Bypass | The VPN Never-Off-Bypass SubType value is being replaced with the value Always-On Bypass |
| Reconnected | Connected or Disconnected | To increase granularity, the Reconnected SubType value is being split into 2 new values, Connected and Disconnected |
| Changed PoP | Connected or Disconnected (The PoP name is returned in the lastPopName field) | To increase granularity, the Changed PoP SubType value is being split into 2 new values, Connected and Disconnected |

- For more information, see this article: [Upcoming EoL for Some SubTypes of Cato Event Data](/v1/docs/upcoming-eol-for-some-subtypes-of-cato-event-data)
