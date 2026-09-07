---
title: "Understanding App Analytics"
slug: "understanding-app-analytics"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/understanding-app-analytics"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understanding App Analytics

This article discusses how to use the App Analytics page to drill down and analyze the network and application usage for your entire account, a specific site, or a specific user.

## Overview of App Analytics

The App Analytics page lets you view the application and network usage data for your entire account as well as for specific sites, users, and applications. The page contains a number of widgets that provide visibility for network and application usage. The page also lets you add items to the analytics filter to drill-down and focus on the relevant analytics and data in your account.

When you manually create a filter or add an item to the update filter, the data and analytics on the Applications Analytics page is automatically updated. The App Analytics page is typically up-to-date within a 5 minutes time frame. However, it is possible that some data will be delayed up to 30 minutes.

You can choose to show the App Analytics page for the data in the entire account. You can also select a specific site or user, and show the data only for that site or user.

> [!NOTE]
> Note:
> 
> The App Analytics page includes data for blocked apps. This is because the PoP allows the client device trying to access the app to send multiple packets to the PoP, so it can identify the app and apply the block rule. This request and response traffic between the client device and PoP is included in App Analytics data. For more about how the Internet Firewall blocks traffic, see [Internet and WAN Firewall Policies – Best Practices](/v1/docs/recommendations-for-internet-and-wan-firewall-policies).

### Getting Started with App Analytics

The App Analytics page shows the total network usage over the time range. There are widgets that show analytics for users, applications, and sites according to their geographical location. The analytics table at the bottom half of the page shows the data for the top items according to the current filter.

![usageanalytics.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275655680285.png)

| Item | Name | Description |
| --- | --- | --- |
| 1 | Events filter bar | Shows the filters that are applied to the events. Click ![Add2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275655739037.png) (Add) to manually configure the settings for a filter. |
| 2 | Time range | Select the time range for the events that are shown in the page. The maximum date range for the **App Analytics** page is 90 days. For more about using the Time range, see [Setting the Time Range Filter](/v1/docs/setting-the-time-range-filter). |
| 3 | Network usage timeline | Timeline that shows the total upstream and downstream network usage over the time range. Hover over a bar to show the exact usage for that time bucket. |
| 4 | Top Users | Top users based on total network usage. |
| 5 | Top Applications | Top applications based on total bandwidth used and shows the percentage of total bandwidth for each application. |
| 6 | Top Sites | Map of the top sites based on selected filters. When there are no filters, all the sites for the account are shown. Hover over a site to show name, location and, total bandwidth usage for the site. |
| 7 | Analytics type tabs | Each tab shows the analytics and data for that entity in your network |
| 8 | Analytics data table | Shows the data for that Analytics type. You can expand the row to drilldown and see analytics in a sortable table. |

## Using the Analytics Data Table

The Analytics data tables shows usage data for various entities in your account:

Once you select a tab, you can click ![plus.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275688218397.png) to expand the row and see more data for that item. The data shown in the expanded areas is based on the current filter for the page. You can click on the columns to sort the data in ascending or descending order.

By combining inline filters or creating specific filters in the filter bar, you can investigate anomalies you see on the timeline or drill-down to understand specific instances. For example, you can easily investigate the cause for a spike in upstream bandwidth.

