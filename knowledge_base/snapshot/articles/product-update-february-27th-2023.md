---
title: "Product Update - February 27th, 2023"
slug: "product-update-february-27th-2023"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-february-27th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - February 27th, 2023

## New Features & Enhancements

- **RBAC Now Available to All Accounts:** Cato’s new [Role Based Access Control (RBAC) feature](/v1/docs/managing-admin-roles-using-rbac) increases security for Cato Management Application admins, and lets you use admin roles to restrict permissions for specific screens.
  - Cato resellers can also use [predefined or custom admin roles](https://support.catonetworks.com/hc/en-us/articles/9087001774365) to manage admin access for the reseller and managed accounts.
- **Full Visibility for SDP User Connectivity Status and Settings:** Over the next few weeks we are gradually releasing the updated **Users** screen (Access > Users), which now features two tabs for enhanced SDP user management:
  - The new **User Activity** tab shows a variety of information regarding SDP Users and their Clients. You can sort and filter for each of the fields to quickly show the relevant data, for example: Connected user, Device OS, Client version, and more
  - The new **User Directory** tab helps you manage all users for your account. You can sort and filter for each of the fields to quickly show the relevant data, for example: Status, Source (SCIM, LDAP, or Manual), Authentication (SSO or MFA), and more
- **Improved Onboarding for SDP Users:** SDP users can activate their individual account by authenticating with SSO, and no need for additional clicks from the invitation email. In addition we are introducing a new [welcome email](/v1/docs/activating-users-with-a-registration-code) that links to the [Client portal](https://clientdownload.catonetworks.com/), where anyone can download the Client.
- **Cato Management Application Enhancements:**
  - **Known Hosts Screen Shows All Hosts by Default:** We updated the Known Hosts screen so that the default view shows all the hosts in the account instead of only the ones for the DHCP ranges.
  - **Navigation Menu Enhancement:** [Digital Certificate](/v1/docs/downloading-cato-digital-certificates) is now located in the **Security** menu (previously it was located under **Administration**)
- **Allowed Domains for Browser Access** - Over the next few weeks we are gradually releasing the ability to add **Allowed Domains** to the **Browser Access** screen. This lets you use generic domains for third party users using Browser Access. For example, allow the domain **gmail.com** to provide access to third-party contractors.
- **Introducing Weekly Product Updates:** As Cato continues to release new capabilities at a fast pace, we are now sending Product Updates every week to announce enhancements and changes.

## Cato SDP Client Releases

- **iOS Client v5.1:** The iOS SDP Client version 5.1 is now available to download from the App Store. This version includes:
  - Fixed bug where the Client didn’t reconnect to the network after the iOS device was activated from sleep mode
