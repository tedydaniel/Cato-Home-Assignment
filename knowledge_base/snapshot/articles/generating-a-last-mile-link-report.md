---
title: "Generating Last Mile Link Reports"
slug: "generating-a-last-mile-link-report"
updated: 2026-08-16T11:14:45Z
published: 2026-08-16T11:14:45Z
canonical: "knowledge.catonetworks.com/generating-a-last-mile-link-report"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating Last Mile Link Reports

This article describes how to generate Cato Last Mile Link reports that highlight the last mile stories created for your account by the Cato Intelligent Last Mile Monitoring (ILMM) service.

## Overview

Cato provides Predefined Report templates that summarize data for all the last mile stories detected for your account by the Cato ILMM service. This lets you generate a report that highlights the ILMM service capabilities for relevant stakeholders in the organization. The Last Mile Link report includes data such as ISPs and sites that generated the most stories, Last Mile Link story trends, and general information about the service for your account.

You can create a Last Mile Link report as a recurring or one-time report.

For more about working with reports, see [Cato Reports](/v1/docs/cato-reports).

![predefined_reports.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30650627066141.png)

### Prerequisites

- Last Mile Link reports are available only for ILMM and NOCaaS customers. For more about subscribing to these services, please contact your Cato representative.

## Creating a Recurring Last Mile Link Report

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

## Creating a One-Time Last Mile Link Report

You can create a one-time report based on the Last Mile Link report template. You define the **Filters** for the items included in the report.

**To create a one-time report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Catalog** tab, select the template you want to use to generate the report.
3. Select **Generate** > **Generate Now**.
4. Enter a **Report Name**.
5. Define the relevant **Filters** for your report. These are specific to the report type.
6. Define the **Timeframe** and **Timezone** of the report.
7. Select the **Format**: PDF or CSV.
8. Click **Generate**. The report is generated, and you can download it from the **Generated** tab.

<editor360-custom-block data-preprocessing="true" data-sanitizationtags="a"><h2 data-block-id="msri6dpn-l60icb-094" class="title" id="downloading-reports"><a id="UUID-d6ca59f0-b7ed-badb-dbaf-f58de7dba913_section-idm293494285885250" display="false" data-zd-article="UUID-d6ca59f0-b7ed-badb-dbaf-f58de7dba913"></a>Downloading Reports</h2></editor360-custom-block>

Download your scheduled or one-time reports from the **Generated** tab. You can use the **Reload** button to refresh the Generated tab and see if a report is **Ready** to download. It may take a few minutes to generate reports with large amounts of data. Recurring reports are **In Progress** when they are automatically emailed. To download recurring reports, generate a new report in the **Saved Reports** tab and then download it. You can use the **Reload** button to refresh the reports to see whether it’s **Ready** to download.

Admins with viewer permissions are allowed to download reports.

![GeneratedReports.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26983606009117.png)

**To download a report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Generated** tab, find the report and click **Download**.
3. To delete a report, click ![more.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29146153826077.png) and select **Delete**.

## Understanding the Last Mile Link Report

The sections in the Last Mile Link Report show data for the configured time range. These are the sections:

- **ILMM Service - General Data** -
  - **ILMM Sites** - The total number of monitored and unmonitored sites included in the ILMM service for your account. Monitored sites are sites with active performance monitoring for at least one of the last-mile links. Unmonitored sites are sites still being onboarded, sites where monitoring was paused on demand, or sites with insufficient ISP information to actively monitor the site.
  - **ILMM Links** - The total number of monitored and unmonitored links included in the ILMM service for your account. Monitored links are actively monitored for last-mile issues. Unmonitored links are sites where monitoring was paused on demand or links with insufficient ISP information to actively monitor the link and manage issues with the ISP.
  - **Single WAN Sites** - The number of sites with a single WAN link connection. Single WAN sites lack best-practice network resiliency. We strongly recommend having multiple last-mile connections for each site.

**Note:** This number also includes sites with Alternative WAN connections.
- **Story Summary**
  - **Providers with Most Stories** - ISPs that generated the most Last Mile Link stories.
  - **Sites with Most Stories** - Sites that generated the most Last Mile Link stories.
  - **Story Summary** - A breakdown by type of last mile link stories that occurred in monitored sites during the report period.
  - **Last Mile Link Story Trends** - Shows the aggregated stories for monitored sites during the generated report period, broken down by story type.
- **Last Mile Link Stories** - For all monitored links that generated stories, this table shows the total number of stories for the report time range, as well as the breakdown by story type (Site Down, Link Down, Quality SLA, and Alt. WAN Link Down). The table is ordered by number of stories generated.
  - Link **Uptime** percentage is measured by dividing the time range into 2-minute buckets and determining if there is last mile connectivity during each bucket based on out-of-tunnel Last Mile Monitoring probes. For more about Last Mile Monitoring probes, see below.

**Note:** **Uptime** is only calculated for links that have probes configured. Alt. WAN links do not support probes, and, by default, the Last-Resort link does not have probes enabled.

A bucket is considered downtime as follows:

**Understanding Last Mile Monitoring Probes** - Cato's Last Mile Monitoring Probes feature help you monitor the quality of the last-mile ISP link. For more about enabling and configuring probes, see [Last Mile Monitoring Probes and Connectivity](/v1/docs/last-mile-monitoring-probes-and-connectivity). You can view metrics generated from the probes in the site Network Analytics page (Network > Sites > <selected site> Site Monitoring > Network Analytics). The metrics related to the Last Mile Monitoring probes are the Last Mile Packet Loss and Last Mile Distance graphs, shown below:

![Last_Mile_Analytics.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30650580021021.png)

For more about these metrics, see [Showing the Site Network Analytics](/v1/docs/showing-the-site-network-analytics).

> [!NOTE]
> Note:
> 
> Stories are triggered when the Cato tunnel goes down. However, in some cases the root cause is not the ISP link, and probes may still detect connectivity. As a result, it’s possible for the report to show multiple stories for a site while the link **Uptime** appears unaffected.
    - For single Socket sites - If all out-of-tunnel probes from a given interface fail to reach any destination during the time period
    - For HA sites - If all probes from the same interface on both sockets fail to reach any destination during the time period

**Note:** This logic assumes Cato's recommended best practice of having a symmetrical configuration of ISP links for the HA Sockets.
