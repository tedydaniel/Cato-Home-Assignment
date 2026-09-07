---
title: "Product Update - Dec. 11th, 2023"
slug: "product-update-dec-11th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-dec-11th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Dec. 11th, 2023

## New Features & Enhancements

- **Strengthen MFA Requirements for Cato Management Application Admins:** For increased security we are adding [MFA requirements for admins](/v1/docs/authenticating-admins) using the Cato User Credential authentication method. This code is available via an Authenticator application.
  - Accounts using SSO authentication are not impacted
  - For new accounts, MFA is always enabled for admins using Cato User Credential authentication method. These admins will be required to provide an MFA code when logging into the Cato Management Application.
  - For existing accounts:
    - Existing admins using Cato User Credential authentication are not impacted
    - New admins will still be able to use Cato User Credential authentication method without MFA. However the default will be changed to MFA-enabled, and admins need to uncheck **MFA** to enable authentication without MFA.
  - For more information see [Configuring Authentication Settings for Administrators](/v1/docs/authenticating-admins#heading-3).
- **XDR Stories - Policy for Notifications:** The new Response Policy page lets you define when [email notifications for XDR stories](/v1/docs/creating-the-response-policy-for-xops-stories) are sent to admins. For example, set notifications to be sent when new stories are created, or when the verdict or target list is updated. You can also configure which admins receive the notifications.
  - For XDR Core, XDR Pro, and MDR customers.
- **XDR Stories Dashboard - Enhanced Account Risk Score:** The Stories Dashboard shows the overall Account Risk Score, which is derived from the risk levels of the detected XDR stories. We improved the formula for calculating the score to provide a more precise evaluation of your account’s risk exposure.
  - Enhancements in the new formula include:
    - Assigning greater weight to stories with recent traffic
    - A refactoring that better reflects risk level and avoids unnecessarily high risk scores
  - The enhanced Account Risk Score is available for XDR Core and XDR Pro customers
- **New Report** **Type for Users:** Over the next few weeks we are releasing the new [Users Report](/v1/docs/generating-a-user-report) that summarizes users connection activity across your account.
  - The report includes data such as:
    - Number of users connected per Country and PoP
    - The Client versions used for each operating system

## Security Updates

- **IPS Signatures:** View more details about the IPS Signatures and Protections in the [Threats Catalog](/v1/docs/using-the-threat-catalog).
  - Ransomware Elbie (New)
  - Ransomware LEAKDB (New)
  - Ransomware MuskOff[Chaos] (New)
  - Ransomware Stop/Djvu (New)
  - Ransomware Worry (New)
  - Malware Cobalt Strike (Enhancement)
  - CVE-2023-46604 (New)
  - CVE-2023-32563 (New)
  - CVE-2023-24941 (New)
  - CVE-2021-27691 (New)
  - CVE-2023-47246 (Enhancement)
  - CVE-2023-28771 (Enhancement)
  - CVE-2022-39987 (Enhancement)
- **Detection and Response:** These are the updates to the [Indications Catalog](/v1/docs/using-the-indications-catalog):
  - Threat Hunting Indication Signatures:
    - Suspicious Network Activity (New)
    - HTTP traffic to low popularity target using download utilities (New)
    - Suspicious Network Activity (MS-Office) (New)
    - Suspicious Network Activity (Telegram) (New)
- **Apps Catalog:** Added dozens of new SaaS applications (you can view the SaaS apps in the [Apps Catalog](/v1/docs/using-the-app-catalog)), and enhanced these applications:
  - AnyDesk
  - Amazon Chime
  - Canon
- **Application Control (CASB):**
  - New granular actions for the following app:
    - Facebook - Comment (Enhancement)
- **TLS Inspection:**
  - Added global bypass for these AppIDs/FQDNs, preventing possible TLS inspection errors:
    - **AppIDs**:
      - Amazon Chime
      - Anydesk
      - Canon (only on OS EMBEDDED)
      - Datadog, Inc.
      - Fortinet
      - GMO Insight
      - Kandji
      - Logitech
      - Microsoft Intune
      - Mycloud
      - Rapid7
      - Skype
      - Tenable
      - Ui
      - VMware, Inc
      - VNC Web
      - Windows Autopilot
      - Yealink
      - Zebra Technologies Corporation
      - Zscaler
    - **FQDNS**:
      - *.jabra.com
      - *.struxurewarecloud.com
      - *.update.filezilla-project.org
      - citrix.*
      - *.onmicrosoft.com (only when recognized as Office365)

## Knowledge Base Updates

- [How to use the Cato Knowledge Base (Video)](/v1/docs/how-to-use-the-cato-knowledge-base-video)
- [How to open a ticket to Cato Support (Video)](/v1/docs/how-to-open-a-ticket-to-cato-support-video)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
