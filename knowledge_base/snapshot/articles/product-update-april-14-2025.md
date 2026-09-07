---
title: "Product Update - April 14, 2025"
slug: "product-update-april-14-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-april-14-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - April 14, 2025

## New Features & Enhancements

- **EPP Supports Deleting Quarantined Files:** You can delete files quarantined by EPP in the [Quarantine page](/v1/docs/monitoring-and-responding-to-endpoint-protection-threats) for each protected endpoint.
- **Custom Branding for Reports:** We are expanding the branding options to include customizing the look and feel of [Cato reports](/v1/docs/reports).
- **Enhancement for Network Stories in XDR:** We adjusted the method for story creation to eliminate redundant [Network stories](/v1/docs/reviewing-site-operations-stories). For example, if a site with two WAN links goes down, a single Site Down story is generated without separate Link Down stories for each WAN link.
  - Click [here](https://academy.catonetworks.com/enhancing-network-stories-in-xdr) to watch a video recording of this feature

## PoP Announcements

- **Vienna, AT:** A new Cato PoP will shortly become available in Vienna.
- **Charlotte, US:** A new range (199.27.39.0/24) will soon be added to the Charlotte PoP location.
- **London, UK:** A new range (216.252.191.0/24) will soon be added to the London PoP location.
- **Seattle, US:** A new range (199.27.38.0/24) will soon be added to the Seattle PoP location.
- **Sydney, AU:** A new range (202.75.244.0/24) will soon be added to the Sydney PoP location.

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
- **XDR Indications of Attack Signatures:**
  - Anomaly Detection:
    - Kerberos Blocked Events (New)
    - First Occurrence Of WinRM Connection (New)
  - Threat Prevention:
    - Suspicious Communication with Blocklisted Targets (New)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - **IOT**
      - IP Camera
        - Axis (Enhancement)
        - Verkada (Enhancement)
      - Alarm
        - WebWayOne (New)
        - Neospot (New)
        - Zenital (New)
        - Crestron (New)
    - **Mobile**
      - Mobile Phone
        - Oppo (Enhancement)
        - iPhone (Enhancement)
    - **Networking**
      - Access Point
        - Aruba Networks (Enhancement)
      - Network Appliance
        - Aruba Networks (Enhancement)
        - Cisco Meraki (Enhancement)
      - Wireless Controller
        - Barco ClickShare (New)
    - **PC**
      - Desktop
        - Dell (Enhancement)
      - Laptop
        - Dell (Enhancement)
        - HP (Enhancement)
        - Lenovo (Enhancement)
        - Toshiba (Enhancement)
    - Server
      - Print Server
        - HP (Enhancement)
        - Axis (Enhancement)
      - Virtual Machine:
        - VMware Windows (New)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
