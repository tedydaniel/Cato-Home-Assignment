---
title: "Configuring Directory Services with Okta LDAP"
slug: "configuring-directory-services-with-okta-ldap"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/configuring-directory-services-with-okta-ldap"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Directory Services with Okta LDAP

## Overview

Cato Networks lets you import the LDAP users from Okta directories instead of Active Directory. It requires you integrate the Cato Directory Services with Okta.

**Note:** You can only configure one LDAP provider for Directory Services.

The following diagram shows the user provisioning flow with Okta using the LDAP interface:

![mceclip0.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33585137221405.png)

To enable the Cato Directory Services with Okta LDAP you must:

1. Add an LDAP Interface to your Okta account.
2. Configure the Directory Services in the Cato Management Application.

## Adding the Okta LDAP Interface

The LDAP Interface is a cloud proxy that LDAP commands and translates them to Okta API calls. This provides a straightforward path to authenticate legacy LDAP apps in the cloud.

**To enable the Okta LDAP Interface:**

1. Log in to your Okta account and go to Your Org.
2. In the Admin area, go to **Directory** > **Directory Integrations** and click **AddLDAP Interface**

The following screenshot shows the settings of an LDAP interface:

![Picture1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33585127999773.png)

These settings are required to complete the integration with the Cato Management Application.

## Configuring the Cato Management Application and Syncing Users

**To configure the Cato Directory Services to integrate with the Okta LDAP Interface:**

1. Go to **Access > Directory Services** and select the **LDAP** tab.
2. Click New and in the **LDAP Authentication Details** section, add the following settings:
  - Login DN: <Okta username>, <base DN of the Okta LDAP interface>. For example: **uid=user1@catonetworks.com, dc=interface,dc=okta,dc=com**
  - Base DN: the Base DN of the Okta LDAP interface. For example: **dc=interface,dc=okta,dc=com**
3. In the **Domain Controllers** section, add the following settings:

**Note**: Cato recommends that you enable SSL and use port 636 for authentication.
  - **Host** of the Okta LDAP interface. For example: **interface.ldap.okta.com**
  - **Port** from the Okta LDAP interface. If you are using SSL, use port 636 otherwise, use the StartTLS port.
4. Click **Save and Close**.

Your account is configured to import your LDAP users from Okta.
