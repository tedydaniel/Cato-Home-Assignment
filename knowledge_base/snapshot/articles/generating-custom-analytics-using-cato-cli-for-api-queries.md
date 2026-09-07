---
title: "Generating Custom Analytics Using Cato CLI for API Queries"
slug: "generating-custom-analytics-using-cato-cli-for-api-queries"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/generating-custom-analytics-using-cato-cli-for-api-queries"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating Custom Analytics Using Cato CLI for API Queries

## Overview

The Cato CLI provides simple command line syntax methods of accessing the Cato GraphQL API endpoints. Several of the query endpoints can provide rich custom analytics reports beyond the predefined dashboards and reports in the Cato Management Application (CMA). These queries let admins extract raw performance and security data, streamlining the process to analyze bandwidth consumption for users and applications, Socket traffic and jitter, and many other data points. It also supports integrating with external analytics, SIEM, or reporting tools.

By using these Core Analytics Queries with the Cato CLI, you can automate data collection for network monitoring, trend analysis, and compliance use cases. Each query retrieves specific types of telemetry from the Cato Cloud, such as site performance, application usage, or threat activity, giving NOC and SOC teams greater flexibility in analyzing operational metrics.

These are some of the custom analytics for the Cato CLI:

- [Account Metrics](https://github.com/catonetworks/cato-cli/blob/main/catocli_user_guide/account-metrics.md) - Network performance metrics by site, user, or interface
- [Application Statistics](https://github.com/catonetworks/cato-cli/blob/main/catocli_user_guide/app-stats.md) - User activity and application usage analysis
- [Events Time Series](https://github.com/catonetworks/cato-cli/blob/main/catocli_user_guide/events-timeseries.md) - Security events, connectivity, and threat analysis
- [Socket Port Metrics](https://github.com/catonetworks/cato-cli/blob/main/catocli_user_guide/socket-port-metrics.md) - Socket interface performance and traffic analysis

For the complete list of supported fields, filters, and aggregation options, see the Cato CLI documentation on GitHub: [Cato CLI - Custom Report Query Operations](https://github.com/catonetworks/cato-cli?tab=readme-ov-file#custom-report-query-operations)

## Example of Risk Analysis Query

The Risk Analysis query provides visibility into applications with elevated risk scores, based on usage across your organization. This query helps SOC teams identify users accessing high-risk applications and evaluate exposure to shadow IT or data-sharing risks.

### Basic Usage (catocli

The following command retrieves applications with a risk score greater than or equal to 7 for the past 7 days:

```plaintext
catocli query appStats '{
    "appStatsFilter": [
        {
            "fieldName": "risk_score",
            "operator": "gte",
            "values": ["7"]
        }
    ],
    "dimension": [
        {"fieldName": "application_name"},
        {"fieldName": "risk_score"},
        {"fieldName": "user_name"}
    ],
    "measure": [
        {"aggType": "sum", "fieldName": "traffic"},
        {"aggType": "sum", "fieldName": "flows_created"}
    ],
    "timeFrame": "last.P7D"
}'
```

### Result

Returns aggregated statistics for applications with a risk score ≥ 7, including total traffic and number of flows per user. SOC and NOC teams can use this output to identify high-risk application usage and prioritize enforcement policies in the CMA.
