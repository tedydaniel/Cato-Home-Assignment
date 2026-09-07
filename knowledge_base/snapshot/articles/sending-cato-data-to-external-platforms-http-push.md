---
title: "Sending Data with the Custom HTTP Push Integration"
slug: "sending-cato-data-to-external-platforms-http-push"
updated: 2026-08-27T15:56:39Z
published: 2026-08-27T15:56:39Z
canonical: "knowledge.catonetworks.com/sending-cato-data-to-external-platforms-http-push"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sending Data with the Custom HTTP Push Integration

## Overview

For organizations that send data to systems for which there isn’t a dedicated Cato integration, we provide the Custom HTTP Push Integration.

Use the **Custom HTTP Push** integration to stream events, and optionally flows, directly to any external platform that accepts JSON or newline-delimited JSON (NDJSON) over HTTP. Data is pushed continuously as it's generated, rather than retrieved on a scheduled basis. This allows downstream systems to receive near real-time updates without polling.

### Common Use Cases

- **SIEM and SOC platforms -** Sample Company uses the [IPS Suspicious Activity Monitoring feature](https://knowledge.catonetworks.com/v1/docs/monitoring-suspicious-activity-with-ips-sam), which generates a high volume of security events. They decide to centralize this data with their existing SIEM platform, for which there's no dedicated Cato integration. Sample Company enables Events Integration and configures a Custom HTTP Push Integration pointing to their SIEM's HTTP ingestion endpoint, so that all IPS events are automatically streamed to the SIEM for correlation, alerting, and long-term retention alongside their other security data.
- **Custom log collection and analytics -** Sample Company wants to feed Cato event data into their internal analytics pipeline for operational reporting. They stand up an HTTP-based log collector to receive the data and configure a Custom HTTP Push Integration in their Cato account, so that events are pushed continuously to the collector as they're generated, without needing to poll Cato for updates.

### Delivery Reliability

Data is sent using best-effort delivery. If a destination endpoint becomes unavailable or returns an authentication error, Cato automatically attempts to reconnect using the following schedule:

- **Short-term retries:** 1 min, 5 min, 10 min, 15 min, 1 hr, 6 hr, and 24 hr
- **Extended retries:** Daily retries after the first 24 hours, continuing for up to 7 days

If the integration remains unable to connect for 7 days, continuous retry attempts stop for the entire integration until the endpoint configuration issue is resolved.

### Native Integrations vs. Custom HTTP Push

Cato provides purpose-built integrations for exporting events to commonly used platforms, including [Splunk](/v1/docs/integrating-cato-data-with-splunk), [Microsoft Sentinel](/v1/docs/integrating-cato-events-with-microsoft-sentinel), [CrowdStrike](/v1/docs/integrating-cato-events-with-crowdstrike), and [Azure Storage](/v1/docs/integrating-cato-events-with-azure-storage-account). When a native integration is available for your destination, we recommend using it. The advantage is that it’s optimized for that platform and may provide platform-specific capabilities.

Use the Custom HTTP Push integration when your destination does not have a dedicated integration, or when you need to deliver events to a custom application or service.

### Filters

Use filters to control which events are exported. This helps reduce ingestion costs, minimize noise, and focus investigations on the events that are most relevant to specific sites, users, or regions. You can also use filters to route different subsets of events to different SIEM environments.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36659528448669.png)

Use filter groups to define filters based on any [Event Field](/v1/docs/understanding-event-fields) or combination of fields. Conditions within each group use AND logic. OR logic is applied between groups. The filters in the screenshot configure the integration to export:

- Events that **originate** from Paris or Madrid, are of **sub-type** Internet Firewall, and resulted in **actions** other than Monitor or Prompt
- **Username** contains Test

## Prerequisites

Before configuring a Custom HTTP Push integration, verify that the destination platform supports all of the following:

- HTTP POST or PUT requests
- JSON or newline-delimited JSON (NDJSON)
- The standard Cato payload without requiring a custom request body, vendor-specific wrapper, or additional directive

The payload structure is fixed. Fields cannot be added, removed, or rearranged.

In summary:

- A destination platform is typically compatible if it can ingest plain JSON objects or an NDJSON event stream exactly as Cato sends them. Examples include SentinelOne, Securonix, and Trend AI.
- A platform is not compatible if its ingestion API requires a proprietary payload structure, such as an envelope, wrapper, or control line, to be added to the request body. Examples include Elastic and Datadog.

## Set up a Custom HTTP Push Integration

### Step 1: Gather Parameters

From your target platform, obtain:

