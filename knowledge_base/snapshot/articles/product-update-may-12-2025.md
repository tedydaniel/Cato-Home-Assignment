---
title: "Product Update - May 12, 2025"
slug: "product-update-may-12-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-may-12-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - May 12, 2025

## New Features & Enhancements

- **New Capabilities for Autonomous Policies:**
  - **Internet Firewall Best Practice Wizard**: We are introducing a new [Best Practice wizard](/v1/docs/using-the-internet-firewall-configuration-wizard) that guides you through the rule configuration process and helps ensure your policy follows best practices and AI-based insights. The wizard also lets you customize the rules to meet your organization’s needs without opening and editing the specific rules.
  - **New Internet and WAN Firewall Autonomous Best Practice Checks**: We are introducing new AI-based Autonomous Policy Insights for the [Internet](/v1/docs/what-is-the-cato-internet-firewall) and [WAN](/v1/docs/what-is-the-cato-wan-firewall) Firewall policies:
    - **Unused Rules**: Identifies firewall rules with an Allow action that have not generated any events in the past 30 days
      - Supported for the Internet and WAN Firewall policies
    - **Contradicting Rules Check**: Identifies firewall rules with identical predicates but different actions, which can create conflicts that prevent lower-priority rules from being applied
      - Supported for the Internet Firewall policy
    - Click [here](https://academy.catonetworks.com/autonomous-policy-wan-firewall) to watch a video recording of this feature

- **Introducing RPF AI-Driven Best Practices:** We expanded the AI-driven Best Practice checks and recommendations to include [Remote Port Forwarding (RPF)](/v1/docs/configuring-remote-port-forwarding-for-the-account) to provide actionable insights to optimize inbound access configurations. These Best Practices include identifying temporary rules, test rules, and expired rules, as well as data-driven recommendations for restricting potentially overly-permissive service exposure.
  - The checks are available on the Security > Remote Port Forwarding and Home > Best Practices pages
  - Click [here](https://academy.catonetworks.com/autonomous-policy-remote-port-forwarding) to watch a video recording of this feature

- **New Best Practices for Application Control & Data Protection:** We’ve added [Best Practices](/v1/docs/reviewing-posture-checks-for-your-account) checks to help you strengthen your security posture by correctly configuring your SaaS API integrations. You can view these checks from the Home > Best Practices page. The new checks are:
  - **App Activities via API (CASB):** Verifies that API integrations are configured correctly for your SaaS apps to extend CASB visibility into [App Activities via API](/v1/docs/what-is-application-control-via-api-with-app-activities)
  - **Policy Check for Data Protection via API (DLP):** Ensures the API integration is active and Data Protection policy rules are configured correctly to enable full [DLP Protection via API](/v1/docs/what-is-the-data-protection-api)

- **Cato Networks Terraform Provider:** Manage your account with Infrastructure as Code (IaC)-based automation with the [Cato Terraform provider](https://registry.terraform.io/providers/catonetworks/cato/latest). You can declaratively configure and maintain resources such as Socket sites, IPsec sites, WAN firewall rules, routing policies, and identity integrations directly in Terraform.
  - Integrate Cato’s global cloud network into CI/CD pipelines
  - Enforce consistent network and security policies across environments
  - Streamline provisioning of secure connectivity for cloud, data center, and branch locations
  - Cato [Terraform modules](https://registry.terraform.io/search/modules?q=cato) support most site deployments and topologies, including: physical Sockets for all models, virtual Sockets (AWS, Azure, GCP), single Socket and HA configuration
  - The provider supports both standalone usage and integration with Cato-certified Terraform modules for cloud deployments

- **Application Control via API Support for Slack**: Connecting SaaS apps to Cato lets you understand who is accessing each app and identify suspicious activities or trends even when users are not connected to the Cato Cloud. You can now connect your [Slack account](/v1/docs/slack-configuring-the-app-activities-integration) to provide visibility into user activities.
  - The Slack app is available from the **Integrations Catalog**, under App Activities
  - This feature requires a CASB license

## PoP Announcements

- New ranges are available for the following PoP locations:
  - **Manila, PH:** 123.253.155.0/24
  - **Tel Aviv, IL:** 216.252.187.0/24
- New ranges will soon be added to these PoP locations:
  - **Marseille, FR:** 159.117.225.0/24
  - **Milan, IT:** 159.117.227.0/24
  - **Paris, FR:** 159.117.224.0/24
  - **Zurich, CH:** 159.117.226.0/24

## Security Updates

- **IPS Signatures:**
  - View more details about the IPS signatures and protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog):
    - CVE-2015-2974 (New)
    - CVE-2018-7445 (Enhancement)
    - CVE-2020-10826 (New)
    - CVE-2020-10827 (New)
    - CVE-2020-10828 (New)
    - CVE-2021-28474 (New)
    - CVE-2024-23721 (New)
    - CVE-2024-30568 (New)
    - CVE-2024-37393 (New)
    - CVE-2024-41593 (New)
    - CVE-2024-57046 (New)
    - CVE-2025-1685 (New)
    - CVE-2025-1974 (New)
    - CVE-2025-27480 (New)
    - CVE-2025-29306 (New)
    - CVE-2025-29793 (New)
    - CVE-2025-31324 (New)
    - CVE-2025-32433 (New)
    - CVE-2025-3248 (New)
    - CVE-2025-34028 (New)
    - Fake Browser Update (New)
    - Ptunnel Pingtunnel Activity (New)
    - Ransomware - AnarchyRansom (Enhancement)
    - Ransomware - Anubi (Anubis) (Enhancement)
    - Ransomware - BlackHeart (MedusaLocker) (Enhancement)
    - Ransomware - BlackPanther (Enhancement)
    - Ransomware - CRFILE (Enhancement)
    - Ransomware - Crone (Enhancement)
    - Ransomware - CrypteVex (Enhancement)
    - Ransomware - Danger (Enhancement)
    - Ransomware - Elons (Enhancement)
    - Ransomware - Forgive (Enhancement)
    - Ransomware - Hero (Enhancement)
    - Ransomware - HexaLocker (Enhancement)
    - Ransomware - Jackalock (Enhancement)
    - Ransomware - Lockedfile (Enhancement)
    - Ransomware - Lookfornewitguy (Enhancement)
    - Ransomware - Mkp (Enhancement)
    - Ransomware - Pandora (Enhancement)
    - Ransomware - PetyaX (Enhancement)
    - Ransomware - Qilra (Enhancement)
    - Ransomware - SHINRA (Enhancement)
    - Ransomware - Spyhunter (Enhancement)
    - Ransomware - Warning (Enhancement)
    - Visual Studio Extension Traffic To Low Popularity Target (New)
- **Apps Catalog**
  - More than 130 new Cloud Apps (see [Apps Catalog](/v1/docs/using-the-app-catalog)), including:
    - Loom (enhancement)
    - ScreenConnect (enhancement)
    - Cloudflare (enhancement)
    - PDQ (enhancement)
    - Remote MCP servers (New)
    - MCP Registry (New)
  - Client Classification:
    - Claude native client (New)
    - GPT native client (New)
    - Cursor IDE (New)
    - Windsurf IDE (New)
    - Zed IDE (New)
    - Highlight AI (New)
    - Cline VScode extension (New)
- **XDR Indications of Attack Signatures:**
  - **Anomaly Detection:**
    - Deprecated or Unauthorized Protocols First Occurrence Anomaly(Enhancement)
  - **Threat Hunting****:**
    - Spoofed Browser Activity (Enhancement)
    - Bot Detection To Low Popularity Destinations (Enhancement)
- **Device Inventory:**
  - These are the updates to the [Device Inventory](/v1/docs/using-the-device-inventory-page) detection engine:
    - IOT
      - CCTV
        - IDIS (Enhancement)
      - Multifunction Device
        - Toshiba (Enhancement)
      - Smart TV
        - Samsung (Enhancement)
      - VoIP
        - Cisco (Enhancement)
        - Grandstream Networks (Enhancement)
        - Mitel (Enhancement)
        - Polycom (Enhancement)
    - Mobile
      - Mobile Computer
        - Honeywell (Enhancement)
      - Mobile Phone
        - Oppo (Enhancement)
        - Samsung (Enhancement)
    - Networking
      - Access Point
        - Aruba Networks (Enhancement)
        - Ubiquiti (Enhancement)
    - OT
      - Area Scan Camera
        - Teledyne FLIR (Enhancement)
    - PC
      - Desktop
        - Dell (Enhancement)
        - HP (Enhancement
      - Laptop
        - Dell (Enhancement)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
