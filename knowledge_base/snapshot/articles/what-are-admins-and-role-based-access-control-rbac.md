---
title: "What are Admins and Role-Based Access Control (RBAC)"
slug: "what-are-admins-and-role-based-access-control-rbac"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/what-are-admins-and-role-based-access-control-rbac"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What are Admins and Role-Based Access Control (RBAC)

This article describes what Cato Admins are and how Role Based Access Control (RBAC) is used to manage their permissions. To learn how to create and manage admins, see [Managing Admins](/v1/docs/managing-admins) and [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).

## What are CMA Admins

Cato admins are users who have permission to access the Cato Management Application (CMA). Cato is a converged platform that manages security policies, network policies, remote user access, and much more. Admins have permission to access all areas unless you limit their permission using RBAC.

## What is RBAC

Role-Based Access Control (RBAC) is a system within the CMA that facilitates the assigning of different roles to admins, each encompassing a set of granular permissions. These roles determine the extent of an admin's capabilities, specifying which pages and features they can view or edit. RBAC enhances security by ensuring admins only have the access required for their responsibilities. This maintains the principle of a zero-trust network and minimizes potential damage.

The CMA includes predefined roles, such as Security Admin and Network Admin, and also allows for the creation of custom roles tailored to your organization's specific needs. This flexibility ensures that access within the CMA is both appropriate and secure.

You can define RBAC admin permissions to edit or only view specific sites, groups of sites, and SDP users. Admins that don't have permissions, can't view the sites or SDP users, and the analytics pages and dashboards are automatically filtered to only show the items with the correct permissions. For example, an admin has view permissions for a group of 10 sites. When the admin opens the Events page, only events for those 10 sites are shown on the page. When creating a new rule for a policy, admins can only choose those sites and user groups that they have permissions to edit.

The Roles & Permissions page comes with several predefined roles with predefined permissions for common admin types. You can also create custom roles to fit the specific needs of admins in your organization. When you create a custom role, you define permissions for the role on a per-page basis. These are the permissions that can be defined for each page:

- **None** - The page doesn't appear in the navigation menu and can't be accessed at all by the admin
- **View** - The admin can view the page but can't make changes
- **Edit** - The admin can perform all actions for the page

![RBAC.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26255629352093.png)

### Roles and Permissions for New Cato Pages

When new pages are added to the CMA, by default the permissions for the page are set to **None** for all existing custom roles. However, there may be exceptions where Cato defines special default permissions for some features. The special default permissions will be published as part of the feature release.

For predefined roles, these are the default permissions for new pages:

- Editor - **Edit** permissions
- Viewer - **View only** permissions
