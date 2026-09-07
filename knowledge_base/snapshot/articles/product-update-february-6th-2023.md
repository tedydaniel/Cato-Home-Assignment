---
title: "Product Update - February 6th, 2023"
slug: "product-update-february-6th-2023"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-february-6th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - February 6th, 2023

## New Features & Enhancements

- **Announcing New Site Throughput up to 5 Gbps:** We improved the infrastructure of the Cato Cloud to support up to 5Gbps throughput per site. These are the types of sites that can provide the faster performance:
  - X1700 Sockets
  - IPsec sites with AES 128 GCM and AES 256 GCM algorithms
- **Review All your Cato Tickets in the Cato Management Application:** Over the next few weeks we are gradually releasing the new Tickets screen, which shows tickets for all Cato services including: Support, ILLM, and MDR. You can open a ticket in a new tab and view the details or manage the ticket.
- **Quickly Review Status for Monitoring Sites and Users:** We completely rebuilt the [site and user preview](/v1/docs/using-the-topology-page) in the **Topology** screen (Monitoring > Topology), and you can easily review the status of the site, links, HA configuration, and more. The preview also provides easier navigation for site and user settings.
- **IPsec IKEv2 Sites Support Single Traffic Selectors:** Additional traffic selector configuration options to improve interoperability with third-party devices (such as Cisco ASA). We added an option to configure a single traffic selector per packet.
- **More Accurate Processing for FQDN in Security Policies - No Impact to Accounts:** The current behavior for **FQDN** entities in security and network rules, is that they are processed as Top Level **Domain** (TLD) entities. Starting on Feb. 20, 2023, Cato will migrate the **FQDN** entities to **Domain** entities, which reflects how these entities are processed.
  - No action is required, and this change will not impact the behavior of any Security and Network policies
  - After Mar. 6, 2023, adding an FQDN entity to a security rule or network rule will be processed as [exact match FQDN](/v1/docs/what-is-the-cato-wan-firewall)
- **Apply Granular Device Conditions in TLS Inspection Policies:** You can now configure specific [platform, country, and device posture](/v1/docs/adding-device-conditions-for-tls-inspection) conditions when creating or editing a policy. For example, you can now create a policy that only applies to iOS devices located in the United States that are in an "unsupervised" posture. This added flexibility allows for more precise control over the implementation of TLS inspection in your organization.
- **Enhanced Support for DNS Forwarding:** We improved DNS response time and redundancy for [DNS Forwarding](/v1/docs/defining-dns-forwarding-rules), and you can now define up to **six** servers in each rule.

## Cato SDP Client Releases

- **iOS Client v5.1:** In the next few days, the iOS SDP Client version 5.1 will be available to download from the App Store. This version includes:
  - Fixed bug where the Client didn’t reconnect to the network after the iOS device was activated from sleep mode

## PoP Announcements

- **Salt Lake City, United States:** A new Cato PoP will shortly become available in Salt Lake City.

## Security Updates

- **IPS Signatures:**
  - Apache Flink Remote Code Execution Vulnerability
  - CVE-2023-0569
  - CVE-2022-41828
  - CVE-2022-37190
  - CVE-2022-32572
  - CVE-2022-25458
  - CVE-2022-25456
  - CVE-2022-25453
  - CVE-2022-25452
  - CVE-2022-25449
  - CVE-2022-25448
  - CVE-2022-25447
  - CVE-2022-25445
  - CVE-2022-25073
  - CVE-2019-13635
  - CVE-2018-9206
  - CVE-2018-18809
  - CVE-2018-13324
  - CVE-2014-125033
- **Application Database:**
  - Added more than 200 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog))
  - Grab (New)
  - WeChat File Transfer (New)
  - Ariba (Enhancement)
- **Application Control Policy (CASB):**
  - Enhanced granular actions for these apps:
    - iCloud: Upload, Download
    - Zendesk: Export
- **Data Loss Prevention (DLP):**
  - Enhanced granular actions for these apps:
    - iCloud: Upload, Download
