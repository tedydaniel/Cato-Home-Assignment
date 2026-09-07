---
title: "Product Update - July 10th, 2023"
slug: "product-update-july-10th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-july-10th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - July 10th, 2023

## New Features & Enhancements

- **LAN Firewall Enhancement:** The **Upgrade to LAN Firewall** action now also supports [migrating the Local Routing rules](/v1/docs/upgrading-the-local-routing-policy-to-the-lan-firewall) to the [LAN Firewall policy](/v1/docs/configuring-the-socket-lan-firewall-policy).
  - After the migration, the Local Routing rules are applied with the default action **Allow Locally**, with no change or impact to functionality
  - You can then configure the migrated rules in the new LAN Firewall policy
- **Enhanced Troubleshooting for TLS Inspection:** To help resolve issues related to [TLS Inspection](/v1/docs/configuring-tls-inspection-policy-for-the-account), we added new events and fields that provide more details. For example, values for the **TLS Error Description** include: unsupported certificate, certificate revoked, unknown CA, no certificate, handshake failure.
  - The new events are generated automatically, without needing to configure an action
  - [New fields](/v1/docs/understanding-event-fields) include: **TLS Error Description**, **TLS Error Type**, **TLS Version**, **Traffic Direction**
- **Cato Management Application Enhancement:**
  - **Enhancement to Stories Investigation:** Under **Detection & Response >** [**Stories Workbench**](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) each story includes a new widget called **Targets Action Status** allowing a quick overview of the relevant events for every target.
    - The information in this widget replaces the **Events** field in the **Details** widget.

## Security Updates

- **Application Database:**
  - Added more than 100 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - Disney Plus
    - Google Photos
  - Enhanced these SaaS applications:
    - ExpressVPN
- **IPS Signatures:**
  - Ransomware Rhysida (New)
  - Ransomware 8Base (New)
  - CVE-2023-34843
  - CVE-2023-29084
  - CVE-2023-2554
  - CVE-2023-24950
  - CVE-2023-1389
  - CVE-2022-32995
  - CVE-2023-28231 (Enhancement)
  - CVE-2022-43771 (Enhancement)
  - Phishing Heuristic (Enhancement)
- **Application Control Policy (CASB):**
  - New granular actions for the following apps:
    - Google Docs: View
    - Google Drive: View
    - Google Photos: Upload
    - Dropbox: View
  - Enhanced granular actions for the following apps:
    - Dropbox: Download and Login
    - Outlook: Send mail
- **TLS Inspection:**
  - Google Hangouts (New)
  - Google Calendar (New)
  - Google Plus (New)
  - Google Maps (New)
  - Google Docs (New)
