---
title: "Product Updates - July 13, 2026"
slug: "product-updates-july-13-2026"
updated: 2026-07-12T13:40:20Z
published: 2026-07-12T13:40:20Z
canonical: "knowledge.catonetworks.com/product-updates-july-13-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - July 13, 2026

## New Features & Enhancements

- **Client Split Tunnel Policy Supports FQDN-Based Apps:** We enhanced the Split Tunnel Policy to use FQDN-based apps that Cato dynamically updates, simplifying policy maintenance. Show me the [Split Tunnel page](https://externallink.cc.catonetworks.com/#/account/me/SplitTunnelPolicy).
  - Clients route matching traffic directly to the Internet or through Cato
  - Supported from Windows Client v6.4 and higher

- **Manage Different Policy Changes in Separate Revisions:** Admins can maintain multiple parallel policy revisions, allowing different policy changes to be developed independently. This enables smaller updates to be published while other changes remain in progress.
  - Switch between published and unpublished revisions
  - Initially available for Internet Firewall, WAN Firewall, and Private Access policies
- **Notify Action Supported for Application Control Policy:** Application and Data Control rules support a Notify action that lets you discourage user activity rather than block it. If a user takes an action that matches this rule, the Client displays a custom notification. Users can dismiss the notification and continue their activity.
  - Customize notification templates (show me the [User Notification page](https://externallink.cc.catonetworks.com/#/account/me/userNotifications))
  - CASB license required
- **SNAT IP Range for Enterprise Browser and Browser Extension:** Configure a dedicated SNAT IP range for Enterprise Browser and Browser Extension. This lets users access WAN applications that use existing IP-based ACLs, even when Cato is not the default gateway at the destination site.
  - Supported on all Enterprise Browser and Browser Extension versions

- **Device Posture Checks Support Lower Than Operator:** Device Posture checks that include a version number support the Lower Than operator. This provides more flexibility when applying rules to devices running versions below a specified threshold.

- **Continuing Rollout for Near Real-Time Updates for Threat Prevention Stories:** XOps Threat Prevention stories continue to be enhanced with near real-time updates, helping admins more quickly detect and respond to supported threat indications.
  - To see the list of enhanced story indications, see here
  - XOps license required

- **Defender for Endpoint XOps Connector Supports Additional Licenses:** The Microsoft Defender for Endpoint XOps connector supports these additional Microsoft licenses:
  - Now supported:
    - Microsoft Defender for Endpoint Plan 2
    - Microsoft 365 E5 or Microsoft 365 E5 Security
    - Microsoft 365 A5 (Education) or Microsoft 365 G5 (Government)
    - Windows 11 Enterprise E5
  - Previously supported for Microsoft 365 E3 or higher
  - Cato XOps license required

- **Simplified AI Gateway Integration:** During the week of July 13, 2026, AI Gateway configuration will become part of the Guards page. Create a single AI Gateway Guard to generate the authorization key and configure your integration, instead of the previous two-step process.
  - AI Security Guards of type AI Gateway are now called Homegrown Apps
  - Existing AI Gateway configurations are migrated automatically
  - For more information about what has changed, see our FAQ
  - AI Security for Applications license required

- **Granular Claude Plan Detection for User Interaction Policy:** Apply different rules for the AI Security User Interaction Policy based on whether users access personal or enterprise Claude environments.
  - Use **Claude Free** and **Claude for Business** as separate applications
  - AI Security for Users license required

- **Automatic Migration to Account-Level Bypass Policy:** To help transition to the account-level Socket bypass policy, we are automatically migrating eligible site-level bypass policies to the account-level policy.
  - Applies to sites running Socket v26 and higher
  - Sites running earlier Socket versions are not eligible for automatic migration
  - The site-level bypass policy will be deprecated from accounts that migrate to the account-level policy

- **Expanded Webhook Fields:** Webhook notifications now include a significantly richer set of fields, giving security teams more data to build complete, actionable payloads for SIEM and SOAR platforms.
  - New security and network event fields follow the same naming conventions as the Events API, making correlation seamless
  - No impact on existing webhook integrations

- **Updates for Cato Terraform Provider:** We released new versions for the Cato Terraform module, including:
  - v0.0.90
    - Stabilized WAN interface hydration
  - v0.0.88
    - Support for Application Control and CASB resources for tenant restriction and application controls (e.g `cato_app_tenant_restriction_rule`)
  - v0.0.87
    - Support for global IP ranges (`cato_global_ip_ranges`)
    - Regression tests
  - Bug fixes and enhancements
  - Read more in the changelog

- **Starting Rollout of Socket v26.0.23517:** We are starting to gradually roll out Socket version 26.0.23517 to all customers, including enhancements and bug fixes. No customer action is required.

## PoP Announcements

- **Detroit, US:** A new range (199.27.55.0/24) is now available for the Detroit PoP location.
- The following new ranges will soon be available:
  - **Melbourne, AU:** 113.30.140.0/24
  - **Paris, FR:** 159.117.247.0/24
  - **Tel Aviv, IL:** 159.117.246.0/24

**Note:** Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this article. See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
