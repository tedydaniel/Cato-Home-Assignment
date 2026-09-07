---
title: "Product Update - Sept. 4th, 2023"
slug: "product-update-sept-4th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-sept-4th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Sept. 4th, 2023

## New Features & Enhancements

- **Improved Section Management for Firewalls:** We’ve added the following usability enhancements to the [Internet and WAN Firewall](/v1/docs/adding-sections-to-the-wan-and-internet-firewalls) policies:
  - A more intuitive process for creating new sections
  - Drag and drop entire sections, and automatically update rule priorities
  - Drag and drop individual rules between sections
- **Create Static Hosts Directly from Known Hosts Page:** The [Known Hosts](/v1/docs/showing-known-hosts-for-a-site) page shows discovered hosts on your site. With one click you can save a discovered host as a [static host](/v1/docs/defining-hosts-for-a-site). This enhancement simplifies the process of saving dynamically discovered hosts as static hosts with reserved IP addresses.
  - The discovered host’s information such as name, IP address, and MAC address are automatically configured to the static host settings
- **Define Country Conditions in Application Control Policy:** We are enhancing the App Control and [Data Control](/v1/docs/creating-the-data-control-policy) rules to include a **SourceCountry** condition. For example, you can set a rule that allows the download of PII to users only in the US.
- **Enhancement for SaaS Security API Dashboard:** We added a [widget](/v1/docs/using-the-data-protection-api-dashboard) that shows the number of events for each rule action. For example, you can see the number of **Quarantine** and **Remove Share** events for the account.
- **New Event Presets:** We are introducing these event presets in the [Events](/v1/docs/analyzing-events-in-your-network) page: Network Connectivity, Socket Upgrade, BGP, and LAN Firewall events types.
- **Deprecating Log Exporter:** We are deprecating the Log Exporter feature and it will be End of LIfe in favor of alternative solutions that provide better coverage, consistency, performance, and ease of use.
  - For accounts that are currently using the Log Exporter, you can continue using this feature until March 2024. After this time, you will no longer be able to use this feature to download log files from the Cato AWS S3 bucket.
  - For all other accounts, starting on Sept. 10th you can’t enable the feature and the Log Exporter page will be removed from the Cato Management Application.
  - You can use one of these solutions to export the events for your account:
    - [Events Integration](/v1/docs/integrating-cato-events-with-aws-s3) to push events to an AWS S3 bucket that belongs to your organization
    - [eventsFeed API](https://api.catonetworks.com/documentation/#query-eventsFeed) to query events to a SIEM solution
    - [auditFeed API](https://api.catonetworks.com/documentation/#query-auditFeed) to export the Audit Trail for your account

## Security Updates

- **IPS Signatures:** View more details about the IPS Signatures and Protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - Ransomware Oiltraffic (New)
  - Ransomware RYK (New)
  - Malware IcedID (Enhancement)
  - CVE-2023-38205
  - CVE-2023-33134
  - CVE-2023-29300
  - CVE-2023-29298
  - CVE-2023-24489
  - CVE-2023-2122
  - CVE-2022-43769
  - CVE-2022-37024
  - CVE-2022-24630
  - CVE-2021-46393
  - CVE-2021-43778
  - CVE-2016-6415
- **Suspicious Activity Monitoring:** These protections were added to the [SAM service](/v1/docs/monitoring-suspicious-activity-with-ips-sam):
  - Exfiltration to High Popularity Online Storage and Code Repository Services
  - Remote Execution with WinRM via PowerShell (Encrypted Data Transmission)
  - Remote Execution with WinRM (Encrypted Data Transmission)
  - Remote Service Creation After EXE Transfer to Admin Share (PsExec-Like Behavior)
- **Apps Catalog:**
  - Added dozens of new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), including these highlights:
  - Bing AI Chat (New)
  - Hola VPN (New)
  - Shoretel (Enhancement)
- **Application Control Policy (CASB):**
  - Granular Activity: OneDrive Business SharePoint - Share (New)
- **OS Detection:** Improved identification of the OS for PS5

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
