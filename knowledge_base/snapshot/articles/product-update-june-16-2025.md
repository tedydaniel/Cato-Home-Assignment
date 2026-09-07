---
title: "Product Update - June 16, 2025"
slug: "product-update-june-16-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-june-16-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - June 16, 2025

## New Features & Enhancements

- **Enhanced Admin Experience for Managing the Split Tunnel Policy at Scale:** We improved management of the [Split Tunnel Policy](/v1/docs/routing-with-the-cato-client-split-tunnel-policy) with the following features:
  - Ability to [modify the policy](/v1/docs/working-with-policy-revisions) in parallel by multiple admins
  - A faster and more responsive page for policies with many rules
  - Public API support will be available soon
- **Additional Data in Device Inventory**: The [Device Inventory](/v1/docs/what-is-device-inventory) page now includes detailed drill-down views, giving you deeper visibility into device activity to help you monitor usage, troubleshoot issues, and strengthen security. The new drill-down includes:
  - The applications and domains each device interacts with
  - Detailed connectivity insights per device
  - Click [here](https://academy.catonetworks.com/device-inventory-device-drilldown-drawer) to watch a video recording of this feature
- **MCP Server Now Available on GitHub:** We implemented a new MCP (model context protocol) server that lets you interact with your account using natural language with questions such as “Which sites are currently in a degraded state?” with no coding required. See this [blog](https://www.catonetworks.com/blog/meet-catos-model-mcp-server/) post about using Cato’s MCP server as a smarter way to integrate AI into your IT and security processes.
  - This is an open-source implementation and Docker image of an MCP server, which is now available on [GitHub](https://github.com/catonetworks/cato-mcp-server). The MCP server uses the [entityLookup](https://api.catonetworks.com/documentation/#query-entityLookup) and [accountSnapshot](https://api.catonetworks.com/documentation/#query-accountSnapshot) APIs
  - Click [here](https://academy.catonetworks.com/cato-mcp-server) to watch a video recording of this feature

## PoP Announcements

- **Buenos Aires, AR:** A new Cato PoP will shortly become available in Buenos Aires with the IP range 199.27.41.0/24.
- New ranges are available for the following PoP locations:
  - **Milan, IT:** 159.117.227.0/24
  - **Zurich, CH:** 159.117.226.0/24

## Knowledge Base Updates

New [articles](/v1/docs/migrating-from-ldap-to-scim-user-provisioning) that provide admins with a clear pathway for migrating existing user and group provisioning from LDAP to SCIM.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
