---
title: "Upgrade Azure vSocket Public IPs from Basic to Standard SKU"
slug: "upgrade-azure-vsocket-public-ips-from-basic-to-standard-sku"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/upgrade-azure-vsocket-public-ips-from-basic-to-standard-sku"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upgrade Azure vSocket Public IPs from Basic to Standard SKU

As part of Microsoft Azure’s planned service changes, Basic SKU Public IP addresses will be [retired on September 30, 2025](https://learn.microsoft.com/en-us/answers/questions/1033456/retirement-announcement-basic-sku-public-ip-addres). If your Azure vSocket site is currently using Basic SKU public IPs, action is required to ensure uninterrupted service.

## **What You Need to Know**

- Basic SKU Public IPs are being deprecated. Microsoft requires all customers to migrate to Standard SKU Public IPs.
- Dynamic IPs should be changed to static: Standard SKU IPs are static by design, and we recommend updating any existing dynamic IPs to static before migration.
- Your IP address may change: During the upgrade process, the public IP associated with your vSocket may change. Please plan for possible reconfiguration of DNS records or dependent systems.

## **Microsoft Documentation & Upgrade Guidance**

To assist you, Microsoft has provided detailed migration instructions:

- General Upgrade Guidance: [Upgrade Basic Public IP Address to Standard SKU in Azure](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-basic-upgrade-guidance)
- Upgrade Process for VMs in Availability Sets: [Upgrade all public IP addresses attached to VMs in an Availability Set from Basic to Standard](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-upgrade-availability-set?source=recommendations)

## **What Happens If I Don’t Make these Changes**

We encourage you to begin planning your migration as soon as possible to avoid any potential issues.

If you don’t migrate the Basic SKU Public IPs to Standard SKU Public IPs by Sept 30, 2025, then your vSocket may experience outages.
