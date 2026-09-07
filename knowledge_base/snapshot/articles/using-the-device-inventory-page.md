---
title: "Using the Device Inventory Page"
slug: "using-the-device-inventory-page"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/using-the-device-inventory-page"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Device Inventory Page

This article discusses how to use the Device Inventory page to keep track of the devices connected to your network.

## Overview of the Device Inventory Page

The Device Inventory page is a single dashboard that provides visibility for all devices that have connected to the network. The page shows a wealth of data about IT, IoT, and OT devices, all of which are classified into granular categories. With the advanced filtering options, you can filter for specific criteria and show all the devices that match the criteria. For example, you can show all IP cameras on the network, and check their operating system versions. For more information, see [What is Device Inventory?](/v1/docs/what-is-device-inventory).

The page includes widgets that show information such as:

- **Devices by Site**
- Clicking on the device shows the Quick View containing a summary of the events generated from the device and detailed device information for example the MAC Address or the apps the device is accessing
- The source of the data being displayed. For example, if the data was collected by Cato or a [third-party integration.](/v1/docs/device-management-connectors)
- The number of devices by the following criteria:
  - **Operating System**
  - General device **Category**, such as: Server, IoT, Mobile
  - Specific **Device Type**, such as: Workstation, Printer, Network Appliance, Mobile Phone, etc.
  - **Manufacturer**

## Getting Started with Device Inventory Page

Use the time range filter to determine the time window for the device data shown on the page. For more information, see [Setting the Time Range Filter](/v1/docs/setting-the-time-range-filter).

![Device_Inventory_EA.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28140574884637.png)

**To show the Device Page:**

- From the navigation menu, click **Home > Devices > Inventory** tab.

## Grouping the Devices

To help you analyze the devices on your network, you can show the devices in groups defined by details including **Site**, **User**, **Manufacturer**, **Type**, and more. For example, you can show together all of the devices related to a specific site, or all IP cameras on the network.

**To group the devices in the Device Inventory page:**

1. From the navigation menu, click **Home > Devices**.
2. On the **Inventory** tab, from the **Group By** drop-down menu, select the required option.

The devices are shown in expandable groups.

## Best Practices for Detection Accuracy

For optimal device detection, accuracy, classification, and granular data, we recommend the following practices:

- [TLS Inspection](/v1/docs/configuring-tls-inspection-policy-for-the-account) enabled
- Using the Cato Cloud as a DHCP server. For more about using Cato Cloud as the DHCP server, see [Configuring DHCP Settings](/v1/docs/configuring-dhcp-settings)

## Supported Devices and Known Limitations

- For devices to be correctly detected, they must communicate with identifiers in one of the following protocols: DHCP, HTTP, MAC, TCP/IP, FTP. Devices that use other protocols are not fully supported, however they might still appear in the Devices page with limited data. For example, a device might be identified as a generic Windows device instead of an IoT device
- A device that didn't communicate for 3 days in WANbound or outbound traffic won't appear in the Devices page. For example, if a user took home a mobile device and didn't use it for 3 days
- Occasionally, the same device might appear more than once on the page, under different **Device IDs**. This can happen if the device connects to the network with multiple IP addresses within a 24 hour period
- Occasionally, different devices might appear under the same entry and **Device ID**. This can happen, for example, if a mobile device and workstation connect using the same IP address within a 24 hour period. When this occurs, the entry might contain conflicting or inaccurate data
