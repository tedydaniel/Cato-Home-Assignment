---
title: "Adding User Awareness to Directory Services"
slug: "adding-user-awareness-to-directory-services"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/adding-user-awareness-to-directory-services"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding User Awareness to Directory Services

This article explains how to configure User Awareness to provide better visibility for AD users on internal networks.

## Overview of User Awareness

The Cato Management Application lets you easily identify remote users that are connected to your corporate network because the user authenticated to the Cato Client. However, for users that are behind a site, they aren't connecting with a Client and you can only see the IP address or the computer name. It is difficult to use analytics for these internal without personal information such as first and last name. The User Awareness feature integrates with Active Directory (AD) to correlate the IP address and username. The PoPs can query the DC login logs and map users to the IP address for their computers. The user data is almost in real-time with just a 30 second delay. User Awareness lets the Topology window and analytics show the names for internal users and not just the IP address.

## Preparing to Configure User Awareness

You must configure Directory Services for the domain before you can enable User Awareness. For more about configuring Directory Services, see [Provisioning Users with LDAP](/v1/docs/provisioning-users-with-scim-and-ldap).

Make sure that the audit policy is configured with the Event IDs that User Awareness uses in the Windows security log in order to map users to IP addresses. For more information, see [Troubleshooting Directory Services and User Awareness Errors and Issues](/v1/docs/directory-services-and-user-awareness-errors-troubleshooting).

The following sections explain how to configure User Awareness for IPsec sites that are behind a third party firewall. If you don't have an IPsec site, continue below with [Defining Real Time Domain Controllers](/v1/docs/adding-user-awareness-to-directory-services#defining-real-time-domain-controllers).

### Configuring a Third Party Firewall for User Awareness Sync

User Awareness synchronization uses a fixed IP address for the System Range. Customers that use third party firewall to control access to their DCs, must update the firewall settings to allow this IP address for all ports and services. The IP address that is used for User Awareness sync is different for accounts that use the default system range, or a custom system range.

For more about default and custom ranges for DNS servers in the Cato Cloud see: [Handling DNS Flows in the Cato Cloud](/v1/docs/example-dns-flows-using-cato-as-your-dns-server).

#### Accounts that Use the Default System Range

The default system range that is reserved for Cato Networks is 10.254.254.0/24. For accounts that use this default range, the fixed IP address for User Awareness sync is: **10.254.254.12**.

#### Accounts that Use a Custom System Range

For accounts that use a custom system range instead of the default one, use the custom range to calculate the fixed IP address for User Awareness sync based. The fixed IP address is the 9th in the custom range. For example, if the custom reserved range is 10.10.10.0/16, then the fixed IP address is 10.10.10.9.

For accounts that use a smaller IP range, they still use the 9th in the custom range. For example, if the custom reserved range is 10.200.200.64/28, then the fixed IP address is 10.200.200.73 (10.200.200.64 + x.x.x.9).

## User Awareness with a Shared Host

User Awareness detects at least 4 different users signing into the same device in a time frame of 2 hours, the device is considered a shared host. Firewall and network rules for the **All Shared Hosts** user group or the host IP address apply to the SDP users logged into the shared host, not the rule for the SDP user.

## Defining Real Time Domain Controllers

Define the WMI controllers on the Domain Controller (DC) that monitor WMI queries in real-time.

For ADs that are behind a site, make sure that you define the Domain Controller (DC) as a host for that site (**Networks > Site Settings > Host**).

> [!NOTE]
> Note:
> 
> For accounts with multiple DCs, you must add all the DCs that login events to the **Real Time Domain Controllers**.

**To define Real Time Domain Controllers:**

1. From the navigation menu, click **Access > User Awareness**.
2. In the **Real Time Domain Controllers** section or tab, click **New**.

The **Add Real Time Domain Controller** panel opens.
3. From the **Domain Controller** drop-down menu, select the AD domain.
4. Define the connection settings to the DC depending on its location:

> [!NOTE]
> Note:
> 
> You must use a public IP addresses for the DC.
  - For DCs on a host defined behind a site, select **Internal Host**, and then select the static host for the LDAP server
  - For DCs that aren't behind a site, select **External IP or Domain**, and enter the IP address or domain for the DC
5. Enter the **Username** and **Password** for the AD user.
6. Click **OK**. The Real Time Domain Controller is added to User Awareness settings and pushed to the Cato Cloud.
7. Repeat the previous steps for each Domain Controller.

### Testing the Domain Controller Connection Status

After you define a Real Time Domain Controller, test the connection status to make sure that the Cato Management Application and the Cato Cloud can connect to the DC.

A pop-up window shows if the connection was successful, or if Cato Cloud failed to connect to the DC.

> [!NOTE]
> Note:
> 
> You can only test the DC connection status for a DC that is a predefined host behind a site.

**To test the Real Time Domain Controller connection status:**

1. From the navigation menu, click **Access > User Awareness**.
2. In the **Real Time Domain Controllers** tab, from the **Connection** column for the domain, click **Test connection**.

The pop-up window shows the results of the connection test.

## Synchronizing the Domain for User Awareness

Define which AD groups for the domain are synchronized to your Cato account for User Awareness. You can also choose whether to automatically sync the AD every day, or only manually perform the sync. The synchronization settings for User Awareness must be the same for all the domains in your account.

When AD groups or users are removed from the domain, they are disabled in your account unless they are used in rules or groups. For more about synchronization setting for Directory Services see [Provisioning Users with SCIM and LDAP](/v1/docs/provisioning-users-with-scim-and-ldap).

### Defining the Active Directory Groups for User Awareness

Select the AD groups in the domain that contain the users which are synchronized for User Awareness, and define the daily sync settings for them.

The users are only synced to your Cato account if a Real-Time Domain Controller is configured, or Identity Agent is enabled (Access > User Awareness > Identity Agent).

The `sAMAaccountName` attribute is used for the name of the User Group in the Cato Management Application.

**To define the AD groups that are synchronized with User Awareness:**

1. From the navigation menu, click **Access > Directory Services**.
2. Select the LDAP tab or section, and click the domain.

The panel opens.
3. From the panel navigation menu, select **User Groups**.

Nested groups are synced if you select the parent group

![UA_AddGroups.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218247699101.png)
4. Select the AD groups for User Awareness.

**Note:** If no groups are selected, then all the AD groups are imported for User Awareness.
5. To automatically sync the User Awareness groups, enable ![enable.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218216818845.png)**Daily sync User Awareness Groups**.
6. Click **Apply**.

## Deleting Real Time Domain Controllers

**To delete a Real Time Domain Controllers:**

1. From the navigation menu, click **Access > User Awareness**.
2. In the **Real Time Domain Controllers** section or tab, in the row of the domain click ![Delete.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24218231761053.svg-xml).
3. Click **Save**. The Real Time Domain Controller is deleted.
