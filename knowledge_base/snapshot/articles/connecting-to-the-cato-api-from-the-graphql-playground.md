---
title: "Connecting to the Cato API from the GraphQL Playground"
slug: "connecting-to-the-cato-api-from-the-graphql-playground"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/connecting-to-the-cato-api-from-the-graphql-playground"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connecting to the Cato API from the GraphQL Playground

This article explains how to use the GraphQL Playground to run some sample queries and test connectivity to the Cato Networks API endpoint.

## Overview of GraphQL Playground

The GraphQL Playground lets you run API queries that are sent directly to the Cato API server. Third-party API query software such as Altair or Postman, provide powerful functionality for running API calls. However, if there is a connectivity issue with API queries, you can use the Playground to help identify the cause of the issue.

### Prerequisites

To run a Cato API query from the GraphQL Playground, you must have the API key for your account (**Resources > API Keys**). For more about the API keys, see [Generating API Keys for the Cato API](/v1/docs/generating-api-keys-for-the-cato-api).

You need to enter the Cato Management Application (CMA) ID for your account in the sample queries. You can find the CMA ID in the [Account Info page](/v1/docs/viewing-the-account-info).

The URL for the API endpoint is specific to the location where the Cato Management Application (CMA) instance is hosted. There can be a <prefix> value that is appended to the URL for your CMA account and to the API endpoint.

- If there is no prefix (`cc.catonetworks.com`), then use the following URL: `https://api.catonetworks.com/api/v1/graphql2`
- If there is a prefix (such as `cc.us1.catonetworks.com`), then you would use the following URL: `https://api.us1.catonetworks.com/api/v1/graphql2`

## Testing Connectivity with Sample Cato API Queries

You can run a sample API query to test connectivity to the Cato API server. When the `accountID` argument and API key are configured correctly, then the sample API query returns the account data and shows the results in the GraphQL Playground. If the query doesn't return results for your account, then there may be a connectivity issue to the API server or the server may be down. The following sample API queries can help you test connectivity to the Cato API server:

- [accountMetrics](https://support.catonetworks.com/hc/article_attachments/360013398157)
- [accountSnapshot](https://support.catonetworks.com/hc/article_attachments/360013489978)

## Running a Sample API Query in GraphQL Playground

Use an Internet browser to open the GraphQL Playground for the Cato API. Configure the HTTP header for the Playground with your API key. Paste the sample query in the left-hand pane and enter your account ID. Then you can run the query and see the results in the Playground.

1. Download one of the sample API queries from this article and open the file in a text editor such as Notepad.
2. From an Internet browser, go to the GraphQL Playground for the Cato API.
3. In the bottom of the left-hand pane, click **HTTP HEADERS**.
4. Enter your API key in this format: `{ "x-api-key" :"&lt;api key&gt;" }`.

The following screenshot shows the HTTP header configured with the API key**AaBbCcDdEeFf0123456789ABCDEF1234**:

![graphql1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24809308787229.png)
5. Copy and paste one of the sample queries into the left-hand pane of the Playground.
6. At the top of the query, in the `accountID` argument enter your account ID.

The following screenshot shows the `accountID` argument configured with the value 2626:

![graphql2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24809288265885.png)
7. Click the play button.
8. The right-hand pane shows the results of the API query. The following screenshot shows the results for the sample accountMetrics query for account ID 2626:

![graphql3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24809302891165.png)
