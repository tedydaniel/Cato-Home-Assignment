---
title: "Product Update - April 24th, 2023"
slug: "product-update-april-24th-2023"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-april-24th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - April 24th, 2023

## New Features & Enhancements

- **Detection and Response View in Cato Management Application:** Cato is introducing new [Detection & Response](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) screens with enhanced investigation capabilities. You can now see highlighted security stories identified for your account, and analyze them with a range of widgets and research sources. Regularly review these stories to significantly improve your security posture and help stay ahead of emerging security threats. Threat stories contain a broad range of information that let the user:
  - Display live data about compromised sources and destinations
  - Track the progress of investigations
  - Analyze details of relevant traffic
  - Learn more about threats with third-party utilities
- **PDF Reports Highlight Security Events:** Now you can generate [Security Reports](/v1/docs/cato-reports) that shows an overview of events for different Cato Security services.
  - Including these services:
    - Internet and WAN firewall
    - IPS
    - Anti-Malware and Next Gen Anti-Malware
    - IPS Suspicious activity (SAM)
    - IPS DNS protections
  - Generate reports for different time ranges and for specific sites and SDP users
- **Use Custom CA Certificates with TLS Inspection:** Cato’s TLS Inspection now supports [custom intermediate Certificate Authority (CA) certificates](/v1/docs/securing-traffic-with-tls-inspection-using-private-certificates). This lets you use your own CA, and work with the certificates already installed on devices in your organization.
- **Improved Granularity for RBAC with Resellers:** Role Based Access Control (RBAC) for the Cato Management Application now lets resellers [assign roles to admins](https://support.catonetworks.com/hc/en-us/articles/9087001774365) for specific customer accounts.

## Cato SDP Client Releases

- **Windows Client v5.7:** We are planning to start the rollout for Windows Client v5.7 during the week of May 1st. Here’s a preview of new features included in this version:
  - **Device Posture for SDP Users in the Office:** The Device Posture Profiles and Device Checks are now also applied for SDP users in the office behind a site (connected to the network). This lets you apply the same security level by enforcing the same device requirements whether SDP users are working from home, or in the office.
  - **SDP User Feedback:** To help us continually improve our remote access, SDP users can now provide feedback to Cato from within the Client.
    - Every few months, users are prompted to give a rating and comments
    - SDP users can also manually provide feedback at any time
  - **Improved Client Resiliency with Rapid Reconnect:** The Client infrastructure now includes multiple tunnels to provide redundancy. So, if there’s an issue, there is minimal packet loss and negligible impact to the SDP user experience.
  - **Enhanced Client PoP Selection**: We improved the PoP selection process to better consider multiple factors including geography and availability. The Client now more accurately selects the best PoP to connect to.
    - Ensure the following URLs can be accessed to use this feature:
      - [https://network-segmentation.catonetworks.com](https://network-segmentation.catonetworks.com/)
      - [https://ip2location.catonetworks.com/pub/getMyLocation](https://ip2location.catonetworks.com/pub/getMyLocation)
  - For more information about the Client rollout process, see the following articles:
    - [Best Practices for Cato Windows and macOS Upgrades](/v1/docs/recommendations-for-cato-client-upgrades)
    - [Client Lifecycle Management](/v1/docs/client-lifecycle-management)

## Knowledge Base Updates

- [Internet and WAN Firewall Policies - Best Practices](/v1/docs/recommendations-for-internet-and-wan-firewall-policies)
