---
title: "LDAP Sync and Provisioning Troubleshooting"
slug: "ldap-sync-and-provisioning-troubleshooting"
updated: 2026-08-30T09:42:06Z
published: 2026-08-30T09:42:06Z
canonical: "knowledge.catonetworks.com/ldap-sync-and-provisioning-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# LDAP Sync and Provisioning Troubleshooting

## Overview

LDAP (Lightweight Directory Access Protocol) synchronization and user provisioning are critical components for maintaining secure and efficient access to resources. However, issues can arise that disrupt this process, leading to access problems and potential security vulnerabilities. This playbook aims to address common LDAP sync and provisioning issues in Cato and provide solutions to resolve them effectively.

## Symptoms

Failures with LDAP sync and provisioning can manifest in several ways. An administrator may note the following symptoms:

- LDAP Sync Failure
- Users fail to be provisioned to Cato
- Unexpected users are provisioned to Cato

## Possible Causes

- Routing issues back to Cato
- Invalid or missing user attributes
- LDAP error or unavailable LDAP server
- TLS connectivity error
- Asymmetric routing to the LDAP server.
- Nested Groups and users within
- Lack of available SDP licenses

## Troubleshooting the Issue

Steps to troubleshoot the symptoms an Administrator may encounter are listed below. These steps are intended to identify possible causes for the issues faced. The resolution steps will be highlighted later in the playbook.

### Troubleshooting LDAP Sync failure

Manual LDAP sync can be triggered by clicking **Sync Now** under Access > Directory Services > LDAP. Otherwise, automatic syncs will be attempted at 00:00UTC daily for the whole account, unless an account has disabled daily syncs. This section addresses the scenario where the LDAP sync fails to complete.

#### Running the Connection Test

Verify the connectivity test result directly from CMA. The test will verify TCP connectivity and LDAP binding with the Domain Controller. Common issues, such as [invalid credentials](/v1/docs/ldap-sync-and-provisioning-troubleshooting#resolving-ldap-credential-errors) and [server down](/v1/docs/ldap-sync-and-provisioning-troubleshooting#troubleshooting-connectivity-issues) can be diagnosed using this tool.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17355761575453.png)

#### Directory Services Event Analysis

A sync failure will generate an event in Cato. Filter these events by selecting **Sub-type** in **DC Connectivity Failure** and **Directory Services** as shown in the screenshot below. The **Event message** field will show the reason for the sync failure.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17301232393885.png)

#### Analyzing LDAP Errors

