---
title: "DLP Troubleshooting"
slug: "dlp-troubleshooting"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/dlp-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# DLP Troubleshooting

This playbook describes steps to resolve issues when DLP is not working as expected on your account.

## Overview

Complications with Data Loss Prevention (DLP) policies can cause unexpected results, leading to potential security risks. This might be due to configuration that doesn't align with the requirements, or inaccurately defined custom data type or profile.dd

## Initial Assessment Using Events

Filtering for Data Loss Prevention (DLP) events using Events can be achieved by setting the "Apps Security" preset:

[![preset.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16892476976157.png)](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16892476976157.png)

Events that are associated with a data control rules will include insightful fields such as the DLP Profiles that were triggered, matched Data Types, file attributes and more.

This will allow you to understand what is currently being triggered, and further ask yourself 'Are the results in line with what I expected according to my configuration?'

## Troubleshooting The Issue

The troubleshooting process is designed to be sequential, with each step building upon the last. If a preceding requirement isn't met, subsequent steps will not be triggered.

> [!NOTE]
> Note:
> 
> A requirement for all the below steps is to make sure you have a FW rule (even temporarily created for troubleshooting purposes) with **event tracking enabled** that will match on the traffic expected to be inspected by DLP.
> 
> Another troubleshooting-oriented configuration will be a fallback DLP rule catching both upload/download for monitoring purposes with no content matching or file type specification.
> 
> It’s also recommended to test using a non-textual file, such as .docx or .pdf, to ensure file type detection problems related to textual files (more on that below).

### (1) TLS Inspection Enabled (for traffic over TLS)

- **Verify in Firewall Event**: Check the **TLS inspection** boolean field in the generated FW event and make sure it is set to **1**. If the value is set to **0,**, ensure to adhere to the guidelines in the following articles for configuring and testing TLS inspection on your account: - [Configuring TLS Inspection Policy for the Account](/v1/docs/configuring-tls-inspection-policy-for-the-account) - [Testing TLS Inspection in the Cato Cloud](/v1/docs/testing-tls-inspection-in-the-cato-cloud)
- Specific OS types (Android, Linux, Unknown OS's) are not TLS inspected.
- Some native client applications are not TLS inspected (due to certificate pinning concerns). TLS [default bypass rules](/v1/docs/configuring-tls-inspection-policy-for-the-account) can be identified in CMA.
- Make sure your Internet firewall policy contains two rules with a high priority (near the top of the rule-base) to block QUIC and GQUIC, as TLS inspection can not work on this type of traffic: ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16920048220701.png)

To verify that a certain request is or is not using the QUIC protocol, generate a HAR file and inspect the "Protocol" column on the relevant POST/GET request. If a request is using QUIC, it will be listed as "h3", "http/2+quic/46" or similar: ![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16920048228381.png)

### (2) Verify destination application identified by Cato

- **Verify in Firewall Event**: Look at the “Application” event field and search for the identified application.
- In case your application is not identified correctly, ensure the following are true:
  - You are accessing the destination of the application using its hostname instead of directly using the IP address.
    - This step ensures CATO sees the associated DNS query, allowing us to derive the destination's hostname, which is crucial for App detection.
  - Ensure traffic destined to the DNS server you are using to resolve the Host name/s of the destination application is visible to CATO (e.g. reached the Socket LAN interface)
- You can define either a specific application for CASB/DLP policies or select "Any Application" (All HTTP/S application traffic).
  - The full list of what CATO defines as "Cloud Applications" and "Applications" can be found under "Resources -> App Catalog" filtered by the type. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17619087946781.png)
  - You can open an RFE(Request For Enhancement) ticket with CATO Support in case you have a specific application that you'd like to have added as Cloud Application.

### (3) Verifying File Size Requirement

