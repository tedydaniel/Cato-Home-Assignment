---
title: "Integrating Cato Data with Splunk"
slug: "integrating-cato-data-with-splunk"
updated: 2026-08-03T13:38:12Z
published: 2026-08-03T13:38:12Z
canonical: "knowledge.catonetworks.com/integrating-cato-data-with-splunk"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating Cato Data with Splunk

## Overview

Use the Splunk integration to include Cato network and security data in your existing monitoring, correlation, and investigation workflows. The native integration sends data directly from Cato to Splunk, allowing you to analyze Cato activity alongside data from other sources in a centralized platform. This helps you create dashboards, searches, alerts, and reports without requiring additional data collection mechanisms.

Cato also offers a custom GitHub integration from the Cato GitHub repository. For more details, see Choosing Between the Native Turnkey and Custom GitHub Integration Methods, below.

## Splunk Data Sources

The Splunk integration supports two data sources:

- **Events** - Generated when specific activity occurs in the network or system, such as when a policy rule is matched or a threat is detected. These records provide discrete, real-time insights into security and policy enforcement. The data is sent using Cato's [event schema](https://api.catonetworks.com/documentation/#definition-EventFieldName).
- **Flows** - Originate as network flows (5-tuple) and are enriched with application-level information as it becomes available from Cato engines. In addition to application and user context, flows include aggregated session data such as bytes, packets, and duration, providing a complete view of network activity over time. The superset of flow fields is represented by the [appStats schema](https://api.catonetworks.com/documentation/#definition-AppStatsFieldName).

Some fields are available only for flows streamed through the native integration and are not part of appStats or Application Analytics. For example, flow_id and aggregated metrics such as upstream and downstream packets and bytes, and flow duration. These fields are marked with the following comment:

Only available for native flows data integration created in the CMA.

By default, new integrations export only **Events**. The **Flows** data source can generate a significantly higher volume of data compared to events. The exact volume depends on your traffic. The CMA supports configuring multiple integrations, allowing you to send different data sources as needed. Filtering is supported for Events only.

## Use Cases

### Events

Sample Company uses Splunk for centralized security monitoring and response. As a Cato customer, they have useful data from key features such as network activity, threats, user data, devices, and all other aspects of traffic traversing the Cato platform. They can use this integration to send this data directly to Splunk, where they can easily integrate it into existing workflows for the SOC and NOC teams.

### Flows

A security analyst in Splunk identifies a suspicious event where a user accessed a high-risk application that may be associated with data exfiltration. Using Cato events alone, the analyst can see the policy decision, user identity, and application. However, the event does not show how much data was transferred or how long the session lasted.

With aggregated traffic flow data correlated to the event using the flow_id field, the analyst can view the full session context, including total bytes transferred, packet count, and session duration. This allows the analyst to determine whether the activity involved minimal interaction or a large data transfer that may indicate exfiltration.

By combining events and flow data, the analyst can quickly validate the severity of the incident and take appropriate action.

## Prerequisites

- To add a connector, you must have editor permission for **Integrations** (in the **Resources** section). For more information, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).
- The Splunk URL and port are the HEC endpoint to access your account. In general, this is the web URL you use to access Splunk with the characters "http-inputs-" appended to the beginning. For example, if your account is **http://mydomain.splunk.com**, you would use **https://http-inputs-mydomain.splunkcloud.com/**. For more details, see the [Splunk documentation](https://help.splunk.com/en/splunk-enterprise/get-started/get-data-in/9.2/get-data-with-http-event-collector/set-up-and-use-http-event-collector-in-splunk-web). The port is optional, and we use 443 if you do not specify anything else (which is the default for Splunk Cloud).
- Review the prerequisites for all Cato event integrations in [Getting Started with Event Integrations](/v1/docs/getting-started-with-event-integrations).

## Creating the Splunk Integration

Add a Splunk integration to send Cato events and flows to a Splunk HTTP Event Collector (HEC) endpoint. To set up the integration, create a HEC token in Splunk, create a new Splunk integration in the CMA, and enter the ingestion URL and API key.

