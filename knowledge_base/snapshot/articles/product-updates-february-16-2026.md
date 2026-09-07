---
title: "Product Updates - February 16, 2026"
slug: "product-updates-february-16-2026"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-february-16-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - February 16, 2026

## New Features & Enhancements

- **New Security Engine Automatically Identifies and Blocks Threats:**[Dynamic Prevention](/v1/docs/what-is-dynamic-prevention) reduces the attack surface by continuously analyzing behavior to detect and automatically block advanced threats. Behavioral patterns are correlated over time to identify subtle anomalies that indicate sophisticated and evasive attacks.
  - When malicious activity is detected, preemptive controls are automatically enforced to block harmful actions
  - These controls dynamically adapt to real-time changes in your environment, ensuring ongoing protection against emerging and evolving threats without manual intervention
  - Advanced Threat Protection license required
- **Secure Enterprise Browser:** Allow users to access any web-based application with a new [Enterprise Browser](/v1/docs/what-is-the-cato-enterprise-browser). Extend Cato’s browser-based security from an extension to a full Enterprise Browser, giving you additional controls over how users interact with applications.
  - Maintaining all Browser Extension controls and configurations
  - Enterprise Browsers increases security by blocking developer tools and restricting the use of browser extensions
  - Protect sensitive data with granular controls for copy, paste, upload, download, printing, typing, and watermarks
  - Secure access for BYOD, contractors, and third parties without full device management
- **CMA Status Page for Real-Time PoP Status and Service Health:** The [Status Page](/v1/docs/using-the-status-page) lets you view how your assets are distributed across the Cato platform, identify the PoPs that your sites and remote users are connected to, and monitor their service health. This helps teams quickly assess operational status and respond to issues.
  - View the overall service health status for all your connected sites and users
  - Get real-time indications for ongoing PoP maintenance events and active incidents
