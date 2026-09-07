---
title: "Migrating LDAP to SCIM (Part 3)"
slug: "migrating-ldap-to-scim-part-3"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/migrating-ldap-to-scim-part-3"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrating LDAP to SCIM (Part 3)

## Change Freeze

Create a change freeze with the relevant team – no changes will be made to groups and users already synced to the CMA. Check and confirm the number of users deleted and users remaining following the removal of the Domain Users AD group. If you removed users from LDAP, check the actual number of users.

## Migration

**Note:** The speed of the migration depends on the IdP performance at the time of migration.

1. From the group lists, extract the number of users for each group.
2. Disable LDAP sync in the CMA.

**Note:** This step is only mandatory if you want to use LDAP for other users or groups.

If you are continuing to use LDAP for syncing users to Cato, make sure that you don't sync the same user or group that is already synced with SCIM.
3. Start the migration of the groups with currently assigned SDP licenses (in groups of 5) from LDAP to SCIM.
4. Continue the migration of the remaining groups (gradually) from LDAP to SCIM
5. Check each group against the extract taken in step 1 to ensure the number of migrated users is the same as the extract.
6. Check each group inside the firewall rules (Internet / WAN), Network Rules, Client Connectivity Policy, and Always On policy.
7. Monitor SCIM sync logs for errors in the IdP and the CMA events.

## Rollback Plan

If you need to roll back your migration to SCIM and restore LDAP user provisioning, please contact Cato Support.

## Appendix

### Deleting LDAP Domain Users and Groups

If you need to remove a large number of domain users and user groups, follow these steps:

1. Uncheck the options that limit the removal/disabling of users and group membership updates.
2. Remove the Domain Users group.
3. During the nightly LDAP sync, all users and groups will be updated and deleted as necessary. It's not necessary to use the **Sync Now** button if you have a high number of users.
4. In case of an issue or failure, please contact Support.
