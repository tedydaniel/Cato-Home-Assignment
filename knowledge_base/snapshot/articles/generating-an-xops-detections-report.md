---
title: "Generating XOps Security Detections Reports"
slug: "generating-an-xops-detections-report"
updated: 2026-08-16T11:14:45Z
published: 2026-08-16T11:14:45Z
canonical: "knowledge.catonetworks.com/generating-an-xops-detections-report"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating XOps Security Detections Reports

This article describes how to generate Cato XOps Security Detections reports that highlight the XOps stories created for your account. It also presents insights about your account's overall security posture.

**Note:** XOps is Cato’s unified analytics layer for security and operations, offering insights and guided remediation. XOps has replaced XDR; for more information, see the [XOps FAQ](/v1/docs/xops-faq).

## Overview

Cato provides Predefined Report templates that summarize data for all the XOps (formerly XDR) Security stories detected for your account, regardless of whether the stories were investigated. This lets you generate a report that highlights Cato XOps' comprehensive threat detection capabilities for relevant stakeholders in the organization. The XOps Detections report includes data such as the total number of Security stories created, with a breakdown by Criticality, and the most common sites and indications of attack in XOps stories.

Create the template for a recurring or one-time report and define the report time range. By default, the Predefined Report template for the XOps Detections report shows story data for the past week.

For more about working with reports, see [Cato Reports](/v1/docs/cato-reports).

![predefined_reports.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30650626806941.png)

### Known Limitations

XOps Security Detections reports do not support filtering by sites or SDP users. If any filters are configured, they will not be reflected in the report, and the report will show data for all sites and SDP users.

## Creating a Recurring XOps Security Detections Report

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

## Creating a One-Time XOps Security Detections Report

You can create a one-time report based on the XOps Security Detections template. You define the **Filters** for the items included in the report.

**To create a one-time report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Catalog** tab, select the template you want to use to generate the report.
3. Select **Generate** > **Generate Now**.
4. Enter a **Report Name**.
5. Define the relevant **Filters** for your report. These are specific to the report type.
6. Define the **Timeframe** and **Timezone** of the report.
7. Select the **Format**: PDF or CSV.
8. Click **Generate**. The report is generated, and you can download it from the **Generated** tab.

## Understanding the XOps Security Detections Report

These are the sections in the XOps Security Detections report:

- **Executive Overview**
  - Overall totals of events and stories for the selected time range, including:
    - **All Events:** The total number of events for the account
    - **Security Events:** The number of events generated by the Cato security engines enabled for the account
    - **Stories Created:** The total number of XOps stories that were generated for the account
    - **High Criticality Stories:** The number of created stories with Criticality between 7-10
- **Created Stories by Criticality:** Number of stories generated for the account with breakdown by Criticality
  - High - Stories with a Criticality between 7-10
  - Medium - Stories with a Criticality between 4-6
  - Low - Stories with a Criticality between 1-3
- **Created Stories by Site:** Number of stories according to the site with the traffic that generated the story
- **Created Stories Over Time by Criticality:** Graph showing the number of created stories over time, including a breakdown by Criticality. The graph shows 6 months of data
- **Top 5 MITRE Techniques:** Top MITRE ATT&CK® techniques in stories created for the account. For more about the MITRE ATT&CK® framework, see [Using the MITRE ATT&CK® Dashboard](/v1/docs/using-the-mitre-att-ck-dashboard)
- **Top 5 Indications of Attack:** Top indications of attack in stories created for the account. For more about indications, see [Using the Indications Catalog](/v1/docs/using-the-indications-catalog)
- **Stories Created by Engine Type:** Number of stories generated for the account with breakdown by engine type. For more about the different XOps engines, see [Using the Indications Catalog](/v1/docs/using-the-indications-catalog)
- **Created Stories by Location:** Top 10 locations by country associated with threats detected in stories for the account. Threat locations include the locations of targets and sources in stories. Therefore, a single story can be associated with multiple threat locations
- **General Security Posture**
  - **Top Blocked Applications Internet Firewall:** Top applications blocked by the Internet Firewall, with the hit count
  - **Top Blocked Categories Internet Firewall:** Top categories blocked by the Internet Firewall, with the hit count
  - **Top Blocked Applications WAN Firewall:** Top applications blocked by the WAN Firewall with the hit count
  - **Top Blocked Categories WAN Firewall:** Top categories blocked by the WAN Firewall with the hit count
  - **IPS Events by Risk Level:** Chart showing breakdown of IPS block events by risk level
  - **Anti-Malware Block Events** Graph showing all the block events for the Anti-Malware service over the time range of the report
- **Created Stories**

This section lets you quickly review all the XOps stories created during the report time range.

These are the table columns:
  - **Link to Story:** Click to open the drill-down page for the story in the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench)
  - **Creation Date:** Date the story was created
  - **Story Duration:** Time passed from the first traffic flow for the story until the story was closed, or until the time the report was generated
  - **Indication:** Indicator of attack for the story. For more about Indications, see [Using the Indications Catalog](/v1/docs/using-the-indications-catalog)
  - **Type:** The XOps engine that created the story.
  - The **Criticality** of the story
  - **Site:** The site on your network with the traffic that generated the story.
  - **Source:** IP address, name of device, or SDP user on your network involved in the story
  - **Status:** The status of the story investigation at the time the report was generated. Possible values include: Open, Closed, Pending more info (including number of days pending)
