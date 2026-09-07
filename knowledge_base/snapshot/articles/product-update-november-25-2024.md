---
title: "Product Update - November 25, 2024"
slug: "product-update-november-25-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-november-25-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - November 25, 2024

## New Features & Enhancements

- **Exclude Applications from Split Tunnel Policy Rules:** For better customization of traffic routing for remote users, you can exclude traffic to specific applications from your [Split Tunnel policy](/v1/docs/routing-with-the-cato-client-split-tunnel-policy). For example, you can configure all traffic to be routed to Cato, except traffic from Zoom.
  - The supported applications are: Google Applications, Outlook, SharePoint and OneDrive Business, Skype and MS Teams, and Zoom
  - Click [here](https://academy.catonetworks.com/application-based-split-tunneling-for-sdp-clients) to watch a video recording of this feature
- **Control CMA Notifications for Your Accounts:** Did you know that you can configure the Cato Management Application (CMA) to send [alerts and notifications](/v1/docs/account-level-alerts-and-system-notifications) to Subscription Groups, mailing lists, or integrations for different activities in your account, such as: locked admins and users, Socket upgrades, user provisioning actions, and more.

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2024-10965 (New)
    - CVE-2024-28987 (New)
    - CVE-2024-28999 (New)
    - CVE-2024-43451 (New)
    - CVE-2024-45507 (New)
    - CVE-2024-9264 (Enhancement)
    - Malware Smokeloader - Payload (New)
    - Ransomware Arcus (New)
    - Ransomware Biobio (Kasper) (New)
    - Ransomware DARKSET (New)
    - Ransomware Harma (Enhancement)
    - Ransomware Heda (Enhancement)
    - Ransomware MrBeast (New)
    - Ransomware Nyxe (Enhancement)
    - Ransomware PlayBoy Locker (Enhancement)
    - Ransomware Sougolock (Enhancement)
    - Scanners - Multi Service Port Scanning (Enhancement)
- **XDR Indications Of Attack Signatures:**
  - Threat Hunting:
    - Spoofed Browser Activity (New)
    - DNS Queries to Phishing-Related Domains (New)
    - Suspicious Non-browser HTTP Activity (Enhancement)
  - Threat Prevention:
    - File Download Attempt from Low-Reputation Target (New)
    - Periodic Communication to Low-Popularity Domains or Ips (New)
- **Apps Catalog**
  - More than 150 new Cloud apps (see Apps Catalog):
    - SageHR (New)
    - Microsoft Office365 )Enhancement)
    - Microsoft General (Enhancement)
    - Microsoft Copilot (Enhancement)
    - SSDP (Enhancement)
    - Movebot (New)
  - Categories:
    - PDF Converters (New)
- **Application Control (CASB and DLP):**
  - Enhanced granular activities for the following apps:
    - Box – Download (Enhancement)
- **File Control:**
  - Archive:
    - Bzip2 (bz, bz2) (Enhancement)
    - Stuffit Archive (stuffit_sit, stuffit) (New)
  - Certificates and Identities files (New):
    - Cert (cer) (New)
    - Cert (crt) (New)
  - Database:
    - SQL (sql, sqlproj, eql) (New)
  - Design:
    - 3dm (New)
  - Executables and Installers:
    - Android Application Package (apk) (Enhancement)
    - Chrome Extension (crx) (Enhancement)
    - iPhone Application (ipa) (New)
  - Fonts (New):
    - TrueType Font (ttf) (New)
    - Web Open Font Format (woff2) (New)
  - Gaming (New)
    - Game Boy Advance (gba) (New)
    - Nintendo DS (3ds, nds) (New)
    - PlayStation (psx) (New)
    - Sega 32X (32x) (New)
  - Generic Textual Group:
    - Kml (New)
    - XAML (xaml) (New)
    - YAML (yaml, yml) (New)
  - Images:
    - Dicom (dcm) (New)
  - Misc and Others:
    - PCAP file (pcap, pcapng) (New)
  - Scripts:
    - Include (inc) (New)
    - Make (mak, mk) (New)
    - NUPKG (nupkg) (New)
  - Source Code:
    - Swift (swift) (New)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - Networking
      - Network Appliance
        - Synology (Enhancement)
    - IOT
      - Printer
        - Brother (Enhancement)
        - HP (Enhancement)
        - Xerox (Enhancement)
        - Zebra (Enhancement)
      - VoIP
        - Avaya (Enhancement)
        - Grandstream (Enhancement)
        - Innovaphone (Enhancement)
        - Polycom (Enhancement)
      - Docking Station
        - Action Star (Enhancement)
      - Payment Terminal
        - Verifone (Enhancement)
      - Smart TV
        - Samsung (Enhancement)
      - Wireless HDMI
        - Airtame (Enhancement)
    - OT,IOT
      - IP Camera
        - Verkada (Enhancement)
    - Mobile
      - Mobile Phone
        - Redmi (Enhancement)
        - Oppo (Enhancement)
        - Samsung (Enhancement)
    - Server
      - Media Server
        - Roku (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
