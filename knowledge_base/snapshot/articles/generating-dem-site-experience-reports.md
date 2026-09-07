---
title: "Generating Site Experience Reports"
slug: "generating-dem-site-experience-reports"
updated: 2026-08-16T11:14:45Z
published: 2026-08-16T11:14:45Z
canonical: "knowledge.catonetworks.com/generating-dem-site-experience-reports"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating Site Experience Reports

## Overview

Cato provides a predefined report template that summarizes the score and usage for sites, users, and applications.

Create the template for the recurring or one-time report with the sites that are included in the report over the defined time range. By default, the predefined report template for Experience Monitoring reports shows traffic and data for sites over the defined time frame.

For more about working with reports, see [Cato Reports](/v1/docs/cato-reports).

## Creating a Recurring Site Experience Report

Create a new recurring report by defining the **Filters** for the items included in the report, as well as the **Schedule** which defines how often the report is generated - every two minutes, daily, weekly, or monthly. Generated reports are stored in the Cato Cloud, and they can be automatically emailed or downloaded. The **Schedule** also defines the time range that is covered by each report.

You can select a mailing list of email addresses for the recipients, which can include Cato Management Application admins, and external users.

For more information about Mailing Lists, see [Working with Mailing Lists](/v1/docs/working-with-mailing-lists).

**To create a recurring report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Catalog** tab, find and select the template you want to use to generate the report.
3. Click **Generate** > **Create Schedule**.
4. Enter a **Report Name**.
5. **(Optional)** In **Filters**, select specific sites or users for the predefined report.

By default, the predefined report includes all sites and users.
6. Define when the report will be generated and sent:
  1. Select the **Frequency**.
  2. For Weekly and Monthly scheduled reports, in **Every** select the day that the report is sent.
  3. Select the timezone.
7. Select the **export format**: PDF or CSV.
8. In **Subscriptions**, select the **Mailing List** that receives the report.

You can click **New** to create a new mailing list.
9. Click **Save Schedule**. The report is added to the **Saved Reports** tab.

### Generating a Recurring Report On Demand

Recurring reports are automatically generated based on their schedule settings. For example, a weekly report configured for Monday, is generated every Monday. You can also choose to manually generate a recurring report on demand, in which case the generated report uses the defined time range based on the current day. If an admin manually generates a weekly report on a Tuesday, the time range for the report is the previous 7 days starting from that Tuesday, regardless of the starting day of the recurring report. For more information about the time range of recurring reports, see [Cato Reports](/v1/docs/cato-reports).

**To generate a recurring report on demand:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Saved Reports** tab, find the recurring report and click **Generate Now**.
3. From the **Generated PDFs** tab, find the report and click **Download**.

## Creating a One-Time Site Experience Report

Create a new One-time report template, and define the **Filters** for the items included in the report. Then define the **Time Range** that the report covers.

**To create a One-Time report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Catalog** tab, select the template you want to use to generate the report.
3. Select **Generate** > **Generate Now**.
4. Enter a **Report Name**.
5. **(Optional)** In **Filters**, select specific sites or users for the report.

By default, the Predefined Report includes all sites and users.
6. Define the relevant **Filters** for your report. These are specific to the report type.
7. Define the **Timeframe** and **Timezone** of the report.
8. Select the **Format**: PDF or CSV.
9. Click **Generate**. The report is generated, and you download it from the **Generated** tab.

## 

<editor360-custom-block data-preprocessing="true" data-sanitizationtags="a"><h2 data-block-id="msri6dpn-l60icb-094" class="title" id="downloading-reports"><a id="UUID-d6ca59f0-b7ed-badb-dbaf-f58de7dba913_section-idm293494285885250" display="false" data-zd-article="UUID-d6ca59f0-b7ed-badb-dbaf-f58de7dba913"></a>Downloading Reports</h2></editor360-custom-block>

