---
title: "Using the Device Overview"
slug: "using-the-device-overview"
updated: 2026-08-30T12:42:16Z
published: 2026-08-30T12:42:16Z
canonical: "knowledge.catonetworks.com/using-the-device-overview"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Device Overview

This article explains how to use the Device Overview to analyze which devices connect to your network and the events they have created.

## Overview

The Device Overview provides visibility for all devices on the network and shows a wealth of data about IT, IoT, and OT devices. The dashboard summarizes device-related events and lets you view and analyze data about all the devices connected to your network. You can filter the dashboard to drill-down the data.

## Getting Started with the Device Overview

The Device Overview contains various widgets and metrics to help you understand device usage across your network. The page is split into four sections, these tables explain the widgets in each section.

### Displaying the Device Overview

You can display the Device Overview by navigating to **Home > Devices > Overview** tab.

### Device Summary Widgets

The Summary Bar displays a short summary of the devices connecting to your network.

![Summary_Bar.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24415163990301.png)

| Item | Description |
| --- | --- |
| Total | The total number of devices that connected to your network during the time range and filter. |
| New | The number of devices detected in the period defined in the time range filter, which were not detected in the preceding period of the same duration. |
| Identified IoT Devices | The total number of IoT devices that connected to your network during the time range and filter. |
| Identified OT Devices | The total number of OT devices that connected to your network during the time range and filter. |

### Discover Now Widgets

The **Discover Now** section contains several widgets that visually display the total number of devices by a variety of criteria, such as operating system and manufacturer.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Devices Overview Discover Now Active Devices.png)

| Item | Description |
| --- | --- |
| Device Types Filter | The number of each type of device that connected to your network during the time range and filter. Clicking on a device type filters the dashboard to that device type. |
| Device Types Graph | The number of different device types that connected to your network during the time range and filter. The graph represents different device models that have connected. Hovering over a segment displays the number of devices of that model, and the percentage of that device model out of the total number of devices. |
| Device Type List | The number of each device model that connected to your network during the time range and filter. |
| Active Devices | Shows the number of active devices over time, broken down by device category. Use the check boxes to show or hide categories. |
| Device Types | The number of each device type that connected to your network during the time range and filter. |
| Operating System | The number of devices running each operating system that connected to your network during the time range and filter. |
| Manufacturer | The number of devices from each manufacture that connected to your network during the time range and filter. |

### Security Widgets

The **Security** section helps to identify potential security risks associated with devices in your network. For example, you can review events for devices that were blocked by the IPS service or the Internet firewall.

![Security_Device.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24415188211229.png)

| Item | Description |
| --- | --- |
| Devices by Threat | The number of block IPS events per device category and type during the time range and filter. This widget can be filtered by the type of IPS rules. |
| All Events by Category | Total number of events per device category during the time range and filter. Use this widget to add or remove a device category from the dashboard filter, or navigate to the **Events** or **Device Inventory** pages with a preset filter for the selected category. |
| Top IoT Services | List of applications that generated events and frequency of the event on an IoT device during the time range and filter. |
| Top OT Services | List of applications that generated events and frequency of the event on an OT device during the time range and filter. |
| Top Device Types by Firewall Events | The devices that generated a firewall event and the frequency of the event. This widget can be filtered by Outbound (Internet) and WAN firewalls. |
| Devices by Site | The number of devices that connected to your network from each site during the time range and filter. |
