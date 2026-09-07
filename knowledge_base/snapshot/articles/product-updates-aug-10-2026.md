---
title: "Product Updates - Aug 10, 2026"
slug: "product-updates-aug-10-2026"
updated: 2026-08-09T15:09:59Z
published: 2026-08-09T15:09:59Z
canonical: "knowledge.catonetworks.com/product-updates-aug-10-2026"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates - Aug 10, 2026

## New Features & Enhancements

- **Cato Knowledge Base Moves to a New Platform:** To provide a more intuitive and efficient knowledge experience, the Knowledge Base moved to a new platform.
  - No impact on Support tickets
  - Improved search filters, easily navigate between related articles, and export multiple articles as a single PDF
  - Access the new platform at [knowledge.catonetworks.com](http://knowledge.catonetworks.com)
  - For more information, see [this article](https://knowledge.catonetworks.com/v1/docs/moving-to-new-knowledge-base-platform)
- **AI Security Proxy Guards Support Passthrough Mode:** Secure AI applications with a Proxy Guard while maintaining compatibility with AI provider endpoints that Cato doesn't inspect.
  - AI Security for Applications license required
- **Managed Agents Visibility for AI Security:** Identify and investigate [managed AI agents](https://knowledge.catonetworks.com/docs/working-with-managed-agents) from connected no-code agent platforms to understand ownership, configuration, accessible resources, and activity. For example, agent prompts, connected knowledge bases, tools, and recent activity.
  - Supported platforms include Copilot Studio, Amazon Bedrock, Microsoft Foundry, ChatGPT, and Amazon Quick
  - AI Security for Applications license required (show me the [Managed Agents page](https://externallink.cc.catonetworks.com/#/account/me/managedAgents))
- **Reminder - CMA Navigation Change:** From Aug. 31, 2026, all accounts will use the new navigation for the Cato Management Application (CMA). The navigation toggle will be removed.
- **Send Events to SIEM or Log Collector via HTTP Push:** Configure a custom [HTTP Push integration](https://knowledge.catonetworks.com/docs/sending-cato-data-to-external-platforms-http-push) to continuously stream events to external HTTP endpoints for unsupported third-party integrations. This enables integration with SIEMs, log collectors, analytics platforms, and other systems that accept JSON or NDJSON over HTTP.
  - Show me the [Integrations page](https://externallink.cc.catonetworks.com/#/account/me/integrationsCatalog)
- **Enterprise Browser v1.2.0.54:** During the week of Aug. 9, 2026, Enterprise Browser [version 1.2.0.54](https://knowledge.catonetworks.com/docs/summary-of-enterprise-browser-releases) will be available. This version contains:
  - **Configure the Homepage:** Define the URL for when users open a new tab
  - Bug fixes, stability improvements, and security enhancements
- **Additional User Actions Supported via API:** The [API](https://api.catonetworks.com/documentation/#group-Operations-Mutations-UserMutations) supports enabling users (`enableUser`) and disabling users (`disableUser`). This simplifies user administration through external workflows and identity management systems.
- **Improved Usability for Authenticating Users with Registration Codes:** [Registration Codes](https://knowledge.catonetworks.com/docs/activating-users-with-a-registration-code) are one-time codes to authenticate users in the Client.
  - Codes can be generated and downloaded as a CSV file in a single step
  - Users can be assigned multiple codes
- **DEM Enhancements:**
  - For quick access to the Experience Monitoring Probes page, we added the **Settings** button to all [Experience Monitoring pages](https://knowledge.catonetworks.com/docs/using-the-experience-monitoring-page)
  - The **Events** feed in [drill-down pages](https://knowledge.catonetworks.com/docs/understanding-the-experience-monitoring-drill-down-pages) includes the **Event ID** and a link to open the Events page pre-filtered to show that event
  - We updated the thresholds for **LAN Gateway** metrics in drill-down pages to the following:
    - **Good** - 7 ms or lower
    - **Fair** - between 7-10 ms
    - **Poor** - 10 ms or higher

### PoP Announcements

- A new range is now available for the Melbourne PoP location:
  - **Melbourne, AU:** 113.30.140.0/24

**Note:** Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](https://knowledge.catonetworks.com/docs/understanding-rollout-to-the-cato-cloud). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
