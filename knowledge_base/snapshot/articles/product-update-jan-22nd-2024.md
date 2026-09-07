---
title: "Product Update - Jan. 22nd, 2024"
slug: "product-update-jan-22nd-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-jan-22nd-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Jan. 22nd, 2024

## New Features & Enhancements

- **XDR for Network Connectivity and Performance Incidents:** The Cato XDR platform now includes [network monitoring stories](/v1/docs/reviewing-site-operations-stories) in addition to Security to provide:
  - **Comprehensive Visibility of Network Incidents:** Admins can gain insight into their network connectivity and performance issues
  - **Unified Incident Investigation:** Correlates data from various sources, translating it into a single story with all the relevant information and links to a suggested playbook to resolve the problem
  - **Automated Response:** Manage automated notifications with the XDR Response Policy
  - **Enhanced Reporting and Analytics:** Provides detailed reports and analytics for Network Incidents
- **DLP Protection for ChatGPT:** Our [DLP service](/v1/docs/what-is-the-cato-dlp-service) can now scan content and enforce policies on ChatGPT traffic to help you prevent users from compromising sensitive data when using Generative AI.
  - [Data Control](/v1/docs/creating-the-data-control-policy) rules for the ChatGPT application support the Upload action
- **Policy to Manage Proxy Configuration File:** The [Proxy Configuration Policy](/v1/docs/centralized-management-of-proxy-configuration-proxy-configuration-policy) provides a granular method to easily manage PAC files, used by the Client for proxy configuration, for remote users and user groups accessing your network.
  - There is no impact for accounts that use the existing Proxy Configuration File, which Cato will automatically migrate
- **Single Filter for All User Events Regardless of User Location:** With the new **User Email** and **User Display Name** fields you can view all [User Events](/v1/docs/working-with-users) with a single filter.
  - Previously, events from users connecting behind a site could not be viewed together with users connecting remotely, two separate filters were required
