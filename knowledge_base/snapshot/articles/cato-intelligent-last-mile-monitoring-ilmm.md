---
title: "What is Cato ILMM"
slug: "what-is-cato-ilmm"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/what-is-cato-ilmm"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What is Cato ILMM

Cato's Intelligent Last-Mile Monitoring (ILMM) service, is a global, last-mile monitoring and management service designed for today’s enterprise.

Cato has a dedicated Network Operation Center (NOC) team that is responsible for the ILMM service and resolving any last mile issues with the Internet Service Providers (ISPs) around the world. The ILMM monitors active Sockets and provides:

- Detecting link outages or degradations in real-time
- Proactively opening tickets with the ISP and follow-up until the link service is restored
- A closed feedback loop for customers with the NOC team

ILMM customers sign a Letter of Authorization (LOA) with the ISP, which gives Cato the legal authority to open tickets with the ISP on behalf of the customer. When the last-mile issue is resolved, Cato automatically notifies the customer with details of the resolution. Communication with the contacts for each site is in English.

For sites with a high availability (HA) configuration, ILMM only monitors the active Socket. The passive Socket isn't monitored. When the primary Socket fails over to the secondary Socket, then ILMM monitors the active secondary Socket.

## Managing ILMM in the Cato Management Application

ILMM is one of Cato's Managed Services in the Cato Management Application, and it provides one place to easily manage all of the items related to the ILMM service.

These are the screens that you can use to manage and onboard the ILMM service for your account:

- **Sites** - Overview of the physical Socket sites and manage the ILMM licenses
- **Links** - Overview and management of the ILMM service for the WAN links
- **ISPs Info & LOA** - Manage the ISPs and their LOAs
- **ILMM Notifications** - Select the mailing list for the ILMM administrative email notifications

## Related Resources

- [Managing ILMM for Your Account](/v1/docs/managing-ilmm-for-your-account)
- [Working with ILMM License for Sites](/v1/docs/working-with-ilmm-license-for-sites)
