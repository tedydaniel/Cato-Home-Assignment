---
title: "Using the Default Recommended CASB/DLP Policy"
slug: "using-the-default-recommended-casb-dlp-policy"
tags: ["Best Practices", "CASB", "Internet Security"]
updated: 2026-06-22T09:26:50Z
published: 2026-06-22T09:26:50Z
canonical: "knowledge.catonetworks.com/using-the-default-recommended-casb-dlp-policy"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Default Recommended CASB/DLP Policy

This article explains the default Cato recommended rules for the Application Control CASB and DLP policy.

For accounts that only have the CASB license, the Data Control (DLP) rules are not included in the Application Control policy.

![Default_AppControl_Policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28884096013981.png)

| Rule Number | Rule Name | Description | Comments |
| --- | --- | --- | --- |
| 1 | Block uploading credit card numbers | Data Control rule that blocks uploading credit card numbers based on the predefined **Credit cards** Content Profile |  |
| 2 | Microsoft - Only allow the tenant catonetworks.com | Uses the Microsoft app with the Allow action for the example tenant **catonetworks.com** | Replace the example tenant with the value for your company For example, see [Get subscription and tenant IDs in the Azure portal](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id) |
| 3 | Microsoft - Monitor logins for external Microsoft tenants (click rule to read Description) | Monitors any Microsoft logins that are not for the tenant defined in the rule above | After you replace the example tenant in the previous rule, enable this rule |
| 4 | OneDrive - Only allow the catonetworks.com tenant | Uses the OneDrive Business app with the Allow action for the example tenant **catonetworks.com** | Replace the example tenant with the value for your company For example, see [View the list of OneDrive URLs for users in your organization](https://learn.microsoft.com/en-us/sharepoint/list-onedrive-urls) |
| 5 | OneDrive - Monitor access to external OneDrive tenants (click rule to read Description) | Monitors access to the OneDrive Business app which aren't for the tenant defined in the rule above | After you replace the example tenant in the previous rule, enable this rule |
| 6 | OneDrive - Monitor personal OneDrive tenants | This rule monitors the OneDrive app, which is used for personal accounts and tenants |  |
| 7 | Gmail - Monitor Gmail attachments | Monitors adding attachments to emails using the Gmail app |  |
| 8 | Monitor online storage apps: risk higher than 3, or no ISO | Monitors apps in the Online Storage category that match one of these criteria: - Cato risk score is higher than 3 (4 or higher) - Doesn't meet ISO 27001 | For more about the Cato risk score and ISO standard compliance, see [Using the App Catalog](/v1/docs/using-the-app-catalog) |
| 9 | Twitter/X - Block posts with the string “samplekeyword” | Data Control rule that blocks Twitter/X posts or tweets that match the strings in the Sample Keyword Profile | Replace the string **samplekeyword** with the relevant keywords for your organization |
| 10 | Twitter/X - Monitor posts with long words (more than 8 characters) | Data Control rule that monitors Twitter/X posts or tweets that are longer than 8 characters | The User Defined Data Type uses REGEX to identify the long words |
| 11 | Twitter/X - Monitor all posts | Monitors Twitter/X posts or tweets (with the Post activity) |  |
| 12 | OpenAI - Restrict logins for allowed users and tenants | Uses the Open AI app (ChatGPT) with the Login action for allowed users and tenants defined in the value set | Edit the value set and define the allowed users and tenants For more information, see [Working with Categories (EA - Value Sets)](/v1/docs/working-with-categories) |
| 13 | Open AI - Monitor logins for external tenant (click rule to read Description) | Monitors any OpenAI (ChatGPT) logins that are not for the tenant defined in the rule above | After you replace the example tenant in the previous rule, enable this rule |
| 14 | OpenAI - Monitor third-party logins | Monitors the OpenAI app for third party logins |  |
| 15 | Monitor PII data uploads to Generative AI tools | Data Control rule that monitors personal data being uploaded to AI tools | For mote information, see [Recommended DLP Configuration to Monitor AI Apps](/v1/docs/recommended-dlp-configuration-to-monitor-ai-apps) |
| 16 | Monitor financial data uploads to Generative AI tools | Data Control rule that monitors financial data being uploaded to AI tools | For mote information, see [Recommended DLP Configuration to Monitor AI Apps](/v1/docs/recommended-dlp-configuration-to-monitor-ai-apps) |
| 17 | Monitor access key & token uploads to Generative AI tools | Data Control rule that monitors key & tokens being uploaded to AI tools | For mote information, see [Recommended DLP Configuration to Monitor AI Apps](/v1/docs/recommended-dlp-configuration-to-monitor-ai-apps) |
| 18 | Monitor legal data uploads to Generative AI tools | Data Control rule that monitors legal data being uploaded to AI tools | For mote information, see [Recommended DLP Configuration to Monitor AI Apps](/v1/docs/recommended-dlp-configuration-to-monitor-ai-apps) |
| 19 | Google Drive - Restrict view to allowed folders | Restricts the view activity for Google Drive to paths defined in the value set | Edit the value set and define the allowed Google Drive paths For more information, see [Working with Categories (EA - Value Sets)](/v1/docs/working-with-categories) |
| 20 | Google Drive - Monitor non-allowed folders (click rule to read Description) | Monitors the view activity for Google Drive for all paths not defined in the previous rule | After you replace the example paths in the previous rule, enable this rule |
| 21 | Test sensitivity labels - edit MIP labels before enabling | Data Control rule that lets you test uploading files that contain content defined in MIP labels | After you import the MIP labels to your account, enable this rule For more information about using MIP labels, see [Using MIP Sensitivity Labels in your Cato DLP Policy](/v1/docs/using-mip-sensitivity-labels-in-your-cato-dlp-policy) |
| 22 | Skip monitoring uploads to sanctioned apps | Data Control rule that allows uploading to the sanctioned apps without generating events | For new CASB and DLP licenses after September 2023, Cato automatically defines sanctioned apps for your account We recommend that you review these sanctioned apps and edit them to meet the requirements of your organization For more information, see [Using the Cloud Apps Dashboard](https://support.catonetworks.com/hc/en-us/articles/24373642591389#UUID-09981eb4-4ee8-8342-804d-70ff2b20f10a) |
| 23 | Non-sanctioned apps - Monitor uploads | Monitors the upload activity for Cloud applications that are not defined in the previous rule (as sanctioned apps) |  |
| 24 | Log Any Cloud Application Granular Activities | Monitors the granular activities of cloud applications |  |
