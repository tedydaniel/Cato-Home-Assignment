---
title: "Product Update - July 7, 2025"
slug: "product-update-july-7-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-july-7-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - July 7, 2025

## New Features & Enhancements

- **Time-Based Configuration for Internet and WAN Firewall Rules:** To give you more control over temporary access, you can now configure [Internet](/v1/docs/what-is-the-cato-internet-firewall) and [WAN](/v1/docs/what-is-the-cato-wan-firewall) firewall rules with a defined start and/or expiration time. This helps you enforce security policies more effectively and reduces the risk of unused rules remaining active.
  - Click [here](https://academy.catonetworks.com/time-expiration-in-firewall-rules) to watch a video recording of this feature

- **Extending Cato UZTNA with Identity for Shared Hosts:** For User Awareness, the Cato [Identity Agent](/v1/docs/using-cato-identity-agents-for-user-awareness) can now identify multiple users connecting to a shared host behind a site. This lets you apply different policies for each of the users or user groups, and provides visibility into the user activities.
  - Supported on Windows Client v5.15 and higher
  - No ZTNA (SDP) license is required for using the Windows Client as an Identity Agent

- **New WAN Firewall Event Fields for NAT Translations:** For better investigation and troubleshooting of connections for internal resources that [require NAT](/v1/docs/configuring-a-site-level-nat-policy), we added WAN Firewall event fields for the translated source (client) and destination (server) IPs. These are the new field names:
  - Translated client IP
  - Translated server IP

- **Next Gen LAN Firewall Improvements:**
  - Send a notification when traffic matches a LAN Firewall rule
  - New event fields for LAN Firewall events:
    - **Domain Name** - Shows internal LAN apps
    - **HTTP Method** - Specifies the action a client intends to perform on a resource when communicating with a server
  - Identifies the WebDAV app
  - Supported from Socket v24 and higher

## PoP Announcements

- The following new PoP locations are now available:
  - **Buenos Aires, AR:** 199.27.41.0/24
  - **Lagos, NG:** 216.252.185.0/24
  - **Vienna, AT:** 216.252.184.0/24

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2018-9843 (New)
    - CVE-2019-9875 (New)
    - CVE-2023-39780 (New)
    - CVE-2024-38475 (Enhancement)
    - CVE-2024-4325 (New)
    - CVE-2025-20188 (New)
    - CVE-2025-28367 (New)
    - CVE-2025-32432 (New)
    - CVE-2025-4632 (New)
    - CVE-2025-49493 (New)
    - Heuristic - Generic Phishing (New)
    - Inspur GS Insecure Deserialization in the GetChildFormAndEntityList (New)
    - Kingdee ERP Insecure Deserialization (New)
    - Malware - Pingback CnC (New)
    - Malware - Pingpull RAT CnC (New)
    - Ransomware - 9062 (Enhancement)
    - Ransomware - AMERILIFE (Enhancement)
    - Ransomware - Backups (Enhancement)
    - Ransomware - BlackHeart (MedusaLocker) (Enhancement)
    - Ransomware - Blackransombdbot (Enhancement)
    - Ransomware - DataLeak (Enhancement)
    - Ransomware - DELTA (Enhancement)
    - Ransomware - Dire Wolf (Enhancement)
    - Ransomware - EnCiPhErEd (Enhancement)
    - Ransomware - Harma (Enhancement)
    - Ransomware - Hero (Enhancement)
    - Ransomware - KaWaLocker (Enhancement)
    - Ransomware - Kyj (Enhancement)
    - Ransomware - NightSpire (Enhancement)
    - Ransomware - Ololo (Enhancement)
    - Ransomware - Pgp (Enhancement)
    - Ransomware - Puld (Enhancement)
    - Ransomware - SafeLocker (Enhancement)
    - Ransomware - Smile (Enhancement)
    - Ransomware - SparkLocker (Enhancement)
    - Ransomware - THRSX (Enhancement)
    - Ransomware - UraLocker (Enhancement)
    - Ransomware - Vatican (Enhancement)
    - Ransomware - Veluth (Enhancement)
    - Ransomware - ZV (Enhancement)
- **Suspicious Activity Monitoring:**
  - These protections were added to the SAM service:
    - Abnormal Large ICMP Ping Request Size (New)
    - Download MCP File From Low Popularity Target (New)
    - Gather Machine Data Protection API keys (New)
    - Gather User Data Protection API keys (New)
    - Impacket-Based Script Execution (New)
    - Suspected VPN Traffic Over ICMP (New)
    - Utilizing Wkssvc to gain users who are currently active on a remote computer, associated with SharpHound (New)
- **Apps Catalog**
  - New Cloud Apps (see [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - Ultraviewer (new)
    - IP cameras P2P (new)
    - Dolynk cameras (new)
    - Dahua cameras (new)
    - AmcrestView Cameras (new)
    - Burg.biz Cameras (new)
    - IPTecno Cameras (new)
    - Imou Cameras (new)
    - Qsee Cameras (new)
- **XDR Indications Of Attack Signatures:**
  - **Anomaly Detection:**
    - Abnormal Outbound File Sharing Activity (New)
    - Abnormal IPS Block Activity (New)
    - Abnormal Prompt Activity (Enhancement)
    - First Time Upload to an S3 Bucket (Enhancement)
    - Abnormal Remote Access Protocol Activity (New)
  - **Threat** **Hunting:**
    - DNS Queries to Phishing-Related Domains (Enhancement)
    - Device Attributes Exfiltration (Enhancement)
    - Domain Generation Algorithm ML Model Detection (Enhancement)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - **IOT**
      - Docking Station
        - Action Star (Enhancement)
      - Printer
        - Brother (Enhancement)
        - Canon (Enhancement)
        - HP (Enhancement)
        - Lexmark (Enhancement)
        - Ricoh (Enhancement)
        - Xerox (Enhancement)
        - Zebra (Enhancement)
      - Signage Media Player
        - BrightSign (Enhancement)
        - Generic Signage (New)
        - Optisigns Signage (New)
      - Smart Display
        - Kyocera (Enhancement)
      - VoIP
        - Aastracom (Enhancement)
        - Algo (Enhancement)
        - Cisco (Enhancement)
        - Grandstream Networks (Enhancement)
        - Mitel (Enhancement)
        - Polycom (Enhancement)
        - Siemens (Enhancement)
        - Snom Technology (Enhancement)
        - Yealink (Enhancement)
        - Yealink Desk Phone (Enhancement)
      - Media Player
        - Apple TV (Enhancement)
      - IoT Gateway (New)
        - DeviceTone Genie IoT Gateway (New)
      - IP Camera
        - Axis (Enhancement)
        - Verkada (Enhancement)
        - Xiaoyi IP Camera (New)
        - Generic IP Camera (Enhancement)
    - **PC**
      - Desktop
        - HP (Enhancement)
        - Lenovo (Enhancement)
      - Laptop
        - Apple (Enhancement) Dell (Enhancement)
        - HP (Enhancement)
        - Lenovo (Enhancement)
        - Microsoft (Enhancement)
        - Toshiba (Enhancement)
        - Macbook (Enhancement)
      - Thin Client
        - Dell (Enhancement)
      - Workstation
        - Fujitsu (Enhancement)
        - Gigabyte Technology (Enhancement)
        - HP (Enhancement)
        - NEC (Enhancement)
        - Panasonic (Enhancement)
        - iMac (Enhancement)
        - iMac Pro (Enhancement)
        - Mac Mini (Enhancement)
    - **Networking**
      - Network Appliance
        - Aruba Networks (Enhancement)
      - WAP
        - Cisco (Enhancement)
    - **Mobile**
      - Mobile Computer
        - Zebra (Enhancement)
      - Mobile Phone
        - OnePlus (Enhancement)
        - Samsung (Enhancement)
        - Zebra (Enhancement)
        - iPhone (Enhancement)
        - Generic Mobile Phone (Enhancement)
      - Tablet
        - Microsoft (Enhancement)
        - Samsung (Enhancement)
        - iPad (Enhancement)
      - iPod (Enhancment)
      - Smart Watch
        - Apple Watch (Enhancement)
    - **Server**
      - Media Server
        - BrightSign (Enhancement)
      - Print Server
        - HP (Enhancement)
