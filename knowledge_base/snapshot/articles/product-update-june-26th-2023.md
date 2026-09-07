---
title: "Product Update - June 26th, 2023"
slug: "product-update-june-26th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-june-26th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - June 26th, 2023

## New Features & Enhancements

- **Block/Prompt Page Supports Dynamic Localization**: For better user experience, the content in the [Block/Prompt page](/v1/docs/customizing-the-warning-block-page-branding) can now inform users in different languages. Select the required languages, and the default message is automatically translated. You can also customize the text in the target language.
  - Each page supports multiple languages and is displayed according to the browser’s default language
  - Supported languages include Chinese, French, German, Italian, Japanese, Korean, and Spanish. We will support additional languages in the future
- **New Related Apps Field for Firewall Events:** We added the new **Related Apps** field to give more information and data about application identification in the traffic flow. This helps you better understand how to define granular rules for specific apps and application sub-services.
- **User Portal Authentication Update:** From July 2nd, 2023, SDP users that authenticate with SSO are no longer required to use the [User Portal](https://myvpn.catonetworks.com/login) to activate their account.
  - The User Portal will no longer support SSO authentication
  - After installing the Client on a device, SDP users can immediately authenticate with SSO and connect to the Cato Cloud
  - SDP users that authenticate with MFA and/or Username and password continue to use the User Portal to activate their account
- **Postponing scope Field for accountMetrics API:** We are postponing the optional **scope** field that was announced on June 19th, 2023.
  - The **scope** field is no longer available in the accountMetrics API
  - The ability to specifically query sites or SDP users will be implemented at a future date
- **Cato Management Application Enhancements:**
  - **New Visibility Widgets for Sites Screen:** We added new widgets to the **Network > Sites** screen that clearly show the following site information:
    - Connectivity status
    - Connection types
    - Socket versions

## Security Updates

- **Application Database:**
  - Added more than 100 new SaaS applications (you can view the SaaS apps in the [Apps Catalog](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcatonetworks.us16.list-manage.com%2Ftrack%2Fclick%3Fu%3D75bb2b7bafe7526c787475fd2%26id%3Dc601070561%26e%3Dfd0756a33e&amp;data=05%7C01%7Cmichael.goldberg%40catonetworks.com%7Cb2c8893f2ae54d79f8d208db5f9116a6%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638208848981959553%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&amp;sdata=QHxiARr7T1cVm10yeGEcHnLCmYVwzKNtWLTUc0FCPbQ%3D&amp;reserved=0))
  - Enhanced these SaaS applications:
    - Tencent
    - Elicit AI
    - Poe AI
    - Agent GPT Reworkd AI
    - JRMI
    - ExpressVPN
    - Skype and MS Teams
    - RingCentral
- **IPS Signatures:**
  - Ransomware Moneybird (New)
  - Ransomware Pysa (New)
  - CVE-2022-24632
  - CVE-2022-24630
  - CVE-2022-24218
  - CVE-2023-34362 (Enhancement)
- **Suspicious Activity Monitoring:**
  - Binary download from low-popularity file sharing (New)
  - Bot downloading file from low-popularity file sharing (New)
  - Microsoft BITS download PE file (New)
  - Wget download PE file (New)
  - curl download binary (Enhancement)
  - Microsoft BITS download binary (Enhancement)
- **Application Control Policy (CASB):**
  - New granular actions for the following apps:
    - OpenAI: Login
    - WhatsApp: Download
    - Yahoo: Login
    - Gmail: Send mail
- **Data Loss Prevention (DLP):**
  - **Enhancement for Gmail**: The DLP engine now scans the email subject in addition to the message body and attachments

## Knowledge Base Updates

[Configuring the Connection SLA Settings](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites)
