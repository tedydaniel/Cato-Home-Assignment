---
title: "Product Updates - Aug. 31, 2026"
slug: "product-updates-aug-31-2026"
updated: 2026-08-31T11:45:42Z
published: 2026-08-31T11:45:42Z
canonical: "knowledge.catonetworks.com/product-updates-aug-31-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - Aug. 31, 2026

## New Features & Enhancements

- **New macOS Client v6.1:** During the week of Aug. 30, 2026, we are rolling out [macOS Client version 6.1](https://knowledge.catonetworks.com/docs/summary-of-cato-macos-client-releases). This version includes bug fixes, security enhancements, and stability improvements.
- **New iOS Client v5.9:** During the week of Aug. 30, 2026, the [iOS Client version 5.9](https://knowledge.catonetworks.com/docs/summary-of-cato-ios-client-releases) will be uploaded to the App Store. This version includes stability improvements, security updates, and bug fixes.
- **New Android Client v5.6.2:** During the week of Aug. 30, 2026, [Android Client version 5.6.2](https://knowledge.catonetworks.com/docs/summary-of-cato-android-client-releases) will be uploaded to the Google Play Store. This version includes stability improvements, security updates, and bug fixes.
- **More Socket Health Data in Experience Monitoring**: Add Socket health context to your analysis with new hardware, port, and flow metrics in [Experience Monitoring](https://knowledge.catonetworks.com/docs/the-site-experience-monitoring-drill-down-page).
  - Metrics include memory usage, flow counts and rates, per-port packet rates, and Socket uptime
  - Supported from Socket v27 and higher
  - DEM license required

- **Gradual Rollout of Socket Minor Versions:** We are starting to gradually roll out the following minor versions of Socket v26 and v27, including enhancements and bug fixes:
  - [v26.0.24087](https://knowledge.catonetworks.com/docs/socket-version-26-0-release-notes)
  - [v27.0.23945](https://knowledge.catonetworks.com/docs/socket-version-27-0-release-notes)
  - No customer action is required
- **Concurrent Editing for the Network Rules Policy:** The [Network Rules](https://knowledge.catonetworks.com/docs/configuring-network-rules) policy now supports multiple unpublished [revisions](https://knowledge.catonetworks.com/docs/working-with-policy-revisions) and concurrent editing.
  - Multiple admins can modify the policy in parallel without conflicts
  - Each admin can maintain independent drafts and publish them when ready
- **Devices Overview - Monitor Connected Device Count Over Time:** Track changes in the number of devices detected across your network directly from the [Overview](https://knowledge.catonetworks.com/docs/using-the-device-overview) tab in the Devices page.
  - Identify sudden changes in connected devices to detect potential security events or network changes
  - Estimate capacity planning and license management
  - Assets Security license required (show me the [Devices page](https://externallink.cc.catonetworks.com/#/account/me/devices))
- **Device Confidence Level Provides Visibility into Classification:** Understand the [estimated accuracy](https://knowledge.catonetworks.com/docs/what-is-device-inventory#understanding-device-confidence1) for Cato to identify and classify each device. For example, devices with a high **Confidence Level** are based on multiple discovery sources.
  - Assets Security license required (show me the [Devices page](https://externallink.cc.catonetworks.com/#/account/me/devices))
- **Multiple NICs Support in Device Inventory:** For devices with multiple network interfaces (NICs), the [Device Inventory](https://knowledge.catonetworks.com/docs/using-the-device-inventory-page) tab shows all MAC addresses, IP addresses, and networks for the device.
  - Hover over an item to show all the data for the device
  - Assets Security license required (show me the [Devices page](https://externallink.cc.catonetworks.com/#/account/me/devices))
- **Near Real-Time Entra ID Stories in XOps**: Investigate Entra ID-based issues faster as Cato XOps processes stories from the Entra ID connector in near real time.
  - XOps license and Microsoft Entra ID connector required
- **Upcoming Stricter Schema Type Validation for Cato API:** The Cato API now enforces stricter type validation to align with the documented schema. Review the [Potentially Breaking Changes](https://knowledge.catonetworks.com/docs/cato-api-potentially-breaking-changes-and-eol) article to verify that your API calls are not impacted.
- **Amazon Bedrock AgentCore Support for Managed Agents**: Discover Amazon Bedrock AgentCore agents with the Amazon Bedrock integration in AI Security, and review them on the **Managed Agents** page.
  - Supports no-code harness agents and custom code agents
  - Shows harness agent details including session history, system prompt, model, and tools
  - Existing Amazon Bedrock integrations require reinstalling the CloudFormation stack for the new read-only permissions
  - AI Security for Apps license required
- **Enhancement for Microsoft Foundry Managed Agents:** Cato now supports monitoring activity from Microsoft Foundry agents for greater visibility into agent interactions for investigation and analysis.
- **CMA Navigation Change:** All accounts will now use the new navigation for the Cato Management Application (CMA). The navigation toggle will be removed.

### PoP Announcements

- **Brisbane, AU:** A new Cato PoP location is now available in Brisbane with the range 113.30.139.0/24.
- **London, UK:** A new range (159.117.244.0/24) is now available for the London PoP location.

### Security Updates

- **Apps Catalog**

View more details about apps in the [Apps Catalog](https://support.catonetworks.com/hc/en-us/articles/7603867737885-Using-the-App-Catalog).
  - New Apps: 24 new apps - .NET Fiddle, 2go Mobile, Astrill VPN, Bansou SMS, Callsign Sony, CentOS Pastebin, Chateagratis.net, CodeBeautify, Codeshare, ControlC · Pastebin, CyberPower PowerPanel, Files.com, JS Bin, JSFiddle, JustPaste.it, KUZEN Support, NetSupport, Notes, PKSHA ChatAgent, Smile Bonus, Team Techo, UOL Chat, bpaste, openSUSE Paste
  - Enhanced Apps:
    - Backlog
      - Added domain **backlog.com**
    - Datto RMM (centrastage)
      - Updated app domains
    - Keeper Security, Inc.
      - Added domains **keeper.io**, **keepersecurity.ca**, **keepersecurity.com.au**, **keepersecurity.eu**, **keepersecurity.jp**, **keepersecurity.us**
    - NotebookLM
      - Added domains **notebook.google**, **notebook.google.com**
    - Windows Update Delivery Optimization (Swarm Protocol)
      - Signature Updated
  - Category Changes:
    - Chat and IM
      - Added app: Chai-Research
  - These are the updates for Socket apps, from Socket v25
    - Modified 1 app
      - Windows Update Delivery Optimization (Swarm Protocol) - Signature updated
- **IPS Signatures**

View more details about the IPS signatures and protections in the [Threats Catalog](https://support.catonetworks.com/hc/en-us/articles/10055007301149).
  - CVE-2024-40422 (New)
  - CVE-2024-56511 (New)
  - CVE-2025-10230 (New)
  - CVE-2025-2636 (New)
  - CVE-2025-64328 (New)
  - CVE-2026-16723 (New)
  - CVE-2026-2614 (New)
  - CVE-2026-33497 (New)
  - CVE-2026-45695 (New)
  - CVE-2026-46442 (New)
  - CVE-2026-47301 (New)
  - CVE-2026-47670 (New)
  - CVE-2026-53787 (New)
  - CVE-2026-54236 (New)
  - CVE-2026-55040 (New)
  - CVE-2026-66066 (New)
  - Detected Source IP Communicating with Known Malicious IPs or Domains from Threat Feeds, Limiting Lateral Movement, Command and Control, Discovery and Data Exfiltration (New) - Added 78 new controls
- **Device Inventory**

These are the updates to the [Device Inventory](https://support.catonetworks.com/hc/en-us/articles/14529548359709-Using-the-Device-Inventory) detection engine:
  - IoT
    - Multifunction Device
      - Canon imageRUNNER ADVANCE {hw.model} (New)
      - Fujifilm {hw.family} {hw.model} (New)
      - Ricoh IM {hw.model} (New)
      - Ricoh MP {hw.model} (New)
      - Sharp BP Series {hw.model} (New)
      - Toshiba (Enhancement)
        - New signals added
        - Metadata Updated
    - Printer
      - Argox (New)
      - Fujifilm {hw.family} {hw.model} (New)
      - Ricoh P {hw.model} (New)
      - Ricoh SP {hw.model} (New)
      - SATO Label Printer {hw.model} (New)
      - UTAX UTAX Printing System (New)
      - Zebra Label Printer {hw.model} (New)
      - Dell (Enhancement)
        - New signals added
        - Metadata Updated
      - Honeywell Thermal Label Printer {hw.model} (Enhancement)
        - New signals added
      - HP (Enhancement)
        - New signals added
      - SATO (Enhancement)
        - New signals added
    - Wireless Controller
      - Aruba Networks {hw.model} Mobility Controller (New)
  - Networking
    - Firewall
      - Cisco Firepower Threat Defense (New)
    - Gateway
      - Aruba Networks {hw.model} Branch Gateway (New)
    - Network Management Device
      - Eaton Gigabit Network Card (New)
    - Router
      - Fujitsu Si-R {hw.model} (New)
      - MikroTik (Enhancement)
        - New signals added
    - Switch
      - Arista Networks (New)
      - Buffalo (New)
      - Cisco Catalyst {hw.family} {hw.model} (New)
      - Dell Networking {hw.model} (New)
      - HPE Instant On {hw.model} (New)
      - Hitachi (New)
      - Aruba Networks (Enhancement)
        - New signals added
      - Cisco (Enhancement)
        - New signals added
        - Metadata Updated
      - Extreme Networks (Enhancement)
        - New signals added
        - Metadata Updated
      - HPE (Enhancement)
        - New signals added
        - Metadata Updated
      - Switch (Enhancement)
        - New signals added
      - TP-Link (Enhancement)
        - New signals added
    - UPS
      - Eaton {hw.family} {hw.model} (New)
      - UPS (Enhancement)
        - New signals added
        - Metadata Updated
    - WAP
      - Aruba Networks Aruba AP-{hw.model} (New)
      - Buffalo (New)
      - Buffalo AirStation {hw.model} (New)
      - Extreme Networks (New)
      - Ruckus (New)
      - Cisco (Enhancement)
        - New signals added
        - Metadata Updated
      - Linksys (Enhancement)
        - New signals added
      - Ubiquiti (Enhancement)
        - New signals added
  - OT
    - Industrial Switch
      - Cisco Industrial Ethernet {hw.model} (New)
  - Server
    - AAA Server
      - Cisco Identity Services Engine (New)
    - NAS
      - Buffalo TeraStation {hw.model} (New)
    - Print Server
      - Print Server (Enhancement)
        - New signals added
        - Metadata Updated
- **TLS Inspection**
  - TLS bypass of Trend Micro (New)
- **XDR Indications of Attack**
  - Threat Prevention
    - Periodic DNS Beaconing to Suspicious C2 Domains (New)
  - Anomaly Detection
    - First Occurrence of Login from Suspicious IP by User (New)
    - First Seen Successful Login from New Country and OS by User (New)
    - Abnormal Data Upload Activity to Evasive Port 80 Application (New)
    - First Seen Ping Sweep Activity By User (New)
    - First Occurrence of temp.sh DNS Query From Site (New)
    - First Occurrence of temp.sh Domain Communication From Site (New)
- **Application Control Via API and Data Protection API Integrations**

The enhancements were made for [Application Control Via API](https://support.catonetworks.com/hc/en-us/sections/24373046669085-Application-Control-via-API-with-App-Activities)
  - Dropbox Activities
    - Added detections for EMM policy weakening, folder join/link/sharing restriction loosening, group creation policy loosening, link expiration removal, and top-level content policy loosening (Enhancement)
  - Azure AD Anomalies
    - Added detections for Conditional Access policy creation/weakening/bypass, secure sign-in session control, authentication method removal, guest privileged role assignment, lockout threshold weakening, and reenabled security settings (tenant creation, security group creation, email subscription signup) (Enhancement)
  - Box Anomalies
    - Added detections for Content Workflow Policy Violation, Device Trust Check Failed, and File Exposed Publicly (Enhancement)
  - Cyera DSPM
    - Fixed risk description rendering to convert HTML-encoded content and paragraph/block tags to plain text (Enhancement)
  - GitHub Anomalies
    - Added detections for default repo permission elevation, member repo deletion enablement, org code scanning disablement, outside collaborator invite loosening, private vulnerability reporting disablement, and secret scanning push protection disablement (Enhancement)
  - Google Drive Anomalies
    - Added detections for shared drive copy restriction removal, folder sharing loosening, non-member access enablement, and reader download enablement (Enhancement)
  - Microsoft General Anomalies
    - Added detection for Copilot indirect prompt injection (Enhancement)
  - Microsoft Intune Device
    - Improved accuracy of IP address pairing with network interface MAC addresses (Enhancement)
  - Microsoft Exchange Anomalies
    - Added detection for email-hiding inbox rules (Enhancement)
  - Salesforce Anomalies
    - Added detection for potential SOQL/SOSL injection attempts (Enhancement)
  - SharePoint Anomalies
    - Added detection for idle session sign-out disabled (Enhancement)
  - Slack Anomalies
    - Added detection for external shared channel connections (Enhancement)

**Note:** Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](https://knowledge.catonetworks.com/docs/understanding-rollout-to-the-cato-cloud). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
