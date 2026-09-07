---
title: "Generating Network Analytics Reports"
slug: "generating-a-network-analytics-report"
updated: 2026-08-16T11:14:45Z
published: 2026-08-16T11:14:45Z
canonical: "knowledge.catonetworks.com/generating-a-network-analytics-report"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating Network Analytics Reports

This article explains how to generate a Cato Network Analytics report that highlights data related to network usage for sites and SDP users in your account.

## Overview

Cato provides a Predefined Report template that summarizes WAN and Internet network usage for sites and SDP users. In addition, it includes the SLA metrics for site traffic: packet loss, discarded packets, jitter, and latency.

Create the template for a recurring or one-time report with the sites and SDP users that are included in the report over the defined time range. By default, the Predefined Report template for the Network Analytics report shows traffic and data for all sites and SDP users for the past week.

For more about working with reports, see [Cato Reports](/v1/docs/cato-reports).

![predefined_reports.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/30650626887069.png)

## Creating a Recurring Network Analytics Report

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

## Creating a One-Time Network Analytics Report

You can create a one-time report based on the Network Analytics template. You define the **Filters** for the items included in the report.

**To create a one-time report:**

1. From the navigation pane, select **Home > Reports**.
2. From the **Catalog** tab, select the template you want to use to generate the report.
3. Select **Generate** > **Generate Now**.
4. Enter a **Report Name**.
5. Define the relevant **Filters** for your report. These are specific to the report type.
6. Define the **Timeframe** and **Timezone** of the report.
7. Select the **Format**: PDF or CSV.
8. Click **Generate**. The report is generated, and you can download it from the **Generated** tab.

## Understanding the Network Analytics Report

For sections in the report that show the top sites, charts that show over time show the top three sites, other charts show the top ten sites.

- Latency measures round trip time inside the tunnel between the site and the PoP in the Cato Cloud
- Jitter is the difference in time delay in milliseconds (ms) between data packets
- Packets discarded is the number of packets discarded by the QoS engine due to congestion
- Packets lost is the number or percentage of dropped packets inside the tunnel between the site and the PoP in the Cato Cloud

These are the sections in the Network Analytics report:

- Traffic Summary
  - **Sites Total Traffic:** Chart showing volume and percentage of upstream and downstream traffic for all sites
  - **Sites Total Traffic Over Time:** Timeline that shows the total upstream and downstream traffic for all sites over the time range
  - **SDP Users Total Traffic:** Chart showing volume and percentage of upstream and downstream traffic for all SDP users
  - **SDP Users Total Traffic Over Time:** Timeline that shows the total upstream and downstream traffic for all SDP users over the time range
- Top Sites by Traffic Consumption
  - **Top Sites by Total Traffic:** Top sites according to total upstream and downstream traffic
  - **Top Sites Traffic Over Time:** Timeline that shows the upstream and downstream traffic for the top three sites over the time range
- SLA Metrics
  - **Top Sites by Average Latency:** Average latency (in ms) for the top sites over the time range
  - **Top Sites by Max Latency:** Maximum latency for the top sites over the time range
  - **Top Sites by Average Jitter Downstream:** Average downstream jitter for the top sites over the time range
  - **Top Sites by Average Jitter Upstream:** Average upstream jitter for the top sites over the time range
- Total Sites Packet Loss
  - **Lost Packets Downstream:** Chart showing downstream packet loss (number of lost packets) for all sites over the time range
  - **Lost Packets Upstream:** Chart showing upstream packet loss (number of lost packets) for all sites over the time range
  - **Lost Packets Downstream %:** Chart showing downstream packet loss (percentage) for all sites over the time range
  - **Lost Packets Upstream %:** Chart showing upstream packet loss (percentage) for all sites over the time range
- Total Sites Packet Discard
  - **Packets Discarded Downstream:** Chart showing downstream discarded packets by the QoS engine (number of discarded packets) for all sites over the time range
  - **Packets Discarded Upstream:** Chart showing upstream discarded packets by the QoS engine (number of discarded packets) for all sites over the time range
  - **Packets Discarded Downstream %:** Chart showing downstream discarded packets by the QoS engine (percentage) for all sites over the time range
  - **Packets Discarded Upstream %:** Chart showing upstream discarded packets by the QoS engine (percentage) for all sites over the time range
- Top Sites Dropped Traffic
  - **Top Sites Packet Loss Over Time:** Timeline that shows the total packet loss (number of lost packets) for upstream and downstream traffic for the top three sites over the time range
  - **Top Sites Packet Discarded Over Time:** Timeline that shows the total packets discarded by the QoS engine (number of lost packets) for upstream and downstream traffic for the top three sites over the time range
- Site Traffic Details - The table shows the following details for up to 100 top sites according to the total traffic volume, sorted in alphabetical order:
  - **Site Name:** Name of the site
  - **Port:** Name for the port (defined in the Cato Management Application)
  - **Bytes Total:** Total traffic for the port in this site
  - **Bytes Upstream:** Total upstream traffic for the port in this site
  - **Bytes Downstream:** Total downstream traffic for the port in this site
  - **Throughput (Max):** Maximum throughput for upstream and downstream traffic for the port in this site
  - **Throughput Downstream (Max):** Maximum throughput for downstream traffic for the port in this site
  - **Throughput Upstream (Max):** Maximum throughput for upstream traffic for the port in this site
- Sites SLA Metrics - The table shows the following SLA details for up to 100 top sites according to the total traffic volume, sorted in alphabetical order:
  - **Site Name:** Name of the site
  - **Interface Name:** Name for the interface (defined in the Cato Management Application)
  - **Latency RTT (avg):** Average round trip time (RTT) for the interface in this site
  - **Jitter Upstream (avg):** Average upstream jitter for the interface in this site
  - **Jitter Downstream (avg):** Average downstream jitter for the interface in this site
  - **Discarded Packets Downstream:** Number of packets discarded by the Cato QoS engine for downstream traffic for the interface in this site
  - **Discarded Packets Upstream:** Number of packets discarded by the Cato QoS engine for upstream traffic for the interface in this site
  - **Lost Packets Downstream:** Number of packets lost for downstream traffic for the interface in this site
  - **Lost Packets Upstream:** Number of packets lost for upstream traffic for the interface in this site
