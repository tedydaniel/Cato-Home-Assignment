---
title: "Users Are Not Added to the Expected LDAP Groups"
slug: "users-are-not-added-to-the-expected-ldap-groups"
updated: 2026-07-12T08:08:15Z
published: 2026-07-12T08:08:15Z
canonical: "knowledge.catonetworks.com/users-are-not-added-to-the-expected-ldap-groups"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Users Are Not Added to the Expected LDAP Groups

## Issue

Despite an imported remote user being a member of a group in the AD server, this remote user does not retain its membership of the group in CMA. This means that firewall policies referencing that group will not catch traffic sourced by that remote user.

## Environment

This problem can occur when you are importing users from AD Directory Services.

## Troubleshooting

1. Ensure that the user is indeed a member of the group that is intended.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13067587566621.png)
2. Note that the admin that is configured to query the AD server in CMA's Access -> Directory Services page does not have the required permissions to read the MemberOf attribute of the users

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13067923776157.png)

## Solution

The most common missing permission for querying accounts with WMI queries is group membership. When importing users into CMA, the memberOf attribute is pulled from the AD server, and used to map the user into the AD groups. If the querying admin cannot read this property it returns blank and the users are not correctly mapped as per the group configuration in AD.

[](https://support.catonetworks.com/hc/article_attachments/13067879706269)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13067879706269.png)
