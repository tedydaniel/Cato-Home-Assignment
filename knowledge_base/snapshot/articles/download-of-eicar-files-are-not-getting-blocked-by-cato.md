---
title: "Download of EICAR Files Are Not Getting Blocked by Cato"
slug: "download-of-eicar-files-are-not-getting-blocked-by-cato"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/download-of-eicar-files-are-not-getting-blocked-by-cato"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Download of EICAR Files Are Not Getting Blocked by Cato

## Issue

Using EICAR test files allows users to evaluate the performance and reliability of their antivirus software without the risk of infecting their systems with actual malware. These files provide a standardized method for testing antivirus software across different platforms and vendors.

Cato can effectively detect and block the download of these files. Below shows the Cato block page when an EICAR file is downloaded through Cato.

In the event that customer is able to download these files successfully through Cato, this article will walk you through on how to further isolate and narrow down on the cause of the issue.

![eicar_download_block.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10917019471389.jpeg)

## Troubleshooting

To investigate why the EICAR files are being downloaded successfully even when going through Cato, perform the following steps:

1. [Validation of Configuration](/v1/docs/download-of-eicar-files-are-not-getting-blocked-by-cato#validation-of-configuration)
2. [Browser Isolation and Cache Issue](/v1/docs/download-of-eicar-files-are-not-getting-blocked-by-cato#browser-isolation-and-cache-issue)
3. [Contact Cato Support](/v1/docs/download-of-eicar-files-are-not-getting-blocked-by-cato#cato-support)

## Validation of Configuration

Since the EICAR website is running on HTTPS, TLS inspection needs to be enabled so that Cato can examine the payload for malicious content. This examination is done by our malware engine, hence Anti-Malware needs to be enabled too.

To verify that TLS Inspection is enabled, go to Security > TLS Inspection

![tlsienabled.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10910079129117.jpeg)

To verify if Anti-Malware is enabled, go to Security > Anti-Malware. If the option is greyed-out, it means that you don't have the license for it.

![AMenabled.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/10910105634845.jpeg)

## Browser Isolation and Cache Issue

After verifying the configuration, users can attempt to download the EICAR files once more. If Cato still doesn't block the download, additional troubleshooting steps can be taken. These include trying a different browser or using incognito mode to perform the download. If the download is successfully blocked using these methods, one potential reason could be related to the browser cache. In such cases, clearing the browser cache and retrying the download is recommended.

If the download starts getting blocked after clearing the cache, it indicates that the files were previously downloaded and saved in the browser's cache. Consequently, when attempting to download them again, the browser retrieves the files from the cache rather than accessing them on the Internet.

## Cato Support

If the issue persist (aka the download of EICAR files remain successful through Cato) despite clearing the browser cache, please provide/collect the below information and contact Cato Support:

- Browser type and version
- Collect the HAR data while the file is being downloaded through Cato (refer to [Gathering-Developer-Tools-Information](/v1/docs/how-to-collect-har-data) on how to collect the HAR data)
- Open a Support case. Refer to [Submitting-a-Support-Ticket](/v1/docs/submitting-a-support-ticket) for the instruction.
