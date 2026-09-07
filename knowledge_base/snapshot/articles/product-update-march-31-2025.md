---
title: "Product Update - March 31, 2025"
slug: "product-update-march-31-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-march-31-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - March 31, 2025

## New Features & Enhancements

- **Cato Browser Extension:** You can now use the [Cato Browser Extension](/v1/docs/configuring-the-cato-browser-extension) to let authorized users access sensitive SaaS resources without installing the Cato Client, for example, for unmanaged devices. The Client Connectivity Policy lets you define who is allowed to use the Browser Extension, which ensures that adaptive access conditions are met.
  - Available for Chrome browsers v88 and later, for browsers that support Extensions
  - Supports SSO authentication with your IdP
  - Requires that a TLS certificate is installed on the device
  - Available in Chrome Web Store starting March 31, 2025

- **Improved Security and Visibility for GenAI Usage:** We are releasing new features and functionality to mitigate the security risks of using [GenAI apps](/v1/docs/securing-ai-app-traffic). This increases visibility into shadow AI apps and provides access control, and tailored data protection. The new capabilities are:
  - **GenAI Protection Dashboard:** Provides [insights](/v1/docs/using-the-genai-apps-dashboard) and highlights risks related to GenAI app usage
  - **Customized Application Control Categories and Activities:** Control how GenAI apps are used with new AI categories and granular activities in the [Application Control](/v1/docs/managing-the-application-control-policy) policy
  - **App Catalog Updates**: A significant increase in the number of GenAI apps in the [App Catalog](/v1/docs/using-the-app-catalog) so you can learn more about an app and decide how to use the app in your organization
  - **GenAI Categories**: New system [categories](/v1/docs/working-with-categories) for GenAI apps that you can use to customize the Network Rules, WAN firewall, and Internet firewall policies
  - Click [here](https://academy.catonetworks.com/cato-genai-security) to watch a video recording of this feature

- **Extending UZTNA with User Risk-Based Adaptive Access:** The [User Risk Score](/v1/docs/understanding-the-user-risk-level) lets you identify users that present a potential security risk, and limit their access to sensitive resources. The risk score is based on an analysis of various indicators and security signals.
  - You can configure Internet and WAN firewall policies to limit access based on a user’s risk score
  - Applies to all users, whether connecting behind a site or remotely
  - Click [here](https://academy.catonetworks.com/user-risk-score) to watch a video recording of this feature

- **Upcoming Automatic Migration of Site LAN Firewall to Account-Level Policy:** We recently released the [Socket Next Gen LAN Firewall](/v1/docs/what-is-the-socket-next-gen-lan-firewall) that provides account-level configurations and Layer 7 enforcement. Starting July 1, 2025, we will migrate existing site-level LAN firewall rules to the account-level policy.
  - Each site-level rule will automatically be configured in the policy as a Next Gen Network rule to specify the routing, and a Next Gen Firewall rule to allow or block the traffic
  - The rules for each site will be added as a separate section in the rulebase
  - The migration is a seamless, automatic process and no service disruption is expected
  - In the coming weeks, we will announce an EA program for on-demand migration

- **App Activities via API for ChatGPT and Google Apps:** Extend your [CASB App Control](/v1/docs/what-is-application-control-via-api-with-app-activities) functionality by connecting your corporate apps to Cato. This lets you understand who is accessing them and identify suspicious activities or trends even when users are not connected to the Cato Cloud. For example, with Google Drive APIs, you can identify large content delete actions performed by the same user.
  - These are the new supported apps available from the Resources > Integrations Catalog, under **App Activities**:
    - [ChatGPT](/v1/docs/chatgpt-configuring-the-app-activities-integration)
    - [Google Drive](/v1/docs/google-drive-and-workspace-configuring-the-app-activities-integration)
    - [Google Workspace](/v1/docs/google-drive-and-workspace-configuring-the-app-activities-integration)
  - Requires a CASB license

- **New AI-Driven WAN Firewall Analysis and Insights:** We’re introducing an AI-driven enhancement to the [WAN Firewall policy](/v1/docs/what-is-the-cato-wan-firewall) that provides admins with actionable insights to optimize their firewall configurations, improve security posture, and ensure compliance with best practices. The Autonomous Firewall AI engine automatically analyzes your WAN Firewall rulebase and detects issues. For example, rules that can be discarded or modified such as:
  - **User segmentation rules:** Indicate users that can be removed from a rule
  - **Temporary rules:** Rules created to function temporarily while a permanent solution is deployed
  - **Rules that are expired or soon to expire:** Rules created to address a specific need with a cutoff date
  - **Test rules:** Rules explicitly created for validating, debugging, or experimenting
  - Click [here](https://academy.catonetworks.com/autonomous-policy-wan-firewall) to watch a video recording of this feature

- **New Report for Best Practices:** Introducing a report that makes it easy to analyze and share the results of [CMA Best Practices checks](/v1/docs/generating-a-posture-or-posture-compliance-report) for your account. You can generate it on demand or schedule it to run automatically from the Home > Reports page.
  - Click [here](https://academy.catonetworks.com/best-practices-report) to watch a video recording of this feature

- **Support for KeyCloak SSO for CMA Admins:** We added [KeyCloak as an SSO provider](/v1/docs/configuring-keycloak-sso) for authenticating CMA admins.

- **Custom Branding Options for RBI:** In an isolated [RBI session](/v1/docs/configuring-the-rbi-service-for-browsing-sessions), a ribbon is displayed to the user. To meet your branding requirements, you can customize the design by changing the background color, text, and text color.

- **EPP Agent - Trigger Action on Multiple Endpoints:** You can now select multiple endpoints and trigger a remote action on all of them at once. For example, you can perform a full system scan for all selected endpoints.
  - Support for each specific action depends on the EPP Agent version
  - Click [here](https://academy.catonetworks.com/epp-actions-triggering-an-action-for-multiple-endpoints) to watch a video recording of this feature

- **Moving Recipients for CMA Notifications to BCC:** We’re aligning account-level [email alerts and notifications](/v1/docs/working-with-mailing-lists) to the standard Cato notification format, so the recipients are all in BCC.
  - Previously, all recipients were in the To field of the email

- **Register for Our May 6 Academy Live Tech Hour:** Unlock the full potential of Cato’s Application Control. Discover best practices, new features, and hidden capabilities to protect your SaaS applications with inline and out-of-band connections. Register [here](https://academy.catonetworks.com/live-master-application-control)

## PoP Announcements

- **Ashburn, US:** A new range (149.20.197.0/24) is now available for the Ashburn PoP location.

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2024-57049 (New)
    - CVE-2025-23120 (New)
    - CVE-2025-24813 (New)
    - CVE-2025-1661 (New)
    - CVE-2024-57045 (New)
    - CVE-2025-26319 (New)
    - CVE-2025-24035 (New)
    - CVE-2025-21400 (New)
    - CVE-2017-12637 (New)
    - CVE-2025-23369 (New)
    - CVE-2025-29927 (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget XamlAssemblyLoadFromFile (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget ToolboxItemContainer (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget ObjRef (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget GetterSettingsPropertyValue (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget GetterSecurityException (New)
    - Generic .Net Insecure Deserialization Over HTTP: Gadget GetterCompilerResults (New)
    - Ransomware - Optimus (Chaos) (New)
    - Ransomware - AstraLocker 2.0 (Enhancement)
    - Ransomware - Anonymous (Xorist) (Enhancement)
    - Ransomware - Worry (WhatsWrongScared) (Enhancement)
    - Ransomware - Elons (Enhancement)
    - Ransomware - Moscovium (Enhancement)
    - Ransomware - Mamona (Enhancement)
    - Ransomware - Data (Enhancement)
    - Ransomware - Anubi (Enhancement)
    - Ransomware - VanHelsing (Enhancement)
    - Ransomware - SuperBlack (Enhancement)
    - Ransomware - Zphs (Enhancement)
    - Ransomware - Moroccan Dragon (Enhancement)
    - Ransomware - Babyk (New)
    - Ransomware - EndPoint (New)
    - Ransomware - Tianrui (Enhancement)
    - Ransomware - Pizdec (Enhancement)
    - Ransomware - Louis (Enhancement)
    - Ransomware - Jett (Enhancement)
    - Ransomware - M142 HIMARS (Enhancement)
    - Ransomware - BlackHeart (MedusaLocker) (Enhancement)
    - Ransomware - Danger (GlobeImposter) (Enhancement)
    - Ransomware - Aptlock (Enhancement)
    - Ransomware - EnCiPhErEd (Enhancement)
    - Ransomware - Weaxor (Enhancement)
    - Ransomware - Netwalker (Enhancement)
    - Ransomware - Monti (Enhancement)
    - Ransomware - Maze (Enhancement)
- **Apps Catalog**
  - More than 120 new Cloud Apps (see [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - PJL (New)
    - Cloudbox Technology Ltd (New)
    - TACACS+ (New)
    - Autodesk (Enhancement)
    - Appid - ninjarmm (Enhancement)
    - Mimecast Services Limited (Enhancement)
- **XDR Indications of Attack Signatures:**
  - Anomaly Detection:
    - Anomaly Detection:
    - Psexec First Occurrence (New)
    - Outbound FTP First Occurrence (Enhancement)
    - Wanbound FTP First Occurrence (New)
    - ConnectWise ScreenConnect Remote Connection First Occurrence (New)
    - Atera Remote Connection First Occurrence Anomaly (New)
    - IP checking services First Occurrence (New)
- **Application Control (CASB and File Control):**
  - **Application Control:**
    - Slack - Send Message (Text) (Enhancement)
    - Perplexity - Login (New)
    - Perplexity - Conversation (New)
    - Perplexity - Upload (New)
    - Google Photos - Download (Enhancement)
    - Google Photos - Upload (Enhancement)
    - MS Teams - upload file (Enhancement)
    - Hiqzen - Upload (New)
    - LinkedIn - Post (Enhancement)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - **IOT**
      - Docking Station
        - Action Star (Enhancement)
        - Multifunction Device
        - Toshiba (Enhancement)
      - Printer
        - HP (Enhancement)
        - MICROPLEX Printer (New)
        - Argox Printer (new)
        - INTERMEC Printer (New)
      - 3D Printer
        - Prusa 3D Printer (New)
      - VoIP
        - Alcatel (Enhancement)
        - Cisco (Enhancement)
        - AudioCodes IP Phone (New)
        - Ascom Device (Enhancement)
        - Biamp VoIP Device (New)
      - Smart TV
        - Samsung Smart TV (Enhancement)
      - Media Player
        - Shiningworth Media Player (New)
      - IP Camera
        - Lorex IP Camera (New)
        - Mobotix IP Camera (New)
      - Alarm
        - Technoalarm Alarm System (New)
      - Smart Home
        - eQ-3 Smart Home Device (New)
      - Workforce Management Terminal
        - Kaba Benzing Device (New)
    - **Mobile**
      - Mobile Phone
        - OnePlus (Enhancement)
        - Samsung (Enhancement)
        - Zebra (Enhancement)
        - iPhone/iPad (Enhancement)
        - Galaxy Smartphone A series (Enhancement)
        - Galaxy Smartphone S series (Enhancement)
    - **Networking**
      - Network Appliance
        - Cisco Meraki (Enhancement)
        - TP-LINK Device (Enhancement)
        - 3Com Network Appliance (New)
      - NAS
        - QNAP NAS (New)
    - **PC**
      - Desktop
        - Dell (Enhancement)
        - Lenovo (Enhancement)
      - Laptop
        - Apple (Enhancement)
        - Dell (Enhancement)
        - HP (Enhancement)
        - Lenovo (Enhancement)
        - Microsoft (Enhancement)
        - Toshiba (Enhancement)
      - Workstation
        - Apple (Enhancement)
        - Asus (Enhancement)
        - Dell (Enhancement)
        - HP (Enhancement)
        - MSI (Enhancement)
      - Thin Client
        - Dell (Enhancement)
        - IGEL Technology (New)
    - Server
      - Print Server
        - HP (Enhancement)
        - Windows VMware (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
