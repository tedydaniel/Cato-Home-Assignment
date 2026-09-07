---
title: "Product Update - June 2, 2025"
slug: "product-update-june-2-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-june-2-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - June 2, 2025

## New Features & Enhancements

- **Enhanced Admin Experience for Managing the Network Rules Policy at Scale:** We improved management of the [Network Rules](/v1/docs/configuring-network-rules) policy with the following features:
  - API support for managing the policy For more information see the [Cato GraphQL API Reference](https://api.catonetworks.com/documentation/#introduction)
  - Ability to [modify the policy](/v1/docs/working-with-policy-revisions) in parallel by multiple admins
  - A faster and more responsive page for policies with many rules

- **Connectivity Health Alert Enhancement:** To more easily identify the relevant Socket interface, alerts for [Connectivity Health rules](/v1/docs/working-with-link-health-rules) now include both the user-configured Socket **Interface Name** and the **Interface ID** (e.g. WAN1).
  - Previously, the **Interface Name** field showed only the ID

- **Reminder - Upcoming Automatic Migration of Site LAN Firewall to Account-Level Policy:** The [Socket Next Gen LAN Firewall](/v1/docs/what-is-the-socket-next-gen-lan-firewall) provides account-level configurations and Layer 7 enforcement and replaces the current site-level LAN Firewall policy. Starting from July 1, 2025, we will migrate existing site-level LAN firewall rules to the account-level policy.
  - Each site-level rule will automatically be configured in the policy as a Next Gen Network rule to specify the routing, and a Next Gen Firewall rule to allow or block the traffic
  - The rules for each site will be added as a separate section in the rulebase
  - The migration is a seamless, automatic process, and no service disruption is expected
  - If you're interested in migrating your policy before July 1, please contact [cato-releases@catonetworks.com](mailto:cato-releases@catonetworks.com)

## PoP Announcements

- **Upcoming Extended Localized IP Range for Paraguay:** An extended localized IP range for Paraguay (serviced through the Santiago PoP location) will soon be available - 150.195.192/27.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
