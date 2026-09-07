---
title: "Retrieving Diagnostic Data with Site Operations Story Actions"
slug: "retrieving-diagnostic-data-with-site-operations-story-actions"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/retrieving-diagnostic-data-with-site-operations-story-actions"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieving Diagnostic Data with Site Operations Story Actions

## Overview

Site Operations stories in the XOps platform let you perform actions to retrieve real-time diagnostic data related to the story. These actions help you accelerate root cause analysis and troubleshoot site-level connectivity or routing issues directly from the story drill-down page. When you retrieve the data, it appears on the story drill-down page, and the action is shown on the story timeline so you can easily access the data whenever you need. You can also export the data by copying it to the clipboard.

The data you can retrieve includes Traceroute and ICMP results, IPsec tunnel status, and BGP status.

## Retrieving and Exporting Traceroute and ICMP Results

For Site Operations stories with the indication **Link quality SLA**, you can export Traceroute and ICMP test results to investigate issues outside of the Cato network. This helps you identify last-mile connectivity problems and share diagnostic data with third parties, such as your Internet Service Provider (ISP).

Use the **Actions** menu In the story drill-down page to export the Traceroute and ICMP data. You can define which link you want to export data for, and select the specific incident based on the timestamp.

![DEM_Export_ISP_Data.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356111893021.png)

**To export Traceroute and ICMP results:**

1. In the story drill-down page, click the **Actions** button.
2. In the drop-down, select **Export data to ISP template**. The **Export data to ISP template** panel opens.

![Export_data_to_ISP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356143386269.png)
3. Select the incident you want to export data for, based on the incident time.
4. Select the link you want to export data for.
5. Click **Retrieve**. The data is shown in the **Underlay Raw Data** panel and a new entry is created in the story timeline.

Click **Copy** to export the data to the clipboard.

![DEM_Export_ISP_Data_Example.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356128579485.png)

## Retrieving and Exporting BGP Status Data

For Site Operations stories for sites using BGP, you can retrieve the real-time status of the BGP session to help investigate the issue. Use the **Actions** menu in the story drill-down page to retrieve the BGP status data.

For more about investigating stories with BGP data, see [XOps Network Playbook - BGP Session Disconnected](/v1/docs/xops-network-playbook-bgp-session-disconnected).

**To export BGP status data:**

1. In the story drill-down page, click the **Actions** button.
2. In the drop-down, select **Check BGP status**. The data is shown in the **Check BGP Status** panel and a new entry is created in the story timeline.

Click **Copy** to export the data to the clipboard.

![Site_Ops_Story_Actions_BGP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356121122589.png)

## Retrieving and Exporting IPsec Status Data

For stories generated for IPsec sites, you can retrieve a state summary of the site to help investigate the issue. Use the **Actions** menu in the story drill-down page to retrieve the last available snapshot of data for the site.

For more about troubleshooting issues with IPsec status data, see [Troubleshooting IPsec Connectivity](/v1/docs/troubleshooting-ipsec-connectivity).

> [!NOTE]
> Note:
> 
> If the site is disconnected no IPsec status data is retrieved.

**To export IPsec status data:**

1. In the story drill-down page, click the **Actions** button.
2. In the drop-down, select **Check IPsec status**. The data is shown in the **IPsec Status** panel and a new entry is created in the story timeline.

Click **Copy** to export the data to the clipboard. ![Site_Ops_Story_Actions_IPsec.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356143555997.png)
