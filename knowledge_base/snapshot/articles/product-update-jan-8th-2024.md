---
title: "Product Update - Jan. 8th, 2024"
slug: "product-update-jan-8th-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-jan-8th-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Jan. 8th, 2024

## New Features & Enhancements

- **Internet Security for Remote Users with One Time Authentication:** Over the next few weeks, for secured Internet access, remote users will only need to [authenticate once](/v1/docs/remote-internet-security-with-one-time-authentication) in the Client.
  - Cato Security policies are always enforced for Internet traffic. With this mode, users have continuous secured Internet access without needing to re-authenticate
  - Supported from Windows Client version 5.9
- **SaaS Security API - Sharepoint Events Now Include the Site Owner Email:** The [SaaS Security API](/v1/docs/what-is-the-data-protection-api) service generates events for violations of the Threat Protection and Data Protection policies for an app. We enhanced these events for [Microsoft Sharepoint](/v1/docs/microsoft-sharepoint-configuring-the-data-protection-api-connector) to provide the email address of the site owner to make it easier for admins to identify and contact owners associated with policy violations.
  - These are the [Sharepoint event fields](/v1/docs/microsoft-sharepoint-configuring-the-data-protection-api-connector) relevant to this change:
    - The site owner email address appears in the **Owner** field
    - Details for the owner site appear in the new **Object Name** field
- **New Integrations Catalog:** We added the [Integrations page](/v1/docs/using-the-integrations-page) in the Assets tab to show all the supported third-party integrations for various use cases, such as IdP integrations for SSO, cloud storage services for logs, SaaS Security integrations, and more.
- **Ability to Delete Generated Reports:** Now you can delete [Generated Reports](/v1/docs/cato-reports) when you no longer need them.

## Cato SDP Client Releases

- **macOS Client v5.5:** From Jan 8th, 2024, we are starting the roll out of macOS Client version 5.5. This version contains:
  - **Always-On Enhancements:** We are introducing new features that ensure Always-On can be used while maintaining business continuity:
    - **New Bypass Mode for Always-On:** Users can [temporarily access the Internet](/v1/docs/protecting-users-with-always-on-security) without waiting for admin approval. Users provide a reason in the Client and Always-On can be temporarily bypassed and the Client can disconnect
    - **Always-On Recovery Mode:** Users can access the Internet if a connection to the [Cato Cloud is unavailable](/v1/docs/protecting-users-with-always-on-security). For example, if a Captive Portal prevents the Client from connecting to Cato Cloud, users can still access the Internet, bypassing Cato security
  - **Improvements to Device Posture Checks:** The new version supports a new device posture check and enhances the Anti-Malware check:
    - **New DLP Device Posture Check:** You can now include a check for DLP within your [Device Posture Profiles](/v1/docs/creating-device-posture-profiles-and-device-checks). The Device Posture Profile can be included in your Client Connectivity and security policies
    - **Real Time Protection for Anti-Malware Device Check:** Connected devices are [continuously verified](/v1/docs/creating-device-posture-profiles-and-device-checks) to ensure they meet the requirements of the Anti-Malware Device Check
  - **Support for macOS Sonoma:** The Client now supports macOS Sonoma (macOS 14)
  - **Stability Improvements:** The new Client version provides users with increased network stability. Key improvements include:
    - Resiliency during network changes
    - Authentication after device wakes up
    - Optimizing time-to-connect

## PoP Announcements

- **Tokyo, JP:** A new IP range will soon become available in the Tokyo PoP location:
  - 150.195.218.0/24
    - This range is instead of the 150.195.217.0/24 range that was previously announced
- **Osaka, JP:** The following IP range is now available in the Osaka PoP location:
  - 150.195.212.0/24
- **Upcoming Decommissioning for China PoP Data Centers:** In line with the continuous infrastructure improvement efforts at Cato Networks, we're announcing changes in our PoP data centers in Beijing, Shanghai and Shenzhen. If these changes impact you, your administrators already have been notified by our Support team with specific instructions - where applicable.
  - Beijing_DC3 is scheduled for decommissioning by Jan 12th, 2024
  - Shanghai_DC3 scheduled for decommissioning by the end of January 2024
  - The following IP addresses in our Shenzhen_DC1 IPs are going to change on Jan 21st, 2024
    - 119.147.8.0/26 and 211.95.135.128/26
  - Cato Networks always recommends following egress and route-via best practices as described [here](https://support.catonetworks.com/hc/en-us/articles/360003919457) to minimize or avoid impact of network changes.

## Security Updates

- **IPS Signatures:** View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - Ransomware GhostLocker (New)
  - Ransomware GrafGrafel (New)
  - Ransomware Eking (Enhancement)
  - Ransomware Elpy (Enhancement)
  - Ransomware HuiVJope (Enhancement)
  - Ransomware Tisak (Enhancement)
  - Malware Formbook (New)
  - Malware NetSupport Manager RAT (New)
  - Cross Site Scripting attempt in query string (New)
  - Remote Code Execution over HTTP (New)
  - CVE-2022-37149 (New)
  - CVE-2020-2551 (New)
- **Detection & Response** These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
  - Threat Hunting Indications:
    - Abnormal Network Activity (New)
    - HTA File Found in MS Office (New)
    - PSTools Download Detection (New)
    - Remote Psexec Service Execution (New)
    - Suspicious Bot Activity (New)
    - chaser_cid_cve_outbound (Enhancement)
    - Suspicious lnk File Download (Enhancement)
    - Suspicious Network Activity (JA3) (Enhancement)
    - Suspicious POST Request (Enhancement)
  - Threat Prevention Indications:
    - Suspicious Network Activity (Enhancement)
    - Suspicious Trello API usage (Enhancement)
- **Suspicious Activity Monitoring:** These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
  - AnyDesk - Download (New)
  - Downloading TightVNC (New)
  - Malware DNS Activity (Emotet) (New)
  - Rclone - Download (New)
  - Phishing heuristic (Enhancement)
- **Apps Catalog:** Added over 300 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), and enhanced these applications:
  - ExpressVPN
  - GitHub
  - Google Photos
  - OneDrive Personal
  - Sharepoint and OneDrive Business
  - Veeam Backup
- **Application Control (CASB):** New granular actions for the following apps:
  - Box – Login
  - Google Docs – Download
  - SharePoint – Download
  - OneDrive – Download
- **File Identification:** Enhanced file identification in Cato Cloud services for the following file types:
  - Java
  - Python
- **Client Classification:**
  - Tor client detection improvement

## Knowledge Base Updates

- [Routing Options in The Cato Cloud (Video)](https://support.catonetworks.com/hc/en-us/articles/15830393436573)
- In the [Production PoP Guide](/v1/docs/production-pop-guide), we added a static URL for the CSV file that contains the PoP IP range data. You can now use this file in automation and scripts.

## Video Feature Overviews

- **New Video Overviews from the Cato Product Team:** We are introducing a new series of videos of technical sessions delivered by Cato Product Managers, which include:
  - Updates and overviews about new and existing features
  - Guest sessions by Cato SMEs providing detailed explanations of a variety of technical topics
  - New video content will be regularly uploaded to the [Feature Overview Video Library](https://support.catonetworks.com/hc/en-us/articles/15820894044061-Feature-Overview-Video-Library-)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
