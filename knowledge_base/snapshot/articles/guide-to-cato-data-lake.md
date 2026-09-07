---
title: "Guide to Cato Data Lake"
slug: "guide-to-cato-data-lake"
updated: 2026-08-24T09:02:42Z
published: 2026-08-24T09:02:42Z
canonical: "knowledge.catonetworks.com/guide-to-cato-data-lake"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Guide to Cato Data Lake

This article discusses the details of the event generation rate and data retention for the Cato Data Lake and your account.

## Overview

The Cato Data Lake contains the data recorded by the different services in the Cato platform, such as Networking, Security, Access, and so on. Data such as event information is added to the Data Lake in real-time and retained for a specific time period, as defined by the customer’s contract. Cato uses Data Lake units to define customer data retention according to:

- Hourly event rate (currently in units of 2.5 million events per hour)
- Retention time (ie. 3 months, 6 months, etc..)

Data that exceeds the terms of the Data Lake unit may be discarded. For example, if there are more than 2.5 million events within an hour or data that is more than 3 months old.

As part of the Cato platform, accounts receive a single Data Lake unit that includes an event rate limit of 2.5 million events per hour and a 3-month retention period. Customers may choose to purchase additional Data Lake units for increased hourly event rate and/or increased event retention time.

Customers may also use different integrations to forward their data to external cloud storage and SIEMs at no additional cost.

This information in this article applies to Cato accounts starting from January 1st, 2024(*).

## Event Retention Approach

Events are retained in real-time and can be tracked in the Cato Management Application (CMA) in the [Events page](/v1/docs/analyzing-events-in-your-network) (**Home > Events**).

- Cato retains a core set of key security and connectivity events for each customer
- Customers can select, within policies, additional events to be generated and retained
- Customer licenses define the hourly rate limit for the maximum number of events that are generated and retained
  - Events in excess of this number are discarded for the remainder of the hour

For more information about optimizing generated events, see [Best Practices for Cato Event Log Storage and Ingestion](/v1/docs/best-practices-for-cato-event-logs-and-ingestion)

### Event Rate Limiting

The details for the default Cato rate limiting for events are based on the Data Lake units owned by an account:

- Cato allows up to one Data Lake unit, free of charge (currently 2.5 million events per hour)
- If more events are generated than the licensed Data Lake units, the excess events may be discarded for the remainder of the hour
- To prevent the possibility of discarding events, customers have the option to purchase additional Data Lake units

