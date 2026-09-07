---
title: "Reviewing Site Operations Stories"
slug: "reviewing-site-operations-stories"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/reviewing-site-operations-stories"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reviewing Site Operations Stories

This article discusses how you can use the Stories Workbench to review Site Operations stories for connectivity and performance issues on your network.

## Overview

Cato XOps identifies network issues such as degradation, in addition to potential security threats. The advanced Site Operations engine detects different indications and metrics related to connectivity and performance, and generates stories that correlate data for issues concerning the network. For example, if a WAN link is intermittently experiencing high packet loss, the engine will create a single story with all the relevant data for the link.

The Stories Workbench page shows the details of each story to help you understand and analyze the issues. You can sort and filter the stories to find the most important incidents, and then drill-down on a story to further investigate the details to resolve the issue.

### Site Operations Story Indications

These are the indications of network connectivity and performance issues that are detected by the Site Operations engine to generate stories:

| Indication | Description | Threshold for Generating a Story |
| --- | --- | --- |
| **Site down** | The site disconnected from the Cato Cloud. | All links are down for 2.5 minutes |
| **Link is down** | One of the WAN links for a site disconnected from the Cato Cloud, the site is still connected. | A link is down for 5 minutes, or a link had 5 shorter disconnections in a 10-minute period |
| **BGP session disconnected** | A BGP session unexpectedly disconnected, which can impact app connectivity and the user experience. | A BGP session is down for 5 minutes or had 5 or more shorter disconnections in a 10 minute period |
| **LAN monitoring - host unreachable** | A monitored host behind a site isn’t responding to keep-alive packets from the PoP and is considered unreachable. Requires a [LAN Monitoring](/v1/docs/configuring-lan-monitoring-for-a-site) rule configured for the host. | One LAN Monitoring Unreachable event |
| **Link quality SLA** | The link SLA quality threshold for a site is exceeded. This can impact user experience. The SLA thresholds are configured for [Quality Health Rules](/v1/docs/working-with-link-health-rules). **Notes:** - Congestion issues for a link are excluded from Link quality SLA stories. - For ILMM customers, jitter and latency based stories are not generated. | One Quality Health Rule event |
| **Socket HA Not Ready status** | There is an issue with the Socket High Availability (HA) configuration, and the status is Not Ready. | If one of the following Socket HA Not Ready conditions occurs: - **Connected** is not ready for 5 minutes - **Keepalive** is not ready for 60 minutes - **Compatible version** is not ready for 60 minutes - **Failover** to secondary socket for 60 minutes For more about these conditions, see [What is Socket HA](/v1/docs/what-is-socket-ha) |
| **PoP reconnect to improve connectivity** | The site was forced to reconnect to the PoP to optimize performance. Reconnecting to the PoP can impact user experience. | One reconnect event with this message: **Performance issue detected, reconnected to a different service node in the Cato Cloud** For more about event message fields, see [Understanding Socket Connectivity Event Message Fields](/v1/docs/understanding-socket-connectivity-event-message-fields) |
| **LAN port down** | One of the LAN ports disconnected | The port is down for 5 minutes |
| **Alt WAN link down** | One of the Alt. WAN links disconnected | The link is down or the number of channels dropped to 0 for 5 minutes |
| **Socket Offline After Upgrade** | A Socket did not re-establish a tunnel within the expected time after upgrading to a new version. | Socket is disconnected for 5 minutes after completion of expected upgrade time |

### Understanding the Site Operations Story Lifecycle

Site Operations stories move through different stages throughout the story lifecycle, from the initial issue that triggered the story, through the final resolution. However, the story lifecycles are slightly different for **Site down** stories versus other story types. This is because when a **Site down** story is ongoing, no other stories for the site are created to avoid the creation of redundant stories.

For example, if a site with two WAN links goes down, a single **Site down** story is generated without separate **Link down** stories for each WAN link.

Below are the potential stages for a **Site down** story and other story types:

- Stages in the **Site down** story lifecycle:
  1. Open - the issue is currently in progress, and the story is created
  2. Monitoring - The issue has been resolved for less than 2 hours
  3. Closed - The issue has been resolved for 2 hours, and the story is closed
- Stages in the lifecycle of other story types:
  1. On hold - The issue is in progress, but no story is created because the site is currently down. The issue remains on hold until 2 minutes have passed after the **Site down** story is closed
  2. Open - the issue is currently in progress, and the story is created
  3. Monitoring - The issue has been resolved for less than 2 hours
  4. Closed - The issue has been resolved for 2 hours, and the story is closed

**Note:** Site Operations stories are also automatically closed in the following cases:

- 30 days old – Closed to ensure fresh tracking if the issue recurs
- Story requires revalidation – The Site Operations engine determined that the story needs to be revalidated. The engine validates and reopens the story if the issue recurs
- Configuration change – An entity in the story (link, site, BGP range, host) is no longer relevant due to configuration updates

### Example Use Case

