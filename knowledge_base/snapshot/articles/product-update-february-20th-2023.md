---
title: "Product Update - February 20th, 2023"
slug: "product-update-february-20th-2023"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-february-20th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - February 20th, 2023

## New Features & Enhancements

- **New Socket v17 Firmware Released:** We are starting the gradual update to Socket version 17, including this content:
  - **BGP Behavior Optimization:** Previously, when a Socket was disconnected from the Cato Cloud, sometimes it would only withdraw ranges for remote Socket sites, while ranges for other remote site types, like IPSec, were not withdrawn. Now the Socket no longer advertises any remote ranges when it is not connected to the Cato Cloud.
  - **Enhancement for Traffic Capture Using the Socket WebUI:** The new traffic capture tool lets you capture traffic from multiple Socket interfaces at the same time, and also includes enhanced packet filtering capabilities.
- **Internet Traffic Backhauling Now Supports IPsec Gateway Sites:** You can use network rules to backhaul specific Internet traffic to [IPsec sites](/v1/docs/backhauling-traffic-via-an-ipsec-site) that are designated as backhauling gateways.
- **Reduced Traffic for Off-Cloud Transport with Last-Resort Links:** When a Socket link is set to precedence 3 (Last-Resort), the Off-Cloud transport setting is now automatically disabled for that link. This new behavior will reduce the control traffic for these links, which is beneficial for last-mile transports such as LTE.
  - There is no change to existing links that are configured to precedence 3 (Last-Resort)
- **Cato Management Application Enhancements:**
  - **Upgrading Site Type from X1500 Socket to X1700:** You can now update the [Connection Type for your Socket sites](/v1/docs/how-to-change-the-socket-model-for-a-site) and adjust the interface settings for the Socket ports.
    - Previously, you needed to contact Support to make these changes
    - If necessary, you can also change a site from X1700 Socket back to X1500
  - **New Portal for Cato API Reference Guides:** In addition to Knowledge Base articles, you can see the explanation of API fields and arguments in our new easy-to-use [portal](https://api.sta.catonet.works/documentation/#introduction).

## Security Updates

- **IPS Signatures:**
  - CVE-2023-21706
  - CVE-2023-21529
  - CVE-2022-47966
  - CVE-2021-46422
  - CVE-2018-5430
- **Application Database:**
  - Added more than 200 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog))
  - SUNMI (New)
  - ByteDance (Enhancement)
  - ExpressVPN (Enhancement)
  - MEGA (Enhancement)
  - TikTok (Enhancement)
- **Application Control Policy (CASB):**
  - Enhanced granular actions for these apps:
    - Box: Login, Upload
    - Microsoft: Login
- **Data Loss Prevention (DLP):**
  - Enhanced granular actions for these apps:
    - Box: Login, Upload

## Knowledge Base Updates

- [How to Integrate Third-Party DDoS Services for Internet-Facing RPF Traffic](/v1/docs/how-to-integrate-third-party-ddos-services-for-internet-facing-rpf-traffic)
- [Backhauling Traffic via an IPsec Site](/v1/docs/backhauling-traffic-via-an-ipsec-site)