In the configuration process, you can configure whether to integrate **Events**, **Flows**, or both. The default is to export only **Events**. The **Flows** data source can generate a significantly higher volume of data compared to Events. The exact volume depends on your traffic. The CMA supports configuring multiple integrations, allowing you to send different data sources as needed.

**Note:**

- For Splunk Enterprise (self-managed) integrations:
  - The Splunk HEC endpoint must be reachable over the Internet (that is, exposed via a public IP address or public DNS name). Private IPs or internal-only endpoints are not supported.
  - TLS inspection must be enabled, and the endpoint must present a valid X.509 certificate issued by a trusted public Certificate Authority. Self-signed certificates or privately issued CA certificates are not supported, as connections are only validated using standard CA trust chains.
- Deleting the integration in the CMA does not remove any resources created in Splunk.

**Filters**

Use filters to control which Cato events are exported to Splunk. This helps reduce ingestion costs, minimize noise, and focus investigations on the events that are most relevant to specific sites, users, or regions. You can also use filters to route different subsets of events to different SIEM environments.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36659528448669.png)

Use filter groups to define filters based on any [Event Field](/v1/docs/understanding-event-fields) or combination of fields. Conditions within each group use AND logic. OR logic is applied between groups. The filters in the screenshot configure the integration to export:

- Events that **originate** from Paris or Madrid, are of **sub-type** Internet Firewall, and resulted in **actions** other than Monitor or Prompt
- **Username** contains Test

**To create the Splunk integration:**

1. In your Splunk account, create a new Event Collector token to use for this integration. For details, see the [Splunk documentation](https://help.splunk.com/en/splunk-enterprise/get-started/get-data-in/10.0/get-data-with-http-event-collector/set-up-and-use-http-event-collector-in-splunk-web). You can define a custom Index or use the default Index for the token.
2. Copy the token value that is displayed. You need it to configure the integration with Cato.
3. From the CMA, select **Resources > Integrations**.
4. On the **Configured Integrations** tab, click **New**. The **New Integration** panel opens.
5. Select **Splunk** and configure the following fields:
  1. In the **Auth dropdown**, select **API Key**.
  2. Enter a **Connector Name** and optional **Description** for this integration.
  3. Enter the **Ingestion URL** for your Splunk environment as explained in the [Splunk documentation](https://help.splunk.com/en/splunk-enterprise/get-started/get-data-in/10.0/get-data-with-http-event-collector/set-up-and-use-http-event-collector-in-splunk-web#ariaid-title6).
  4. Enter the **API Key** that you created in Splunk.
  5. Specify the **Index** that receives the data from Cato. If you leave this blank, Cato uses the default Index defined on the HEC token.
  6. Whether to integrate **Events**, **Flows**, or both.
  7. Optional: Add filters to control which Cato events are sent to Splunk. **Note:** Filters only apply to Events.
  8. Specify whether to create an event when integration errors occur.
6. Click **Save**.

The integration status appears in the **Configured Integrations** tab.

## Choosing Between the Native Turnkey and Custom GitHub Integration Methods

In addition to the native turnkey integration described in this article, you can also integrate Cato events with Splunk using the tools in the Cato [GitHub account](/v1/docs/introduction-to-the-cato-github-account). Each approach offers distinct advantages depending on your goals and environment. You can also use both integrations if needed.

### When to Use the Native Integration

Cato’s native integration offers a scalable and supportable solution with minimal configuration. Benefits of the native integration include:

- Handles large volumes of events efficiently with no API-based limitations
- Is fully maintained and supported by Cato
- Supports filters to fine-tune the data sent to Splunk

### When to Use the GitHub Integration

The GitHub integration provides flexibility for advanced use cases where custom data sources or processing logic are needed. You might want to use this integration in the following situations:

- You want to send data from Cato's Audit Log to Splunk
- You want to use the Cato GitHub repository as an open-source resource to customize the integration

## Known Limitations

- **Large event limitation:** Incident information may be truncated when sent to Splunk if the raw_data field (which includes story information) exceeds 5 MB in size (this is the Splunk default, but it can be increased).
