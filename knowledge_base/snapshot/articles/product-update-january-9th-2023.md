---
title: "Product Update - January 9th, 2023"
slug: "product-update-january-9th-2023"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-january-9th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - January 9th, 2023

## New Features & Enhancements

- **MDR Stories View in Cato Management Application:** Customers of Cato’s MDR service now have full visibility for investigations into threats in the new [Detection & Response](/v1/docs/reviewing-detection-response-stories-for-mdr-customers) screen. Threat stories contain a broad range of information that lets the customer:
  - Show live data about compromised sources and destinations
  - Track the progress of investigations
  - Analyze details of relevant traffic
  - Learn more about threats with third-party utilities
  - Coordinate better with the MDR team for effective remediation
- **Improved Visibility for Domain Categorization:** The [Domain Lookup](/v1/docs/identifying-the-category-for-a-domain) tab is a new feature for the [Apps Catalog](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcatonetworks.us16.list-manage.com%2Ftrack%2Fclick%3Fu%3D75bb2b7bafe7526c787475fd2%26id%3D6106fb226e%26e%3D2b9a2985a2&amp;data=05%7C01%7Cjonathan.rabinowitz%40catonetworks.com%7C7085e924b4e94783d28c08daf18dec0e%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638087889101335549%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&amp;sdata=eIffNt9iJezCQT%2BEC5Et1s3rtsCj%2BdoNj6D8htJnxyI%3D&amp;reserved=0) that lets you identify how a specific domain is categorized in Cato Cloud. For example, you can look up a website and see if it is included in the **Gambling** category that is blocked by the Internet Firewall.
- **New Supported File Type for Anti-Malware:** SVG files are included in [Anti-Malware](/v1/docs/what-is-the-cato-anti-malware-policy) scans. The Anti-Malware service can now inspect SVG files for malicious and suspicious content.
- **Cato Management Application Enhancements**:
  - **Get the Latest Events with a New Refresh Button**: Starting on January 16, there will be a new **Refresh** button in the [Events](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcatonetworks.us16.list-manage.com%2Ftrack%2Fclick%3Fu%3D75bb2b7bafe7526c787475fd2%26id%3D391f4eb65d%26e%3D2b9a2985a2&amp;data=05%7C01%7Cjonathan.rabinowitz%40catonetworks.com%7C7085e924b4e94783d28c08daf18dec0e%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638087889101335549%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&amp;sdata=nVFBcVDsZExXGvtm7KTzYAgy15Sibk9YHWpyZMMvD2E%3D&amp;reserved=0) screen to quickly and easily refresh it. The events list and any new or changed events are updated.

## Cato SDP Client Releases

- **Windows Client v5.6:** Soon we will start the gradual roll-out for the Windows Client version 5.6. Below is a preview of planned features and enhancements for this version. Read more about [best practices for upgrading Clients](/v1/docs/recommendations-for-cato-client-upgrades).
  - **Improved Out-of-the-Box Security:**
    - **Deploying Clients with Always-On Enabled:** You can automatically enable [Always-On](/v1/docs/protecting-users-with-always-on-security) for new Client installations, so that users will not have Internet access until after they are authenticated.
    - **Automatically Show Client when the Device Starts:** To let an SDP user set up a new device and easily find the Client and then Connect to the network, you can now use a registry flag to define if the Client app automatically opens or not.
  - **Exclude Network Ranges from LAN Blocking:** Use the [Split Tunnel feature with LAN Blocking](https://support.catonetworks.com/hc/en-us/articles/7537633519773) to define subnets that are excluded from the tunnel. For example, this lets a device connect to a LAN printer even though LAN Blocking is enabled.
  - **Enhanced Windows Client Upgrade Process:** We added roll-back functionality to the Client, and if there’s an issue during the upgrade, the Client automatically rolls back to the previous version.
    - The Client automatically upgrades to the next minor Client version when it is available
  - **Improvements to Client Self Service:** When using Self Service to troubleshoot the Client, now includes data from the Cato Cloud in addition to the local device.
- **macOS Client v5.3:** Soon we will start the gradual roll-out for the macOS Client version 5.3. Below is a preview of planned features and enhancements for this version. Read more about [best practices for upgrading Clients](/v1/docs/recommendations-for-cato-client-upgrades).
  - Improved upgrade experience for SDP users, and they are no longer required authenticate to the macOS during the upgrade
  - Admins no longer need to manually distribute the Cato certificate for TLS Inspection, the Client automatically installs it on the macOS device (similar to the Windows Client)
  - Performance improvements for macOS devices with the native Apple CPU chips

## Security Updates

- **IPS Signatures:**
  - Malware - Brute Ratel (New)
  - Malware - Qakbot (Enhancement)
  - CVE-2022-37149
  - CVE-2022-2564
- **Application Database:**
  - Added more than 200 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - Active Directory Global Catalog over LDAP
  - Enhanced the following SaaS application:
    - WeTransfer
- **Updates to Application Control Policy:**
  - New granular actions for this app:
    - Pastebin: Download
  - Enhanced actions for these apps:
    - WeTransfer: Upload
    - GigaFile: Upload
    - Yahoo Mail: Upload
    - LinkedIn: Add Attachment
