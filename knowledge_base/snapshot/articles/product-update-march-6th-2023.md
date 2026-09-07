---
title: "Product Update - March 6th, 2023"
slug: "product-update-march-6th-2023"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-march-6th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - March 6th, 2023

## New Features & Enhancements

- **Cato Cloud Supports High Bandwidth Cross Connect Sites:** We added a new site connectivity type that lets you [connect third-party public/private clouds to Cato](/v1/docs/cloud-interconnect-sites) over point-to-point Layer 2 circuits. With this new option we can now support use cases such as:
  - High performance connectivity with the following public cloud providers: AWS DirectConnect, Azure ExpressRoute, GCP InterConnect, Oracle FastConnect and more
- **DLP Support for Microsoft Information Protection (MIP) Labels:** You can define [DLP Data Types](/v1/docs/working-with-custom-data-types-for-dlp) as the MIP labels and easily re-use them in the Data Control policy. The labels are fully managed in your Microsoft tenant and then the DLP engine applies them to identify the sensitive content.
- **Improved Redirect Pages:** To help you implement your corporate security policy, we improved the look-and-feel and customization options for the [block and prompt Redirect Pages](/v1/docs/customizing-the-warning-block-page-branding).
  - Use a rich text editor to customize the page content and links
  - Show or hide the link for reporting the wrong category
  - Optimized for various screen resolutions, including mobile devices
  - Enhanced fields to support up to 1000 characters
- **Use New Query (Read-Only) APIs to Analyze Application Data and Events:** We are improving the [read-only API](/v1/docs/cato-read-only-api-appstats) with the following new queries to help you monitor and analyze data and metrics in the account:
  - **AppStats API** - Use the API query to analyze application traffic data in a SIEM or existing analytics solution. This query returns information and data related to the **Application Analytics** screen, for example:
    - Calculate total/average/max bandwidth for a specific site
    - Maximum number of flows generated to a specific destination
    - Top 10 applications used by a host
  - **AppStatsTimeSeries API** - Shows the analytics and data for the AppStats query according to the specified time-frame (buckets) in the query. This can include historical and near real-time statistics and metrics.
- **Configuration API Now Supports Static Range Translation for Sites:** There is a new API field that lets you define or edit the translated IP ranges for sites that use Static Range Translation.
- **Support for Site IP Overlapping:** Now you can enable IP overlapping between sites in your account. (Previously you needed to work with Support to enable IP overlapping.)
  - Important - After enabling IP overlapping between sites, you can’t disable it
  - You can only enable IP Overlapping on an account that does NOT use Static Range Translation
  - One range must be smaller and fully contained within the other range
  - Make sure that each site has a unique IP address for the Native Range
- **User Awareness Supports macOS Client v5.3 with LDAP provisioning:** Over the next few weeks, Cato’s [Identity Agent](https://support.catonetworks.com/hc/en-us/articles/7784362141085) for macOS Clients will support User Awareness for SDP users provisioned with LDAP.

## PoP Announcements

- **Salt Lake City, United States:** A new Cato PoP is now available in Salt Lake City.

## Security Updates

- **IPS Signatures:**
  - Ransomware BlackBasta 2.0 (New)
  - Ransomware Lockbit Green (New)
  - Ransomware Nevada (New)
  - Malware Laplas Clipper (New)
  - CVE-2022-46169
  - CVE-2022-44877
  - CVE-2022-0342
  - Generic protection for RDP brute force (New)
  - Generic PHP Upload (Enhancement)
- **Application Database:**
  - Added more than 200 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog))
  - Zalo (Enhancement)
  - MEGA (Enhancement)
  - Cisco Meraki Cloud (Enhancement)
  - ESPN (Enhancement)
- **Operating System Detection:**
  - iOS (Enhancement)
