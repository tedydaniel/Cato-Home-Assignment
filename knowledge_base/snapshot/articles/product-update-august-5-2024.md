---
title: "Product Update - August 5, 2024"
slug: "product-update-august-5-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-august-5-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - August 5, 2024

- **Enriched Event Data Available via API and Event Integrations:** We are adding more contextual data to existing events that you consume via API or a [direct feed to cloud storage](/v1/docs/event-integration) (AWS or Azure).
  - The change is backward compatible and does not require code or configuration changes when using events() and eventsFeed() APIs and integrations.
  - Multiple events contain data on fields that were previously not populated. For example, a security event may contain network and identity information such as the Host MAC Address and the User ID.
  - The data available via events API and Event Integration is now fully aligned with the data available on the Events page.
- **New Device Posture Checks for Running Processes, Registry Keys, and Property Lists:** To increase security, you can now include checks for running processes, registry keys (on Windows devices), and property lists (on macOS devices). These checks can be included within your [Device Posture Profiles](/v1/docs/creating-device-posture-profiles-and-device-checks) and added to Client Connectivity and Security policies.
  - Supported on Windows Client v5.11 and macOS Client v5.7
- **Detect and Enforce Rules for OT Devices:** To help secure networks that include Operational Technology (OT) industrial systems, we added a number of common OT protocols as Services that can be configured in [WAN](/v1/docs/managing-the-wan-firewall-policy) and [Internet](/v1/docs/managing-the-internet-firewall-policy) firewall rules. For example, create a rule that monitors traffic that uses these protocols to identify OT devices on the network. Then add rules to control the OT device traffic.
  - Supported protocols include: GE SRTP, HART IP, DNP3, Modbus, OPC UA, BACnet, CIP
- **New API for Socket Inventory Data:** The [Administration > Socket Inventory](/v1/docs/using-the-socket-assignment-page) page shows information and data about all the Sockets ordered for and connected to your account.
  - You can use the new Beta accountSocketInventory query to ingest this data.
  - For more about Beta API queries, see this [article](/v1/docs/what-is-the-cato-api)
- **SaaS Security API Supports Quarantine for SharePoint Files:** You can now define the **Quarantine** action in [Data Protection and Threat Protection](/v1/docs/microsoft-sharepoint-configuring-the-data-protection-api-connector) rules to remediate potential security breaches in your organization's SharePoint tenant.
- **New EPP Agent v1.1**.**6:** From August 4, 2024, we are starting to roll out Endpoint Protection (EPP) Agent version 1.1.6 which includes this enhancement:
  - File Paths added to the [Allow List](/v1/docs/configuring-endpoint-protection) are now excluded from Behavioral Analysis detections as well as Anti-Malware detections
- **Android Client v5.0.4.119**: Android Client version 5.0.3.117 was uploaded to the Google Play Store on August 4, 2024. This version includes bug fixes and stability improvements.
- **New Training Courses in Cato Academy:** We added these new courses to the [Academy](https://academy.catonetworks.com/):
  - [Managing Socket Sites](https://academy.catonetworks.com/path/getting-started-with-cato-network): Learn about the different Socket models, configuration, and basic management of Socket sites
  - [Getting started with Zero Trust Network Access](https://academy.catonetworks.com/identity-fundamentals): Provides an overview of Zero Trust Network Access with examples and a common configuration flow

Go to the [Cato Product Roadmap](https://bit.ly/49aFEKU) in the Knowledge Base to follow the status of upcoming features and enhancements.

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - BadSpace CnC Activity (New)
    - Horabot CnC Host Exfiltration (New)
    - Malware Vidar Stealer (New)
    - Ransomware Cyb3r Bytes (Enhancement)
    - Ransomware DeathGrip (Enhancement)
    - Ransomware Eject (Enhancement)
    - Ransomware ForceLock (Enhancement)
    - Ransomware GameCrypt (Enhancement)
    - Ransomware LostInfo (Enhancement)
    - Ransomware Ncov (Enhancement)
    - Ransomware NetForceZ (Enhancement)
    - Ransomware Pomochit (Enhancement)
    - Ransomware Stop/Djvu (Enhancement)
    - Ransomware StormCry(Stormous) (Enhancement)
    - Ransomware Ursq (Enhancement)
    - Ransomware ZILLA (Enhancement)
    - CVE-2024-36104 (New)
    - CVE-2024-0769 (New)
    - CVE-2024-29972 (New)
    - CVE-2020-15922 (New)
    - CVE-2023-36457 (Enhancement)
    - CVE-2020-26879 (New)
- **Detection & Response:**
  - These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
    - **Threat Hunting:**
      - Suspicious JavaScript File Download (Enhancement)
      - Phishing Detection (Enhancement)
      - Suspicious Network Activity (Enhancement)
- **Suspicious Activity Monitoring**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - SplashTop Lateral Transfer (New)
    - Atera Agent Ingress Tool Transfer (New)
- **Apps Catalog:**
  - Added over 130 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - Azure Scc Public Cloud Service (Enhancement)
    - Azure Service Fabric (Enhancement)
    - Azure SQL (Enhancement)
    - Azure SQL Management (Enhancement)
    - Azure Storage (Enhancement)
    - Azure Traffic Manager (Enhancement)
    - Azure Update Delivery (Enhancement)
    - Azure Web Pubsub (Enhancement)
    - Azure Windows Admin Center (Enhancement)
    - NAVER MYBOX - (New)
    - Open VPN protocol - (Enhancement)
    - Private Internet Access VPN - (Enhancement)
    - Rakurakumeisai (Enhancement)
    - Soti - (New)
    - Splashtop (Enhancement)
    - UKG - (New)
    - Yoursix - (New)
    - OT Protocol - BACNet - (New)
    - OT Protocol - Common Industrial Protocol (CIP) - (New)
    - OT Protocol - DNP3 - (New)
    - OT Protocol - GE SRTP - (New)
    - OT Protocol - HART IP - (New)
    - OT Protocol - Modbus - (New)
    - OT Protocol - OPC UA - (New)
- **Application Control (CASB and DLP):**
  - Enhanced granular activities for the following app:
    - Microsoft Copilot (BingAI) - Search (Enhancement)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - IOT:
      - Payment Terminal
        - Castles Technology (Enhancement)
      - Printer
        - Brother (Enhancement)
        - Canon (Enhancement)
        - Zebra (Enhancement)
      - Smart Display
        - Kyocera (Enhancement)
      - VoIP
        - Cisco (Enhancement)
        - Grandstream Networks (Enhancement)
        - Mitel (Enhancement)
        - Polycom (Enhancement)
    - OT, IOT:
      - IP Camera
        - Axis (Enhancement)
    - Mobile:
      - Mobile Phone
        - Realme (Enhancement)
        - Samsung (Enhancement)
- **Client Classification:**
  - Scanner RecordedFuture ASI (New)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
