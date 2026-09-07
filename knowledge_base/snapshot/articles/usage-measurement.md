---
title: "Usage Measurement"
slug: "usage-measurement"
updated: 2026-09-01T10:55:22Z
published: 2026-09-01T10:55:22Z
canonical: "knowledge.catonetworks.com/usage-measurement"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Usage Measurement

> [!NOTE]
> Note:
> 
> Cato account licenses use one of two models. This article only applies to the [Bursting Model](https://knowledge.catonetworks.com/docs/jan-2027-license-bursting-model) (starting in January 2027) and is not relevant for accounts using the Enforcement Model. Not sure which license model your account uses? See [Identifying your License Model](https://knowledge.catonetworks.com/docs/identifying-your-license-model).

Usage measurement defines how we calculate consumption for each license. Customers have visibility into usage metrics and reports through the Cato Management Application (CMA).

Usage is generally measured monthly and evaluated according to the applicable license scope and region group.

Licenses that are aligned to Base Products are not measured independently. Their usage measurement and fair use follow the applicable Base Product and its licensed capacity. For example, a Premium Security license aligned to Bandwidth Pool follows the measured Bandwidth Pool usage, while a license aligned to ZTNA Users follows the measured ZTNA User usage.

- Licenses that are licensed independently follow the measurement and fair-use rules defined for that specific license.

## Region Groups

Cato licenses are purchased, measured, and evaluated per region group. Region groups define how usage is aggregated and how licenses are applied geographically.

Region groups apply to Base Products, including Bandwidth Pool and ZTNA Users. Other services, such as Premium Security and Insights, are not scoped per region group and apply across the entire account.

The applicable region group is determined based on the license type:

- **Bandwidth Pool** - determined by the geographical location of the site. Licensed and measured per region group (Group 1, Group 2, and stand-alone country groups)
- **ZTNA Users** - determined by the user’s primary work location. Licensed in the general region (Group 1 and Group 2 combined) and separately for stand-alone country groups

Licenses are scoped to a specific region group. Capacity purchased for one region group cannot be used to cover usage in another group, and unused capacity cannot be transferred between region groups.

**Region Groups Definition**

The following region groups are defined:

- **Group 1** – North America, Europe, and select Asia and Oceania countries
- **Group 2** – APAC, Japan, Latin America, the Middle East, Africa, Australia, New Zealand

The following countries are defined as stand-alone region groups:

- **China**
- **Vietnam**
- **Morocco**

An up-to-date list of countries included in each region group is published on the [Cato Knowledge Base.](/v1/docs/country-s-allocation-to-license-groups-and-ztna-users)

### Restricted Countries

Licenses cannot be purchased for countries that are included on Cato’s restricted country list, as defined in the Cato Master Services Agreement ([https://www.catonetworks.com/msa/](https://www.catonetworks.com/msa/)).

## ZTNA User Measurement and Fair-Use

ZTNA Users are measured as the number of monthly distinct authenticated users who connect remotely to the Cato Cloud. A user is counted as a ZTNA User if they successfully authenticate and generate traffic during the calendar month.

Only remote user connectivity is considered, users who connect from behind a site are not counted.

ZTNA Users are purchased per region group but measured across the entire account.

For example, a customer purchases 100 users: 80 in the General region (Group 1 + Group 2) and 20 in China.

In each month, the customer uses 90 users in the General region and 10 users in China.

Although the usage per region differs from the purchased quantities, the total usage is still 100 users, which is within the licensed capacity.

If the number of users is higher than the licensed user capacity for the applicable license and region group, the excess is considered overuse and is handled as described in [License Over-Usage](/v1/docs/usage-measurement#license-overusage).

### ZTNA User Fair-Use

ZTNA User usage is considered within fair-use when the number of users remains within the licensed capacity.

If the number of users exceeds the licensed capacity, the excess is considered over-usage. The customer has the option to resolve the over-usage by increasing the licensed user capacity or paying a one-time charge for the excess, as described in [License Over-Usage](/v1/docs/usage-measurement#license-overusage).

Bandwidth usage for users connecting remotely to the Cato Cloud is not measured or licensed separately.

Cato reserves the right to apply bandwidth control mechanisms, including rate limiting or traffic shaping, when required to protect platform stability and service quality.

## Bandwidth Pool Measurement and Fair-Use

Bandwidth usage for the Bandwidth Pool license is measured using the 95th percentile (P95). P95 represents sustained bandwidth usage by excluding short-lived traffic spikes, providing a stable and predictable measurement of consumption.

The calculation is performed in the following steps:

1. **5-second sampling**

Traffic is sampled every 5 seconds for each site. For each 5-second sample, Cato sums upstream traffic across all last-mile interfaces and sums downstream traffic across all last-mile interfaces. The 5-second sample value is the higher of the two summed values (upstream vs. downstream).
2. **5-minute buckets**

The 5-second samples are grouped into 5-minute intervals (60 samples per interval). For each 5-minute interval, the highest 5-second sample is stored as the 5-minute bucket value.
3. **Daily site P95**

For each site, a daily P95 value is calculated by discarding the **top 5% of five-minute buckets**, equivalent to **70 minutes per day**. The highest remaining bucket determines the site’s daily P95 value. Daily calculations are performed from **00:00 to 00:00 UTC**.
4. **Daily aggregate (region group / pool)**

For each day, the daily site P95 values of all sites within the same region group are summed to produce a daily aggregate usage value for that region group.
5. **Monthly P95 (region group / pool)**

At the end of the calendar month, the highest daily aggregate usage value is taken as the monthly P95 result for the region group. The monthly calculation window runs from 00:00 UTC on the 1st day of the month to 00:00 UTC on the last day.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/p95.png)

If measured bandwidth usage exceeds the licensed bandwidth capacity for the applicable license and region group, the excess is considered over-usage and handled according to the [License Over-Usage](/v1/docs/usage-measurement#license-overusage) article.

### Site Types and Enforcement Behavior

Bandwidth behavior varies by site type and region, with a distinction between how usage is measured at the pool level and how bandwidth is enforced per site.

For Socket and IPsec site types in Group 1 and Group 2 regions, bandwidth is not enforced per site by default. Customers can utilize the full available capacity of their last-mile connectivity, and enforcement can be optionally configured per site if required. Bandwidth usage is aggregated across all sites and measured against the Bandwidth Pool using P95.

Cloud Interconnect sites follow a fixed enforcement model. Bandwidth is limited to the configured capacity per site and does not support exceeding the allocated bandwidth.

In stand-alone country regions (such as China, Vietnam, and Morocco), bandwidth is enforced based on configured capacity for all site types. Customers must define maximum bandwidth per site, and usage cannot exceed the configured per-site limits or the total licensed Bandwidth Pool capacity for the region.

### Bandwidth Fair-Use

Bandwidth usage is considered within fair use when the measured monthly P95 remains within the licensed Bandwidth Pool capacity for the applicable region group

.If the measured monthly P95 exceeds the licensed capacity, the excess is considered over-usage. The customer has the option to resolve the over-usage by increasing the licensed Bandwidth Pool capacity or paying a one-time charge for the excess, as detailed in the [License Over-Usage](/v1/docs/usage-measurement#license-overusage) article.

## AI Security for Users Measurement and Fair-Use

AI Security for Users is measured based on the number of users protected by the service during the calendar month. A user is counted if they are enabled for AI Security and generate activity through supported integration methods.

The licensed quantity represents the total number of users selected for protection and is not required to match the total number of users in the account.

### AI Security for Users Fair-Use

AI Security for Users usage is considered within fair use when the number of protected users remains within the licensed capacity.

If the number of users exceeds the licensed capacity, the excess is considered over-usage. The customer has the option to resolve the over-usage by increasing the licensed user capacity or paying a one-time charge for the excess, as detailed in the [License Over-Usage](/v1/docs/usage-measurement#license-overusage) article.

## Assets Security Measurement and Fair-Use

Device-based licenses are measured based on the number of unique devices identified during the calendar month. A device is counted if it sends or receives traffic through the Cato Cloud or is identified on the local LAN environment.

Device measurement includes devices identified through inline traffic inspection as well as devices discovered through supported out-of-band integrations that forward traffic through the Cato Cloud.

Cato Sockets are not included in the device count.

### Assets Security Fair-Use

Device usage is considered within fair use when the number of identified devices remains within the licensed device block capacity.

If the number of devices exceeds the licensed capacity, the customer must purchase the device block that matches the total number of identified devices. Cato will work with the customer to align the licensed capacity with actual usage.

## DEM Measurement and Fair-Use

DEM is measured based on the number of users monitored during the calendar month. A user is counted if their activity is included in DEM monitoring and analytics.

The licensed quantity typically aligns with the total number of users in the organization.

### DEM Fair-Use

DEM usage is considered within fair use when the number of monitored users remains within the licensed capacity.

If the number of users exceeds the licensed capacity, the excess is considered over-usage. The customer has the option to resolve the over-usage by increasing the licensed user capacity or paying a one-time charge for the excess, as detailed in the [License Over-Usage](/v1/docs/usage-measurement#license-overusage) article.

## Data Lake Measurement

Data Lake usage is measured based on the total event ingestion rate, expressed as events per hour.

Each Data Unit (DU) provides a fixed ingestion capacity. The total licensed capacity is determined by the number of purchased DUs.

All events generated across the Cato Cloud are counted toward the total ingestion rate and compared against the total licensed capacity.

### Data Lake Fair-Use

Data Lake usage is considered within fair use when the measured event ingestion rate remains within the total licensed capacity.

If the ingestion rate exceeds the licensed capacity, the excess is considered over-usage. Events are not dropped when capacity is exceeded.

The customer must purchase the DU capacity that matches the measured ingestion rate. Cato will work with the customer to align the licensed capacity with actual usage.

## License Over-Usage

Over-usage occurs when the measured usage for a license exceeds the licensed capacity for that license during a calendar month. Usage is measured monthly, and over-usage is evaluated independently for each license.

Unused capacity cannot be transferred between licenses or between region groups to offset over-usage.

When over-usage occurs, the customer must resolve the excess usage by increasing the licensed capacity or as described in the Over-Usage Resolution section of this guide.

When over-usage occurs for Base Products (Bandwidth Pool or ZTNA Users), associated Premium Security and Insights licenses must also be increased accordingly.

### Notification of Over-Usage

When over-usage is detected for a given calendar month, Cato sends a notification to the customer and the partner. Notifications are issued at the end of the calendar month and are sent only for months in which over-usage occurs.

Detailed usage reports and historical visibility for usage measurement and over-usage are available. Customers can configure the notification recipients through the CMA.

### Over-Usage Resolution Options

When over-usage is identified, customers have two options to address the excess usage, depending on whether the increased consumption is temporary or ongoing.

**True-Up (One-Time)**

A one-time charge covering the over-usage for the specific month or months in which it occurred. This option is typically used to address short-term or seasonal spikes in usage.

**True-Forward (Expansion)**

An increase in the licensed capacity to cover the over-usage for the remainder of the current contract term (co-term). The increased licensed quantity must be at least equal to the measured over-usage. Customers can only true-forward a quantity that is the same or greater than the over-usage amount.

When choosing True-Forward, the increased licensed capacity applies from the following billing period onward. The month in which the over-usage occurred is not retroactively billed under the True-Forward option.

The applicable pricing and commercial terms for True-Up and True-Forward are defined in the customer’s commercial agreement.
