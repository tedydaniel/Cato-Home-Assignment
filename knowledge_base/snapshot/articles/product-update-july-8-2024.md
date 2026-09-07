---
title: "Product Update - July 8, 2024"
slug: "product-update-july-8-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-july-8-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - July 8, 2024

## New Features & Enhancements

- **Patched Socket Version for Socket v20:** Further to the [security notification](https://support.catonetworks.com/hc/en-us/articles/19952349220381-Security-Vulnerability-CVE-2024-6387-OpenSSH-regreSSHion) from July 3, 2024, Cato Sockets will be automatically upgraded to Socket v20.0.18453 to mitigate a [vulnerability](https://www.catonetworks.com/blog/cve-2024-6387-openssh-rce-vulnerability-regresshion-cato-networks-impact-and-analysis/) found in OpenSSH.
  - To date, Cato's Security Research team has not found any exploitation attempts or viable exploits of this vulnerability in the wild. In addition, by default Cato Sockets do not have a public-facing SSH management interface, limiting exposure to the vulnerability.
- **Dynamic PoP Selection for IPsec Sites:** For improved stability of [IPsec sites](/v1/docs/configuring-ipsec-ikev2-sites), you can use FQDN for the destination of the IPsec tunnel and the PoP dynamically resolves the IP address. You can select to have Cato automatically use the ideal PoP location for the site, or choose a specific PoP location to connect to.
  - When using FQDN, Cato uses DNS responses to dynamically resolve the IP
  - Available for IPsec IKEv2 sites, and Cato Responder mode (FW Init) only
- **App Catalog Shows CASB Granular Activities:** To help you implement your app security policy, you can now use the [App Catalog](/v1/docs/using-the-app-catalog) to see which specific activities are available for an app in [CASB Application Control](/v1/docs/managing-the-application-control-policy) rules. For example, the catalog shows that you can create rules configured with these Salesforce activities: Export, Edit, Save Report, Login, Full Path URL.
  - The catalog also shows the fields that can be configured for each activity

Go to the [Cato Product Roadmap](https://bit.ly/49aFEKU) in the Knowledge Base to follow the status of upcoming features and enhancement

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - Kryptik Dropper CnC Communication (New)
    - Kryptik Dropper-CNC Communication (New)
    - Lumma Stealer CnC Communication-Configuration Attempt (New)
    - PikaBot Loader CnC Checkin (New)
    - Ransomware 2000USD (Enhancement)
    - Ransomware Anonymous Arabs (Enhancement)
    - Ransomware AzzaSec (Enhancement)
    - Ransomware Cebrc (Enhancement)
    - Ransomware DataDestroyer (Enhancement)
    - Ransomware Geometrical (Enhancement)
    - Ransomware GhostHacker (Enhancement)
    - Ransomware Harma (Enhancement)
    - Ransomware Inc (New)
    - Ransomware Jinwooks (Enhancement)
    - Ransomware LIZARD (Enhancement)
    - Ransomware Lsoc (Enhancement)
    - Ransomware Ncov (Enhancement)
    - Ransomware ONION (Enhancement)
    - Ransomware Rapax (Enhancement)
    - Ransomware Senanam (Enhancement)
    - Ransomware Stop/Djvu (Enhancement)
    - RansomwareSYSDF (Enhancement)
    - Scanners - Netscan write access block (New)
    - CVE-2014-100005 (New)
    - CVE-2016-2510 (New)
    - CVE-2019-19642 (New)
    - CVE-2021-26857 (Enhancement)
    - CVE-2021-31252 (New)
    - CVE-2022-30448 (New)
    - CVE-2022-31830 (New)
    - CVE-2022-38129 (New)
    - CVE-2023-1718 (New)
    - CVE-2023-39362 (New)
    - CVE-2023-49606 (New)
    - CVE-2024-20404 (New)
    - CVE-2024-2053 (New)
    - CVE-2024-22320 (New)
    - CVE-2024-2448 (New)
    - CVE-2024-27348 (New)
    - CVE-2024-28254 (New)
    - CVE-2024-29059 (New)
    - CVE-2024-29849 (New)
    - CVE-2024-29973 (New)
    - CVE-2024-4577 (New)
    - CVE-2024-5806 (New)
- **Detection & Response:**
  - These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
    - Threat Hunting Indications:
      - Exploitation Attempt (Enhancement)
      - Suspicious Network Activity (User-Agent) (Enhancement)
    - Threat Prevention:
      - CVE Exploitation Attempt (Inbound) (New)
    - Domain Generation Algorithm (DGA) Communication (Enhancement)
    - Log4j C2 Communication (Enhancement)
    - Metasploit Exploitation Detection (Enhancement)
- **Suspicious Activity Monitoring**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - SimpleHelp Lateral Tool Transfer (New)
    - SimpleHelp Remote Management Tool Remote Connectivity UDP (New)
    - Teamviewer Lateral Transfer Over SMB (New)
    - TeamViewer WAN Lateral Remote Connectivity (New)
- **Apps Catalog:**
  - Added over 100 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - Myepaywindow (New)
    - Proton VPN (Enhancement)
    - X-VPN (Enhancement)
- **Application Control (CASB and DLP):**
  - Enhanced granular activities for the following apps:
    - Zoho Mail - Add Attachment, Send Mail
    - Zoho - Login, Login Third Party
    - Citrix Sharefile - Login
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - **IOT**:
      - Payment Terminal
        - Castles Technology (Enhancement)
        - Ingenico (Enhancement)
      - Printer
        - Xerox (Enhancement)
      - Smart TV
        - Samsung (Enhancement)
      - VoIP
        - Avaya (Enhancement)
        - Cisco (Enhancement)
        - Grandstream Networks (Enhancement)
        - Polycom (Enhancement)
        - Ubiquiti (Enhancement)
    - Networking:
      - Network Appliance
        - Aruba Networks (Enhancement)
    - Mobile
      - Mobile Phone
        - Redmi (Enhancement)
        - Samsung (Enhancement)
- **Client Classification:**
  - Client Class Enhancement | NMAP (New)

**Note:** Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](https://support.catonetworks.com/hc/en-us/articles/11968052021277-Understanding-Cato-s-Gradual-Rollout). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
