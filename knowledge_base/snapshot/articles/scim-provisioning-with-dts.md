---
title: "SCIM Provisioning with DTS"
slug: "scim-provisioning-with-dts"
updated: 2026-07-02T15:29:40Z
published: 2026-07-02T15:29:40Z
canonical: "knowledge.catonetworks.com/scim-provisioning-with-dts"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SCIM Provisioning with DTS

## Overview

SCIM defines a standard for exchanging identity information across different cloud app vendors. User information is securely synced from your IdP to Cato to create users. Any changes to users’ details that were made in the IdP are reflected in Cato in near real time. For example, if an employee leaves a company, their account is removed from the company IdP. This change is synced with Cato, and the user is deleted. For more information on SCIM Provisioning, see [Provisioning Users with SCIM.](/v1/docs/provisioning-users-with-scim)

### Capabilities Supported

- Push new users - Creates a new user in the Cato Management Application (CMA)
- Push profile update - Updates a user's attributes in the CMA
- Deactivate user - Deactivates users in the CMA
- Reactivate users - Reactivates a deactivated user in the CMA
- Push groups - Creates and updates group membership in the CMA

### Prerequisites

- DTS tenant with admin access

## Configuring SCIM Provisioning with DTS

To configure SCIM provisioning with DTS, you need to:

1. Create SCIM credentials in the CMA
2. Create an Application in the DTS Admin Console
3. Configure Users and Groups in the DTS Admin Console to be provisioned

### Step 1: Creating SCIM Credentials in the CMA

In the Cato Management Application (CMA), identify the Base URL and generate the Bearer Token.

**To create SCIM credentials:**

1. In the CMA, navigate to **Access > Directory Services**.
2. On the **SCIM** tab, click **New**.
3. Choose a **Directory Name** and from the **Provider** drop-down, select **DTS Identity**.
4. Copy and save the **Base URL** so that it can be entered into the DTS Admin Console.
5. Click **Generate Token** and copy and save the **Bearer Token** so that it can be entered into the DTS Admin Console.
6. Click **Save**.

### Step 2: Create an Application in the DTS Admin Console

In the DTS Admin Console, create an application with the credentials you created in step 1.

**To create an application:**

1. In the DTS Admin Console, navigate to **Admin Console > Applications**.
2. Click **Create custom app**.
3. Add an Application name and choose **Web Application**.
4. Click **Create Application**.
5. In the Application you created, navigate to the **Provisioning** tab.
6. Click **Configure provisioning > Configure SCIM**.
7. In the **SCIM base URL** field, enter the **Base URL** you created in step 1.
8. In the **SCIM authentication method** drop-down, select **Bearer Token**.
9. In the **Bearer Token** field, enter the **Bearer Token** you created in step 1.
10. In the **Provisioning to App settings,** select the entities you want to provision into the CMA.
11. Click **Save changes**.
12. Click **Test & Activate provisioning**.

### Step 3: Configure Users and Groups in the DTS Admin Console to be Provisioned

Create and add the users and groups you want to provision into the CMA to the application.

**To provision users:**

1. If you have not created users, in the DTS Admin Console, navigate to **Admin Console > People**, click **Add person**.
2. Navigate to **Admin Console > Applications** and open the application you created in step 2.
3. On the **Assignments** tab, assign the users you want to provision

**To provision groups:**

1. If you have not created groups, in the DTS Admin Console, navigate to **Admin Console > Groups**, click **Create new group** and add users.
2. In the group, navigate to the **Application** tab and assign the application you created in step 2.

## Assigning ZTNA Licenses

In the IdP, define the groups and users that are synced to your Cato account. After the initial sync is completed, all users are then created in the Cato Management Application and visible on the **Users Directory** page.

You can then assign ZTNA licenses to users. For more information, see [Defining Remote Access for Users](/v1/docs/assigning-ztna-licenses-to-users).

## Understanding Events for SCIM Provisioning

The Cato Management Application generates events whenever users and groups are blocked because they fail to meet the requirements of the Client Connectivity Policy.

Each hour, the Cato Management Application sends email alerts that summarize the SCIM provisioning actions (success or failure).

The following table explains the different events.

| Event Type | Action | Description |
| --- | --- | --- |
| SCIM Provisioning | Success | The action to sync the users or groups to your account with the SCIM app succeeded. |
| SCIM Provisioning | Failure | The SCIM app failed to sync the IdP with your account. The **event message** explains the reason for the sync failure. |
| SCIM Provisioning | Disabled | A disabled user in the IdP was successfully synced and disabled in your Cato account. |
