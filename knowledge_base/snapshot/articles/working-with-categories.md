---
title: "Working with Categories"
slug: "working-with-categories"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/working-with-categories"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Categories

This article discusses how to use the predefined Cato system categories and create custom categories to meet the specific needs of your organization.

## Overview

The **Categories** page shows you Cato system and custom categories. Categories are global objects that you can use to customize the Networking, WAN, and Internet firewall rules to meet the specific needs of your network.

When you add multiple categories to a single networking, WAN, or Internet firewall rule, there is an OR relationship between them.

![categories.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24447628163229.png)

### Understanding System Categories

The system categories are predefined and group web content into common categories, such as News, Gambling, Weapons, and so on. You can also create custom categories to include a group of system categories, specific websites, services, and applications.

If a system category doesn't have any members defined for it, then there are no apps or services associated with the category. However, the category can still include domains as part of third-party URL filtering. For more information about domains and categories, see [Identifying the Category for a Domain](/v1/docs/identifying-the-category-for-a-domain).

> [!NOTE]
> Note:
> 
> System categories can include Cato-defined members, and members defined according to third-party URL filtering services. The Cato category definitions are applied to both Internet and WAN traffic flows. However, category definitions based on third-party URL filtering services are only applied to Internet traffic flows.

### Uncategorized vs. Undefined System Categories

The system Categories in the CMA are managed by Cato Networks for ease of use. However, what exactly is the difference between the content in the Uncategorized and Undefined system Categories?

- Uncategorized - web content or domains that does not fit in an existing system Category. Often this follows standard practices that the specific web content is considered as uncategorized by different security vendors.
- Undefined - web content or domains that temporarily the Cato Cloud is unable to define. There are numerous reasons that can cause traffic to be undefined, for example a Microsoft Teams domain can be identified as **Chat & IM** and then later temporarily identified as **Undefined**.

## Showing a Category

The **Categories** page lets you show the details for each system and custom category. System categories can include Cato-defined members, and members defined according to third-party URL filtering services. However, only the Cato-defined members for a category are shown in the page.

**To show a category:**

1. From the navigation panel, click **Resources > Categories**.

The **Categories** panel opens, displaying the **Custom Categories** tab and the **System Categories** tab.
2. Select if you want to show the predefined **System Categories** or **Custom Categories**.
3. Click the **Name** or **Description** column headings to sort the table in alphabetical order.

## Creating a Custom Category

Custom categories give you increased control over the corporate network and security policy. You can define the applications, Internet content, and services that belong to the new category. It is a global object that you can use for the Firewall and Networking rules, events, analysis and so on. These are the types of content that you can use to define a custom category:

- Applications and custom applications
- Services and custom services
- Domains and Fully Qualified Domain Names (FQDN)
  - A Domain is a Second-Level Domain (SLD) and matches all subdomains. For example, the Domain **example.com** matches **example.com**, **host.example.com**, and **subhost.host.example.com**
  - FQDN is an exact match of the fully qualified domain (for example, the FQDN **example.com** only matches **example.com**)

When there are multiple content types in a custom category, such as a Domain Name and a Service, there is an OR relationship between them.

**To create a custom category:**

1. From the navigation panel, click **Resources > Categories**.
2. Click the **Custom Categories** tab.
3. Click **New**. The **Add Category** panel opens.
4. Enter the **Name** and **Description** for the category.
5. From the **Members** drop-down menu, select the content type that you are adding to this category.
6. Repeat the previous step to add more content types.
7. Click **Apply**. The custom category is added.
8. Click **Save**. The custom category is created.

## Creating a Value Set

**Value Sets** are user defined categories that help you manage Application Control rules for groups of items such as URLs or email addresses. **Value Sets** can contain comma-separated text strings for use in [Application Control rules](/v1/docs/managing-the-application-control-policy), or lists of domains to define [allow lists for RBI](/v1/docs/configuring-the-rbi-service-for-browsing-sessions).

The **Value Sets** category is included in the CASB and RBI licenses. For more about purchasing licenses, please contact your Cato representative.

> [!NOTE]
> Note:
> 
> **Value Sets** are only used with the Application Control policy.

![Value_Sets_Tab.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24447643895581.png)

**To create a Value Set:**

1. From the navigation panel, click **Resources > Categories**.
2. Click the **Value Sets** tab and click **New**.
3. Enter the **Name** and **Description** for the **Value Set**.
4. Select the type depending on what you are using the Value Set for:
  - **Application Control Rules:** The type should be **Text Strings**
  - **RBI:** The type should be **Domain List**
5. Enter text strings or valid domains/URLs separated by commas depending on the type you selected above. Domains/URLs can include one wildcard.
6. Click **Add**.
7. Click **Apply**.
