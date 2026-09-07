---
title: "Product Updates - April 27, 2026"
slug: "product-updates-april-27-2026"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-april-27-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - April 27, 2026

## New Features & Enhancements

- **Create Internet Firewall Rules with Ask AI:** Save time and reduce manual work by describing the Internet Firewall rule you want in natural language.
  - Ask AI generates a proposed Internet Firewall rule for your review
  - After you approve the proposed rule, Ask AI creates the rule and then you can manually review and publish the policy
  - If the rule isn’t quite right, refine the request, and Ask AI generates a new version
- **Identify Data Sovereignty Requirements in App Traffic:** The Data Sovereignty map provides visibility into app traffic that may have data sovereignty implications, so you can quickly identify where regulated traffic is flowing and focus on AI-related activity when relevant.
  - Review app headquarters locations to understand potential data protection regulatory exposure by country
  - Monitor apps by traffic that are subject to data protection requirements
  - View PoP usage to see where your networking data is processed
- **Account-Level Socket Bypass Policy for FQDN-Based Applications**: Define account-wide rules to bypass trusted Internet traffic directly from Socket sites, including FQDNs and domains.
  - Supports FQDNs, domains, IPs, and custom apps as bypass destinations
  - Single, unified policy across sites with full API and event support (previously, Bypass Policy was only available per site)
  - Ideal for Windows Update, cloud backups, guest Wi-Fi, and similar use cases
  - Supported from Socket v25 and higher
- **Domain and FQDN Support for Client Split Tunnel Policy:** Use Domain and FQDN in Split Tunnel policies to include or exclude destinations. This provides a more flexible way to route traffic for remote users, particularly for SaaS services and Applications using dynamic public IPs.
  - Requires DNS Relay running on the device
- **Use Enterprise Browser or Browser Extension in Firewall Policies:** We are starting to gradually roll out the ability to enforce more granular Internet and WAN firewall policies based on how users access applications, and use the Cato [Enterprise Browser](/v1/docs/what-is-the-cato-enterprise-browser) and [Browser Extension](/v1/docs/what-is-the-cato-browser-extension) as the **Origin of the connection** for a rule. This helps you apply different controls for access paths while improving segmentation for sensitive applications.
- **Dynamic Prevention Events Contribute to User Risk Score:** To provide a more complete view of risky user behavior, block events triggered by Dynamic Prevention’s behavior-based security engine are incorporated into the user’s risk score.
  - Advanced Threat Protection license required
- **Starting Rollout of Socket v26:** We are starting to gradually roll out [Socket version 26](/v1/docs/socket-version-26-0-release-notes) to all customers, including firmware for new features, enhancements, and bug fixes.
  - No customer action is required
- **Take Remote User Remediation Actions in Ask AI:** As part of user investigation, within Ask AI you can adjust a user risk score or revoke their session without leaving the conversation.
  - Review the relevant user details before revoking the session or resetting the risk score
  - Admin approval is required before Ask AI completes the action
  - Supported in Ask AI and through the remote MCP server
- **Cisco Meraki Access Point Events in Experience Monitoring:** Integrate Wi-Fi access point events from [Cisco Meraki](/v1/docs/cisco-meraki-creating-the-experience-monitoring-connector) and correlate them with user experience data to improve troubleshooting of office connectivity issues.
  - Requires a DEM license and configuration of the Cisco Meraki connector
- **Control PII Visibility in the CMA with Data Obfuscation:** Reduce exposure to personally identifiable information (PII) while preserving access to relevant Cato Management Application (CMA) pages.
  - Obfuscate selected PII fields such as usernames and email addresses
  - Allow specific admins to view original data
  - Applies to pages that rely on events and application analytics data
- **XOps Integration with Sentra for Contextual Data Risk Visibility:** Integrate Sentra alerts with Cato XOps to generate stories that highlight sensitive data exposure, risky access patterns, and misconfigurations. This lets you leverage Sentra’s data classification, lineage analysis, and identity-aware access insights within the Stories Workbench.
  - Requires XOps license
- **New Indication for Predictive Insight Stories:** As part of the Cato Insights platform, XOps analyzes event generation trends to proactively alert when event quota limits are expected to be exceeded before it impacts visibility and operations. Stories are created with all relevant signals and recommended remediation actions.
  - Webhook notification is supported via the [Response Policy](/v1/docs/creating-the-response-policy-for-xops-stories)
  - Requires an XOps license
- **Linux Client v5.7:** Starting the week of April 26, 2026, we are rolling out the new Client [version 5.7](/v1/docs/summary-of-cato-linux-client-releases) for Linux. This version includes:
  - Stability improvements
  - Bug fixes
  - Security updates
