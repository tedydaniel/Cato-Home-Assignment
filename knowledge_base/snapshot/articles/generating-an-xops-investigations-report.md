---
title: "Generating XOps Security Investigations Reports"
slug: "generating-an-xops-investigations-report"
updated: 2026-08-16T11:14:45Z
published: 2026-08-16T11:14:45Z
canonical: "knowledge.catonetworks.com/generating-an-xops-investigations-report"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating XOps Security Investigations Reports

This article describes how to generate Cato XOps Security Investigations reports that highlight XOps story investigations, summarize data for security events, and present insights about your account's overall security posture.

**Note:** XOps is Cato’s unified analytics layer for security and operations, offering insights and guided remediation. XOps has replaced XDR, for more information, see [XOps FAQ](/v1/docs/xops-faq).

## Overview

Cato provides Predefined Report templates that summarize data related to the XOps (formerly XDR) stories investigated for your account. This lets you generate an XOps report that presents an overview of all story investigations, as well as breakdowns that focus on the most important ones, such as for malicious and suspicious stories.

Create the template for a recurring or one-time report and define the report time range. By default, the Predefined Report template for the XOps Investigations report shows story data for the past week.

For more about working with reports, see [Cato Reports](/v1/docs/cato-reports).

![predefined_reports.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30650611026205.png)

### Known Limitations

XOps Security Investigations reports do not support filtering by sites or SDP users. If any filters are configured, they will not be expressed in the report, and it will show data for all sites and SDP users.

## Creating a Recurring XOps Security Investigations Report

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

## Creating a One-Time XOps Investigations Report

You can create a one-time report based on the XOps Security Investigations template. You define the **Filters** for the items included in the report.

**To create a one-time report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Catalog** tab, select the template you want to use to generate the report.
3. Select **Generate** > **Generate Now**.
4. Enter a **Report Name**.
5. Define the relevant **Filters** for your report. These are specific to the report type.
6. Define the **Timeframe** and **Timezone** of the report.
7. Select the **Format**: PDF or CSV.
8. Click **Generate**. The report is generated, and you can download it from the **Generated** tab.

## Understanding the XOps Security Investigations Report

These are the sections in the XOps Security Investigations report:

- **Executive Overview**
  - Overall totals of events and stories for the selected time range, including:
    - **All Events:** The total number of events for the account
    - **Security Events:** The number of events generated by the Cato security engines enabled for the account
    - **Investigated Stories:** The total number of Detection & Response stories that were investigated and given a verdict in the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench)
    - **Suspicious and Malicious Stories:** The number of stories that were investigated and given a verdict of Suspicious or Malicious in the Stories Workbench
  - **Investigated Stories by Verdict:** Breakdown by verdict of all investigated stories
  - **Investigated Stories Over Time:** Graph showing the amount of investigated stories over time, including a breakdown by the threat type (for example: Suspicious Activity, Reputation, Policy Violation, Malware)
- **Malicious and Suspicious Stories**

Shows information about stories that received a verdict of Malicious or Suspicious, including:
  - **Malicious & Suspicious Stories by Threat Type:** Number of Malicious or Suspicious stories according to the type of threat (for example, Suspicious Activity, Reputation, Policy Violation, Malware)
  - **Malicious & Suspicious Stories by Site:** Number of Malicious or Suspicious stories according to site with the traffic that generated the story
  - **Malicious Stories by Severity:** Chart showing the number of Malicious stories by severity (High, Medium, Low)
  - **Malicious & Suspicious Stories by Location:** Graph showing Number of Malicious or Suspicious stories according to the location of the threat. Locations are based on the targets and sources in the story, and therefore one story can have multiple threat locations.
- **General Security Posture**
  - **Top Blocked Applications Internet Firewall:** Top applications blocked by the Internet Firewall, with the hit count
  - **Top Blocked Categories Internet Firewall:** Top categories blocked by the Internet Firewall, with the hit count
  - **Top Blocked Applications WAN Firewall:** Top applications blocked by the WAN Firewall with the hit count
  - **Top Blocked Categories WAN Firewall:** Top categories blocked by the WAN Firewall with the hit count
  - **IPS Events by Risk Level:** Chart showing breakdown of IPS block events by risk level
  - **Anti-Malware Block Events** Graph showing all the block events for the Anti-Malware service over the time range of the report
- **Investigation Audit**

This section lets you quickly review all the XOps story investigations that reached a verdict during the report time range. The information in the audit table reflects the state of the investigations at the time the report was generated.

These are the table columns:
  - **Link to Story:** Click to open the drill-down page for the story in the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench)
  - **Creation Date:** Date the story was created
  - **Indication:** Indicator of attack for the story. For more about Indications, see [Using the Indications Catalog](/v1/docs/using-the-indications-catalog)
  - **Type:** The XOps engine that created the story.
  - **Classification** of the threat type. For example: Suspicious Target, C&C, Suspicious Browser Extension, Scanner
  - **Verdict** for the story as determined by an analyst
  - **Severity** of the story as determined by an analyst (possible values: Low, Medium, High)
  - **Site:** The site on your network with the traffic that generated the story.
  - **Source:** IP address, name of device, or SDP user on your network involved in the story
  - **Status:** The status of the story investigation. Possible values include: Open, Closed, Pending more info (including number of days pending)
