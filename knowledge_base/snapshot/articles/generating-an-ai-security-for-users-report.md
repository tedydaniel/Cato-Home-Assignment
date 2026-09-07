---
title: "Generating AI Security for Users Reports"
slug: "generating-an-ai-security-for-users-report"
updated: 2026-08-18T07:11:21Z
published: 2026-08-18T07:11:21Z
canonical: "knowledge.catonetworks.com/generating-an-ai-security-for-users-report"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating AI Security for Users Reports

This article describes how to generate the AI Security for Users report that highlights the significant data and information related to AI application adoption, usage, and risk for the users in your account.

## Overview

Cato provides a Predefined Report template, AI Security for Users, that summarizes AI application adoption, usage, and risk across the users in your account.

Create the template for a recurring or one-time report over the defined time range. By default, the Predefined Report template for the AI Security for Users report shows AI adoption, usage, and policy violation data for all users in your account for the past week.

For more about working with reports, see [Cato Reports](/v1/docs/cato-reports).

## Creating a Recurring AI Security for Users Report

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

## Creating a One-Time AI Security for Users Report

You can create a one-time report based on the AI Security for Users template. You define the **Filters** for the items included in the report.

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

## Understanding the AI Security for Users Report

The AI Security for Users report summarizes which AI applications are used in your account, who is using them, and how their usage aligns with your AI Security policies.

These are the sections in the report, the data is based on the report time range:

- AI Adoption Overview
  - **AI Applications by Users:** The number of users for each AI application
  - **AI Users:** The number of users who accessed AI applications or conducted AI interactions
  - **AI Interactions:** The number of AI interactions
  - **AI Applications:** The number of distinct AI applications used
- **AI Applications:** Top 25 AI applications with the **AI Risk Level** (for example Low, Medium, or High), the application **Category**, and the number of **AI Users** for each application
- **AI Users:** Top 25 users with AI activity, showing the user's **Department**, the number of **AI Applications** they used, and their number of **AI Interactions**
- AI Interaction Analysis
  - **Top AI Applications:** The AI applications with the most AI Interactions
  - **Topic Popularity:** The most common topics in AI interactions, such as General, Business Management, or Computing
- AI Interaction Policy & Violations
  - **Violations Breakdown:** Top 10 User Interaction Policy rules with the most violations
  - **User Interaction Policy Rules:** Top 25 policy rules, the AI Applications and AI Users they apply to, and the number of Violations they generated
