---
title: "Product Update - May 29th, 2023"
slug: "product-update-may-29th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-may-29th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - May 29th, 2023

## New Features & Enhancements

- **Look-and-Feel Update to Cato API GraphQL Playground:** As part of enhancing the Cato API server infrastructure, we are making some cosmetic changes to the GraphQL playground.
  - There is no change or impact to API queries, scripts, and configurations
  - We recommend that you only use the GraphQL playground as a test or staging environment. The content in the playground is not persistent and can be deleted
- **Audit Trail Includes SaaS Security API:** The [Audit Trail](/v1/docs/using-the-audit-trail) now shows changes in the [SaaS Security API](/v1/docs/what-is-the-data-protection-api) policy, including:
  - Creating and deleting connectors
  - Editing, creating, and deleting Threat Protection and Data Protection rules

## Cato SDP Client Releases

- **macOS Client v5.4 / Linux Client v5.1:** We are updating the rollout plans for macOS Client v5.4 and Linux Client v5.1. These Clients will start gradual rollout in the next few weeks.
  - For more information about the features in these versions, see [Summary of Client Releases](/v1/docs/summary-of-cato-client-releases)

## Security Updates

- **Application Database:**

**IPS Signatures:**
  - Added more than 100 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - CyberghostVPN
    - IPvanishVPN
    - MullvadVPN
    - PrivateInternetAccessVPN
    - ProtonVPN
    - PureVPN
    - SurfsharkVPN
    - TunnelbearVPN
  - Enhanced these SaaS applications:
    - ExpressVPN (Enhancement)
    - Naver (Enhancement)
    - Line Works (Enhancement)
  - Ransomware RA Group (New)
  - Ransomware SHTORM (New)
  - Ransomware Akira (New)
  - CVE-2023-28432
  - CVE-2023-28231
  - CVE-2023-27350
  - CVE-2023-24949
  - CVE-2022-45928
  - CVE-2022-45926
  - CVE-2022-45925
  - CVE-2022-45924
  - CVE-2022-43938
  - CVE-2022-43771
  - CVE-2022-41828
  - CVE-2021-34427
  - CVE-2020-36222
- **Suspicious Activity Monitoring:**
  - Remote Execution - CSExec (New)
  - Remote Execution - PAExec (New)
  - Remote Execution - RemCom (New)
  - Remote Execution - WinRM via PowerShell (New)
  - Remote Execution - WinRS (New)
  - Remote Execution - Impersonated CsExec (New)
  - Upload Bash Script (New)
  - Upload JSP Web Shell (Enhancement)

## Knowledge Base Updates

- [Android Devices Unable to Reach Internal Resources Via Cato](/v1/docs/android-devices-unable-to-reach-internal-resources-via-cato)
- [Download of EICAR Files Are Not Getting Blocked by Cato](/v1/docs/download-of-eicar-files-are-not-getting-blocked-by-cato)
