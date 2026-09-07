---
title: "Cato API Reference for Technology Partners"
slug: "cato-api-reference-for-technology-partners"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/cato-api-reference-for-technology-partners"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato API Reference for Technology Partners

## Introduction to Cato API

The **Cato API** is the primary automation interface for interacting with data and management functions on the Cato SASE platform. It uses GraphQL for flexible querying and efficient data retrieval, enabling both:

- **Read-only operations** (data extraction)
- **Mutation operations** (configuration changes)

For detailed schema reference, see the Cato API documentation: [https://api.catonetworks.com/documentation/](https://api.catonetworks.com/documentation/)

The API endpoint is in the format: [https://api.catonetworks.com/api/v1/graphql2](https://api.catonetworks.com/api/v1/graphql2)

### API Lifecycle

For a full overview of the API lifecycle and usage guidelines, see [What is the Cato API](/v1/docs/what-is-the-cato-api)

### How to Use Cato API Keys

To authenticate requests to the Cato API, include an HTTP header named x-api-key in your API client. Set the value of this header to your Cato API key using the format: x-api-key: <api-key>. For example: x-api-key: abcdef12345. This header authorizes your request and grants access to the relevant Cato API endpoints based on the permissions associated with your key.

API keys and a sandbox environment will be provided after Cato’s approval of the integration scoping document.

### Schema Changes

Cato’s SLA for potentially breaking changes is documented in the [Announcing and Managing Potentially Breaking Changes](/v1/docs/what-is-the-cato-api) section of the [What is the Cato API](/v1/docs/what-is-the-cato-api) article.

APIs and fields planned for End-of-Life (EoL) are identified as *deprecated* in the [API documentation](https://api.catonetworks.com/api/v1/graphql2). Where available, a recommended replacement and the scheduled EoL date are provided.

In addition, potentially breaking changes are communicated in the [Cato API Potentially Breaking Changes and EoL](/v1/docs/cato-api-potentially-breaking-changes-and-eol) article. Technology Partners are strongly encouraged to follow this article to receive notifications regarding upcoming schema updates and deprecations.

### Rate Limiting and Fair Usage

The **rate limiting policy** defines the maximum request throughput allowed per account and is designed to ensure platform stability and fair resource usage. Integrations should implement appropriate retry and backoff mechanisms to handle rate limit responses. For details, refer to the [Understanding Cato API Rate Limiting](/v1/docs/understanding-cato-api-rate-limiting) article.

### Core API Endpoints for Integration

Below are the most common APIs used during early integration and data ingestion:

| **Data Type** | **API** | **Purpose** | **Typical Use-Cases** |
| --- | --- | --- | --- |
| **Raw Events / Security Telemetry** | [eventsFeed](https://api.catonetworks.com/documentation/#query-eventsFeed) | Recommended entry point for consuming raw event logs and security telemetry. | SIEM ingestion, security monitoring, compliance logging, threat detection. |
| **Administrative Audit Logs** | [auditFeed](https://api.catonetworks.com/documentation/#query-auditFeed) | Retrieves audit logs for admin actions and configuration changes. | Compliance auditing, change tracking, governance monitoring. |
| **Application & Flow Analytics** | [appStats](https://api.catonetworks.com/documentation/#query-appStats) [appStatsTimeSeries](https://api.catonetworks.com/documentation/#query-appStatsTimeSeries) | Provides application usage statistics and flow performance metrics over time. | Application monitoring, network performance analysis, usage reporting. |
| **Security Incidents / Alerts** | [stories](https://api.catonetworks.com/documentation/#query-xdr.stories) | High-level insights into security incidents and correlated alerts. | SOC workflows, incident management, alert enrichment. |
| **Traffic Metrics** | [accountMetrics](https://api.catonetworks.com/documentation/#query-accountMetrics) | Traffic and usage metrics across sites and remote users. | Network usage analytics, capacity planning, and reporting dashboards. |
| **Connectivity & Inventory Snapshot** | [accountSnapshot](https://api.catonetworks.com/documentation/#query-accountSnapshot) | Connectivity status and inventory information for sites, sockets, and users. | Infrastructure monitoring, topology visibility, and environment discovery. |
| **Device Inventory & Attributes** | [devices.attributesCatalog](https://api.catonetworks.com/documentation/#query-devices.attributesCatalog) [devices.list](https://api.catonetworks.com/documentation/#query-devices.list) | Provides device inventory and associated attributes discovered by the platform. | Asset management systems, IoT/OT visibility, device classification, and inventory tracking. |
| **Socket Port Metrics** | [socketPortMetrics](https://api.catonetworks.com/documentation/#query-socketPortMetrics) [socketPortMetricsTimeSeries](https://api.catonetworks.com/documentation/#query-socketPortMetricsTimeSeries) | Provides current and historical metrics for socket interfaces and ports. | Infrastructure monitoring, link health monitoring, capacity planning, and network troubleshooting. |

For full API operation definitions and sample responses, refer to the [Cato GraphQL API Reference](https://api.catonetworks.com/documentation/).

## Reference Tools and Examples

To support development and integration workflows, Cato provides several reference resources:

- [Cato GitHub Account](https://github.com/CatoNetworks) - Sample code, API helper tools, Jupyter notebooks, Postman collections, and CLI utilities. Examples:
- [data-analytics](https://github.com/CatoNetworks/data-analytics) - Jupyter notebooks demonstrating eventsFeed use cases.
- [cato-toolbox](https://github.com/CatoNetworks/cato-toolbox) - General-purpose helpers for API consumption and testing, including Python code for fetching events.
- [GraphQL Playground](https://api.catonetworks.com/api/v1/graphql2) - A browser-based interactive tool for testing API queries. See [Cato API from the GraphQL Playground](/v1/docs/connecting-to-the-cato-api-from-the-graphql-playground) for details.
- **Cato Remote MCP Server** - Enables integration with the Cato API using AI assistants and LLM-based tools via the Model Context Protocol (MCP). This allows interacting with Cato data using natural language or AI-driven workflows. For more information, see: [Working with the Cato Remote MCP Server](/v1/docs/working-with-the-cato-remote-mcp-server).

## Support and Community Resources

Partners can raise API related questions through

- [Cato Support Portal](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings)
- [Cato Connect Community — API Discussions](https://connect.catonetworks.com/category/api/discussions/api-discussions)
