---
title: "Product Update - July 22, 2024"
slug: "product-update-july-22-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-july-22-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - July 22, 2024

## New Features & Enhancements

- **Streamlined IPsec IKEv2 Sites Deployment via the API**: Our new configuration API enhances managing IPsec IKEv2 sites, enabling you to create, update, and delete IPsec IKEv2 sites programmatically.
  - The API supports the following calls:
    - addIpsecIkev2Site
    - updateIpsecIkeV2SiteGeneralDetails
    - updateIpsecIkeV2SiteTunnels
    - removeSite
    - entityLookup for allocated IPs
  - For more information, see our [API documentation](https://api.catonetworks.com/documentation/) and [sample scripts](https://support.catonetworks.com/hc/en-us/articles/8130916998429-Configuration-API-Scripts)
- **Simplified Process for Onboarding Remote Users**: Following the announcement on [July 1, 2024](/v1/docs/product-update-july-1-2024), Users configured to authenticate with username & password or MFA, can set their password (and MFA) during the [sign in process](/v1/docs/signing-in-to-the-cato-client) in the Cato Client.
  - This replaces users setting their password (and MFA) from an automatic activation email sent when a user is created. Admins can still enable a welcome email if required.
  - No impact to users that authenticate with SSO, or existing users that authenticate with username & password, or MFA.
- **Customize the Number of User Group Changes per LDAP Sync:** If an LDAP sync changes group membership of 1500 or more users, Microsoft on-premise Active Directory may remove the users from the group. To prevent this, you can customize the [maximum number of users](/v1/docs/syncing-users-with-ldap) that can change user group membership in a single sync.
- **New Explorer Simplifies Using the Cato API:** We added an API Explorer to the [GraphQL API Playground](https://api.catonetworks.com/api/v1/graphql2). The Explorer simplifies building GraphQL queries and mutations with an intuitive point-and-click interface that automatically adds fields and parameters to the playground.
  - Open the Explorer from the new button on the navigation panel
  - For more about the GraphQL Playground see [this article](/v1/docs/connecting-to-the-cato-api-from-the-graphql-playground)
- **Upcoming Automatic Upgrade of Local Routing Rules to LAN Firewall:** Starting on October 20, Cato will automatically upgrade all sites that are still using the Local Routing page to the LAN Firewall policy. The LAN Firewall provides security and management improvements for sites requiring local traffic segmentation routing.
  - You have the option to [manually upgrade](/v1/docs/upgrading-the-local-routing-policy-to-the-lan-firewall) to the LAN Firewall before October 20. The upgrade process does not cause any downtime
  - The upgrade is for all sites using Socket v18 and higher. There is no impact on Socket sites with earlier versions.

Go to the [Cato Product Roadmap](https://bit.ly/49aFEKU) in the Knowledge Base to follow the status of upcoming features and enhancements.

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - Cobalt Strike-Beacon Activity (Enhancement)
    - Private Loader CNC Activity (New)
    - Ransomware 2000USD (Enhancement)
    - Ransomware Anonymous Arabs (Enhancement)
    - Ransomware Cyb3r Bytes (Enhancement)
    - Ransomware DataDestroyer (Enhancement)
    - Ransomware DeathGrip (Enhancement)
    - Ransomware Eject (Enhancement)
    - Ransomware LIZARD (Enhancement)
    - Ransomware Ncov (Enhancement)
    - Ransomware Senanam (Enhancement)
    - Ransomware Sorcery (Enhancement)
    - Ransomware Stop/Djvu (Enhancement)
    - Ransomware StormCry (Stormous) (Enhancement)
    - Scanners Escalation | Nmap (New)
    - CVE-2020-26948 (New)
    - CVE-2020-5792 (New)
    - CVE-2021-1385 (New)
    - CVE-2021-35250 (New)
    - CVE-2022-45269 (New)
    - CVE-2023-34992 (Enhancement)
    - CVE-2023-36255 (New)
    - CVE-2023-4220 (New)
    - CVE-2024-21644 (New)
    - CVE-2024-23692 (New)
    - CVE-2024-26331 (New)
    - CVE-2024-27130 (New)
    - CVE-2024-28995 (Enhancement)
    - CVE-2024-30080 (New)
    - CVE-2024-3410 (New)
    - CVE-2024-5084 (New)
    - CVE-2024-3596 (New)
    - Inbound SSH Brute Force (Enhancement)
- **Detection & Response:**
  - These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
    - **Threat Hunting:**
      - Blocked Download Attempt (New)
    - **Threat Prevention:**
      - Block download of .hta files from low reputation (New)
      - Suspicious Network Activity (URLs) (Enhancement)
- **Suspicious Activity Monitoring**
  - These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
    - SplashTop Download (Enhancement)
- **Apps Catalog:**
  - Added over 130 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - Scaleway (Enhancement)
    - Azure Windows Virtual Desktop (Enhancement)
- **Application Control (CASB and DLP):**
  - Enhanced granular activities for the following apps:
    - Google Translate - upload (New)
    - Webex - Download (Enhancement)
    - Citrix Sharefile – Login Third Party (New)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - IOT:
      - Payment Terminal
        - Castles Technology (Enhancement)
        - Verifone (Enhancement)
      - Printer
        - Brother (Enhancement)
        - Ricoh (Enhancement)
        - Zebra (Enhancement)
      - Smart TV
        - LG (Enhancement)
      - VoIP
        - Algo (Enhancement) Avaya (Enhancement)
        - Cisco (Enhancement)
        - Grandstream Networks (Enhancement)
        - Polycom (Enhancement)
        - Snom Technology (Enhancement)
        - Ubiquiti (Enhancement)
    - PC:
      - Thin Client
        - Dell (Enhancement)
      - Workstation
        - Apple (Enhancement)
    - OT, IOT:
      - IP Camera
        - Axis (Enhancement)
        - Hikvision (Enhancement)
    - NETWORKING:
      - Network Appliance
        - Synology (Enhancement)
      - Access Point
        - Aruba Networks (Enhancement)
    - MOBILE:
      - Mobile Phone
        - LGE (Enhancement)
        - Oppo (Enhancement)
        - Realme (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
