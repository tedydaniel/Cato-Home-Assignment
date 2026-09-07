---
title: "Product Updates - November 3 ,2025"
slug: "product-updates-november-3-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-november-3-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - November 3 ,2025

## New Features & Enhancements

- **Upgrade Old Client Versions:** We recently identified a bug in the following older Cato Client versions that prevents devices from connecting to the Cato Cloud. If you have devices using one of these versions, you must update immediately to restore connectivity and ensure continued service access.
  - Windows Clients v5.9 or lower
  - macOS Clients v5.5 or lower
  - iOS Clients v5.1 or lower
  - Android Clients v5.1 or lower
  - Linux Clients v5.1 or lower You can download the newest Client version from the [Client Download Portal](https://clientdownload.catonetworks.com/). For more information, see this [article](/v1/docs/legacy-client-versions-require-upgrade).
- **New Release for macOS Client v5.10.6:** In the week of November 2, 2025, we are starting to roll out macOS Client version 5.10.6. This version includes:
  - Support for a fully silent installation, including EULA suppression
  - Stability improvements
  - Security updates
  - Bug fixes
- **Improved CMA Best Practice Experience:** Gain clarity and control over your account posture with the improved [Best Practices experience](/v1/docs/reviewing-posture-checks-for-your-account). Monitor your score evolution, explore detailed breakdowns, and focus your efforts where they matter most.
  - Visualize score trends to understand progress and identify patterns
  - Filter and sort by category to uncover high-impact areas for improvement
  - Drill into specific metrics to guide targeted remediation efforts
- **Granular RBAC for Access to Advanced Groups:** You can manage which admins have view or edit access to each [advanced group](/v1/docs/working-with-cma-advanced-groups-and-groups).
  - For example, you want only specific admins to edit a group of IP ranges used in your Internet Firewall policy
- **DEM Enhancement - Underlay Performance Monitoring for Remote Users:** The [Experience Monitoring](/v1/docs/the-user-experience-monitoring-drill-down-page-remote-and-office-users) (DEM) page now shows packet loss and distance metrics specific to the last-mile underlay for Client traffic. This helps identify and diagnose out-of-tunnel issues that could impact last-mile performance for remote users.
  - The new metrics are shown in the **Underlay Probes** section in the **Last Mile** tab for a specific user
  - Requires Client versions macOS 5.10 or Windows 5.17 (or higher)
- **Reminder – Upcoming Deprecation of ILMM Scheduled Maintenance Page:** As part of the migration of the ILMM service to the CMA, the [ILMM Scheduled Maintenance](/v1/docs/managing-ilmm-for-your-account) page will be deprecated on Nov. 21 and fully replaced by the [Mute Stories](/v1/docs/muting-xops-stories) policy.
  - After Nov. 21, create Mute Stories rules to suppress alerts during planned maintenance windows
  - Important: Existing Scheduled Maintenance entries **will not be automatically migrated** to the Mute Stories policy
  - For more details, see the [original announcement](/v1/docs/upcoming-migration-of-ilmm-service-to-the-cma)

## PoP Announcements

- **New Localized IP Range for Bosnia and Herzegovina:** The following new localized IP range for Bosnia and Herzegovina (serviced through the Prague PoP location) is now available:
  - **BA:** 209.206.22.128/27

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