We recommend that you purchase additional Data Lake units to meet the data requirements of your organization, for more information, see below [Estimating Event Requirements without an Event History](/v1/docs/guide-to-cato-data-lake#estimating-event-requirements-without-an-event-history).

### Event Retention

For contracts and renewals starting from January 1st, 2024, the default retention period for events is 3 months.

- After the retention period (ie., after 3 months), event data is deleted from the Cato Cloud and is no longer accessible (you can’t recover deleted data)
- Customers may purchase additional data retention if they wish to retain event data for more than three months

If a customer chooses to pay for additional data retention, no allowance is made for the free retention that is provided by default: all event retention is chargeable.

- For more about purchasing additional data retention, please contact your Cato representative.

Cato supports the following event storage options:

- Directly in the Cato Management Application (see [Analyzing Events in Your Network](/v1/docs/analyzing-events-in-your-network))
- A high-scale feed to Cloud Storage, such as [AWS S3](/v1/docs/integrating-cato-events-with-aws-s3) and Azure Blob Storage
- Using the [Cato API](https://api.catonetworks.com/documentation/#definition-EventFieldName)

## Data Lake Units

By default, each account has the following Data Lake units:

- Hourly event rate (currently in units of 2.5 million events per hour)
- Retention time (ie. 3 months, 6 months, etc...)

You can choose to purchase additional Data Lake units to increase the hourly event rate and/or the retention time.

### Increasing the Event Rate Limit

Data Lake units define the **peak** number of events that can be generated per hour. A period when fewer events are generated per hour will have no bearing on the number that can be generated in future hours.

Each Data Lake unit is purchased to increase the rate-limiting by 2.5 million events per hour. So, for example:

- Two Data Lake units allow an additional 2.5 million events per hour (up to 5 million events per hour total)
- Three units will allow an additional 5 million events per hour (up to 7.5 million events per hour total)

### Increasing the Event Retention Period

Data Lake units are available in three variants, according to the retention period required:

- A three-month unit
- A six-month unit
- A twelve-month unit

The chosen variant applies to all data units, it is not possible to mix units.

### Examples

The table below illustrates the use of Data Lake units to cover customer event storage requirements.

| Peak number of events generated per hour | Retention period required | Additional Data Lake units required | Type of Data Lake unit required |
| --- | --- | --- | --- |
| Up to 2.5 million | 3 months | 0 | N/A |
| Up to 2.5 million | 6 months | 1 | 6-month unit |
| Up to 5 million | 3 months | 1 | 3-month unit |
| Up to 7.5 million | 12 months | 2 | 12-month unit |

## Estimating Data Lake Unit Requirements Based on Event History

Customers with a stable history of event generation can inspect the event chart in the CMA to see how many events are being generated. They can use the peaks in this chart to consider their requirements for event rate limiting.

In the example chart below, the peaks reach a maximum of just over 400,000 events per hour. This would be covered by the free single Data Lake unit.

![Data_SKUs_Event_History_1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24394118553757.png)

In the example chart below, the number of events per hour exceeds 2.5 million in every hour, and the highest peak approaches 3 million. This is more than can be covered by the default event rate limiting for 1 Data Lake unit. 1 additional unit would cover these storage requirements, allowing up to 5 million events per hour to be generated.

![Data_SKUs_Event_History_2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24394118690845.png)

Note that the exact height of each bar can be inspected by hovering the cursor over the bar, as illustrated in the chart below.

![Data_SKUs_Event_History_2_hover.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24394118784413.png)

Further points to note:

- These examples cover a small period, for convenience. A longer analysis period would be prudent.
- The time period represented by each bar will change according to the time period covered by the chart. Pay attention to the Time Series Granularity as you change the time period covered.

## Estimating Event Requirements without an Event History

This section helps you create an initial rough estimate of the peak events per hour to understand how many Data Lake units are required. We recommend that you continuously monitor the actual event rates and adjust as required. The actual events generated per hour depends on several variables, such as traffic patterns and policy logging configuration. For more information, see [Best Practices for Cato Event Log Storage and Ingestion](/v1/docs/best-practices-for-cato-event-logs-and-ingestion).

Event generation is correlated to both the total bandwidth in use across the network and the number of SDP users supported. Customers without a history of event generation can estimate their likely event rate limiting requirements by adding the sum of total account site bandwidth and the number of SDP users. In addition, services enabled for the account can also impact the event requirements. For example, if the LAN Firewall is enabled, this will increase the event requirements proportionate to the amount of LAN traffic and which traffic generates events.

Tables are provided below to assist with estimating the **peak** events generated per hour. Follow this procedure to calculate requirements from the tables:

1. Find the row in the **Total Bandwidth** table that corresponds to the peak bandwidth for the network. Read off the estimated **peak events per hour** that will be generated
2. Find the row in the **SDP Clients** table that corresponds to the number of SDP Clients in use. Read off the estimated **peak events per hour** that will be generated
3. Add the sums from steps 1 and 2.
4. Divide the total events per hour by 2.5 million, and round up, to estimate the number of Data Lake units required for site bandwidth and SDP Clients.
5. If you are using multiple Cato services that generate a large number of events, such as CASB or LAN Firewall, add 1 Data Lake unit. (1 unit for bandwidth, 1 unit for SDP users, and 1 unit for CASB and RBI)

### Event Generation Tables

Use these tables to estimate the **peak** number of events per hour generated for a customer. They assume that the customer is logging all events.

| Total Bandwidth | Estimated peak events per hour | SDP Clients | Estimated peak events per hour |
| --- | --- | --- | --- |
| Up to 2.5Gbps | 1,000,000 | Up to 3K | 1,000,000 |
| 2.5-6Gbps | 5,000,000 | 3K-7K | 5,000,000 |
| 6-9Gbps | 7,500,000 | 7K-11K | 7,500,000 |
| 9-12Gbps | 10,000,000 | 11K-15K | 10,000,000 |
| 12-15Gbps | 12,500,000 | 15K-19K | 12,500,000 |
| 15-18Gbps | 15,000,000 | 19K-23K | 15,000,000 |
| 18-21Gbps | 17,500,000 | 23K-27K | 17,500,000 |
| 21-24Gbps | 20,000,000 | 27K-31K | 20,000,000 |
| 24-27Gbps | 22,500,000 | 31K-35K | 22,500,000 |
| 27-30Gbps | 25,000,000 | 35K-39K | 25,000,000 |
| 30-33Gbps | 27,500,000 | 39K-43K | 27,500,000 |

#### Example Estimation

In the table above:

- A total of **3 Gbps** bandwidth across all sites would generate an estimated **peak** of **five million** events per hour
- A total of **5,000** SDP clients would generate an **additional** estimated **peak** of **two and a half million** events per hour
- Therefore, the customer could expect a peak of 5+2.5= **7.5 million** events per hour (2 units)
- The customer uses the CASB and RBI service (1 unit)
- This could be covered by buying **three** more Data Lake Storage units of the appropriate duration.

## Estimating Actual Retention Required

The unit of measure for Data Lake units is the number of events generated per hour. The volume of **data** involved is **not** used in the calculation or purchase of additonal units and it is not reported by the CMA.

However, customers may wish to estimate the implications if they plan to export data to external storage or a SIEM. Customers can make a rough estimate for the volume of data involved, by assuming that one Data Lake unit (2.5 million events per hour) is very roughly equivalent to 180 GB per month of data storage, as illustrated in the table below.

Note that this is a very rough estimate. Data Lake units define the **maximum** number of events that can be generated in an hour. It is self-evident that a customer who buys units to cope with occasional large peaks in event generation will have a very different external storage requirement than a customer who buys the same number of units to cope with a consistently high number of events generated.

The following table shows a very rough estimate of the total GB according to the retention period:

| Events per hour | Additional Data Lake units | GB per month (estimated) | 3 months | 6 months | 12 months |
| --- | --- | --- | --- | --- | --- |
| 2.5 million | 0 | 180 | 540 | 1080 | 2160 |
| 5 million | 1 | 360 | 1080 | 2160 | 4320 |
| 7.5 million | 2 | 540 | 2160 | 4320 | 8640 |

(*) Some contracts with Cato may include terms that differ from the information in this article
