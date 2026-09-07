---
title: "Product Update - December 12th, 2022"
slug: "product-update-december-12th-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-december-12th-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - December 12th, 2022

## New Features & Enhancements

- **New Device Checks Provide More Security for Windows Devices:** In the next few weeks, we are enhancing Device Checks and Profiles for the Windows Clients (Access > Device Posture). The new checks let you define stricter device requirements in the Client Connectivity and Firewall policies. For example, only allow devices with disk encryption and a specific certificate installed. [Read more](/v1/docs/creating-device-posture-profiles-and-device-checks).
  - Patch Management - For organizations with device management solutions such as Intune or JAMF, this verifies the status of the relevant software installed on the device
  - Disk Encryption - Verifies that the specified drives are encrypted on the device
  - Device Certificate - Verifies that there is a certificate installed on a device that matches a certificate defined for your account
    - For accounts that already use Device Authentication, you can use this Device Check instead and apply it only to specific items, such as User Groups, OS, and geolocation.
  - Read more about the [Client Connectivity policy](/v1/docs/configuring-the-client-connectivity-policy) and [adding Device Conditions to Firewall rules](/v1/docs/adding-device-conditions-to-firewall-rules)
- **Device Posture Includes Support for macOS Clients:** In the next few weeks, you can update Device Checks and Policies to include macOS devices in your account. This lets you define stricter device requirements for the Client Connectivity and Firewall policies. For example, only allow devices with disk encryption and a specific certificate installed. [Read more](/v1/docs/creating-device-posture-profiles-and-device-checks).
  - macOS Clients support these Device Checks: Anti-Malware, Firewall, and Patch Management
  - Read more about the [Client Connectivity policy](/v1/docs/configuring-the-client-connectivity-policy) and [adding Device Conditions to Firewall rules](/v1/docs/adding-device-conditions-to-firewall-rules)
- **Now You Can Easily Download SDP Clients:** Starting on Dec. 12, 2022, any user can go to the new Client portal and download the Cato Client, without requiring authentication to access it.
  - You will be able to download the Clients here: [https://clientdownload.catonetworks.com/](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcatonetworks.us16.list-manage.com%2Ftrack%2Fclick%3Fu%3D75bb2b7bafe7526c787475fd2%26id%3D9471617572%26e%3D2b9a2985a2&amp;data=05%7C01%7Cjonathan.rabinowitz%40catonetworks.com%7C7151793eb77f4c5d087e08dadb85ab68%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638063664395334807%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&amp;sdata=9SrU3sXt8L9BCGpzx5%2FYd3EURIOc5c32Y64yDlT%2FhJA%3D&amp;reserved=0)
- **Improved Onboarding for SDP Users (with SSO):** Over the next few weeks, for accounts that use invitation emails, after installing the Client on a device, users can immediately authenticate with SSO and connect to the Cato Cloud. There is no impact for existing SDP users.
  - The previous behavior was to use the [Cato User Portal](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcatonetworks.us16.list-manage.com%2Ftrack%2Fclick%3Fu%3D75bb2b7bafe7526c787475fd2%26id%3D74d6d4e8ef%26e%3D2b9a2985a2&amp;data=05%7C01%7Cjonathan.rabinowitz%40catonetworks.com%7C7151793eb77f4c5d087e08dadb85ab68%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638063664395334807%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&amp;sdata=xW8ss3o7gkzmsj23fyi9se4uTn%2FhCM9gT2TqHBJFtZ4%3D&amp;reserved=0) to activate the account
  - As part of this improvement, the User Portal will no longer support SSO authentication
    - There is no change for SDP users that don’t use SSO
- **Export Security Rules to CSV:** Starting on Dec. 11th, you can easily export rules from the Security policies to a readable spreadsheet format (CSV file). [Read more](/v1/docs/exporting-security-rules-to-a-csv-file). The Security policies include:
  - Internet and WAN firewall
  - TLS Inspection
  - Application Control and Data Control
- **Enhancements for IPsec IKEv2 Sites (Cato Initiated):** Cato introduces the following enhancements that improve interoperability with 3rd party devices, including Cisco ASA, and better protection against DoS attacks. No action is required for the relevant IPsec IKEv2 sites.
  - Enhanced support for working with multiple Traffic Selectors
    - If there are too many traffic selectors, and they can’t be sent on a single packet, the PoP will send the traffic selectors in multiple packets
    - PoPs can now send a single traffic selector per packet
  - Improved protection against half-open IKE SAs DoS attacks
    - Cato now supports IKEv2 cookie flows

## Cato SDP Client Releases

- **macOS Client v5.2:** macOS Client version 5.2 will soon be available in the [User Portal](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fcatonetworks.us16.list-manage.com%2Ftrack%2Fclick%3Fu%3D75bb2b7bafe7526c787475fd2%26id%3D8e86db83cb%26e%3D2b9a2985a2&amp;data=05%7C01%7Cjonathan.rabinowitz%40catonetworks.com%7C7151793eb77f4c5d087e08dadb85ab68%7Cd03fe63fee564020a121dd5b65bc7ea3%7C0%7C0%7C638063664395334807%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&amp;sdata=TnxEI9aJ2c16%2Bir1ZjyJxnZJQNQbyYt5OYDqJ1uz3aE%3D&amp;reserved=0). This version includes:
  - **Device Posture:** macOS Support for [Client Connectivity Policy](/v1/docs/configuring-the-client-connectivity-policy) and [Device Posture](/v1/docs/creating-device-posture-profiles-and-device-checks).
  - **Enhanced Reauthentication Experience:** A notification lets users know that the SSO or MFA session will soon expire, and allows them to seamlessly reauthenticate. [Read more](/v1/docs/understanding-expiring-session-for-users).
  - **Status Bar Icon:** Users can easily connect, disconnect, quit, and open the Client right from the status bar of macOS devices
  - Security fixes and enhancements
  - Resiliency enhancements

## Security Updates

- **Improved Classification for Google Translate in Proxy Mode:** The Cato Cloud now identifies Google Translate in proxy mode and it is included in the Anonymizer category. This means that for block rules using the Anonymizer category, the relevant traffic for end-users will be blocked.
- **Enhanced Classification for iOS Devices:** The Cato Cloud now more accurately identifies the iOS operating system. For example, iPhone devices that were previously classified as **UNKNOWN**, are now classified correctly as iOS. This change may impact the TLS Inspection policy, because UNKNOWN OS bypasses inspection, and iOS devices would now be inspected and require the Cato certificate.
- **IPS Signatures:**
  - Malware - SVCReady
  - Malware - Azorult Stealer
  - CVE-2022-35405
  - CVE-2022-2880
  - CVE-2022-28108
  - CVE-2022-24706
  - CVE-2022-0557
  - CVE-2021-34746
  - CVE-2017-5521
- **Application Database:**
  - Added more than 200 new SaaS applications (you can view the SaaS apps in Monitoring > Apps Catalog), including:
    - Azure Databricks
    - Azure SQL - North Europe
    - Azure Event Hubs - North Europe
    - Google Translate Website Proxy
  - Enhanced the following SaaS applications:
    - Amazon General
    - Daum
    - KakaoTalk
    - LINE
    - LINE WORKS
    - Microsoft Azure
    - NAVER
    - Rapid7
    - Skype
    - RTP service
    - RTCP service
- **Updates to Application Control Policy:**
  - Enhanced actions for this app:
    - Quora: Post
