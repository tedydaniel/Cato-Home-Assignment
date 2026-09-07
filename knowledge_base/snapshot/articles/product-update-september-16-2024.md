---
title: "Product Update - September 16, 2024"
slug: "product-update-september-16-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-september-16-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - September 16, 2024

- **Enhanced Admin Experience for Managing the WAN Firewall at Scale:** Over the next few weeks, we are gradually rolling out a new [WAN Firewall policy](/v1/docs/what-is-the-cato-wan-firewall) that introduces several improvements, including:
  - API support for managing the policy
  - Ability to [modify the policy](/v1/docs/working-with-policy-revisions) in parallel by multiple admins
  - Faster and more responsive page for policies with many rules
  - Click [here](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcatonetworks.us16.list-manage.com%2Ftrack%2Fclick%3Fu%3D75bb2b7bafe7526c787475fd2%26id%3D9f4947b8a6%26e%3Da04538e456&amp;data=05%7C02%7Cyaron.libman%40catonetworks.com%7C1a6ef065d5d74334165c08dcd59037b4%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638620062597524819%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&amp;sdata=au5%2FMvKgrRZ0BDj7Sy710i1oaSo0hV%2BIhcheXxurSBo%3D&amp;reserved=0) to watch a video recording of this feature
- **New PoP Sites for Cloud Interconnect:** Two new PoPs for [Cloud Interconnect](/v1/docs/getting-started-with-cloud-interconnect-sites) in Singapore and Tokyo are available, expanding connectivity and access in the Far East region.
- **CMA Enhancements:**
  - **Improved Management of Signing Certificates:** You can now disable and re-enable a [signing certificate](/v1/docs/legacy-device-authentication) without removing it from your account.
  - **Export Known Hosts and Routing Table to CSV:** To assist with monitoring and troubleshooting, you can export the data in the Known Hosts and Routing Table pages to CSV files to integrate with existing workflows.
- **Reminder - Upcoming Automatic Upgrade of Local Routing Rules to LAN Firewall:** The LAN Firewall provides security and management improvements for Socket sites requiring local traffic segmentation routing. Starting on October 20, 2024, Cato will automatically upgrade all sites still using Local Routing Rules to the LAN Firewall policy. You can [manually upgrade](/v1/docs/upgrading-the-local-routing-policy-to-the-lan-firewall) to the LAN Firewall before October 20, and the upgrade process doesn’t cause any downtime.

Go to the [Cato Product Roadmap](https://bit.ly/49aFEKU) in the Knowledge Base to follow the status of upcoming features and enhancements.

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2021-21892 (New)
    - CVE-2022-40005 (Enhancement)
    - CVE-2023-25280 (Enhancement)
    - CVE-2023-27240 (New)
    - CVE-2024-29272 (New)
    - CVE-2024-36401 (New)
    - CVE-2024-36991 (New)
    - CVE-2024-38856 (Enhancement)
    - CVE-2024-45241 (New)
    - CVE-2024-6911 (New)
    - CVE-2024-7029 (New)
    - CVE-2024-7954 (New)
    - Ransomware Colony (New)
    - Ransomware Datablack (Enhancement)
    - Ransomware Devil (Enhancement)
    - Ransomware ELPACO-team (Enhancement)
    - Ransomware Insom (Enhancement)
    - Ransomware Like (Enhancement)
    - Ransomware MoneyIsTime (Enhancement)
    - Ransomware PURGAT0RY (Enhancement)
    - Ransomware Pwn3d (Enhancement)
    - Ransomware RDanger (Enhancement)
    - Ransomware Stop/Djvu (Enhancement)
    - EnGenius EnShare Remote Code Execution (New)
    - MediaTek WiMAX Remote Code Execution (New)
- **Suspicious Activity Monitoring**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - PsExec To Multiple Servers (New)
    - ScreenConnect Remote Connection (New)
- **Apps Catalog:**
  - 
    - More than 90 new Cloud Apps (see Apps Catalog)
      - Successfactors )Enhancement)
- **TLS Inspection**:
  - Added New Applications to default bypass:
    - Cursor AI (New)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - IOT:
      - Payment Terminal
      - 
        - Castles Technology (Enhancement)
      - Printer
      - 
        - Kyocera (Enhancement)
      - VoIP
      - 
        - Ascom (Enhancement)
        - Cisco (Enhancement)
        - Grandstream Networks (Enhancement)
        - Polycom (Enhancement)
        - Mitel (Enhancement)
        - Snom Technology (Enhancement)
    - OT, IOT:
      - IP Camera
      - 
        - Avigilon (Enhancement)
      - Power Device
        - Eaton (Enhancement)
    - Mobile:
      - Mobile Phone
      - 
        - Oppo (Enhancement)
    - Networking:
      - Network Appliance
        - Aruba Networks (Enhancement)
        - Buffalo (Enhancement)
        - Lancom Systems (Enhancement)
    - PC:
      - Workstation
        - Apple (Enhancement)
        - MSI (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
