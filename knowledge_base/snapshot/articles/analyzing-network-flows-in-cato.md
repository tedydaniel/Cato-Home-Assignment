---
title: "Analyzing Network Flows in Cato"
slug: "analyzing-network-flows-in-cato"
updated: 2026-06-15T09:34:13Z
published: 2026-06-22T09:20:31Z
canonical: "knowledge.catonetworks.com/analyzing-network-flows-in-cato"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Analyzing Network Flows in Cato

## Overview

Cato provides flow-level visibility for traffic that is inspected and processed by the Cato Cloud. Flow data helps you investigate traffic behavior, understand policy decisions, analyze application usage, and review routing decisions across your environment.

Cato flow data helps admins perform many of the same tasks as NetFlow, IPFIX, and sFlow, such as traffic monitoring, troubleshooting, reporting, and forensic analysis. However, Cato flow data is enriched with context of the single pass architecture, which includes application-level, user, site, policy, and security information.

You can work with flow data in real time or export and query it for external workflows:

- Use the Cato Management Application (CMA) for native analysis based on Cato objects and entities.
- Push data to turnkey integrations, third-party SIEMs, or cloud storage
  - Structured flow analysis based on your existing tools and workflows
- Use the Cato GraphQL API to query data for custom workflows. This helps you build dashboards, automate investigations, and retrieve data programmatically

## Understanding Cato Flow Data

A flow represents a traffic session processed by a PoP in the Cato Cloud. Cato generates flow data for traffic evaluated by Cato services, multiple networking and security engines that simultaneously analyze and process traffic flows.

Each flow record includes the context needed to understand how Cato processed the traffic. This helps admins investigate flows by Cato objects and entities, such as applications, sites, users, firewall rules, and network rules. This approach lets you analyze traffic using Cato objects and entities instead of relying only on basic network metadata. For example, admins can investigate flows by application, site, user, firewall rule, or network rule.

Cato does not require separate NetFlow, IPFIX, or sFlow collectors at each branch. The Cato Cloud processes traffic inline and generates enriched flow data from the same inspection pipeline that applies networking, remote access, and security policy decisions. This gives admins centralized visibility across sites, users, applications, and policies through the CMA, supported integrations, and the Cato API.

## Native Discovery in the CMA

The CMA provides native analysis of Cato flow data using the same Cato objects and entities that you configure and monitor in the CMA. This helps you investigate traffic in its native context, including sites, users, applications, firewall rules, and network rules.

Use the relevant CMA pages, such as events and Application Analytics, to investigate traffic and drill down into flow-level details.

## Turnkey Integrations

The CMA provides turnkey integrations for supported platforms, such as the Cato app for Splunk. This integration lets you analyze Cato flow and event data in Splunk using structured Cato fields and dashboards. This helps security and network teams correlate Cato data with other telemetry in their Splunk environment.

## Configuring Third-Party Integrations

Cato supports additional methods to send or retrieve flow-related data for external systems. The available data, fields, and behavior can vary depending on the integration method.

### Pushing Data to SIEM and Cloud Storage

Cato can push event and flow-related data to external systems. Use this option when you need to ingest Cato data into a SIEM, store data for compliance or retention, or correlate Cato data with other telemetry sources.

#### SIEM Integrations

SIEM integrations let you ingest Cato data into third-party security analytics platforms. These integrations help security teams analyze Cato events and flow-related data together with other security telemetry.

For more information, see the relevant SIEM integration documentation.

#### Cloud Storage Integrations

Cato can push data to cloud storage for ingestion by external tools or for retention workflows. Supported cloud storage destinations include:

- AWS S3
- Azure Blob

External tools can then retrieve the data from the cloud storage destination for analysis, reporting, or archival workflows.

### Pulling Data with the Cato GraphQL API

You can use the Cato GraphQL API to query data for custom dashboards, automation, reporting, and investigations. This option is useful when you need programmatic access to Cato data for workflows that are not covered by native pages or supported integrations.

For more information, see What is the Cato API.
