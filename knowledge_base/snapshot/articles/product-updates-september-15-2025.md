---
title: "Product Updates - September 15, 2025"
slug: "product-updates-september-15-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-september-15-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - September 15, 2025

## New Features & Enhancements

- **Introducing Advanced Groups with Full API Support:** Over the next few weeks, we are gradually rolling out [advanced groups](/v1/docs/working-with-cma-advanced-groups-and-groups) that use a new infrastructure for CMA policies:
  - Provides full API support for automation and integration workflows
  - Available for use in Internet and WAN Firewall policies
  - Improved user experience with built-in validation, only compatible advanced groups are available for the rule (such as a **Source** for the WAN Firewall)
  - Supports member types: sites, hosts, subnets, etc. **Note:** Existing groups remain available and fully supported for relevant use cases
- **Important - Microsoft Azure is Changing Default Outbound Access for New Virtual Networks:** After Mar. 31, 2026, [new Azure virtual networks](/v1/docs/microsoft-changing-default-outbound-access-behavior-for-new-virtual-networks) will be configured by default with private subnets, requiring explicit outbound access to reach the Internet or Microsoft services.
  - According to [Microsoft documentation](https://azure.microsoft.com/en-us/updates?id=default-outbound-access-for-vms-in-azure-will-be-retired-transition-to-a-new-method-of-internet-access), existing vSockets with the **None** setting remain supported
  - New vSockets from the Marketplace will default to **Public IP**
  - Cato has updated its [Azure Terraform modules](/v1/docs/using-terraform-with-the-cato-cloud) to align with this change
  - Please review [Microsoft's guidance](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access) to plan for this change
- **File Hash Blocklist Support in Anti-Malware Policy:** You can now block files based on SHA-256 hashes from your own threat intelligence sources by adding them to the [Anti-Malware blocklist](/v1/docs/managing-anti-malware-exceptions), providing stronger protection against known threats.
  - Also supported via API
- **NAT Policy Enforcement Includes All Inbound Traffic:** For consistent policy application across all relevant traffic types, we now enforce the NAT policy on DNS and LAN Monitoring traffic.
  - Previously, this traffic was classified as system traffic and excluded from the policy
  - Gradually rolling out over the next few weeks
- **New IoT/OT Security Integration with Zoom for Enhanced Device Context and Visibility:** To enrich device information, you can now integrate [Zoom metadata](/v1/docs/zoom-configuring-the-device-management-integration) with Cato’s device inventory. A unified view with enriched attributes from both systems is presented on the Home > Device Inventory page.
  - Configure in the Resources > Integrations page, or with the API
  - This integration provides:
    - **Expanded device context:** Incorporating Zoom session and connection metadata into device profiles
    - **Greater accuracy in device attribution**: Helping security teams correlate devices
  - Requires DEM and IoT/OT licenses

## Security Updates

- **App Catalog**
  - ON24, Inc. (Enhancement)
  - Foxit Software (Enhancement)
- **IPS Signatures**
  - IPS Signatures: View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2020-11455 (New)
    - CVE-2020-13886 (New)
    - CVE-2020-15050 (New)
    - CVE-2020-17456 (New)
    - CVE-2020-24285 (New)
    - CVE-2020-26073 (New)
    - CVE-2020-27191 (New)
    - CVE-2020-35736 (New)
    - CVE-2020-8641 (New)
    - CVE-2021-20092 (New)
    - CVE-2021-23241 (New)
    - CVE-2021-24227 (New)
    - CVE-2021-29006 (New)
    - CVE-2021-33544 (New)
    - CVE-2021-35380 (New)
    - CVE-2021-38751 (New)
    - CVE-2021-40651 (New)
    - CVE-2021-41293 (New)
    - CVE-2021-41749 (New)
    - CVE-2021-43421 (New)
    - CVE-2021-43495 (New)
    - CVE-2021-43496 (New)
    - CVE-2021-43831 (New)
    - CVE-2021-45043 (New)
    - CVE-2021-45967 (New)
    - CVE-2021-46381 (New)
    - CVE-2022-24288 (New)
    - CVE-2023-26469 (New)
    - CVE-2023-3722 (New)
    - CVE-2024-20356 (New)
    - CVE-2024-23334 (New)
    - CVE-2024-3673 (New)
    - CVE-2024-38018 (New)
    - CVE-2024-7399 (New)
    - CVE-2024-8752 (New)
    - CVE-2024-8859 (New)
    - CVE-2024-9707 (New)
    - CVE-2025-1097 (New)
    - CVE-2025-1098 (New)
    - CVE-2025-1974 (Enhancement)
    - CVE-2025-24513 (Enhancement)
    - CVE-2025-24514 (New)
    - CVE-2025-34300 (New)
    - CVE-2025-53778 (New)
    - Malware - Oyster (New)
    - Ransomware - 707 (Enhancement)
    - Ransomware - Charon (Enhancement)
    - Ransomware - CyberHazard (Enhancement)
    - Ransomware - GRYPHON (Enhancement)
    - Ransomware - Keversen (New)
    - Ransomware - Matrix (Proton) (Enhancement)
    - Ransomware - RDAT (Enhancement)
    - Ransomware - SolutionWeHave (New)
    - Ransomware - Traders (Enhancement)
    - Web Application Attack - Active Directory Certificate Services (ADCS) ESC1 Attack - Certificate Signing Request (CSR) with Enrollee-Supplied Subject (New)
  - **SAM Signatures**
    - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
      - UPX Packed File Download (New)
  - **OS Detection**
    - OS embedded signature for Cisco Meraki devices (New)
    - OS Linux signature for IO DATA devices (New)
  - **Application Control Policy**
    - Inline tenant control for Zendesk (New)
  - **XOps Indications of Attack**
    - **Anomaly Detection**
      - First Occurrence of Outbound Remote Access Activity from Site (New)
      - Abnormal File Sharing/Cloud Storage App Outbound Activity from Site (New)
      - Unusual SMB Traffic from Site Over the WAN (New)
    - **Threat Prevention**
      - Suspicious Network Activity (MS-PowerShell) (Enhancement)
      - Abnormal HTTP/TLS on Non-Standard Ports in a Site) (Enhancement)
      - Device fingerprint sending via user agent (Enhancement)
      - Suspicious Network Activity (MS-Office) (Enhancement)
  - **Device Inventory**
    - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
      - **IoT**
        - Multifunction Device
          - Canon (Enhancement)
        - Payment Terminal
          - Castles Technology (Enhancement)
          - Verifone (Enhancement)
        - Printer
          - Brother Industries (Enhancement)
          - Epson (Enhancement)
          - HP (Enhancement)
          - Konica Minolta (Enhancement)
          - Kyocera (Enhancement)
          - Lexmark (Enhancement)
          - Xerox (Enhancement)
          - Zebra (Enhancement)
        - Signage Media Player
          - BrightSign (Enhancement)
        - Speaker
          - Algo (Enhancement)
        - Unidentified IoT
          - Grandstream Networks (Enhancement)
          - Synology (Enhancement)
        - Video Conferencing
          - Cisco (Enhancement)
        - VoIP
          - Aastracom (Enhancement)
          - Avaya (Enhancement)
          - Cisco (Enhancement)
          - Digium (Enhancement)
          - Grandstream Networks (Enhancement)
          - Polycom (Enhancement)
          - Snom (Enhancement)
          - Yealink (Enhancement)
      - **PC**
        - Desktop
          - Dell (Enhancement)
          - HP (Enhancement)
          - Lenovo (Enhancement)
        - Laptop
          - Apple (Enhancement)
          - Dell (Enhancement)
          - HP (Enhancement)
          - Lenovo (Enhancement)
          - Microsoft (Enhancement)
          - Toshiba (Enhancement)
          - Vaio (Enhancement)
        - Thin Client
          - Dell (Enhancement)
        - Workstation
          - Apple (Enhancement)
          - Fujitsu (Enhancement)
          - HP (Enhancement)
          - NEC (Enhancement)
          - Panasonic (Enhancement)
      - **Mobile**
        - Mobile Computer
          - Zebra (Enhancement)
        - Mobile Phone
          - Newland (Enhancement)
          - Oppo (Enhancement)
          - Samsung (Enhancement)
          - Vivo (Enhancement)
          - Galaxy Note (Enhancement)
        - Tablet
          - Samsung (Enhancement)
          - **Networking**
            - Network Appliance
              - 3Com (Enhancement)
              - Aruba Networks (Enhancement)
              - Juniper Networks (Enhancement)
              - Ubiquiti (Enhancement)
      - **Server**
        - Media Server
          - Roku (Enhancement)
        - Print Server
          - HP (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
