---
title: "Product Update - Apr. 29th, 2024"
slug: "product-update-apr-29th-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-apr-29th-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Apr. 29th, 2024

## New Features & Enhancements

There are no new features or enhancements for the Cato service for this week. Take a look at these great features that we released over the past few weeks:

- **Entra ID (Azure AD) Sign-in Activity Integration:** Admins can comprehensively view usage within their ecosystem of sanctioned apps to identify potential security concerns by integrating Entra ID sign-in activity with Cato. The [Entra ID API connector](/v1/docs/configuring-the-microsoft-entra-id-azure-ad-connector) extends visibility to all user sign-in and sign-in anomaly events, showcased in the [Cloud Activity Dashboard](https://support.catonetworks.com/hc/en-us/articles/15931659820445-Using-the-Cloud-Activity-Dashboard) and security event sub-types for sign-in and identity-related anomalies.
- **Seamlessly Connect your Cloud Tenants to Cato:** We enhanced [Cross Connect sites](/v1/docs/cloud-interconnect-sites) and added a turnkey provisioning configuration so you can quickly connect your cloud resources to the Cato PoP location.
  - Supported Cloud Providers: AWS DirectConnect, Azure Express Route, GCP Interconnect, Oracle FastConnect
- **AWS Marketplace vSocket Deployment:** Cato simplified and streamlined the deployment process for [AWS virtual Sockets](/v1/docs/deploying-a-vsocket-site-from-the-aws-marketplace) (vSockets) by using the AWS Marketplace. The marketplace automatically creates the necessary virtual resources for the vSocket.
  - Previously you could only manually deploy AWS vSockets
- **Access Policies and Improvements:** Check out these improvements for Remote Access policies that provide increased flexibility:
  - **Policy to Manage Proxy Configuration File:** Provides a granular method to easily manage PAC files, used by the Client for [proxy configuration](/v1/docs/centralized-management-of-proxy-configuration-proxy-configuration-policy)
  - **Split Tunnel Policy:** Provides a granular method to easily configure [traffic routing](/v1/docs/routing-with-the-cato-client-split-tunnel-policy) for remote users and control which traffic is tunneled towards the Cato Cloud
  - **Enforce Different Security Policies When a User Connects Behind a Site or Remotely:** You can use the [Device Posture Profiles](/v1/docs/creating-device-posture-profiles-and-device-checks) to enforce different security policy rules when a user connects remotely with the Client or behind a site
  - **Device Posture Check Enforces Minimum Client Version:** You can ensure any device connecting to your network has a [minimum Client Client version installed](/v1/docs/creating-device-posture-profiles-and-device-checks) on it

Go to the [Cato Product Roadmap](https://support.catonetworks.com/hc/en-us/articles/14517158733853-Cato-Product-Roadmap) in the Knowledge Base to follow the status of upcoming features and enhancements.

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog)
    - Ransomware - DumbStackz (Enhancement)
    - Ransomware - FBIRAS (Enhancement)
    - Ransomware - AttackFiles (New)
    - Ransomware - HWABAG (New)
    - Ransomware - DysentryClub (Enhancement)
    - Ransomware - Crocodile Smile (Enhancement)
    - Ransomware - L00KUPRU (Enhancement)
    - Ransomware - Datah (Enhancement)
    - Ransomware - Rincrypt (Enhancement)
    - Ransomware - Unkno (Enhancement)
    - Ransomware - Ncov (Enhancement)
    - Ransomware - Stop/Djvu (Enhancement)
    - Malware - Cryptbotv2-CnC communication (New)
    - Malware - DarkGate CnC communication (New)
    - Malware - ObserverStealer CnC communication-Check-in (New)
    - Malware - FFDroider-CnC communication (New)
    - Malware - Vodkagats Loader CnC communication-Payload (New)
    - Malware - TrickBot Anchor-Checkin (New)
    - Malware - Vidar Stealer CnC communication - Style Headers In HTTP POST (New)
    - Malware - Vidar Stealer CnC communication - Style Headers post (New)
    - Malware - Stealc Stealer CnC communication - Style Headers post (New)
    - Malware - Generic Stealer CnC communication - Style Headers post (New)
    - Malware - GCleaner Downloader - CnC communication (New)
    - Malware - Konni RAT CnC communication (New)
    - Malware - PureLogs Stealer - C2 Connection (New)
    - Malware - Arkei Stealer C2C Communication - IP Lookup (Enhancement)
    - CVE-2022-38108 (New)
    - CVE-2023-32714 (New)
    - CVE-2024-3400 (Enhancement)
    - CVE-2023-26477 (New)
    - CVE-2024-25153 (New)
    - CVE-2024-1403 (New)
    - CVE-2023-43208 (New)
    - CVE-2020-24391 (New)
    - CVE-2023-4634 (New)
    - CVE-2022-4305 (New)
    - CVE-2018-14716 (New)
    - CVE-2023-24955 (New)
    - CVE-2020-13957 (New)
    - CVE-2023-36210 (New)
    - CVE-2021-31474 (New)
    - Exploiting Server Side Template Injection to gain Remote Code Execution (New)
- **Detection & Response:**
  - These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
    - Threat Hunting Indications:
      - Malware DNS Activity (Emotet) (Enhancement)
      - Dynamic DNS services (Enhancement)
      - Suspicious Network Traffic (Enhancement)
      - Suspicious Cryptomining Activity (JSON-RPC) (Enhancement)
      - Suspicious SSH Communication to Low-Popularity Domains (Enhancement)
      - Lateral transfer of possibly suspicious tool over SMB (Enhancement)
    - Threat Prevention:
      - Suspicious TOR Traffic (Enhancement)
- **Suspicious Activity Monitoring:**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - Downloading PowerToll (New)
    - Lateral ADfind transfer over SMB (Enhancement)
    - Lateral Filezilla transfer (Enhancement)
    - Lateral PuTTY transfer (Enhancement)
    - Lateral MobaXterm transfer (Enhancement)
    - Lateral Nmap transfer (Enhancement)
    - Lateral Mimikatz transfer (Enhancement)
    - Lateral WinSCP transfer (Enhancement)
    - Lateral Powershell script transfer (New)
    - Lateral Netcat transfer over SMB (Enhancement)
- **Apps Catalog:**
  - Added over 100 new SaaS applications including (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)):
    - Enhanced these apps:
      - Private Internet Access VPN (Enhancement)
      - Tunnelbear (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
