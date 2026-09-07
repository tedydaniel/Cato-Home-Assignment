---
title: "Welcome to the CMA"
slug: "welcome-to-the-cma"
updated: 2026-08-12T09:10:51Z
published: 2026-08-12T09:10:51Z
canonical: "knowledge.catonetworks.com/welcome-to-the-cma"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Welcome to the CMA

This article introduces key concepts and practical tips to help you quickly get started and comfortably navigate within the Cato Management Application (CMA).

## Overview

The CMA is the single management console to monitor traffic and configure settings in your Cato account. The CMA menus are built around the core themes of Security, Access, and Network, which are based on a logical flow for CMA admin activities - monitoring traffic and activity, and configuration changes. For example, admins can monitor security activities in the Threats Dashboard page and then allowlist traffic that is false-positive in the Anti-Malware and IPS configuration pages under the Security menu. In addition, the Home menu contains pages that are useful across multiple themes to help you fully leverage Cato's converged SASE platform.

You can easily navigate to your most frequently used pages by adding them to your favorites.

### CMA Menus

The following are some general guidelines for understanding how the new menus are organized:

- The **Home** menu contains pages with cross-platform information that spans multiple domains and themes
- The **Network**, **Security**, and **Access** menus contain both monitoring and configuration pages for the relevant policies and features
- The **Resources** menu includes items and objects that are used across the themes, such as Groups, Detection & Response Policy, and Catalogs
- The **Account** menu contains pages relevant to account management and administration

**Note:** The new navigation menus have no impact on [RBAC](/docs/welcome-to-the-cma#UUID-4304ca4e-34ab-e79d-2532-e414cf568c79https://catonetworks.zendesk.com/hc/en-us/articles/8601848215197#UUID-4304ca4e-34ab-e79d-2532-e414cf568c79) role scopes. The page permissions for all predefined and custom roles remain the same. However, when you open the settings for a role on the Roles & Permissions page, the pages are shown organized according to the new menus.

## CMA Global Regions and Data Residency

The Cato Management Application (CMA) service is hosted on multiple data centers. Every account uses one of the locations, which is assigned when the account is created. Migrating to a different region is not supported.

This lets customers maintain data residency in their chosen location to meet regulatory requirements and address data sovereignty concerns.

Currently, the CMA is hosted in the following locations:

- Ireland (cc.catonetworks.com)
- US - Virginia (cc.us1.catonetworks.com)
- India (cc.in1.catonetworks.com)
- Japan (cc.jp1.catonetworks.com)

Several URLs for Cato services differ depending on the location of your data center. This will impact what you see when monitoring Cato traffic.

## Propagating Settings to Your Account

The CMA is the unified management console for managing your account. When you save changes or publish policies, the new settings are saved to a central database and then gradually propagated to the PoPs in the Cato Cloud. During the propagation, there are several phases of automated checks that are performed to validate the configuration and prevent the impact of a bad configuration on the entire Cato Cloud.

The multi-tenant system of the CMA applies the configuration changes from all tenants across the Cato Cloud in real-time. Any specific saved configuration for settings and policies can take up to 5 minutes to propagate and apply to all PoPs and to your entire account.

**Note:** For sites or SDP users that are connected through China PoPs, the CMA policy propagation status isn't tracked.

## Understanding Concurrent Admins

> [!NOTE]
> IMPORTANT:
> 
> Some policies support concurrent admins and policy revisions, for more information, see [Working with Policy Revisions](/v1/docs/working-with-policy-revisions).

When multiple admins are logged in to the CMA at the same time (concurrently), occasionally, there can be an issue if they try to configure the same setting at the same time. To manage these types of issues, the CMA shows a warning message when there is a possibility of saving a configuration which can overwrite changes that were recently made by a different admin.

This is an example of the warning message shown to concurrent admins.

1. Admin1 is editing the New York site at the same time as Admin2 is editing the same site.
2. Admin1 saves the changes to the site.
3. Admin2 tries to save changes to the site.
4. Admin2 sees a pop-up window, which states that saving the changes may overwrite the recently configured changes made by a different admin.
5. Admin2 can choose to overwrite and save these changes, or discard the changes.

If Admin2 discards the changes, the CMA refreshes and shows the configuration saved by Admin1 (in step 2).

### Configuring the Same Entity Types in the CMA

Issues related to concurrent admins only occur when they are working on the same entity type. Otherwise, admins can make changes at the same time. These are the entity types in the CMA:

- Account settings (such as security and network settings)
- Sites
- SDP users
- Groups
- Admins

**Example of Changes to Different Entity Types**

Admin1 saves changes to the New York site, and then Admin2 saves changes to an SDP user. The admins can successfully save the changes.

**Example of Changes to the Same Entity Type**

Admin1 saves changes to a firewall rule and then Admin2 saves changes to a network rule. Admin2 is shown the warning message about saving the changes or discarding them.

## Searching for a Page

Use the CMA search menu to find a page by using the search bar or by browsing the menu contents.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(177).png)

## Managing Favorite Pages

You can add up to 10 pages to your favorites for quick and easy access. Favorites are saved at the admin level, allowing each admin to customize their own list. If you no longer need frequent access to a page, simply remove it from your favorites. You can also add or remove favorites from the account menu.

![Favorites.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27100307241629.png)

**To add a page to your favorites:**

1. Navigate to the page you want to add to your favorites.
2. Click the star icon next to the page breadcrumbs.

The page is added to your favorites.

**To view your favorite pages:**

- From the navigation menu, click the star.

The list of your favorite articles is displayed.

**To remove a page from your favorites:**

1. Navigate to the page you want to remove from your favorites.
2. Click the star next to the breadcrumbs.

The page is removed from your favorites.

## Viewing Recently Visited Pages

You can view up to 10 of the most recently visited pages in the CMA to help you find what you're looking for as fast as possible. Data is stored per user in your local browser, so if you clear your cache, use a different browser or device, the list will be reset.

![recently_viewed_CMA_pages.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27100276616349.png)

**To view recently visited pages:**

1. At the top of the left-hand navigation pane, click the **Recent** button.
2. Click the page names to navigate directly to the pages.

> [!NOTE]
> Note:
> 
> The recently visited pages list only includes general CMA pages, like the Sites page. For example, if you drilled down from the Sites page to a specific site, the list will display and link to the main Sites page instead.

## Providing Feedback

We strongly encourage our customers to provide feedback, including what you like about the new navigation and suggestions for improvement. You can provide feedback through these channels:

- In the CMA **Help** menu, use the **Send Feedback** option
- Schedule a call with a Cato Product Manager, contact us at [ea@catonetworks.com](mailto:ea@catonetworks.com)

## Approving the Cato MSA

The Cato Master Service Agreement (MSA) defines the terms of the agreement between Cato and each customer. The first time that an admin logs in to the CMA for an account, they need to accept the MSA. This requires an admin with edit permissions. You can view the full MSA [here](https://www.catonetworks.com/msa/).
