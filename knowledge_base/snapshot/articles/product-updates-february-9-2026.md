---
title: "Product Updates - February 9, 2026"
slug: "product-updates-february-9-2026"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-february-9-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - February 9, 2026

## New Features & Enhancements

- **Flexible Traffic Routing using the Cato Client** Cato is introducing new capabilities that make the Cato Client more adaptable to your existing network infrastructure, whether you're maintaining local services or gradually onboarding to Cato.
  - **Granular Client Control with Managed Networks:** Dynamically adjust Split Tunnel and Always-On behavior based on the [detected source network](https://support.catonetworks.com/hc/en-us/articles/29049792088093-Working-with-Managed-Networks-EA), supporting hybrid environments and gradual onboarding.
    - Source Networks in Split Tunnel Policy:
      - Dynamically apply Split Tunnel Policy rules based on Source Network condition
      - Enforce full tunneling on unmanaged networks like public WiFi or home setups
      - Seamlessly adjust Split Tunnel configuration when a Managed Network is detected
      - Requires Windows Client v5.16 and higher
    - Defining Managed Networks as Trusted:
      - Suspend Always-On enforcement for Managed Networks defined as Trusted
      - Trusted Networks page is now renamed Managed Networks
  - **DNS Split Tunneling Support for Internal DNS Resolution**: [Exclude internal domains](/v1/docs/routing-with-the-cato-client-split-tunnel-policy) from Cato DNS to resolve them locally, while continuing to protect DNS traffic with Cato DNS Protection.
    - Route internal DNS queries to local DNS servers while using Cato for public DNS
    - Define specific internal DNS suffix to bypass Cato DNS
    - Requires Windows Client v5.16 and higher
  - Click [here](https://academy.catonetworks.com/selective-on-ramp) to watch a video recording of this feature
- **Ask AI Expands with Deeper Account Intelligence:** Ask AI provides additional account-aware intelligence that helps you understand policies, settings, and changes across your environment, and identify items that require attention.
  - **Choose the right experience for the task:** Work with Ask AI while navigating the Cato Management Application (CMA), or switch to a dedicated, full-page AI Workspace for deeper analysis
  - **Richer, account-aware answers:** Ask AI analyzes your account data and configuration to answer questions such as:
    - Why is this Internet Firewall rule blocking traffic?
    - Which applications are affected by this security policy?
    - What changed in my network that could explain this traffic spike?
  - These capabilities are available as part of a free trial
- **CMA Instance for Japan:** We are introducing a [CMA instance based in Tokyo, Japan](/v1/docs/welcome-to-the-cma). The new CMA instance offers the same functionality to manage global accounts and networks, and seamlessly connect to all PoPs worldwide.
  - Enables compliance with Japan-specific data residency and sovereignty requirements
  - The Japan CMA instance has no impact on existing Cato customers and partners
- **DSPM Integration with XOps for Visibility of Data Risk:** We are extending [XOps](/v1/docs/welcome-to-the-cato-xops-service) to include data from [Cyera](/v1/docs/cyera-creating-the-xops-integration), a Data Security Posture Management (DSPM) platform. Stories are generated based on data-centric risk context to be investigated in the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) (Home > Stories Workbench).
  - This integration brings visibility into where sensitive data resides, how it is accessed, and whether it is exposed or misconfigured so you can prioritize incidents based on business impact, not just technical severity.
- **Autonomous Policy Detects RPF Exposure to OpenClaw Clawdbot/Moltbot:** The [Cato Autonomous Policy tool](/v1/docs/understanding-cato-autonomous-policies) identifies overly permissive Remote Port Forwarding (RPF) rules that expose OpenClaw Clawdbot/Moltbot–related services. It then provides reccomendations inlcuding: narrowing internal and external port ranges to reduce the risk of agentic-AI abuse, unauthorized remote control, and malware activity.
  - Read more in this [Cato blog](https://www.catonetworks.com/blog/when-ai-can-act-governing-openclaw/)
- **Global API Endpoint Available for Integrations:** API-based [third-party integrations](/v1/docs/using-the-integrations-page) are now available in all [CMA regions](/v1/docs/welcome-to-the-cma).
  - Integrations that use the Cato API are supported across all CMA regions
  - No change or impact for existing integrations
  - New integrations for non-EU regions require a new API key

- **NAT Monitoring Using Internet Firewall Events:** We added the [new field](/v1/docs/understanding-event-fields) **NAT Error** to Internet Firewall events to highlight connectivity issues related to NAT. For example, when the source port is exhausted, the **NAT Error** field indicates the failure reason.

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
