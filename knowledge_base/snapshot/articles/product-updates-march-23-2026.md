---
title: "Product Updates - March 23, 2026"
slug: "product-updates-march-23-2026"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-march-23-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - March 23, 2026

## New Features & Enhancements

- **New Windows Client v6.2:** During the week of March 22, 2026, we will begin the roll out of Windows Client version 6.2. This version includes:
  - Stability improvements
  - Security updates
  - Bug fixes

- **AI Root Cause Analysis in XOps Stories**: Use AI to automatically execute investigative steps to help identify the root cause of issues without manual analysis.
  - Supported for [Predictive Insight stories](/v1/docs/drilling-down-and-analyzing-xops-predictive-insight-stories)
  - Requires an XOps license

- **HA for GCP vSocket Sites:** Cato now supports redundant high availability (HA) deployments of virtual Sockets in Google Cloud Platform (GCP) for seamless failover and improved uptime for your cloud infrastructure.
  - Deploy primary/secondary vSockets across separate GCP zones for enhanced availability
  - Deploy the vSockets from the [marketplace](/v1/docs/deploying-a-gcp-vsocket-from-the-marketplace) or using the dedicated [Terraform module](/v1/docs/configuring-high-availability-ha-for-gcp-vsocket-sites-using-terraform)

- **Expanded Control for SCIM Users and Directories:** Manage [SCIM-synced users](/v1/docs/scim-user-provisioning) and directories directly from the Cato Management Application (CMA) for greater administrative control and lifecycle management.
  - Disable and delete active SCIM users, and delete SCIM directories
  - User and group deletions sync with the SCIM application
  - Filter users and groups based on deleted SCIM directories
- **API Support for Managing Custom Applications**: You can automate the full lifecycle management of custom applications through the API instead of creating and updating them manually in the CMA. This helps you scale policy automation and keep application objects aligned with your operational workflows.

## PoP Announcements

- **New Delhi, IN:** A new Cato PoP will soon be available in New Delhi with the IP range 202.75.240.0/24.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
