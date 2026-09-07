---
title: "Product Update - February 10, 2025"
slug: "product-update-february-10-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-february-10-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - February 10, 2025

## New Features & Enhancements

- **IoT/OT Security Service Providing Visibility and Control of Assets:** Cato recently announced the Device Inventory service that provides visibility and policy enforcement for IT, IoT, and OT devices, including:
  - AI-powered device visibility, discovery, and classification with the [Device Inventory](/v1/docs/using-the-device-inventory-page) and [Device Dashboard](/v1/docs/using-the-device-dashboard) pages
  - Extend Cato’s single context with multi-level asset classification that enriches events with properties such as manufacturer, function, type, and more
  - Solve complex contextual access control and segmentation challenges with AI classification-based [device conditions](/v1/docs/adding-device-conditions-to-firewall-rules) in Internet and WAN firewall policies
  - Tailor security protections for various device types and manufacturers

- **Events Page Quick View:** We added a fast-loading view of the [Events page](/v1/docs/analyzing-events-in-your-network) that displays the most commonly used fields.
  - Viewing only Quick View fields improves performance when exporting data
  - You can disable Quick View to show all event fields (possible performance impact)
  - Click [here](https://academy.catonetworks.com/events-page-quickview/) to watch a video recording of this feature

- **XDR APIs (Beta) No Longer Support limit=0:** Following industry best practices, we are changing the functionality of the limit field for the API queries [stories](https://api.catonetworks.com/documentation/#query-xdr.stories) and [story](https://api.catonetworks.com/documentation/#query-xdr.story), so that limit=0 is no longer supported. To ensure continued smooth operation, you need to update any scripts or queries that rely on this parameter. Instead, you can set a limit between 1-2000, which the API fully supports. If you need to retrieve all stories, we recommend using a pagination approach.

## PoP Announcements

- **Los Angeles, United States:** A new range (199.27.32.0/24) is now available for the Los Angeles PoP location.
- **Tokyo, Japan:** A new Tokyo DC4 PoP location (150.195.222.0/24) will soon be available.
  - Tokyo_DC4 is available as a PoP location for [**Preferred PoP**](/v1/docs/defining-a-preferred-pop-for-a-site), and [Network Rule](/v1/docs/configuring-network-rules) **Route Via** settings

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
