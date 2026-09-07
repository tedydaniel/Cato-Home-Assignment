---
title: "Activating Users with a Registration Code"
slug: "activating-users-with-a-registration-code"
updated: 2026-08-13T17:48:32Z
published: 2026-08-13T17:48:32Z
canonical: "knowledge.catonetworks.com/activating-users-with-a-registration-code"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Activating Users with a Registration Code

This article explains how to activate users with a registration code.

## **Overview**

The registration code method simplifies the activation process for new users. Each user is assigned a one-time code that they use to register the Cato Client. Once the code is validated, the Cato Client is authenticated until an admin revokes the code or disables the user in the Cato Management Application. Users can register multiple devices, with a separate code for each device.

You can also set the amount of time that the registration code is valid for until it expires. Afterwards, the user needs a new registration code to authenticate the Cato Client for that device. For security reasons, registration codes can be valid for a maximum of 7 days.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/activating-users-with-a-registration-code-ea-image-llieyi6b.png)

> [!NOTE]
> Note:
> 
> Multi-Factor Authentication (MFA) is NOT supported for users that are provisioned with a registration code. Make sure that users in your account are not configured with MFA before you enable the registration code User Provisioning method.

#### **High-Level Overview of Implementing the Registration Code**

This is a high-level overview of the process to implement the registration code to provision users for your account. You can configure how long the registration code is valid before it expires. Once the code expires, it can't be used to authenticate the Cato Client. You then need to generate a new code for that user, see below [Generating a Registration Code for Specific Users](/v1/docs/activating-users-with-a-registration-code#generating-a-registration-code-for-specific-users1)

> [!NOTE]
> Note:
> 
> If you have misplaced a previous file containing registration codes for users, generate new codes for the impacted users.

**To implement provisioning all users with a registration code:**

1. From the navigation menu, click **Access > Directory Services**.
2. Click the **User Provisioning** tab or section.
3. Set the provisioning **Method** to **Registration Code**.
4. In **Registration Code expires after**, set the time settings for how long the code is valid. Set when (value and either days or hours) the Registration Code expires. Maximum allowed time is 7 days and applies to all new users.
5. Generate and download the registration codes and use an external solution to send the registration codes to the remote users.

### **Managing Registration Codes**

This section explains how to generate and manage registration codes for the users in your account. Each code is a combination of letters and numbers:

- Codes are NOT case sensitive
- To avoid confusion, the codes don't contain the following characters: 0, o, 1, I, L

#### **Generating Registration Codes for Users**

You can generate registration codes for every remote user who hasn't used a code yet. This includes new users, users whose code expired or was revoked, and users who currently hold an unused code. New users appear first in the CSV.

This action can create multiple codes for an individual user. Any one of these codes can be used to authenticate; once one code is used, the remaining codes for that user are revoked. This means if a user has more than one code, only the first one they use allows authentication, the remaining codes are immediately revoked with no additional action required.

**To generate a registration code for users:**

1. From the navigation menu, click **Access > Directory Services.**
2. Click the **User Provisioning** tab.
3. From the drop down, choose **Registration Code**.
4. Click **Generate Registration Code and Download**.
5. In the Warning confirmation window, click **OK**. As CSV with the Registration Codes is downloaded.

#### **Generating a Registration Code for Specific Users**

You can generate a registration code for specific users. For example, a user whose code expired. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/activating-users-with-a-registration-code-ea-image-h7t3asft.png)

**To generate a registration code for specific users:**

1. From the navigation menu, click **Access > Users**.
2. Select one or more users.
3. Click **Actions** and then from the drop-down menu, click **Generate & download registration code**.
4. In the confirmation window, click **OK**. A new code is generated for these users and downloaded in a CSV.

#### **Revoking Registration Codes**

You can use the **Reset Password** menu option to revoke registration codes and reset VPN access to your network for users.

After you generate a new code for a user and it is successfully entered, the user is authenticated again to the Cato Client.

#### **Note**

**Note:** When revoking a user's registration code, as detailed below, new registration codes are not automatically generated. Select **Generate invitation code** from the Actions drop-down menu to generate a new code.

**To revoke the registration codes:**

1. From the navigation menu, click **Access > Users**.
2. Select one or more users.
3. Click **Actions** and then from the drop-down menu, select **Reset Password**.
4. In the confirmation window, click **OK**. The current codes are revoked for the users.

### **Analyzing Registration Code Events**

The **Event Discovery** window shows all the Registration Code events for your account. The powerful search tools let you drill-down and identify the few events that contain the relevant data that you need.

You can learn more about using the Events screen in [Analyzing Events in Your Network](https://euc-word-edit.officeapps.live.com/hc/en-us/articles/4413273461905#UUID-f2fd1fc7-ac0b-f6aa-3ee6-743332e93f62).

#### **Explaining the Registration Code Events Discovery Actions**

These are actions for the Registration Code event sub type:

| **Name** | **Description** |
| --- | --- |
| Generated | Registration code generated for a specific user |
| Used | Registration code is used to authenticate a user |
| Revoked | Registration code is revoked and no longer valid for the user |