- **Enhanced Account Experience Visibility in Experience Monitoring:** We improved the Experience Monitoring page with expanded account experience and performance views and a prioritized insights feed across your account sites, users, hosts, and applications.
  - Easily pivot between multiple performance views, including hardware metrics, Wi-Fi signal, application probes, and more
  - The new Feed widget highlights the latest network and performance insights across the account
  - The account-level experience score graph includes breakdown by sites and remote users
  - Requires DEM license
- **Event Timeline in Experience Monitoring Drill-Down Pages:** Correlate connectivity and security events with experience metrics in a unified timeline available in the site, user, and host drill-down pages.
  - Requires DEM license
- **Data Protection via API Support for Citrix ShareFile:** Ensure data protection and control over sensitive data within your [ShareFile](/v1/docs/citrix-sharefile-configuring-the-data-protection-api-connector) account. This connector provides visibility and control over user actions (for example, remove share) even when not connected to the Cato Cloud.
  - The ShareFile app is available from the **Integrations Catalog**, under **Data Protection**
  - SaaS Security API license required
- **Additional SSO Providers:** We added [PingOne](/v1/docs/configuring-pingone-identity-sso) and [Cisco DUO](/v1/docs/configuring-duo-sso) as [SSO providers](/v1/docs/single-sign-on) for authenticating admins and users (supported in the Client, Browser Extension, and Enterprise Browser).
- **Flows Data Source for Splunk Integration:** Extend visibility beyond discrete events with flow-based telemetry in the Cato [Splunk](/v1/docs/integrating-cato-data-with-splunk) push integration. This provides a session-level view of network activity and supports advanced traffic analytics and detection use cases.
  - Includes aggregated traffic flows enriched with application, user, and network context
  - Uses the [appStats schema](https://api.catonetworks.com/documentation/#query-appStats) with augmented metrics such as upstream/downstream bytes and packets (field availability may vary)
  - Aligns with Splunk CIM, including the Network Traffic model

## PoP Announcements

- We added the following new Cato PoP locations:
  - **Anchorage, US**
  - **Lisbon, PT**

## Security Updates

- **Apps Catalog**

View more details about apps in the [Apps Catalog](/v1/docs/using-the-app-catalog).
  - New Apps: 8 new apps A2A (Agent2Agent) Protocol, CADY, Jylo, Legora, Sentra, Tencent RTC, TypeWhisper, Zoom Apps
  - Enhanced Apps:
    - Progress ShareFile
      - Modified name from **Citrix ShareFile - File Transfer & Sharing** to **Progress ShareFile**
    - Glassdoor
      - Added detection expression
    - Legalon Technologies
      - Added domain **legalontech.com**
    - Threads
      - Added domain **threads.com**
- **Application Control Policy / CASB**
  - Telenet
    - Telenet - Upload (New)
    - Telenet - Send Mail (New)
  - NoteGPT
    - NoteGPT - Upload (New)
    - NoteGPT - Conversation (New)
  - GitHub
    - GitHub - Download (via browser) (New)
  - Gmail
    - Gmail - Send (New)
  - Microsoft Copilot
    - Microsoft Copilot - Login Third Party (New)
  - Snapchat
    - Snapchat - Login (New)
    - Snapchat - Login SSO (New)
    - Snapchat - Create Snap (New)
    - Snapchat - Send Message (New)
    - Snapchat - Logout (New)
  - Reddit
    - Reddit - Create Post (New)
    - Reddit - Upvote / Downvote (New)
    - Reddit - Edit Post (New)
    - Reddit - Delete (New)
    - Reddit - Logout (New)
    - Reddit - Media Upload (New)
    - Reddit - Manage Profile (New)
    - Reddit - Watch Video (New)
  - TikTok
    - TikTok - Login (New)
    - TikTok - Post Video (New)
    - TikTok - Like (New)
    - TikTok - Logout (New)
    - TikTok - Watch Video (New)
    - TikTok - Manage Settings (New)
    - TikTok - Delete Video (New)
    - TikTok - Comment (New)
    - TikTok - Manage Profile (New)
  - X (Twitter)
    - X (Twitter) - Login (New)
    - X (Twitter) - Third Party Login (New)
    - X (Twitter) - Delete Tweet (New)
    - X (Twitter) - Like (New)
    - X (Twitter) - Logout (New)
    - X (Twitter) - Manage Profile (New)
    - X (Twitter) - Change Language (New)
    - X (Twitter) - Retweet (New)
  - Weibo
    - Weibo - Login (New)
    - Weibo - Watch Video (New)
  - YouTube
    - YouTube - Channel Post (New)
    - YouTube - Like (New)
    - YouTube - Channel Image Upload (New)
    - YouTube - Share (New)
    - YouTube - Delete Video (New)
    - YouTube - Logout (New)
    - YouTube - Download Video (New)
  - LinkedIn
    - LinkedIn - Edit Post (New)
    - LinkedIn - Like (New)
    - LinkedIn - Delete Post (New)
    - LinkedIn - Repost (New)
    - LinkedIn - Logout (New)
    - LinkedIn - Manage Profile (New)
    - LinkedIn - Manage Settings (New)
    - LinkedIn - Watch Feed Video (New)
    - LinkedIn - Request Recommendation (New)
  - Facebook
    - Facebook - Share Post (New)
    - Facebook - Delete Post (New)
    - Facebook - Like (New)
    - Facebook - Upload Video (New)
    - Facebook - Play Video (New)
    - Facebook - Edit Profile (New)
    - Facebook - Edit Post (New)
  - Craigslist
    - Craigslist - Login (New)
    - Craigslist - Post (New)
    - Craigslist - Edit Post (New)
    - Craigslist - Upload Image (New)
    - Craigslist - Share (New)
    - Craigslist - Logout (New)
    - Craigslist - Manage Profile (New)
  - GitLab
    - GitLab - Login (New)
    - GitLab - Third Party Login (New)
  - Glassdoor
    - Glassdoor - Login (New)
    - Glassdoor - Login Third Party (New)
    - Glassdoor - Upload (New)
    - Glassdoor - Delete (New)
    - Glassdoor - Logout (New)
    - Glassdoor - Manage Profile (New)
  - Instagram
    - Instagram - Edit Profile (New)
    - Instagram - Like (New)
    - Instagram - Unsend Message (New)
    - Instagram - Delete Post (New)
    - Instagram - Share Story (New)
    - Instagram - Logout (New)
- **Data Loss Prevention**
  - Telenet - Upload (New)
  - Telenet - Send Mail (New)
  - NoteGPT - Upload (New)
  - NoteGPT - Conversation (New)
  - GitHub - Download (via browser) (New)
  - Gmail - Send (New)
  - YouTube - Channel Image Upload (New)
  - Facebook - Share Post (New)
- **IPS Signatures**

View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - CVE-2023-40924 (New)
  - CVE-2025-56819 (New)
  - CVE-2026-27483 (New)
  - CVE-2026-32201 (New)
  - CVE-2026-33340 (New)
  - Bot Activity Following Suspicious Activity (New)
  - Dnscat2 C2 Activity (New)
  - Explicit Content Access Following Suspicious Activity (New)
  - Impersonation of Legitimate Domain Following Suspicious Activity (New)
  - Malicious Payload Download Following Suspicious Activity (New)
  - Outbound Low Reputation Access Following Suspicious Activity (New)
  - Service Scan Activity Following Suspicious Activity (New)
  - Shortened URL Access Following Suspicious Activity (New)
  - Suspicious URL Access Following Suspicious Activity (New)
  - Tool Download Following Suspicious Activity (New)
  - Tool Transfer Following Suspicious Activity (New)
- **DNS Protection**
  - dns2tcp Activity (New)
- **SAM Signatures**

These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
  - High Velocity SMB Connections Across Hundreds of Destinations (New)
  - OpenClaw Agent Communicating with Low Reputation Domain (New)
  - OpenClaw Agent Communicating with Low Reputation IP (New)
  - OpenClaw Gateway Chat WAN (New)
  - OpenClaw Gateway Config URL WAN (New)
  - OpenClaw Gateway CSP Headers WAN (New)
  - OpenClaw Gateway JavaScript WAN (New)
  - SMB Anonymous Null Sessions Scanning (New)
- **XDR Indications of Attack**
  - Anomaly Detection
    - Massive Send activities by a user (New)
    - Massive SoftDelete activities by a user (New)
    - Massive HardDelete activities by a user (New)
- **Device Inventory**

These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
  - NETWORKING
    - Access Point
      - HPE Aruba (New)
- **Application Control Via API and Data Protection API Integrations**

The enhancements were made for [Application Control Via API](/v1/docs/application-control-via-api-with-app-activities)
  - Atlassian
    - Activity (Enhancement)
  - Azure AD
    - Activity (Enhancement)
    - Third Party Apps (Enhancement)
  - Microsoft General
    - Anomalies (Enhancement)
  - Salesforce
    - Activity (Enhancement)
    - Anomalies (New)
    - Third Party Apps (Enhancement)
  - Slack
    - Third Party Apps (Enhancement)
  - Zendesk
    - Anomalies (New)
  - Progress ShareFile
    - Activity (New)
  - Sentra
    - DSPM Alerts (New)
  - Cisco Meraki
    - WiFi events (New)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
