---
title: "Example Site Bandwidth with accountMetrics API"
slug: "example-site-bandwidth-with-accountmetrics-api"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/example-site-bandwidth-with-accountmetrics-api"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Example Site Bandwidth with accountMetrics API

This article explains a sample accountMetrics API query to monitor the maximum upstream and downstream throughput for a site.

## Creating the Query

We recommend that you use bytesUpstreamMax and bytesDownstreamMax, which are peak metrics. Cato licenses are based on these values, not the average throughput.

This is a query to retrieve a timeseries of 10 buckets for the timeframe of 15:00:00 to 15:10:00 on February 6, 2024, for the site with ID=12345. 10 buckets for a 10 minute timeframe means each bucket is effectively one minute.

```
{
    accountMetrics(
        accountID: 7890
        timeFrame: "utc.2024-02-06/{15:00:00--15:10:00}"
        groupDevices: true
        groupInterfaces: true
    ) {
        from
        to
        sites (siteIDs:[12345]) {
            interfaces {
                name
                timeseries (labels:[bytesUpstreamMax] buckets:10) {
                    label
                    units
                    data
                }
            }
        }
    }
}
```

This is what the query looks like in the GraphQL API Playground:

![01_accountMetrics.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25296975243037.png)

The full response is:

```
{
  "data": {
    "accountMetrics": {
      "from": "2024-02-06T15:00:00Z",
      "to": "2024-02-06T15:10:00Z",
      "sites": [
        {
          "interfaces": [
            {
              "name": "all",
              "timeseries": [
                {
                  "label": "bytesUpstreamMax",
                  "units": "bytes",
                  "data": [
                    [
                      1707231600000,
                      6008
                    ],
                    [
                      1707231660000,
                      12802
                    ],
                    [
                      1707231720000,
                      6557
                    ],
                    [
                      1707231780000,
                      3467
                    ],
                    [
                      1707231840000,
                      7168
                    ],
                    [
                      1707231900000,
                      3660
                    ],
                    [
                      1707231960000,
                      6791
                    ],
                    [
                      1707232020000,
                      5839
                    ],
                    [
                      1707232080000,
                      4183
                    ],
                    [
                      1707232140000,
                      4684
                    ]
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  }
}
```

## Interpreting the timeseries Results

### Timestamp

Each element of the timeseries / data array is a list where the first element is the timestamp at the start of that bucket, and the second element is the metric for that bucket. The timestamps are in UTC, the Unix Epoch time in nanoseconds. A Python one-line command converts the timestamp in the first bucket to a human-readable string:

```
python3 -c "import datetime;print(datetime.datetime.fromtimestamp(1707231600000/1000))"
```

Running this command on a Mac looks like this:

```
sh-3.2$ python3 -c "import datetime;print(datetime.datetime.fromtimestamp (1707231600000/1000))"
2024-02-06 15:00:00
sh-3.2$
```

You can also run a bash command as follows:

```
date -r $((1707231600000/1000))
```

This the results of the bash command:

```
Cato-admin-M:tools catoadmin$ date -r $((1707231600000/1000))
Tue 6 Feb 2024 15:00:00 GMT
```

Using these techniques to convert all of the timestamps from the above output, we see that they match the start of the buckets for each minute in our timeframe:

```
1707231600000 -> 2024-02-06 15:00:00
1707231660000 -> 2024-02-06 15:01:00
1707231720000 -> 2024-02-06 15:02:00
1707231780000 -> 2024-02-06 15:03:00
1707231840000 -> 2024-02-06 15:04:00
1707231900000 -> 2024-02-06 15:05:00
1707231960000 -> 2024-02-06 15:06:00
1707232020000 -> 2024-02-06 15:07:00
1707232080000 -> 2024-02-06 15:08:00
1707232140000 -> 2024-02-06 15:09:00
```

### Peak Upstream Throughput

The second item in each timeseries element is the metric which in this case is the peak upstream throughput in that bucket. Multiple metrics can be requested in a single query – it is common to request both bytesUpstreamMax and bytesDownstreamMax. The metric is always expressed as a rate regardless of the perSecond input parameter. The `units` field indicates that these are bytes, so we must multiply by 8 to convert to the more usual bits per second.

Looking at the first element in our response above:

```
[
1707231600000,
6008
],
```

We can interpret this as:

- 2024-02-06 15:00:00 UTC was the start of this bucket
- We know from our parameters that this is a one-minute bucket (you can also ask the API to return the bucket granularity if you are unsure)
- During this bucket, the highest throughput was 6008 bytes per second. Multiplying by 8, we get a peak value of 8*6008 = 48,064 bits per second = 48kbps.

Applying this same principle to all of the items in our returned timeseries, we get these values:

```
1707231600000 -> 2024-02-06 15:00:00 48kbps
1707231660000 -> 2024-02-06 15:01:00 102kbps
1707231720000 -> 2024-02-06 15:02:00 52kbps
1707231780000 -> 2024-02-06 15:03:00 27kbps
1707231840000 -> 2024-02-06 15:04:00 57kbps
1707231900000 -> 2024-02-06 15:05:00 29kbps
1707231960000 -> 2024-02-06 15:06:00 54kbps
1707232020000 -> 2024-02-06 15:07:00 46kbps
1707232080000 -> 2024-02-06 15:08:00 33kbps
1707232140000 -> 2024-02-06 15:09:00 37kbps
```

If we graph these values in Excel, the line chart looks like this:

![02_excel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25296996693789.png)

For the corresponding timeframe and site, the “Max Throughput – Upstream” graph looks like this:

![03_excel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25296996785949.png)

At first glance these graphs look somewhat different, but that’s mostly because the CMA graph comes from a query with a much higher number of buckets – for ease of demonstration, we are using a small bucket count (10) with our Playground query. If we place the Excel graph from our query data over the CMA graph, you can see a strong correlation:

![04-excel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25296952629789.png)
