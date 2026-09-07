---
title: "Cato API - AuditFeed"
slug: "cato-api-auditfeed"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/cato-api-auditfeed"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato API - AuditFeed

We strongly recommend that before you start using the Cato API, please review the [Support Policy for the Cato API](/v1/docs/support-policy-for-the-cato-api).

## Overview of auditFeed

The auditFeed query helps you analyze actions taken by admins in the Cato Management Application. The data that this query returns is similar to the **System> Audit Trail** window in the Cato Management Application.

For reseller accounts, you can create separate API keys inside each customer account that you are connecting to the Cato API. For more about rate limiting and the auditFeed API query, see [Understanding Cato API Rate Limiting](/v1/docs/understanding-cato-api-rate-limiting).

## Understanding Fetched Data

The auditFeed API call is designed to support pulling over 2M items of audit data per hour. To help paginate the returned data, when there are more than 1000 audit items over the duration of the timeFrame, then the query iterates the fetch until it returns all the audit data.

These fields are related to the pagination for the audit data: marker, fetchedCount, and hasMore. See below for explanations of these fields.

## Details for the auditFeed Fields

These are the details that the auditFeed fields can show for the query:

- from - starting time
- to - ending time
- marker - The marker field is a unique identifier for the last item of audit data that the API query returned
- fetchedCount - number of items fetched (maximum 1000 items per fetch)
- hasMore - when true, indicates that there are more items for the query to fetch
- accounts (auditFeedAccountRecords) - For resellers that manage multiple accounts, this field specifies the account that was changed and includes all the records and audit data (array with nested queries and fields)

## auditFeed From

The From field shows the starting time for the query data and is defined in the timeFrame argument.

## auditFeed To

The To field shows the ending time for the query data and is defined in the timeFrame argument.

## auditFeed Marker

When there are more than 1000 items of audit data over the duration of the query, the Marker field shows an identifier that indicates the start of a new iteration to fetch the items. For example, if the query returns 2500 items, then these are the results over the fetch iterations:

- first iteration - fetchedCount = 1000 (items), marker = 1234abc, hasMore = true
- second iteration - fetchedCount = 1000 (items), marker = 4567def, hasMore = true
- third iteration - fetchedCount = 500 (items), marker = 8901xyz, hasMore = false

You can ignore the marker value the final iteration

## auditFeed fetchedCount

The fetchedCount fields shows the total number of items in the current fetch action. The maximum value for this field is 1000.

## auditFeed hasMore

When the value for the hasMore field is true, then there is another iteration of fetching items after this one.

## auditFeed Accounts

The Accounts (auditFeedAccountRecords) fields show the admin IDs and audit data for this query. Use the auditFeedAccountsRecords > AuditRecord > AuditFieldName argument to filter the event data that is displayed for the query. For more about the AuditRecords fields, see below *auditFeed > fieldName > AuditFieldName*.

## Arguments for the auditFeed

These are the arguments that you can pass and define the data that is returned by the query:

- accountIDs - account IDs (for multiple accounts, enter the IDs as an array)
- ids - account ID (legacy argument)
- timeFrame - starting and ending time of the query
- filters (AuditFieldFilterInput) - filter the audit log data that is queried (array with nested queries)
- marker - only show items for a specific fetch iteration according to the marker value

## auditFeed accountIDs Argument

Enter one or more account IDs for the data that the query returns. This argument is mandatory.

This account ID isn't shown in the Cato Management Application, instead it is the number in the URL for the Cato Management Application. For example, the account ID is 26 for the following URL: https://cc2.catonetworks.com/#!/**26**/topology.

## auditFeed timeFrame Argument

Enter the time frame for the data that the query returns. The argument is in the format `&lt;type&gt;.&lt;time value&gt;`. This argument is mandatory.

These are the supported options to define the time frame:

- last.<time duration> - The <time duration> value for the `last` type is according to ISO-8601 and returns data for the previous specific times. For example:
  - timeFrame = `last.PT5M` shows the previous 5 minutes
  - timeFrame = `last.PT2H` shows the previous 2 hours
  - timeFrame = `last.P1D` shows the previous 1 day
  - timeFrame = `last.P3M` shows the previous 3 months
  - timeFrame = `last.P1Y` shows the previous 1 year
- <timezone>.<short-time-frame-spec> - The time-frame combines a start and end date in the format YY-MM-DD/hh:mm:ss according to the specified time zone. For example, timeFrame = `utc.2020-02-{11/04:50:00--21/04:50:00}` shows analytics data from February 11, 2020 4:50:00 am to February 21, 2020 4:50:00 am.

## auditFeed filters Argument

The filters (AuditFieldFilterInput) argument lets you define the specific item that are included in the audit trail query. These are the arguments you can define:

- fieldName > AuditFieldName - define the items from Audit Trail
- operator - define how to activate the values to filter the audit data
- values - define the filter value that is used with the operator

### auditFeed > fieldName > AuditFieldName

These are the field names for the different types of Cato Management Application configurations monitored in **System > Audit Trail**.

- admin - the admin whose action generated the record
- model_name - the name of the object that was affected, for example My Site
- admin_id - the ID of the admin whose action generated the record
- module - system module that was changed, for example MFA Configuration, or TLS Inspection
- insertion_date - time that the change was committed or saved
- change_type - describes the change that admin made, the values are: CREATED, DELETED, MODIFIED, ENABLED, DISABLED, SKIPPED
- creation_date - time that the change was started
- change - a detailed account of the change in JSON format
- model_type - the type of object that was changed, for example Site, Socket, SocketInterface

## auditFeed marker Argument

The marker argument lets you limit the query to the events for a specific fetch iteration. To show the marker values, run the query with the marker argument with an empty value. The query returns the marker values for the defined timeFrame argument.

For example, if the query returns 2500 events, then these are the results over the first three fetch iterations:

- first iteration - fetchedCount = 1000 (events), marker = 1234abc, hasMore = true
- second iteration - fetchedCount = 1000 (events), marker = 4567def, hasMore = true
- third iteration - fetchedCount = 1000 (events), marker = 8901xyz, hasMore = true

To show only the events in the second iteration, set the marker argument to **4567def**.
