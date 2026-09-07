---
title: "Exporting User Data"
slug: "exporting-user-data"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/exporting-user-data"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Exporting User Data

You can generate a CSV file that contains a report of all the SDP users and User Awareness users in your account.

## Exporting User Data

You can export the user data to a CSV file and see more information about these users.

**To export user data:**

1. From the navigation menu, click **Access > Users**.
2. Click **Export Users**, and in the pop-up window click **OK**.

The Save window for the browser opens.
3. Select the location for the CSV file and click save. The Cato Management Application generates the user report and exports it to a CSV file.

> [!NOTE]
> Only Cato Management Application admins with **Editor** role have permissions to export to a CSV file. For more about configuring admin roles, see [Managing Administrators](/v1/docs/managing-admins).

### Known Limitations

- Only users with [SDP licenses](/v1/docs/assigning-ztna-licenses-to-users) are exported

## Understanding the Report Fields

This section explains the values of the columns in the exported CSV file.

| Column | Description |
| --- | --- |
| First Name | User's first name |
| Last Name | User's last name |
| Email | User's email address |
| Phone Number | User's phone number |
| Status | User's status, values include: - **Active** - Corresponds to **Configured** in the CMA. The user has been created in the Cato Management Application. - **Disabled** - The user is disabled. They cannot connect to the Cato Cloud. - **Locked** - The user is locked because they failed too many consecutive authentication attempts. |
| Creation Date | The date and time the user was created in the format: YYYY/MM/DD HH:MM |
| Last Connection Date | The date and time the user last connected to the Cato Cloud in the format YYYY/MM/DD HH:MM |
| Device Name | The name of the device the user is using to connect to the Cato Cloud |
| Device OS Type | The operating system of the device used by the user |
| Device OS Version | The version of the operating system used by the user |
| Client Version | The version of the Client used by the user |
| Origin | How the user was provisioned. Possible values are: - **SCIM**- User created automatically with SCIM sync - **LDAP**- User created automatically with LDAP sync - **Manual**- User created manually in the CMA |
| Authentication Type | The method of authentication used by the user. Possible values are: - **MFA** - The user authenticates using Multi-Factor authentication - **SSO** - The user authenticates using Single Sign On - **Username and Password** - The user authenticates using a Username and Password |
