---
title: "Using AD Query for User Awareness"
slug: "using-ad-query-for-user-awareness"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/using-ad-query-for-user-awareness"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using AD Query for User Awareness

This article provides an overview of how to enable User Awareness with AD query.

## Overview

User Awareness lets you easily identify the end-users in your network. In addition, use the Analytics features to show traffic and events according to the AD first and last name, host name and IP address.

For more information about how to provision users with LDAP, see [Provisioning Users with LDAP](/v1/docs/implementing-ldap-user-provisioning).

Changes that are made in the AD, are with automatically synced with the Cato Management Application (at 12:00 am UTC daily), or on demand by the administrator.

## High Level Overview of Integrating AD and the Cato Management Application

This section describes the end-to-end workflow to configure the Windows server to allow the PoPs to integrate for User Awareness with AD query.

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
2. Configure the Directory Service settings in the Cato Management Application. See [Provisioning Users with LDAP](/v1/docs/implementing-ldap-user-provisioning).
  1. Add the AD domain to the Directory Services for the account.
  2. Add the Domain Controllers.
  3. Define the AD groups that are synchronized, and the sync settings.
3. Configure the User Awareness settings in the Cato Management Application. See the [User Awareness](/v1/docs/user-awareness) articles .
  - User Awareness with an AD server:
    1. Add the AD domain to User Awareness.
    2. Add the Real Time Sync Domain Controllers.
    3. Define the AD groups that are participating in User Awareness.
  - User Awareness with the Cato Identity Agent:
    1. Enable [User Awareness Identity Agent](/v1/docs/using-cato-identity-agents-for-user-awareness) for your account.
    2. Install the Cato Client on the devices where you're identifying the users.

## Providing Users With Limited Access

To collect EventLog information for User Awareness using WMI, you can provide a user with limited access in your Active Directory and then add this user to Real Time Domain controllers.

### Step 1: Providing Limited Access to a User

In you Active Directory create a user with limited access.

**To provide limited access to a user:**

1. In your Active Directory, add the user to these groups:
  - Distributed COM Users
  - Event Log Readers
  - Server Operators

In Windows 2003, the service account must be given the “Audit and manage security log” user right through a group policy.
2. In the Command Prompt, run the following command to open the WMI console:

`wmimgmt.msc`
3. Right click on **WMI Control (Local)** and select **Properties**.

The **WMI Control (Local) Properties** dialog box opens.
4. On the **Security** tab, select the **CIMV2** folder and click **Security**.

The **Security for Root\CIMV2** dialog box opens.
5. Click **Add** and select the user that you are providing limited access to.
6. Check the Allow check box for **Enable Account** and **Remote Enable**.
7. Click **Apply** then **OK**.
8. Repeat steps 2-7 for every Domain Controller used as a Real Time Domain Controller.

### Step 2: Add the User as a Real Time Domain Controller

Add the user to the Real Time Domain Controllers. For more information, see [Adding User Awareness to Directory Services](/v1/docs/adding-user-awareness-to-directory-services).

## Email Notifications and Events for Directory Services and User Awareness

There are specific email notifications and events for Directory Services and User Awareness.

### Working with Alerts

You can configure the Cato Management Application to send email notifications for Directory Service sync actions and connectivity status with the DC:

- Syncing with the AD - success, failure, manual, or automatic
- Connectivity failure with the DC - there is a connectivity issue between the Cato Management Application and the DC, and most likely impacts User Awareness

For more about configuring alerts, see [Account Level Alerts and System Notifications](/v1/docs/account-level-alerts-and-system-notifications).

### Analyzing Events

The **Event Discovery** window shows all the Directory Services and User Awareness events for your account. You can learn more about using Event Discovery [here](/v1/docs/analyzing-events-in-your-network).
