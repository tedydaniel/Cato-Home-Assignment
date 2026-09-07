---
title: "Generating Posture or Posture Compliance Reports"
slug: "generating-a-posture-or-posture-compliance-report"
updated: 2026-08-18T07:09:00Z
published: 2026-08-18T07:09:00Z
canonical: "knowledge.catonetworks.com/generating-a-posture-or-posture-compliance-report"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating Posture or Posture Compliance Reports

This article describes how to generate a report that summarizes areas where your account does and does not meet Cato's recommended best practices.

## Overview

Cato provides predefined report templates that summarize a snapshot of the data on the Best Practices page. This lets you generate reports that include the:

- **Posture (Best Practices) Report**: Evaluates the configurations and settings in your account and shows how they comply with Cato’s recommendations for optimal performance and security. For example, the report shows whether critical security services are enabled and can identify security rules that are too permissive. The assessment also focuses on detailed settings, such as whether specific risky categories and services are blocked.
- **Posture Compliance Report**: Maps compliance controls from leading compliance frameworks, including GDPR, ISO 27001:2022, and NIST SP 800-53 Rev. 5, to the relevant Cato posture checks. This helps you understand compliance coverage, identify gaps, and prioritize remediation based on the impact and status of each check.

Create the template for the recurring or one-time report with data from the status of the Best Practices page at the time the report is generated.

To review the checks for your account at a specific point in time, you can generate a Best Practices report from a date in the past. This capability helps you compare historical results with the current report to track improvements and demonstrate progress over time.

For more about working with reports, see [Cato Reports](/v1/docs/cato-reports).

## Creating a Recurring Posture or Posture Compliance Report

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

## Creating a One-Time Report

You can create a one-time report based on the Best Practices template. You define the **Filters** for the items included in the report.

**To create a One-Time report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Catalog** tab, select the template you want to use to generate the report.
3. Select **Generate** > **Generate Now**.
4. Enter a **Report Name**.
5. **(Optional)** In **Filters**, add a filter to the report so it only includes specific data.

To generate a report for a specific compliance framework, add a filter this filter:
  - **Field**: Compliance
  - **Operator**: is
  - **Value**: Your chosen compliance framework
6. Enter the start date for the information to be included using the **Date** option.
7. Select the **Format**: PDF or CSV.
8. Click **Generate**. The report is generated, and you download it from the **Generated** tab.

## Downloading Report PDFs

Download a Recurring or One-Time report as a PDF from the Generated PDFs tab. You can use the **Reload** button to refresh the Generated PDFs tab and see if the report is **Ready** to download.

Admins with viewer permissions are allowed to download reports.

**To download the PDF of a report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Generated PDFs** tab, find the report and click **Download**.
3. To delete a Generated PDF, click the More button ![more.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35883092649117.png) and select **Delete**.

## Understanding the Best Practices Report

These are the sections in the Best Practices report:

- **Best Practices Overview:** Displays the Cato Score, the percentage of passed and failed checks, and the last time the Best Practices was updated for this report.
- **Best Practice Categories:** Each category has a table with the Best Practices information for all checks performed on that category. For example, Internet Firewall and Threat Prevention each have their own tables with the full details of their Best Practices checks.

## Understanding the Posture Compliance Report

These are the sections in the Posture Compliance Report:

- **Best Practices Overview:** Displays the Cato Score, the percentage of passed and failed checks, and the last time the Best Practices was updated for this report.
- **Compliance Requirement:** Each compliance requirement includes a table that lists the posture checks used to satisfy it.

## Modifying a Predefined Report Template

You can create custom report templates based on one of the predefined report templates. This allows you to quickly generate reports designed for your exact needs, while benefiting from the basic composition and design of our predefined templates.

For details, see [Generating a Custom Report](/v1/docs/generating-a-custom-report).
