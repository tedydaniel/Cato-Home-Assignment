---
title: "Product Update - August 8th, 2022"
slug: "product-update-august-8th-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-august-8th-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - August 8th, 2022

## New Features & Enhancements

- **First Upgraded Users for Client Upgrade:** For the Automatic Silent Upgrade and User Upgrade policy for Windows and macOS Clients, you can define a group of users that are the first to receive the Client upgrade to the new version. You can monitor these users and review the new Client behavior. [Read more](/v1/docs/recommendations-for-cato-client-upgrades).
- **Enhanced DLP Support for OpenOffice Files:** DLP Data Control Rules (Security > Application Control) now supports OpenOffice files as an out-of-the-box file type. [Read more](/v1/docs/creating-the-data-control-policy).
- **Exporting Events and Users Requires Admin Editor Permissions:** Now only Cato Management Application admins with **Editor** permissions can export events or users.
  - Exporting events – Monitoring > Events ([read more](/v1/docs/analyzing-events-in-your-network))
  - Exporting users – Access > Users ([read more](/v1/docs/exporting-user-data))
- **Update to the Users Screen:** Starting on August 14th, 2022, the Users screen (Access > Users) will also show the following information: **User Principal Name** and **Authentication Method**. [Read more](/v1/docs/working-with-analytics-for-specific-sdp-users).

## Cato SDP Client Releases

- **Windows Client v5.4:** Starting the week of August 7th, we are planning to start the gradual release of the Windows Client version 5.4. This version includes:
  - Improved error messages in the Client for SDP users which better explain connectivity issues
  - Performance enhancements
  - Also includes infrastructure for upcoming features
  - Bug fixes:
    - When the Client is in Office Mode, it now uses the PAC file of the local system instead of the PAC file defined in the Cato Management Application

## PoP Announcements

- **Bogota, Colombia:** A new Cato PoP is now available in Bogota

## Security Updates

- **IPS Signatures:**
  - Malware Electron Bot
  - Malware LockBit 3.0
  - CVE-2022-32275
  - CVE-2022-29499
  - CVE-2022-26133
  - CVE-2022-25546
  - CVE-2022-24497
  - CVE-2022-24491
  - CVE-2022-23270
  - CVE-2021-44864
  - CVE-2021-35211
  - CVE-2016-6366
  - CVE-2015-2051
  - Google Hacking Database exploits (Enhancment)
- **Application Database:** Updated app definitions in the Cato Cloud:
  - Show the SaaS apps in Monitoring > Cloud Apps Catalog
- **Application Control Policy:** New granular actions added to these apps:
  - ClickUp - Download file, Change status, Assign, Upload file, Create task
  - Confluence - Edit, Share, Post (Publish)
  - Exavault - Download, Upload
  - Hubspot - Export
  - Monday - Add Person To Item, Change Task Status, Create Task
  - Wrike - Upload, Download
- **Data Loss Prevention:**
  - OpenOffice Documents (New Group):
    - OpenDocument Spreadsheet(ods,ots)
    - OpenDocument Presentation(odp,otp)
    - OpenDocument Text(odt,ott)

## Knowledge Base Updates

- [Monitoring Users with a Snapshot](/v1/docs/monitoring-users-with-a-snapshot)
