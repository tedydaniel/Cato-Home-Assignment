---
title: "Analyzing Events in Your Network"
slug: "analyzing-events-in-your-network"
updated: 2026-06-22T09:24:17Z
published: 2026-06-22T09:24:17Z
canonical: "knowledge.catonetworks.com/analyzing-events-in-your-network"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Analyzing Events in Your Network

## Overview

Cato Events provide detailed data about traffic and activity across your account. Each event records information about something that occurred in the environment, such as a connection attempt, a security action, or a configuration-related activity, including the context needed to understand what happened and how Cato handled it.

Use the Events page in the Cato Management Application (CMA) to investigate traffic, monitor account activity, validate policy behavior, and troubleshoot operational issues. You can narrow event data by time range, event type, field values, presets, custom filters, or natural language search to focus on the events that are relevant to a specific network or security question.

For additional analysis, centralized monitoring, or retention, you can:

- Send events to external platforms with Event Integrations, see [Getting Started with Event Integrations](/v1/docs/getting-started-with-event-integrations)
- Export event data from the Events page, see below [Exporting Events to a File](/v1/docs/analyzing-events-in-your-network#h_01K7K8YT3VQ0VW9DJ93Y6WV52K)

Event data is stored in Cato's Data Lake. For more information, see [Guide to Cato Data Lake](/v1/docs/guide-to-cato-data-lake).

> [!NOTE]
> **Notes:**
> 
> - After an event is generated, typically within a 5 minute time frame the data for that event is shown in the **Events** page. However, it is possible that some events will be delayed up to 30 minutes.
> - Changes to entity names (such as policy rules) can take up to 24 hours to be reflected in the relevant event fields.

## Viewing Event Fields using Quick View

Quick View is an option that displays fewer fields for each Event in order to improve page performance. It is enabled by default, and displays the fields that are most commonly required for analysis. It significantly improves the performance of the Events page as well as the export performance when you select the Quick View export option.

Any fields that are manually selected or mentioned in a filter are also displayed when Quick View is enabled.

You can disable Quick View at any time to load all fields, however this may impact performance.

### Fields Included in Quick View

The following fields are displayed for each event when Quick View is enabled. The list of fields is based on customer usage data.

- Always-On
- App Activity Category
- Application
- Application Activity
- Application Risk
- Authentication Method
- BGP Disconnect Error Code
- Bypass Method
- Bypass Reason
- Category
- Cato App
- Client Certificate Name
- Client Class
- Client Version
- Configured Host Name
- Connector Type
- Custom Category
- Destination Country
- Destination IP
- Destination is Site or SDP User
- Destination Port
- Destination Site
- Device Certificate
- Device Name
- Device OS Type
- Device Posture Profiles
- Directory IP
- Directory Sync Result
- DLP Profiles
- DNS Protection Category
- DNS Query
- Domain Name
- Egress PoP Name
- Event Type
- event_message
- Failure Reason
- File Hash
- File Type
- Full Path URL
- HA Role
- Host IP
- Host MAC Address
- Interface ID
- IP Protocol
- Is Sanction App
- ISP Name
- LAN Acess
- Link Health - Packet Loss
- Link Type
- Logged In User
- Login Type
- Network Rule
- OS Type
- PoP Name
- Public Source IP
- QoS Priority
- Reference URL
- Related Apps
- Risk Level
- Rule
- Rule ID
- SAM Account Name
- Severity
- Signature ID
- Socket Reset
- Source Country
- Source IP
- Source is Site or SDP User
- Source ISP IP
- Source Port
- Source Site
- Split Tunnel
- Status
- Subnet Name
- Sub-Type
- TCP Acceleration
- Threat Name
- Threat Type
- Thread Verdict
- Time
- TLS Certificate Error
- TLS Error Description
- TLS Error Type
- TLS Rule Name
- Traffic Direction
- Trusted Networks
- Tunnel Protocol
- URL
- User Agent
- User Display Nae
- User Email
- User Name
- User Principal Name
- Windows Domain Name

## Viewing the Events Page

You can view events for your whole account in the **Home > Events** page.

### Elements on the Events Page

The following image and table explain the elements of the **Events** page with the **Events** tab:

![events_elements_on_page.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29398003167901.jpg)

| Item | Name | Description |
| --- | --- | --- |
| 1 | Select Presets menu | Drop-down menu with preset filter options to show the events for common scenarios as well as any custom presets you manually saved. |
| 2 | Events filter bar | Shows the filters that are applied to the events. Click ![Add2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29397986183709(1).png) (Add) to manually configure the settings for a filter. |
| 3 | Refresh | Refreshes data for events on the page (takes about 5 seconds to refresh) |
| 4 | Time range | Select the time range for the events that are shown in the page. The default time range is Last 2 Days, which shows events for the previous 48 hours. For more information, see [Setting the Time Range Filter](/v1/docs/setting-the-time-range-filter). **Note:** The maximum date range for the **Events** page is 31 days. |
| 5 | Export events menu | Exports events in the current filter to a file. You can export all the fields (columns), or only the ones that you selected. |
| 6 | Add to custom presets | Add the current filter to your custom presents so you can easily use the filter again. |
| 7 | Natural Language Search | Filter the events list using natural language filters. |
| 8 | Manual Filter Toggle | After you have used a natural language search, this button toggles back to the manual filter options. |
| 9 | Events timeline | Shows the number of filtered events. Each event type is represented by a different color. |
| 10 | Total number of events | Shows the total number of events for the current time range and filter settings. |
| 11 | Event type quick filters | Click an event type to hide the events for that type. For example, when you click **Network**, the Network events aren't shown in the page. |
| 12 | Event data view tabs | Select the tab to choose the view for the event data. - **Events:** Shows all the event data in a condensed row. When you expand the row each item of data is on a separate line. - **Smart View:** Shows the event data in an easy-to-read format that provides quick insights. When you expand a row the data is shown in the same way as the Events tab. - **Top Distributions:** Shows the percentage of events according to these charts: - **Event Type Distribution** - Shows the total number of events and the percentage for each of the event types - **Top Connectivity Events** - Shows the top action for connectivity events - **Top Security Events** - Shows the top action for security events - **Top Source Sites and SDP Users** - Shows the top traffic sources from sites and SDP usernames - **Top Source IPs** - Shows the top traffic sources based on IP address - **Top Target Host Names** - Shows the top traffic target (destination) based on host name - **Commonly Inspected Files OR Top Inspected** - Shows the top file names inspected by the Threat Protection engines |
| 13 | Event fields | All fields that are in the raw data for the filtered events. You can easily add or exclude a field in the filter. Shows the cardinality (distinct values) of events that match each field category. When you expand the category, it shows the total number of events for each event type. |
| 14 | Time and Raw Data for an event | Shows the time stamp when the event was generated and the raw data for each field in the event. You can also add the fields as new columns to this table. |
| 15 | QuickView | QuickView is enabled by default, displaying all the fields that are typically required for analysis for each Event. This significantly improves the page performance. This also improves the export performance when you select the QuickView export option. |

### Understanding the Event Types

These are the types of events on the **Events** page:

- **Connectivity** - Events related to connectivity for LAN monitoring, sites, and VPN Clients in the account
  - Connectivity events are related to issues with the site connection, for example link quality related to packet loss
- **Detection and Response -** Events related to XOps stories
  - Detection and Response events are related to new and updated XOps stories generated by the Response Policy
- **Posture -** Events related to Posture checks
  - Posture events are related to posture score changes and new checks
- **Routing** - Routing, and BGP events
  - Routing events are related to the status of BGP sessions and routes
- **Security** - Events generated by Threat Protection and Firewall engines
  - Security events are related to potential security issues, and can help you to fine-tune rules for the firewall
- **Sockets Management** - Events related to Sockets, such as firmware updates
  - Socket management events are related to a Socket successfully updating to the newest version
- **System** - Events related to LDAP, User Awareness, license, and user accounts
  - System events are related to the status of a Directory Services sync

## Filtering and Sorting Events

You can filter events to help you quickly find relevant information.

### Filtering Events Using Natural Language Search

You can easily search for events using everyday language to drill-down and identify relevant data on the page. For more details, see [Using Natural Language Search](https://support.catonetworks.com/hc/en-us/articles/#UUID-7117ded8-4ea4-c3ff-4e2a-8b3d31f6e909).

### Filtering Events Using Present or Custom Filters

You can use Cato's preset filters or create a custom filters to help you find the relevant events. For details, see [Filtering Data on a Page](/v1/docs/filtering-data-on-a-page)

### Adding Event Values to the Events Filter

The left-hand section of the **Events** page shows the fields and values that are included in the events (item 5 in the previous example). You can easily add a field value to the events filter to drill-down and identify the relevant events.

The following table explains the buttons in the events fields:

| Item | Description |
| --- | --- |
| ![Add_button.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29397968122013(1).png) | Adds the field to the **Selected Fields** section, and the page only shows event data for these fields. Click X at the top of the column to remove it. |
| ![Include_button.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29397973235229(1).png) | Adds the specific value for the field to the filter. The **Events** page automatically updates and shows events that match the new filter. |
| ![Exclude_button.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29398003625373(1).png) | Adds an exclusion for this specific value of this field to the filter. The **Events** page automatically updates and shows events that do NOT match this value. |

In addition, you can add a new column that shows event data for the specific field. The following table explains the buttons in the events fields:

**To add an event value to the filter:**

1. In the **Events** page, click the field to expand the values.

![EventValue.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29397973434909(1).png)
2. For the specific value, click the button to add the value or the exclusion to the filter.

The **Events** page refreshes and shows the events that match the new filter. The field value shows the number of matching events.

## Exporting Events to a File

You can export the event data in the Events page to a file for additional analysis. You can export up to 250,000 events at one time to a file. All Events in the current filter and time range are included in the export. You can use the following three options to control which event fields are included in the export:

- **All fields:** Include all fields for every event in the export.
- **Selected Fields:** Only include fields that you added in the export.
- **QuickView:** When QuickView is enabled, this only includes QuickView fields as well as any fields that were added manually or mentioned explicitly in the filter. This option is designed to improve export performance.

> [!NOTE]
> **Notes:**
> 
> - Only CMA admins with an **Editor** role have permission to export to a CSV file. For more about configuring admin roles, see [Managing Admins](/v1/docs/managing-admins).
> - Sometimes, trying to export events will fail because the query takes too long and the request times out. You can reduce the time frame of the event filter or use the QuickView export option and then try again.
> - The number of events in the Events page can be rounded up. For example, the Events page shows 2K events, and the actual number of events is 1952.
> - After exporting the events, the events_count column in the CSV file can show multiple events for each row, this happens when the same event occurred more than once over the time span of one minute. The COUNT of this column can show a different number than the total exported events. To show the total number of exported events, use the SUM of the events_count column.

**To export events to a CSV file:**

1. **(Optional)** Click **Add** for the fields that you are exporting.
2. From the **Events** page, click **Export Events**.
3. Select the scope of the export: **All fields** in the events, the **Selected fields** in the filter, or the fields included in **QuickView**.
  - **All fields** in the events
  - **Selected fields** in the filter
  - Fields included in **QuickView**
4. Click **OK**. The events are exported to the CSV file and the file is downloaded according to the settings of your Internet browser.
