---
title: "Adding Users to Your Cato Account"
slug: "adding-users-to-your-cato-account"
updated: 2026-08-16T10:06:06Z
published: 2026-08-16T10:06:06Z
canonical: "knowledge.catonetworks.com/adding-users-to-your-cato-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding Users to Your Cato Account

This article explains the options for how to add users to your Cato account so that they can securely connect to the network.

## Overview

When users are added to your account, Cato can identify them, ensure they are authenticated (for example, using SSO), and enforce policies based on their identity. You can provision users directly from your IdP using SCIM or LDAP. This ensures your IdP remains the central location for managing users and User groups. Any change to a user in your IdP is automatically synced with Cato (with SCIM provisioning, this is reflected in real time, with LDAP provisioning, this is reflected within 24 hours). You can also use the Cato Management Application (CMA) to manually add users to your account.

When new users are created in your account, you can choose to send an email to introduce them to remote access with Cato.

After a user is added to your account, they can be assigned a license and added to policies. After you add a user to a policy, it will be enforced whether the user is located behind a site or remotely.

## Provisioning Users

Cato supports provisioning users from your IdP with SCIM and LDAP as well as adding users manually.

### Provisioning Users Process Flow

This process explains how users are provisioned from your IdP, and then assigned licenses and added to policies so they can securely connect to the network.

![User_Provisioning.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218221854109.png)

1. In your IdP, define the users and/or groups to be provisioned to Cato.
2. Configure automatic user sync with Cato.

After users are synced, they can be viewed from the [**Users Directory**](/v1/docs/working-with-users) page and identified with [User Awareness](/v1/docs/using-cato-identity-agents-for-user-awareness).
3. Assign licenses to required users
4. Apply policies to users

Policies are enforced wherever the user connects.

### Provisioning Users with SCIM

These are the IdPs that are supported for provisioning users with SCIM:

- Azure
- Okta
- One Login

For more information on how to configure SCIM provisioning for each IdP, see [Provisioning Users with SCIM](/v1/docs/scim-user-provisioning).

### Provisioning Users with LDAP

These are the IdPs that are supported for provisioning users with LDAP:

- Azure
- Okta
- One Login
- Jump Cloud

For more information on how to configure LDAP provisioning for each IdP, see [Provisioning Users with LDAP](/v1/docs/ldap-user-provisioning).

## Manually Creating User

Users can also be created manually by entering their name and email address. For more information about creating users manually, see [Working with Users](/v1/docs/working-with-users).

## Sending Onboarding Emails

When a user is added to your account, you can configure them to receive an email to introduce them to Cato. By default, users are not sent an onboarding email. You can choose to send these onboarding emails:

- **Onboarding email:**
  - Welcome email - Emails automatically sent to users when they are created with a link to download the Cato Client. This is sent when a user is created in the CMA.
  - Disabled users - An email to notify the user that their account is disabled. This is sent when a user is disabled in the CMA.
- **Registration code:** Users enter a one-time code to activate their account. For more information, see [Activating Users with a Registration Code](/v1/docs/activating-users-with-a-registration-code).

You can choose to send users an email containing details of the account and a link to download the Cato Client from the [Client download portal](https://clientdownload.catonetworks.com/).

![UserProv-InviteEmail.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218208993437.png)

**To configure settings for the onboarding email:**

1. From the navigation menu, click **Access > Directory Services**.
2. Click the **User Provisioning** tab.
3. Set the **Method** to **Onboarding Email**.
4. To send emails with links to download the Client, select **Send welcome email to new SDP users**.
5. To let users know that their remote access is disabled, select **Send email notifications to SDP users that are disabled in the account**.
6. Click **Save**.

### Manually Resending an Activation Email

Users who authenticate with Username and Password (and MFA) are sent an email to create their password when they [sign in](/v1/docs/signing-in-to-the-cato-client) to the Client. You can choose to resend this email to individual users. You can only send activation emails to users with a [remote user license](/v1/docs/assigning-ztna-licenses-to-users).

**Note:** Users on headless Linux devices must be sent an Activation email to sign in to the Client.

![Activation_email.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218192846877.png)

**To resend an activation email:**

1. From the navigation menu, click **Access > Users**.
2. On the **Users Directory** tab, select the user to send the Activation email to.
3. From the **Actions** drop-down menu, select **Resend activation email**.
