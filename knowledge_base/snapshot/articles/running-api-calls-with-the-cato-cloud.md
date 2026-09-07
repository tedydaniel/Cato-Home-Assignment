---
title: "Running API Calls with the Cato Cloud"
slug: "running-api-calls-with-the-cato-cloud"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/running-api-calls-with-the-cato-cloud"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Running API Calls with the Cato Cloud

The Cato API server collects data from all the PoPs in the Cato Cloud and then makes that data available for API calls. Due to the global nature of the Cato Cloud, there is some delay for the data that is returned.

- The data in accountMetrics API calls is typically available within a 5 minutes time frame. However, it is possible that some data will be delayed up to 30 minutes. To fully guarantee that all data is reported in the API call, set the timeframe after of the API call to more than 30 minutes.
- The data in accountSnapshot API calls can show a delay for up to 15 seconds.

Based on the above delays, we recommend using accountSnapshot to analyze the data in close to real-time.
