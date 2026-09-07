---
title: "Product Update - July 24th, 2023"
slug: "product-update-july-24th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-july-24th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - July 24th, 2023

## New Features & Enhancements

- **License Bandwidth Management for China and Vietnam Sites:** Over the next few weeks, we are gradually rolling out an enhancement that lets you view and assign the regional and global bandwidth site licenses for the China and Vietnam regions.
  - Provides clear visibility of the maximum regional and global bandwidth site licenses (**Administration > License**)
  - Manually assign and un-assign regional and/or global bandwidth licenses for sites in the China and Vietnam regions
  - There is no impact on traffic or settings in your account
- **Change in Navigation Menu:**
  - **Catalogs Move to Assets Section:** The **App Catalog** and **Threat Catalog** screens are now located under the **Assets** section.
    - Previously they were located under the **Monitoring** section
  - **Reports Move to Monitoring Section**: The **Reports** screen is now located under the **Monitoring** section.
    - Previously it was located under the **Administration** section

## Cato SDP Client Releases

- **Gradual Rollout of macOS Client v5.4**: We are starting the gradual rollout of macOS Client v5.4 the week of July 23rd, 2023. For more information about the features and bug fixes in this version, see [Summary of macOS Client Releases.](/v1/docs/summary-of-cato-macos-client-releases)
- **Android Client v5.0.1.112:** Android Client version 5.0.1.112 is available for download from the Google Play Store. This version contains infrastructure improvements for future versions. For more information, see [Summary of Cato Android Client Releases](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsupport.catonetworks.com%2Fhc%2Fen-us%2Farticles%2F11276499734685&amp;data=05%7C01%7Cyaakov.simon%40catonetworks.com%7Cf4c28afff0314975c38e08db88329c53%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638253523216045167%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&amp;sdata=nfjbZs7%2BNWdN%2FIEu6IrlEaU3J4%2BJFlP6RRn%2Bw1WwAxA%3D&amp;reserved=0).

## Security Updates

- **Application Database:**
  - Added more than 100 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcatonetworks.us16.list-manage.com%2Ftrack%2Fclick%3Fu%3D75bb2b7bafe7526c787475fd2%26id%3Dbaf6fede53%26e%3Dfd0756a33e&amp;data=05%7C01%7Cmichael.goldberg%40catonetworks.com%7Cb2ffed98fd314a105c8908db7d65cff3%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638241648484607138%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&amp;sdata=QeTqFcLYomMiNoryQ2Abk%2BbTQpQcp74XHlfNqAgYQxg%3D&amp;reserved=0)), including:
    - Threads
    - Windstream Video Conferencing
- **IPS Signatures:**
  - CVE-2020-12641: Roundcube Webmail Remote Code Execution
  - CVE-2021-27876: Veritas Backup Exec Agent File Access
  - CVE-2021-27877: Veritas Backup Exec Agent Remote Code Execution
  - CVE-2022-2414: Dogtag PKI XML External Entity Injection
  - CVE-2023-23333: SolarView Command Injection
  - CVE-2023-25135: vBulletin Remote Code Execution
  - CVE-2023-25717: Ruckus Wireless Devices Remote Code Execution
  - CVE-2023-32986: Jenkins File Parameters Plugin Directory Traversal
  - CVE-2023-34960: Chamilo Command Injection
  - CVE-2023-20887: Aria Operations for Networks Command Injection (Enhancement)
  - CVE-2021-27878: Veritas Backup Exec Agent Remote Code Execution (Enhancement)
  - Ransomware AlphVM (Enhancement)
- **Suspicious Activity Monitoring:**
  - Java download PE file (New)
  - PowerShell over HTTP (New)
- **Application Control Policy (CASB):**
  - New granular actions for the following apps:
    - Google Docs: View
  - Enhanced granular actions for the following apps:
    - Facebook: Comment, Login
    - Google: Login
    - MS Teams: Upload
    - Yahoo: Login
- **Data Loss Prevention (DLP):**
  - Added these new file types:
    - Toast Disk
    - Virtual CD
    - ISO Disk
    - Universal Disk Format (UDF)

## Knowledge Base Updates

- [TLS Connection Failure Over Off-Cloud or Alt-WAN Links](/v1/docs/tls-connection-failure-over-off-cloud-or-alt-wan-links)
