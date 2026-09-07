---
title: "Product Update - Oct. 9th, 2023"
slug: "product-update-oct-9th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-oct-9th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Oct. 9th, 2023

## New Features & Enhancements

- **Allow List Policy for Detection & Response in the Stories Workbench:** Now you can now provide human feedback to Cato’s [Detection & Response](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) engines for more precise threat detection, and reduce alerts on known behaviors. This feature is available for XDR Core, XDR Pro, and MDR customers.
  - Define parameters for an [Allow List](/v1/docs/muting-xops-stories) rule based on an XDR story, such as IP, URL, Site and more. When suspicious traffic matches an Allow List rule, the Detection & Response engine does not create a story. This helps avoid new Detection & Response stories for traffic that is expected and known as benign.
- **Expanded Information for Similar Stories in the Stories Workbench:** To help investigate Detection & Response stories, the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) uses machine learning models to show **Similar Stories** that share some common parameters, such as the **Target** or **Indication**. We enhanced the **Similar Stories** field to show more information, including:
  - More related stories
  - Important details about each story, such as:
    - Story indication and verdict
    - A new metric that evaluates the level of similarity

## Cato SDP Client Releases

- **macOS Client version 5.4.3**: The gradual rollout of macOS Client [version 5.4.3](/v1/docs/summary-of-cato-macos-client-releases) started on the week of Oct. 8th, 2023. This version contains stability fixes and security enhancements including:
  - Resolved issue that caused the device certificate check to fail after upgrading from version 5.3 to 5.4
  - Resolved issue that caused the Client to be unresponsive after collecting logs if the device clock was not configured to 24 hour format
  - Hardened the Client upgrade mechanism to protect upgrade components

## PoP Announcements

- **Dublin, Ireland**: A new range (85.255.23.0/24) is now available in the Dublin, Ireland PoP location
- **Los Angeles, United States**: A new range (216.205.115.0/24) will be added to the Los Angeles PoP location
- **Miami, United States**: A new range (150.195.202.0/24) will be added to the Miami PoP location

## Knowledge Base Updates

[Socket High Availability Failover Fails Due To Meraki Switch GARP Limitation](/v1/docs/socket-high-availability-failover-fails-due-to-meraki-switch-garp-limitation)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