- **Verify in the DLP (sub-type "Apps Security") Event:** Look for the **Threat Verdict** event field and check if the value set to **Bypass By Size** - seeing this value will indicate that the content was not scanned due to the file size not falling into the required minimum/maximum range.
- The maximum file size for inline DLP is **50MB** (500MB for Data Protection API)
  - Generally, you can identify the gzip behavior behind the scenes by following the steps below:
    - Open the browser devtools, “network” tab
    - While downloading a file, spot the request that represents the download (in Google suite, it’s most likely spottable by filtering domain:*.googleusercontent.com, blue frame in the image below)
    - Look for the Content-Encoding header in the response (red frame in the image below). If it’s gzip, you can tell there's compression under the hood ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17619102777373.png)
- For [DLP OCR Profiles](/v1/docs/creating-dlp-content-profiles) Supported File Size is between 10KB and 50 MB

### (4) File Type Is Identified + Supported For DLP

- **Verify in the DLP (sub-type "Apps Security") Event:** Look for the **File Type** field indicating which file class was detected by CATO
- If the value is **Unknown File Types**, that means CATO failed to identify the file + it's being exempted from content scanning.
- Verify the file type is supported for DLP: audio, video, and binary files are not supported.
- Extra caution needs to be exercised when matching the JAR file using the Content Type because a .JAR file can either be a Zip archive or a Java archive (JAR) file. Refer to [Data Control Rule Doesn't Work on JAR File When Match By Source Code](/v1/docs/data-control-rule-doesn-t-work-on-jar-file-when-match-by-source-code) for more details.
- For [DLP OCR Profiles](/v1/docs/creating-dlp-content-profiles), supported file types include: PNG, JPEG, TIFF, BMP, PNM, WEBP, JPEG

**Textual File Detection Limitations**

Textual file detection, such as CSV & TXT, faces challenges due to the absence of specific indicators. Our detection relies on three main inputs:

- Magiclib: A file's header unique to its type. For example, PDF files begin with a distinctive header (%PDF-1.5, %µµµµ, etc.), serving as a strong file type indicator.
- HTTP Headers: The "Content-Type" header in file uploads can hint at the file type, such as application/vnd.ms-excel for Excel files during an upload.
- File Name Extension: Used when other indicators are absent or inconclusive, assuming the file name is correctly extracted.

Limitations arise with textual files because:

- They lack a unique magic header to distinguish types (CSV, TXT, Python script).
- HTTP requests for uploads (e.g., via curl) may not have sufficient metadata on the type of the file (e.g. "Content-Type" header).
- The file name might not be present in the HTTP request.
  - In case the file name is absent from the events, please [Contact Support](/v1/docs/cato-support-communication-methods-and-contact-information)

These factors can make it challenging to differentiate between a simple text body in a POST/PUT request and an actual textual file upload, potentially causing DLP to miss these files.

For other **known limitations** for DLP, refer to [Creating the Data Control Policy](/v1/docs/creating-the-data-control-policy).

### (5) DLP Profile Matches The Scanned Content

- This step helps pinpoint whether the issue stems from the data type's alignment with the file's content
- DLP Validator Tool: Validating Data Types with a Test File is an essential and helpful step in the troubleshooting process. It provides a hands-on way to validate DLP rules against real-world data, serving as an effective method for identifying and rectifying issues.
  - An example of successfully validating a keyword Data Type on a .csv file: ![scan-work.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16920067462045.png)
  - **Validating Regular Expressions**: When using custom Data Type with regex, the regex tester box becomes an invaluable asset. It allows you to test your regex patterns and validate their accuracy. It's always advisable to test your patterns here first to avoid unwanted results in the DLP system. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16920048268573.png)
  - The "**Export Extracted Text**" Option can be useful for examining the parsed textual data of the file as was scanned by the DLP engine: ![export-text-show.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16920048275997.png)
  - For example, verifying sensitivity labels IDs attached to a document are detected can be done by reviewing the .txt file generated by the "Export Extracted Text" option. Below is the textual result of parsing a .docx containing an MIP label: mip-example.png ![mip-example.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16920067493917.png)
