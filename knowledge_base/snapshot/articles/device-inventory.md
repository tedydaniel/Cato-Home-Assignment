---
title: "What is Device Inventory?"
slug: "what-is-device-inventory"
updated: 2026-08-30T12:40:20Z
published: 2026-08-30T12:40:20Z
canonical: "knowledge.catonetworks.com/what-is-device-inventory"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is Device Inventory?

This article explains the Cato Networks IoT/OT Security service and how to use Device Inventory in the Cato Management Application (CMA) to discover devices on your network. Then you can monitor the devices and create firewall rules to manage their access control.

## Overview

IoT/OT Security is the Cato service you can use to discover, monitor, and manage devices connected to your network. The Device Inventory engine analyzes WANbound and outbound traffic to detect, identify, and classify connected devices. The Cato Cloud automatically identifies the devices using a passive method of detection with no special setup or agents required.

The Device Inventory engine uses machine learning and AI to identify each device, giving you a full inventory of devices and detailed data for each device.

You can configure integrations with third-party apps to automatically include their collected data in the **Device Inventory** page. For more information and a list of supported applications, see [Device Inventory Connectors](/v1/docs/device-management-connectors).

![Device_Inventory_EA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26773196442653.png)

A separate Device Inventory license is required for Device Inventory pages and features. For more about purchasing a license, please contact your Cato representative.

### Device Inventory Use Cases

#### Only Allowing Approved Video Conferencing Device Manufacturers

A security admin receives a task to review the security posture of the meeting rooms in the site for the London branch office. The admin goes to the [Device Inventory](/docs/what-is-device-inventory#UUID-175e1012-d91f-eb1c-99b6-6506ec00134c) page, filters for **Field - Device Type**, **Operator - In**, **Value - Video Conferencing** , and sees all the video conferencing devices in the London site. The admin realizes that there are video conferencing devices from several different manufacturers, and this does not meet the organizational security policy. The IT team already have an IoT security license and creates new rules in the WAN and Internet firewall policies with **Device Attribute** settings that only allow the two approved manufacturers for the video conferencing devices. Some of the video conferencing devices in the London site will no longer work because they are blocked by the firewall policies until they can be replaced with new devices from the approved manufacturers.

#### Weekly Security Review with Device Dashboard

During the weekly meeting for the SecOps team, they use the Device Dashboard to review the number of new device types and categories that connected to the network.

Then they review the widgets in the **Security** section to trace any anomalous behavior that was detected by the security engines. When they find something suspicious, they use options to pre-filter the relevant CMA pages:

- **View in Device Inventory** is used to follow up on the device details and data
- **View Events** is used to get more data about the traffic and connections

## Discovering Devices with Device Inventory

The **Device Inventory** page is continuously updated with new devices and data based on the Device Inventory engine. It can take up to 12 hours to complete the identification process and for the data to be displayed on the relevant pages (such as **Device Inventory** and **Device Dashboard**). The engine categorizes as much data on the device as it can confidently identify. This means that not all of the data fields may be available for a specific device.

Due to the fact that the device identification is based on the device behavior patterns, it's possible that the data and fields for a specific device can be incorrect.

For more information, see [Using the Device Inventory Page](/v1/docs/using-the-device-inventory-page).

### Understanding Device Confidence

To help you evaluate how reliable the device identification is, Cato assigns each device a Confidence level. The level for each device is shown in the Device Inventory and indicates how reliably the engine can identify and classify the device. Possible values are **High**, **Medium**, and **Low**. Lower Confidence levels usually indicate that Cato has less information available to identify the device, such as its Manufacturer, Model, or OS.

### Devices with Multiple Network Interfaces

For devices with multiple network interfaces (NICs), Cato provides a complete view of the device by associating all detected MAC addresses, IP addresses, and networks with the same device entry in the Device Inventory. This helps you find and identify the device regardless of which interface or IP address it uses.

## Monitoring Devices with Device Dashboard

The **Device Dashboard** is a centralized interface that provides visibility to monitor connected devices within your network. The dashboard focuses on two tasks, **Discover Now** and **Security**.

The **Discover Now** section contains several widgets that visually display the total number of devices by a variety of criteria, such as operating system and manufacturer.

The **Security** section helps to identify potential security risks associated with devices in your network. For example, you can review events for devices that were blocked by the IPS service or the Internet firewall.

You can drill-down for further analysis by selecting an item in the widget, and show the filtered data in the **Device Inventory** or **Event** page.

For more information, see [Using the Device Dashboard](/v1/docs/using-the-device-dashboard).

## Enforcing Firewall Policies for Devices

You can define WAN, Internet, and LAN firewall policies that specify which types of devices are allowed or blocked from accessing certain network resources.

Use the **Device Attributes** condition to define rules for devices that were detected on the network by the Device Inventory engine. You can use the following attributes in a firewall rule: **Category**, **Type**, **Model**, **OS**, **Manufacturer**, **OS Version**.

For more information, see [Adding Device Conditions to Firewall Rules](/v1/docs/adding-device-conditions-to-firewall-rules).

## Device Attributes

These are the attributes that are identified and managed as part of Device Inventory:

1. Type
2. Manufacturer
3. Model
4. OS
5. Category
6. OS version
7. Device name
8. MAC Address
9. Device IP

## Related Resources

For more information about IoT/OT Security, see these Cato blog posts:

- [Leveraging MAC Address Logic for IoT Classification](https://www.catonetworks.com/blog/leveraging-mac-address-logic-for-iot-classification/)
- [Advanced Behavioral Analysis of IoT and OT Devices for IoC Collection](https://www.catonetworks.com/blog/cato-ctrl-advanced-behavioral-analysis-iot-ot-devices-ioc-collection/)

## Known Limitations

- Firewall rules with **Device Attribute** settings are enforced only for devices whose MAC address was detected. Cato recommends as a best practice to use the Cato DHCP service to help ensure detection of MAC addresses.
- For known limitations related to devices appearing on the Devices page, see [Using the Device Inventory Page](/v1/docs/using-the-device-inventory-page).
