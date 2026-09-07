---
title: "Cato API - AccountMetrics"
slug: "cato-api-accountmetrics"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/cato-api-accountmetrics"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato API - AccountMetrics

We strongly recommend that before you start using the Cato API, please review the [Support Policy for the Cato API](/v1/docs/support-policy-for-the-cato-api).

## Overview of accountMetrics

The accountMetrics query helps you analyze the state and quality of the connections of sites and SDP users to the Cato Cloud. This data is for the traffic inside the DTLS tunnel between the site and the Cato Cloud.

accountMetrics shows historical metrics, statics, and analytics for the account. It returns data that is similar to the **Site Connectivity** window in the Cato Management Application.

For reseller accounts, you can create separate API keys inside each customer account that you are connecting to the Cato API. For more about rate limiting and the accountMetrics API query, see [Understanding Cato API Rate Limiting](/v1/docs/understanding-cato-api-rate-limiting).

## Working with Bucket Granularity and API Query Limits

There is a maximum limit of 100,000 returned items per accountMetrics API query. If a query reaches this limit, then the query doesn't return any additional data and an error message is displayed.

Cato calculates this limit based on multiplying the following elements:

- Total number of sites plus VPN users
- Number of metrics (API labels/telemetry)
- Number of buckets

In other words, the sum of (sites + VPN users) * (metrics) * (buckets) must be less than 100,000. For example, the following query will produce an error:

- 10 sites
- 140 VPN users
- 5 metrics
- 150 buckets

(10 + 140) * 5 * 150 = 112,500 items in the query. In this example, you can reduce the number of buckets to successfully run the query.

For more about the types of API labels, see [Cato API - AccountMetrics > Timeseries](/v1/docs/cato-api-accountmetrics-timeseries).

### Calculating the Minimum Granularity for a Query

This section explains how to calculate the minimum granularity (bucket size) based on the time frame for the query.

1. Timeframe - Convert the time frame to seconds
2. Bucket limit - Calculate the bucket limit based on 100000 / ( (sites + VPN users) * (metrics) )
3. Minimum Granularity = (timeframe) / (bucket limit)

For example, the first row in the table below shows the query limit for 7 days, 100 sites and VPN users, with 5 metrics:

- 7 days = 604,800 seconds
- 200 buckets = 10000 / (100) * (5)
- 3024 seconds minimum granularity = 604800 / 200

The following table shows sample settings for the accountMetrics query with the minimum bucket granularity:

| Query Timeframe (days) | Sites and VPN Users | Metrics (Labels) | Bucket Limit | Minimum Granularity (in seconds) |
| --- | --- | --- | --- | --- |
| 7 (604800 seconds) | 100 | 5 | 200 | 3024 |
| 7 (604800 seconds) | 100 | 10 | 100 | 6048 |
| 7 (604800 seconds) | 500 | 10 | 20 | 30240 |
| 3 (259200 seconds) | 100 | 5 | 200 | 1296 |
| 3 (259200 seconds) | 100 | 10 | 100 | 2592 |
| 3 (259200 seconds) | 500 | 10 | 20 | 12960 |
| 1 (86400 seconds) | 100 | 5 | 200 | 432 |
| 1 (86400 seconds) | 100 | 10 | 100 | 864 |
| 1 (86400 seconds) | 500 | 10 | 20 | 4320 |

## Details for the accountMetrics Fields

These are the details that the accountMetrics fields can return for the query:

- ID - account ID
- from - starting time
- to - ending time
- granularity - bucket size
- sites -data that is returned for each site (array with nested queries and fields)
- timeseries - time frame for the data, and defines the relationship between the buckets and the data (array with nested queries and fields)

## accountMetrics ID

The ID field shows the unique account internal ID.

This account ID isn't shown in the Cato Management Application, instead it is the number in the URL for the Cato Management Application. For example, the account ID is 26 for the following URL: https://cc2.catonetworks.com/#!/**26**/topology.

## accountMetrics From

The From field shows the starting time for the query data and is defined in the timeFrame argument.

## accountMetrics To

The To field shows the ending time for the query data and is defined in the timeFrame argument.

## accountMetrics Granularity

The Granularity field shows the duration in seconds for a single metrics bucket. The number of buckets are defined in the timeseries > bucket argument.

