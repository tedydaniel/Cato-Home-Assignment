---
title: "Generating GenAI Reports"
slug: "generating-a-genai-report"
updated: 2026-08-16T11:14:45Z
published: 2026-08-16T11:14:45Z
canonical: "knowledge.catonetworks.com/generating-a-genai-report"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating GenAI Reports

This article describes how to generate a Cato GenAI Report that highlights GenAI usage in your account and the associated risks.

## Overview

Cato provides a Predefined Report template that summarizes how GenAI is used in your account. The report can be run for your entire account or filtered by specific Sites or Users. This report can be used as a key part of your strategy to protect your organization and its sensitive data while enabling secure AI application usage. For more information, see [Securing AI App Traffic](/v1/docs/securing-ai-app-traffic).

You can generate the GenAI report as either a one-time or recurring report.

![Reports.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30650627040029.png)

For more about working with reports, see [Cato Reports](/v1/docs/cato-reports).

## Creating a Recurring GenAI Report

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

## Creating a One-Time GenAI Report

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

<editor360-custom-block data-preprocessing="true" data-sanitizationtags="a"><h2 data-block-id="msri6dpn-l60icb-094" class="title" id="downloading-reports"><a id="UUID-d6ca59f0-b7ed-badb-dbaf-f58de7dba913_section-idm293494285885250" display="false" data-zd-article="UUID-d6ca59f0-b7ed-badb-dbaf-f58de7dba913"></a>Downloading Reports</h2></editor360-custom-block>

Download your scheduled or one-time reports from the **Generated** tab. You can use the **Reload** button to refresh the Generated tab and see if a report is **Ready** to download. It may take a few minutes to generate reports with large amounts of data. Recurring reports are **In Progress** when they are automatically emailed. To download recurring reports, generate a new report in the **Saved Reports** tab and then download it. You can use the **Reload** button to refresh the reports to see whether it’s **Ready** to download.

Admins with viewer permissions are allowed to download reports.

![GeneratedReports.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26983606009117.png)

**To download a report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Generated** tab, find the report and click **Download**.
3. To delete a report, click ![more.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29146153826077.png) and select **Delete**.

## Understanding the GenAI Report

These are the sections in the GenAI Report:

- **GenAI Usage**
  - **GenAI Applications Traffic**: Traffic volume generated by GenAI applications, split into Download and Upstream
  - **Sanctioned vs Unsanctioned Applications**: Number of sanctioned and unsanctioned GenAI apps used
  - **Top GenAI Applications by Usage**: List of the most used GenAI apps in your environment
  - **Top Categories by Usage**: List of the most used GenAI app categories
  - **Top Risky GenAI Applications**: List of the most used risky GenAI apps
  - **User Activities Over Time**: Number of user activities on GenAI apps over time
- **Data Protection**
  - **Events by Action**: Total number of Data Protection events created by GenAI apps, split by Allow and block
  - **Violations by Data Profile**: Proportion of each data type involved in Data Protection policy violations
  - **Rules Hit Count**: The number of times each Data Protection rule was enforced
  - **Data Violations Over Time**: The amount of data policy violations over time
- **GenAI Applications by Users**
  - **Applications**: Summary of GenAI app usage in your account
