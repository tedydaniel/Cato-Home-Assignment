---
title: "Changing your Account Name and Subdomain"
slug: "changing-your-account-name-and-subdomain"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/changing-your-account-name-and-subdomain"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Changing your Account Name and Subdomain

This article discusses how to change your account name and subdomain for the Cato Management Application (CMA).

## Overview

Your account name is the name of your instance of the CMA.

The subdomain is used as the URL for your instance of the CMA and the URL for [Browser Access](/v1/docs/browser-application-portal-overview-securing-remote-access-to-applications). If an SDP user has been provisioned in two accounts with the same email address, the subdomain is used to identify which account to connect to.

Both the account name and the subdomain can be changed after your account has been created and SDP users have been provisioned, with no impact to your security policies and with minimal impact to your SDP users.

### Sample Use Case

Company ABC recently merged with another company and rebranded to a new name. They need to update their Browser Access portal URL to reflect the new brand so that it's easy for SDP users to identify their company’s account name. The company needs to manage this change with no impact to their security posture and minimal impact to SDP users.

The company opens a ticket with the Support to change the name of their account and change the subdomain for the CMA. When the name is changed, there is no change to the company’s Security, Network, or Access configuration, and SDP users are not disconnected.

The IT department sends an email to Browser Access users informing them that the URL they use has been updated to reflect the company’s new name. They are able to log into the updated URL using their existing credentials.

## Changing Your Account Name and Subdomain

This section describes how to change your account name and subdomain and explains the impact of this change.

### Changing Your Account Name

To change your account name, contact your official Cato representative and provide the details of the new account name. The new account name must be unique and different from the current and previous CMA account names.

#### Impacts of Changing Your Account Name

After your account name has been changed, only the new account name can be used to sign into the [User Portal](/v1/docs/managing-sdp-clients-with-the-cato-user-portal).

Changes to your account name do not impact:

- Any configuration or security policy
- The connectivity of your SDP users
- Your subdomain

### Changing Your Subdomain

You can change your subdomain from the CMA.

As of September 2023, hyphens are no longer supported when changing the subdomain for your account.

**To change your subdomain:**

![Change Subdomain](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218244323101.png)

1. From the navigation menu, click **Access > Single Sign-On**.
2. In the **Cato Subdomain** section, change your subdomain.
3. Click **Save**.

#### Impacts of Changing Your Subdomain

These are the impacts of changing your Subdomain:

1. The following URLs are changed to reflect your new subdomain:
  - The URL for your instance of the CMA
  - The Browser Access Portal URL
2. If you have devices with Pre Login enabled, you must update the configuration to reflect the new subdomain. For more information, see [Using Windows Pre Login and the SDP Client](/v1/docs/using-windows-pre-login-and-the-sdp-client).

If an SDP user uses the same email to connect to more than one account, only the new subdomain can be used to connect to your account.

Changes to your subdomain do not impact:

- Any configuration or security policy
- The connectivity of your SDP users
- Your account name
