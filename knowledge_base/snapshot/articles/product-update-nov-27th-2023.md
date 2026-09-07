---
title: "Product Update - Nov. 27th, 2023"
slug: "product-update-nov-27th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-nov-27th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Nov. 27th, 2023

## New Features & Enhancements

- **Automatically Upload Events to an Azure Storage Account:** [Integrate an Azure storage](/v1/docs/integrating-cato-events-with-azure-storage-account) account with Cato to automatically push events to your Azure storage account.
  - You can choose to filter to only push specific event types, or sub-types
- **AI-Powered Summaries for XDR Stories:**The new [AI Summary](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench) feature for XDR stories uses an AI model that takes the pieces of the story and creates a natural language description with rich context. This helps the IT team understand the incident and take appropriate action.
  - The natural language description is generated only on-demand
  - All sensitive data in the story is tokenized before it’s sent to the generative AI service
  - Available for XDR Core, XDR Pro, and MDR customers
- **New Networking Best Practices Checks:** The [Best Practices](/v1/docs/reviewing-posture-checks-for-your-account) page shows the evaluation of the settings in your account, and how they comply with Cato’s recommendations for optimal performance and security. We added checks for Network Rules and account level networking configurations, to verify that your settings are optimized for Network resiliency.
  - Site-level networking checks will be added in the future
- **DLP Engine Scans All Content for Specific App Activities:** We enhanced the DLP engine with the capability to scan for sensitive data within app activities regardless of size and format, including fileless formats. For example, you can create a rule that scans short messages sent through your corporate email, or in social media such as Slack or X (Twitter) posts.
  - The engine extracts content in activities both within files and in fileless formats
  - The enhanced scans are supported for [specific apps and activities](/v1/docs/what-is-the-cato-dlp-service)
  - Previously, scans were supported for files of at least 1 KB
- **Improved Category Reporting on Block/Prompt Pages:** The [Block/Prompt redirect pages](/v1/docs/customizing-the-warning-block-page-branding) for security policies report the categories that the traffic matches. Previously it was possible that only some of the matching categories were shown. This improvement ensures that all matched categories appear on the Block/Prompt page.
- **Resolved Issue with Visibility for Socket Port Connectivity Status:** The ports in the Socket page are again outlined in green when they are connected. This makes it easy to distinguish from disabled ports which are outlined in grey.
  - Connected ports previously were outlined in black

## PoP Announcements

- On Sunday, Nov. 26th we are making the following changes to the Beijing, CN PoP location:
  - Adding 123.58.120.0/26 as a new IP range
  - Permanently removing the IP range 111.206.238.128/26
- **Milan, Italy:** A new range (216.252.177.0/24) is now available in the Milan, IT PoP location

## Security Updates

- **IPS Signatures:** View more details about the IPS Signatures and Protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - Malware Agent Tesla Exfiltration via SMTP (New)
  - Malware JsOutProx RAT (New)
  - Malware GootLoader (New)
  - Malware Stealc Checkin (New)
  - Ransomware 8Base (Enhancement)
  - Phishing generic heuristic based on specific domains (New)
  - Phishing heuristic | OWA (New)
  - CVE-2023-41763 (New)
  - CVE-2023-40044 (New)
  - CVE-2023-35042 (New)
  - CVE-2022-39986 (New)
  - CVE-2021-1435 (New)
  - CVE-2023-4966 (Enhancement)
  - CVE-2023-38148 (Enhancement)
  - CVE-2023-20198 (Enhancement)
- **Detection and Response:** These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
  - Threat Prevention IOA signatures:
    - Suspicious DNS Traffic
    - Exploitation Attempt
- **Apps Catalog:** Added dozens of new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), and enhanced these applications:
  - AnyDesk
  - DHCP
  - Gigya, Inc.
  - Tiktok
- **Application Control (CASB):**
  - New granular actions for the following apps:
    - Atlassian download
    - Confluence share
    - Zendesk upload
- **File Identification:**
  - Added more than 100 new file type identifications
  - Enhanced file identification in Cato Cloud services for the following file types:
    - Archives
    - Binaries
    - Executables

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
