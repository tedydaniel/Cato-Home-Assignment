---
title: "Changing the Email Address or User Principal Name of Users"
slug: "changing-the-email-address-or-user-principal-name-of-users"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/changing-the-email-address-or-user-principal-name-of-users"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Changing the Email Address or User Principal Name of Users

Email addresses or User Principal Names (UPN) of SDP Users that are updated in your SCIM or LDAP provider are reflected in your Cato account.

## Overview

For users that are provisioned to your Cato account using a SCIM or LDAP IdP, changing an email address or UPN in the provider automatically updates that information in the Cato Management Application.

Changes in a SCIM provider sync with your Cato account automatically in near real time. LDAP providers sync with your Cato account automatically once every 24 hours. For a more frequent sync, you can choose to manually sync your LDAP provider with your Cato account. For more information, see [Provisioning Users with LDAP.](/v1/docs/syncing-users-with-ldap)

After an email or UPN is changed, SDP users remain authenticated and connected to the Cato Cloud.

## Updating the Details of Existing SDP Users

This section describes how to change the email address or UPN of existing SDP users in your account.

### Changing the Email Address or UPN in the SCIM or LDAP Provider

In your LDAP or SCIM provider, update the email address or UPN of the user. The update is automatically reflected in your account after the next sync between your LDAP or SCIM provider and the Cato Management Application.

#### Limiting Email Updates for LDAP

For accounts that use LDAP for Directory Services, you can choose to limit the number of emails that are updated for each sync. After the limit is exceeded, no more emails are updated during that sync. The emails that are updated in a sync are chosen at random. For example, if the number is set to 100, and 125 email addresses were updated in the LDAP provider. Then the sync completes and updates 100 email addresses.

The default setting is to not update any emails during LDAP sync, the limit is set to 0 users. If you uncheck the **Update user emails, up to** check box, no limits to the number of updated emails are applied.

![updateEmail.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218223115421.png)

**To configure the number of emails that are updated per LDAP sync:**

1. From the navigation menu, click **Access > Directory Services**, and select the **LDAP** tab or section.
2. Edit the **LDAP Provider**.

The **Edit Directory Service** panel opens.
3. In the **General** tab under the **SDP User Sync Settings** section, enter the maximum number of user emails to be updated per sync.
4. Click **Save and Close**.

## Known Limitations

- You can't change the email address of SDP users manually added to your Cato account
- If you delete and re-add a SDP user from Windows Client version 4.7 or below, they are required to create a new password
