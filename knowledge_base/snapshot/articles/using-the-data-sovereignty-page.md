---
title: "Using the Data Sovereignty Page"
slug: "using-the-data-sovereignty-page"
updated: 2026-06-22T09:24:33Z
published: 2026-06-22T09:24:33Z
canonical: "knowledge.catonetworks.com/using-the-data-sovereignty-page"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Data Sovereignty Page

## Overview

The Data Sovereignty page helps you review app traffic in your account that may be subject to data sovereignty requirements. You can use this page to identify regulated apps and regulated traffic, review AI-related app activity, and understand how traffic patterns relate to country regulations and PoP processing.

The page provides visibility into these types of context for the applications and traffic in your account:

- Regulatory context for the country associated with the application
- Application traffic origin based on source countries in your account
- Traffic processing based on PoP location

For more information about data sovereignty and Cato, see [SASE Sovereignty at Cato Networks](/v1/docs/sase-sovereignty-at-cato-networks).

## Reviewing Applications and Traffic Data

Use the summary at the top of the page to understand the distribution of applications, traffic, and the scope of regulated and AI-related activity in your account.

![data_sovereignty.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35681795405213(1).png)

The **Applications** section shows:

- **Total** - Total number of apps detected in the selected time range
- **Regulated apps** - Number of apps with headquarters in countries that have data protection regulations
- **AI Apps** - Number of detected AI-related apps

The **Traffic** section shows:

- **Total** - Total amount of traffic for the selected time range
- **Regulated traffic** - Amount of traffic for apps with headquarters in countries that have data protection regulations
- **AI traffic** - Amount of traffic for detected AI-related apps

For more information about filtering the page, see [Filtering Data on a Page](/v1/docs/filtering-data-on-a-page).

## Understanding Data Sovereignty Context

Use the map layers to understand the data sovereignty context for the traffic in your account.

### Drilling Down to a Layer

When you click a country location, the page filters the view for the selected country based on the active layer:

- In the App Headquarters layer, the page filters the data for apps headquartered in that country
- In the Traffic by source country layer, the page filters the data for traffic that originates from that country

![click_app_node.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/35681805492765(1).png)

After you click a country location, the details are updated for the active layer, including the number of apps and the traffic for that country.

### Comparing App Headquarters with Country Bandwidth Usage

The **App Headquarters** layer helps you compare the bandwidth usage of apps that have headquarters in that country with the data regulations associated with the country

This view gives you a high-level way to compare app-related country context with the applications that are used in your account.

Use this layer to quickly compare app headquarters locations with the countries shown in the **Bandwidth by country** panel and identify where additional review may be required.

### Reviewing Application Traffic by Source Country

The **Traffic by source country** layer shows the data protection regulations for application traffic based on the country where the traffic originates. This gives you visibility into the geographic source for applications used in your account.

### Reviewing PoP Locations for Traffic Processing

The **PoP locations** layer shows the PoPs that process site and user traffic in your account. This helps you understand where traffic is processed in motion across the Cato Cloud.

Data at rest remains based on your [CMA region](/v1/docs/welcome-to-the-cma).

## Disclaimer

The data transfer locations presented are based on the application HQ only and may not reflect actual transfer destinations. The regulatory information shown is a high-level summary and does not represent a complete overview of applicable privacy laws in each jurisdiction, and should not be relied upon as legal advice.
