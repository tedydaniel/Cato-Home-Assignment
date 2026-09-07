---
title: "Cato Reports"
slug: "cato-reports"
updated: 2026-08-16T11:14:45Z
published: 2026-08-16T11:14:45Z
canonical: "knowledge.catonetworks.com/cato-reports"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Reports

## Overview

You can use the Cato Management Application (CMA) to generate different types of granular and flexible reports that highlight various aspects of your Cato account. These reports can be useful for multiple stakeholders in the organization, from executives to CISO/CIO and IT professionals. You can create recurring reports that are automatically generated and emailed, or generate a one-time report to download from the CMA.

The CMA includes a number of predefined report templates for common scenarios, such as security incidents, network usage, and best practices. You can also create a custom template to define which widgets are included in the report.

The templates are granular and let you specify which sites, users, or other items are included in the report over the defined time range.

### Recurring and One-Time Reports

You can create these kinds of predefined reports:

- Recurring report - A report that is automatically generated and emailed to the [Mailing List](/v1/docs/working-with-mailing-lists) on a daily, weekly, or monthly schedule

You can also download the report from the **Generated PDFs** tab.
- One-Time report - A report that is generated on demand

Create a new report template, or use an existing one, and then generate the PDF and download it from the **Generated PDFs** tab

### Predefined Cato Report Templates

For the full list of predefined report templates, see [Cato Reports](/v1/docs/cato-reports)

## Creating Recurring Reports

Recurring reports are automatically emailed to the recipients defined in the Mailing List for that report. You can define reports to only show data for certain items (such as specific sites and/or SDP users) and define the frequency which the report is generated. For weekly reports, select the day of the week that the report starts on, for monthly reports, select the day or the first day of the month.

Recurring report time ranges start on 00:00 in your selected time zone.

The reports may take a few hours after their scheduled time to be generated and sent.

## Generating One-Time Reports

One-time reports show the relevant data and information in your account over the time range for the report. You can define reports to only show data for certain items (such as specific sites and/or SDP users) and customize the time range for the report.

### Understanding the Report Time Range

By default, the Predefined Report templates show data and information for all sites and SDP users for the past week. The **Time Range** of the report defines the range of data that is included when you generate the report. For example, if you create and generate a report on May 7 to show data for the **Last Week**, it shows data from May 1 - 7. When you generate this report again on May 20, it shows data from May 14 - 20.

For standard time ranges, if your range is 24 or 48 hours, the report ends exactly when you generate it and goes back exactly 24 or 48 hours. If your range is longer, reports always start and end at midnight and will not include data from the current day.

For custom time ranges (e.g. June 25-June 28), the report will include data from 00:00 June 25 in your time range until 00:00 June 29, no matter how many times you generate the report. The time in the report is displayed in your selected time zone.

The maximum **Time Range** for a report is three months. For example, you can define the start date five months earlier, however, the maximum time range of the report is three months after the start date.

The earliest start date (**From**) of the predefined report is based on the [Data Processing Agreement (DPA) for your account](/v1/docs/guide-to-cato-data-lake). The default data retention period for an account is 3 months.

![PredefinedReports.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26983590951325.png)

<editor360-custom-block data-preprocessing="true" data-sanitizationtags="a"><h2 data-block-id="msri6dpn-l60icb-094" class="title" id="downloading-reports"><a id="UUID-d6ca59f0-b7ed-badb-dbaf-f58de7dba913_section-idm293494285885250" display="false" data-zd-article="UUID-d6ca59f0-b7ed-badb-dbaf-f58de7dba913"></a>Downloading Reports</h2></editor360-custom-block>

Download your scheduled or one-time reports from the **Generated** tab. You can use the **Reload** button to refresh the Generated tab and see if a report is **Ready** to download. It may take a few minutes to generate reports with large amounts of data. Recurring reports are **In Progress** when they are automatically emailed. To download recurring reports, generate a new report in the **Saved Reports** tab and then download it. You can use the **Reload** button to refresh the reports to see whether it’s **Ready** to download.

Admins with viewer permissions are allowed to download reports.

![GeneratedReports.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26983606009117.png)

**To download a report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Generated** tab, find the report and click **Download**.
3. To delete a report, click ![more.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29146153826077.png) and select **Delete**.

## Generating Reports Longer Than One Week

Reports for time ranges longer than 1 week may show inaccurate data in time series graphs when the selected time zone differs significantly from UTC. This issue occurs because daily data aggregation is based on UTC day boundaries. To avoid this discrepancy, we recommend using UTC as the time zone for these reports.
