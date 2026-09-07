---
title: "Product Updates - March 2, 2026"
slug: "product-updates-march-2-2026"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-march-2-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - March 2, 2026

## New Features & Enhancements

- **Securely Connect to Private Applications Using App Connectors**: Establish outbound connections to the Cato Cloud using [App Connectors](/v1/docs/what-is-cato-private-access), enabling identity-driven, least-privileged access with centralized inspection and enforcement.
  - Publish private applications using FQDNs or domains without inbound firewall changes
  - Enforce Zero Trust access with identity- and context-based Private Access Policy rules
  - Broker all user-to-app traffic through the nearest Cato PoP with centralized inspection
  - Deploy App Connectors as lightweight virtual machines or physical Sockets in on-premises or cloud environments
- **LAN IPS Enforcement on Cato Sockets**: Protect LAN traffic behind your sites by enforcing [IPS directly on Sockets](/v1/docs/configuring-ips-in-the-lan). This extends Threat Prevention to LAN traffic, enabling immediate, local enforcement without sending traffic to the Cato Cloud, and helps maintain low latency for internal communications.
  - Enable LAN IPS at the account level and define which sites enforce it
  - Configure per-site enforcement modes:
    - Block to actively prevent malicious traffic
    - Monitor to detect and log threats without blocking
- **Updated X1600 Socket Hardware for Wi-Fi Support:** We are introducing [integrated Wi-Fi support](/v1/docs/configuring-and-monitoring-socket-wi-fi-networks) for the X1600 Socket family. The models X1600 and X1600 5G are available with the option for built-in Wi-Fi 6, eliminating the need for an external access point.
  - Dual-band 2.4/5 GHz, up to 4 SSIDs, and PSK authentication option
  - Full WLAN configuration and analytics in the CMA - SSID settings and visibility for connected hosts, signal quality, and real-time utilization
- **End-to-End Post-Quantum Cryptography:** Strengthen your organization’s crypto-agility and long-term security posture by preparing remote access, site-to-site IPsec tunnels, and TLS inspection for quantum-era threats. This unified enhancement introduces quantum-resistant key exchange for underlay traffic for Clients and IPsec sites. Post-Quantum Cryptography (PQC) capabilities in TLS inspection let you monitor and manage your gradual transition toward full post-quantum encryption.
  - **Client**
    - Enable [PQC for all traffic between the Client and the PoP](/v1/docs/what-is-pqc-for-the-cato-client) to strengthen the cryptographic handshake
    - Protect remote access traffic against future quantum-computing threats
    - Supported for Windows Client v6.0 and higher
  - **IPsec**
    - Configure PQC-capable [IKEv2 negotiation for IPsec tunnels](/v1/docs/what-is-pqc-for-ipsec-tunnels) using a hybrid-first approach to maintain interoperability while introducing quantum-resistant key exchange
    - Extend PQC configuration support to IPsec APIs and AccountSnapshot fields for programmatic management
    - Manage cryptographic settings consistently across tunnels without adding operational complexity
  - **TLS Inspection**
    - Log PQC-related [TLS parameters](/v1/docs/what-is-pqc-for-tls-inspection) for client and server connections, including key exchange and digital signature algorithms
    - Monitor PQC adoption across your environment to track progress toward full quantum-resistant encryption
    - Enforce the use of PQC or Hybrid-PQC encryption algorithms to support crypto-agility and long-term security posture
- **20 Gbps Throughput with the X1700C Socket:** We are introducing the new X1700C Socket as an additional hardware model for X1700 Socket sites.
  - The X1700C supports two optional add-ons: dual-100G (2×100G) and dual-25G (2×25G) modules
  - For supported configurations, the platform reaches up to 20 Gbps aggregate throughput
  - Pricing remains the same for all X1700 Socket models
  - Cato will continue to provide support for all X1700 Socket models, subject to the [EOS policy](/v1/docs/product-lifecycle-notice-end-of-support-for-cato-socket-hardware)
- **Introducing the Cato Remote MCP Server:** Access [Cato context from any MCP-compatible client](/v1/docs/working-with-the-cato-remote-mcp-server) to enrich custom AI workflows with real-time network and security insights. Everything is secured and managed by Cato, with no code required.
  - Requires a [Cato API key](/v1/docs/generating-api-keys-for-the-cato-api) and appropriate [admin permissions](/v1/docs/managing-admin-roles-using-rbac)
  - Operates with customer-provided LLM resources
