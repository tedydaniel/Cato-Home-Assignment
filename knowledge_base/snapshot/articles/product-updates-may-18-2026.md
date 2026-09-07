---
title: "Product Updates - May 18, 2026"
slug: "product-updates-may-18-2026"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-may-18-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - May 18, 2026

## New Features & Enhancements

- **Adaptive Access for WAN Sessions**: Control whether active WAN sessions are terminated as part of the [Client Connectivity Policy](/v1/docs/configuring-the-client-connectivity-policy) when they no longer meet the conditions for WAN access. This limits the risk of continued WAN access after authorization, such as confidence level, is reduced.
  - For example, if a user is granted WAN access based on their confidence level and their authentication token expires, this setting determines whether their current WAN sessions are disconnected
  - No change in behavior for existing rules - WAN sessions are not dropped
- **Benchmark Your Account Posture:** The [Posture page](/v1/docs/reviewing-posture-checks-for-your-account) helps you compare your account posture with other organizations in your industry so you can identify and prioritize improvements based on benchmarks. Additional enhancements to the Posture page include:
  - Share feedback, and track important posture-related changes
  - View posture-related events, including score changes and new checks
- **New Android Client v5.5.1:** During the week of May 17, 2026, [Android Client version 5.5.1](/v1/docs/summary-of-cato-android-client-releases) will be available for download from the Google Play Store. This version includes:
  - Stability improvements
  - Security updates
  - Bug fixes
- **New iOS Client v5.8.2:** During the week of May 17, 2026, [iOS Client version 5.8.2](/v1/docs/summary-of-cato-ios-client-releases) will be available for download from the App Store. This version includes:
  - Stability improvements
  - Security updates
  - Bug fixes
- **Device Posture Continuous Checks Enhancements:** Device Posture checks can run [continuously](/v1/docs/client-connectivity-policy-continuous-posture-checks-check-policy) at configured intervals, even before the Client connects. We added these enhancements to align with best practices:
  - Improved the usability of the Resources > Device Posture > Settings page
    - This page is renamed **Check Policy**
  - Added checks to the Home > Posture page to help you configure continuous checks according to best practices
- **Cloud Activity Dashboard Displays SaaS Anomalies:** For increased visibility of how SaaS applications are used in your network, the [Cloud Activity Dashboard](/v1/docs/using-the-cloud-activity-dashboard) includes a widget to show SaaS anomalies. The new widget helps you identify potential risks from activities that deviate from normal behavior.
  - CASB license required
- **Always-On Bypass Code Enhancement:** Define how long a bypass code is valid for Clients with Always-On enabled.
  - Supported from Windows Client 5.18 and macOS Client 5.10.6
- **Upcoming New Platform for Knowledge Base:** To provide a more intuitive and efficient knowledge experience, the Knowledge Base will be hosted on a new platform starting in July 2026.
  - No impact on Support tickets
  - Enhanced search with filtering options to help you find relevant content more easily
  - A built-in AI assistant to help you find information faster
  - For more information, see [this article](/v1/docs/moving-to-new-knowledge-base-platform)

## PoP Announcements

- New ranges are now available for these PoP locations:
  - **Munich, DE:** 85.255.18.0/24
  - **Tokyo, JP:** 113.30.134.0/24

- **Madrid, ES:** A new range (216.252.188.0/24) will soon be available for the Madrid PoP location.
