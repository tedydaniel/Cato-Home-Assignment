---
title: "Product Updates - March 30, 2026"
slug: "product-updates-march-30-2026"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-march-30-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - March 30, 2026

## Introducing Cato AI Security

### **Secure and Govern AI Usage Across Your Organization**

The new AI Security service lets you confidently adopt AI tools and applications across your environment while maintaining full visibility, policy enforcement, and data protection. AI Security includes these scopes:

- AI for End Users governs how employees use external AI services and AI-enabled SaaS applications
  - Click [here](https://academy.catonetworks.com/path/product-update-12-march-2026) to watch video recordings of AI for Users
- AI for Applications protects AI capabilities built into your enterprise systems and custom applications
  - Click [here](https://academy.catonetworks.com/path/product-update-19-march-2026) to watch video recordings of AI for Applications
- AI Security helps you control AI usage with the following capabilities:
  - Gain visibility into AI interactions across public AI tools, AI-enabled SaaS applications, and custom AI-powered apps
  - Apply consistent threat prevention and data protection controls to AI interactions
  - Monitor prompts and responses to detect misuse and prevent data leakage in real time
  - Enforce acceptable use and compliance policies for AI services used by employees
  - Secure API calls and data flows between enterprise applications and AI models
- Available in Demo Mode in the Cato Management Application (CMA)
- Read the Knowledge Base articles [here](/v1/docs/ai-security) (you must be logged in to view the articles)
- Requires an AI Security for Users or AI Security for Applications license. For more information, contact your Cato representative or authorized reseller

## New Features & Enhancements

- **Accelerate Troubleshooting with Expanded Ask AI Event Coverage:** We added broader event coverage across your environment so that Ask AI helps you resolve issues faster, including:
  - Investigating security, network, connectivity, and audit events in one place
  - Getting Socket-related information, such as how many X1500B Sockets do I have?
  - Starting troubleshooting immediately and resolve issues before opening a Support ticket
  - Available in the [Ask AI assistant](/v1/docs/what-is-cato-s-ask-ai-agent) in the CMA and through [Cato’s remote MCP server](/v1/docs/working-with-the-cato-remote-mcp-server)
  - Click [here](https://academy.catonetworks.com/path/product-update-29-march-2026) to watch a video recording of this feature
- **Aggregated WAN Throughput for Socket Sites in Network Analytics:** You can view total aggregated WAN link throughput for Socket sites in the [Network Analytics](/v1/docs/showing-the-site-network-analytics) page, including concurrent hosts and flows. This provides a unified view of site capacity and utilization, helping you better monitor performance and identify bottlenecks across all WAN links. Previously, metrics were shown only per link.
  - The existing **Site & Tunnel** tab is now split into separate **Site** and **Tunnel** tabs. The new aggregated metrics appear in the **Site** tab
- **RBI Profiles for Granular Browser Isolation Policies:** Create Remote Browser Isolation (RBI) [profiles](/v1/docs/configuring-the-rbi-service-for-browsing-sessions) with different browsing isolation controls and assign them to specific Internet Firewall rules. This lets you apply different RBI behavior based on user role, risk level, or business need. For example, you can enforce stricter RBI controls for uncategorized domains and more relaxed controls for SaaS apps.
  - Click [here](https://academy.catonetworks.com/path/product-update-29-march-2026) to watch a video recording of this feature
- **Cato Security App for Splunk with a Threats Dashboard:** Monitor and investigate security threats with the official Cato Security App for Splunk, giving you visibility similar to the [Threats Dashboard page](/v1/docs/using-the-security-threats-dashboard) in the CMA.
  - View IPS, DNS, Anti-Malware, and suspicious activity data
  - Filter data by time range, index, and SPL query
  - Click [here](https://academy.catonetworks.com/path/product-update-29-march-2026) to watch a video recording of this feature
- **Device-based Criteria for Network Rules**: Apply device criteria conditions to [Network Rules](/v1/docs/what-are-network-rules) to control routing and connectivity decisions based on device identity, posture, and context.
  - Apply attributes such as OS, platform, manufacturer, and model when matching Network Rules
  - Use Device Posture Profiles to route traffic only for compliant devices (for example, approved Client versions)
  - Differentiate Network Rules based on device location, origin (remote or behind a site), or device category (such as IoT/OT)
  - Click [here](https://academy.catonetworks.com/path/product-update-5-march-2026) to watch a video recording of this feature
- **Configure Custom Thresholds for Default DEM Probes:** Fine-tune alert sensitivity for default [DEM probes](/v1/docs/configuring-the-experience-monitoring-probes-and-policy) by configuring custom thresholds to help you detect issues more accurately based on your environment. The configurable predefined default probes include:
  - LAN Gateway
  - Underlay Reachability
  - Underlay Socket Traceroute
  - Supported from:
    - Socket v25 and higher
    - Windows Client v5.22 and higher
    - macOS Client v5.11 and higher
  - Click [here](https://academy.catonetworks.com/path/product-update-15-january-2026) to watch a video recording of this feature
- **Application Control via API - Support for Miro:** Connecting SaaS apps to Cato lets you understand who is accessing each app and identify suspicious activities or trends even when users are not connected to the Cato Cloud. You can now connect your [Miro](/v1/docs/miro-configuring-the-app-activities-integration) account to provide visibility into user activities.
  - The Miro connector is available from the **Integrations Catalog**, under **App Activities**
  - CASB license required
- **AI-Driven LAN Firewall Analysis and Insights:** We’re extending an [AI-driven enhancement](/v1/docs/understanding-cato-autonomous-policies) to the Socket Next Gen LAN Firewall policy that provides admins with actionable insights to optimize their firewall configurations, improve security posture, and ensure compliance with best practices. The Autonomous Firewall engine automatically analyzes your LAN Firewall rulebase and detects issues such as:
  - Temporary rules
  - Rules that are expired or soon to expire
  - Test rules
  - Click [here](https://academy.catonetworks.com/path/product-update-12-march-2026) to watch a video recording of this feature
- **LAN Firewall and Network Rules Hit Counter:** The LAN Firewall and Network Rules policies now include a hit counter to help you monitor the performance of each rule in the policy. Hit counts are based on events generated by the rules, and show:
  - The number of events generated by each rule in the policy
  - How often the rule is hit relative to other rules (ranked by percentile)
  - Click [here](https://academy.catonetworks.com/path/product-update-16-november-2025) to watch a video recording of this feature
- **Advanced Groups for Network Rules and Socket LAN Firewall Include Support for IP Ranges:** We extended support for advanced [groups](/v1/docs/working-with-cma-advanced-groups-and-groups) to Network Rules and the Socket Next Gen LAN Firewall, including defining and reusing large sets of [IP ranges](/v1/docs/using-ip-ranges-in-policies). This reduces manual configuration and ensures consistency at scale.
  - Previously available for the Internet and WAN Firewall policies
- **User Risk Score Dashboard Role-Based Permissions**: Better control which admins can access user-related security data and take actions such as revoking sessions or resetting risk levels.
  - Available from the Access Admin role in the Account > Roles and Permissions page
  - By default, users with the Access role have edit permissions on the User Monitoring > [User Risk page](/v1/docs/understanding-the-user-risk-level)
- **Microsegmentation with Third-party DHCP Server Using DHCP Relay:** Enforce [microsegmentation](/v1/docs/adding-microsegmentation-zero-trust-security-to-sites) for network ranges that use an external DHCP server, without changing your existing DHCP infrastructure. When Cato is configured as a DHCP relay, the external server assigns IP addresses while Cato applies the same /32 host routing and east-west traffic inspection as with Cato-managed DHCP.
  - Click [here](https://academy.catonetworks.com/path/product-update-8-january-2026) to watch a video recording of this feature
- **Enhanced OCR Scanning for DLP:** To improve detection accuracy for image-based content [OCR scanning](/v1/docs/creating-dlp-content-profiles) now includes coverage for more complex image conditions and text patterns, for example:
  - Low-resolution and blurred mobile images
  - Warped, rotated, or crumpled images
  - Images that contain text in two languages
- **Optimized Real-Time Quality Health Alerts:** Faster and more responsive detection of quality issues improves visibility into network performance.
  - Automatically applied to [Quality Health Rules](/v1/docs/working-with-link-health-rules)
  - May generate more frequent alerts due to increased sensitivity. To reduce alert volume, adjust your Quality Health Rules configuration
- **Events Show When Sites are Down:** For better visibilty into site availability, we added new events to indicate when all site links are down and when one or more links recover.
  - Previously, events were reported only per link
- **API for Creating and Managing Webhooks, Mailing Lists, and Subscription Groups:** Automate notification delivery across email and third-party systems using a unified API.
  - For more information, see this [article](/v1/docs/cato-api-changelog)

## PoP Announcements

- **Seoul, KR:** A new range (113.30.133.0/24) will soon be added to the Seoul PoP location.
- **Upcoming New Localized IP Range for Estonia:** The following localized IP range for Estonia (serviced through the Helsinki PoP location) will soon be available:
  - **EE:** 159.117.235.32/27

## Security Updates

- **Apps Catalog**

View more details about apps in the [Apps Catalog](/v1/docs/using-the-app-catalog).
  - New Apps: 5 new apps - ADB, Claud GPT, Sparkup, StackAI, Tango
  - Removed Apps: 1 apps - Hangouts for desktop (Deprecated)
  - Enhanced Apps:
    - Apple Account
      - Application is now available in Application Control rules
    - Apple App store
      - Application is now available in Application Control rules
    - Apple iCloud Private Relay
      - Application is now available in Application Control rules
    - Apple location services
      - Application is now available in Application Control rules
    - Apple Safe Browsing proxy
      - Application is now available in Application Control rules
    - Apple software update
      - Application is now available in Application Control rules
    - Asana
      - Updated app domains
    - Autodesk
      - Updated app domains
    - Cisco General
      - Application is now available in Application Control rules
    - Cisco Secure Endpoint (formerly AMP)
      - Modified name from **Cisco Advanced Malware Protection (AMP)** to **Cisco Secure Endpoint (formerly AMP)**
      - Application is now available in Application Control rules
    - Darktrace
      - Updated app domains
    - Google Chat
      - Updated app domains
    - Google meet
      - Added domains **duo.google.com**, **meet.turns.goog**, **tel.meet**
      - Updated app IPs
    - Huntress
      - Updated app domains
    - Jfrog
      - Updated app domains
    - Kandji
      - Updated app domains
    - Microsoft Exchange (Outlook)
      - Signature Updated
    - Microsoft Office365
      - Signature Updated
    - Ninjarmm
      - Updated app domains
    - PDF Converters Unified
      - Removed domain **dfcfw.com**
    - RingCentral
      - Updated app IPs
    - Splashtop
      - Updated app domains
    - Vicarius
      - Updated app domains
    - Vonage
      - Updated app domains
    - Zscaler
      - Updated app IPs
  - Category Changes:
    - Generative AI Tools:
      - Added app: Notion
    - News:
      - Added app: Meteofrance
    - Productivity:
      - Added app: Notion
    - Restaurants, Leisure and Recreation:
      - Removed app: Meteofrance
    - Travel:
      - Added app: Meteofrance
- **IPS Signatures**

View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - CVE-2025-34067 (New)
  - CVE-2025-40551 (New)
  - CVE-2025-40552 (New)
  - CVE-2025-40553 (New)
  - CVE-2025-71243 (New)
  - CVE-2026-0770 (New)
  - DNS Tunneling Abusing NULL Quereies (New)
  - DNS Tunneling | Iodine (Enhancement)
  - Long DNS Type A Query Request (New)
  - Malware - Chrysalis C2 Traffic (New)
  - Websocket Traffic To Low Popularity Target (New)
- **SAM Signatures**

These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
  - Agent Skill ClawHub Web Search (New)
  - Agent Skill ClawHub Download Web (New)
- **XDR Indications of Attack**
  - Threat Hunting
    - Suspicious Files Downloaded From Netlify (New)
- **Device Inventory**

These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
  - IOT
    - IP Camera
      - Ubiquity IP Camera (Enhancement)
- **Application Control Via API and Data Protection API Integrations**

The enhancements were made for [Application Control Via API](/v1/docs/application-control-via-api-with-app-activities)
  - Miro Activities
    - Activity (New)
  - Microsoft Exchange
    - Activity (Enhancement)
    - Anomalies (Enhancement)
  - Microsoft Teams
    - Experience (Enhancement)
  - Zoom
    - Activity (Enhancement)
  - GitHub
    - Activity (Enhancement)
    - Anomalies (Enhancement)
  - Google Apps
    - Activity (Enhancement)
    - Anomalies (Enhancement)
  - Google Drive
    - Activity (Enhancement)
  - Dropbox
    - Anomalies (Enhancement)
  - Slack
    - Anomalies (Enhancement)
    - Third Party Apps (Enhancement)
  - DocuSign
    - Activity (Enhancement)
    - Anomalies (Enhancement)
  - Microsoft General
    - Activity (Enhancement)
    - Anomalies (Enhancement)
  - Azure AD
    - Third Party Apps (Enhancement)
  - SalesForce
    - Third Party Apps (Enhancement)
