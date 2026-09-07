---
title: "Reviewing Detection & Response Stories for MDR Customers"
slug: "reviewing-detection-response-stories-for-mdr-customers"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/reviewing-detection-response-stories-for-mdr-customers"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reviewing Detection & Response Stories for MDR Customers

## Overview of Detection & Response Stories

Cato Detection & Response is a new layer of security that creates stories for threats. When Cato’s advanced correlation engines analyze traffic data and find a match for a potential threat, they generate a story. The story contains data from traffic flows with common properties that relate to the same threat. The Stories Workbench shows the details of each story to help you understand and analyze the threats. You can sort and filter the stories to find the most important potential attacks, and then drill-down on a story to further investigate the details.

These are examples of data that a story can include:

- Sources in your network
- External targets of network traffic
- Identification and description of the threat
- Relevant geolocations
- Related applications
- Relevant traffic flows
- Popularity of the target according to Cato internal data
- Malicious score of the target according to Cato threat intelligence algorithms

### Prerequisites

- This version of the Detection & Response feature is available for Cato MDR customers only. For more about subscribing to the MDR service, please contact your Cato representative.

## Showing the Stories Workbench

The Stories Workbench shows a summary of the stories for the potential threats in your account.

**To show the Stories Workbench:**

- From the navigation menu, click **Home> Stories Workbench**.

### Understanding the Stories Columns

![XDR_Incidents.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24427107272093.png)

| Column | Description |
| --- | --- |
| ID | Unique Cato ID for this story |
| Created | Date of the first traffic flow for the story |
| Updated | Date of the most recent traffic flow for the story |
| Risk Score | Cato's risk analysis of the story (values are from 1 - 10) |
| IOA | Indicator of Attack for the story |
| Source | IP address or name of device on your network impacted by the story |
| Type | - Threat Hunting - A story where Cato's algorithms and machine learning detected a potential security incident - Usage Anomaly - A story where an application showed unusual behavior that indicates a potential security incident - Events Anomaly - A story where there is an unusual number of security events triggered by an entity on your network |
| Status | - Pending Customer - Story was sent to customer and is waiting for a response from them - Pending Analyst - Waiting for more information from Cato security analysts - Closed - Cato security analysts closed the incident |

## Grouping the Stories

To provide context when reviewing the stories, you can show the stories in groups defined by details including **Source**, **Indication**, **Status**, and **Type**. For example, you can show together all of the stories related to a specific source IP address or all of the Cybersquatting stories. This gives you a broader perspective when analyzing the stories, and can help you reach faster and more accurate conclusions.

Each group highlights the criticality levels for the stories in that group, including the number of high, medium, and low criticality stories.

![Stories_Workbench_Grouping.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24427135422621.png)

**To group the stories in the Stories Workbench:**

1. From the navigation menu, click **Home > Stories Workbench**.
2. From the **Group By** drop-down menu, select the required criterion.

The stories are shown in expandable groups.

## Filtering the Stories

There are two ways to filter the data in the Stories Workbench: automatically update the filter with the selected item, or manually configure the filter.

### Automatically Filtering for an Item

As you hover over an item or field where a filter option is available, the ![TD_Filter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24427149334941.png) button appears. Click the icon to show the filter options:

- **Add to Filter** - Adds the item to the filter, and the Stories Workbench now only shows stories that includes this item. For example, if you filter for a specific Risk Score, the screen only shows stories with that Risk Score.
- **Exclude from Filter** - Updates the filter to exclude this item, and the Stories Workbench now only shows stories that do NOT include this item.

You can continue to add items to the filter, click ![TD_Filter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24427149334941.png) again to update the filter and drill-down further.

### Selecting the Time Range

The default time range for the Stories Workbench is the previous two days. You can select a different time range to show the stories a longer or shorter time period. For more information, see [Setting the Time Range Filter](/v1/docs/setting-the-time-range-filter).

The maximum date range for the Stories Workbench is 90 days.

### Manually Configuring the Filter

You can manually configure the story filter for greater granularity to analyze the stories. After you configure the filter, it is added to the stories filter bar and the screen is automatically updated to show the stories that match the new filter.

**To create a filter:**

1. In the filter bar, click ![Add2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24427095071645.png).
2. Start typing or select the **Field**.
3. Select the **Operator**, which determines the relationship between the **Field** and the **Value** you are searching for.
4. Select the **Value**.
5. Click **Add Filter**. The filter is added to the filter bar and the **Stories Workbench** is updated to show stories based on the filters.

