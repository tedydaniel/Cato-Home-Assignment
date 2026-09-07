---
title: "Generating XOps Network Monitor Reports"
slug: "generating-an-xops-network-monitor-report"
updated: 2026-08-16T11:14:45Z
published: 2026-08-16T11:14:45Z
canonical: "knowledge.catonetworks.com/generating-an-xops-network-monitor-report"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating XOps Network Monitor Reports

This article describes how to generate Cato XOps Network Monitor reports that highlight the Network stories created for your account and present insights about your account's overall network performance.

**Note:** XOps is Cato’s unified analytics layer for security and operations, offering insights and guided remediation. XOps has replaced XDR, for more information, see [XOps FAQ](/v1/docs/xops-faq).

## Overview

Cato provides Predefined Report templates that summarize data for all the Network stories detected for your account by the Cato XOps (formerly XDR) service. This lets you generate a report that highlights the comprehensive network detection capabilities of Cato XOps for relevant stakeholders in the organization. The XOps Network Monitor report includes data such as the total number of Network stories created with breakdown by Criticality, and sites with the most Network stories.

Create the template for a recurring or one-time report and define the report time range. By default, the Predefined Report template for the XOps Network Monitor report shows story data for the past week.

For more about working with reports, see [Cato Reports](/v1/docs/cato-reports).

![predefined_reports.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30650611067933.png)

### Known Limitations

XOps Network Monitor reports do not support filtering by sites or SDP users. If any filters are configured, they will not be expressed in the report and it will show data for all sites and SDP users.

## Creating a Recurring XOps Network Monitor Report

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

## Creating a One-Time XOps Network Monitor Report

You can create a one-time report based on the XOps Network template. You define the **Filters** for the items included in the report.

**To create a one-time report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Catalog** tab, select the template you want to use to generate the report.
3. Select **Generate** > **Generate Now**.
4. Enter a **Report Name**.
5. Define the relevant **Filters** for your report. These are specific to the report type.
6. Define the **Timeframe** and **Timezone** of the report.
7. Select the **Format**: PDF or CSV.
8. Click **Generate**. The report is generated, and you can download it from the **Generated** tab.

## Understanding the XOps Network Monitor Report

The sections in the XOps Network Monitor Report show data for the configured time range. These are the sections:

- **Top 10 Sites by Number of Stories** - Sites in the account with the most Network XOps stories
- **Stories by Type** - Number of Network XOps stories detected for the account with breakdown by indication type. For more about the indications, see [Reviewing Site Operations Stories](/v1/docs/reviewing-site-operations-stories)
- **Stories by Type Over Time** - Graph showing the number of detected stories over time, including a breakdown by indication type. The graph shows 6 months of data
- Breakdowns by site for each story indication type, including:
  - **Link Down Stories by Site**
  - **Site Down Stories by Site**
  - **Link Quality SLA Stories by Site**
  - **BGP Session Disconnected Stories by Site**
  - **LAN Monitoring Host Unreachable Stories by Site**
  - **Socket HA Status is Not Ready Stories by Site**
