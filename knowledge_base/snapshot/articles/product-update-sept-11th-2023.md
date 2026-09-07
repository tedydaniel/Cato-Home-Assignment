---
title: "Product Update - Sept. 11th, 2023"
slug: "product-update-sept-11th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-sept-11th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Sept. 11th, 2023

## New Features & Enhancements

- **Cato Now Supports Deploying Azure vSockets from the Marketplace:** We added the Cato virtual Socket (vSocket) for the Azure public cloud to the [Azure Marketplace](/v1/docs/deploying-azure-vsockets-from-the-marketplace). This enhancement significantly simplifies the deployment process of the vSocket.
- **Streamlined App Security with New CASB and DLP Pre-Defined Rules:** We're adding a comprehensive set of new CASB and DLP pre-defined rules that are designed to simplify and streamline the onboarding process, and provide a suggested rule set that ensures effective protection and adaptability of the service. With these new rules, organizations can quickly enhance their security posture, manage cloud access with precision, and safeguard sensitive data.
  - No impact for existing CASB and DLP customers
- **SaaS Security API Supports Remediation Actions for Google Drive:** You can now define actions in [Data Protection and Threat Protection](/v1/docs/google-drive-and-gmail-configuring-the-data-protection-api-connector) rules to remediate potential security breaches in your organization’s Google Drive tenant. When a rule is matched, these actions can be applied:
  - **Remove Share:** When a user tries to share a file, the SaaS Security API engine removes the unauthorized sharing permission
  - **Quarantine:** When a user tries to upload a file, the SaaS Security API engine moves it to a quarantine folder and then users can no longer access it. The admin can access the file to investigate and restore it if necessary
- **New Network Performance Dashboard:** The [Network Dashboard](/v1/docs/using-the-network-overview-page) provides comprehensive visibility for network throughput and performance. The dashboard helps you identify top sites and links for metrics such as throughput, packet loss, and more.
- **Improved Mechanism for Detecting and Alerting Link Congestion:** Over the next few weeks we are introducing a new mechanism that detects when there is [congestion for links](/v1/docs/working-with-link-health-rules) (discarded packets).
  - For existing congestion Quality Health Rules, this improvement might generate more email notifications. You can adjust the [**Tracking**](/v1/docs/working-with-link-health-rules#h_01H8Y6YMEBS914982EVQF0NF3D) settings to reduce the **Frequency** of the email notifications.

## Cato SDP Client Releases

- **EoL for Client Versions Earlier than v5.0, and EoS for Windows Version 8.1 and Earlier:** Starting from November 1st, 2023, all Client versions earlier than v5.0 will be [End of Life (EoL)](/v1/docs/important-updates-for-legacy-client-and-windows-versions) and will no longer be able to connect to the network. To continue to use the Cato Client and receive the latest features and enhancements, upgrade to the newest version.
  - This follows the end of support announcements earlier this year ([Windows and macOS](/v1/docs/eos-for-windows-and-macos-clients-earlier-than-v5-0),[Linux, IOS and Android](/v1/docs/eos-for-linux-ios-and-android-clients-earlier-than-v5-0)).
  - In addition, we are announcing [End of Support (EoS)](/v1/docs/important-updates-for-legacy-client-and-windows-versions) for all Windows Clients installed on Windows OS version 8.1 and earlier. If you have devices running these legacy Windows OS versions, upgrade to a newer supported version, and then upgrade the Cato Client.
  - For a list of supported versions, see [here](/v1/docs/preparing-to-install-the-cato-client)

## PoP Announcements

**New York, United States:** A new range (150.195.207.0/24) will be added to the New York PoP location

## Knowledge Base Updates

[Data Control Rule Doesn't Work on JAR File When Match By Source Code](/v1/docs/data-control-rule-doesn-t-work-on-jar-file-when-match-by-source-code)

> [!NOTE]
> Note:
> 
> Content described in this update is gradually rolled out to the Cato PoPs over a two-week period. In addition, new features are gradually activated in the Cato Management Application over the same two-week rollout period as the PoPs. For more information, see this [article](/v1/docs/understanding-rollout-to-the-cato-cloud-1). See the [Cato Status Page](https://status.catonetworks.com/) for more information about the planned maintenance schedule.
