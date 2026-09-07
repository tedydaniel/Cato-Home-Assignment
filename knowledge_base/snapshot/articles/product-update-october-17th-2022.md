---
title: "Product Update - October 17th, 2022"
slug: "product-update-october-17th-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-october-17th-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - October 17th, 2022

## New Features & Enhancements

- **Use SDP Device Posture, Source Operating System, and Source Country Conditions in Firewall Policies:** Starting on October 23, new source device settings are supported for WAN and Internet firewall rules and gives you the ability to include conditional access based on the actual device of the SDP user. [Read more](/v1/docs/adding-device-conditions-to-firewall-rules).
- **DLP User-Defined Data Types:** Starting on October 23, you can now create your own custom-sensitive data types to meet your specific business needs. Use keywords, dictionaries, regular expressions and thresholds to protect from sensitive data loss. [Read more](/v1/docs/working-with-custom-data-types-for-dlp).
- **Improved Management for Groups:** Starting on October 23 (and gradually releasing over the next several weeks), to help simplify managing users in your account, such as SDP and User Awareness users, we added User Groups to the Cato Management Application. These new groups can only contain users and are conveniently located in the Access tab (Access > User Groups).
  - The previous groups (Assets > Groups) can contain the other items such as: sites, network ranges, hosts, and so on.

## Security Updates

- **IPS Signatures:**
  - CVE-2022-41040 Microsoft Exchange Server Side Request Forgery
  - CVE-2022-41082 Microsoft Exchange Server Remote Code Execution
- **Application Database:**
  - Added more than 250 new SaaS applications (you can view the SaaS apps in Monitoring > Cloud Apps Catalog) including WeChat File Transfer
  - Enhanced over 60 SaaS applications
    - The **Screen** app was renamed to **Screen Cloud**
- **Updates to Application Control Policy:** New granular actions for this app:
  - Citrix ShareFile: Upload, Download