- **IPv6 Socket Underlay Support:** Connect Socket sites to ISPs that deliver connectivity [using IPv6](/v1/docs/configuring-a-socket-site-for-ipv6-only-internet-connectivity), expanding deployment options in environments where IPv4-only underlay is not available.
  - Uses IPv4-over-IPv6 tunneling to support IPv4-dependent apps
  - Supports ISPs that provide IPv6-only or IPv6-first access
  - Configure in the Socket Web UI
- **Step-Up Authentication in Internet Firewall:** Cato supports step-up authentication for sensitive web resources by leveraging the [Confidence Level user attribute](/v1/docs/adding-device-conditions-to-firewall-rules) in Internet Firewall rules. This lets you enforce stronger user authentication before allowing access to sensitive web resources, such as a SaaS tenant.
  - Create rules that require a **High Confidence Level**, based on the user's current authentication context
  - When users don't meet the required level, a [dedicated block page](/v1/docs/creating-user-notification-templates) guides the users to reauthenticate with the Cato Client
- **Posture Checks for Compliance Standards:** We have made the following enhancements to the [Posture page](/v1/docs/reviewing-posture-checks-for-your-account):
  - Posture Checks are mapped to leading compliance frameworks, helping you understand how Cato configurations support audit and regulatory requirements. Easily identify gaps and prioritize improvements based on compliance impact.
    - Supported compliance standards are ISO 27001:2022, NIST SP 800-53 Rev. 5, and GDPR
  - Each check includes AI-powered, step-by-step remediation guidance to accelerate resolution.
  - Renamed the Best Practice page to **Posture** and Best Practice checks to **Posture Checks**.
- **Device-based Criteria for Next Gen LAN Firewall Rules:** Apply the same device-based Criteria conditions available in Internet and WAN Firewall rules to [Next Gen LAN Firewall rules](/v1/docs/managing-the-socket-next-gen-lan-firewall-policy), letting you control routing and connectivity decisions based on device identity, posture, and context.
  - Apply device attributes such as OS, platform, manufacturer, and model
  - Use Device Posture Profiles to route traffic only for compliant devices (for example, encrypted disks or approved Cato Client versions)
  - Differentiate Next Gen LAN Firewall rules based on device location, origin (remote or behind a site), or device category (such as IoT/OT)
- **App Catalog Contains Additional Insights for Cloud Apps:** The [App Catalog](/v1/docs/using-the-app-catalog) now includes more details for cloud apps, such as threat intelligence data, and uptime and availability metrics. This enables you to make more informed and confident decisions when validating apps to be used in your organization.

- **Clearer Re-Authentication Prompt**: Improved messaging to coach users when access to applications is blocked due to an expired authentication token.
  - When [access to an application is blocked](/v1/docs/adding-device-conditions-to-firewall-rules) because the user’s token expired and the policy requires a high confidence level, Cato shows a [dedicated authentication block page](/v1/docs/creating-user-notification-templates)
  - The dedicated block page clearly indicates that re-authentication is required to restore access
  - Replaces the firewall block page previously shown in this scenario
- **Device Inventory Integration with Microsoft Defender:** Admins can enrich Cato’s Device Inventory with data from [Microsoft Defender](/v1/docs/microsoft-defender-configuring-the-device-management-integration). This integration adds additional device context, enabling more accurate classification and a clearer picture of connected assets. By combining endpoint insights from Microsoft Defender with Cato’s own discovery, admins gain better visibility and precision in identifying devices across the network.
  - IoT/OT Security license is required
- **Turnkey Integration with CrowdStrike Falcon Next-Gen SIEM:** Streamline operations by automatically forwarding Cato events to [CrowdStrike](/v1/docs/integrating-cato-events-with-crowdstrike) for unified monitoring and analysis. The built-in integration:
  - Reduces setup time and eliminates the need for custom scripts or connectors
  - Uses predefined event mapping to CrowdStrike to simplify configuration in the CMA
  - Enhances visibility through centralized event management
