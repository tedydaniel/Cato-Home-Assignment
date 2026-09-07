---
title: "Working with User and System Groups"
slug: "working-with-user-and-system-groups"
status: "update"
updated: 2026-09-06T10:23:53Z
published: 2026-09-06T10:23:53Z
canonical: "knowledge.catonetworks.com/working-with-user-and-system-groups"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with User and System Groups

## Overview

Users in your account are included within two different types of groups.

### User Groups

User groups are objects for use in rules, policies, or assigning licenses. For example, if you add a User group to a rule within your Internet Firewall policy, that rule applies to all the users within the User group. There are three types of User groups:

- **System groups:** Automatically created
- **SCIM/LDAP defined:** Provisioned from your IdP
- **User defined:** Manually created

**Note**: The maximum number of users that can be added to a user defined group is 50,000

You can view the User groups in your account from the **Access > User Groups** page.

#### Understanding System Defined User Groups

Cato automatically creates the **All Users** System User group. This contains all the users created in your account. Use this User group if you want a rule, policy, or settings to apply to all users.

If you have at least one WMI controller configured, these System User groups are also created:

- **All Users Pending Identification:** Users that have been synced but have not signed into the Client
- **All Unidentified Users:** Users that cannot be identified
- **All Unmapped Users:** Uses that can be identified, but cannot be matched to information (e.g. organizational data) that synced from LDAP

#### System Groups for Assigning Licenses

System groups are objects for assigning SPD licenses to users, they are only visible on the **Access > License Assignment** page. For example, you can assign a SDP license to all manually created users. System groups cannot be used in rules or policies. There are three types of System groups:

- **All LDAP users:** All users provisioned with LDAP
- **All SCIM users:** All users provisioned with SCIM
- **All Manual users:** All users created manually

For more information about assigning SDP licenses, see [Assigning ZTNA Licenses to Users](/v1/docs/assigning-ztna-licenses-to-users).

## Showing User Groups and Members

![User_Groups.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34810730615197.png)

**To show the members of a User group:**

1. In the navigation menu, click **Access > User Groups** and select the User group.
2. In the navigation menu, click **Members**. The group members are displayed.

## Adding User Groups

You can define User groups and their members. For User groups that are created as part of SCIM or LDAP user provisioning:

- Definitions in the **General** pane are defined by the Cato Management Application and can't be modified
- To modify members of LDAP or SCIM User groups, modify the settings in the AD or IdP
- The **Type** of the User group is **SCIM defined** or **LDAP defined**

**To add a group and define its members:**

1. In the navigation menu, click **Access > User Groups** and select the User group.
2. Click **New**. The **Create User Group** panel opens.
3. Enter the group **Name** and click **Apply**. The User group is added to the screen.
4. Click the User group. The **General** screen for the User group opens.
5. **(Optional)** Enter a **Description**.
6. Add the items that are the members of this group:
  1. In the navigation menu, click **Members**. The User group members are displayed.
  2. From the **Add Members** drop-down menu, select the type of member to add (SDP User or User).
  3. Select all the users that you are including in the User group.

The SDP Users and Users are added to the Members list.
7. Click **Save**.

## Deleting User Groups

Depending on how they were created, User groups can be permanently deleted or disabled.

- Manually created User groups can be manually deleted. After being deleted, they are no longer visible on the **User Groups** page. Deleted User groups are still visible in policies and marked as deleted and the policy is not applied to the User group.
- Provisioned User groups can be deleted in the CMA but we recommend you delete them from your IdP. After being deleted from your IdP, they are no longer visible on the **User Groups** page. Deleted User groups are still visible in policies and marked as deleted and the policy is not applied to the User group.
  - User Groups that were deleted in the CMA, and provisioned by:
    - Okta - are recreated with all membership
    - Entra - are recreated without membership

> [!NOTE]
> Note:
> 
> You cannot undo a deletion.

**To manually delete a User group:**

1. In the navigation menu, click **Access > User Groups** and select the User group.
2. Click ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/img-cc8e2cca6fcdef2b25cda91a4cf0207c(2).svg) (Delete) next to the User group you wish to delete.

A confirmation window opens.
3. Click **Delete.**

The User group is deleted.

## Viewing Policies Applied to a Group

For a clear, centralized view of each groups policy coverage, you can view all the policy rules that are applied to a group on the **Applied Policies** page.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(204).png)

**To view policies applied to a group:**

1. In the navigation menu, click **Access > User Groups** and select the User group.
2. Navigate to the **Applied Polices** page.

### Changing the Path to a Group in your Domain Controller

For LDAP provisioned User groups, if you change the path to a Group in your Domain Controller, you must also update the **Base DN** in the Cato Management Application (CMA).

If you do not update the CMA to the new path, User groups that have been moved are no longer included in syncs and are deleted. These User groups are no longer visible on the **User Groups** page. Deleted User groups are still visible in policies and marked as deleted and the policy is not applied to the User group.SDP licenses are removed from users within the deleted LDAP provisioned User group and can no longer connect to the network. If the users need to connect to the network, then it's necessary to re-assign SDP licenses to them.

### Version Control

| Date | Description |
| --- | --- |
| September 6, 2026 | Updated with details of the **Applied Policies** page |