An LDAP error seen in the DC event when attempting to sync can imply the type of issue you are experiencing. An error showing the DC cannot be reached (error code 81, server down) suggests a connectivity error. See [Troubleshooting Connectivity Issues](/v1/docs/ldap-sync-and-provisioning-troubleshooting#troubleshooting-connectivity-issues).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17306053205021.png)

An error returning a specific LDAP error suggests connectivity can be made to the LDAP service but the sync process fails within the LDAP protocol. Specific LDAP errors can be investigated based on the error code generated. You may find [this list of LDAP errors](https://ldap.com/ldap-result-code-reference/) helpful.

The example below shows a failed sync attempt due to invalid login credentials. To solve this issue continue with [Resolving LDAP Credential Errors](/v1/docs/ldap-sync-and-provisioning-troubleshooting#resolving-ldap-credential-errors)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17301800563869.png)

#### Troubleshooting Connectivity Issues

Bi-directional connectivity is required between Cato CMA and the LDAP server for the sync to be completed successfully. Confirm the following:

1. The DC server must be able to receive traffic from the Cato LDAP IP address and have a route back to Cato to return traffic to that address. To identify the Cato LDAP IP address, see [CMA IP Allowlist](/v1/docs/cma-ip-allowlist) (you must be signed in to view this article).
2. If your Domain Controller is behind an IPsec connection or if you are routing only some subnets to the Socket, be sure to include the Cato LDAP IP address in your VPN tunnel routing configuration. To identify the Cato LDAP IP address, see [CMA IP Allowlist](/v1/docs/cma-ip-allowlist) (you must be signed in to view this article).
3. Firewall or security policies on the DC server must allow the bi-directional flow of this traffic.

For local LDAP servers behind a socket site, not only should the traffic be bi-directional, but it should also be symmetrical. An LDAP query initiated by Cato will reach the server via the socket tunnel. The return traffic must also be routed back through the socket tunnel. Failure to do this will lead to an asymmetric connection causing an unsuccessful sync.

Confirm the aliveness of the internal Domain Controller by checking the **Last Host Activity** value from the **Know Hosts** page on the site. See [Showing Known Hosts for a Site](/v1/docs/showing-known-hosts-for-a-site)

Connectivity issues can be further troubleshot by running a [PCAP capture](/v1/docs/how-to-capture-traffic-on-a-socket) on the Socket LAN connected to the DC server while running a **manual sync** from CMA. Set filter *ip.addr==Cato LDAP IP address*. Unencrypted LDAP traffic uses port TCP/389 and encrypted LDAP (LDAPS) uses port TCP/636.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17304591550109.png)

Capturing unencrypted LDAP traffic can facilitate troubleshooting the sync issue, given that LDAP responses can be seen in clear text.

To switch to unencrypted LDAP, uncheck the SSL encryption option under the Directory Services configuration.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17304579692701.png)

If LDAP syncs must be SSL encrypted, continue with [Troubleshooting TLS errors.](/v1/docs/ldap-sync-and-provisioning-troubleshooting#troubleshooting-tls-errors)

#### Troubleshooting TLS errors

When doing LDAPS, the TLS conversation could fail either by the Cato PoP or the LDAP server. An error can be identified in the packet capture, such as Fatal Alert. In the example below, the PoP closes the TCP connection after receiving the Client Hello ACK which indicates an issue with the PoP.

![mceclip0 (2).png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17304579697949.png)

Identify any TLS errors when doing LDAPS from the packet capture. To resolve these, continue with [Resolving LDAPS TLS Errors](/docs/ldap-sync-and-provisioning-troubleshooting#h_01HR5KY1EVSJCSYZWFB3FBD46Z)

### Troubleshooting User Provisioning Failure

LDAP users may fail to be provisioned to Cato for different reasons. This section explains the most common scenarios that may explain this behavior.

#### Checking the Users Directory Page

Attempt to identify the affected user on the **Users Directory** page under **Access > Users**. Identify whether:

- The user is missing from the Users Directory. If so, check for [missing user attributes](/v1/docs/ldap-sync-and-provisioning-troubleshooting#checking-for-missing-user-attributes), [user sync settings](/v1/docs/ldap-sync-and-provisioning-troubleshooting#checking-user-sync-settings), [disabled users](/v1/docs/ldap-sync-and-provisioning-troubleshooting#checking-for-disabled-ldap-users), [user query limitations](/v1/docs/ldap-sync-and-provisioning-troubleshooting#checking-for-user-query-limitation) and [duplicate users](/v1/docs/ldap-sync-and-provisioning-troubleshooting#checking-for-duplicate-users).
- The user was provisioned without an SDP License. This will result in the user not being able to connect to Cato from the Cato SDP Client. If this is the issue, check for [missing SDP licenses](/v1/docs/ldap-sync-and-provisioning-troubleshooting#checking-for-user-query-limitation), [missing user attributes](/v1/docs/ldap-sync-and-provisioning-troubleshooting#checking-for-missing-user-attributes), and [duplicate users](/v1/docs/ldap-sync-and-provisioning-troubleshooting#checking-for-duplicate-users).

#### Checking for Missing User Attributes

User Attributes may be considered invalid or missing by Cato and can lead to users being skipped from provisioning. Make sure that the following attributes are correctly configured for the user:

- First and Last names must be configured for AD users. Otherwise, users missing a first or last name are not synced to your Cato account.
- The email and UPN attributes must be defined in the following format: *user@domain*. Otherwise, the user will be provisioned but it will fail to get an SDP license assignment.

#### Checking User Sync Settings

Changes to LDAP users on the Domain Controller can trigger a high number of user modifications in CMA which is controlled in LDAP settings. As explained in [Updating the Details of Existing Users](/v1/docs/changing-the-email-address-or-user-principal-name-of-users), the options **Prevent removing or disabling users in case more than...** and **Update user emails, up to** will limit the number of users that can be removed, disabled, or updated for each sync.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20323654735005.png)

If the limit is exceeded, the next LDAP sync will fail and new LDAP users will fail to be provisioned. A **Directory Services** event will be generated if the above issue takes place.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17328246910365.png)

To resolve this issue, uncheck these options if the high number of user changes is preventing the sync from completing.

#### Checking for Disabled LDAP Users

When running a sync, if the user to be provisioned is disabled or expired in Active Directory, the user will not be provisioned to CMA. There will be no failed event in CMA.

Confirm on the Domain Controller that the user is enabled.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17305283075485.png)

#### Checking for User Query Limitation

Microsoft Active Directory LDAP has a built-in limitation that only allows objects with less than **1500 attributes** to be returned in any single query. Thus, when CMA runs the LDAP query, any groups with more than 1500 members will return an empty members list to CMA, resulting in deactivated/deleted users in CMA.

A [PCAP capture](/v1/docs/how-to-capture-traffic-on-a-socket) can be run from the Socket LAN to verify if you're experiencing this limitation. The member attribute will be empty and there will be an additional member attribute showing **range=0-X**. This indicates that the AD server was trying to force pagination.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17356425461789.png)

To resolve this issue, see [Resolving User Query Limitation](/v1/docs/ldap-sync-and-provisioning-troubleshooting#resolving-user-query-limitation)

#### Checking for Duplicate Users

When running a sync, if the email address of the user to be provisioned already exists in CMA, the new user provisioning behavior will depend on how the duplicate user was imported to CMA:

- If the duplicate user is LDAP, the new LDAP user will be provisioned successfully but there will be no SDP License assigned on the **Users Directory** page. An **SDP license** event will be generated under the conditions explained above.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17328234312733.png) To resolve this issue, modify the email address or user name of the newly provisioned user or remove the duplicate LDAP user. These fields must be unique across all users in the Directory Service.
- If the duplicate user is SCIM, the new LDAP user won't be provisioned as it won't override the SCIM provisioned user as explained in [Changing from SCIM to LDAP Provisioning](/v1/docs/changing-between-scim-and-ldap-user-provisioning). To resolve this issue, make sure that the email address of each user is unique and that users and groups provisioned with LDAP and SCIM do not overlap with each other.
- If the duplicate user is manual, the new LDAP user won't be provisioned as it won't override the manually provisioned user. To resolve this issue, make sure that the email address of each user is unique or remove the manually provisioned user from CMA before LDAP syncing.

#### Checking for Missing SDP Licenses

When running a sync, if there are no available SDP licenses in the account or for the user and user group in question, the user will be provisioned successfully but there will be no SDP License assigned on the **Users Directory** page.

Verify that an SDP license is assigned to the user or its user group as explained in [Assigning SDP Licenses](/v1/docs/assigning-ztna-licenses-to-users). If the issue is related to SDP licenses in the account, an **SDP license** event will be generated as shown below.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18528825366557.png)

To solve this issue, see [Resolving SDP License Errors](/v1/docs/ldap-sync-and-provisioning-troubleshooting#resolving-sdp-license-errors)

### Troubleshooting Unexpected Provisioned Users

Imported LDAP users may differ from what is configured in CMA for different reasons. This section explains the most common scenarios that may explain this behavior.

#### Empty User Groups Field

As explained in [Importing Active Directory Groups](/v1/docs/implementing-ldap-user-provisioning), if no user groups are selected under LDAP settings, the entire Active Directory is imported. This will result in the import of the entire userbase to CMA and in Cato user license exhaustion.

To solve this issue, define only those specific LDAP groups that you wish to import to Cato and follow [Resolving SDP License Errors](/v1/docs/ldap-sync-and-provisioning-troubleshooting#resolving-sdp-license-errors)

#### Checking for Nested Groups

If after performing an LDAP sync, you noticed that some of the provisioned users were not defined for import in **Access** > **Directory Services** > **LDAP** > **User Groups** check the following:

- Cato LDAP sync scans the members of each defined User group. These groups may include users and also other **nested** groups. In this example, only **VPN group** is defined in CMA. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17306387217437.png)
- You can check all the groups that a specific user belongs to from the **Member of Groups** page in CMA. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17306372710301.png)
- In the example above, **subgroup** is a nested group of **VPN group** so any member of **subgroup** will be imported to CMA given that Cato imports nested groups and their users if they reside within a defined User Group.

## Resolving Discovered Issues

### Resolving LDAP Credential Errors

Confirm that the **Login DN** and **Base DN** fields in LDAP settings are correct based on the attributes of the Admin user configured in Active Directory.

To confirm the Login DN, run the following command from the DC's command prompt:

```plaintext
 dsquery user -name <username>
```

The output will show the full **distinguishedName** configured for the admin user which must match with the **Login DN** field in CMA

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17306127046173.png)

