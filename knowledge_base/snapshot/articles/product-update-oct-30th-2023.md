---
title: "Product Update - Oct. 30th, 2023"
slug: "product-update-oct-30th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-oct-30th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Oct. 30th, 2023

## New Features & Enhancements

- **BGP Routes Summarization is now Supported for Socket Sites:** You can [aggregate multiple individual routes](/v1/docs/working-with-bgp-summary-routes) into a route summary. You can add BGP communities for the summary routes as an option.
  - Supported for Socket sites running v19.0 and higher

## Cato SDP Client Releases

- **Reminder - Important Updates for Legacy Clients and Windows OS Version:** Cato has announced important End of Life (EoL) updates that impact Client connectivity from November 1st, 2023:
  - End of Life for all Client versions earlier than version 5.0
  - End of Support for Windows version 8.1 and below

## PoP Announcements

- Added the following [IP Ranges Owned by Cato Networks](/v1/docs/production-pop-guide)
  - 202.75.240.0/21
  - 216.252.176.0/20
- The following ranges will be added to these PoP locations:
  - **Boston, United States:** 216.205.119.0/24
  - **Detroit, United States**: 216.205.116.0/24
  - **Hong Kong, HK:** 202.75.242.0/24
  - **Las Vegas, United States**: 216.205.118.0/24
  - **Manchester, United Kingdom**: 216.252.178.0/24
  - **Milan, Italy**: 216.252.177.0/24
  - **Minneapolis, United States:** 216.205.117.0/24

## Security Updates

- **IPS Signatures:**
  - Malware BunnyLoader (New)
  - CVE-2023-4596
  - CVE-2023-39110
  - CVE-2023-39109
  - CVE-2023-39108
  - CVE-2023-38646
  - CVE-2023-35078
- **Suspicious Activity Monitoring:** These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
  - Tactical RMM - Download
  - VulnRecon - Download
- **Apps Catalog:** Added dozens of new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), including these highlights:
  - Amazon Prime Video (Enhancement)
  - Bittorent (Enhancement)
  - Dropbox (Enhancement)
- **Detection and Response:** These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
  - Threat Hunting IOA signatures:
    - HTTP Client Downloaded a portable executable
    - Suspected Exfiltration to Cloud Storage Applications
    - Suspicious Response Headers
  - Threat Prevention IOA signatures:
    - BitTorrent Outbound Communication
    - Common Scanners Not-Blocked (Inbound)
    - Known Scanner (Outbound)
    - Low Reputation Target Communication

## Knowledge Base Updates

[Security Playbook - Malicious Target Communication](/v1/docs/xops-security-playbook-suspicious-target-communication)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
