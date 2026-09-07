---
title: "Defining Remote Access for Users"
slug: "assigning-ztna-licenses-to-users"
updated: 2026-08-17T13:49:53Z
published: 2026-08-17T13:49:53Z
canonical: "knowledge.catonetworks.com/assigning-ztna-licenses-to-users"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Defining Remote Access for Users

## Overview

Remote access lets users securely connect to your organization’s network using the Cato Client when they are not behind a Cato site. As an admin, you control which users and user groups are allowed to use the Client and connect remotely.

> [!NOTE]
> **Note:**
> 
> Cato account licenses use one of two models: **Enforcement** and [**Bursting**](https://knowledge.catonetworks.com/v1/docs/jan-2027-license-bursting-model). The way you license and control remote access depends on your account license model. Not sure which license model your account uses? See [Identifying your License Model](https://knowledge.catonetworks.com/docs/identifying-your-license-model).

## Defining Remote Access Users (Bursting Model)

In the bursting license model, remote connectivity to WAN and private applications is licensed using the Remote User base product, and access to the internet is licensed through the internet security product. Use the Remote Access Eligibility page to define which users or user groups are permitted to connect to the network with the Cato Client.

- Users are measured monthly as distinct authenticated remote users per region group
- If measured usage exceeds the licensed capacity, the excess is considered overusage

### Use Case - Remote Access (Bursting Model)

A company has finance, marketing, and product development teams working in its head office in New York, and a Data Center in Virginia. The company also has sales teams working remotely in 20 different states. Teams working in the head office connect to the data center from behind a Socket site and are in a head office user group.

The sales teams connect to Cato using the Windows Client and are all assigned to a sales team user group. Remote access is only available to users in the sales team user group.

The company ensures that policies are enforced for all users, enabling all teams to securely access network resources. The company optimizes costs by only paying for the sales team to use the Cato Client for secure remote access.

### Defining Remote Access

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/base64-converted-image-1782743863015.png)

**To define users and user groups that can connect with remote access:**

1. From the navigation menu, click **Access** > **Remote Access Eligibility**.
2. Under **Remote Access available to**, select one of the following options:
  - All Users
  - Selected Users or Groups
3. If you chose **Selected Users or Groups**, specify the users and groups allowed to use secure remote access.
4. Click **Save**.

### 

## Assigning ZTNA Licenses (Enforcement Model)

You can manage assigning remote licenses to all your users (whether they are provisioned with SCIM or LDAP, or created manually) from the **License Assignment** page. In the Enforcement Model, users must have a Remote User license to connect remotely using the Cato Client. Remote access is controlled by assigning these licenses to users or groups.

You can also monitor how licenses are assigned in your account, for example, by viewing how many users have a Remote User license.

**Note:** All manually created users are included in the **All Manual Users System** group. To automatically assign manually created users a ZTNA license, add this System group to the **License Assignment** table.

### Prerequisites

- A license can only be assigned to users with an email address
- A license can only be assigned to users with Usernames smaller than 57 characters
- ​​ZTNA user licenses are based on the user’s primary work location. For example, a user located in China requires a China ZTNA license and can continue to use that license when they travel to other countries. The primary work location isn't visible or configurable in the CMA.

### Use Case - ZTNA License (Enforcement Model)

A company has finance, marketing, and product development teams working in its head office in London and a data center in Frankfurt. The company also has sales teams working remotely in 20 different states. Teams working in the head office connect to the data center from behind a Socket site and are not assigned a ZTNA license. The sales teams connect to the data center through the Windows Client and are all assigned ZTNA licenses. The company ensures that policies are enforced for all users, enabling all teams to securely access network resources.

### Assigning ZTNA Licenses to Users and User Groups

**To assign ZTNA licenses:**

1. From the navigation menu, click **Access > License Assignment**.
2. Define how licenses are assigned to your account. The options are:
  - **Assign SDP licenses to all users**
  - **Assign SDP licenses to a selected group**
3. If you are assigning ZTNA licenses to a selected group, select the users or groups from the drop-down.
4. Click **Save**.
