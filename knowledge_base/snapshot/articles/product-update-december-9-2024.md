---
title: "Product Update - December 9, 2024"
slug: "product-update-december-9-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-december-9-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - December 9, 2024

## New Features a[Device Dashboard](/v1/docs/using-the-device-dashboard)nd Enhhancements

- **Introducing an Innovative IoT/OT Security Service Providing Visibility and Control of Assets:** The new service includes these features and capabilities:
  - AI-powered device discovery and classification - The new [Device Inventory](/v1/docs/using-the-device-inventory-page) and [Device Dashboard](https://support.catonetworks.com/hc/en-us/articles/23323277760541-Using-the-Device-Dashboard-EA) pages seamlessly provide visibility for all IT, IoT, and OT devices on the network with detailed attributes
  - Data enrichment - Extending the single context with multi-level asset classification that enriches events with properties such as manufacturer, function, type, and more
  - Policy enforcement using dynamic device attributes - Solving complex contextual access control and segmentation challenges with AI classification-based [device conditions](/v1/docs/adding-device-conditions-to-firewall-rules) in Internet and WAN firewall policies
  - Device-aware Threat Prevention for contextual security - Tailored security protections for various device types and manufacturers
  - The free-trial Device Inventory beta page is no longer available, please contact your Cato representative for additional information

- **Import Custom IoC Lists:** You can now add custom IoC lists as [**Container** objects](/v1/docs/integrating-custom-ioc-lists-with-containers) (Assets > Categories) for the threat intelligence feeds in your Cato account to meet specific requirements for the organization’s industry or location. For example, home-brewed IoC lists or threat feeds provided by third parties. Configure the IoC lists directly in the Cato Management Application or through automated API processes, and then include the lists in Internet Firewall rules. Supported IoC types include:
  - FQDNs
  - IP addresses
  - IP ranges
- **Closed XDR Security Stories** **Automatically Reopen Based on New Findings:** When the XDR Security engines detect new traffic that matches a closed story, the story automatically reopens and is assigned the new status **Reopened**. This lets admins and analysts know that the story may require further review.
- **New Labels for EA and Rollout Phases for APIs:** We are starting to mark new Cato APIs in the [API Reference portal](https://api.catonetworks.com/documentation/#introduction) with these labels:
  - EA - APIs that are only available to customers who join Cato's EA program Please contact us at [ea@catonetworks.com](http://mailto:ea@catonetworks.com/) if you wish to join the relevant EA
  - Rollout - APIs that are being gradually rolled out to all accounts over a period of a few weeks

## PoP Announcements

- **Paris, France:** A new range (216.252.179.0/24) is now available for the Paris PoP location.
- **New PoP Ranges Coming Soon**:
  - **Frankfurt, Germany**: A new range (216.252.180.0/24) will soon be added
  - **New York, United States**: A new range (216.205.126.0/24) will soon be added
  - **Tokyo, Japan:** A new range (150.195.222.0/24) will soon be added
- **New Localized IP Ranges:** New localized IP ranges will soon be available for:
  - Bahamas (serviced through the Miami PoP location) - 216.194.96.0/28
  - Uruguay (serviced through the Sao Palo PoP location) - 216.205.124.0/27. This will replace the current localized IP range serviced through Miami

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - Belkin Play Max Remote Code Execution (New)
    - JVC/Vanderbilt/Honeywell IP Camera Directory Traversal (New)
    - Movistar ADSL Router Directory Traversal (New)
    - Netgear JNR1010 Directory Traversal (New)
    - P2P Wificam Remote Code Execution (New)
    - CnC - Diamotrix Clipper (New)
    - Technicolor DWG-855 Authentication Bypass (New)
    - Technicolor DWG-855 Authentication Bypass (New)
    - CVE-2017-11519 (New)
    - CVE-2017-17215 (New)
    - CVE-2017-18372 (New)
    - CVE-2017-18369 (New)
    - CVE-2018-6000 (New)
    - CVE-2018-9995 (New)
    - CVE-2018-10106 (New)
    - CVE-2021-4446 (New)
    - CVE-2022-21445 (New)
    - CVE-2023-29827 (New)
    - CVE-2024-0012 (Enhancement)
    - CVE-2024-29847 (Enhancement)
    - CVE-2024-36527 (New)
    - CVE-2024-38148 (New)
    - CVE-2024-39713 (New)
    - CVE-2024-41992 (New)
    - CVE-2024-45216 (New)
    - CVE-2024-45488 (New)
    - CVE-2024-5910 (Enhancement)
    - CVE-2024-6386 (New)
    - CVE-2024-7928 (New)
    - CVE-2024-8190 (Enhancement)
    - CVE-2024-8956 (New)
    - CVE-2024-8957 (New)
    - CVE-2024-9264 (Enhancement)
    - CVE-2024-9474 (New)
- **Suspicious Activity Monitoring:**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - SplashTop Remote Connection (New)
    - Zoho Assist Remote Connection (New)
    - Impacket Official Release Download (New)
    - Impacket 3rd Party Download (New)
- **Apps Catalog**
  - More than 120 new Cloud Apps (see Apps Catalog):
    - SageHR (New)Sage HR (New)
    - HiQzen (New)
    - Datto )Enhancement)
- **Application Control (CASB and DLP):**
  - Slack – Upload (Enhancement)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - Networking
      - Network Appliance
        - Juniper Networks (Enhancement)
        - Lancom Systems (Enhancement)
    - IOT
      - Printer
        - Zebra (Enhancement)
      - VoIP
        - Mitel (Enhancement)
        - Snom Technology (Enhancement)
      - IoMT
        - Ascom (Enhancement)
    - PC
      - Thin Client
        - PCoIP Endpoint Device (Enhancement)
      - Workstation
        - Apple (Enhancement)
    - Mobile
      - Mobile Phone
        - Samsung (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
