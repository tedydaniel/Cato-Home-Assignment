---
title: "Product Updates - November 17, 2025"
slug: "product-updates-november-17-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-november-17-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - November 17, 2025

## New Features & Enhancements

- **Improved Autonomous WAN Firewall Insights:** AI-powered insights of WAN firewall rules evaluate compliance with Cato’s recommendations for optimized firewall configurations and security posture. The new [Review Over-Permissive Rules](/v1/docs/what-is-the-cato-wan-firewall) insight provides recommendations to help you identify and refine overly broad firewall rules using:
  - **Topological heuristics:** Identify over-permissive rules using network topology analysis, not just LLM-based judgment
  - **Expanded business context and metadata:** Understand the intent and operational impact behind each recommendation with enriched contextual details
  - **Improved rule descriptions:** Benefit from clearer, more flexible, and comprehensive rule explanations for faster decision-making
  - **Actionable next steps:** Receive additional, targeted recommendations to guide effective rule optimization and strengthen enforcement
- **New Actions for Investigating XOps Site Operations Stories:** To quickly access relevant data and simplify analysis, you can [perform new actions](/v1/docs/retrieving-diagnostic-data-with-site-operations-story-actions) directly from a Site Operations story page (XOps license required). The data retrieved by each action is displayed directly on the story timeline. These are the supported actions:
  - **Export Data to ISP Template:** Provides ICMP and Traceroute results for the underlay at the time of the issue
  - **Get IPsec Status:** Retrieves the current status and configuration parameters of the IPsec tunnel
  - **Get BGP Status:** Retrieves the current status and configuration parameters of the BGP session
- **Zero-Touch Provisioning Enhancement for Socket Sites:** To simplify on-prem Socket deployments, you can now [pre-assign a Socket](/v1/docs/managing-sockets) to the site (Account > Sockets & Accessories) using the serial number (S/N) even before the Socket connects to the Internet.
  - Previously, Sockets required Internet connectivity to be assigned to a site
  - Click [here](https://academy.catonetworks.com/socket-assignment-before-power-up) to watch a video recording of this feature
- **iOS Client v5.6.4:** The new Client will be available to download from the App Store the week of November 16. This version includes:
  - Stability improvements
  - Security updates
  - Bug fixes
- **Terraform Module for WAN Network Rules:** [Streamline deployment and management](/v1/docs/using-terraform-with-the-cato-cloud) of WAN Network Rules with Infrastructure as Code. Admins can define WAN Network Rules and sections in JSON and automate updates to the Network Rules page using Terraform.
  - Automate the bulk import of WAN Network rules and sections from a structured JSON file
  - Maintain rule order, section hierarchy, and item placement during policy updates in the CMA

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
