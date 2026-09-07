---
title: "Managing Admin Roles Using RBAC"
slug: "managing-admin-roles-using-rbac"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/managing-admin-roles-using-rbac"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Admin Roles Using RBAC

This article explains how to configure admin roles that control access to the Cato Management Application (CMA). To learn more about RBAC, see [What are Admins and Role-Based Access Control (RBAC)](/v1/docs/what-are-admins-and-role-based-access-control-rbac).

## Understanding the Predefined Admin Roles

Cato provides a number of predefined roles that you can assign to admins. You can click on the row of a role to show the permissions for each page in the **Edit Role** panel. However, predefined roles can't be modified or deleted.

These are the predefined roles:

- **Editor** - Full read/write permissions for all pages
- **Viewer** - Read only permissions for all pages
- **Network Admin** - Admins that primarily deal with connectivity and network access. Permissions include editing of all pages under the Network menu and other relevant pages such as WAN Firewall, but view only permissions for security features such as Internet Firewall. Permissions for access features are also view only.
- **Security Admin** - Admins that primarily deal with security. Permissions include, for example, editing of all pages under the Security and Assets menus, but view only permissions for network and access features.
- **Access Admin** - Allows editing of all the pages under the Access menu, with permissions for all other pages set to **None**
- **Regional Viewer** - Read only permissions for all sites and SDP users, and also for all events and application analytics
- **Restricted Viewer** - Read only permissions for all sites and SDP users (no access to events and application analytics)
- **Logistics Admin** - Full read/write permission for the Sockets and Accessories page
- **AI Security Sensitive** - Access to view prompt data entered by users in the AI Security module.

## Working with Custom Admin Roles

You can create custom roles and define granular permissions for all pages in the CMA to fit the exact needs of your organization. However, you can't set separate permissions for individual tabs and features within a page.

By default, when you create a new role all permissions are set to **View only**. You can click in the row of the role to modify the permissions in the **Edit Role** panel. You can delete a role from the more menu in the row of the role, however, you can't delete a custom role that is currently assigned to an admin.

- Only an admin with the **Editor** role can create or modify roles
- You can audit changes to custom roles in the Audit Trail (Monitoring > Audit Trail), including creating, modifying, and deleting roles

The permissions for some pages automatically configure dependent permissions for other pages and features. The following dependent permissions apply when creating a role:

- pages in the navigation menu define the permissions for pages and sections that are under them. For example, permissions for the Sites page (Network > Sites) determine the permissions for the Site Configuration pages accessed from the Sites page.
- For pages that support an export feature, granting **Edit** permissions lets the admin export data or policies. For example, a role with **Edit** permissions for the Internet Firewall page lets the admin export the rules to a CSV file.
- Viewing or editing permissions for the following pages grant **View only** permissions to the Events page. You can change the Events permissions to **Edit** but not to **None**.
  - Sites (Network > Sites)
  - Users (Access > Users)
  - Application Analytics (Home > App Analytics)
  - Threats Dashboard (Security > Security Threats)
  - Cloud Apps Dashboard (Security > Cloud Apps Dashboard)
  - [MITRE ATT&CK®](/v1/docs/using-the-mitre-att-ck-dashboard) (Security > MITRE ATT&CK®)

**To create a custom admin role:**

1. From the navigation menu, click **Account > Roles & Permissions**.
2. Click **New** to create a custom role. The **Create Role** panel opens.
3. Enter a **Role Name** and expand the sections to define permissions for the Cato Management Application pages in each section.
4. Click **Submit**.

The custom role appears in the list of roles.

## Assigning Roles to Admins

In the Administrators page, you can assign one or more roles to each admin. When an admin is assigned multiple roles that include different permissions for the same page, the greater permissions apply. For example, if an admin is assigned one role with **Edit** permissions for the WAN Firewall page, and another role with **View only** permissions, the admin can edit the WAN Firewall policy.

**Note:** If you used an IdP to import a group of admins, you can use this procedure to define their roles as a group.

- Only an admin with the **Editor** role can assign or remove roles
- You can review changes to role assignments in the Audit Trail (Monitoring > Audit Trail)

![Assign_Role.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31477785863453.png)

**To assign roles to an admin:**

1. From the navigation menu, click **Account > Administrators**.
2. Click in the row of an admin to open settings for the admin.
3. From the **Roles** drop-down menu, select one or more roles.
4. Click **Save**.

The roles are applied to the admin.

## Provide Admin Access to Sites, Users, and Advanced Groups

You can define which sites, SDP users, and advanced groups that Cato Management Application admins have permissions to edit or view. Admins that do not have view permissions for a particular site or user will not see information about that entity in CMA pages.

- When admins are granted edit/view permission for a **group** (not advanced group), it refers the ability to view/edit sites within that group. If there are non-site items in the group, they are ignored.
- When admins are granted permission to view/edit an **advanced group**, it means they can view which entities are in the group, or that they can add, or remove members from the group.
- Admins can only create new SDP users when they have **Edit** permissions for all user groups.
- For admins that are assigned permissions based on roles, there is an AND relationship between the role and the entity. For example, if an admin is assigned view permissions for the London site and they do not have permissions to view the Sites page, then they can't view the London site. Or if they have edit permissions for the London site, but have view permissions for the site page, then they can only view the site and can't edit it.

![Admin_site_users.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31477785898909.png)

**To allow admins to access sites, users, and advanced groups:**

1. From the navigation menu, click **Account > Administrators**.
2. Create a new admin, or edit an existing admin.
3. In **Access Permissions for Entities**, select the type of item in the drop-down.
4. Use the drop-down to select one or more entities. The entities are added to the table.
5. Review all settings relating to the entity type. For example, if you just added permission to an individual site, make sure the setting for access to All Sites is appropriate.
6. Define the admin **Permission** for the item in the table.
7. Click **Save**. The sites and user groups are assigned to the admin.

### Known Limitations for Entity Permissions

- Admins can have permissions for up to 1000 SDP users, combining all the user groups assigned to the admin

If an admin has permissions for more than 1000 SDP users, then they receive an error. It is necessary to remove permissions for some user groups so they contain permissions for fewer than 1000 SDP users.
- Admins can have permissions for up to 200 individual sites. There is no limit when sites are applied to a group.
- Cato Reports aren't filtered according to admin permissions for sites and users. You can limit access to the Reports page, to control which admins can generate and view reports.
- When you assign a group to an admin, only the sites and users are applied. Other items in the group (such as network ranges) are ignored.
- The following dashboards and monitoring pages are not automatically filtered for sites or SDP users:
  - Routing Table
  - Audit Trail
  - SaaS Security API Dashboard
  - XDR Dashboard
  - Detection and Response
  - Assets
- When managing rules in policies, admins can create rules using the **Any** value (e.g., Any site, Any user group, etc), even if they only have permissions for some sites, user groups, or advanced groups.
- Admins who have permissions for user groups, can only add SDP users to rules. They can't add users identified with User Awareness to rules.
