---
title: "Data Lake Storage"
slug: "data-lake-storage"
updated: 2026-06-25T14:13:22Z
published: 2026-07-02T07:05:10Z
canonical: "knowledge.catonetworks.com/data-lake-storage"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Lake Storage

## Data Lake

Data Lake provides centralized storage and retention for events generated across the Cato Cloud. It enables customers to retain, analyze, and investigate telemetry and event data across users, sites, and services.

### Licensing

Data Lake is licensed using Data Units (DU). Each Data Unit includes a fixed ingestion capacity of 2.5 million events per hour, together with a selected data retention period.

By default, each account includes one Data Unit with 3 months retention at no additional charge.

**Data retention and scaling**

Data retention is available in 3-month, 6-month, and 12-month tiers, with a single retention tier selected per account.

Customers can increase usage in two ways:

- Increase ingestion capacity by adding more Data Units at the same retention tier (for large-scale deployments generating more events)
- Increase retention period by selecting a higher retention tier (for compliance, investigation, or operational needs)

**Usage**

When event usage exceeds the licensed Data Unit capacity, events are not discarded. Excess usage is handled according to the Usage Measurement and Fair Use Policy.
