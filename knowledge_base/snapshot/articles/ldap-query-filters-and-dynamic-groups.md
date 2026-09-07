---
title: "LDAP Query Filters and Dynamic Groups"
slug: "ldap-query-filters-and-dynamic-groups"
updated: 2026-06-22T09:25:29Z
published: 2026-06-22T09:25:29Z
canonical: "knowledge.catonetworks.com/ldap-query-filters-and-dynamic-groups"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# LDAP Query Filters and Dynamic Groups

This article provides information about how to use LDAP query language to filter users and create dynamic groups.

## Overview

Cato lets you streamline user management by importing only the relevant users from your LDAP directory using LDAP query language. With the LDAP Directory Filter, you can define precise LDAP queries to control which users are synced to Cato. In addition, you can use LDAP queries to organize users into dynamic groups within the CMA. Using LDAP attributes, you can create dynamic groups either as a subset of your original filter or of all your users.

Using the Directory Services page, you can integrate your organization's LDAP directory with Cato and configure user import settings.

### Use Case - Query Filters

ABC Company works with full-time employees and contractors, as well as interns. When importing users to the CMA, as an admin, you only want to import the full-time employees. You create the following query filter for your Azure LDAP instance to import only the relevant employees:

(&(objectCategory=person)(objectClass=user)(employeeType=full-time))

### Use Case - Dynamic Groups

ABC Company has sales representatives all over the country, and they all belong to the Sales department. Using the employeeType attribute, you create a subset of the sales representatives for all of the managers in the Sales department. When a user is promoted and assigned the employeeType Manager and department is set to Sales, they are automatically included in the dynamic group.

### Prerequisites

Before you configure LDAP directory filters or dynamic user groups, make sure that:

- You have an existing LDAP directory integration configured in the CMA
- You are a Cato admin with permissions to modify Directory Services settings

### Known Limitations

- The LDAP Directory Filter imports users only. LDAP user groups are not imported.
- Each account supports up to 10 unique LDAP attributes across all dynamic groups.

Reusing the same attribute with different values (e.g., memberOf=Admin, memberOf=Finance) counts as one attribute.
- Each account supports up to 50 dynamic user groups
- Dynamic groups do not support nested group membership from LDAP.

## Import Users using LDAP Query Filters

You can choose to import users using traditional group selection or the new LDAP query filter. You can also define Dynamic User Groups that automatically group users based on attributes from your directory.

> [!NOTE]
> Note:
> 
> LDAP query language is not developed nor maintained by Cato. You are responsible for writing and validating queries that meet your organization’s requirements.

![ldap-query-filter.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31298491467677.png)

**To configure an LDAP directory filter:**

1. From the navigation menu, select **Access > Directory Services**.
2. Select an existing LDAP configuration or click New to create one.
3. Under Filters, in the **Filter Method Field**, select **LDAP Query**.
4. In the **Query** field, enter an LDAP query using your vendor's directory prefix and LDAP attributes. The query must begin with a valid vendor-specific prefix.

See below for some example query filters.
  - **Azure:** (&(objectCategory=person)(objectClass=user))
  - **OKTA + OpenLDAP:** (&(objectClass=inetOrgPerson))
  - **JumpCloud + OneLogin:** (&(objectClass=person))
5. Click **Save**.

### Example Query Filters

The following are examples of several different filters you can use. Refer to the documentation for your LDAP vendor for more information.

#### Fetch Users from a Specific Group (Azure)

The following example imports users from a specific group using the memberOf attribute, and is formatted for Azure:

```plaintext
(&(objectCategory=person)(objectClass=user)(memberOf=CN=Developers,OU=Groups,DC=catonetworks,DC=com))
```

#### Fetch Users from Two Groups (Okta)

The following example imports all users from two groups, and is formatted for Okta:

```plaintext
(&(objectClass=inetOrgPerson)(memberOf=CN=Admins,OU=Groups,DC=catonetworks,DC=com)(memberOf=CN=VPNUsers,OU=Groups,DC=catonetworks,DC=com))
```

#### Fetch Users from Either of the Two Groups (Jumpcloud)

The following example imports all users who belong to either of the two groups defined, and is formatted for Jumpcloud:

```plaintext
(&(objectClass=person)(|(memberOf=CN=Admins,OU=Groups,DC=catonetworks,DC=com)(memberOf=CN=VPNUsers,OU=Groups,DC=catonetworks,DC=com)))
```

## Configure Dynamic Groups

After importing users with either user group selection or LDAP filter, you can create dynamic groups based on LDAP attributes.

![ldap-dynamic-groups.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/31298520048413.png)

**To configure a dynamic group:**

1. From the navigation menu, select **Access > Directory Services**.
2. Select an existing LDAP configuration or click New to create one.
3. Under **Dynamic Groups:** enter a name for the group and define the query.
  - No prefix is required for dynamic groups.
  - If you defined an LDAP query filter, the dynamic group is a subset of that filter. Otherwise, the dynamic group is a subset of all your users.
4. Click **Save**.

### Examples

The following are examples for defining dynamic groups:

- Define a dynamic group using a single attribute

```plaintext
(department=Finance)
```

```plaintext
(title=*Manager)
```
- Define a dynamic group using multiple attributes with the AND operator:

```plaintext
(&(department=Sales)(title=Executive*))
```
- Define a dynamic group using multiple attributes with the OR operator:

```plaintext
(|(appRole=Admin)(appRole=Support))
```

## Troubleshooting Filter Queries and Dynamic Groups

The following is a list of possible error messages and their explanations.

- You can define either a Group DN Filter or an LDAP Query Filter

Appears when you have defined both a Group Filter and an LDAP Query Filter. You can define either one or neither one, but you can't define both.
- LDAP Query Filter is invalid. The error is '<ERROR MESSAGE FROM SDK>'

Appears for several reasons, and the individual error message will provide more information. For example, Unable to parse string '(&amp;(objectClass=group)(cn=*)'. This message appears when you are missing a closing parenthesis.

Refer to the vendor-specific LDAP documentation for more information.
- LDAP Query Filter is missing required user object filters

Appears if you didn't include the required objectClass attribute.
- LDAP Query Filter contains unsupported object filters

Appears if you included a filter on an unsupported attribute, for example, groups instead of users.
- Dynamic Groups require too many additional LDAP attributes (maximum 10 allowed beyond default attributes)

Appears when the sum of all request attributes is not larger than 10 additional attributes (in addition to the ones we fetch by default)
- Too many Dynamic Groups (maximum 50 allowed)

Appears when the maximum of 50 dynamic groups in the account has been exceeded
- Dynamic Group name '<GROUP_NAME>' already exists

Appears when the Group name is not unique.
- Dynamic Group '<GROUP_NAME>' has invalid LDAP query syntax

Appears when the LDAP syntax for the dynamic group is incorrect. Refer to the vendor-specific LDAP documentation for more information.
- Dynamic Group '<GROUP_NAME>' contains user object attributes which are already applied automatically and should not be included in your dynamic group query

Appears when the LDAP query syntax includes attributes that are applied by default by Cato.
