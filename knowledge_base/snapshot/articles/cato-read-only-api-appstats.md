---
title: "Cato Read Only API - appStats"
slug: "cato-read-only-api-appstats"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/cato-read-only-api-appstats"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Read Only API - appStats

## Overview of appStats

The appStats API is based on the Application Analytics screen and provides aggregated network data over a time range by source, destination, application, and so on.

Each query calculates aggregation over different measures (bytes up, bytes down, number of flows, etc…) given a certain aggregation function (sum, max, avg, etc…) and different dimensions (site_name, user, app, etc…)

Examples of using the appStats query:

- Calculate total/average/max bandwidth of a specific site
- Max number of flows generated to a specific destination
- Top 10 used applications by a certain given host

## Arguments for appStats

These are the arguments that you can pass and define the data that is returned by the query (all fields are mandatory):

- accountIDs
- measures
- filters
- dimension
- sort
- timeframe

### appStats accountIDs Argument

Enter one or more account IDs for the data that the query returns.

This account ID isn't shown in the Cato Management Application, instead it is the number in the URL for the Cato Management Application. For example, the account ID is 26 for the following URL: https://cc.catonetworks.com/#!/26/topology.

### appStats filters Argument

The `filters` argument lets you define the specific data that are included in the query. These are the arguments you can define:

- fieldName - defines the type of field that you want to filter (for more information, see below [appStats Fields](/v1/docs/cato-read-only-api-appstats#appstats-fields))
- operator - defines how to activate the values to filter the data (for more information, see below [appStats filterOperator](/v1/docs/cato-read-only-api-appstats#appstats-filteroperator))
- values - defines the filter value that is used with the operator

The following `filters` syntax is an example of a query that is filtered to show data for a specific application:

```plaintext
"filters": [
    {  
        "fieldName": "application",
        "operator": "is",
        "values": [   
            "Slack"
        ]
      }
]
```

### appStats dimensions Argument

Use the `dimensions` argument to group fields with the same values into summary rows.

The following example, groups the fields according to the site names:

```plaintext
"dimensions": [
    {
        "fieldName": "site_name"
    }
]
```

### appStats measures Argument

The `measures` argument lets you define the fields you want the query to return and their aggregation type. These are the arguments you can define:

- fieldName - defines the type of field that you want to filter (for more information, see below [appStats Fields](/v1/docs/cato-read-only-api-appstats#appstats-fields))
- aggType - defines the aggregation type (for more information, see below [appStats Aggregation](/v1/docs/cato-read-only-api-appstats#appstats-aggregation))

The following example shows the `measures` syntax for a query that measures the summary of the flows created for the Slack application:

```plaintext
"filters": [
    {  
        "fieldName": "application",
        "operator": "is",
        "values": [   
            "Slack"
        ]
      }
]
"measures": [
    {
        "fieldName": "flows_created",
        "aggType": "sum"
    },

]
```

### appStats sort Argument

The `sort` argument defines how the data is sorted.

The following example shows the `sort` syntax for a query that measures the summary of the flows created for the Slack application. It then sorts the data in descending order of flows created:

```plaintext
"filters": [
    {  
        "fieldName": "application",
        "operator": "is",
        "values": [   
            "Slack"
        ]
      }
]
"measures": [
    {
        "fieldName": "flows_created",
        "aggType": "sum"
    },

]
"sort": [
    {
        "fieldName": "flows_created",
        "order": "dec"
    },

]
```

### appStarts timeframe Argument

Defines the `timeframe` of the query.

```plaintext
"timeFrame": "last.P2D"
```

## Sample appStats Query

This is an example of using the appStats API query to retrun the sum of created flows for the Slack application for each site over the time period of the last two days. The data is sorted in descending order for the top five sites.

**Sample Query**

```plaintext
query appStats($accountID: ID!, $measures: [Measure], $dimensions: [Dimension], $filters: [AppStatsFilter!], $sort: [AppStatsSort!], $timeFrame: TimeFrame!, $limit: Int, $from: Int) {
  appStats(
    accountID: $accountID
    timeFrame: $timeFrame
    measures: $measures
    dimensions: $dimensions
    filters: $filters
    sort: $sort
  ) {
    id
    records(limit: $limit, from: $from) {
      fieldsUnitTypes
      fieldsMap
      trends
   
    }
  }
}
```

**Variable Values**

```plaintext
{
  "accountID": "1234",
  "dimensions": [
    {
      "fieldName": "site_name"
    }
  ],
  "measures": [
    {
      "fieldName": "flows_created",
      "aggType": "sum"
    },
  ],
"filters": [
    {  
        "fieldName": "application",
        "operator": "is",
        "values": [   
            "Slack"
        ]
      }
]
  "sort": [
    {
      "fieldName": "flows_created",
      "order": "desc"
    }
  ],
  "timeFrame": "last.P2D",
  "limit": 5,
  "from": 0
}
```

**Sample AppStats Output**

```plaintext
{
   "data": {
     "appStats": {
       "id": "1234",
       "records": [
         {
           "fieldsMap": {
             "flows_created": "116660",
             "site_name": "Sample Socket"
           }
         },
         {
           "fieldsMap": {
             "flows_created": "105655",
             "site_name": " Sample Socket 2"
           }
         }
       ]
     }
   }
 } 
```

## appStats Fields

This is a description of the fields in the appStats queries.

| Item | Description |
| --- | --- |
| application | cloud application name |
| new_app | new cloud application identifier |
| discovered_app | total number of apps used |
| traffic | the total sum of upstream and downstream data in bytes |
| upstream | data uploaded to cloud applications |
| downstream | data downloaded from cloud applications |
| risk_score | the application risk score assigned by Cato |
| risk_level | the risk level of the application |
| sanctioned | cloud applications approved for use and managed by the organization |
| hq_location | the country in which the registered application headquarters is located |
| is_cloud_app | indicates whether the application is considered cloud app/SaaS app |
| category | the cloud application category |
| description | description of the category |
| ip | IP of the host or SDP Client |
| subnet | name of the subnet |
| domain | SSL SNI, HTTP host name, DNS name, or destination IP |
| dest_ip | server IP address (only relevant for WAN connections) |
| src_site_id | unique internal Cato ID for the site |
| src_site_name | source site or SDP user |
| site_country | country where the site is located |
| site_state | state where the site is located |
| vpn_user_id | unique internal Cato ID for the SDP user |
| flows_created | Number of connections created |
| dest_site | destination site or SDP user ID (proto) |
| dest_is_site_or_vpn | destination site or SDP user |
| dest_site_id | destination site or SDP user ID (DB) |
| dest_site_name | destination site or SDP username |
| traffic_direction | traffic direction |
| device_name | PC or device name |
| ad_name | Active Directory name |
| src_ip | IP for host or SDP Client |
| socket_interface | name for Socket interface |
| src_is_site_or_vpn | traffic is site or SDP Client |

## appStats Aggregation

These are the values for the appStats `aggType`:

- sum
- count
- count_distinct
- distinct
- avg
- max
- min
- any

## appStats filterOperator

These are the values for the appStats filterOperator:

- is
- is_not
- in
- not_in
- exists
- not_exists
- between
- not_between
- gt
- gte
- lt
- lte
