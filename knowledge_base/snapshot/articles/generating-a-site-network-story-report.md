---
title: "Generating Site Network Story Reports"
slug: "generating-a-site-network-story-report"
updated: 2026-08-16T11:14:45Z
published: 2026-08-16T11:14:45Z
canonical: "knowledge.catonetworks.com/generating-a-site-network-story-report"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating Site Network Story Reports

This article describes how to generate Cato Site Network Story reports that highlight network stories created for the different sites in your account.

## Overview

Cato provides Predefined Report templates that summarize data for all the Network stories detected for the sites in your account by the Cato XDR and ILMM services. This lets you generate a report that highlights the XDR and ILMM service capabilities for relevant stakeholders in the organization. The Site Network Story report includes data such as ISPs and sites that generated the most stories, and the total number and type of Network stories generated for each site in your account.

Create the template for the Scheduled or One-Time report and define the report time range. By default, the Predefined Report template for the Site Network Story report shows story data for the past month.

For more about working with reports, see [Cato Reports](/v1/docs/cato-reports).

![predefined_reports.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30650615535645.png)

### Prerequisites

- Site Network Story reports are available only for ILMM and NOCaaS customers. For more about subscribing to these services, please contact your Cato representative.

## Creating a Scheduled Site Network Story Report

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

## Creating a One-Time Site Network Story Report

Create a new One-time report template, and define the **Time Range** that the report covers.

**To create a one-time report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Catalog** tab, select the template you want to use to generate the report.
3. Select **Generate** > **Generate Now**.
4. Enter a **Report Name**.
5. Define the relevant **Filters** for your report. These are specific to the report type.
6. Define the **Timeframe** and **Timezone** of the report.
7. Select the **Format**: PDF or CSV.
8. Click **Generate**. The report is generated, and you can download it from the **Generated** tab.

## Understanding the Site Network Story Report

The sections in the Site Network Story Report show data for the configured time range. These are the sections:

- **Site Network Story Summary**
  - **Providers with Most Stories** - ISPs that generated the most Network XDR stories.
  - **Sites with Most Stories** - Sites in your account that generated the most Network XDR stories.
  - **Stories by Type** - Number of Network XOps stories detected for the account with breakdown by indication type. For more about the indications, see [Reviewing Site Operations Stories](/v1/docs/reviewing-site-operations-stories)
  - **Stories by Type Over Time** - Graph showing the number of detected stories over time, including a breakdown by indication type. The graph shows 6 months of data
- **Site Network Stories** -
  - **Site Network Story Breakdown** - Breakdowns by story indication type for each account site. For more about the indications, see [Reviewing Site Operations Stories](/v1/docs/reviewing-site-operations-stories).
