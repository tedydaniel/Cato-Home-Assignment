---
title: "Product Update - June 10, 2024"
slug: "product-update-june-10-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-june-10-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - June 10, 2024

## New Features & Enhancements

- **CASB Enhancement - Visibility for All Cloud App Activities:** We added an option to configure **Any Activity** in a single [Application Control](/v1/docs/managing-the-application-control-policy) rule that monitors all app activities. This lets you configure a single rule that monitors **Any Activity** for **Any Cloud Application** to discover all the apps and activities used on your network.
  - For customers with a new CASB license, a rule that monitors **Any Activity** for **Any Cloud Application** is automatically added at the bottom of the Application Control rulebase
- **New Academy Training - Network Operation Stories in XDR:** Learn how Cato XDR can help Network Operation Center (NOC) teams identify and resolve network and connectivity issues. This [training unit](https://academy.catonetworks.com/network-stories-in-cato-xdr) helps you understand:
  - Building blocks of Network stories
  - XDR functionality for network issues
  - Reporting and notification options

Go to the [Cato Product Roadmap](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fbit.ly%2F49aFEKU&amp;data=05%7C02%7Cmichael.goldberg%40catonetworks.com%7C98a0c3b85bc6404ffc4408dc88653424%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638535215452009450%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&amp;sdata=X2NvQNrG2OSBaL2C95Jkp5ltQX6rB6BsDRlZ4LwgYoo%3D&amp;reserved=0) in the Knowledge Base to follow the status of upcoming features and enhancements.

## Cato Client Releases

- **New Client Versions**: From June 6, 2024, we started the rollout of the following Clients:

The new versions contain an important security update and bug fixes.
  - Windows version 5.10.34
  - Linux version 5.2.1.1
  - Android version 5.0.3.117

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog)
    - Ransomware 0day (Enhancement)
    - Ransomware Banta (New)
    - Ransomware BOMBO (Enhancement)
    - Ransomware Chaddad (Enhancement)
    - Ransomware EDHST (Enhancement)
    - Ransomware Eject (Enhancement)
    - Ransomware FUNNY (Enhancement)
    - Ransomware Harma (Enhancement)
    - Ransomware Lexus (Enhancement)
    - Ransomware Nett (Enhancement)
    - Ransomware OPIX (Enhancement)
    - Ransomware payB (Enhancement)
    - Ransomware POLSAT (New)
    - Ransomware Qilin (New)
    - Ransomware QRYPT (New)
    - Ransomware Stop/Djvu (Enhancement)
    - Ransomware SYSDF (Enhancement)
    - Ransomware xDec (Enhancement)
    - Sality Checkin (New)
    - Ducktail-Payload Communication(New)
    - FlyStudio - CnC Activity (New)
    - Low Credibility File Names(New)
    - CVE-2024-31982 (New)
    - CVE-2020-25858 (New)
    - CVE-2021-26914 (New)
    - CVE-2022-47075 (New)
    - CVE-2023-38204 (New)
    - CVE-2023-50386 (New)
    - CVE-2024-21683 (New)
    - CVE-2024-24919 (New)
    - CVE-2024-31848 (New)
    - CVE-2024-31849 (New)
    - CVE-2024-31850 (New)
    - CVE-2024-31851 (New)
    - CVE-2024-32113 (New)
    - CVE-2024-3273 (New)
    - CVE-2024-4040 (New)
    - CVE-2024-4956 (New)
    - CVE-2024-4978 (New)
    - Generic Java Serialization Over HTTP (New)
    - JS File Downloaded From Low-Popularity Target (New)
- **Detection & Response:**
  - These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
    - Threat Hunting Indications:
      - Communication with suspicious targets (New)
      - Dynamic DNS services (Enhancement)
    - Threat Prevention:
      - Suspicious DNS Communication with Blacklisted Targets
- **Suspicious Activity Monitoring:**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - Downloading Teamviewer (New)
    - Lateral Batch Script Transfer (New)
    - SimpleHelp Remote Management Tool Lateral Remote Connectivity (New)
    - TeamViewer Inbound Remote Session (New)
    - Wininet/Winsock (Native Windows Client) to low Popularity (Enhancement)
    - AnyDesk WAN Remote Desktop Connection Initiation (New)
    - Transfer AnyDesk over SMB (New)
- **Apps Catalog:**
  - Added over 100 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - C3 AI
    - Intuit sub-services:
      - TurboTax
      - QuickBooks
      - Mint
      - Credit Karma
      - Mailchimp
  - Enhanced these applications:
    - Commvault
    - ProtonVPN
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - IoT:
      - Access Point:
      - 
        - Aruba Networks (Enhancement)
      - Docking Station:
      - 
        - Action Star (Enhancement)
      - IP Camera:
      - 
        - Axis (Enhancement)
        - Hanwha (Enhancement)
        - Verkada (Enhancement)
      - IoMT:
      - 
        - Ascom (Enhancement)
      - Media Server:
      - 
        - BrightSign (Enhancement)
      - Network Appliance:
      - 
        - Cisco Meraki (Enhancement)
        - Ewon (Enhancement)
        - Juniper Networks (Enhancement)
        - Synology (Enhancement)
      - Payment Terminal:
      - 
        - CCV (Enhancement)
        - Castles Technology (Enhancement)
        - Verifone (Enhancement)
      - Power Device:
      - 
        - APC (Enhancement)
      - Printer
      - 
        - Canon (Enhancement)
        - HP (Enhancement)
        - Lexmark (Enhancement)
        - Ricoh (Enhancement)
        - Xerox (Enhancement)
        - Zebra (Enhancement)
      - Single Board Computer:
      - 
        - Raspberry Pi Foundation (Enhancement)
      - Smart Display:
      - 
        - Kyocera (Enhancement)
      - VoIP:
      - 
        - Cisco (Enhancement)
        - Commend (Enhancement)
        - Digium (Enhancement)
        - Grandstream Networks (Enhancement)
        - Innovaphone (Enhancement)
        - Mitel (Enhancement)
        - Polycom (Enhancement)
        - Snom (Enhancement)
        - Ubiquiti (Enhancement)
        - Yealink (Enhancement)
      - WAP:
      - 
        - Cambium Networks (Enhancement)
        - Cisco (Enhancement)
      - Video Encoder:
        - Axis (Enhancement)
    - Mobile:
      - Mobile Phone:
      - 
        - Samsung (Enhancement)
      - Tablet:
      - 
        - Amazon (Enhancement)
        - Apple (Enhancement)
      - Thin Client:
      - 
        - Dell (Enhancement)
        - PCoIP Endpoint Device (Enhancement)
      - Workstation:
        - Apple (Enhancement)
        - Dell (Enhancement)
        - HP (Enhancement)
        - MSI (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
