---
title: "Product Update - July 14, 2025"
slug: "product-update-july-14-2025"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/product-update-july-14-2025"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - July 14, 2025

## New Features & Enhancements

- **New Release for Linux Client v5.5:** Starting July 13, 2025, we are rolling out the new Client version 5.5 for Linux. This version includes:
  - Advanced Device Posture Collection - To improve performance when connecting, Device Posture is now collected continuously, even before connecting, to ensure Device Posture stays up-to-date.
    - Previously, this was supported only on Windows Client v5.15 and macOS Client v5.9
  - Security update:
    - Patch for a vulnerability ([CVE-2025-7012](/v1/docs/cve-2025-7012-linux-sdp-client-local-privilege-escalation)) impacting Linux Clients v5.4 and lower
  - Additional bug fixes and enhancements
  - Linux Client v5.5 is supported from Ubuntu v20 and higher
- **Network Stories Auto-Closure Enhancements:** In the coming weeks, we're updating the conditions for automatically closing [Network Stories](/v1/docs/reviewing-site-operations-stories), even when the issue isn't fully resolved. These are the new conditions for closing stories:
  - 30 days old – Closed to ensure fresh tracking if the issue recurs
  - Story requires revalidation – An issue was detected with the story, and the Network XDR engine validates and reopens it if the issue recurs
  - Configuration change – An entity in the story (link, site, BGP range, host) is no longer relevant due to configuration updates
- **Terraform Modules for Bulk Firewall Provisioning:** The new [Internet](https://registry.terraform.io/modules/catonetworks/bulk-if-rules/cato/latest) (bulk-if-rules) and [WAN](https://registry.terraform.io/modules/catonetworks/bulk-wf-rules/cato/latest) (bulk-wan-rules) modules let you automate large-scale provisioning of Internet and WAN firewall policies using Infrastructure as Code. They integrate with CI/CD pipelines and support concurrent policy management, enabling multiple admins to edit and publish the firewall security policies in parallel.
- **Join Cato's Product Rewind Session on July 16:** Product Rewind is a fast-paced monthly webinar, where we will break down the most compelling product updates from June 2025. See the latest innovations in action with live demos and get practical insights on how these updates can enhance your experience.
  - Topics include: Device Inventory drill-down, CatoLabs, Granular control over TLS, Account Overview dashboard
  - Register [here](https://academy.catonetworks.com/product-monthly-rewind/269140) for July 16, 12 pm ET

## PoP Announcements

- **Update for Localized Argentina Range:** The geo-localized range for Argentina (150.195.196.0/24) will now be serviced through the Buenos Aires PoP location.
  - Previously, the range was serviced through Santiago, CL
- **Oslo, NO:** A new Cato PoP will shortly become available in Oslo with the IP range 85.255.22.0/24
- **Beijing, CN:** The following new ranges will soon be added to the Beijing PoP location:
  - 106.39.250.192/26
  - 111.202.125.0/25

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
