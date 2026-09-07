---
title: "Product Update - Aug 19, 2024"
slug: "product-update-aug-19-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-aug-19-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Aug 19, 2024

There are no new features or enhancements for the Cato service for this week. Take a look at these great features that we released over the past few weeks:

- **Enterprise-Grade Management for Internet Firewall:** The updated [Internet Firewall policy](/v1/docs/managing-the-internet-firewall-policy) makes it easier to manage Internet traffic with these improvements:
  - Multiple admins can seamlessly edit the policy at the same time
  - Save changes in your own private revision and then continue editing later
  - For policies with a large number of rules, the page is faster and more responsive
  - Use the [Cato mutation API](https://api.catonetworks.com/documentation/#mutation-policy.internetFirewall.addRule) to create and configure Internet Firewall rules and settings
- **Full Cloud App Visibility with CASB:** You can use a single rule in the [Application Control policy](/v1/docs/managing-the-application-control-policy) to monitor all activities for cloud apps in your organization. Use the **Any Granular Activity** setting in a rule to generate events for **Any Cloud Application**. For example, you can use these settings to log the full path URL for all cloud apps.

Go to the [Cato Product Roadmap](https://bit.ly/49aFEKU) in the Knowledge Base to follow the status of upcoming features and enhancements.

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - Heuristic Download of executables/scripts using WebDAV (New)
    - Ransomware Allarich (New)
    - Ransomware AttackNew (Enhancement)
    - Ransomware ForceLock (Enhancement)
    - Ransomware GameCrypt (Enhancement)
    - Ransomware LostInfo (Enhancement)
    - Ransomware NetForceZ (Enhancement)
    - Ransomware Pomoch (Enhancement)
    - Ransomware Pomochit (Enhancement)
    - Ransomware Risen (Enhancement)
    - Ransomware ZILLA (Enhancement)
    - Tnaket-CnC Checkin (New)
    - CVE-2017-3066 (New)
    - CVE-2021-26855 (Enhancement)
    - CVE-2022-0666 (New)
    - CVE-2022-1390 (New)
    - CVE-2022-1391 (New)
    - CVE-2022-1574 (New)
    - CVE-2022-1609 (New)
    - CVE-2022-23347 (New)
    - CVE-2022-23854 (New)
    - CVE-2022-24816 (New)
    - CVE-2022-2486 (New)
    - CVE-2022-2486 (New)
    - CVE-2022-24900 (New)
    - CVE-2022-25485 (Enhancement)
    - CVE-2022-25486 (Enhancement)
    - CVE-2022-25497 (New)
    - CVE-2022-26233 (New)
    - CVE-2022-27043 (New)
    - CVE-2022-29298 (New)
    - CVE-2022-31126 (New)
    - CVE-2022-31656 (New)
    - CVE-2022-32409 (New)
    - CVE-2022-33901 (New)
    - CVE-2022-34121 (New)
    - CVE-2022-36642 (New)
    - CVE-2022-37042 (New)
    - CVE-2022-37191 (New)
    - CVE-2022-38296 (New)
    - CVE-2022-38794 (New)
    - CVE-2022-3980 (New)
    - CVE-2022-40734 (New)
    - CVE-2022-41840 (New)
    - CVE-2022-4328 (New)
    - CVE-2022-45699 (New)
    - CVE-2022-47501 (New)
    - CVE-2022-47615 (New)
    - CVE-2023-0126 (New)
    - CVE-2023-1177 (New)
    - CVE-2023-2356 (New)
    - CVE-2023-26069 (Enhancement)
    - CVE-2023-26347 (New)
    - CVE-2023-2648 (New)
    - CVE-2023-29887 (New)
    - CVE-2023-31059 (New)
    - CVE-2023-33440 (New)
    - CVE-2023-33510 (New)
    - CVE-2023-3380 (New)
    - CVE-2023-34259 (New)
    - CVE-2023-35843 (New)
    - CVE-2023-35885 (New)
    - CVE-2023-3712 (Enhancement)
    - CVE-2023-37629 (New)
    - CVE-2023-39026 (New)
    - CVE-2023-39120 (New)
    - CVE-2023-39141 (New)
    - CVE-2023-41599 (New)
    - CVE-2023-42344 (New)
    - CVE-2023-49442 (New)
    - CVE-2023-49897 (Enhancement)
    - CVE-2023-50917 (New)
    - CVE-2023-51449 (New)
    - CVE-2023-6020 (New)
    - CVE-2023-6023 (New)
    - CVE-2023-6634 (New)
    - CVE-2023-6831 (New)
    - CVE-2023-6909 (New)
    - CVE-2024-2044 (New)
    - CVE-2024-38112 (New)
    - CVE-2024-39903 (New)
    - CVE-2024-4879 (New)
    - CVE-2024-5178 (New)
    - CVE-2024-5217 (New)
    - CVE-2024-6188 (New)
    - CVE-2024-6746 (New)
    - CVE-2024-7120 (New)
    - CVE-2024-7340 (New)
- **Detection & Response:**
  - These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
    - **Threat Prevention:**
      - Suspected Qakbot/Emotet traffic (Enhancement)
- **Suspicious Activity Monitoring**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - Teamviewer Remote Session to Low Popularity IP (New)
    - ScreenConnect Lateral Transfer (New)
    - Atera Agent Activity (New)
- **Apps Catalog:**
  - Added over 120 new Cloud applications (you can view the Cloud apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - DSI Cloud (New)
    - OT Protocols - IEC 60870-5-104
    - Anonymizers - 1VPN (New)
    - Anonymizers - Anonymous VPN (Enhancement)
    - Anonymizers - Anonymox Gmbh (New)
    - Anonymizers - Browsec (New)
    - Anonymizers - DotVPN (New)
    - Anonymizers - Free VPN (New)
    - Anonymizers - Hoxx VPN (New)
    - Anonymizers - Ivacy (New)
    - Anonymizers - Planet VPN (New)
    - Anonymizers - Sweet VPN (New)
    - Anonymizers - Telleport (New)
    - Anonymizers - Touchvpn (New)
    - Anonymizers - Troywell VPN (New)
    - Anonymizers - Tuxler (New)
    - Anonymizers - Urban VPN (New)
    - Anonymizers - Veepn (New)
    - Anonymizers - VPN-free.pro (New)
    - Anonymizers - VPNCity (New)
    - Anonymizers - VPNLY (New)
    - Anonymizers - Working VPN (New)
    - Anonymizers - Zenguard Gmbh (New)
- **Application Control (CASB and DLP):**
  - Enhanced granular activities for the following apps:
    - AWS S3 - Upload (New)
    - AWS S3 - Download (New)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - IOT:
      - Payment Terminal
        - Verifone (Enhancement)
      - Printer
      - 
        - Brother (Enhancement)
        - Kyocera (Enhancement)
        - Xerox (Enhancement)
        - Smart TV
        - LG (Enhancement)
      - VoIP
        - Avaya (Enhancement)
        - Cisco (Enhancement)
        - Grandstream Networks (Enhancement)
        - Mitel (Enhancement)
        - Polycom (Enhancement)
        - Ubiquiti (Enhancement)
    - OT, IOT:
      - IP Camera
        - Axis (Enhancement)
      - CCTV
        - IDIS (Enhancement)
    - Mobile:
      - Mobile Phone
        - Redmi (Enhancement)
        - Samsung (Enhancement)
    - Networking:
      - Network Appliance
        - Aruba Networks (Enhancement)
    - PC:
      - Workstation
        - Apple (Enhancement)
        - Asus (Enhancement)

**Note:** Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
