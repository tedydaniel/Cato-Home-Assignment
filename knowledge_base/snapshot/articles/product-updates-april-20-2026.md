---
title: "Product Updates - April 20, 2026"
slug: "product-updates-april-20-2026"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-updates-april-20-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - April 20, 2026

## New Features & Enhancements

- **Visualize Ask AI Answers in Charts:** Faster troubleshooting and analysis in [Ask AI](/v1/docs/what-is-cato-s-ask-ai-agent) with pie and line charts that make trends, anomalies, and distribution easier to understand.
  - Quickly spot trends and anomalies in network and security data
- **Enterprise Browser v1.0.4.38:** The [Enterprise Browser](/v1/docs/what-is-the-cato-enterprise-browser) provides secure access to sensitive SaaS and private applications from unmanaged devices, without installing the Cato Client.
  - Dedicated, managed workspaces where corporate activity is isolated from personal browsing
  - Unified security policies such as Internet Firewall, CASB, and Data Protection are consistently enforced across all users
- **Detailed Visibility of Interconnected Apps - Support for Zendesk and Google Workspace:** View detailed information about third-party apps and plugins connected to [Zendesk](/v1/docs/zendesk-configuring-the-interconnected-apps-integration) or [Google Workspace](/v1/docs/google-workspace-configuring-the-interconnected-apps-integration). This visibility helps you understand which external apps are used in your environment and how they interact with core services.
  - View the **Plugins** option in the Security > Applications page on the **Inventory** tab
  - Requires a CASB license
- **Traceroute-Based Path Analysis in Experience Monitoring:** Gain hop-by-hop visibility into network paths with continuous [traceroute data](/v1/docs/using-traceroute-for-path-analysis-in-experience-monitoring) to quickly identify where latency or packet loss occurs between the Socket, PoP, and application.
  - Available in the **Connection Details** section of Site, Host, and Office User drill-down pages
  - Supported for Socket site traffic with Socket v25 and higher
  - Requires a DEM license
- **DEM Enhancements for Microsoft Teams Integrations:** To better indicate end-user experience issues, MS Teams performance on the [Experience Monitoring page](/v1/docs/the-user-experience-monitoring-drill-down-page-remote-and-office-users) is now displayed as a meetings timeline instead of a general application experience score. This enables more precise detection and troubleshooting of experience degradation.
  - Requires DEM license
- **Global Language Support for Predefined ML Classifiers in DLP:** Predefined [ML classifiers for DLP](/v1/docs/working-with-predefined-data-types-for-dlp) now support over one hundred languages. This improves the detection of sensitive content in multilingual documents. You can use these classifiers in DLP content profiles to identify sensitive document types such as medical records, tax forms, patent documents, resumes, and immigration forms.
- **Use Enterprise Browser or Browser Extension in Firewall Policies:** We are starting to gradually roll out the ability to enforce more granular Internet and WAN firewall policies based on how users access applications, and use the Cato [Enterprise Browser](/v1/docs/what-is-the-cato-enterprise-browser) and [Browser Extension](/v1/docs/what-is-the-cato-browser-extension) as the **Origin of the connection** for a [rule](/v1/docs/adding-device-conditions-to-firewall-rules). This helps you apply different controls for access paths while improving segmentation for sensitive applications.
  - Available from April 30, 2026
- **Domain and FQDN Support for Client Split Tunnel Policy:** Use Domain and FQDN in Split Tunnel policies to include or exclude destinations. This provides a more flexible way to route traffic for remote users, particularly for SaaS services and Applications using dynamic public IPs.
  - Requires DNS Relay running on the device
  - Available from April 30, 2026
- **Provide AI Security Analysis Feedback from the CMA:** When reviewing prompts in the Cato Management Application (CMA) [Session Explorer](/v1/docs/ai-security-for-end-users-monitoring-and-analytics-with-session-explorer), you can give feedback for false positives and missed detections. This feedback helps improve the AI Security engine results.
  - Select the specific detectors you want to give feedback for each prompt, and add additional free-text feedback
  - Requires AI Security license
- **Bidirectional Webhooks Integration with ITSMs for Stories:** Integrate XOps stories with external service management platforms using [bidirectional webhooks](/v1/docs/creating-bi-directional-integrations-with-service-management-platforms). When an XOps story is created, a matching ticket is automatically created in the service management platform. Comments added to that ticket are synced to the CMA, making it easier to follow updates and collaborate from one place.
  - Built-in templates for ServiceNow and Zendesk
  - Requires XOps license
- **New Fields for appStats API:** We enhanced the appStats API with new application experience metrics, enabling programmatic access to user, host, and application performance data. Previously, these metrics were only available in the Experience Monitoring pages.
  - For more information about the fields, see [this article](/v1/docs/cato-api-changelog)
  - Requires a DEM license
- **Gradual Rollout of Socket v25.0.22707:** We are starting to gradually roll out Socket [version 25.0.22707](/v1/docs/socket-version-25-0-release-notes) to customers, including firmware for new features, enhancements, and bug fixes. No customer action is required.

## PoP Announcements

- **New Delhi, IN:** We added a new Cato PoP location in New Delhi on a limited availability basis.
  - For more information about limited availability PoPs, see [this article](/v1/docs/faq-limited-availability-pops)

- **New Localized IP Range for Estonia:** The following localized IP range for Estonia (serviced through the Helsinki PoP location) is now available:
  - **EE:** 159.117.235.32/27

- New ranges will soon be added to these PoP locations:
  - **Chicago, US:** 199.27.51.0/24
  - **Tokyo, JP:** 113.30.134.0/24

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
