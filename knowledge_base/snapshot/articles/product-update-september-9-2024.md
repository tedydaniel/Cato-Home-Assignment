---
title: "Product Update - September 9, 2024"
slug: "product-update-september-9-2024"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-september-9-2024"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - September 9, 2024

## New Features & Enhancements

- **DLP Enhancement - More Languages for OCR Scans:** Our enhanced DLP engine now supports [OCR in 99 languages](/v1/docs/creating-dlp-content-profiles), ensuring your sensitive information is protected across diverse environments. The engine extracts text from image files and then scans the extracted text for all languages.
  - You can select up to 5 languages to scan for your account
  - Previously, OCR scans were supported only for English
  - Also supported for out-of-band [SaaS Security API Data Protection](/v1/docs/what-is-the-data-protection-api) scans
- **RBI Enhancement - Continue Browsing in the Same Session:** To enhance browsing security and improve end-user experience, we added an option to let users continue browsing to multiple domains within the same [RBI session](/v1/docs/configuring-the-rbi-service-for-browsing-sessions). These are example use cases for continuing the same RBI session:
  - **Authentication:** Configure a list of domains including all subdomains of a file-sharing app to let users sign in when they are redirected to a different domain to authenticate. Previously, users were redirected to a new RBI session and couldn't sign in.
  - **Prevent Non-Isolated Browsing to Risky Domains:** Create an extensive domain list using wildcards to ensure the user’s entire browsing session takes place in an isolated environment, even if the user navigates away from Uncategorized or Undefined domains
  - Click [here](https://academy.catonetworks.com/avoiding-rbi-escape-isolation) to watch a video explaining this feature
- **mDNS Across Multiple Subnets for Socket Sites:** This feature enables [mDNS across multiple VLANs](/v1/docs/enabling-mdns-between-subnets) within the branch. mDNS is commonly used for AirPrinting and other zero-configuration-based networking features. When the Socket acts as an mDNS gateway, mDNS requests and responses from clients on one subnet are forwarded to other subnets.
  - Not supported for virtual Sockets and routed subnets
  - Supported for physical Sockets running v20.0.18453 and higher
  - Click [here](https://academy.catonetworks.com/mdns-support-for-socket-sites) to watch a video explaining this feature

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
