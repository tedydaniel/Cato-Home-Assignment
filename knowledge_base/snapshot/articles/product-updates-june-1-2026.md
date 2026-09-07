---
title: "Product Updates - June 1, 2026"
slug: "product-updates-june-1-2026"
updated: 2026-06-29T13:02:35Z
published: 2026-06-29T13:02:35Z
canonical: "knowledge.catonetworks.com/product-updates-june-1-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - June 1, 2026

## New Features & Enhancements

- **Ask AI Finds Where Entities Are Used in Policies:** Ask AI helps you quickly identify which rules use a specific entity across your account, so you can assess policy impact, remove unused items, and troubleshoot more efficiently.
  - View where entities such as sites, users, hosts, applications, IP addresses, groups, and websites are used across policy rulebases in one place
  - Policies include: WAN Firewall, DLP, CASB, Client Connectivity Policy, and more (already supported for the Internet Firewall)
- **XOps Stories Include Multiple Related Entities:** XOps stories provide a more comprehensive view of users, sites, devices, and other objects. These appear in story drill-downs in the new **Entities** widget, which replaces the **Source** widget.
  - The data is also available via the [IncidentEntity](https://api.catonetworks.com/documentation/#definition-IncidentEntity) API
  - Requires XOps license
  - This feature is gradually being implemented in the various producers
- **Cato AI Security Integrates with Third-Party Vendors to Expand GenAI Discovery**: Cato AI Security expands your visibility into AI usage by integrating with third-party vendors and enriching Shadow AI discovery with additional telemetry sources. These integrations help you identify more GenAI activity and improve coverage for unmanaged and distributed environments. Requires AI Security for End Users license.
  - **Netskope integration** - Cato AI Security connects to your Netskope environment with read-only API access and uses usage logs to provide a more complete view of GenAI discovery
  - **Palo Alto Networks Cortex XDR integration** - Cato AI Security enriches Shadow AI discovery with inventory data from Cortex XDR and combines it with HTTP and HTTPS metadata to identify more AI-related activity
- **Navigation Change for Experience Monitoring Probes Page**: The Experience Monitoring Probes page is now located under **Home** instead of **Network**, providing a more centralized location for DEM configuration and monitoring in the Cato Management Application.
- **Visibility of Paused Automatic Client Rollouts:** In rare cases where Cato identifies an issue with a Client version during rollout, Cato may pause the rollout. When a Client rollout is paused, a notification banner appears on the Client Rollout page
  - Supported for Upgrade Policies configured as **Automatic by Cato**
- **Resuming Rollout of Active/Active Support for IPsec Sites:** We are resuming the rollout of support for IPsec sites to establish and route traffic through multiple active tunnels. This enables higher bandwidth and improved stability for your IPsec sites by better utilizing multiple last-mile links.
  - You can establish up to 3 active tunnels per role (Primary and Secondary)
  - All active tunnels for a role must be connected to the same PoP location
  - Previously available only for new accounts
  - Click [here](https://academy.catonetworks.com/multiple-active-tunnels-for-ipsec-sites) to watch a video recording of this feature

**Note:** Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this article. See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
