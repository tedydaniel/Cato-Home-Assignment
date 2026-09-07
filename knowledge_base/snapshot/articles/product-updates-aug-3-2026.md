---
title: "Product Updates - Aug 3, 2026"
slug: "product-updates-aug-3-2026"
updated: 2026-08-03T10:19:16Z
published: 2026-08-03T10:19:16Z
canonical: "knowledge.catonetworks.com/product-updates-aug-3-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - Aug 3, 2026

## New Product Launch

**New Cato Security Service - Agentic Threat Prevention**

- **Automatically Block Agentic AI Threats and Attacks:** [Agentic Threat Prevention](https://knowledge.catonetworks.com/docs/what-is-agent-threat-prevention) employs AI agents to help protect against attackers that use frontier AI models to automate, adapt, and accelerate attacks. The service analyzes security events, threat signals, and network activity to identify and block suspicious behavior.
  - **Detect emerging threats faster:** Identify suspicious behavior and early indicators of attacks that use frontier AI models at machine speed
  - **Disrupt attack progression:** Automatically block behaviors associated with the current attack stage and the attacker’s likely next tactic before there is any impact to your network
  - **Adapt protection continuously:** Reassess activity and update enforcement as attacker behavior changes
- Contact your Cato representative for more information

## New Features & Enhancements

- **AI Security Access Control with User Access Policy:** For users with the AI Security Browser Plugin, the [User Access Policy](https://knowledge.catonetworks.com/docs/configuring-the-ai-security-user-access-policy) gives you granular control over access to AI applications. This helps you reduce risky AI usage and guide users to approved alternatives.
  - Configure user notifications that warn users, require acknowledgment, or redirect them to an approved AI application
  - AI Security for Users license required (show me the [User Access Policy page](http://cc.catonetworks.com/#/account/me/endUsersProtectionsAccessPolicy))
- **Agents Overview for Local AI Activity:** AI Security helps you monitor local agent usage, policy outcomes, top users, tools, MCP servers, and violations from a single page.
  - Drill down to Agent Inventory and Agent Sessions pages
  - AI Security for Users license required
- **Visibility for Claude Agent Skills:** Identify the skills used in Claude agent sessions to investigate unapproved or malicious activity in the Skills tab on the Local Agents page.
  - Inspect details for the skill content, source, repository, and file path
  - Filter sessions by detected skill
  - AI Security for Users license required (show me the [Local Agents page](https://externallink.cc.catonetworks.com/#/account/me/agentsLocalAgents))
- **Client Notifications for AI Security User Interaction Policy:** Inform remote users when access to public AI applications is blocked.
  - The same notification messaging is used for Clients and the browser plugin
  - AI Security for Users license required
- **CMA Report for AI Security for Users:** We are adding a report that provides insights and highlights AI usage and interactions. You can generate it on demand or schedule it to run automatically (show me the [Reports page](https://externallink.cc.catonetworks.com/#/account/me/reports)).
- **Improved Visibility for AI Security Data Sovereignty:** Choose where sensitive AI Security data, including prompts, is stored for your account.
  - **Cato Storage** - stores data automatically in the region closest to where it was processed
  - **Account Storage** - writes data to your AWS S3 or Azure Blob Storage
  - No impact on existing AI Security data integrations settings, they are shown in the Data Sovereignty page
  - AI Security for Users or AI Security for Applications license required
- **Access Overview Enhancements:** The **Access Overview** [page](https://knowledge.catonetworks.com/docs/using-the-access-overview-page) now provides deeper visibility into user access behavior. You can analyze connection methods, accessed resources and applications, geographic access trends, and policy enforcement outcomes, helping you identify unusual patterns and investigate issues more efficiently. (Show me the [Access Overview page](https://externallink.cc.catonetworks.com/#/account/me/usersDashboard))
- **Add Connection Origin to the Client Connectivity Policy:** To enforce more granular [Client Connectivity Policies](https://knowledge.catonetworks.com/docs/configuring-the-client-connectivity-policy), you can define the **Connection Origin** for each rule. This lets you apply different rules based on how users connect to Cato.
  - Supported connection origins are Site, Client, Browser Extension, and Cato Browser.
- **Support for RSA SSO:** We added [RSA](https://knowledge.catonetworks.com/docs/configuring-rsa-sso) as an SSO provider for authenticating Cato Management Application (CMA) admins and remote users (supported in the Client, Browser Extension, and Enterprise Browser).

## Security Updates

- **Apps Catalog**

View more details about apps in the [Apps Catalog](https://knowledge.catonetworks.com/docs/using-the-app-catalog).
  - New Apps: 6 new apps: Puppet, SaltStack, WSUS, MammothCyber, PostHog, pCloud.com
- **IPS Signatures**

View more details about the IPS signatures and protections in the [Threats Catalog](https://knowledge.catonetworks.com/docs/using-the-threat-catalog).
  - CVE-2026-6875 (New)
  - CVE-2026-56164 (New)
  - CVE-2026-50522 (New)
  - CVE-2026-50518 (New)
  - CVE-2026-48276 (New)
  - CVE-2026-48313 (New)
  - CVE-2026-48282 (New)
  - CVE-2026-34909 (New)
  - CVE-2026-34908 (New)
  - CVE-2026-5027 (New)
  - CVE-2026-34910 (New)
  - CVE-2026-7482 (New)
  - CVE-2026-33439 (New)
  - CVE-2026-4747 (New)
  - CVE-2026-22557 (New)
  - CVE-2026-25049 (New)
  - CVE-2025-24963 (New)
- **Application Control Policy**
  - CASB
    - Adding conversation detection for CASB bing_ai (Enhancement)
  - Granular Apps
    - Gmail Add Attachment - split phase 1 into internal metadata_detector (Enhancement)
    - Gitlab login (New)
    - Salesforce granular actions for both classical and lightning (Enhancement)
- **TLS Inspection**
  - Puppet bypass (New)
  - Bypass Fathom.video (New)
  - Wiz Sensor Bypass (New)
  - New bypass rule for HP app (New)
  - New Bypass rule for Palo Alto Cortex XDR Traps (New)
  - Narrow TLS inspection bypass for broken HP (New)
- **Dynamic Prevention**
  - Detected Source IP Downloading Offensive/Hacking Tools, Limiting Command and Control, Lateral Movement, Data Exfiltration and Discovery (New) - Added 82 new controls
  - Detected Source IP Using Scanning Tools, Limiting Lateral Movement, Command and Control and Discovery (New) - Added 48 new controls
  - Detected Connection to Malicious IP with Low Reputation Score, Limiting Lateral Movement, Command and Control, Data Exfiltration and Discovery (New) - Added 85 new controls
  - Detected Source IP Accessing Multiple Low Reputation Malicious Domains, Limiting Lateral Movement, Discovery, Command and Control and Data Exfiltration (New) - Added 88 new controls
  - Detected Source IP Downloading Offensive/Hacking Tools, Limiting Command and Control, Lateral Movement, Data Exfiltration and Discovery (Enhancement) - Condition detection enhanced
  - Detected Source IP Downloading Binaries via CLI Clients from Low-Reputation Sources, Limiting Lateral Movement, Discovery, Command and Control and Data Exfiltration (New) - Added 77 new controls
  - For the full control list, please refer to the Threat Catalog in the CMA.
- **XDR Indications of Attack**
  - Known Malicious Domain Communication (New)
- **Application Control Via API and Data Protection API Integrations**

The enhancements were made for [Application Control Via API](https://knowledge.catonetworks.com/docs/application-control-via-api-with-app-activities)
  - Atlassian
    - SaaS Alerts (Enhancement)
      - Enriched alert descriptions with dynamic actor context
      - Consolidated overlapping admin-privilege-grant alerts into a single alert type
  - Azure AD
    - SaaS Alerts (Enhancement)
      - Enriched alert descriptions with dynamic actor context
      - Removed a redundant role from the global-admin-escalation alert to cut false positives
    - Third Party Apps (Enhancement)
      - Added newly cataloged app IDs (July Studio batch) to third-party app discovery
  - Box
    - SaaS Alerts (Enhancement)
      - Refined alert descriptions and logic
  - Cisco Meraki
    - Network Infrastructure (Enhancement)
  - Dropbox
    - SaaS Alerts (Enhancement)
      - Enriched alert descriptions with dynamic actor context
  - GitHub
    - SaaS Alerts (Enhancement)
      - Refined alert descriptions and logic
  - Google Drive
    - SaaS Alerts (New)
      - Added new alert coverage: public-web exposure, cross-domain sharing, ownership changes, external file sharing/emailing, and script trigger creation
  - Microsoft General
    - SaaS Alerts (Enhancement)
      - Enriched alert descriptions with dynamic actor context
  - Microsoft Exchange
    - SaaS Alerts (Enhancement)
      - Enriched alert descriptions with dynamic actor context
  - Salesforce
    - SaaS Alerts (Enhancement)
      - Replaced generic encryption-change alerts with more precise tenant-secret export/destroy alerts
      - Retired the admin login-as-impersonation and sandbox-creation alerts
  - SentinelOne
    - EDR (Enhancement)
      - Fixed EDR incident resource capping so large incidents (100+ resources) preserve process context and connected resources instead of dropping them, preventing incomplete incident graphs
  - SharePoint
    - SaaS Alerts (Enhancement)
      - Refined alert descriptions
  - Slack
    - SaaS Alerts (Enhancement)
      - Refined alert descriptions
      - Removed the Denial of Service alert
  - Zendesk
    - SaaS Alerts (Enhancement)
      - Refined alert descriptions
      - Consolidated authentication-change alerting into a single alert

**Note:** Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](https://support.catonetworks.com/hc/en-us/articles/11968052021277-Understanding-Cato-s-Gradual-Rollout). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
