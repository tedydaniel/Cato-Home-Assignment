---
title: "Product Update - March 24, 2025"
slug: "product-update-march-24-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-march-24-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - March 24, 2025

## New Features & Enhancements

- **Cato Captive Portal for your Guest Network:** For enhanced network security when granting Internet access to your guest network, users can be directed to the [Cato Captive Portal](/v1/docs/configuring-the-cato-captive-portal) to accept terms and conditions.
  - Customize the Captive Portal page to include branding, terms of service, and a user identifier such as email address
  - Track and monitor network usage to ensure compliance with organizational policies and identify potential security threats
  - Click [here](https://academy.catonetworks.com/cato-captive-portal) to watch a video recording of this feature

- **Visibility for User Directories in CMA:** For LDAP and SCIM provisioning, you can now easily filter users and user groups by the directory name.
  - Simplifies management when working with multiple directories
  - Available in the **Directory Name** column on the [Access > Users Directory](/v1/docs/working-with-users) and [Access > User Groups](/v1/docs/working-with-user-and-system-groups) pages
  - Replaces the **Add prefix to imported groups** LDAP option
  - Click [here](https://academy.catonetworks.com/managing-multiple-user-directories) to watch a video recording of this feature

- **App Activities via API for Microsoft 365 (including Copilot) and Entra ID:** Extend your CASB App Control functionality by connecting your corporate instance of Copilot, Entra ID, and other [Microsoft apps](/v1/docs/microsoft-apps-including-copilot-configuring-the-app-activities-integrations) to Cato.
  - Even when users are not connected to Cato, this lets you understand who is accessing Microsoft apps and identify suspicious activities or trends. For example, monitor Copilot chats and detect file uploads
  - The Microsoft apps are available from Resources > Integrations Catalog, under **App Activities**
  - Requires a CASB license
  - Click [here](https://academy.catonetworks.com/api-application-control-entraid-m365) to watch a video recording of this feature
- **macOS Client v5.8.5:** Starting March 24, 2025, we are rolling out macOS [Client version 5.8.5](/v1/docs/summary-of-cato-macos-client-releases). This version includes:
  - Support for the following [DEM enhancements](/v1/docs/experience-monitoring):
    - **Underlay Performance Monitoring in Socket Last Mile:** Identify and diagnose out-of-tunnel issues that could impact last-mile performance
    - **Group Multiple Devices:** DEM hardware metrics are now grouped by device name, helping you easily understand the performance of each device when there are multiple devices for the same user
    - **Support for Different LAN Gateways:** LAN gateway probes are now grouped by LAN gateway IP, letting you easily understand the performance of each LAN gateway when different gateways are present at different timeframes
  - Critical bug fixes for Device Posture to support macOS v15.2 (Sequoia)
    - Cato discovered issues when using earlier versions of the macOS Client on Sequoia while using Device Posture
      - Upgrade your macOS Client to v5.8.5 before upgrading your device to Sequoia.
      - If you have already upgraded your OS version to macOS Sequoia, contact Customer Support to get the Client v5.8.5 release

## PoP Announcements

- Added the following [IP Ranges Owned by Cato Networks](/v1/docs/production-pop-guide):
  - 113.30.128.0/20
  - 159.117.224.0/19
- **Cincinnati, US**: A new range (199.27.35.0/24) is now available for the Cincinnati PoP location.
- **Portland, US**: A new range (199.27.34.0/24) is now available for the Portland PoP location.
- **(Upcoming) Toronto, CA:** A new range (199.27.36.0/24) will soon be added to the Toronto PoP location.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
