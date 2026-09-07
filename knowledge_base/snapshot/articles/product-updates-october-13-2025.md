---
title: "Product Updates - October 13, 2025"
slug: "product-updates-october-13-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-october-13-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - October 13, 2025

## New Features & Enhancements

- **Update Flow Enhancements for Webhook Integrations:** CMA notifications sent via [webhook integrations](/v1/docs/sending-cma-notifications-via-webhooks) now support updating existing objects in third-party platforms, such as a ticket or message thread. These enhancements simplify lifecycle management across a range of external systems.
  - Support for PUT requests in addition to POST
  - Added the ability to use variables in the target URL and custom header definitions
  - Templates now cover all fields
  - New reference templates for creation and update flows, including examples for Jira, ServiceNow, and Zendesk
  - Automate ticket creation and updates for correlated (XOps) notifications. This correlation requires an XOps license.
- **Create Access Policy Rules Based on the Public Source IP Address:** Now you can define rules in access policies using the Source IP address as the condition for the rule.
  - In the [IP Allocation policy](/v1/docs/ip-allocation-policy-for-remote-users), you can assign IP addresses for remote users based on where they connect from. Use the IP Allocation Policy to define the **Public ISP IP Range** as a policy condition, enabling location-aware dynamic IP assignment for remote users. This can be helpful for WAN applications that enforce access control lists (ACLs) based on specific IP ranges.
    - Configure in the Access > IP Allocation Policy page, or with the <kbd>dynamicIpAllocationPolicy</kbd>[mutation API](https://api.catonetworks.com/documentation/#mutation-policy.dynamicIpAllocation.addRule)
  - In the [Client Connectivity policy](/v1/docs/what-is-the-client-connectivity-policy), you can define access control rules based on different criteria. Use the Client Connectivity policy to define the **Public ISP IP Range** as a policy condition to determine access to resources.
    - Configure in the Access > Client Connectivity Policy page

## PoP Announcements

- **Paris, France:** A new range (159.117.234.0/24) will soon be added to the Paris PoP location.
- **Resizing Localized Range for Slovakia to 209.206.22.0/25:** We are changing the geo-localized range for Slovakia serviced through Prague, to 209.206.22.0/25
- **Upcoming Localized Range for Bosnia and Herzegovina:** A new geo-localized range (209.206.22.128/27) for Bosnia and Herzegovina (BA), serviced through Prague, will be available soon.

## Security Updates

- **App Catalog**
  - **New Apps**
    - Turbo VPN
  - **Removed Apps**
    - Wixsite deprecated - now under Wix
  - **Enhanced Apps**
    - Akamai - modify name from "akamai" to "Akamai"
    - Augment Code - Modify name from "Augment Computing" to "Augment Code"
    - California High-Speed Rail - Modify name from "Ca" to "California High-Speed Rail"
    - Cato Endpoint Protection - Modify app domains
    - Cato Management Application - Modify app domains
    - Fc2 Portal - Modify name from "Fc2" to "Fc2 Portal"
    - Netlify - Modify app domains
    - Skype and MS Teams - Modify app IPs
    - Wix.com Limited - Modify app domains
    - 8x8 - Added domain "8x8.vc"
    - Bahn - Added domains "db.de", "deutschebahn.com"
    - Egym Gmbh - Added domain "egym.de"
    - Google AdWords - Modify app domains
    - jitsi - Signature Updated
    - Microsoft Office365 - Modify app domains
    - sgx - Added domain "bidfx.com"
    - Talk2M By Ewon - Modify app IPs
    - WebEx - Added domains "broadcloud.com.au", "broadcloud.eu", "broadcloudpbx.com", "broadcloudpbx.net"
    - Zscaler - Modify app IPs
- **IPS Signatures**
  - IPS Signatures: View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2020-11546 (New)
    - CVE-2020-11798 (New)
    - CVE-2020-11991 (New)
    - CVE-2020-13851 (New)
    - CVE-2020-23575 (New)
    - CVE-2020-24949 (New)
    - CVE-2020-25079 (New)
    - CVE-2020-35598 (New)
    - CVE-2020-8813 (New)
    - CVE-2021-21479 (New)
    - CVE-2021-21881 (New)
    - CVE-2021-25864 (New)
    - CVE-2021-27931 (New)
    - CVE-2021-32305 (New)
    - CVE-2021-34805 (New)
    - CVE-2021-36356 (New)
    - CVE-2021-40978 (New)
    - CVE-2021-41291 (New)
    - CVE-2021-43734 (New)
    - CVE-2021-46417 (New)
    - CVE-2022-24288 (Enhancement)
    - CVE-2022-40799 (New)
    - CVE-2023-0261 (Enhancement)
    - CVE-2023-3710 (New)
    - CVE-2024-0939 (New)
    - CVE-2024-22319 (New)
    - CVE-2024-22942 (New)
    - CVE-2024-23057 (New)
    - CVE-2024-23058 (New)
    - CVE-2024-23059 (New)
    - CVE-2024-23060 (New)
    - CVE-2024-23061 (New)
    - CVE-2024-24325 (New)
    - CVE-2024-24326 (New)
    - CVE-2024-24327 (New)
    - CVE-2024-24328 (New)
    - CVE-2024-24329 (New)
    - CVE-2024-24330 (New)
    - CVE-2024-24331 (New)
    - CVE-2024-24332 (New)
    - CVE-2024-24333 (New)
    - CVE-2024-36857 (New)
    - CVE-2024-36858 (New)
    - CVE-2024-46938 (New)
    - CVE-2024-6587 (New)
    - CVE-2024-7332 (New)
    - CVE-2025-47916 (New)
    - CVE-2025-48828 (New)
    - CVE-2025-54309 (Enhancement)
    - CVE-2025-54918 (New)
    - CVE-2025-57790 (New)
    - CVE-2025-61882 (New)
    - Malware - Lumma Stealer (New)
    - Malware - Vidar Stealer (Enhancement)
    - Mythic C2 Apfell Agent - Download and Upload via FTP (New)
    - Python Reverse Shell Download over HTTP (New)
- **SAM Signatures**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - PowerShell over HTTP to low popularity target (Enhancement)
- **OS Detection**
  - OS embedded signature for Cisco Meraki devices (New)
  - OS Linux signature for IO DATA devices (New)
- **Application Control Policy**
  - **CASB**
    - Amazon AWS - Inline tenant control (New)
    - Atlassian - AI Chat Bot (New)
    - Bitbucket Pull (Enhancement)
    - ChatGPT - extract model (New)
    - Github pull (Enhancement)
    - Gmail - Inline tenant control (New)
    - Google Search - AI Search (New)
    - Google Drive - Upload (Enhancement)
    - Google Translate - Search (New)
    - ChatGPT - Share Conversation (New)
    - Jetbrains - Install Plugin (New)
    - Exchange - Download Attachment (New)
    - Slack - Summarize Thread (New)
    - Visual Studio - Install Extension (New)
    - Webex - Inline tenant control (New)
    - X Ai - Upload (New)
    - Zendesk - Inline tenant control (New)
    - Deepl - Inline tenant control (New)
  - **DLP**
    - Deepl - Start Conversation (New)
    - Deepl - Upload File (New)
    - Deepl - Download File (New)
- **XOps Indications of Attack**
  - **Anomaly Detection**
    - First Occurrence of a New Tenant for Known Application (New)
    - Abnormal DNS Activity (Enhancement)
    - Deprecated or Unauthorized Protocols First Occurrence Anomaly (Enhancement)
    - Abnormal Outbound SSH/Telnet over Non-Standard Ports Activity (Enhancement)
    - Abnormal SMB Traffic from a User Over the WAN (New)
    - First Occurrence of Wanbound Scanning Activity by a User (New)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
