---
title: "Getting Started with Event Integrations"
slug: "getting-started-with-event-integrations"
updated: 2026-08-11T13:44:02Z
published: 2026-08-11T13:44:02Z
canonical: "knowledge.catonetworks.com/getting-started-with-event-integrations"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with Event Integrations

## Overview

The Cato service generates rich and granular events, providing comprehensive visibility across network and security features. You can directly consume these events in the following ways:

- Directly in the Cato Management Application (see [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network))
- A high-scale feed to Cloud Storage, such as [AWS S3](/v1/docs/integrating-cato-events-with-aws-s3) and Azure Blob Storage
- Using the [Cato API](https://api.catonetworks.com/documentation/#definition-EventFieldName)

Event Integrations let you automatically forward Cato event data to external platforms and storage destinations for retention, monitoring, and analysis. This helps you use Cato events in your existing SOC, SIEM, and data lake workflows without manually exporting data or continuously polling for it.

Depending on the integration type, Cato either continuously uploads events to cloud storage, forwards data directly to a supported third-party platform through a native connector, or streams events and flows to a compatible HTTP endpoint using the [Custom HTTP Push integration](/v1/docs/sending-cato-data-to-external-platforms-http-push). Use the Custom HTTP Push integration when the destination platform has no dedicated Cato integration and can accept the standard Cato JSON or NDJSON payload.

### Filtering Events

The available filtering options depend on the integration type:

- Cloud storage integrations, such as Amazon S3 and Azure Storage, support filtering by event type or sub-type.
- Native CMA integrations for SIEMs, such as CrowdStrike, Microsoft Sentinel, and Splunk, support filter groups. These groups let you filter events using fields such as action, severity, rule name, application, site, or user.

### Prerequisites

- If access to the third-party service is limited to specific IP addresses, see this [article](https://support.catonetworks.com/hc/en-us/articles/20511945810589) for the Cato IP addresses that you need to allow (you must be signed in to view this article).
- You can define up to three Event Integrations for your account.

## Turnkey Integrations

Forward events directly to the following SIEM solutions and storage accounts using native connectors configured in the CMA.

For information about license requirements for third-party integrations, see [License and Apps for Cato Third-Party Integrations](/v1/docs/license-and-apps-for-cato-third-party-integrations).

| Vendor | Cato Knowledge Base Documentation |
| --- | --- |
| ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image-1786438147928.png) | [Integrating Cato Events with CrowdStrike Falcon NG-SIEM](/v1/docs/integrating-cato-events-with-crowdstrike) |
| ![Microsoft Sentinel](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28357341749149.png) | [Integrating Cato Events with Microsoft Sentinel](/v1/docs/integrating-cato-events-with-microsoft-sentinel) |
| ![Splunk](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28357372258205.png) | [Integrating Cato Events with Splunk](/v1/docs/integrating-cato-data-with-splunk) |
| ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(171).png) | [Integrating Cato Events with AWS S3](/v1/docs/integrating-cato-events-with-aws-s3) |
| ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(173).png) | [Integrating Cato Events with Azure Storage](/v1/docs/integrating-cato-events-with-azure-storage-account) |

## Custom HTTP Push Integration

For organizations that send data to systems for which there isn’t a dedicated Cato integration, we provide the [Custom HTTP Push Integration](/v1/docs/sending-cato-data-to-external-platforms-http-push).

Use the **Custom HTTP Push** integration to stream events, and optionally flows, directly to any external platform that accepts JSON or newline-delimited JSON (NDJSON) over HTTP. Data is pushed continuously as it's generated, rather than retrieved on a scheduled basis. This allows downstream systems to receive near real-time updates without polling.

## Third-party Integrations

To learn about the many other services which integrate with Cato, see [catonetworks.com/integrations/](https://www.catonetworks.com/integrations/)
