---
title: "Managing Admins with the Cato API"
slug: "managing-admins-with-the-cato-api"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/managing-admins-with-the-cato-api"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Admins with the Cato API

This article discusses the different Cato APIs that let you manage admins and admin roles for the Cato Management Application. This API supports managing admins for both reseller accounts and regular accounts.

## addAdmin Configuration API

The `addAdmin` configuration API creates new admins for the account in the Cato Management Application.

### addAdmin Input Parameter

- accountId (mandatory)

### addAdmin Arguments

These are the arguments for the `addAdmin` configuration API:

- firstName: The first name of the admin (max 255 characters) – this field is mandatory
- lastName: The last name of the admin (max 255 characters) – this field is mandatory
- email: The email address, unique per admin (max 255 characters) – this field is mandatory
- passwordNeverExpires: Boolean value (true/false). If value set to true, the password of the admin never expires – this field is mandatory
- mfaEnabled: Boolean value (true/false). If value set to true, admin must use an MFA code to log in to the Cato Management Application - this field is mandatory
- managedRoles: array of updateAdminRoleInput. Defines one or more roles that are assigned to the admin. For reseller admins, this field defines the roles that are assigned to the admin for the managed accounts. If this field isn’t defined for the API call, then the admin is assigned the viewer role (ID 2)
  - Use the ID 1 to assign the editor role to the admin
- resellerRoles: array of updateAdminRoleInput (relevant only for reseller admins). Defines the roles that the admin is assigned for the reseller account. If this field isn’t defined for the API call, then the admin is assigned the viewer role for the reseller account.

Once the admin is created, the flow is the same as it if the admin was created in the Cato Management Application.

If the account is defined to let admins log in with username and password, then the admin will receive the welcome email with a link to activate the account and set the password.

| ![image1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/8788772690717(1).png) |
| --- |

### addAdmin API Example

```plaintext
mutation  {
  admin(accountId:"xxxxxx") {
    addAdmin(input: {
      firstName :"dani2",
      lastName :"din2"
      email: "danidin5@4catonetworks.com",
      passwordNeverExpires: true,
      mfaEnabled: false,
      managedRoles: [{ role: { id: 2} }, {role: {id:3}}]
    }) {
        adminID
    }
  }
}
```

| ![image2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/8788805455517(1).png) |
| --- |

| ![image3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/8788805492637(1).png) |
| --- |

## updateAdmin Configuration API

