---
title: "Generating Application Analytics Reports"
slug: "generating-an-application-analytics-report"
updated: 2026-08-16T11:14:45Z
published: 2026-08-16T11:14:45Z
canonical: "knowledge.catonetworks.com/generating-an-application-analytics-report"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating Application Analytics Reports

This article describes how to generate a Cato Application Analytics report that highlights data related to application usage and traffic data for your account.

## Overview

Cato provides a Predefined Report template that summarizes application usage and traffic in your account. Create the template for the Scheduled or One-Time report with the sites and SDP users that are included in the report over the defined time range. By default, the Predefined Report template for the Application Analytics report shows traffic and data for all sites and SDP users for the past week.

For more about working with reports, see [Cato Reports](/v1/docs/cato-reports).

![predefined_reports.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30650626861725.png)

## Creating a Recurring Application Analytics Report

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

## Creating a One-Time Application Analytics Report

Create a new One-time report template, and define the **Filters** for the items included in the report. Then define the **Time Range** that the report covers.

**To create a one-time report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Catalog** tab, select the template you want to use to generate the report.
3. Select **Generate** > **Generate Now**.
4. Enter a **Report Name**.
5. Define the relevant **Filters** for your report. These are specific to the report type.
6. Define the **Timeframe** and **Timezone** of the report.
7. Select the **Format**: PDF or CSV.
8. Click **Generate**. The report is generated, and you can download it from the **Generated** tab.

## Understanding the Application Analytics Report

For sections in the report that show the top applications, they include up to the top 12 items for that section.

These are the sections in the Security report:

- Application Traffic Summary
  - **Application Traffic:** Timeline that shows the total upstream and downstream traffic for all apps over the time range
  - **Total Traffic by Direction:** Chart showing volume and percentage of upstream and downstream traffic
  - **Total Traffic by Application Type:** Chart showing volume and percentage of Cloud/SaaS apps vs. On Premise apps
- Applications by Traffic
  - **Top Applications by Downstream Traffic:** Top apps according to downstream traffic with the total traffic per app
  - **Top Applications by Upstream Traffic:** Top apps according to upstream traffic with the total traffic per app
  - **Top Applications Downstream Traffic :** Graph showing the daily downstream traffic of the top three apps
  - **Top Applications Upstream Traffic:** Graph showing the daily upstream traffic of the top three apps
- Applications Breakdown
  - **Top Traffic Categories:** Top categories according to total traffic
  - **Top Applications by Users:** Top apps according to total number of users accessing the app
  - **Top Traffic Destination Domains:** Top domains that are the destination of app traffic according to total traffic
  - **Top Applications by Sites:** Top apps according to total number of sites accessing the apps
- Applications Risk
  - **Applications by Risk:** Chart showing count and percentage of high, medium, and low risk apps used

Cato's risk level is calculated based on the analysis of millions of data flows. For more about the risk levels, see [Using the App Catalog](/v1/docs/using-the-app-catalog)
  - **Traffic by Risk:** Chart showing traffic volume and percentage of traffic for high, medium, and low risk apps
  - **Sanctioned vs. Unsanctioned Applications:** Chart showing count and percentage of sanctioned and unsanctioned apps used

For more about working with sanctioned and unsanctioned apps, see [Using the Cloud Apps Dashboard](https://support.catonetworks.com/hc/en-us/articles/24373642591389#UUID-09981eb4-4ee8-8342-804d-70ff2b20f10a)
  - **Sanctioned vs. Unsanctioned Application Traffic:** Chart showing traffic volume and percentage of traffic for sanctioned and unsanctioned apps
- Applications Traffic Details - The table shows the following details for up to 100 top apps according to the total traffic volume:
  - **Application:** Name of the app
  - **Risk:** Cato's risk level for the app (high, medium, or low)
  - **Cloud App:** Boolean value showing if this app is a cloud/SaaS app (1=cloud app, 0=on prem app)
  - **Sanctioned:** Boolean value showing if this app is a sanctioned app (1=sanctioned app, 0=unsanctioned app)
  - **Users/Hosts:** Number of users and hosts that accessed the app
  - **Downstream:** Total downstream traffic for the app
  - **Upstream:** Total upstream traffic for the app
  - **Total Traffic:** Total downstream and upstream traffic for the app