The Granularity is calculated according to the following formula: timeFrame/buckets. For example, if the query is returning five minutes of data (timeFrame) with 60 buckets, then the Granularity (bucket size) is 5 seconds (300 seconds / 60).

The minimum Granularity for a bucket is 5 seconds. When the bucket Granularity is less than 5 seconds, then it is possible that no data is returned for that bucket.

For more about the Granularity field, see [Working with accountMetrics > Granularity](/v1/docs/working-with-accountmetrics-granularity).

## accountMetrics Sites

The Sites field contains data related to one or more sites in the account. You can also specify data for VPN users with their user IDs.

For more about the Sites field for accountMetrics, see [Cato API - AccountMetrics > Sites](/v1/docs/cato-api-accountmetrics-sites).

## accountMetrics Timeseries

Shows the metrics for the account according to the specified time-frame (buckets) in the query, and includes historical statistics and metrics. This data is similar to the field **Site Connectivity** window in the Cato Management Application for each site.

For more about the timeseries field for accountMetrics, see [Cato API - AccountMetrics > Timeseries](/v1/docs/cato-api-accountmetrics-timeseries).

## Arguments for the accountMetrics

These are the arguments that you can pass and define the data that is returned by the query:

- accountID - account ID
- ID - account ID (legacy argument)
- timeFrame - starting and ending time of the query
- groupInterfaces - Combine analytics for the links into a single link (for boolean value **true**)
- groupDevices - For multiple sites, and a single site with multiple Sockets, combine the analytics into a single Socket (for boolean value **true**)

## accountMetrics accountID Argument

Enter the account ID for the data that the query returns. This argument is mandatory.

This account ID isn't shown in the Cato Management Application, instead it is the number in the URL for the Cato Management Application. For example, the account ID is 26 for the following URL: https://cc2.catonetworks.com/#!/**26**/topology.

## accountMetrics timeFrame Argument

Enter the time frame for the data that the query returns. The argument is in the format `&lt;type&gt;.&lt;time value&gt;`. This argument is mandatory.

These are the supported options to define the time frame:

- last.<time duration> - The <time duration> value for the `last` type is according to ISO-8601 and returns data for the previous specific times. For example:
  - timeFrame = `last.PT5M` shows the previous 5 minutes
  - timeFrame = `last.PT2H` shows the previous 2 hours
  - timeFrame = `last.P1D` shows the previous 1 day
  - timeFrame = `last.P3M` shows the previous 3 months
  - timeFrame = `last.P1Y` shows the previous 1 year
- utc.<short-time-frame-spec> - The time frame combines a start and end date in the format YY-MM-DD/hh:mm:ss according to the specified time zone. You must enter all the date and time values for the argument. For example:
  - timeFrame = `utc.2020-02-{11/04:50:00--21/04:50:00}` shows 10 days of analytics data from February 11, 2020 4:50:00 am to February 21, 2020 4:50:00 am
  - timeFrame = `utc.2020-02-11/{04:50:15--16:50:15}` shows 12 hours of analytics data on February 11, 2020, from 4:50:15 am to 16:50:15 pm
  - timeFrame = `utc.2020-{02-11/04:50:00--04-11/04:50:00}` shows 2 months of analytics data from February 11, 2020 4:50:00 am to April 11 4:50:00 am
  - timeFrame = `utc.{2019-10-01/04:50:00--2020-02-01/04:50:00}` shows 4 months of analytics data from October 1, 2019 4:50:00 am to February 11, 2020 4:50:00 am

This format lets you configure a time frame that includes more than one calendar year

For more about the timeFrame argument and the Granularity field, see [Working with accountMetrics > Granularity](/v1/docs/working-with-accountmetrics-granularity).

## accountMetrics groupInterfaces Argument

When the boolean argument groupInterfaces is set to **true**, then the data for all the interfaces are aggregated to a single interface.

## accountMetrics groupDevices Argument

When the boolean argument groupDevices is set to **true**, then the analytics for all the Sockets (usually two in high availability) are aggregated as one result. For the best results for aggregated Sockets, we recommend that there is consistent names and functionality (for example Destination) for the links on both Sockets.

**Note:** This argument is mandatory for queries of multiple sites and the only valid value for groupDevices value is **true**.
