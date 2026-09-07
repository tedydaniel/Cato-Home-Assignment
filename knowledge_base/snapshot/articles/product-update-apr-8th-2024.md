---
title: "Product Update - Apr. 8th, 2024"
slug: "product-update-apr-8th-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-apr-8th-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Apr. 8th, 2024

## New Features & Enhancements

- **Single accountMetrics Query for Socket and Interface Metrics across Multiple Sites:** Now you can use the [accountMetrics](https://api.catonetworks.com/documentation/#query-accountMetrics) API query for multiple sites:
  - Set the 'groupInterfaces' field to 'false' (the default value) and specify multiple sites in the `siteIDs[]` list
    - Until now, this setting was only supported when querying a single site, as specified in the `siteIDs[]` list
  - You can also leave the `siteIDs[]` list empty (the default value), and query all the sites in your account
  - Querying specific sites results in more efficient metrics collection and reduces the risk of hitting the [accountMetrics API rate limit](/v1/docs/understanding-cato-api-rate-limiting)
- **Cato Management Application Enhancement:**
  - **New Socket Sites Use the LAN Firewall Policy:** New Socket sites will now manage local traffic using the [LAN Firewall Policy](/v1/docs/configuring-the-socket-lan-firewall-policy).
    - Previously sites had the Local Routing page and were able to upgrade to the LAN Firewall Policy
    - No impact or changes to existing sites
- **Roadmap Updates:** Go to the [Cato Product Roadmap](https://support.catonetworks.com/hc/en-us/articles/14517158733853-Cato-Product-Roadmap) in the Knowledge Base to follow the status of upcoming features and enhancements.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
