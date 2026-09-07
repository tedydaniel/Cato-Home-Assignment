---
title: "Product Update - September 2, 2024"
slug: "product-update-september-2-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-september-2-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - September 2, 2024

- **XDR Stories for Entra ID Protection Sign-In Anomalies:** To let analysts include data from risky sign-ins within the broader context of XDR investigations, we added an integration that creates [XDR stories from Entra ID Protection alerts](/v1/docs/microsoft-entra-id-configuring-the-xops-integration).
  - Available for XDR Core, XDR Pro, and MXDR customers using Microsoft Entra ID Protection
  - Cato’s [Microsoft Entra ID Protection connector](/v1/docs/configuring-the-microsoft-entra-id-protection-connector-for-sign-in-anomaly-data) is available free of charge
  - Click [here](https://academy.catonetworks.com/xdr-entra-id-stories-1) to watch a video recording of this feature
- **Visibility for Default TLS Inspection Bypass Rules:** Cato manages default TLS Inspection rules that bypass specific apps, operating systems, and clients that may cause issues. Admins can now view the settings for these rules for improved planning and decision-making for the [TLS Inspection policy](/v1/docs/configuring-tls-inspection-policy-for-the-account).
  - The default rules can’t be edited
- **Improved Management of SaaS Security API Connectors:** To ensure continuous monitoring of data, we have made these enhancements to [SaaS Security API](/v1/docs/what-is-the-data-protection-api):
  - **Events for** **Changes in Connector Status:** When the connector status changes, an event is generated in near real-time with specific connectivity details. For example, an event is generated when the OneDrive connector changes from **Connected** to **Connectivity Error**. The event can be viewed on the [Events](/v1/docs/analyzing-events-in-your-network) page, and the connector status information is also available on the [Assets > Integrations](/v1/docs/using-the-integrations-page) page
  - **Salesforce and ServiceNow - Refresh Tokens:** To proactively keep the [Salesforce](/v1/docs/salesforce-configuring-the-data-protection-api-connector) and [ServiceNow](/v1/docs/servicenow-configuring-the-data-protection-api-connector) tokens valid, re-consent to the vendor so the SaaS Security API can continuously monitor the data.
  - **ServiceNow - Token Expiration Warning:** 14 days before the ServiceNow connector authentication token expires, a warning is displayed on the **Installed SaaS Applications** page.
- **Change to CMA Admin Preferences:** As part of an infrastructure update, the Cato Management Application (CMA) no longer supports the [admin preferences](/v1/docs/setting-the-cma-user-interface-preferences) for changing the navigation layout.

Go to the [Cato Product Roadmap](https://bit.ly/49aFEKU) in the Knowledge Base to follow the status of upcoming features and enhancements.

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - Ransomware Pwn3d (New)
    - Ransomware Insom (Enhancement)
    - Ransomware Devil (Enhancement)
    - Ransomware Like (Enhancement)
    - Ransomware Datablack (Enhancement)
    - Ransomware RDanger (Enhancement)
    - Ransomware Allarich (Enhancement)
    - Ransomware AttackNew (Enhancement)
    - Malware Cobalt Strike (Enhancement)
    - CVE-2022-27002 (New)
    - CVE-2022-30023 (New)
    - CVE-2024-1800 (New)
    - CVE-2024-37085 (New)
    - CVE-2024-6387 (New)
    - Heuristic - DNS Tunneling | Iodine (New)
- **Detection & Response:**
  - These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
    - **Threat Prevention:**
      - Suspected Qakbot/Emotet traffic (Enhancement)
- **Suspicious Activity Monitoring**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - Ligolo Command and Control Communication (New)
- **XDR Indications Of Attack Signatures:**
  - **Threat Prevention:**
    - Domain Generation Algorithm (DGA) Communication over DNS (New)
  - **Threat Hunting:**
    - Communication To Suspicious IP (New)
    - Suspicious Network Activity (Domains) (New)
    - Lateral transfer of possibly suspicious tool over SMB (Enhancement)
- **Apps Catalog:**
  - More than 130 new Cloud Apps (see Apps Catalog)
    - IPFS bootstrap (New)
    - IPFS Web Gateway (New)
    - IPFS (Enhancement)
    - Autodesk (Enhancement)
    - Arlo (Enhancement)
    - Target (Enhancement)
    - ANZ (Enhancement)
    - Lazada (Enhancement)
    - Leagueoflegends (Enhancement)
    - Netflix (Enhancement)
- **Application Control (CASB and DLP):**
  - Enhanced granular activities for the following apps:
    - Microsoft Teams – Send Message(New)
    - Egnyte – Login (New)
    - Egnyte – Upload (New)
    - Egnyte – Download (New)
- **TLS Inspection**:
  - ChatGPT on macOS and iOS – Bypass by default (New)
  - Reddit on iOS – Bypass by default (New)
  - Dropbox - coverage update (Enhancement)
  - WhatsApp - coverage update (Enhancement)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - IOT:
      - Payment Terminal
        - Verifone (Enhancement)
        - Castles Technology (Enhancement)
      - Printer
        - Canon (Enhancement)
        - Kyocera (Enhancement)
        - Xerox (Enhancement)
        - Zebra (Enhancement)
        - Smart TV
        - LG (Enhancement)
      - VoIP
        - Ascom (Enhancement)
        - Cisco (Enhancement)
        - Grandstream Networks (Enhancement)
        - Polycom (Enhancement)
        - Snom Technology (Enhancement)
      - Unidentified IoT
        - TP (Enhancement)
    - OT, IOT:
      - IP Camera
        - Avigilon (Enhancement)
    - Mobile:
      - Mobile Phone
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
