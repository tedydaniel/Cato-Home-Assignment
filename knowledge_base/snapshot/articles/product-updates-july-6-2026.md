---
title: "Product Updates - July 6, 2026"
slug: "product-updates-july-6-2026"
updated: 2026-07-05T13:29:21Z
published: 2026-07-05T13:29:21Z
canonical: "knowledge.catonetworks.com/product-updates-july-6-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - July 6, 2026

## New Features & Enhancements

- **Updated EOS Policy for Cato Clients:** We are updating the End of Support (EOS) policy for Cato Clients for all operating systems and devices to make the support lifecycle clearer and help you plan Client upgrades more effectively.
  - Each Client version automatically reaches EOS one year after its release date. For information, see this article

- **Ask AI Simplifies Support Escalation:** Ask AI helps you investigate issues faster with guided answers and relevant context. Troubleshoot issues directly in Ask AI, and if needed, it will create a draft of a Support ticket populated from the full context of your conversation.

- **Socket Hardware Refresh for X1500A and X1700A Models:** Following the February 2026 End of Support (EOS) announcement for X1500A and X1700A Sockets (effective July 1, 2030), Cato is starting the hardware refresh process to replace eligible devices with newer models. Cato notifies eligible accounts during the renewal process. For details, see this article.

- **XOps Experience Anomaly Enhancements:** We expanded Experience Anomalies with new detections for application response time and HTTP latency across remote users, sites, and ISPs. Other enhancements include:
  - Related anomalies detected for multiple users are automatically aggregated into a single story
  - The new Entities widget shows all impacted entities
  - Each anomaly detection generates an event of subtype Anomaly shown in the story Incident Timeline, and available in the Events page
  - DEM and XOps licenses required. Show me the [CMA page](https://externallink.cc.catonetworks.com/#/account/me/detectionAndResponse)

- **Expanded Posture Checks:** Get broader visibility into your account with new checks for SSO, Always-On, Device Posture, and network settings to make sure you are aligned with Cato best practices. To view posture checks, go to Home > Posture (open the Posture CMA page).

- **Improved AI Security Engine Detection:** We enhanced the AI Security Engine to more accurately detect sensitive personal identifiers in AI interactions, including a significantly improved **Name** detector. This helps identify more relevant AI Security events with fewer false positives.
  - AI Security for Applications or AI Security for Users license required

- **CMA Enhancement - Improvements to the App Catalog:**
  - **Display FQDNs:** The App Quick View panel displays the FQDNs associated with each app
  - **Search Account Overridden Domains:** On the Account Overridden Domains panel, you can search the list of domain categories that you redefined for your account

## PoP Announcements

- **Tokyo, JP:** A new range (113.30.138.0/24) is now available for the Tokyo PoP location.
- The following localized IP ranges for Egypt and Martinique are now available:
  - **EG:** 216.252.183.32/27 (serviced through the Milan PoP location)
  - **MQ:** 45.62.191.160/28 (serviced through the Miami PoP location)
- The following new ranges will soon be available:
  - **London, UK:** 159.117.244.0/24
  - **Paris, FR:** 159.117.245.0/24

## Security Updates

- **Apps Catalog**

View more details about apps in the Apps Catalog.
  - New Apps: 9 new apps: AireSpring AirePBX, Gurkerl, Kifli, Knuspr, Rohlik, Rohlik Group, S7comm, Sezamo, Wonderful
  - Enhanced Apps:
    - Amazon Bedrock
      - Updated app domains
    - RTP
      - Signature Updated
    - Tnt
      - Added domain [**tnt.fr**](http://tnt.fr)
    - Tor Network
      - Signature Updated
      - Updated app IPs
  - Category Changes:
    - Business Operations AI:
      - Removed app: SiliconExpert
    - Business Systems:
      - Added apps: Deon Gmbh & Kg, Qzzr, Inc., Yasoon Gmbh, conceptboard
    - Chat and IM:
      - Added app: Keybase
    - Computers and Technology:
      - Added apps: Bechtle Ag, Boschsecurity, Telekom
    - ERP And CRM:
      - Added apps: Scopevisio Ag, ariba
    - Education:
      - Added apps: Duden, Toddle
    - Finance:
      - Added apps: Billomat Gmbh & Kg, Lexoffice
    - Generative AI Tools:
      - Removed app: SiliconExpert
    - Government:
      - Added app: Af
    - Hiring:
      - Added apps: Gradar, Heavenhr Gmbh
    - News:
      - Added apps: Bmj, Computerbase, Gsmarena, Heise, Sport1, Tvspielfilm, Wallstreet-online, Winfuture
    - Online Storage:
      - Added apps: Amana, Filesanywhere, Lucidlink Corp, Qumulo, T&D WebStorage, TeamDrive, Your Secure Cloud Gmbh
    - Shopping:
      - Added apps: Galerieslafayette, Hagebau, Hoffmann-Group, Notebooksbilliger
    - Vehicles:
      - Added apps: Adac, Autobahn Technologies Llc, Autozone, Cummins, LeasePlan Corporation N.V., Louis, Paccar, Vanmoof B V, terex
    - Voip Video:
      - Added app: Snom
    - Web Hosting:
      - Added apps: Hetzner, Strato, hosteurope
- **IPS Signatures**

View more details about the IPS signatures and protections in the Threats Catalog.
  - CVE-2024-36420 (New)
  - CVE-2025-69971 (New)
  - CVE-2026-4810 (New)
  - CVE-2026-33032 (New)
- **TLS Inspection**
  - Remove [cursor.ai](http://cursor.ai) from global TLS bypass rules (Enhancement)
- **XDR Indications of Attack**
  - Threat Prevention
    - First Seen External Teams Chat from Suspicious Tenant by Account (New)
    - First Seen External Teams Chat from Suspicious Tenant by Account (New)
    - First Seen External Teams Chat from Suspicious Tenant by Account (New)
  - Anomaly Detection
    - First Seen Kerberos Bruteforce Activity By Site (New)
    - First Seen Kerberos Bruteforce Activity By User (New)
    - First Seen External Teams Chat from Suspicious Tenant by Account (New)
    - First Seen External Teams Call from Suspicious Tenant by Account (New)
    - First occurrence of a high risk AI application on the account (New)
    - Sensitive File Download to First Seen Device (New)
  - Indications of Attack
    - First Seen Kerberos Bruteforce Activity By Site (New)
    - First Seen Kerberos Bruteforce Activity By User (New)
    - Sensitive File Download to First Seen Device (New)
- **Device Inventory**

These are the updates to the [Device Inventory](https://support.catonetworks.com/hc/en-us/articles/14529548359709-Using-the-Device-Inventory) detection engine:
  - New Devices: 9 new devices
  - OT:
    - Circuit Breaker Network Interface:
      - Schneider Electric EnerlinX IFE LV434010 (New)
    - Flow Meter:
      - Emerson Micro Motion 5700 5700 Ethernet Coriolis Flowmeter (New)
    - OT Gateway:
      - Modbus/TCP to RTU Bridge (New)
      - Schneider Electric Acti9 PowerTag Link A9XMWD20 (New)
      - Schneider Electric ComX 510 EBX510 (New)
      - Schneider Electric EnerlinX IFE Switchboard Server LV434011 (New)
    - PLC:
      - Schneider Electric Modicon M340 BMX P34 2020 (New)
      - Schneider Electric Twido TWDLCAE40DRF TWDLCAE40DRF (New)
    - Power Meter:
      - Phoenix Contact EMpro EEM-MA371-R 2907985 (New)
- **Application Control Via API and Data Protection API Integrations**

The enhancements were made for [Application Control Via API](https://support.catonetworks.com/hc/en-us/sections/24373046669085-Application-Control-via-API-with-App-Activities)
  - New: SaaS Security Posture Management (SSPM) - 10 apps
    - Salesforce | SaaS Security Posture (New) - 43 posture checks across session, password and lockout policy, clickjack/CSRF/session hardening, OAuth token hygiene, SSO, IP restrictions and external sharing
    - Microsoft 365 | SaaS Security Posture (New) - 38 posture checks across Entra ID MFA/passwordless, Conditional Access, legacy-auth blocking, privileged-role and guest governance, and SharePoint sharing/app-consent controls
    - Zendesk | SaaS Security Posture (New) - 32 posture checks across 2FA/SSO enforcement, admin and end-user session controls, password policy, API token hygiene, and attachment/privacy settings
    - GitHub | SaaS Security Posture (New) - 26 posture checks across org MFA/2FA and SSO enforcement, repository visibility and permission defaults, secret scanning/push protection, and outside-collaborator governance
    - Google Workspace | SaaS Security Posture (New) - 22 posture checks across 2SV enforcement, super-admin governance and recovery, session/password policy, Gmail spoofing/attachment protections, and marketplace app-access restrictions
    - Google Drive | SaaS Security Posture (New) - 18 posture checks across external sharing and web-publishing restrictions, shared-drive access governance, Drive SDK/desktop controls, and file-security enforcement
    - Dropbox | SaaS Security Posture (New) - 15 posture checks across admin/suspended-user counts, external sharing and shared-link policy, link expiration/password enforcement, and device (EMM) and group-creation controls
    - ChatGPT | SaaS Security Posture (New) - 8 posture checks across Enterprise admin governance, unused API-key revocation, project visibility and spend alerts, and external-account/custom-GPT sharing restrictions
    - Cursor | SaaS Security Posture (New) - 8 posture checks across admin count and external-admin/account review, orphaned/inactive account cleanup, repository blocklist, spend limits, and client-version currency
    - Slack | SaaS Security Posture (New) - 6 posture checks across workspace/admin MFA, inactive-user and admin-count review, guest-user governance, and externally shared channel detection
  - Enhancements: Activity
    - Microsoft General | Activity (Enhancement) - extracts additional resource and device fields ([resource.id](http://resource.id), os.type)
    - Microsoft Defender | EDR (Enhancement)
    - Citrix ShareFile | Activity (Enhancement)
  - Enhancements: EDR
    - Microsoft Defender (Enhancement)

**Note:** Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this article. See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