This is an example use case for an admin identifying and resolving a Site Operations network story with the Stories Workbench:

- Filtered the Stories Workbench to show open Site Operations stories grouped by site
- Identified a high criticality story for the New York site, with the indication **Link is down**
- Opened the drill-down page for the story, reviewed the story data, and discovered the site's WAN 01 link was disconnected from the Cato Cloud
- Reviewed the relevant [playbook](/v1/docs/reviewing-site-operations-stories#investigating-stories-with-playbooks) to investigate and troubleshoot the issue
- After checking the physical Socket at the New York site, discovered the WAN 01 link cable was faulty
- Replaced the cable, confirmed the link was up and connected, and continued to monitor the story for possible recurrence of the issue
- Story automatically closed after two hours with no recurrence

## Showing the Stories Workbench Page

The Stories Workbench page shows a summary of the XOps stories for your account.

**To view the Stories Workbench page:**

- From the navigation menu, click **Home > Stories Workbench**.

### Understanding the Stories Columns

![Detection___Response_Workbench_w_Network.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356111483933.png)

| Column | Description |
| --- | --- |
| **ID** | Unique Cato ID for this story |
| **Status** | The statuses for a Site Operations story represent different stages throughout the story lifecycle, from the initial issue that triggered the story, through the final resolution. The Site Operations engine automatically updates the status when it detects the relevant changes in the network incident. These are the status types: - **Open** - The Site Operations engine detected a network issue that triggered the generation of a story - **Monitoring** - The Site Operations engine detected that the initial issue is resolved, and continues monitoring for a recurrence for two hours. If a recurrence is detected, the status changes back to **Open** - **Closed** - A story with a status of **Monitoring** changes to **Closed** when there is no detected recurrence for two hours. > [!NOTE] > Note: > > Only Site Operations stories close automatically, and only after 120 minutes that the issue no longer occurs. XOps Security stories do not close automatically. |
| **Created** | Date of the first traffic flow for the story |
| **Updated** | Date of the most recent traffic flow for the story |
| **Criticality** | - The potential impact of the issue on your network. Values are from 1 (low impact) to 10 (high impact) |
| **Indication** | - Indication of the network issue for the story |
| **Source** | - The site where the network issue is occurring |
| **Occurrences** | The number of times the issue occurred, including recurrences after a temporary resolution. For example, if a link repeatedly disconnects and reconnects, each disconnection counts as an occurrence |
| **Engine Type** | The engine that created the story. For Site Operations stories, the engine is Site Operations |

## Grouping the Stories

To provide context when reviewing the stories, you can show the stories in groups defined by details including **Sources**, **Indication**, **Status**, and **Type**. For example, you can show together all of the stories related to a specific source site, or all of the **Link quality SLA** stories. This gives you a broader perspective when analyzing the stories, and can help you more quickly understand and resolve issues.

For Site Operations stories, **Sources** are sites in your network.

We recommend as a best practice to begin your analysis of Network stories by grouping by **Sources**.

Each group highlights the criticality levels for the stories in that group, including the number of high, medium, and low criticality stories.

![Stories_Workbench_Grouping.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356142925981.png)

**To group the stories in the Stories Workbench:**

1. From the navigation menu, click **Home > Stories Workbench**.
2. From the **Group By** drop-down menu, select the required criterion.

The stories are shown in expandable groups.

## Filtering the Stories

There are three ways to filter the data in the Stories Workbench:

- Select a preset filter
- Automatically update the filter with a selected item
- Manually configure the filter

### Preset Filters

You can select a preset filter to focus on either **Network Operations** or **Security Operations** stories. When you select a preset filter, the story columns most relevant for that type of story are shown by default.

**To select a preset filter:**

1. In the filter bar, click the **Select Presets** dropdown menu.
2. Select the preset. The Stories Workbench is updated to show the stories that match the preset.

### Automatically Filtering for an Item

As you hover over an item or field where a filter option is available, the ![TD_Filter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356150671389.png) button appears. Click the icon to show the filter options:

- **Add to Filter** - Adds the item to the filter, and the Stories Workbench now only shows stories that include this item. For example, if you filter for a specific Criticality score, the page only shows stories with that Criticality.
- **Exclude from Filter** - Updates the filter to exclude this item, and the Stories Workbench now only shows stories that do NOT include this item.

You can continue to add items to the filter, click ![TD_Filter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356150671389.png) again to update the filter and drill-down further.

### Selecting the Time Range

The default time range for the Stories Workbench is the previous two days. You can select a different time range to show a longer or shorter time period. For more information, see [Setting the Time Range Filter](/v1/docs/setting-the-time-range-filter).

The maximum date range for the Stories Workbench is 90 days.

### Manually Configuring the Filter

You can manually configure the story filter for greater granularity to analyze the stories. After you configure the filter, it is added to the stories filter bar and the page is automatically updated to show the stories that match the new filter.

**To create a filter:**

1. In the filter bar, click ![Add2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356150713117.png).
2. Start typing or select the **Field**.
3. Select the **Operator**, which determines the relationship between the **Field** and the **Value** you are searching for.
4. Select the **Value**.
5. Click **Add Filter**. The filter is added to the filter bar and the Stories Workbench is updated to show stories based on the filters.

### Clearing the Filter

You can remove each item in the filter separately, or clear the entire filter.

**To clear the filters for the Stories Workbench page:**

1. To clear a single filter, click ![remove.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356150766749.png) next to the filter.
2. To clear all the filters, click X at the right end of the filter bar.

## Drilling-Down and Analyzing Stories

You can click on a story in the Stories Workbench to drill-down and investigate the details in a different page. This page contains a number of widgets that help you evaluate the potential issue identified by the Site Operations engine.

### Investigating Stories with Playbooks

The Stories Workbench drill-down includes a [link](/docs/reviewing-site-operations-stories#UUID-9d4fb928-b8fe-a7aa-8f32-cb6e29b7bc68_N1704352867243) to a playbook that provides steps to investigate, troubleshoot, and resolve the issue. Each Site Operations story links to a playbook for the story's specific indication. For example, a playbook for stories with the indication **Socket HA Not Ready status**.

### Generating AI Story Summaries

The Stories Workbench drill-down includes a tool that lets you create a natural language story description generated by AI, which provides rich context and helps you quickly assess the story. The story summary is generated dynamically to reflect the current state of the story. If the story updates with new information, you can regenerate the summary to reflect the changes.

For more about generating AI story summaries, see [below](/docs/reviewing-site-operations-stories#UUID-9d4fb928-b8fe-a7aa-8f32-cb6e29b7bc68_N1707652620384).

- The AI story summary is generated only on-demand by the admin

#### Protecting Sensitive Data with Tokenization

For robust data security during the transmission of story data to third-party AI services, Cato uses tokenization to ensure all sensitive data remains in the Cato XOps platform. This involves replacing sensitive information with unique identifiers, or "tokens," rendering the data meaningless to unauthorized entities. Sensitive data is never exposed to third-party services. This approach ensures the confidentiality of the story's details, aligning with our commitment to robust data privacy and security standards.

> [!NOTE]
> Note:
> 
> Due to the limitations of generative AI, the information provided in story summaries may occasionally contain inaccuracies.

### Understanding the Story Drill-Down Widgets

![Detection___Response_Network_callouts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356143166365.png)

These are the story drill-down widgets:

| Item | Name | Description |
| --- | --- | --- |
| 1 | Story summary | A summary of basic information about the story, including: - The story type - The name of the site associated with the story - The story's criticality - The number of times the issue occurred - The number of days since the story was generated - The story's current status |
| 2 | Story timeline | Shows a timeline of changes in the story status |
| 3 | **Story Details** | Basic information for analyzing the story, including a story description, when the story was created and updated with new related network incidents, and information about the site. - Click **Generate AI Summary** for a natural language story description that provides rich context and helps you quickly assess the story - Click the **Playbook KB article** link to open the playbook explaining how to troubleshoot and resolve this type of story |
| 4 | **Current Site Overview** | Information about the site in your network impacted by the story. The widget includes a link to view recent connection logs for the site, and drop-down menus with shortcuts to [Site Configuration](/v1/docs/site-configuration) and [Site Monitoring](/v1/docs/site-monitoring-1) pages. This widget is the same as the [Site Information Panel](/v1/docs/using-the-topology-page) on the Topology page. |
| 5 | **Incident Timeline** | A list of the detected incidents for issues and resolutions in the story. For example, the Incident Timeline for a **Link is down** story includes these incidents: - WAN1 Active link of Primary socket - Disconnected from the Cato Cloud - WAN1 Active link of Primary socket - Successfully re-established connectivity to the Cato Cloud - No more occurrences of the issue after 120 minutes, story status changed from Monitoring to Closed > [!NOTE] > Note: > > Only Site Operations stories close automatically, and only after 120 minutes that the issue no longer occurs. XOps Security stories do not close automatically. These are the columns for the Incident Timeline: - **Created** - When the incident was first detected - **Validated** - When the created incident was confirmed - A **Description** of the incident - **Event** - A link to show the [Events](/v1/docs/analyzing-events-in-your-network) page pre-filtered for the incident |

## Using the Response Policy for Site Operations Stories

![Detection___Response_Network_Response_Policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33356137456029.png)

The XOps Response Policy helps you monitor XOps stories by defining when email notifications for stories are sent to admins. You can create rules that define the story criteria for when notifications are sent, and can use mailing lists to configure which admins receive the notifications. For example, you can create a rule to send notifications for a Site Operations story with high Criticality, and define the mailing list to include a helpdesk email address to automatically open a support ticket.

For more about creating Response Policy rules, see [Creating the Response Policy for XOps Stories](/v1/docs/creating-the-response-policy-for-xops-stories)
