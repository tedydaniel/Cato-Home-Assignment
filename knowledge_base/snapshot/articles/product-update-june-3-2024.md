---
title: "Product Update - June 3, 2024"
slug: "product-update-june-3-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-june-3-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - June 3, 2024

## New Features & Enhancements

- **Preview Pages for Licensed Services:** We introduced a new 'preview mode' that lets you explore and configure licensed features even though they don't have a [license](/v1/docs/working-with-cato-license-types). This enables you to experiment with the settings and understand the capabilities of the feature without requiring a full license.
  - Enabling the service requires an active license
- **Enhanced Connection SLA Mechanism for Socket Sites:** We improved the granularity of the [Connection SLA](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites) mechanism that determines when a link experiences an unacceptable SLA. You can define a specific percentage (N%) of a time window that is used to determine if the link has an acceptable SLA. For example, if the Packet Loss is set to 50% of a 120-second time window, if there is Packet Loss for 60 seconds within that window, the site has an unacceptable SLA and takes the appropriate action.
  - Previously, the SLA was calculated according to 100% of the time window, the new default value is 50%
  - Supported for Socket v20.0 and higher
- **SaaS Security API - Threat Protection for Additional Connectors:** We added support for [Threat Protection malware scans](/v1/docs/data-protection-api) to the following connectors: ServiceNow, SalesForce, GitHub.
- **New Troubleshooting Playbooks for Common Issues:** We added [playbooks to the Knowledge Base](/v1/docs/common-issues-playbooks) that help you address and troubleshoot a range of common issues. For example, the [Socket Deployment and Registration playbook](/v1/docs/socket-deployment-and-registration-troubleshooting) describes common symptoms related to registering Sockets to Cato and tools to check registration status and connectivity.
- **Update for Transition to Client Connectivity Policy:** For customers who have not yet manually transitioned to the Client Connectivity Policy, after June 1st, 2024, the Device Authentication page will remain available until you complete the transition to the Client Connectivity Policy. There will be no change in behavior for users.
  - For customers who were automatically transitioned to the Client Connectivity Policy, in the next few weeks, the Device Authentication page will be removed
  - The Device Authentication page is no longer available for customers who didn’t configure settings on the Device Authentication page
- **Cato Management Application Enhancement:**
  - The [Socket Inventory](/v1/docs/using-the-socket-assignment-page) page now has an optional column that displays the **Description** for each Socket

Go to the [Cato Product Roadmap](https://bit.ly/49aFEKU) in the Knowledge Base to follow the status of upcoming features and enhancements.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