The following table explains the data that is shown in each tab. The **Available for** column shows which tabs are available for the entire account, specific sites or users (see below [Accessing the App Analytics Page](/v1/docs/understanding-app-analytics#accessing-the-app-analytics-page)).

| Name | Description | Available for |
| --- | --- | --- |
| Sites | Shows all the sites that match the current filter. The default view with no filter shows all sites in the account. Expand a site to show the analytics for all the users behind the site. There is a separate row for **Remote Users**, who are connecting with the Cato Client and aren't behind a site. | Account |
| Applications | Shows all the applications that match the current filter. The default view with no filter shows all applications used during the time range. Cato provides a risk score for each application between 0 (no risk) to 10 (very high risk). The risk score is calculated based on the analysis of millions of data flows. A high risk score (typically 7 or 8) indicates that Cato detected high levels of vulnerabilities for this application. Expand an application to show the analytics and usage data for each user. **Note:** Custom apps don't show a risk score. | Account, sites, users |
| Categories | Shows all the categories (as defined in **Resources > Categories**) that match the current filter. The default view with no filter shows all the categories used during the time range. Expand a category to show the each application in the category that was used during the time range. It also shows the total usage data for the application. **Tip:** To drill-down for an application in the category, hover over the application and click ![filter_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275664776221.png). The application is added to the filter, and you can select a different tab for more granular data. | Account, sites, users |
| Users | Shows the application usage of all users that match the current filter. The default view with no filter shows all users that are connected to your account during the time range. Individual users are only displayed once in this table, regardless of the user location. For example, if a user connects remotely and then connects behind a site, all their activity is combined into a single row on the table. Expand a user to show the applications analytic and usage data. | Users |
| Users/Hosts | Shows the application usage of all the users and hosts that match the current filter. The default view with no filter shows all users and hosts that are connected to your account during the time range. Users can be displayed twice in this table. If a user connects remotely and then connects behind a site, two separate rows of data are displayed for the same user. Expand a user or host to show the application analytic and usage data. If a host is detected as Shared Host, the last logon user is displayed. For hosts with a static IP, the configured hostname is displayed. | Users/Hosts |
| Sources | Shows the IP address that initiated the session that match the current filter. The default view with no filter shows all the IP address that initiated a session during the time range. | Account, sites, users |
| Destinations | Shows all the destination apps by the top level domains (TLDs) that match the current filter. The default view with no filter shows all the app domains that were accessed during the time range. The Destinations tab can also help you identify private apps and configure them as custom apps to include in policies. For more about private apps, see [Working with Private Applications on the App Analytics Page](/v1/docs/working-with-private-applications-on-the-app-analytics-page) | Account, sites, users |
| Connections | Shows the application usage of all the users and hosts that match the current filter. The default view with no filter shows all users and hosts that are connected to your account during the time range. Expand a user or host to show the Destination and Direction of traffic flow for each app used by the user/host. | Users/Hosts |

## Filtering the App Analytics Page

There are two ways to filter the data in the App Analytics page: automatically update the filter with the selected item, or manually configure the filter.

### Automatically Filtering for an Item

As you hover over an item or field where a filter option is available, the ![filter_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275664776221.png) button appears, click the icon to add the item to the filter. The App Analytics page now only shows data that includes this item. For example, if you filter for the Zoom application, the page only shows analytics and data that are related to using the Zoom application. No other application data is available until you change or clear the filter.

You can continue to add items to the filter, click ![filter_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275664776221.png) again to update the filter and drill-down further.

### Manually Configuring the Filter

You can manually configure the event filter for greater granularity to analyze the application usage. After you configure the filter, it is added to the filter bar and the page is automatically updated to show the analytics and data that match the new filter.

![createfilter2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275648207645.png)

**To create a filter:**

1. In the filter bar, click ![Add2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275655739037.png).
2. Start typing or select the **Field** (for example: Site Name or Risk Level).
3. Select the **Operator**, which determines the relationship between the **Field** and the **Value** you are searching for.
4. Select the **Value**.
5. Click **Add Filter**.

The filter is added to the filter bar and the **App Analytics** page is updated to show results based on the filters.

### Clearing the Filter

You can remove each item in the filter separately, or clear the entire filter.

![ClearFilter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275671798685.png)

**To clear the filters:**

1. To clear a single filter, click ![remove.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24275688632861.png) next to the filter.
2. To clear all the filters, click X at the right end of the filter bar.

## Accessing the App Analytics Page

The App Analytics page is available at the account, site and, user levels. To show the page for a specific site or user, select it and then open the App Analytics page from the navigation menu.

### Accessing Account-level App Analytics

**To access account-level analytics:**

- From the navigation menu, click **Home > App Analytics**. The **App Analytics** page for the account is displayed.

### Accessing Site-level App Analytics

The App Analytics page shows the data for the specific site. You can't edit the filter to show data for a different site.

**To access site-level analytics:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Monitoring > Application Analytics**.

The **Application Analytics** page for the selected site is displayed.

### Accessing User-level App Analytics

The Applications Analytics page shows the data for the specific user. You can't edit the filter to show data for a different user.

**To access user-level analytics:**

1. From the navigation menu, click **Access > Users** and select a user.
2. From the navigation menu, click **User Monitoring > Application Analytics**.

The **Application Analytics** page for the selected user is displayed.

## Comparing App Analytics and Network Analytics

The analytics and metrics for the App Analytics page and the pages for network analytics (such as Network > Sites Overview) can have a small discrepancy because the data is calculated differently.

- For network analytics data (including the account Metrics API query):
  - Upstream and downstream bytes are counted for encapsulated packets (including DTLS headers overhead)
  - Upstream and downstream data for all flows related to the given tunnel are aggregated together
- For the App Analytics data:
  - Upstream and downstream bytes are counted for non-encapsulated packets (before DTLS encapsulation).
  - Upstream and downstream data is displayed per application
