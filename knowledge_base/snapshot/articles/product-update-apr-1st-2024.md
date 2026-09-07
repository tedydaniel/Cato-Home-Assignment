---
title: "Product Update - Apr. 1st, 2024"
slug: "product-update-apr-1st-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-apr-1st-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Apr. 1st, 2024

## New Features & Enhancements

- **Improved Usability for Muting XDR Security Stories:** To simplify the process for creating a [Mute Stories](/v1/docs/muting-xops-stories) rule from an XDR security story in the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench), the **Source** and **Destination** values are now automatically populated based on the story data.
- **ML-Based Predictions and Similar Stories for XDR Anomaly Stories:** We enriched the XDR [Usage Anomaly and Events Anomaly](/v1/docs/analyzing-xops-ueba-stories-for-usage-and-events-anomalies) stories with the following new fields:
  - **Predicted Verdict** and **Predicted Type:** Machine learning predictions for the probable verdict and potential malware type that you may identify. This helps you make an initial assessment of the likelihood that a story is malicious.
  - **Similar Stories:** A list of stories that helps you get important context for your analysis by showing stories with similar targets.
  - Anomaly stories are available for XDR Pro and MDR customers.
- **New Query API to Easily Integrate Cato XDR with SIEM Solutions**: We're introducing a [new query API](http://api.catonetworks.com/documentation/#introduction) for Cato XDR stories that lets you automate flows and implement integrations with your SIEM or other systems.
  - The API includes Security and Network stories
- **Include Any Vendor or Product in Device Posture Checks:** You can create a general [Device Posture check](/v1/docs/creating-device-posture-profiles-and-device-checks) for any supported vendor or product. For example, you can create a check to allow access for a device with any of the supported Anti-Malware solutions installed. This improves usability for admins adopting Device Posture gradually.
  - Previously you had to specify which vendor or product to check for
  - Supported for Anti-Malware, Firewall, Patch Management, and DLP Device Posture checks
- **Introducing the Cato Academy Training Portal**: The Cato [Learning Center](https://support.catonetworks.com/hc/en-us) now includes the Cato Academy with a range of training options to complement the Community and Knowledge Base. The Cato Academy includes: eLearning courses, videos, certifications, and you can register for online sessions and webinars.
  - Check it out at: [https://academy.catonetworks.com](https://academy.catonetworks.com/)
- **Roadmap Updates:** Go to the [Cato Product Roadmap](https://auth.catonetworks.com/?backTo=https://%7Bsubdomain%7D.auth.catonetworks.com/zd/authenticate?brand_id%3D1168669%26locale_id%3D1%26return_to%3Dhttps%253A%252F%252Fsupport.catonetworks.com%252Fhc%252Fen-us%252Farticles%252F14517158733853-Cato-Product-Roadmap%26timestamp%3D1781111373) in the Knowledge Base to follow the status of upcoming features and enhancements.

## Cato SDP Client Releases

- **Windows Client v5.10.26:** From March 31st, 2024, we are starting the rollout of Windows Client version 5.10.26. This version contains bug fixes including:
  - Anti-Malware Device Checks could not validate Microsoft Defender for Endpoint (Defender ATP) real-time protection
- **iOS Client v5.3:** From April 6th, 2024, the iOS Client version 5.3 will gradually be available for download from the App Store. You can download this version for testing before it is rolled out to your users [here](https://testflight.apple.com/join/ob2m1ra0).
  - This version contains:
    - **New Device Posture Check for Device Certificates Provides Increased Security:** You can now include a check for Device Certificates within your [Device Posture Profiles](/v1/docs/creating-device-posture-profiles-and-device-checks). The Device Posture Profile can be included in your Client Connectivity and Security policies
    - **Increased Visibility of Connection Data:** The **Statistics** page in the Client now displays the status of the Split Tunnel Policy and the Proxy Configuration Policy
    - Bug fixes and enhancements

## PoP Announcements

- **Osaka, JP:** A new IP range will soon become available in the Osaka PoP location - 202.75.243.0/24

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog)
    - Ransomware DeepInDeep (New)
    - Ransomware Nacugunder (New)
    - Ransomware Afire (Enhancement)
    - Ransomware cursoDFIR (Enhancement)
    - Ransomware DoNex (Enhancement)
    - Ransomware Duralock (Enhancement)
    - Ransomware Genesis (Enhancement)
    - Ransomware Gotmydatafast (Enhancement)
    - Ransomware Locked (MedusaLocker) (Enhancement)
    - Ransomware Ncov (Enhancement)
    - Ransomware Payuranson (Enhancement)
    - Ransomware Rocklee (Enhancement)
    - Ransomware Stop/Djvu (Enhancement)
    - Ransomware Zarik Locker (Enhancement)
    - Malware SilentCryptoMiner Checkin (New)
    - Malware WasabiSeed (New)
    - CVE-2024-20767 (New)
    - CVE-2023-48023 (New)
    - CVE-2023-42442 (New)
    - CVE-2023-35813 (New)
    - CVE-2023-3486 (New)
    - CVE-2023-31419 (New)
    - CVE-2023-2522 (New)
    - CVE-2022-32994 (New)
    - CVE-2021-32924 (New)
    - CVE-2021-26120 (New)
    - Nagios XI Command Injection (New)
    - Malicious IP based on ASN scoring (New)
- **Detection & Response**
  - These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
    - Threat Hunting Indication:
      - Suspicious Scanning Tool Download (New)
    - Threat Prevention Indication:
      - Blocked Phishing Attack (Enhancement)
- **Suspicious Activity Monitoring:**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - Download Impersonated Image (New)
    - Enumerating User Terminal Sessions in RPC (New)
    - Harnessing spools service to gain authentication on target machine (New)
    - Pastebin Bot Communication (New)
    - PowerShell impersonated IMG (New)
- **TLS Inspection:**
  - Added [TLS inspection](/v1/docs/configuring-tls-inspection-policy-for-the-account) for on Safari browser for these applications:
    - Dropbox
    - WhatsApp
- **Apps Catalog:**
  - Added over 100 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), and enhanced these applications:
    - Airslate
    - IPFS
    - Tor Network
    - WireGuard Protocol
- **Application Control (CASB and DLP):**
  - Enhanced granular actions for the following app:
    - Bing AI - Search
- **File Identification:**
  - Enhanced file identification in Cato Cloud services for the following file type:
    - Binary files
- **Client Classification:**
  - Azure Remote Desktop (New)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
