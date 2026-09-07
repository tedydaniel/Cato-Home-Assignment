---
title: "Product Updates - September 29, 2025"
slug: "product-updates-september-29-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-september-29-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - September 29, 2025

## New Features & Enhancements

- **Time Zone Selection and Visibility in Reports**: You can now choose a time zone when [generating reports](/v1/docs/cato-reports), for example, to align report data with a specific time zone. The selected time zone is shown in all reports.
- **Terraform Modules for Azure vSocket HA and Bulk Socket Provisioning:** The new modules let you automate:
  - **Bulk provisioning for Socket sites:** Streamlines [deployment efforts for Sockets](https://registry.terraform.io/modules/catonetworks/socket-bulk-sites/cato/latest) and accommodates backup and restore, as well as brownfield deployments. Configurations can be exported in either CSV or JSON format, updated to add modifications to existing Socket sites, interfaces, and network range configurations, and configuration updates can be pushed back to the CMA for those existing sites
  - **Azure vSocket HA sites:** Enables integration with new or existing Azure VWAN resource deployments using [HA vSockets](https://registry.terraform.io/modules/catonetworks/azure-vwan-vsocket-ha/cato/latest) for fully resilient deployments

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
