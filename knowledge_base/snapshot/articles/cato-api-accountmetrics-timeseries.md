---
title: "Cato API - AccountMetrics > Timeseries"
slug: "cato-api-accountmetrics-timeseries"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/cato-api-accountmetrics-timeseries"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato API - AccountMetrics > Timeseries

Shows the metrics for the account according to the specified time-frame (buckets) in the query. Includes historical and near real-time statistics and metrics. This data is similar to the **Site Connectivity** window in the Cato Management Application for each site.

## Timeseries Fields

The timeseries fields shows the time frame for the AccountMetrics data, and how it is displayed according to the time buckets.

These are the details that the AccountMetrics fields can return for the query:

- data - metrics according to the time stamp returned as an array of tuples
- label - metrics that are defined in the labels argument
- sum - summary of the metrics over the given time frame
- units - unit of measurement for the metrics
- info - information related to this data set

## Data

The Data field is an array of tuples, each one contains two values: [timestamp, metric].

- timestamp - amount of time (in milliseconds) from the epoch (1.1.1970)
- metric - the data that you requested in the **labels** argument

Data Argument

- perSecond - A boolean value. When set to **true**, the data is normalized into per second units (divided by the granularity). For example, if the data returns 24 bytes over 6 seconds, then it is shown as 4 bytes per second.

## Label

The Label field shows the value that is defined in the timeseries > labels argument.

## Sum

The Sum field shows a summary of the values over the time frame of the query.

## Units

The Units field shows the unit of measurement these metrics:

- bytes
- packets
- bits
- ms
- percent
- score - health analytics for the site similar to the **Analytics > Sites > Connectivity** window
- count - the number of occurrences for this unit
- seconds - for metrics that are measured in seconds, such as tunnelAge, the number of seconds

## Info

The info field shows information about this set of data, for example: site ID, Socket, and interface.

## Timeseries Arguments

The timeseries arguments let you define the labels and buckets for the query.

- Labels - An enum array that defines the metrics for query
- Buckets - Define the number of buckets for the time duration of the query

## Labels

The **Labels** argument is an array to define the metrics that the query returns. For example, upstream and downstream traffic in bytes.

**Note:** All of the data that is returned for a label shows the metrics over the duration of that time bucket.

These are the options for this argument:

- bytesUpstream - Total number of bytes of upstream traffic (from the Cato Cloud to the site)
- bytesDownstream - Total number of bytes of downstream traffic (from the Cato Cloud to the site)
- bytesUpstreamMax - Maximum upstream throughput (in bytes) - when the time bucket is the minimum value, 5, bytesUpstreamMax is the same as bytesUpstream
- bytesDownstreamMax - Maximum allowed bandwidth (in bytes) for downstream bandwidth - when the time bucket is the minimum value, 5, bytesDownstreamMax is the same as bytesDownstream
- packetsUpstream - Total upstream packets
- packetsDownstream - Total downstream packets
- lostUpstream - Number of packets lost for upstream traffic
- lostDownstream - Number of packets lost for downstream traffic
- lostUpstreamPcnt - Percent of packets lost for upstream traffic
- lostDownstreamPcnt - Percent of packets lost for downstream traffic
- packetsDiscardedDownstream - Total packets discarded for downstream traffic
- packetsDiscardedUpstream - Total packets discarded for upstream traffic
- jitterUptstream - jitter for upstream traffic (difference in time delay in milliseconds (ms) between data packets)
- jitterDownstream - jitter for downstream traffic (difference in time delay in milliseconds (ms) between data packets)
- bytesTotal - Total number of bytes of upstream and downstream traffic
- rtt - Round-trip time from the site to the Cato Cloud
- health - health analytics for the site similar to the **Analytics > Sites > Connectivity** window
- tunnelAge - age of DTLS tunnel (in miliseconds) since the last reconnect
- lastMilePacketLoss - Packet loss measured from the Socket to the Cato Cloud, measures last mile performance of the ISP
- lastMileLatency - Latency measured from the Socket to the Cato Cloud, measures last mile performance of the ISP

## Buckets

The **Buckets** argument defines the number of buckets for the time interval of the query (as defined by the timeFrame argument). For example, a time interval of 24 hours with 48 buckets means that the time duration for each bucket is 30 minutes.

For more about the the Buckets argument and the Granularity field, see [Working with accountMetrics > Granularity](/v1/docs/working-with-accountmetrics-granularity).

These are the details for using the Bucket argument in a query:

- Default value - **10** buckets
- Minimum value - 1 bucket of 5 seconds granularity
- Maximum value - **1000** buckets
