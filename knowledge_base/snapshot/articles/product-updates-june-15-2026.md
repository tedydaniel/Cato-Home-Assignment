---
title: "Product Updates - June 15, 2026"
slug: "product-updates-june-15-2026"
updated: 2026-07-09T08:09:42Z
published: 2026-07-09T08:09:42Z
canonical: "knowledge.catonetworks.com/product-updates-june-15-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - June 15, 2026

## New Features & Enhancements

- **Per-App VPN Support for iOS Devices with Intune:** Configure iOS Clients to route traffic from specific apps through the Cato Cloud, while all other traffic stays outside the tunnel. This selective tunneling approach removes the need for Always-On and route-based Split Tunnel policy.
  - Enables secure access to corporate applications without enforcing full device tunneling
  - Users can run native iOS apps that don't require inspection or control outside the tunnel
  - Reduces performance overhead and avoids unnecessary traffic inspection
  - Simplifies compliance with BYOD and mobile use cases
  - Supported from iOS Client v5.8 and higher, deployed with Microsoft Intune
- **Coding Agents Policy Manages AI Agents Activity:** Protect coding agent use with centralized controls for prompts and tool use. The new Coding Agents Policy page helps you prevent sensitive data exposure and unsafe actions by letting you monitor or block risky activity across supported local agents.
  - Requires AI Security for Users license
- **Android Work Profile Support with Intune:** Securely connect Android Work Profile applications to the Cato Cloud while Personal Profile traffic bypasses the tunnel and uses the device’s local network connection. Selectively route traffic for managed corporate apps while separating corporate and personal traffic on the same Android device, and apply Always-On enforcement only to the Work Profile scope.
  - Requires deployment using Microsoft Intune and Android Work Profiles
  - Requires app traffic routing to be managed by the Android OS and MDM profile
  - Supported from Android Client v5.5 and higher, deployed with Microsoft Intune
- **New Windows Client v6.8.2:** During the week of June 14, 2026, we will begin rolling out the Windows Client version 6.8.2. This version includes:
  - Client Management now runs on a separate service to better support resiliency
    - To ensure this service runs correctly, add coresvc.exe to your security allowlist
  - Bug fixes, security fixes, and stability improvements
- **Oct 1 EoS for Cato Clients:** From October 1, 2026, the following Clients will be End of Support (EoS). We recommend that you update devices to the newest Client version to ensure continued support and security protections.
  - Windows Clients v5.17 and lower
  - macOS Clients v5.10.0 and lower
  - Linux Clients v5.5 and lower
  - iOS Clients v5.6.0 and lower
  - Android Clients v5.2.1 and lower
- **Sandbox Support for macOS Files**: The Sandbox supports forensic static analysis of suspicious and malicious files on macOS, in addition to static and dynamic forensics analysis on Windows.
  - Requires an Advanced Threat Prevention license
- **Configure DNS Protection Threshold for Newly Registered Domains:** DNS protection detects DNS requests to domains that were recently registered and may not yet have an established reputation. To give you more control over how aggressively DNS Protection identifies and blocks risky domains, configure a threshold to block domains registered within the last 7, 14, 21, 30, or 60 days.
  - Requires a Threat Prevention license
- **Show Detected Emails for Unidentified Local AI Agents:** We enhanced the Local Agents page to show detected email addresses for unidentified users, helping you investigate agent activity from personal and shadow users.
  - Shows detected email addresses based on data from the network flow
  - Helps investigate activity during initial deployment and trial stages
  - Requires AI Security for Users license
- **Detailed Visibility of Interconnected Apps - Support for Atlassian:** View detailed information about third-party apps and plugins connected to Atlassian. This visibility helps you understand which external apps are used in your environment and how they interact with core services.
  - View the **Plugins** option in the Security > Applications page on the **Inventory** tab
  - Requires a CASB license
- **Improved Visibility for Socket Hardware:** We added a summary bar to the Sockets & Accessories > Socket Assignment page that shows the Socket types and hardware models in your account. This helps you quickly review your Socket inventory and understand whether any hardware requires a refresh.
  - See how many Sockets you have for each hardware model, such as X1700A and X1700B
- **CMA Highlights Insights about Frontier AI:** We are introducing a Frontier AI News section in the CMA What’s New to provide curated insights from Cato experts on emerging developments in AI and cybersecurity. It helps organizations stay updated on new attack techniques, defensive innovations, real-world practices, major AI industry announcements, and the enterprise security impact of frontier AI. Example topics:
  - Advanced AI models and their security implications
  - Moving beyond patch SLAs toward time-to-protection
  - TeamPCP supply chain attacks targeting trusted development and AI components
- **CMA Enhancement:** We have updated the Access > Users page to include:
  - Overview section displaying a summary of user status and provisioning updates
  - Enhanced filtering, including predefined preset filters

## PoP Announcements

- **Mumbai, IN:** A new range (113.30.136.0/24) is now available for the Mumbai PoP location.
- The following new ranges will soon be available:
  - **Ashburn, US:** 199.27.54.0/24
  - **Detroit, US:** 199.27.55.0/24

**Note:** Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](https://support.catonetworks.com/hc/en-us/articles/11968052021277-Understanding-Cato-s-Gradual-Rollout). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
