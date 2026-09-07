---
title: "Using the Topology Page"
slug: "using-the-topology-page"
updated: 2026-07-16T10:23:25Z
published: 2026-07-16T10:23:25Z
canonical: "knowledge.catonetworks.com/using-the-topology-page"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Topology Page

This article explains how to use the Topology page to get an overview of the sites in your account and SDP users connected to the network.

## Overview

The Topology page shows a high-level view of the sites for the account, and the users that are currently connected to the Cato Cloud. It also contains options to let you easily control commonly used settings and shows some real-time analytics and data.

You can use the **Remote Socket WebUI** feature for centralized access to the Socket WebUI for a specific site. For more information see, [Accessing the Socket WebUI](/v1/docs/accessing-the-socket-webui).

## Using the Topology Page

The **Topology** page provides several shortcuts for users and sites that take you directly to the Network Analytics page for specific sites or users, or the entire account.

**To show the Topology page:**

- From the navigation menu, click **Home > Topology**.

The following screenshot shows the sections of the **Topology** page.

![Topology_Callouts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275637390493.png)

| Status | Description |
| --- | --- |
| 1 | - The site icon is according to the **Type** setting (in the **General** section for the site). Types include Branch, Headquarters, Cloud Data Center, and Data Center. - The user icon is according to the Client OS The **Topology** page doesn't show individual users that are connected to the network with office mode. |
| 2 | - ![ZoomIn.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275645333917.png) Zoom-in - ![ZoomOut.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275685459357.png) Zoom out - ![Recenter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275637582493.png) Center the **Topology** page and reset to the default zoom - ![expandAll.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275645553693.png) Expand all site, PoP, and SDP user nodes - ![collapseAll.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275669197725.png) Collapse all site, PoP, and SDP user nodes |
| 3 | The quick filter section for the Topology page lets you show only the following items: - **Sites** - All the sites that are configured for your account - **Connected** - All the sites that actively connected to a PoP in the Cato Cloud - **Disconnected** - Sites that are NOT connected to the Cato Cloud - **Degraded** - Sites that have connectivity issues, e.g. a port or tunnel is down, or HA Status is not ready - **Disconnected (Disabled)** - Sites that are disabled in the CMA (manually or due to an expired license) - **Connected SDP Users** - SDP and LAN users that are actively connected to the Cato Cloud |
| 4 | **Search** - enter the search string (even a partial name for a site or SDP user) and the **Topology** page automatically updates to only show items that match the search |
| 5 | **Filter & Group** - Click this button to open the **Filter & Group** panel for granular control about how the items in the Topology page are displayed. See below, [Using the Filter & Group Panel](/v1/docs/using-the-topology-page#using-the-filter-group-panel). |

### Understanding the Site Information Panel

When you click on a site in the Topology page, a panel opens and shows details about the site. For information about the Site Preview pane, see [Working with the Site Preview Pane](/v1/docs/working-with-the-site-preview-pane).

## Using the Filter & Group Panel

The **Filter & Group** panel lets you easily control how the sites and SDP users are displayed in the Topology page. The **Show** section manages which sites and SDP users currently appear in the page. The **Group** section lets you manage which nodes are used to display the sites and SDP users. Each node aggregates the relevant sites and SDP users around them. The following example shows sites according to the provider (ISP):

![Topology_Group.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275669278365.png)

### Explanation of the Filter & Groups Options

These are the display options in the **Filter & Group** panel:

- **Show > Sites** - Displays all the sites in the account. Use the following options to select which sites are displayed or hidden in the **Topology** page:
  - **Connected** - Sites that are currently connected to the Cato Cloud
  - ​​**Degraded**​​ - Sites that have connectivity issues
  - **Disconnected** - Sites that are NOT connected to the Cato Cloud
  - **Disconnected (Disabled)** - Sites that are currently disabled
- **Show > SDP Users** - Shows or hides all the SDP users that are currently connected to your account.
- **Group** drop-down menu - Select a preconfigured option for how the sites and SDP users are grouped around nodes in the **Topology** page:
  - **Default** - default Topology view (according to the number of connected sites and users in your account)
  - **None** - No nodes are used, all sites and SDP users are grouped around the Cato Cloud
  - **Full Topology** - The following nodes are used: PoP location > Sites, Users > Country, operating system (OS), and ISP
  - **Customized Grouping** - see below
- **Customized Grouping > Sites** or **Users** - Select one or more of the following options to control which nodes are used to group the sites and SDP users:
  - **PoP** - Grouped according to geographical PoP location
  - **Sites** - All sites are grouped around a single Sites node (only for sites)
  - **Users** - All SDP users are grouped around a single Users node (only for users)
  - **Country** - All sites and SDP users are grouped around nodes for the country that is defined for sites (in the Cato Management Application)
  - **Provider** - All sites and SDP users are grouped around nodes for each local Internet Service Provider (ISP)
  - **Operating System** - All SDP users are grouped around nodes for each device operating system (only for users)

### Customized Grouping - Changing the Node Hierarchy

The order of the **Group** options defines the hierarchy of the nodes in the **Topology** page. The option that is at the top of the list is the node that is closest to the Cato Cloud. You can drag and drop the options to change the hierarchy of the **Customized Grouping** settings.

The following example shows changing the Sites hierarchy, so that the Provider nodes are closest to the Cato Cloud, and then the PoP nodes are after the Provider nodes.

![Topology_CustomizedGrouping.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275685839517.png)
