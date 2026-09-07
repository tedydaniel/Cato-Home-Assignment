---
title: "Deprecating metrics Field in accountSnapshot API on Jan. 15, 2024"
slug: "deprecating-metrics-field-in-accountsnapshot-api-on-jan-15-2024"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/deprecating-metrics-field-in-accountsnapshot-api-on-jan-15-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deprecating metrics Field in accountSnapshot API on Jan. 15, 2024

As part of improving the Cato API, we will be making changes to the accountSnaphsot API queries and all metrics information and data will be available only with the accountMetrics API queries.

On Jan. 15th, 2024, we will deprecate the **metrics** field in the [accountSnapshot](https://api.catonetworks.com/documentation/#query-accountSnapshot) API. After this date, the [metrics](https://api.catonetworks.com/documentation/#definition-Metrics) field in the accountSnapshot API will no longer be available. All traffic metrics and data are available using the [accountMetrics](https://api.catonetworks.com/documentation/#query-accountMetrics) API.

## What changes do we need to make?

Review the accountSnapshot queries as follows:

- If you are not using the metrics field with the accountSnapshot API, no changes are required
- If you are using the metrics field with the accountSnapshot API - remove this field and start using the metrics field in the accountMetrics API

## What is the impact to my account?

After, Jan. 15th any queries or scripts that use the accountSnapshot **metrics** field will no longer work. You can use the **metrics** field in the accountMetrics API to retrieve the relevant data.

## Who do I talk to if I have questions?

Please contact [api@catonetworks.com](mailto:api@catonetworks.com)
