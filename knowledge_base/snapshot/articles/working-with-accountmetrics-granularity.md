---
title: "Working with accountMetrics > Granularity"
slug: "working-with-accountmetrics-granularity"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/working-with-accountmetrics-granularity"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with accountMetrics > Granularity

This article discusses how to configure the **accountMetrics > timeFrame** and **accountMetrics > timeSeries > buckets** arguments to control the Granularity fields and the time duration for each bucket of data.

## Working with the Granularity Field for API Calls

The accountMetrics API call returns account data of the specified timeFrame and it is divided into the number of buckets. Each bucket has the same Granularity or time duration. The Granularity is calculated according to the following formula: timeFrame/buckets.

The API server fetches the data every 5 seconds, so the minimum value for Granularity is 5. If the Granularity is less than 5, then some of the buckets will return no data (value 0).

## Sample API Call with Data for Each Bucket

- Set the **accountMetrics > timeFrame** argument to `last.PT2H` (2 hours, or 7200 seconds)
- Set the **accountMetrics > timeSeries > buckets** argument to 80
- The account **Metrics > Granularity** field shows that the time duration for each bucket is 90 seconds (7200 / 80)
