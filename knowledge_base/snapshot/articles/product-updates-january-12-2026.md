---
title: "Product Updates - January 12, 2026"
slug: "product-updates-january-12-2026"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-january-12-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - January 12, 2026

## New Features & Enhancements

- **Upcoming Rollout of Socket v25:** We are starting to gradually roll out [Socket version 25](/v1/docs/socket-version-25-0-release-notes) to all customers, including firmware for new features, enhancements, and bug fixes.
  - No customer action is required
- **Define Multiple Dynamic and Static IP Ranges for Cato Client IP Allocation:** To better [manage IP allocation](/v1/docs/ip-allocation-policy-for-remote-users) for environments that require specific IP addresses across multiple offices, define multiple dynamic and static IP ranges to support user-level IP assignment. For example, call centers that service multiple accounts.
  - Previously, only a single CIDR range could be defined
- **Reset / Refresh FirewallHit Counter:** Reset and refresh [Internet](/v1/docs/what-is-the-cato-internet-firewall) and [WAN](/v1/docs/what-is-the-cato-wan-firewall) Firewall rule hit counters for up-to-date visibility. This lets you accurately measure rule effectiveness and immediately validate rule activity.
  - Resetting the hit counter for a specific firewall rule returns the hit count to 0
  - Refreshing the hit counter updates the hit count for all firewall rules
    - Previously, rule hit counters were updated automatically only once every 24 hours
- **Faster HA Failover for BGP-Connected Socket Sites:** We've enhanced the resilience and responsiveness of Socket HA failover in [BGP](/v1/docs/bgp) scenarios to minimize downtime.
  - Reduces failover time with optimized BGP timers and BFD support
  - Improves reliability when the primary Socket goes down mid-session
  - Helps maintain session continuity and SLA targets for BGP-routed sites
  - Supported from Socket v25 and higher
- **Category for DEM Socket Probes in Network and Security Policies:** For simplified and consistent policy enforcement across all relevant [DEM probe types](/v1/docs/configuring-the-experience-monitoring-probes-and-policy), we added the category **DEM Socket Synthetic Probes.** This category can be configured in Network and Security policies to control probe traffic.
  - Supported from Socket v25 and higher
- **New Fields for DNS and Apps Security Events:** These [events](/v1/docs/understanding-event-fields) provide deeper visibility into request/response behavior, performance characteristics, and transaction details. You can use the data to improve troubleshooting and analytics.
  - Duration (ms) - only DNS events
  - Record Type
  - Request Size
  - Response Size
  - Transaction Size
  - HTTP Response Code
- **Expanded Webhook Payloads:** Webhook integrations include [additional fields](/v1/docs/understanding-the-json-fields-for-alert-integrations) that give you more context for automation, monitoring, and troubleshooting, reducing the need for follow-up queries.
  - Webhooks for Connectivity Health events:
    - <kbd>socketSerial</kbd>
  - Webhooks for XOps Site Operations stories:
    - <kbd>lastIncidentDescription</kbd>
    - <kbd>storyStatus</kbd>
    - <kbd>ISPName</kbd>
    - <kbd>socketSerial</kbd>, <kbd>socketMacAddress</kbd>, <kbd>socketDescription</kbd>
    - <kbd>secondarySocketSerial</kbd>, <kbd>secondarySocketMacAddress</kbd>, <kbd>secondarySocketDescription</kbd>
- **Additional SSO Providers for Users:** We added Hennge IdP and ForgeRock as [SSO providers](/v1/docs/single-sign-on) for authenticating users.
- **Browser Extension v1.4:** During the week of January 11, a [new Browser Extension](/v1/docs/summary-of-browser-extension-releases) version 1.4 will be rolled out to users and available in the Chrome Web Store, and includes the following bug fix:
  - Improved performance issues that caused increased browser CPU consumption
- **CMA Enhancement - Data Protection Dashboard:** The Inline Protection tab of the Data Protection Dashboard displays data violation events only. This lets you focus on potential data leaks.
  - Previously, all App Security events were displayed

## PoP Announcements

- **Frankfurt, DE:** A new range (159.117.236.0/24) is now available for the Frankfurt PoP location.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