- **User Risk Score Dashboard**: Drill down into an individual [user's risk score](/v1/docs/understanding-the-user-risk-level) to understand how their risk level is calculated and how it changes over time. The dashboard provides visibility to help you prioritize investigations and take proactive steps, such as revoking a session to reduce organizational risk.
  - View a historical timeline of the user’s risk score
  - Identify which risk domain (e.g., malware, access abuse) most influences the score
- **Use Case-Driven Security Posture Checks:** To streamline onboarding and daily operations, implement [best practices for specific use cases](/v1/docs/working-with-predefined-security-policy-rules-posture-checks) to enhance your security posture, eliminating the need to design policies from scratch. Use a configuration wizard to quickly and easily implement these rules, helping you deploy best practice protections faster.
  - Initially supported for the Internet Firewall, then in the coming weeks, this will be rolled out to the following policies:
    - WAN Firewall
    - TLS Policy
    - Application Control
    - Data Control
- **New Clients:** During the week of February 15, 2026, we are starting to roll out the following Clients, or they will be available from the relevant app store. The versions contain stability improvements, internal enhancements, security updates, and bug fixes:
  - [macOS Client v5.11](/v1/docs/summary-of-cato-macos-client-releases)
  - [Android Client v5.4](/v1/docs/summary-of-cato-android-client-releases)
  - [Linux Client v5.6](/v1/docs/summary-of-cato-linux-client-releases)
- **DEM Integration for Access Point Events:** Gain visibility into Wi-Fi [access point events](/v1/docs/the-user-experience-monitoring-drill-down-page-remote-and-office-users) from third-party vendors and correlate them with user experience data to identify the root cause of office connectivity issues. This lets you analyze access point events such as authentication, reassociation, roaming, and deauthentication together with existing DEM metrics for a more complete view of the network path.
  - Initial support includes Juniper Mist access points
  - Requires a DEM license and configuration of the [Juniper Mist connector](/v1/docs/juniper-mist-creating-the-device-management-integration)
- **Security Controls for Browser Extension:** Apply granular data [security controls](/v1/docs/security-controls-for-the-cato-browser-extension) to Browser Extension users to reduce the risk of a data leak
  - Block or allow clipboard, file downloads/uploads, printing, and typing
  - Add a watermark to the page containing the user’s information
  - Policies and rules apply to users throughout all remote access methods: Client, Browser Extension, and Enterprise Browser
- **Data Protection via API Support for Egnyte:** Ensure data protection and control over sensitive data within your [Egnyte](/v1/docs/egnyte-configuring-the-data-protection-api-connector) account. This connector provides visibility and control over user actions (for example, remove share) even when not connected to the Cato Cloud.
  - The Egnyte app is available from the **Integrations Catalog**, under **Data Protection**
  - SaaS Security API license required
- **Split Tunnel Policy for Web-Only Connection Mode:** Route only web traffic through the Client DTLS tunnel, while all other traffic is excluded and routed directly to the Internet or a third-party solution. This enables you to gradually migrate your users to Cato Internet security.
  - Configure the **Web-only** Connection mode in the [Split Tunnel policy](/v1/docs/routing-with-the-cato-client-split-tunnel-policy) (Access > Split Tunnel) for the relevant users or user groups
  - The Client requires write permissions on the system PAC file
  - Supported for Windows Client v5.16 and higher
- **Customize End User Block Pages and Notifications:** To coach users on why an action was blocked, create and assign multiple [notification templates](/v1/docs/creating-user-notification-templates) and assign them to a policy rule. This lets you provide contextual notifications tailored to specific use cases at the point of enforcement.
  - Create the notification template and assign it to a Firewall, CASB, or DLP policy rule
- **Forensic Analysis for DLP:** To investigate incidents more effectively, understand their context, and validate false positives, [forensic evidence](/v1/docs/investigating-dlp-violations-with-forensic-evidence) for DLP policy violations is available on demand.
  - Evidence is encrypted and stored only in a configured third-party destination, Cato does not retain the data
  - Visibility of the evidence is restricted based on [admin roles](/v1/docs/what-are-admins-and-role-based-access-control-rbac)
- **IoT Internet Traffic Visibility with Sankey Diagram:** The [Device Dashboard](/v1/docs/using-segmentation-flows) now includes a Sankey diagram that provides visibility for the protocols and destinations used by IoT devices when accessing the Internet. This diagram enables more informed segmentation and security policy decisions.
- **Improved Clarity and Visibility for LDAP Sync Results:** LDAP synchronization now provides clearer visibility into which changes are previewed and which are actually applied. This helps you better understand sync outcomes and reduces confusion when comparing to manual or SCIM-provisioned users and groups.
  - The first LDAP sync (manual or scheduled) may generate a higher-than-usual number of LDAP provisioning events. This is expected behavior.
- **New User Attributes - Department and Job Title:** Department and Job Title are available as user attributes in the Cato Management Application (CMA). These fields provide more granular insight into your user base and let you configure targeted policies.
  - For LDAP, no action is required. A full directory sync will occur once the feature is enabled
    - Update events might be generated for all users
  - For SCIM, you must [update your Cato app](/v1/docs/scim-user-provisioning) for the SCIM vendor and map the new attributes
  - For manually created users, the fields are available in each user profile and can be updated by Admins as required
- **New Release for EPP Agent v1.6:** Starting the week of Feb 15, 2026, we are rolling out [EPP Agent version 1.6](/v1/docs/summary-of-epp-agent-versions). This version includes bug fixes and enhancements.
- **Share Advanced Device Analytics:** Enables sharing of enhanced device usage analytics to help improve product quality and support, with no traffic or data SKU overhead.
  - You can [disable](/v1/docs/configuring-system-settings-for-the-account) this feature under **Resources > System Settings > System**
  - This is being gradually rolled out over the next few weeks
- **Site Socket Descriptions Supported via API**: Manage descriptions for primary and secondary Sockets using the API. This configuration was previously available only in the CMA.
  - Use the **updateSiteSocketConfiguration** API

## Security Updates

- **Apps Catalog**

View more details about apps in the [Apps Catalog](/v1/docs/using-the-app-catalog).
  - Enhanced Apps:
    - Cato Management Application
      - Added domain **cc.catonetworks.com**
      - Application is now available in Application Control rules
    - Google Drive
      - Updated app domains
    - Quad9
      - Updated app IPs
  - Category Changes:
    - Advertisements:
      - Removed app: Criteo S.A.
    - Business Information:
      - Added app: Criteo S.A.
- **Application Control Policy**
  - CASB
    - Chrome Extension - Install (New)
    - YouTube - Watch (Enhancement)
- **IPS Signatures**

View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - CVE-2021-39935 (New)
  - CVE-2022-31678 (New)
  - CVE-2022-36923 (New)
  - CVE-2022-37932 (New)
  - CVE-2024-37079 (New)
  - CVE-2025-25570 (New)
  - CVE-2025-52665 (New)
  - CVE-2025-54236 (New)
  - CVE-2025-56520 (New)
  - CVE-2026-1281 (New)
  - CVE-2026-23760 (New)
  - Exploitation - MongoMeltdown MongoDB Denial of Service (New)
  - Heuristic - Python Reverse Shell Download over HTTP (Enhancement)
  - Malware - Foxveil (New)
- **XDR Indications of Attack**
  - Anomaly Detection
    - Zoho Remote Connection First Occurrence Anomaly (Enhancement)
  - Threat Hunting
    - Abnormal Protocol Activity (Enhancement)
  - Threat Prevention
    - Lateral Movement activity blocked by Dynamic Prevention on WANBOUND (New)
    - C2 activity blocked by Dynamic Prevention on OUTBOUND (New)
    - Data Exfiltration activity blocked by Dynamic Prevention on OUTBOUND (New)
    - Discovery activity blocked by Dynamic Prevention on WANBOUND (New)
    - Impact activity blocked by Dynamic Prevention on WANBOUND (New)
- **Application Control Via API and Data Protection API Integrations**

The enhancements were made for [Application Control Via API](/v1/docs/application-control-via-api-with-app-activities)
  - Microsoft Entra ID | Third Party Apps (New)
  - Slack | Third Party Apps (New)
  - Microsoft Teams | Experience Monitoring (Enhancement)
  - Juniper Mist | WiFi Events (New)
  - Egnyte | DLP (New)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