### Clearing the Filter

You can remove each item in the filter separately, or clear the entire filter.

**To clear the filters for the Stories Workbench:**

1. To clear a single filter, click ![remove.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24427106302237.png) next to the filter (item 1 above).
2. To clear all the filters, click X at the right end of the filter bar (item 2 above).

## Drilling-Down and Analyzing Stories

You can click on a story in the Stories Workbench to drill-down and investigate the details in a different screen. This screen contains a number of widgets that help you evaluate the potential threat. There are specialized widgets to analyze data for Threat Hunting or Usage Anomaly stories.

### Understanding the Threat Hunting Widgets

![XDR_Drill_ThreatHunting.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24427149687453.png)

These are the widgets for a Threat Hunting story:

| Item | Name | Description |
| --- | --- | --- |
| 1 | Story summary | A summary of basic information about the story, including: - Threat category - Severity of the threat as determined by analysts - Number of signals (traffic flows) associated with the attack - Number of compromised devices - Story status |
| 2 | Story timeline | Shows a timeline of the story, such as changes made to the story verdict and severity, and when new targets related to the story are identified |
| 3 | **Details** | Key information for analyzing the story, including a threat description, Cato threat signatures detected in the relevant traffic, and MITRE ATT&CK® techniques identified for the threat. For more about the MITRE ATT&CK® framework, see [Working with the MITRE ATT&CK® Dashboard](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings). - Hover the mouse over a signature to show a summary event log - Click the signature to open the Events screen pre-filtered for the signature - Click a MITRE ATT&CK® technique to read its description on the MITRE ATT&CK® website |
| 4 | **Source** | Basic information about the devices in your network impacted by the threat |
| 5 | **Attack Geolocation** | Shows the geolocation for sources in your network (orange locations) and external sources (red locations) related to the threat. Arrows connecting the sources indicate the direction of traffic |
| 6 | **Attack Distribution** | Time distribution of attack related flows. - To make it easier to read the graph, in **Targets**, click a target to hide that data from the graph - To show the attack details, hover the mouse over the graph |
| 7 | **Targets** | Shows data for the potentially malicious sources outside your network site related to the story. \| Column \| Description \| \| --- \| --- \| \| **Creation Date** \| Registration date of the target domain \| \| **Target** \| Domains or IP addresses of external sources identified in traffic flows related to the story \| \| **Target Links** \| Links to look up the target in various threat intelligence sources. For additional information, click the VirusTotal icon, or select other resources from the drop-down menu. \| \| **Malicious Score** \| The malicious score of the target according to Cato threat intelligence algorithms. Scores range from 0 (benign) to 1 (malicious) \| \| **Popularity** \| How often the target appears in Cato internal data sources. Values are: **Unpopular, Low, Medium, High** \| \| **Categories** \| Cato categories for the target domain \| \| **Threat Feeds** \| Number of Cato threat intelligence sources that detected the target as malicious \| \| **Engines** \| Number of third party security engines that detected the target as malicious \| \| **Country** \| Country where the target domain is registered \| \| **Google Search Hits** \| Number of Google search results for the target \| |
| Column | Description |
| **Creation Date** | Registration date of the target domain |
| **Target** | Domains or IP addresses of external sources identified in traffic flows related to the story |
| **Target Links** | Links to look up the target in various threat intelligence sources. For additional information, click the VirusTotal icon, or select other resources from the drop-down menu. |
| **Malicious Score** | The malicious score of the target according to Cato threat intelligence algorithms. Scores range from 0 (benign) to 1 (malicious) |
| **Popularity** | How often the target appears in Cato internal data sources. Values are: **Unpopular, Low, Medium, High** |
| **Categories** | Cato categories for the target domain |
| **Threat Feeds** | Number of Cato threat intelligence sources that detected the target as malicious |
| **Engines** | Number of third party security engines that detected the target as malicious |
| **Country** | Country where the target domain is registered |
| **Google Search Hits** | Number of Google search results for the target |
| 8 | **Attack Related Flows** | Shows data for a representative sample of traffic flows related to the attack. \| Column \| Description \| \| --- \| --- \| \| **Target** \| Target domain or IP of the flow \| \| **Start Time** \| Timestamp for the beginning of the flow \| \| **Direction** \| Direction of the flow. Directions include: - **Inbound** - Traffic to your network originating at an external source - **Outbound** - Traffic from your network to an external source - **WANbound** - Traffic from your network to another site on your network \| \| **Source IP** \| Source IP address in your network sending or receiving the flow \| \| **Source Port** \| Source port in your network sending or receiving the flow \| \| **Destination IP** \| IP address of the external target sending or receiving the flow \| \| **Destination Port** \| The port of the external target sending or receiving the flow \| \| **Method** \| The HTTP method in the flow (GET, POST, and so on) \| \| **Full Path URL** \| The complete URL of the external resource in the flow \| \| **HTTP Response Code** \| The status code issued by the target in response to the browser-side request from the client \| \| **Client** \| The client type in the flow \| \| **Cato App** \| Cato's application used in the flow \| \| **Referrer** \| The address for the original website, that contains the link for the requested resource \| \| **User Agent** \| The agent (for example, browser version) identified in the User Agent field in the HTTP request header in the flow \| \| **Destination Country** \| Location of the **Destination IP** in the flow \| |
| Column | Description |
| **Target** | Target domain or IP of the flow |
| **Start Time** | Timestamp for the beginning of the flow |
| **Direction** | Direction of the flow. Directions include: - **Inbound** - Traffic to your network originating at an external source - **Outbound** - Traffic from your network to an external source - **WANbound** - Traffic from your network to another site on your network |
| **Source IP** | Source IP address in your network sending or receiving the flow |
| **Source Port** | Source port in your network sending or receiving the flow |
| **Destination IP** | IP address of the external target sending or receiving the flow |
| **Destination Port** | The port of the external target sending or receiving the flow |
| **Method** | The HTTP method in the flow (GET, POST, and so on) |
| **Full Path URL** | The complete URL of the external resource in the flow |
| **HTTP Response Code** | The status code issued by the target in response to the browser-side request from the client |
| **Client** | The client type in the flow |
| **Cato App** | Cato's application used in the flow |
| **Referrer** | The address for the original website, that contains the link for the requested resource |
| **User Agent** | The agent (for example, browser version) identified in the User Agent field in the HTTP request header in the flow |
| **Destination Country** | Location of the **Destination IP** in the flow |

