---
title: "Overview of Directory Services and User Awareness"
slug: "overview-of-directory-services-and-user-awareness"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/overview-of-directory-services-and-user-awareness"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview of Directory Services and User Awareness

This article provides an overview of using Directory Services to integrate your LDAP service (such as Active Directory) with your Cato account. It also discusses how User Awareness can help to identify users according to their LDAP settings (such as first and last name).

## Using Directory Services and User Awareness with the Cato Cloud

Cato Networks lets you integrate Active Directory (AD) with your account to make it easier to manage SDP users in your account.

- The Directory Services feature helps to onboard and manage SDP users. Select the AD user groups that are synchronized with your account in the Cato Management Application.
- User Awareness lets you easily identify the end-users in your network. In addition, use the Analytics features to show traffic and events according to the AD first and last name, host name and IP address.

Changes that are made in the AD are automatically synced with the Cato Management Application (at 12:00 am UTC daily), or on demand by the administrator.

For accounts that enable User Awareness, first you must configure Directory Services.

## High Level Overview of Integrating AD and the Cato Management Application

This section describes the end-to-end workflow to configure the Windows server to allow the PoPs to integrate for Directory Services and User Awareness. The steps to configure the WMI settings in section 1c are only for User Awareness. For accounts that are configuring only Directory Services, do not perform the steps in section 1c.

1. Prepare the Windows Server for Cato Directory Services and User Awareness. See [Configuring the Windows Server for Directory Services](/v1/docs/configuring-the-windows-server-for-directory-services).
  1. Create a dedicated AD user that belongs to Distributed COM Users and Event Log Readers groups. The PoPs use this user to connect to the AD server.
  2. Configure these Windows settings for Directory Services:
    - Windows services
    - DCOM settings
    - COM security permissions
  3. (**For User Awareness**) Configure the WMI settings to allow the PoPs to query the user login events:
    1. Configure the server to allow remote connections using WMI. (See the Microsoft documentation, [Securing a Remote WMI Connection](https://docs.microsoft.com/en-us/windows/win32/wmisdk/securing-a-remote-wmi-connection)).
    2. Configure the WMI user access settings.
    3. Configure the WMI Controller registry permissions.
    4. Configure the Windows firewall to allow DCOM communications.
2. Configure the Directory Service settings in the Cato Management Application. See [Implementing LDAP User Provisioning](/v1/docs/implementing-ldap-user-provisioning) .
  1. Add the AD domain to the Directory Services for the account.
  2. Add the Domain Controllers.
  3. Define the AD groups that are synchronized, and the sync settings.
3. Configure the User Awareness settings in the Cato Management Application. See the [User Awareness](/v1/docs/user-awareness) articles.
  - User Awareness with an AD server:
    1. Add the AD domain to User Awareness.
    2. Add the Real Time Sync Domain Controllers.
    3. Define the AD groups that are participating in User Awareness.
  - User Awareness with the Cato Identity Agent:
    1. Enable User Awareness Identity Agent for your account.
    2. Install the Cato Client on the devices where you're identifying the users.

## Email Notifications and Events for Directory Services and User Awareness

There are specific email notifications and events for Directory Services and User Awareness.

### Working with Alerts

You can configure the Cato Management Application to send email notifications for Directory Service sync actions and connectivity status with the DC:

- Syncing with the AD - success, failure, manual, or automatic
- Connectivity failure with the DC - there is a connectivity issue between the Cato Management Application and the DC, and most likely impacts User Awareness

For more about configuring alerts, see [Account Level Alerts and System Notifications](/v1/docs/account-level-alerts-and-system-notifications).

### Analyzing Events

The **Event** page shows all the Directory Services and User Awareness events for your account. You can learn more about using Cato events [here](/v1/docs/analyzing-events-in-your-network).

**Note:** If a user does not appear in the CMA as provisioned, they will appear as **Unmapped user** in generated events. For more information about unmapped users, see [this troubleshooting article](/v1/docs/user-not-mapped-by-wmi-based-user-awareness).