If necessary, reset the password for the admin user on the Domain Controller and make sure it matches the password entered in CMA.

### Resolving LDAPS TLS Errors

If a TLS error is sent by the LDAP server, you may check Windows [Event Viewer](https://learn.microsoft.com/en-us/answers/questions/410696/enforcing-tls-1-2-eventviewer-full-of-event-36871) for more information. If it is sent by the PoP you can try removing and [re-adding](/v1/docs/syncing-users-with-ldap) the related Domain Controller under Directory Services. This will force a re-establishment of the TLS connection with the LDAP server.

### Resolving User Query Limitation

As mentioned in [Syncing Users with LDAP](/v1/docs/syncing-users-with-ldap), to prevent the unwanted deactivation/deletion of users due to this limitation, you can customize the maximum number of users that can change user group membership in a single sync by configuring the "Prevent updating group membership" option in CMA.

To resolve the empty query response from the Domain Controller, you can follow these steps:

- Adjust the Microsoft LDAP policy attribute for MaxValRange which controls how many values will be returned. The procedure is explained in this [MS article](https://learn.microsoft.com/en-GB/troubleshoot/windows-server/active-directory/view-set-ldap-policy-using-ntdsutil).
- Alternatively, the query restriction can be removed entirely as explained in this [MS article](https://learn.microsoft.com/en-us/archive/blogs/qzaidi/override-the-hardcoded-ldap-query-limits-introduced-in-windows-server-2008-and-windows-server-2008-r2).
- If no changes are allowed in Active Directory, the only alternative is to use an LDAP group with less than 1500 attributes to provision users to Cato.

### Resolving SDP License Errors

Licensing status of accounts can be found under **Administration > License > User**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17304907399965.png)

In instances where there are no sufficient licenses available, reduce the scope of users and user groups under **Access > License Assignment**. Otherwise, check with your CSM or account owner to purchase additional SDP licenses.

## Raising cases to Cato Support

Submit a [Support ticket](/v1/docs/submitting-a-support-ticket) with the results of the above troubleshooting steps. Please include the following information in the ticket:

- Details of the experienced issue and overall impact on users.
- Related Directory Services events and the result of the manual LDAP sync.
- PCAP capture file showing the full conversation with the LDAP server.