- **Ingestion URL:** the HTTP(S) endpoint that accepts events
- **Authentication details:** the integration supports Custom Header(s), API Key, Bearer Token, or Basic Auth. If your vendor expects a prefixed value (e.g. Bearer <token>), you'll enter the entire string — prefix included — as a single value. It's stored encrypted on the Cato side.

### Step 2: Test With curl

Validate the destination independently using a command-line curl request. This isolates vendor-side issues (auth, endpoint, payload acceptance) and gives you a working request you can reuse directly in the connector setup.

The following example shows a curl request for Elastic that doesn't succeed:

```bash
curl -X POST "https://<your-elastic-endpoint>/_bulk" \
 -H "Authorization: ApiKey <KEY>" \
 -H "Content-Type: application/x-ndjson" \
 --data-binary $'{"create":{"_index":"logs-cato.events-default"}}\n{"message":"test event from curl","event_type":"test","timestamp":"2026-07-05T12:00:00Z"}\n'
```

This fails the connector's requirements, even though the curl call itself may succeed against Elastic. The payload requires a create directive line before every event line; the integration has no way to inject that extra line, since the body format is fixed.

The following example shows a curl request for SentinelOne that succeeds:

```bash
curl -i "https://ingest.us1.sentinelone.net/services/collector/raw?sourcetype=cato_events" \
 -H "Authorization: <token>" \
 -H "Content-Type: application/x-ndjson" \
 --data-binary $'{"event_type":"test"}\n'
```

This works because SentinelOne's HEC raw endpoint accepts a plain event object per line — no wrapper, no extra directive — which is exactly what the connector sends. When a curl test like this succeeds, you can use it verbatim in the connector setup:

- **URL:** paste the full endpoint including query parameters (for example, ?sourcetype=cato_events)
- **Auth:** Custom Headers → header name Authorization, value set to your real token (stored as Secret)
- **Body:** set the content type to match what you tested (application/x-ndjson here)

If your curl test succeeds, continue to step 3.

### Step 3: Configure the Connector

1. In the CMA, go to **Resources > Integrations > Configured Integrations**, and click **New**.
2. Under **Integration**, select **Custom HTTP Integration**.
3. Under **Capability**, choose **Data Export**.
4. Under **Auth**, select the method that matches what you validated with curl (Custom Headers, API Key, Bearer Token, or Basic Auth).
5. Enter a **Name** and optional **Description**.
6. Enter the **URL** — the same endpoint you tested with curl.
7. Add your **Custom Headers** (or equivalent auth fields) — carry over the exact header names and values from your successful curl command. Each value can be stored as **Secret** or **Plain**.
8. Under **Body**, confirm the content type (default is `application/json`; NDJSON is also supported).

The request body sent by the connector is **not configurable**: you cannot add custom fields or restructure the payload.

1. Under **Data Sources**, select **Events**, **Flows**, or both.
2. Optionally scope what's sent using the **Events Filter** and **Flows Filter** (match ANY of the configured filter groups). For more information, see [Filters](/v1/docs/sending-cato-data-to-external-platforms-http-push#filters1) above.
3. Choose whether to **track errors with connector events**. This is recommended so that delivery failures surface as events you can alert on.
4. Save the configuration and confirm the status shows **Connected**.

## Troubleshooting

- **Curl succeeds, but Cato shows Connectivity Error:** Double-check that headers/auth entered in Cato exactly match what you used in curl, including any required prefix (for example, Bearer) as part of the encrypted value.
- **No events are arriving at my external platform:** Check your Events Filter/Flows Filter. An overly narrow filter can silently exclude everything.
- **Vendor rejects payload:** Review the prerequisites. Your vendor likely requires a custom body structure that this connector can't produce.

## Article Changelog

| Date | Description |
| --- | --- |
| Aug 04, 2026 | - Added detailed use cases - Added [Filters](/v1/docs/sending-cato-data-to-external-platforms-http-push#filters1) section |

## FAQ

#### Q: Can I push to multiple endpoints at once?

A: You should configure a separate Custom HTTP Push integration per destination.

#### Q: Does this replace native integrations (Splunk, Sentinel, CrowdStrike, etc.)?

A: No. Where a native Cato integration exists, use it. Custom HTTP Push integrations are for platforms without a dedicated integration, or for non-SIEM destinations.

#### Q: What if my vendor isn't in the supported list?

A: Check whether their HTTP ingestion API accepts plain JSON or NDJSON without a required wrapper structure. If so, test with curl first, then configure the connector as described on this page.

#### Q: Can I customize the JSON body or add fields?

A: No. The payload schema is fixed.
