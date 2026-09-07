---
title: "Product Update - Dec. 25th, 2023"
slug: "product-update-dec-25th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-dec-25th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Dec. 25th, 2023

## New Features & Enhancements

- **PingFederate Supported for SSO Authentication:** [PingFederate](/v1/docs/configuring-pingfederate-sso-for-your-account) can be used by remote users and Cato Management Application admins to authenticate with SSO.

## PoP Announcements

- The following IP range is now available in this PoP location:
  - **Ashburn, VA:** 150.195.206.0/24

## Security Updates

- **IPS Signatures:** View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - Ransomware BuLock (Enhancement)
  - Ransomware Fun (Enhancement)
  - Malware Amadey (New)
  - Malware Amadey CnC Check-In (New)
  - Malware Arkei Stealer Variant (New)
  - Malware DCRAT Activity (GET) (New)
  - Malware Koadic Malware (New)
  - Malware Mars Stealer Variant (New)
  - Malware Redline Stealer TCP CnC - Id1Response (New)
  - Malware Vidar Stealer Variant (New)
  - CVE-2023-50164 (New)
  - CVE-2023-46214 (New)
  - CVE-2023-2986 (New)
  - CVE-2023-29798 (New)
  - CVE-2022-22956 (New)
  - CVE-2017-6884 (New)
  - CVE-2020-1472 (Enhancement)
  - CVE-2023-20273 (Enhancement)
- **Detection & Response** These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
  - Threat Hunting Indication:
    - Protected ZIP Download from Low-Reputation Sources (New)
    - Downloading a Suspicious Script (Enhancement)
    - Malware Activity (Enhancement)
    - Suspicious Network Activity (Enhancement)
    - Suspicious Trello API usage (Enhancement)
    - WebShell uploaded (Enhancement)
  - Threat Prevention Indication:
    - Suspicious Network Activity JA3 (Enhancement)
    - BitTorrent Outbound Communication (Enhancement)
- **Suspicious Activity Monitoring:** This protection was added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
  - Downloaded a password protected archive file (New)
- **TLS Inspection:**
  - Added global bypass for these apps and FQDNs, preventing possible TLS inspection errors:
    - **Apps**:
      - Huawei Technologies Co. Ltd
    - **FQDNS**:
      - supportview.com
      - ota-cloudfront.net
- **Apps Catalog:** Added over 450 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), and enhanced this application:
  - Viber
- **Application Control (CASB):**
  - New granular actions for the following apps:
    - Gmail download attachment (New)
    - Google Photos - download (New)
    - Workplace - upload files (New)
    - OneDrive Personal - download and upload (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