- **Easily Identify and Enforce Policies for Private Applications:** When deploying ZTNA solutions, admins often aren’t aware of all the applications and destinations their users require. We enhanced the process for [identifying private applications](/v1/docs/working-with-private-applications-on-the-app-analytics-page) and configuring them as [Custom Applications](/v1/docs/working-with-custom-apps) that let you enforce policies for them. On the [Application Analytics](/v1/docs/understanding-app-analytics) page, you can now filter for unidentified private applications, and convert them into Custom Applications directly on the page.
- **XDR Response Policy Enhancement - Generate and Export Story Events:** You can now generate and export events for XDR stories as part of the [XDR Response policy](/v1/docs/creating-the-response-policy-for-xops-stories). The policy lets you configure rules that define the story criteria for generating events. For example, generate an event when a high risk story is created. The events appear in the Events page, and can be exported to third-party systems such as SIEMs using [eventsFeed API](https://api.catonetworks.com/documentation/#query-eventsFeed).
  - Story events are optional and only generated according to user configuration
  - Story events are categorized as a **Detection & Response** Event Type
  - Available for XDR Core and XDR Pro licenses
- **Faster BGP Convergence with BFD:** Over the next 3-4 weeks we are gradually enabling [Bi-Directional Forwarding Detection (BFD)](/v1/docs/configuring-bfd-for-bgp-neighbors) for BGP. This ensures swift convergence over IPSec and Cross Connect sites for enhanced network reliability.
  - BFD can reduce the detection time to 1 second, while typical BGP hold time is 60 seconds
  - The BFD status can be seen in the Events page under the Event Type **Routing** and the Sub-Type **BFD session**
  - Cato follows RFCs 5880, 5881, and 5882
- **New Degraded Status for Sites Shows Connectivity Issues at a Glance:** Over the next few weeks we are gradually enabling the [**Degraded**](/v1/docs/connectivity-statuses-for-cato-sites) status, which lets you quickly identify sites with connectivity issues. In addition, you can hover over the status to show the root cause. For example, from the Topology page you can see that a passive port or tunnel is down, or the site HA status is **Not Ready**. Previously you needed to drill-down and detect where the issue was.
  - The **Degraded** status is applied to all active and passive links
- **View Information for Your Cato Management Application Account:** The new [Account Info](/v1/docs/viewing-the-account-info) page (Administration > Account Info) shows information for your account in the Cato Management Application, including:
  - Account Name
  - Account ID
  - Description (user defined)
  - Creation Date

## Cato SDP Client Releases

- **Linux Client v5.2:** From Jan 22nd, 2024, we are starting the rollout of Linux Client v5.2. This version contains:
  - **Connect on Boot:** The Client connects to the Cato Cloud [automatically](/v1/docs/protecting-users-with-always-on-security), without any user interaction, after the device boots
  - **User Authentication is No Longer Required Behind a Site:** To simplify the user experience for users behind a site, the Client can connect automatically in [Office Mode](/v1/docs/configuring-office-mode) without users manually authenticating. There is no impact on Security and User Awareness policies
  - Bug fixes and enhancements, including:
    - Improved process for prioritizing which PoP the Client connects to
    - Faster time to reconnect when the Client changes from an out of office network to an office network

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
    - Ransomware 3000USDAA (New)
    - Ransomware Jopanaxye (New)
    - Ransomware Albabat (Enhancement)
    - Ransomware CookiesHelper (Enhancement)
    - Ransomware Karsovrop (Enhancement)
    - Ransomware Ncov (Enhancement)
    - Ransomware Shuriken (Enhancement)
    - Ransomware Stop/Djvu (Enhancement)
    - CVE-2023-5360 (New)
    - CVE-2023-48365 (New)
    - CVE-2023-41266 (New)
    - CVE-2023-41265 (New)
    - CVE-2023-20889 (New)
    - CVE-2022-30808 (New)
    - CVE-2022-27498 (New)
    - CVE-2022-20705 (New)
    - CVE-2016-10372 (Enhancement)
- **Detection & Response**
  - These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
    - Threat Hunting Indications:
      - Downloading a Suspicious Script (Enhancement)
      - Hta File Found in MS Office (Enhancement)
      - Netscan Write Access Check Attempts (Enhancement)
      - PSTools Download Detection (Enhancement)
      - Suspicious Network Activity (Geo-Restriction) (Enhancement)
      - Suspicious File Downloaded From OneDrive (Enhancement)
    - Threat Prevention Indications:
      - Anti-Malware Detection (Enhancement)
      - Rclone Client Uploads Files to the Mega Share Service (Enhancement)
      - Suspicious Cryptomining Activity (JSON-RPC) (Enhancement)
      - Torrent Outbound Communication (Enhancement)
      - Transferring a Suspicious Script ((Enhancement)
      - WordPress Exploitation Attempt (Enhancement)
- **Suspicious Activity Monitoring:**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - Enumerating All Users on the Domain Controler - Using SAMR RPC (New)
    - Netsupport Download (New)
- **TLS Inspection**
  - Added global bypass for these applications and FQDNs, preventing possible [TLS inspection](/v1/docs/configuring-tls-inspection-policy-for-the-account) errors:
    - Applications:
      - Cisco Intersight
      - Cisco
    - FQDNs:
      - dealer.spotify.com
  - The following applications are now inspected and the global bypass for them was removed:
    - ChatGPT
    - OpenAI
- **Apps Catalog:**
  - Added over 200 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), and enhanced these applications:
    - ChatGPT
    - Cisco
    - Cisco Intersight
    - GitHub
    - Google Photos
    - GoTo (Formerly LogMeIn)
    - GoTo Meeting
    - GoToAssist
    - GoToMyPC
    - Huawei
    - OpenAI
    - Tor
- **Application Control (CASB and DLP):**
  - New granular actions for the following apps:
    - Google Photos - Download (New)
    - Gmail - Download Attachment (Enhancement)
    - Outlook - Send Mail (Enhancement)
  - These apps are included in DLP scans:
    - ChatGPT Upload (New: including conversations and attachments)
    - Google Photos - Download (New)
- **Client Classification:**
  - HTTP detection enhancements
  - SNI based enhancements

## Video Feature Overviews

- [XDR Stories Events](https://support.catonetworks.com/hc/en-us/articles/16231544069789)
- [Bi-Directional Forwarding Detection (BFD)](https://support.catonetworks.com/hc/en-us/articles/16231508979229-BFD-for-IPsec-and-Cross-Connect-Video)
- [New Linux Client v5.2](https://support.catonetworks.com/hc/en-us/articles/16231613031837)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
