---
title: "Generating Custom Reports"
slug: "generating-a-custom-report"
updated: 2026-08-16T11:14:45Z
published: 2026-08-16T11:14:45Z
canonical: "knowledge.catonetworks.com/generating-a-custom-report"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating Custom Reports

This article describes how to generate a custom report that includes any combination of widgets from all other predefined reports. You can configure the content and layout to help you design the perfect report for your use case.

## Overview

Cato provides predefined report templates for many different use cases. The custom report template allows you to create a template that includes widgets from all other templates.

For example, your CISO would like a weekly report on specific elements of your security profile. He has particular graphs he is interested in that are spread across the existing GenAI, Security Events, and Rule Hit Count templates. You can create a custom report template with the exact layout and content that your CISO requires.

For more about working with reports, see [Cato Reports](/v1/docs/cato-reports).

## Creating a Custom Report Template

Custom report templates can include any combination of widgets from all other predefined report templates. You create the template by defining the layout, as well as which widgets will be included in the report. This procedure describes how to create a custom template from scratch. If you want to start with one of the predefined templates instead, see [Editing a Predefined Report Template](/v1/docs/generating-a-custom-report#editing-a-predefined-report-template).

Note that some widgets are designed to be in larger layouts. Adding these widgets to pages without sufficient room may have unexpected results.

![custom_reports.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30650588436125.png)

**To create a Custom Report Template:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Catalog** tab, click **New Template**.
3. Enter a **Template Name**.
4. Define individual pages in the report:
  1. Define the **Page Name**.
  2. Define the **Number of Widgets** and the **Layout** of the page.
  3. On the menu on the left, click each widget to select which widget will be displayed. You can search for widgets by name or select a category to help you navigate the list of widgets.
  4. You can edit the name, number of items, and layout of each widget by clicking the three dots next to the widget after it has been added.
  5. Click the Plus icon to add additional pages.
5. Click **Save**. The template will be added to the **Catalog** tab, where you can modify it or generate the report.

## Editing a Predefined Report Template

Cato provides a number of predefined report templates that you can use as starting points to create a template. The predefined templates cannot be edited directly, but you can duplicate them and edit the duplicated version.

**To create a template based on a predefined template:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Catalog** tab, select the template you want to edit and click the three dots on the right of the page.
3. Click **Duplicate Template**.
4. Click the new template, and click **Edit**.
5. Define individual pages in the report:
  1. Define the **Page Name**.
  2. Define the **Number of Widgets** and the **Layout** of the page.
  3. On the menu on the left, click each widget to select which widget will be displayed. You can search for widgets by name or select a category to help you navigate the list of widgets.
  4. You can edit the name, number of items, and layout of each widget by clicking the three dots next to the widget after it has been added.
  5. Click the Plus icon to add additional pages.
6. Click **Save**.

## Generating a Recurring Custom Report

After creating a custom template, you use it to generate a report. You define the **Filters** for the items included in the report, as well the **Schedule** , which defines how often the report is generated - daily, weekly, or monthly. Generated reports are stored in the Cato Cloud, and they can be automatically emailed or downloaded.

You can select the Mailing List of email addresses for the recipients, which can include Cato Management Application admins and external users.

For more information about Mailing Lists, see [Working with Mailing Lists](/v1/docs/working-with-mailing-lists).

**To create a recurring Custom report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Catalog** tab, select the template you want to use to generate the report.
3. Click **Generate > Create Schedule**.
4. Enter a **Report Name**.
5. **(Optional)** In **Filters**, filter the report by status (passed or failed).
6. Define when the report will be generated and sent:
  1. Select the **Frequency** that the report is automatically sent: **Daily**, **Weekly**, or **Monthly**.
  2. For Weekly and Monthly Scheduled reports, in **Every** select the day that the report is sent.
7. In **Send to Mailing List**, select the **Mailing List** that receives the report.

You can click **New** to create a new mailing list.
8. Click **Save Schedule**. The report is added to the **Saved Reports** tab.

### Generating a Recurring Report On Demand

Recurring reports are automatically generated based on their schedule settings. For example, a weekly report configured for Monday, is generated every Monday. You can also choose to manually generate a recurring report on demand, in which case the generated report uses the defined time range based on the current day. If an admin manually generates a weekly report on a Tuesday, the time range for the report is the previous 7 days starting from that Tuesday, regardless of the starting day of the recurring report. For more information about the time range of recurring reports, see [Cato Reports](/v1/docs/cato-reports).

**To generate a recurring report on demand:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Saved Reports** tab, find the recurring report and click **Generate Now**.
3. From the **Generated PDFs** tab, find the report and click **Download**.

## Creating a One-Time Custom Report

You can create a one-time report based on a custom template. You define the **Filters** for the items included in the report.

**To create a one-time report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Catalog** tab, select the template you want to use to generate the report.
3. Select **Generate** > **Generate Now**.
4. Enter a **Report Name**.
5. Define the relevant **Filters** for your report. These are specific to the report type.
6. Define the **Timeframe** and **Timezone** of the report.
7. Select the **Format**: PDF or CSV.
8. Click **Generate**. The report is generated, and you can download it from the **Generated** tab.
