---
title: "Product Update - Jan. 15th, 2024"
slug: "product-update-jan-15th-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-jan-15th-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Jan. 15th, 2024

## New Features & Enhancements

- **Visibility for Devices on the Network with Device Inventory**: The [new Device Inventory page](/v1/docs/using-the-device-inventory-page) shows a wealth of data about IT, IoT, and OT devices, enriched by dynamic widgets and advanced filtering options. By using advanced machine learning models, this extension to our platform detects and classifies devices into granular categories, with extremely high accuracy. This provides clear and effective monitoring and management for the devices on your network, and can help you identify potential security vulnerabilities. For example, you can see all the IP cameras on the network and check that their firmware is up to date.
  - Information reported for each device includes the device type, model and version, operating system, device user, network connection data, and more
- **Integrate Entra ID (Azure AD) Sign-in Activity:** You can comprehensively view usage in your sanctioned app ecosystem, and identify potential security concerns and trends related to sign-ins. We added a [connector to the Entra ID](/v1/docs/configuring-the-microsoft-entra-id-azure-ad-connector) API to extend visibility to all user sign-in and sign-in anomaly events on your corporate Entra ID IdP tenant. The sign-in data is shown in the new [Cloud Activity Dashboard](https://support.catonetworks.com/hc/en-us/articles/15931659820445-Using-the-Cloud-Activity-Dashboard-EA-) and in a new security event sub-types for sign-in and identity related anomalies.
  - Example insights from the Cloud Activity Dashboard:
    - Users with suspiciously high numbers of failed sign-ins
    - Breakdown of number of failed sign-ins per country
  - New Event sub-types: **Application Sign-in** and **Identity Alert** added in [Events](/v1/docs/analyzing-events-in-your-network), [eventsFeed API](https://api.catonetworks.com/documentation/#query-eventsFeed), and [Event Integration](/v1/docs/event-integration) feeds
- **OCR Scanning for DLP Content Inspection**: Cato’s DLP engine can now [scan and analyze text within image files](/v1/docs/creating-dlp-content-profiles), providing an added layer of protection for your sensitive data. For example, easily detect sensitive information in scanned documents, and ensure compliance by identifying text content in image files.

## PoP Announcements

- **Shanghai, China:** A new IP range will soon become available in the Shanghai PoP location - 140.207.250.192/26
- **Reminder for Decomissioning of IP Ranges in the China PoP Data Centers:** We’re reminding you about the following changes to the specified IP ranges in our PoP locations in Beijing, Shanghai and Shenzhen.
  - Beijing (Beijing_DC3) 123.59.229.192/26 is being decommissioned on Jan 14, 2024
  - Shenzhen (Shenzhen_DC1) 58.254.183.224/27, 59.36.210.32/27 will be decommissioned on Jan 21, 2024
    - Adding the following ranges on Jan 21, 2024: 119.147.8.0/26, 211.95.135.128/26
  - Shanghai (Shanghai_DC3) 221.228.77.128/27 will be decommissioned on Jan 31, 2024 For more information see the [Production PoP Guide](/v1/docs/production-pop-guide), and this [article](https://support.catonetworks.com/hc/en-us/articles/16030705545885).

## Knowledge Base Updates

- [Azure Conditional Access Fails to Allow Cato SSO Authentication](/v1/docs/azure-conditional-access-fails-to-allow-cato-sso-authentication)

## Video Feature Overviews

- [OCR Scanning for DLP Content Inspection](https://support.catonetworks.com/hc/en-us/articles/16083768905885)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](https://support.catonetworks.com/hc/en-us/articles/11968052021277-Understanding-Cato-s-Gradual-Rollout). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
