---
title: "Cato Read Only API - events"
slug: "cato-read-only-api-events"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/cato-read-only-api-events"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Read Only API - events

## Overview of the events API Query

The events API query provides a way to obtain summary information about the events generated for an account without having to first extract the individual events and performing the analysis.

Examples of the kind of analysis the events API include:

- Number of SDP users that logged in over a specific timeframe
- Percentage of firewall block vs. allow events
- Show how many events (cardinality) were generated for each event type in the previous 30 days

## Arguments for events

These are the arguments that you can pass to the events api call to modify its operation:

- accountID
- measures
- filters
- dimensions
- sort
- timeFrame

### The accountID argument

This is the accountID for the account you are running the query against.

> [!NOTE]
> Note:
> 
> This account ID isn't shown in the Cato Management Application, instead it is the number in the URL for the Cato Management Application. For example, the account ID is 26 for the following URL: https://cc.catonetworks.com/#!/26/topology.

### The measures argument

The `measures` argument lets you define the fields you want the `events` query to examine and the way the results should be aggregated. For each field you want to analyze, you must define the following:

- fieldName - defines the field that you want to aggregate
- aggType - defines how you want the aggregation to be performed (e.g. count_distinct)

The following example shows the `measures` syntax for a query that returns the sum of the event_count fields:

```plaintext
 "measures": [
    {"fieldName":"event_count","aggType":"sum"}
]
```

### The filters argument

The `filters` argument lets you define a filter that will result in only a limited subset of the events being examined. For each filter you must define the following:

- fieldName - defines the name of field that you want to filter
- operator - defines the filter operation that should be used to filter the field
- values - defines the filter value that is used with the operator

Here is an example of the filters argument used to select only events with an event_type of **Security**:

```plaintext
"filters": [
    {
        "fieldName": "event_type",        
         "operator": "is",
         "values": ["Security"]
    }
]
```

### The dimensions argument

Use the `dimensions` argument to group fields with the same values into summary rows.

Here is an example that groups the files according to the event_type:

```plaintext
"dimensions": [
    {"fieldName": "event_type"}
]
```

### The sort argument

The `sort` argument defines how the returned data is to be sorted. Here is an example usage of the sort argument

```plaintext
  'sort': [ 
      {'fieldName': 'event_count', 'order': 'desc'},
      {'fieldName': 'event_type', 'order': 'asc'}
  ]
```

### The timeFrame argument

Defines the `timeframe` of the query. This is specified using the format defined by the ISO 8601 specification. Here is an example of how you would specify the time-frame for the past 30 days:

```plaintext
"timeFrame": "last.P30D" 
```

> [!NOTE]
> **Notes:**
> 
> - The maximum length of time that can be specified for the timeFrame argument is currently 89 days.
> - The actual ISO 8601 specification can be obtained [here](https://www.iso.org/standard/70907.html), but it is not free. You can also refer to this [Wikipedia article](https://en.wikipedia.org/wiki/ISO_8601#Durations) for more information to understand how to define this argument.

## Sample events Query

### Sample Query

```plaintext
query events(
    $accountID: ID!,
    $measures: [EventsMeasure],
    $dimensions: [EventsDimension],
    $filters: [EventsFilter!],
    $sort: [EventsSort!],
    $timeFrame: TimeFrame!,
    $limit: Int,
    $from: Int) {  
    events(
        accountID: $accountID
        timeFrame: $timeFrame
        measures: $measures
        dimensions: $dimensions
        filters: $filters
        sort: $sort  ) {
        id    
        from
        total
        records(limit: $limit, from: $from) {
            fieldsMap
        }
    }
}
```

### Variable Values

```plaintext
{  
    "accountID": "1234",
    "measures": [ {
          "fieldName": "event_sub_type",
          "aggType": "count_distinct"
          }
    ],
    "filters": [ {
          "fieldName": "event_type",
          "operator": "is", "values": ["Security"]
          }  
    ],  
    "timeFrame": "last.P1M"
}
```

### Sample events Output

```plaintext
{  
    "data": {
        "events": {
            "id": "xxx",
            "from": "2023-01-26T00:00:00Z",
            "to": "2023-02-27T00:00:00Z",
            "total": 1,
            "records": [        
                 { 
                     "fieldsMap": {          
                        "event_sub_type": "6"
                        }
                 }
             ]
        }
    }
}
```
