---
title: "Integrating Cato Data with Datadog"
slug: "integrating-cato-data-with-datadog"
updated: 2026-09-01T11:19:45Z
published: 2026-09-06T06:00:18Z
canonical: "knowledge.catonetworks.com/integrating-cato-data-with-datadog"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating Cato Data with Datadog

## Overview

The Datadog integration lets you analyze Cato network and security data alongside data from other sources in Datadog. You can use this data for dashboards, monitors, alerts, and log analytics without deploying additional data collection mechanisms.

Cato sends normalized events and, optionally, network flows directly to your Datadog account. You configure the native Datadog integration in the Cato Management Application (CMA).

## Use Cases

### Events

You can send Cato events to Datadog to centralize security monitoring and observability. The events provide data about network activity, threats, users, devices, and traffic traversing the Cato platform. SOC and NOC teams can incorporate this data into their existing monitoring and investigation workflows.

### Flows

When investigating suspicious activity, you can use aggregated flow data to add network context to Cato events. Events show information such as policy decisions, user identity, and applications. Flow data adds details such as total bytes transferred, packet count, and session duration.

This additional context helps you distinguish minimal activity from large data transfers that can indicate potential data exfiltration.

## Prerequisites

Before configuring this integration, ensure the following:

- You have **Editor** permission for Integrations in the **Resources** section of the CMA. See [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).
- You have reviewed the prerequisites for all Cato event integrations in [Getting Started with Event Integrations](/v1/docs/getting-started-with-event-integrations).
- You have a Datadog account with permissions to create an API key.
- You have your **Datadog Site** URL (for example: `datadoghq.com`, `datadoghq.eu`).

## Data Sources

You can configure the integration to send **Events**, **Flows**, or both.

### Events

- Generated when specific activity occurs in the network or system (for example, when a policy rule is matched or a threat is detected).
- Provide discrete, real-time insights into security and policy enforcement.
- Sent using Cato's event schema.
- **New integrations export only Events by default.**
- Filtering is supported for Events.

### Flows

- Originate as network flows (5-tuple), enriched with application-level information from Cato engines.
- Include application and user context, plus aggregated session data: bytes, packets, and duration.
- Can generate significantly higher data volume than events. The exact volume depends on traffic.

## Creating the Datadog Integration

To send Cato events and flows to Datadog, you’ll create an integration in the CMA using an API key from Datadog.

### Step 1: Obtain a Datadog API Key

1. Log in to your Datadog account.
2. Navigate to **Organization Settings** > **API Keys**.
3. Click **New Key**, enter a descriptive name (for example, `Cato Integration`), and click **Create Key**.
4. Copy and save the **API Key** value. It will not be shown again.
5. Note your **Datadog Site** (visible in the URL, for example, `datadoghq.com`).

### Step 2: Test with curl

Before configuring the integration in the CMA, validate that your Datadog API key and ingestion endpoint work by sending a test log directly from the command line. This isolates any vendor-side issues (auth, endpoint, payload acceptance) before you touch the CMA.

The Datadog Logs ingestion API uses the `DD-API-KEY` header for authentication. Cato sets the `source` field to `cato` and uses a `data_source` tag to distinguish events from flows in Datadog Log Explorer.

**Example — Datadog (US site):**

  

```plaintext
curl -X POST "https://http-intake.logs.datadoghq.com/v1/input" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "DD-API-KEY: <your-api-key>" \
  -d '[
    {
      "ddsource": "cato",
      "ddtags": "env:staging,version:5.1",
      "message": { "message":"test event from curl","event_type":"test","timestamp":"2026-07-05T12:00:00Z" }
    }
  ]'
```

Replace `&lt;YOUR_API_KEY&gt;` with the API key obtained in Step 1, and use the ingestion URL that matches your Datadog site.

A successful response returns HTTP `202 Accepted`. You can then verify the log appears in Datadog under **Logs** > **Search**, filtering by `source:cato`.

### Step 3: Configure the Integration in the CMA

![Screenshot 2026-08-02 at 22.04.38.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1788261074594.png)

  

1. From the navigation menu, go to **Resources** > **Integrations**.
2. Click the **Configured Integrations** tab, then click **New**.
3. In the **New Integration** panel, select **Datadog** from the integration dropdown.
4. The **Capability** is automatically set to **Data Export**.
5. In the **Auth** dropdown, select **API Key**.
6. Enter a **Name** for the integration (required).
7. Optionally, enter a **Description**.
8. Enter the **Datadog Site** (for example: `datadoghq.com`).
9. Enter the **API Key** you copied from Datadog.
10. Under **Data Sources**, select **Events**, **Flows**, or both.
11. Optionally, configure **Events Filter** and/or **Flows Filter** groups to control which data is sent (see Filters below).
12. Click **Save**.
13. Refresh the Integrations page. The integration appears in the **Configured Integrations** table with a **Connected** status.

## Filters

Filters let you control which Cato events (and flows) are exported to Datadog.

- Help reduce ingestion costs, minimize noise, and focus investigations.
- Allow routing different subsets of events to different platforms.
- Filter groups are defined based on any **Event Field** or combination of fields.
- Conditions **within** each group use **AND** logic; **OR** logic is applied **between** groups.

### Events Filter

Available in the New Integration panel under **Events Filter**. Click **Add Filter** to define a condition, or **Add Group** to create an additional filter group (OR logic between groups).

### Flows Filter

Available under **Flows Filter** when Flows is selected as a data source. Follows the same logic as the Events Filter.

## Troubleshooting

| Issue | Solution |
| --- | --- |
| Integration shows **Connectivity Error** | Verify the Datadog Site URL and API Key are entered correctly. Ensure the API key has not been revoked in Datadog. |
| No events arriving in Datadog | Check your Events Filter configuration — an overly narrow filter can silently exclude all data. |
| No flows arriving in Datadog | Confirm **Flows** is selected under Data Sources, and check the Flows Filter for overly restrictive conditions. |
| Integration saved but status does not show **Connected** | Refresh the Integrations page. If the issue persists, verify your Datadog API key permissions. |
