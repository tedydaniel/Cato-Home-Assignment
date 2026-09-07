---
title: "Product Update - April 28, 2025"
slug: "product-update-april-28-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-april-28-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - April 28, 2025

## New Features & Enhancements

- **Flexible Text Matching for Event Filters:** The Home > Events page now supports [filtering events](/v1/docs/filtering-data-on-a-page) based on partial or similar values in text fields such as **Domain Name** and **User Name**, even when you don’t know the exact value. Two new operators are available:
  - 
    - **Contains** – Matches values that include the input as a substring (e.g., example.com matches mail.example.com)
    - **Approximate Match** – Matches similar values, even with minor typos or character changes (e.g., **john.doe** matches **jonh.dot**)
    - Click [here](https://academy.catonetworks.com/flexible-text-matching-for-event-filters) to watch a video recording of this feature
- **ILMM Integrated into XDR Ecosystem**: For Intelligent Last Mile Monitoring (ILMM) customers, the service will fully integrate with Cato XDR to provide enhanced control and deeper insights directly in the CMA.
  - 
    - **View Incidents in CMA:** Use the [Stories Workbench](/v1/docs/reviewing-site-operations-stories) to view the status of incidents and review past issues
    - **Granular Reporting:** Configure and schedule reports in the CMA for any recipient, with customizable timeframes to suit your operational needs
    - **Enhanced Alert Customization:** Adjust **Link Quality** SLA alert sensitivity using [Link Health Rule](/v1/docs/working-with-link-health-rules) settings to better align with your network needs
    - **Define Scheduled Maintenance:** Minimize alert noise during planned maintenance windows using the [Mute Stories](/v1/docs/muting-xops-stories) policy
    - **Granularly Define Alert Recipients:** Use the XDR [Response Policy](/v1/docs/creating-the-response-policy-for-xops-stories) to configure recipients to receive alerts for specific incident types, ensuring relevant stakeholders stay informed
    - These enhancements require account-level configuration changes. A dedicated email will be sent to ILMM customers detailing the required changes. See [this article](/v1/docs/upcoming-migration-of-ilmm-service-to-the-cma) for more information
- **Reporting Socket Version Known Limitations and Resolved Issues:** We are now reporting the Known Limitations and Resolved Issues as part of the Socket Release Notes articles starting with [v22](/v1/docs/socket-version-22-0-release-notes) and [v23](/v1/docs/socket-version-23-0-release-notes).
  - 
    - You can also ask the [Knowledge AI Assistant](/v1/docs/what-is-cato-s-ask-ai-agent) in the CMA for information about Socket versions
- **API Announcements:**
  - 
    - **Update to Marker Behavior in eventsFeed:** The [eventsFeed API](https://api.catonetworks.com/documentation/#query-eventsFeed) uses a marker to iteratively pull events. The API reads events from the queue based on the marker specified by the caller and provides the next marker location in the response. Now, if no input marker is specified, the API returns the most recent data.
      - 
        - Previously, when no input marker was specified, the API returned the oldest available marker
        - If you have a dedicated logic to consume the queue to reach the recent events, this logic is no longer required, and the corresponding scripts and automated processes should be updated. For more information, see this [article](/v1/docs/cato-api-potentially-breaking-changes-and-eol)
    - **Reminder - EoL for Fields and Types in eventFieldName:** 8 fields and types in the eventFieldName API will be end-of-life (EoL) as of May 1, 2025. For details, see this [article](/v1/docs/cato-api-potentially-breaking-changes-and-eol)
- **Better Control over DHCP Lease Time:** We changed the minimum [Cato DHCP lease time](/v1/docs/configuring-dhcp-settings) to 1 minute. This provides greater flexibility for scenarios that require temporary access or short-term connectivity, such as guest Wi-Fi networks, IoT connections, and mobile devices.
  - Previously, the minimum DHCP lease time was 30 minutes
- **Join Cato's Product Rewind Session on May 7:** Product Rewind is a fast-paced monthly webinar, and we will break down the most compelling product updates from April 2025. See the latest innovations in action with live demos and get practical insights on how these updates can enhance your experience.
  - Register [here](https://academy.catonetworks.com/product-monthly-rewind/269140) for May 7, 12 pm ET

## PoP Announcements

- **Toronto, CA:** A new range (199.27.36.0/24) is now available for the Toronto PoP location.
- **Dubai, AE:** A new range (202.75.245.0/24) will soon be added to the Dubai PoP location.
- **Lagos, NG:** A new Cato PoP will shortly become available in Lagos.

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2018-19410 (New)
    - CVE-2020-14472 (New)
    - CVE-2021-20124 (New)
    - CVE-2021-35393 (New)
    - CVE-2021-35395 (Enhancement)
    - CVE-2021-42911 (New)
    - CVE-2023-24229 (New)
    - CVE-2024-0200 (New)
    - CVE-2024-13159 (New)
    - CVE-2024-13160 (New)
    - CVE-2024-13161 (New)
    - CVE-2024-3080 (New)
    - CVE-2024-40890 (New)
    - CVE-2025-1316 (New)
    - CVE-2025-2294 (New)
    - CVE-2025-23369 (New)
    - CVE-2025-24045 (New)
    - CVE-2025-24061 (New)
    - CVE-2025-27218 (New)
    - CVE-2025-27636 (New)
    - CVE-2025-29927 (New)
    - CVE-2025-31131 (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget BaseActivationFactory (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget WindowsClaimsIdentity (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget XamlImageInfo (New)
    - Block Medusa Ransomware (gaze.exe) over SMB (New)
    - Ransomware - 888 (Enhancement)
    - Ransomware - Adobe (Enhancement)
    - Ransomware - Anonymous (Xorist) (Enhancement)
    - Ransomware - Anubi (Enhancement)
    - Ransomware - Aptlock (Enhancement)
    - Ransomware - AstraLocker 2.0 (Enhancement)
    - Ransomware - Craxsrat (Enhancement)
    - Ransomware - CrazyHunter (Enhancement)
    - Ransomware - Cyb3r Drag0nz (Enhancement)
    - Ransomware - Danger (GlobeImposter) (Enhancement)
    - Ransomware - Data (Enhancement)
    - Ransomware - Elons (Enhancement)
    - Ransomware - FLMN (Enhancement)
    - Ransomware - FuxSocy ENCRYPTOR (Enhancement)
    - Ransomware - HWABAG (Enhancement)
    - Ransomware - Mamona (Enhancement)
    - Ransomware - Maximsru (Enhancement)
    - Ransomware - Moscovium (Enhancement)
    - Ransomware - Nanocrypt (Enhancement)
    - Ransomware - Netwalker (Enhancement)
    - Ransomware - Nullhexxx (Enhancement)
    - Ransomware - Optimus (Chaos) (Enhancement)
    - Ransomware - PelDox (Enhancement)
    - Ransomware - RALord (Enhancement)
    - Ransomware - SKUNK (Enhancement)
    - Ransomware - Spectra (Enhancement)
    - Ransomware - TheAnonymousGlobal (Enhancement)
    - Ransomware - VanHelsing (Enhancement)
    - Ransomware - Weaxor (Enhancement)
    - Ransomware - Wiki (Enhancement)
    - Ransomware - Worry (WhatsWrongScared) (Enhancement)
    - Ransomware - ZasifrovanoXTT2 (Enhancement)
- **Suspicious Activity Monitoring:**
  - These protections were added to the SAM service:
    - Suspicious Traffic of RDP Over TLS (New)
    - Impacket atexec Execution (New)
- **XDR Indications of Attack Signatures:**
  - Anomaly Detection:
    - First Occurrence of WANBOUND AnyDesk Remote Desktop Connection (New)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - 
      - Docking Station
        - Action Star (Enhancement)
      - Multifunction Device
        - Toshiba (Enhancement)
      - Printer
        - HP (Enhancement)
        - Xerox (Enhancement)
      - VoIP
        - Aastracom (Enhancement)
        - Cisco (Enhancement)
        - Grandstream Networks (Enhancement)
        - Polycom (Enhancement)
      - Smart TV:
        - Sony TV (Enhancement)
        - TCL Smart TV (New)
      - Automobile:
        - Tesla Vehicle (New)
        - Tesla Wall Connector (New)**IOT**
      - IP Camera:
        - Generic IP Camera (Enhancement)
        - Uniview IP camera (New)
    - **Mobile**
      - Mobile Phone
        - Samsung (Enhancement)
        - Zebra (Enhancement)
        - iOS (Enhancement)
      - Smart Watch
        - Pixel Watch (Enhancement)
        - Apple Watch (Enhancement)
    - **Networking**
      - Network Appliance
        - Aruba Networks (Enhancement)
        - Juniper Networks (Enhancement)
        - Generic Switch (Enhancement)
        - Extreme Networks (New)
    - **OT**
      - Area Scan Camera
        - Teledyne FLIR (Enhancement)
    - **PC**
      - 
      - Laptop
        - Dell (Enhancement)
        - HP (Enhancement)
        - Lenovo (Enhancement)
      - Workstation
        - Apple (Enhancement)
        - Panasonic (Enhancement)
        - HP
        - Generic
    - **Server**
      - Virtual Machine:
        - VMware
    - **Vendors**
      - BrightSign
      - TCL
      - Honeywell SPS
      - Hand Held
      - AUDIO CODES
      - Observint
      - Night Owl
      - Qnap
      - SecureCom Wireless

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