- **Introducing XOps Account Operations Stories:**[Account Operations stories](/v1/docs/drilling-down-and-analyzing-xops-account-operations-stories-1) highlight systemic problems across directory services, connectivity, routing, and integrations, helping you identify issues sooner and restore normal operation using guided remediation.
  - Detect account-wide issues such as directory sync failures, IP conflicts, BGP prefix exhaustion, IPsec tunnel negotiation failures, and SaaS app connector disconnections
  - Use remediation playbooks in the CMA to troubleshoot and resolve issues more efficiently
  - The stories are generated by the new **Account Operations** producer
- **Packet Processing Time:** We now support a Packet Processing Time SLA of up to 10ms for HTTP and HTTPS traffic, as defined in the MSA and subject to its terms and exclusions. See [the MSA](https://www.catonetworks.com/msa/) for full terms and conditions.
- **CMA Enhancement - Experience Monitoring Highlights Bar**: Get instant, account-wide visibility into application experience, site connectivity, and DEM integration status with the highlights bar we added to the Experience Monitoring page.
  - Requires a DEM license
- **Browser Extension v1.6:** During the week of March 1, 2026, a [new Browser Extension version 1.6](/v1/docs/summary-of-browser-extension-releases) will be available in the Chrome Web Store, and includes improved performance fixes.

## PoP Announcements

- **New Localized IP Range Available for Kazakhstan:** The following localized IP range for Kazakhstan (serviced through the Helsinki PoP location) is now available:
  - **KZ:** 159.117.235.0/27
- New ranges are now available for these PoP locations:
  - **Marseille, FR:** 159.117.239.0/24
  - **Chennai, IN:** 113.30.132.0/24

## Security Updates

- **Apps Catalog**

View more details about apps in the [Apps Catalog](/v1/docs/using-the-app-catalog).
  - New Apps: 12 new apps – Action1 RMM, Alza, Applivery, ArborXR, Esper, Hexnode UEM, Miradore, Polymarket, Samsung Knox, Scalefusion, SimpleMDM, Syxsense Manage
  - Enhanced Apps:
    - 21Strategies
      - Modified name from **21Strategies Gmbh** to **21Strategies**
    - Microsoft Entra ID
      - Modified name from **Microsoft Entra ID (formerly Azure Active Directory)** to **Microsoft Entra ID**
    - One
      - Updated app domains
    - Samsung
      - Removed domains **samsungknox.com**, **secb2b.com**
  - Applications that are now available in Application Control rules: Workast, Walnut, UserGems, Timy, Tatsu, Stream Security, StatusGator, Standuply, Shufflet, Semgrep, Redash, Pylon, Polly, PollChamp, Peerbound, OpenPoll, NewReleases, Linear, BuzzSumo, Geekbot, 1VPN
  - Category Changes:
    - Business Systems:
      - Added app: SurveyPlanet
    - Generative AI Tools:
      - Removed app: SurveyPlanet
    - Productivity:
      - Removed app: SurveyPlanet
- **IPS Signatures**

View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - CVE-2019-19006 (New)
  - CVE-2024-6250 (New)
  - CVE-2025-12420 (New)
  - CVE-2025-12480 (New)
  - CVE-2025-14528 (New)
  - CVE-2025-15503 (New)
  - CVE-2025-4078 (New)
  - CVE-2025-6205 (New)
  - CVE-2026-1603 (New)
  - Malware - Phantom - CnC Activity (New)
  - Malware - Kimwolf Botnet Command and Control Traffic (Enhancement)
  - Malware - MaliciousCorgi Extensions (New)
- **SAM Signatures**

These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
  - Discord Malicious Activity (New)
  - Suspicious Cursor Extension Download (New)
  - Downloading Files over Netlify Application (Enhancement)
- **Application Control Via API and Data Protection API Integrations**

The enhancements were made for [Application Control Via API](https://support.catonetworks.com/hc/en-us/sections/24373046669085-Application-Control-via-API-with-App-Activities)
  - SalesForce
    - App Activities - Support for ExternalClientApp Authentication (Enhancement)
  - Zoom
    - Experience (Enhancement)
  - Microsoft Defender
    - EDR (Enhancement)
  - Juniper Mist
    - WiFi Events (Enhancement)
  - Armis
    - Devices (Enhancement)
  - Intune
    - Devices (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
