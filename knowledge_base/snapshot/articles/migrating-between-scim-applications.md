---
title: "Migrating Between SCIM Applications"
slug: "migrating-between-scim-applications"
updated: 2026-07-06T13:36:27Z
published: 2026-07-06T13:36:27Z
canonical: "knowledge.catonetworks.com/migrating-between-scim-applications"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrating Between SCIM Applications

This article explains how to migrate user and group provisioning between SCIM applications. This includes migrations within the same identity provider (IdP), such as Microsoft Entra to Microsoft Entra, and migrations between different IdPs, such as Microsoft Entra to Okta.

## Overview

When replacing one SCIM application with another, Cato recommends configuring the new application to use the **same SCIM directory** as the existing application.

Using the same SCIM directory allows Cato to recognize existing users and groups and update them during provisioning. Creating a new SCIM directory is supported, but can result in duplicate objects or failed updates because Cato treats the new directory as a different provisioning source.

## Recommended Migration Workflow

To migrate between SCIM applications:

1. Configure the new SCIM application to use the existing Cato SCIM directory
2. If you are migrating users and groups within the same IdP, assign users and groups with the same UPNs and group names to the new application
3. Run a provisioning cycle from the new application
4. Verify that existing users and groups were updated successfully without duplication
5. If required, remove any users or groups that should no longer exist after the migration

## How Users Are Matched

Cato matches existing users using these identity attributes:

- **User Principal Name (UPN)** (`userName`)
- **IdP Object ID** (`externalId`)

When the new application uses the same SCIM directory:

| Migration Scenario | Result |
| --- | --- |
| Matching UPN or Object ID (with active or inactive user) | Existing user is updated |
| No matching UPN or Object ID | New user is created |

When the new application uses a different SCIM directory:

| Migration Scenario | Result |
| --- | --- |
| Matching UPN or Object ID and existing user is inactive | Existing user is updated |
| Matching UPN or Object ID and existing user is active | Update is rejected, the old user remains and can’t be updated |
| No matching UPN or Object ID | New user is created |

For migrations between different IdPs, Object IDs typically change. This is expected and does not prevent a successful migration if the user's UPN remains unchanged.

If both the UPN and Object ID change, Cato cannot identify the incoming user as the stored user. In this case, a new user is created and the previous user must be removed manually.

## How User Groups Are Matched

Cato matches user groups using these attributes:

- **Group display name**
- **Group Object ID** (`externalId`)

When the new application uses the same SCIM directory:

| Migration Scenario | Result |
| --- | --- |
| Matching group name or Object ID (with active or inactive group) | Existing group is updated |
| No matching group name or Object ID | New group is created |

When the new application uses a different SCIM directory:

| Migration Scenario | Result |
| --- | --- |
| Matching inactive group name or Object ID | Group is not updated |
| Matching active group name or Object ID | Update is rejected, the old user group remains and can’t be updated |
| No matching group name or Object ID | New group is created |

For migrations between different IdPs, group Object IDs usually change. To ensure groups are matched correctly, keep the group display names unchanged whenever possible.

Group membership is determined by the users provisioned through the same SCIM directory. Users who are not provisioned by the new application aren't added to migrated groups.

## Reviewing the Migration

SCIM provisioning only updates the users and groups assigned to the new application. It doesn't automatically remove objects that were previously provisioned by the old application.

After the migration:

- Verify that all required users and groups were provisioned by the new application
- Remove or deactivate users who are no longer assigned
- Remove user groups that are no longer required