### Understanding the Usage Anomaly Widgets

![XDR_Drill_Anomaly.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24427107767837.png)

These are the widgets for a Usage Anomaly story:

| Item | Name | Description |
| --- | --- | --- |
| 1 | Story summary | Provides a summary of basic information about the story, including: - Anomaly name - Severity - The period of training for the machine learning model to determine anomalous behavior - Story status |
| 2 | **Details** | Key information for analyzing the story, including a threat description and summary, and MITRE ATT&CK® techniques identified for the threat. For more about the MITRE ATT&CK® framework, see [Working with the MITRE ATT&CK® Dashboard](/v1/docs/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings). - Click a MITRE ATT&CK® technique to read its description on the MITRE ATT&CK® website |
| 3 | **Anomaly Distribution** | Graph of the anomalous behavior for the last 14 days - To show the anomaly details, hover the mouse over the graph - Click **View All** to open the Application Analytics screen pre-filtered for the apps related to the anomaly |
| 4 | **Top Hosts** | Top hosts related to the anomaly, with relevant details. For example, a host for an upstream bandwidth anomaly appears with the number of uploads from the host - Click **View All** to open the Application Analytics screen and show the hosts pre-filtered for the apps related to the anomaly |
| 5 | **Top Applications** | Top applications related to the anomaly, with relevant details. For example, an app for an upstream bandwidth anomaly appears with the number of uploads from the app - Click **View All** to open the Application Analytics screen pre-filtered for the apps related to the anomaly |
| 6 | **Top Servers/Destinations** | Top servers and destinations related to the anomaly, with relevant details. For example, a server for an upstream bandwidth anomaly appears with the number of uploads to the server - Click **View All** to open the Application Analytics screen and show the destinations pre-filtered for the apps related to the anomaly |

## Reviewing Ticketed Stories

The Cato MDR team opens tickets to notify you about significant stories. When you receive a ticket you can easily review the story in the Stories Workbench by clicking the link provided in the ticket. This is a sample ticket:

![XDR_Ticket.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24427123362205.png)
