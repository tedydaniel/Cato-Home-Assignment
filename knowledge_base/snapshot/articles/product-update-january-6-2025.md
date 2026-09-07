---
title: "Product Update - January 6, 2025"
slug: "product-update-january-6-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-january-6-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - January 6, 2025

## New Features & Enhancements

- **Manage Users from Multiple IdPs:** For greater flexibility and simplified user management, you can now configure [multiple identity providers](/v1/docs/configuring-multiple-identity-providers) (IdPs) to provision and authenticate users. For example, after a merger or acquisition, each company can continue to use their existing IdP, without the complexity of consolidating them. This also includes multiple tenants from the same IdP. Users can now be:
  - Provisioned from multiple user directories that support SCIM
  - Authenticated using different SSO providers
  - Click [here](https://academy.catonetworks.com/managing-users-from-multiple-idps) to watch a video of this feature
- **New Navigation for CMA:** The new grouping and ordering for the Cato Management Application (CMA) menus are now the default navigation structure. The [new navigation](/v1/docs/welcome-to-the-cma) helps create a logical flow for monitoring traffic and activity and configuration changes to provide better usability and experience for admins.
  - You can still use the toggle to easily return to the previous navigation structure
  - We added a Home menu to highlight cross-platform workflows spanning multiple domains, such as XDR Stories Workbench and Experience Monitoring. The single-domain perspective is maintained in the Network, Access, and Security menus that include monitoring and configuration pages
  - The new navigation has no impact on traffic in your account and supports existing flows and browser bookmarks (no changes to the current URLs)
- **New AI Assistant to Help you with Features and Functionality:** Ask the [AI Assistant](/v1/docs/what-is-cato-s-ask-ai-agent) any Cato-related question directly from the CMA, and the assistant scans the Knowledge Base to provide an answer.
  - Access the AI Assistant from the Help menu
  - The AI assistant cannot provide specific answers for your account
  - Click [here](https://academy.catonetworks.com/cato-kb-bot-in-the-cma) to watch a video of this feature
- **Windows Client v5.13:** Starting January 5, 2025, we are rolling out Windows Client version 5.13.
  - The following [DEM enhancements](/v1/docs/experience-monitoring) are now supported with this version:
    - **Underlay Performance Monitoring in Socket Last Mile**: Identify and diagnose out-of-tunnel issues that could impact last-mile performance
    - **Group Multiple Devices**: DEM hardware metrics are now grouped by device name, helping you easily understand the performance of each device when there are multiple devices for the same user
    - **Support for Different LAN Gateways:** LAN gateway probes are now grouped by LAN gateway IP, letting you easily understand the performance of each LAN gateway when different gateways are present at different timeframes
  - Bug fixes and enhancements
  - Click [here](https://academy.catonetworks.com/client-releases-windows-v513) to watch a video about this new version
- **macOS Client v5.8:** Starting January 5, 2025, we are rolling out macOS Client version 5.8. This version contains:
  - **Record Client Issues:** An additional troubleshooting tool that lets users [record](/v1/docs/recording-issues-using-the-cato-client) and then reproduce an issue that occurred with the Client. The traffic capture and log files can be uploaded to Support for further analysis.
    - This feature and the existing ability to send logs to Support are available on the new Support tab in the Client
  - **Updated OPSWAT OESIS Framework**: We updated the OPSWAT OESIS framework used by the Client to version 4.3.3685
  - Improved support for macOS 15 (Sequoia)
  - Bug fixes and enhancements
  - Click [here](https://academy.catonetworks.com/client-releases-macos-v58) to watch a video about this new version
- **Important Update for LDAP User Provisioning:** We updated the IP addresses used for LDAP synchronization. Ensuring your firewall ACLs (Access Control Lists) are updated with the new IP addresses is essential to maintain seamless LDAP synchronization. Without updating these IP addresses, LDAP syncs will fail.
  - The new IP addresses are listed [here](https://support.catonetworks.com/hc/en-us/articles/20511945810589-Using-Cato-IP-Addresses) (you must be signed in to view this article)
  - To ensure that user provisioning with LDAP is not impacted, you must update these IP addresses by:
    - January 19, 2025 - for on-demand syncs
    - February 9, 2025 - for automated daily sync
- **Exclude Socket Sites from the Automatic Upgrade Service:** You can exclude specific sites from automatically upgrading the Sockets to the newest version. This ensures business-critical sites are not disrupted during the configured [maintenance window](/v1/docs/configuring-the-socket-upgrade-maintenance-window).
  - Cato recommends you resume the upgrades after the maintenance window to ensure that the Socket is upgraded in the next cycle

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
