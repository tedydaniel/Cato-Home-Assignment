---
title: "Product Updates - June 22, 2026"
slug: "product-updates-june-22-2026"
updated: 2026-06-29T13:07:16Z
published: 2026-06-29T13:07:16Z
canonical: "knowledge.catonetworks.com/product-updates-june-22-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - June 22, 2026

## New Features & Enhancements

- **Upgraded CMA Admin Experience Enabled by Default**: The upgraded Cato Management Application (CMA) admin experience is the default view for admins. This experience helps you focus on the CMA pages most relevant to your use case, with no impact to RBAC permissions or direct page links.
  - Admins can continue to toggle between the upgraded experience and the previous experience
- **Coming Soon - Start with Ask AI for Faster Support**: Starting June 28, when you click **Submit a Request** in the Knowledge Base, the AI Workspace in the Cato Management Application automatically opens in a new tab. Describe what you need help with, and the Ask AI assistant helps you resolve issues faster with guided answers, account context, and relevant Knowledge Base articles.
  - Describe the issue to Ask AI to get the answers you need
  - Open a Support ticket from Ask AI when additional help is needed
- **New Android Client v5.6:** Android Client version 5.6 will be uploaded to the Google Play Store during the week of June 21, 2026. This version includes:
  - To ensure stable Always-On connectivity, the Client displays an in-app message when Android Battery Optimization is enabled to advise users to disable it
  - For managed deployments:
    - Suppress displaying the EULA to users
    - Set the default browser for authentication
  - Bug fixes, security enhancements, and stability improvements
- **New macOS v5.13.1:** During the week of June 21, 2026, we are rolling out macOS Client version 5.13.1. This version includes bug fixes, security enhancements, and stability improvements.
- **Enforce Policies for Unclassified AI Tools and MCPs**: Strengthen your AI security posture by blocking tools and MCPs that aren’t explicitly approved. We enhanced the AI Coding Agents Policy to include the new **Unclassified** approval status, which helps prevent new or unknown tools from running automatically.
  - AI Security for Users license is required
- **Simplified Actions for CASB and DLP Policies:** To make policy configuration clearer, Application Control (CASB) and Data Control (DLP) rules now support only **Allow** and **Block** actions.
  - We removed the **Monitor** action, instead select the **Allow** action and enable event tracking (to monitor user actions) for the rule
  - No impact on existing rules
- **Multi-Hop BFD Support for BGP Peers**: For greater flexibility for BGP deployments where peers are not directly connected, you can configure multi-hop BFD for BGP peers on IPsec and Cloud Interconnect sites. This improves routing resilience across more complex network topologies.
- **Simplified Experience for Local Agents**: We enhanced the deployment and monitoring of protection for local AI coding tools in the CMA. Agent Controls, formerly hooks, are now managed together with Scout from a single page, with the option to monitor only or enable enforcement.
  - AI Security > Scout includes the functionality of the previous Hooks page
  - No impact on existing hooks deployments
  - Use the AI Security > Agent Session page to monitor Agent Control activity
  - AI Security for Users license required
- **Export XOps Stories Workbench Data:** Export XOps story data to a CSV file from the Stories Workbench page for offline analysis, reporting, and collaboration.
  - Requires an XOps license
- **Bulk Edit Sockets & Accessories Shipping:** Save time when managing hardware shipments by updating multiple orders at once from the **Shipping** tab on the **Sockets & Accessories** page.

## Security Updates

- **Apps Catalog**

View more details about apps in the Apps Catalog.
  - New Apps: 6 new apps - ArcSight, Devo Security Data Platform, Graylog, Gurucul, NetWitness, Securonix
  - Enhanced Apps:
    - 8x8
      - Updated app IPs
    - Gemini
      - Updated app domains
      - Added domains [**appsgenaiserver-pa.clients6.google.com**](http://appsgenaiserver-pa.clients6.google.com), [**gemini.gstatic.com**](http://gemini.gstatic.com)
    - Microsoft Copilot
      - Updated app domains
    - Microsoft Office365
      - Updated app domains
    - These are the updates for Socket apps, from Socket v25
      - Modified 1 apps
      - 8x8 - Modified app IPs
- **Application Control Policy / CASB**
  - Instagram
    - Delete post (Enhancement)
    - Edit profile (form load) (Enhancement)
    - Like post (Enhancement)
    - Logout (Enhancement)
    - Share story (DM) (Enhancement)
    - Unsend DM message (Enhancement)
  - YouTube
    - Share (Enhancement)
    - Post (Enhancement)
    - Like (Enhancement)
    - Upload image (Enhancement)
    - Delete video (Enhancement)
    - Logout (Enhancement)
    - Delete video (Enhancement)
    - Logout (Enhancement)
    - Download video (Enhancement)
- **IPS Signatures**

View more details about the IPS signatures and protections in the Threats Catalog.
  - CVE-2025-32395 (New)
  - CVE-2026-32746 (New)
  - CVE-2026-35273 (New)
  - CVE-2026-41103 (New)
- **XDR Indications of Attack**
  - Threat Prevention
    - Automated Suspicious Activity (New)
  - Anomaly Detection
    - First Occurrence of WinRM Connection (New)
- **Device Inventory**

These are the updates to the Device Inventory detection engine:
  - IOT
    - Environmental Sensor
      - Dickson Environmental Sensor (New)
      - Hygiena Environmental Sensor (New)
  - SERVER
    - Server
      - Cisco UCS Server (New)
    - Storage
      - HPE Nimble Storage (New)
  - PC
    - Printer
      - Lexmark Printer (New)
      - HP Printer (New)
- **Application Control Via API and Data Protection API Integrations**

The enhancements were made for Application Control Via API
  - Dropbox
    - Activity (Enhancement) - Improved access-method detection in activity events, including handling for tagged objects and better null handling
    - Anomalies (Enhancement) - Clearer anomaly detection descriptions covering impersonation, unauthorized access, and account-security risks
  - GitHub
    - Anomalies (Enhancement) - Clearer anomaly detection descriptions covering impersonation, unauthorized access, and malicious-activity indicators
  - Cisco Meraki
    - Network Infrastructure (Enhancement)
  - Microsoft Teams
    - Experience (Enhancement) - Added per-call participant aggregation for richer call-quality data to support Microsoft Teams API changes
  - Microsoft Defender
    - EDR (Enhancement)

**Note:** Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this article. See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
