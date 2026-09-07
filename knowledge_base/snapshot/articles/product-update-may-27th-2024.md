---
title: "Product Update - May 27th, 2024"
slug: "product-update-may-27th-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-may-27th-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - May 27th, 2024

## New Features & Enhancements

- **New AI-Powered Localization for the Cato Management Application:** We're integrating AI technology to localize the Cato Management Application for these languages:
  - Mandarin (Simplified) Chinese, Hindi, Spanish, French, Bengali, Russian, Portuguese, Korean, and Japanese
  - Easily change the language from the [admin profile](/v1/docs/setting-the-cma-user-interface-preferences)
- **Enhancement for Cloud Activity Dashboard:** The [dashboard](http://support.catonetworks.com/hc/en-us/articles/15931659820445-Using-the-Cloud-Activity-Dashboard) now indicates whether users authenticated to an app via the Cato Cloud or directly over the public Internet. This helps you identify which apps are protected by Cato's Security services and assess the overall security posture for your organization's SaaS app environment.
- **Granular Control for Untrusted Certificates in TLS Inspection Policy:** You can now define how each [TLS Inspection](/v1/docs/configuring-tls-inspection-policy-for-the-account) rule handles untrusted server certificates. For example, create a rule that allows specific traffic from contractors who use self-signed certificates.
  - Previously, the behavior for untrusted certificates was defined globally for the account
  - There is no impact for existing TLS Inspection rules
- **License Query API:** We added a new licenses GraphQL query that retrieves data for the purchased licenses on your account, including status and usage information. Please refer to the [Cato API documentation](https://api.catonetworks.com/documentation/) for detailed schema definitions and reference query calls.
- **Cato Management Application Enhancement:**
  - **IP Range and Floating Ranges Pages:** Added the ability to sort and search for specific entities on these pages. Previously all ranges were always displayed on the pages.

Go to the [Cato Product Roadmap](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcatonetworks.us16.list-manage.com%2Ftrack%2Fclick%3Fu%3D75bb2b7bafe7526c787475fd2%26id%3D2a7169d7d3%26e%3D2b9a2985a2&amp;data=05%7C02%7Cjonathan.rabinowitz%40catonetworks.com%7C98971ce7aae549a4ee1c08dc64642750%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638495628531686831%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&amp;sdata=H1v1TGT3zsRpHAGgTb2rp1Tm9Ulx5Cx5REZMJwfwq5o%3D&amp;reserved=0) in the Knowledge Base to follow the status of upcoming features and enhancements.

## PoP Announcements

- **Update to Localized Range for Croatia:** The localized IP range for Croatia (serviced through the Prague PoP location) is now 209.206.3.0/25

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog)
    - Malware - Latrodectus (New)
    - Ransomware - Capibara (New)
    - Ransomware - EnigmaWave (New)
    - Ransomware - Mango (New)
    - Ransomware - Shadow (New)
    - Ransomware - EDHST (Enhancement)
    - Ransomware - Eject (Enhancement)
    - Ransomware - KUZA (Enhancement)
    - Ransomware - Ncov (Enhancement)
    - Ransomware - OPIX (Enhancement)
    - Ransomware - Robaj (Enhancement)
    - Ransomware - SHINRA (Enhancement)
    - Ransomware - Stop/Djvu (Enhancement)
    - CVE-2024-31982 (New)
    - CVE-2024-2389 (New)
    - CVE-2024-20931 (New)
    - CVE-2023-3368 (New)
    - CVE-2021-45456 (New)
    - CVE-2021-43164 (New)
    - CVE-2021-32706 (New)
    - CVE-2020-3495 (New)
    - CVE-2019-9733 (New)
    - CVE-2019-17444 (New)
    - CVE-2018-1000600 (New)
- **Detection & Response:**
  - These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
    - Threat Prevention:
      - Potential Hack Tool Download (New)
- **Suspicious Activity Monitoring:**
  - These protections were added to the [SAM service:](/v1/docs/monitoring-suspicious-activity-with-ips-sam)
    - Outbound Access to a Python simpleHTTP Server (New)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - IoT:
      - Access Point:
        - Aruba Networks (Enhancement)
      - Docking Station:
        - Action Star (Enhancement)
      - IP Camera:
        - Axis (Enhancement)
        - Hanwha (Enhancement)
        - Verkada (Enhancement)
      - IoMT:
        - Ascom (Enhancement)
      - Media Server:
        - BrightSign (Enhancement)
      - Network Appliance:
        - Cisco Meraki (Enhancement)
        - Ewon (Enhancement)
        - Juniper Networks (Enhancement)
        - Synology (Enhancement)
      - Payment Terminal:
        - CCV (Enhancement)
        - Castles Technology (Enhancement)
        - Verifone (Enhancement)
      - Power Device:
        - APC (Enhancement)
      - Printer
        - Canon (Enhancement)
        - HP (Enhancement)
        - Lexmark (Enhancement)
        - Ricoh (Enhancement)
        - Xerox (Enhancement)
        - Zebra (Enhancement)
      - Single Board Computer:
        - Raspberry Pi Foundation (Enhancement)
      - Smart Display:
        - Kyocera (Enhancement)
      - VoIP:
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
        - Cambium Networks (Enhancement)
        - Cisco (Enhancement)
      - Video Encoder:
        - Axis (Enhancement)
    - Mobile:
      - Mobile Phone:
        - Samsung (Enhancement)
      - Tablet:
        - Amazon (Enhancement)
        - Apple (Enhancement)
      - Thin Client:
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
