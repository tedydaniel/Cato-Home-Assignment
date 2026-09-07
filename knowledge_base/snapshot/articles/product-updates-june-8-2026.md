---
title: "Product Updates - June 8, 2026"
slug: "product-updates-june-8-2026"
updated: 2026-06-29T13:04:27Z
published: 2026-06-29T13:04:27Z
canonical: "knowledge.catonetworks.com/product-updates-june-8-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - June 8, 2026

## New Features & Enhancements

- **Granular Filtering for Event Integrations:** Optimize SIEM ingestion for events by applying granular filters before they are ingested by external integrations.
  - Filter events by specific event fields, such as action, severity, rule name, application, site, or user
  - Only relevant events are ingested to integrations such as Microsoft Sentinel, Splunk, and CrowdStrike
  - Reduce low-value event ingestion while preserving important security and operational events

- **End of Client Support for macOS Version 13.3 and Lower:** From November 7, 2026, the Cato macOS Client will not be supported on devices running macOS v13.3 (Ventura) and lower.
  - To ensure continued support for the Cato Client, upgrade devices running these macOS versions before November 7, 2026.

- **Cloud Interconnect Sites for Internet Backhauling:** You can use Cloud Interconnect sites as gateways for Internet Backhauling rules, making it easier to route selected Internet traffic through centralized cloud connectivity.

- **Codex AI Agent Controls:** AI Security supports Codex hooks across all tenants, so you can monitor and govern Codex usage as part of your existing hooks enforcement.
  - Discover and monitor Codex activity with Scout and Hooks, including MCPs and tools
  - Define security policies for Codex interactions with the Coding Agents Policy (EA), for example, block PII from user messages to the AI agent
  - Requires AI Security for Applications license

- **Review Hardware Shipping Costs Before Confirmation:** To help you review charges and avoid unexpected costs, view the shipping costs in the CMA for each hardware item before you confirm the shipment.

- **Interaction Explorer for AI Security for Applications:** We added the Interaction Explorer page, which gives you a centralized view of AI interactions and related detections across multiple guards.
  - Monitor detection data alongside interaction logs
  - Requires AI Security for Applications license

## PoP Announcements

- The following new ranges are now available:
  - **Manchester, UK:** 159.117.243.0/24
  - **Santa Clara, US:** 199.27.52.0/24
  - **Singapore, SG:** 113.30.135.0/24

- **Upcoming Localized IP Range for Egypt:** The following localized IP range for Egypt (serviced through the Milan PoP location) will soon be available:
  - **EG:** 216.252.183.32/27

## Security Updates

- **Apps Catalog**

View more details about apps in the Apps Catalog.
  - New Apps: 5 new apps - Cradlepoint NetCloud, Finster AI, Kakao Map, Nigal AI, Whisper Flow
  - Enhanced Apps:
    - Notion
      - Added domain [**notionusercontent.com**](http://notionusercontent.com)
- **Application Control Policy / CASB**
  - TikTok
    - Manage Profile (New)
  - GitHub
    - Change Repository Visibility (New)
    - Create Repo (New)
    - Delete Repo (New)
- **IPS Signatures**

View more details about the IPS signatures and protections in the Threats Catalog.
  - CVE-2021-4463 (New)
  - CVE-2026-32202 (New)
  - CVE-2026-39352 (New)
  - CVE-2026-41089 (New)
  - CVE-2026-42945 (New)
  - CVE-2026-4631 (Enhancement)
  - DNS Tunneling Abusing A Queries (New)
  - DNS Tunneling Abusing AAAA Queries (New)
  - DNS Tunneling Abusing CNAME Queries (New)
  - DNS Tunneling Abusing MX Queries (New)
  - High Rate DNS Exfiltration (New)
- **XDR Indications of Attack**
  - Threat Prevention
    - cURL Communication to Low-Reputation Domains (New)
    - Modbus Scanner Activity (New)
- **Device Inventory**

These are the updates to the Device Inventory detection engine:
  - CASwell Network Appliance (New)
  - Audinate (Enhancement)
  - Compex Link-AX (Enhancement)
  - Teradek Video Encoder (New)
  - SmallHD Monitor (New)
  - Evoko Room Display (New)
  - Screencloud digital signage (New)
- **Application Control Via API and Data Protection API Integrations**

The enhancements were made for Application Control Via API
  - CrowdStrike
    - EDR (Enhancement)
      - Incident grouping now sourced from CrowdStrike's aggregate_id field for more reliable correlation, and the alerts query is scoped to product=epp (replacing the legacy type=ldt/edr filter)
  - GitHub
    - SaaS Alerts (Enhancement)
      - Replaces the new-organization-member detection with seven new detections: organization admin added, protected branch settings changed, new app installed, private repo turned public, force push to protected branch, new personal access token created, and owner role granted
