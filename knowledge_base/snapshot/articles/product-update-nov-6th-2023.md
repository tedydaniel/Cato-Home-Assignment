---
title: "Product Update - Nov. 6th, 2023"
slug: "product-update-nov-6th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-nov-6th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Nov. 6th, 2023

## New Features & Enhancements

- **Improved Process to Redeploy a vSocket:** You can now re-install a vSocket for a site without removing and recreating the site. We added an option to the Cato Management Application to unregister an existing vSocket from a site, and then recreate the vSocket and redeploy it on a new VM resource.
  - For example, you can use this process to migrate a vSocket to a different VNet/VPC, or reinstall a vSocket on a different VM instance type
  - During the process the site configuration is preserved
  - Available for AWS, Azure, or ESXi sites
- **Arctic Wolf Supports Cato for SIEM Integration:** For Cato customers that also use Arctic Wolf, you can [connect your Cato account](https://docs.arcticwolf.com/cloud/cato_credentials.html) to send event data to their Cloud Detection and Response service.
  - [Read more](/v1/docs/cato-data-third-party-supported-integrations) about other SIEM vendors that integrate with Cato
- **Improved Search for LAN Firewall Page:** The search capability of the [LAN Firewall](/v1/docs/configuring-the-socket-lan-firewall-policy) page now includes all fields.

## Cato SDP Client Releases

- **Update Your DNS Configuration to Support Office Mode:** We made improvements to ensure the Client more accurately selects the best PoP location to connect to. Following this improvement, if you use a private DNS server, add this DNS entry to support remote users when they connect in Office Mode:
  - [tunnel-api.catonetworks.com](http://tunnel-api.catonetworks.com/) resolves to IP address 10.254.254.3 (or the customized reserve service range x.y.z.7 IP address)

## PoP Announcements

- **Miami, United States**: A new range (150.195.202.0/24) is now available in the Miami, US PoP location

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](https://support.catonetworks.com/hc/en-us/articles/11968052021277-Understanding-Cato-s-Gradual-Rollout). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
