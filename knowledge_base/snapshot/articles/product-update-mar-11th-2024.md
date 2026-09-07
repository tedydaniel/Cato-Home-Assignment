---
title: "Product Update - Mar. 11th, 2024"
slug: "product-update-mar-11th-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-mar-11th-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Mar. 11th, 2024

## New Features & Enhancements

- **Split Tunnel Policy for Cato Client:** The [Split Tunnel Policy](/v1/docs/routing-with-the-cato-client-split-tunnel-policy) provides a granular method to easily configure traffic routing for remote users and control which traffic is tunneled towards the Cato Cloud.
  - Configuration can now be managed from a policy with an ordered rule base
  - Use the [Global IP Ranges](/v1/docs/using-ip-ranges-in-policies) global object in the Split Tunnel Policy to adjust rules per user or user group
  - No impact to current split tunnel behavior, IP ranges in the policy are added as Global IP Ranges (even if the feature is disabled)
- **Optimized PoP Selection for Socket Sites**: We improved the accuracy of our automatic PoP selection mechanism by adding the **City** field to the **General** settings of Socket sites. The city for the site lets us use the geographical coordinates where the site is located for ideal PoP selection.
  - The **City** field is a mandatory field when creating new sites, and is also available in the **General** settings for existing sites
    - Editing the **City** field doesn’t impact the current connection to the PoP
- **NAT Policy for Socket Sites:** A new [site-level NAT policy](/v1/docs/configuring-a-site-level-nat-policy) with granular matching conditions and actions, including DNAT and SNAT. With this policy, you can now integrate with third-party networks (such as contractors) connected over Sockets and require NAT to avoid IP conflicts.
  - The policy is already available for IPsec and Cross Connect sites
- **Cato Management Application Enhancement:**
  - **Display Degraded Status for Recent Issues:** You now have the [option to display](/v1/docs/configuring-system-settings-for-the-account) the **Degraded** status only for sites with issues that occurred within the past 30 days. Sites with connectivity issues for more than 30 days appear as **Connected**.
    - Previously the **Degraded** status was always displayed
- **Important Update for Azure vSocket Sites:** Cato identified a new Microsoft validation that impacts Azure vSockets with the **Standard_D2s_v4 VM** size.
  - All impacted customers were sent a dedicated email, you can see the full details [here](/v1/docs/for-microsoft-azure-sites-changing-cato-vsocket-vms-to-standard-d8ls-v5-vm-size).
  - For Azure vSocket sites with the **Standard_D2s_v4 VM** size, it is required to resize the vSocket VM from **Standard_D2s_v4** to **Standard_D8ls_v5**. For more information, see [Resizing VMs for Azure vSockets](/v1/docs/changing-azure-vsockets-to-a-different-vm-size).
  - The vSockets will continue to function normally as long as the VM instance doesn’t power off, so plan your Azure resizing accordingly to prevent future issues.
- **Reminder - Upcoming EoL for Log Exporter:** We are reminding customers that use the Log Exporter feature that it will be End of Life in favor of alternative solutions that provide better coverage, consistency, performance, and ease of use.
  - For accounts that are currently using the Log Exporter, you can continue using this feature until the end of April 2024 (an extension from the original March 2024 EoL date). After this time, you will no longer be able to use this feature to download log files from the Cato AWS S3 bucket.
  - You can use one of these solutions to export the events for your account:
    - [Events Integration](/v1/docs/integrating-cato-events-with-aws-s3) to push events to an AWS S3 bucket that belongs to your organization
    - [eventsFeed API](https://api.catonetworks.com/documentation/#query-eventsFeed) to query events to a [SIEM solution](https://support.catonetworks.com/hc/en-us/articles/5617138183069-SIEM-Integration-Guide-for-the-Cato-API)
    - [auditFeed API](https://api.catonetworks.com/documentation/#query-auditFeed) to export the Audit Trail for your account

## PoP Announcements

- For the following PoP locations, a new IP range is now available:
  - **Atlanta, US:** 216.205.113.0/24
  - **Casablanca, MA:** 150.195.215.0/24
  - **London, UK:** 85.255.27.0/24
  - **Mumbai, IN:** 123.253.153.0/24
  - **Shanghai, CN:** 114.94.55.192/26 and 140.207.250.192/26
- A new geo-localized IP range is available for Barbados, serviced through the Miami PoP location: 45.62.191.112/28
- **Hawaii, US:** A new PoP Location will soon be available in Hawaii with this IP range - 216.205.120.0/24
- For the following PoP locations, a new IP range will soon become available:
  - **Munich, DE:** 85.255.18.0/24
  - **Vancouver, CA:** 150.195.195.0/24

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
