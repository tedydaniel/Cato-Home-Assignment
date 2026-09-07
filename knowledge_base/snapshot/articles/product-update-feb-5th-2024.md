---
title: "Product Update - Feb. 5th, 2024"
slug: "product-update-feb-5th-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-feb-5th-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Feb. 5th, 2024

## New Features & Enhancements

- **Introducing Cato’s Endpoint Protection:** Cato Endpoint Protection (EPP) is the industry’s first SASE-managed [EPP solution](/v1/docs/getting-started-with-cato-s-endpoint-protection-epp) protecting endpoints against advanced malware, evasive attacks, and zero-day threats. This adds endpoint protection and detection to Cato’s multi-layer SASE architecture while reducing management overhead, increasing security team efficiency, and improving the enterprise security posture.
- **Experience Monitoring for App Performance and User Experience:** [Experience Monitoring](/v1/docs/using-the-experience-monitoring-page) provides insight into user experience, proactively monitors app performance, and pinpoints issues. You can seamlessly start using Experience Monitoring without deploying any agents and no configuration is required. For example, you can:
  - Quickly identify and troubleshoot issues impacting application performance
  - Gain immediate insights into your application metrics with a user-centric focus
  - Proactively identify bottlenecks and latency issues that could impact user experience
  - A free trial of Experience Monitoring is available
- **Configure SA Lifetime for IPsec Sites:** You can configure the IPsec P1 and P2 Security Associations (SA) lifetime for the tunnels between the site and the PoP by using the [site-level Advanced Configuration](/v1/docs/advanced-configurations-for-a-site).
  - Supported for IKEv1 and IKEv2 sites

## Cato SDP Client Releases

- **iOS Client v5.2.1:** In the next few weeks, iOS Client v5.2.1 will be available to download from the App Store. This version contains bug fixes and enhancements including:
  - Reduced the time it takes for the Client to connect
  - Resolved an issue where the connection time stopped even if the Client was connected to the Cato Cloud

## PoP Announcements

- **Kansas City, US:** A new Cato PoP is now available in Kansas City with the range - 216.205.112.0/24
- **Tokyo, JP:** A new IP range is now available in the Tokyo PoP location - 150.195.218.0/24
- For the following PoP locations, a new IP range will soon become available:
  - **Atlanta, US:** 216.205.113.0/24
  - **London, UK:** 85.255.27.0/24
  - **Mumbai, IN:** 123.253.153.0/24
  - **Shanghai, CN:** 114.94.55.192/26

## Video Feature Overviews

- [Configure SA Lifetime for IPsec Sites](https://support.catonetworks.com/hc/en-us/articles/16529562475421-Configure-SA-Lifetime-for-IPsec-Sites-Video)
- [Monitoring for App Performance and User Experience](https://support.catonetworks.com/hc/en-us/articles/16529593582749-Monitoring-for-App-Performance-and-User-Experience-Video)
- [DLP ML Classifiers - Content Detection with Pre-Trained Models](https://support.catonetworks.com/hc/en-us/articles/16529597998621-DLP-ML-Classifiers-Content-Detection-with-Pre-Trained-Models-Video)
- [DLP Engine Scans ChatGPT Traffic](https://support.catonetworks.com/hc/en-us/articles/16529643536541-DLP-Engine-Scans-ChatGPT-traffic-Video)
- [Custom App Detection and Configuration from within App Analytics](https://support.catonetworks.com/hc/en-us/articles/16529647126941-Custom-App-Detection-and-Configuration-from-within-App-Analytics-Video)
- [New iOS Client v5.2](https://support.catonetworks.com/hc/en-us/articles/16529624104861-New-Client-for-iOS-v5-2-Video)
- [Filter Unified Events for All Users](https://support.catonetworks.com/hc/en-us/articles/16529695158813-Filter-Unified-Events-for-All-Users-Video)
- [Proxy Configuration Policy](https://support.catonetworks.com/hc/en-us/articles/16529697553053-Proxy-Configuration-Policy-Video)

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog)
    - Ransomware Empire (New)
    - Ransomware SilentAnonymous (New)
    - Ransomware Slime (New)
    - Ransomware Avanzi (Enhancement)
    - Ransomware Backoff (Enhancement)
    - Ransomware CookiesHelper (Enhancement)
    - Ransomware Frivinho (Enhancement)
    - Ransomware Gotmydatafast (Enhancement)
    - Ransomware Karsovrop (Enhancement)
    - Ransomware LEAKDB (Enhancement)
    - Ransomware Messec (Enhancement)
    - Ransomware Wessy (Enhancement)
    - CVE-2024-0204 (New)
    - CVE-2023-43261 (New)
    - CVE-2023-30258 (New)
    - CVE-2023-24734 (New)
    - CVE-2022-28915 (New)
    - CVE-2022-20707 (New)
    - CVE-2024-23897 (New)
    - CVE-2023-22527 (New)
- **Detection & Response**
  - These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
    - Threat Hunting Indications:
      - Device Attributes Exfiltration (New)
      - Suspicious Network Activity - MS-PowerShell (New)
      - Suspicious Bot Activity (New)
      - AdFind Download Attempt (Enhancement)
      - Autoit downloads a binary (Enhancement)
      - BITS abnormal activity (Enhancement)
      - Downloading From Exploit-DB (Enhancement)
      - Device Attributes Exfiltration (Enhancement)
      - Dynamic DNS services (Enhancement)
      - HTTP client downloaded a portable executable (Enhancement)
      - HTTP client downloads a binary (Enhancement)
      - Lateral transfer of possibly suspicious tool over SMB (Enhancement)
      - Submission to Risky Web Forms (Enhancement)
      - Suspected Exfiltration to Cloud Storage Applications (Enhancement)
      - Suspicious DLL Download Attempt (Enhancement)
      - Suspicious EXE Download Attempt (Enhancement)
      - Suspicious Network Activity (Enhancement)
      - Suspicious Network Activity - Telegram (Enhancement)
      - Suspicious POST Request (Enhancement)
      - Suspicious Trello API usage (Enhancement)
    - Threat Prevention Indications:
      - IRC Bot Activity (Enhancement)
      - Malware Activity (Enhancement)
      - Meterpreter Activity (Enhancement)
      - Microsoft Reverse Shell - HoaxShell (Enhancement)
      - Squiblydoo Attack Detection (Enhancement)
      - Unauthorized Directory Access (Enhancement)
- **Suspicious Activity Monitoring:**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - Advanced IP Scanner Download
    - PuTTY SSH Connection To Low Reputation IP
    - PuTTY SSH Connection To Low Reputation Domain
- **Apps Catalog:**
  - Added over 300 new SaaS applications, including more than 140 new Generative AI Tools (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), and enhanced these applications:
    - Amazon
    - Apple App store
    - Apple iCloud
    - Bing
    - CNN
    - Deezer
    - Digicert
    - dotomi
    - eBay
    - Fox News
    - GitHub
    - Google Ads
    - Google Maps
    - GoToMyPC
    - Intercom
    - Microsoft General
    - Mozilla
    - OneDrive
    - Outlook
    - Reddit
    - Salesforce
    - Skype and MS Teams
    - Snapchat
    - Solar Winds N-Central & MSPC
    - Spotify
    - Steam
    - Symantec End-Point Protection
    - Tor Network
    - Windows Update
    - Yahoo Mail
    - Zendesk
- **Application Control (CASB and DLP):**
  - Enhanced granular actions for the following apps:
    - Outlook: Add attachment
    - YouTube: Watch
  - Enhanced DLP content matching for the following app:
    - Outlook: Upload

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