`updateAdmin` configuration API lets you update admin information (admin's email and id cannot be updated).

### updateAdmin Input Parameters

- accountId (mandatory)

### updateAdmin Arguments

- adminID (mandatory)
- firstName: The first name of the admin
- lastName: The last of the admin
- passwordNeverExpires: Boolean value (true/false). If value is set to **true**, the password of the admin never expires
- mfaEnabled: Boolean value (true/false). If the value set to **true**, the admin must use an MFA code to log in to the Cato Management Application
- managedRoles: array of `updateAdminRoleInput`. Defines one or more roles that are assigned to the admin. For reseller admins, this field defines the roles that are assigned to the admin for the managed accounts.
- resellerRoles: array of `updateAdminRoleInput` (relevant only for reseller admins). Defines the roles that the admin is assigned for the reseller account.

### updateAdmin API Example

```plaintext
mutation {
  admin(accountId: "26") {
    updateAdmin(
      adminID: "28876"
      input: {
        firstName: "sample"
        lastName: "admin"
        passwordNeverExpires: true
        managedRoles: [{ role: { id: 1 } }]
      }
    ) {
      adminID
    }
  }
}
```

![updateAdmin.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/8788805514781(1).png)

## removeAdmin

The `removeAdmin` configuration API lets you delete an admin from the account.

### removeAdmin Arguments

- accountId (mandatory)
- adminID (mandatory)

### removeAdmin API Example

```plaintext
mutation  {
  admin(accountId:"XXX") {
    removeAdmin(adminID:YYY
    ) {
        adminID
    }
  }
}
```

## admins Read-Only API

The `admins` read-only API query returns data regarding all the admins of the account, including: id, email, First Name, Last Name, passwordNeverExpires, mfaEnabled, and roles.

### admins Input Parameter

- accountId (mandatory)

### admins Arguments

- id: The Cato ID of the admin
- firstName: The first name of the admin
- lastName: The last of the admin
- email: The email address
- passwordNeverExpires: Boolean value (true/false). If value is set to **true**, the password of the admin never expires
- mfaEnabled: Boolean value (true/false). If value is set to **true**, the admin must use an MFA code to log in to the Cato Management Application
- managedRoles: array of updateAdminRoleInput. Defines one or more roles that are assigned to the admin. For reseller admins, this field defines the roles that are assigned to the admin for the managed accounts.
- resellerRoles: array of updateAdminRoleInput (relevant only for reseller admins). Defines the roles that the admin is assigned for the reseller account.

### admins API Example

```plaintext
query {
  admins(accountID: XXXX) {
    items {
      id
      email
      firstName
      lastName
      modifyDate
      creationDate
      passwordNeverExpires
      mfaEnabled
      managedRoles {
        role {
          id
          name
        }
	resellerRoles {
        role {
          id
          name
        }
      }
    }
  }
}
```

![admins.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/8788772828573(1).png)

## getAdmin Read-Only API

The `getAdmin` read-only API query returns information about a single account admin, such as: Email, First Name, Last Name, passwordNeverExpires, mfaEnabled, and roles

### getAdmin Input Parameters

- accountId (mandatory)
- adminID (mandatory)

### getAdmin Arguments

- firstName: The first name of the admin
- lastName: The last name of the admin
- email: The email address
- passwordNeverExpires: Boolean value (true/false). If set to true, the password of the admin never expires
- mfaEnabled: Boolean value (true/false). If set to true, the admin must use an MFA code to log in to the Cato Management Application
- managedRoles: array of updateAdminRoleInput. Defines one or more roles that are assigned to the admin. For reseller admins, this field defines the roles that are assigned to the admin for the managed accounts.
- resellerRoles: array of updateAdminRoleInput (relevant only for reseller admins). Defines the roles that the admin is assigned for the reseller account.

### getAdmin API Example

```plaintext
query {
  getAdmin(accountId: "XXX", adminID: YYY) {
    id
    firstName
    lastName
    email
    passwordNeverExpires
    mfaEnabled
    creationDate
    managedRoles {
      role {
        id
        name
      }
    }
    resellerRoles {
      role {
        id
        name
      }
    }
  }
}
```

![getAdmin.png](https://support.catonetworks.com/hc/article_attachments/8788772860701)

## accountRoles Read-Only API

The `accountRoles` API read-only query returns all the roles defined for the account (custom roles and the predefined ones). It is required for customers that use the `addAdmin` API, because this APIs shows the role IDs (used by the addAdmin API).

### accountRoles Input Parameters

- accountId
- accountType
  - Regular (for regular or managed accounts roles)
  - Reseller (for reseller account roles)

#### accountRoles Arguments

```plaintext
   id: ID! (the id of the role)
   name: String! (the name of the role)
   description: String (the description)
   isPredefined: Boolean! (is it a predefined or a custom role)
```

| ![image4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/8788772888605(1).png) |
| --- |

### accountRoles Query Example

```plaintext
query{
  accountRoles(accountID:XXX, accountType:REGULAR)
  {
    items
    {
      id
      name
      isPredefined
      description
    }
    total
  }
}
```

## updateAdminRoleInput Configuration API

The `updateAdminRoleInput` configuration API lets you update the settings for an admin role for the Cato Management Application.

```plaintext
input updateAdminRoleInput {
  role: updateAccountRoleInput!
  allowedEntities: [entityInput!]
}
```
