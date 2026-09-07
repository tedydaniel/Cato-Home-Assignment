---
title: "Generating Executive Reports"
slug: "generating-executive-reports"
updated: 2026-08-16T11:14:45Z
published: 2026-08-16T11:14:45Z
canonical: "knowledge.catonetworks.com/generating-executive-reports"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating Executive Reports

## Overview

Cato Executive Report gives executives a single, high-level view of account health across networking, security, applications, users, and operations. It helps quickly identify the trends, risks, and usage patterns that matter most for leadership reviews without manually collecting data from multiple pages. The report combines selected widgets from other Cato reports. It also includes dedicated views for User Risk and License Utilization so that you can highlight exposure, adoption, and operational priorities in one place.

You can generate the Executive Report as either a one-time or recurring report.

For more about working with reports, see [Cato Reports](/v1/docs/cato-reports).

## Creating a Recurring Executive Report

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

## Creating a One-Time Executive Report

Create a new One-Time report template and define the Filters for the items included in the report. Then define the Time Range that the report covers.

**To create a one-time report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Catalog** tab, select the template you want to use to generate the report.
3. Select **Generate** > **Generate Now**.
4. Enter a **Report Name**.
5. Define the relevant **Filters** for your report. These are specific to the report type.
6. Define the **Timeframe** and **Timezone** of the report.
7. Select the **Format**: PDF or CSV.
8. Click **Generate**. The report is generated, and you can download it from the **Generated** tab.

## Understanding the Executive Report

These are the sections in the Executive Report:

- Sites Overview
  - **Sites Total Upstream and Downstream Traffic Over Time**: Total upstream and downstream traffic for all sites
  - **Top Sites by Total Traffic**: Sites with the highest total traffic volume
  - **Top Sites by Average Latency**: Sites with the highest average latency
  - **Top Sites by Max Latency**: Sites with the highest maximum latency
  - **Total sites: Lost Packets Upstream %**: Upstream packet loss percentage for sites
  - **Total sites: Lost Packets Downstream %**: Downstream packet loss percentage for sites
  - **Top Sites Packet Discard Over Time**: Packet discard data for top sites
- Users Overview
  - **Remote users Total Upstream and Downstream Traffic Over Time**: Total upstream and downstream traffic for remote users
  - **Remote users Total Upstream and Downstream Traffic**: Total remote user traffic by direction
  - **Number of Remote Users Connected per Day**: Number of remote users connected each day
  - **Distribution of devices by OS**: Remote user devices by operating system
  - **Number of Windows clients by version**: Windows Client versions used in the account
  - **Number of macOS clients by version**: macOS Client versions used in the account
  - **Number of Remote Users per PoP**: Remote user distribution by PoP
  - **Number of Remote Users per Country**: Remote user distribution by country
  - **Top Risky Users**: Users with the highest average risk score
  - **Avg. User Risk Score Over Time**: Average user risk score over the report period
- License Utilization
  - **License Usage Overview**: Allocated and total license usage
  - **Services**: Enabled and disabled services, plans, and status
  - **Purchased Services**: Purchased services for the account
- Posture
  - **Posture Score**: Passed and failed best practice checks and the overall posture score
  - **Posture Score Over Time**: Posture score trends by category
  - **TLS Inspection status**: Current TLS Inspection status
  - **IPS status**: Current IPS status
- Security
  - **Block Security Events over Time**: Blocked security events over the report period
  - **Top Block Events**: Security engines with the most blocked events
  - **Top Sites by Block Security Events**: Sites with the most blocked security events
  - **Top Users by Block Security Events**: Users with the most blocked security events
- Internet Firewall
  - **Block and Prompt Events over Time - Internet Firewall**: Internet Firewall block and prompt events over the report period
  - **Top Blocked Categories - Internet Firewall**: Categories with the most blocked Internet Firewall events
  - **Top Blocked Applications - Internet Firewall**: Applications with the most blocked Internet Firewall events
  - **Top Blocked Domains - Internet Firewall**: Domains with the most blocked Internet Firewall events
- IPS and TLS Inspection
  - **Top Threat Types - IPS**: Threat types with the most IPS events
  - **Block Events over Time - IPS**: Blocked IPS events over the report period
  - **Top Users By IPS Events**: Users with the most IPS events
  - **Inspected VS Bypassed**: Inspected and bypassed TLS traffic
  - **Top Inspected Applications by Hits - Outbound**: Outbound applications with the most inspected hits
  - **Top Bypassed Applications by Hits - Outbound**: Outbound applications with the most bypassed hits
- Applications
  - **Total Traffic by Application Type**: Total traffic for Cloud/SaaS and On Premise applications
  - **Top Applications by Sites**: Applications used by the highest number of sites
  - **Top Applications by Downstream Traffic**: Applications with the highest downstream traffic
  - **Top Application Categories by Traffic**: Application categories with the highest traffic
  - **Sanctioned vs Unsanctioned Applications**: Sanctioned and unsanctioned applications
  - **Application Traffic by Risk**: Traffic by application risk level
  - **Applications by Risk**: Number of applications by risk level
  - **Top Best Performing Applications**: Applications with the best average experience
  - **Top Worst Performing Applications**: Applications with the worst average experience
- GenAI
  - **Top Applications by Usage - GenAI Apps**: GenAI applications with the highest usage
  - **Sanctioned vs Unsanctioned Applications - GenAI Apps**: Sanctioned and unsanctioned GenAI applications
  - **Top Risky Applications - GenAI Apps**: Risky GenAI applications used in the account
- Experience Monitoring
  - **Average Experience Score over Time**: Average experience score over the report period
  - **Avg. Experience For Most Active Users**: Experience score and usage for the most active users
  - **Experience Monitoring - Top Sites per Usage**: Sites with the highest usage and their average experience
  - **Experience Monitoring - Top Applications per Usage**: Applications with the highest usage and their average experience
- XOps
  - **Created Stories by Criticality**: Created stories by criticality
  - **Total Investigated Stories**: Number of investigated stories
  - **Threat types by number of malicious & suspicious stories**: Threat types found in malicious and suspicious stories
  - **Stories by type - Operational Stories with breakdown by type**: Operational story types
