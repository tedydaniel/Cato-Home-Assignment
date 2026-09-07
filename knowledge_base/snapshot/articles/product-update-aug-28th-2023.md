---
title: "Product Update - Aug. 28th, 2023"
slug: "product-update-aug-28th-2023"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/product-update-aug-28th-2023"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - Aug. 28th, 2023

## New Features & Enhancements

- **New Single User Identity to Simplify Policy Enforcement and User Management:** Over the next few weeks, we are unifying users into a [single user identity](/v1/docs/understanding-the-single-user-identity) to enhance policy enforcement and user management.
  - Policies will be enforced whether users are located behind a site or remotely
    - Cato will automatically update all your users to the new single user identity
    - Policies that were enforced for either a User Awareness user or a SDP user, will now be enforced for the new single user identity
  - All users will now be visible from the Users Directory page, providing a single location to manage and view all your users
- **User Awareness Supports Manually Created Users:** If you are using the single user identity (see above), you can identify manually created users behind a site using the Cato Identity Agent.
  - Users are required to have an SDP license and authenticate once
- **SDP User Authentication is No Longer Required Behind a Site:** To simplify the user experience for SDP users behind a site, the Windows Client can connect automatically in Office Mode without SDP users manually authenticating. There is no impact on Security and User Awareness policies.
  - Supported on Windows Client v5.8 and higher
  - This replaces the previous behavior where, behind a site, authentication was required but had no impact on Security or Access policies
  - Over the next few weeks, for [SDP users with Always-On enabled](/v1/docs/protecting-users-with-always-on-security), you can choose to configure them to authenticate even when in Office Mode
- **Stories Workbench Enhancement - New Options for Grouping Stories:** We added more grouping options in the [Stories Workbench](/v1/docs/reviewing-detection-response-xops-stories-in-the-stories-workbench). You can now show the stories grouped by investigation **Status** and engine **Type**. For example, you can show all the open investigations together.
- **Indications Catalog Now Shows Which Indications Apply for Your Account:** We added information to the [Indications Catalog](/v1/docs/using-the-indications-catalog) to show which indications are supported for the account, based on your license.
  - The catalog also shows your current Detection & Response license
- **SaaS Security API Supports Remediation Action for Box:** [Box Data Protection and Threat Protection](/v1/docs/box-configuring-the-data-protection-api-connector) rules support remediating potential security breaches in your organization’s Box tenant. When a rule is matched, the following action can be applied:
  - **Remove Share:** When a user tries to share a file, the SaaS Security API engine removes the unauthorized sharing permission

## Knowledge Base Updates

- [SDP Users not being added to expected LDAP groups](https://support.catonetworks.com/hc/en-us/articles/13067479713821)
