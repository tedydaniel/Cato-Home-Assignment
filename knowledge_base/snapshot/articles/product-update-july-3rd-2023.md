---
title: "Product Update - July 3rd, 2023"
slug: "product-update-july-3rd-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-july-3rd-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - July 3rd, 2023

## New Features & Enhancements

- **New X1600 Socket Model for Mid-Size Sites:** The [X1600 Socket](/v1/docs/cato-socket-deployment-guides-and-data-sheets) bridges the gap between the X1700 and X1500 Sockets, with the following details:
  - 1 Gbps max tunnel throughput
  - 8 ports (in total)
  - Fiber ports
- **Immediately Validate DLP Content Scans:** For each DLP [Data Type](/v1/docs/working-with-custom-data-types-for-dlp), you can verify that the DLP engine recognizes and matches the sensitive data. For example, when you define a Keyword data type, you can upload and scan a test file to validate that the DLP engine detects the keywords. This helps you make sure that different Data Types correctly match content and prevent users from leaking sensitive data.
  - All DLP data types can be validated using test files, including: predefined types in the [Data Types Catalog](/v1/docs/creating-dlp-content-profiles), user defined data types, and [sensitivity labels](/v1/docs/using-mip-sensitivity-labels-in-your-cato-dlp-policy)
  - For better troubleshooting and enhanced supportability for cases where the file doesn’t match the data type, you can download a text file of the content extracted by the DLP engine
- **DLP Engine Now Detects Encrypted Files:** We enhanced the [DLP](/v1/docs/what-is-the-cato-dlp-service) engine with the ability to identify and block [encrypted files](/v1/docs/creating-the-data-control-policy) to let you prevent users from uploading or downloading sensitive information hidden in password-protected files.
- **Change to Preferred PoP Settings:** You are no longer able to manually define the following China PoP locations for the site’s **Preferred PoP location** settings: **Beijing_DC3, Beijing_DC4, Shanghai_DC3, Shanghai_DC4, Shenzhen_DC4** Existing sites configured with these China PoP locations will continue to get service from these PoPs.
  - No configuration changes are required
  - Existing sites will not be impacted by the change
  - The PoPs mentioned above will keep providing services

## Cato SDP Client Releases

- **Linux Client v5.1:** The [Linux Client v5.1](/v1/docs/summary-of-cato-linux-client-releases) was uploaded to the [Client download portal](https://clientdownload.catonetworks.com/)
- **Reminder - End of Life for Linux, iOS and Android Clients Earlier than v5.0:** Linux, iOS and Android Clients earlier than v5.0 are now declared [end of life](/v1/docs/eos-for-linux-ios-and-android-clients-earlier-than-v5-0)

## PoP Announcements

- **Ashburn, United States:** A second Cato PoP will shortly become available in Ashburn
- **Nairobi, Kenya:** A new Cato PoP will shortly become available in Nairobi
