---
title: "Generating User Reports"
slug: "generating-a-user-report"
updated: 2026-08-16T11:14:45Z
published: 2026-08-16T11:14:45Z
canonical: "knowledge.catonetworks.com/generating-a-user-report"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating User Reports

This article describes how to generate a Cato Analytics report that highlights data related to the user's connectivity in your account.

## Overview

Cato provides a Predefined Report template that summarizes user connectivity in your account.

You can use this template to generate either a one-time or recurring report. When generating the report, you select the specific time range, sites, and SDP users to include. By default, the report includes data for all sites and SDP users over the past week.

For more about working with reports, see [Cato Reports](/v1/docs/cato-reports).

![reports_catalog_user_report.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36085136185117.jpeg)

## Creating a Recurring User Report

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

## Creating a One-Time User Report

You can create a one-time report based on the User report template. You define the **Filters** for the items included in the report.

**To create a one-time report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Catalog** tab, select the template you want to use to generate the report.
3. Select **Generate** > **Generate Now**.
4. Enter a **Report Name**.
5. Define the relevant **Filters** for your report. These are specific to the report type.
6. Define the **Timeframe** and **Timezone** of the report.
7. Select the **Format**: PDF or CSV.
8. Click **Generate**. The report is generated, and you can download it from the **Generated** tab.

## Understanding the User Report

These are the graphs in the User report:

- **Users Connected per Day:** The total number of users connected to the Cato Cloud per day
- **Users per Country:** The total number of users connected to the Cato Cloud per country
- **Users per PoP:** The total number of users that connected to the Cato Cloud per PoP location
- **OS Distribution:** Clients per OS that connected to the Cato Cloud
- **Windows Client Version:** The number of users that connected to the Cato Cloud using each Windows Client version
- **Windows Distribution:** Clients per Windows version that connected to the Cato Cloud
- **macOS Client Version:** The number of users that connected to the Cato Cloud using each macOS Client version
- **macOS Distribution:** Clients per macOS version that connected to the Cato Cloud
- **Linux Client Version:** The number of users that connected to the Cato Cloud using each Linux Client version
- **Linux Distribution:** Clients per Linux version that connected to the Cato Cloud
- **iOS Client Version:** The number of users that connected to the Cato Cloud using each iOS Client version
- **iOS Distribution:** Clients per iOS version that connected to the Cato Cloud
- **Android Version:** The number of users that connected to the Cato Cloud using each Android Client version
- **Android Distribution:** Clients per Android version that connected to the Cato Cloud