Download your scheduled or one-time reports from the **Generated** tab. You can use the **Reload** button to refresh the Generated tab and see if a report is **Ready** to download. It may take a few minutes to generate reports with large amounts of data. Recurring reports are **In Progress** when they are automatically emailed. To download recurring reports, generate a new report in the **Saved Reports** tab and then download it. You can use the **Reload** button to refresh the reports to see whether it’s **Ready** to download.

Admins with viewer permissions are allowed to download reports.

![GeneratedReports.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26983606009117.png)

**To download a report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Generated** tab, find the report and click **Download**.
3. To delete a report, click ![more.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29146153826077.png) and select **Delete**.

## Understanding the Site Experience Report

There are two Experience Monitoring reports:

- Site Experience Report - Shows details about the sites' average scores, as well as top sites, hosts, and applications (by usage)
- Site and User Experience Report - Shows details about users' experience, and includes some basic site experience data

The report includes information about the Average Experience Score and is followed by sections that display the top sites, top hosts, and top applications by usage.

> [!NOTE]
> Note:
> 
> Sections that show data for application experience are filtered to show data only for sanctioned applications.

### Site Experience Report

These are the sections in the Site Experience report:

- Average Experience by Site
  - **Average Experience:** Indicates the site's average experience over the report range
  - **Unique Users:** The number of users using the site
  - **Apps:** The number of apps accessed through the site
  - **Source Site Country:** The country from which traffic for the site originates
  - **Downstream:** The total volume of traffic entering the site
  - **Upstream:** The total volume of traffic leaving the site
  - **Total Usage:** The sum total of traffic traversing the site
- Average Experience by Host
  - **Average Experience:** Indicates the site's average experience over the report range
  - **Unique Users:** The number of users using the site
  - **Apps:** The number of apps accessed through the site
  - **Source Site Country:** The country from which traffic for the site originates
  - **Downstream:** The total volume of traffic entering the site
  - **Upstream:** The total volume of traffic leaving the site
  - **Total Usage:** The sum total of traffic traversing the site

### Site and User Experience Report

These are the sections in the Site and User Experience report:

- User Average Experience by Site
  - Top Users by CPU Utilization
    - **User name:** The user for which the information is provided
    - **Avg. experience:** The average experience score for this user
    - **Avg. CPU:** The average CPU usage for this user
  - Top Users by Memory Utilization
    - **User name:** The user for which the information is provided
    - **Avg. experience:** The average experience score for this user
    - **Avg. Memory:** The average memory usage for this user
  - Top Users by Wi-Fi Signal Strength
    - **User name:** The user for which the information is provided
    - **Avg. experience:** The average experience score for this user
    - **Signal Strength:** The actual signal strength over the range of the report
  - Top Users by LAN Gateway RTT
    - **Avg. experience:** The average experience score for this user
    - **Packet Loss:** Percentage of packets that were lost over the last mile
    - **RTT:** The average amount between the HTTP request and the receipt of the first byte
  - Top Users by Tunnel RTT
    - **Avg. experience:** The average experience score for this user
    - **Packet Loss Upstream:** Percentage of packets that were lost over the last mile inside the tunnel for upstream traffic.
    - **Packet Loss Downstream:** Percentage of packets that were lost over the last mile inside the tunnel for downstream traffic
    - **RTT:** The average amount between the HTTP request and the receipt of the first byte
    - **Usage:** The sum total of traffic traversing the site
  - Sites Average Experience
    - **Average Experience:** Indicates the site's average experience over the report range
    - **Unique Users:** The number of users using the site
    - **Apps:** The number of apps accessed through the site
    - **Source Site Country:** The country from which traffic for the site originates
    - **Downstream:** The total volume of traffic entering the site
    - **Upstream:** The total volume of traffic leaving the site
    - **Total Usage:** The sum total of traffic traversing the site
  - Users Average Experience
    - **Average Experience:** Indicates the site's average experience over the report range
    - **Unique Users:** The number of users using the site
    - **Apps:** The number of apps accessed through the site
    - **Source Site Country:** The country from which traffic for the site originates
    - **Downstream** The total volume of traffic entering the site
    - **Upstream** The total volume of traffic leaving the site
    - **Total Usage** The sum total of traffic traversing the site
