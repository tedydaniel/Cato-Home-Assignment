---
title: "Cato API - EntityLookup"
slug: "cato-api-entitylookup"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/cato-api-entitylookup"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato API - EntityLookup

We strongly recommend that before you start using the Cato API, please review the [Support Policy for the Cato API](/v1/docs/support-policy-for-the-cato-api).

## Overview of entityLookup

The entityLookup query works with Cato Management Application entities such as sites and VPN users. The query can help you look up an entity name to return the specific ID, and automatically extract a list of entities in the account. Each entity is returned with additional relevant information, such as the creation date and the description.

For reseller accounts, you can create separate API keys inside each customer account that you are connecting to the Cato API. For more about rate limiting and the entityLookup API query, see [Understanding Cato API Rate Limiting](/v1/docs/understanding-cato-api-rate-limiting).

## Details for the entityLookup Fields

These are the details that the auditFeed fields can show for the query:

- items - the items field contains the data for each entity
- total - total number of entities returned for this query

## entityLookup Items

The EntityInfo fields show the data for each entity, including:

- entity - shows the **id**, **name** from the Cato Management Application, and the **type** of entity usually site or vpnUser
- description - description of the entity from the Cato Management Application
- helperFields - additional relevant information and data about the entity

## entityLookup Total

The Total field shows the total number of entities for your account in the Cato Management Application. The value of this field doesn't change during the pagination of the API return, and can help you easily compare it to the total number of records retrieved.

## Arguments for the entityLookup

These are the arguments that you can pass and define the entities that are returned by the query:

- accountIDs - account IDs, for multiple accounts, enter the IDs as an array (mandatory argument)
- type - return entities that match the type, for example the **site** or **vpnUser** (mandatory argument)
- limit - maximum number of entities returned for this query (default value is 50)
- from - according to the index of entries, start the query from this specific entity
- search - filter the return according to this value
- entityIDs - entity IDs, for multiple entities, enter the IDs as an array
- sort - defines how the entities that the query returns are sorted

## entityLookup accountIDs Argument

Enter one or more account IDs for the data that the query returns.

This account ID is displayed in the Administration > General Info page.

The accountIDs argument is mandatory for the query.

## entityLookup type Argument

The type argument defines the entity data that the query returns. These are the supported values for the type argument: **site**, **vpnUser**, and **admins**.

The type argument is mandatory for the query. Refer to the schema for the enum items for each value.

## entityLookup limit Argument

The limit argument defines the maximum number of entities that the query returns. If you don't specify the limit argument, then the query is limited to 50 entities.

Each query can return a maximum of 1000 entities.

## entityLookup from Argument

The from argument defines which entity to start the query. For example, if an account has 100 VPN users, set ir to **60** to show only the last 40 VPN user entities.

The first item in the query is 0. So, if you want to only show starting from item 20, then set it to 19.

## entityLookup search Argument

The search argument filters the query to only return matching entity names. The search argument is a string value.

## entityLookup entityIDs Argument

The entityIDs argument only returns entities that match the IDs.

## entityLookup sort Argument

The sort argument lets you sort the data according to the id or name for the entities, in ascending or descending order.

- field - use **name** or **id** as the field value
- order - sort the results in ascending (**asc**) or descending (**dsc**) order

For example, to sort the results in ascending order (a-z) according to the name, use this argument: `sort:{field"name", order:asc}`

## entityLookup parent Argument

The parent argument is used to query entities with a hierarchy, where you need to supply the entity and it's parent. For example, for the type `networkInterface` , you need to enter the parent with these values: **id** <site id>, **type** site.

## Sample entityLookup Queries

This section has examples of entityLookup queries.

### Query All Sites in the Account

**Sample Postman Script**

```plaintext
query entityLookup ($accountID: ID!, $type: EntityType!, $search: String) {
    entityLookup (accountID: $accountID, type: $type, search: $search) {
        items {
            entity {
                id
                name
            }
        }
    }
}
```

**GraphQL Variables**

```plaintext
{
    "accountID": "26",
    "type": "site"
}
```

### Search for Site Using the Site Name

**Sample Postman Script**

```plaintext
query entityLookup ($accountID: ID!, $type: EntityType!, $search: String) {
    entityLookup (accountID: $accountID, type: $type, search: $search) {
        items {
            entity {
                id
                name
            }
        }
    }
}
```

**GraphQL Variables**

```plaintext
{
    "accountID": "26",
    "type": "site",
    "search": "MySite"
}
```

### Search for networkInterface Including parent Argument

**Sample Postman Script**

```plaintext
query entityLookup ($accountID: ID!, $type: EntityType!, $parent: EntityInput!) {
    entityLookup (accountID: $accountID, type: $type, parent: $parent) {
        items {
            entity {
                id
                name
                type
            }
            description
            helperFields
            }
        }
    }
}
```

**GraphQL Variables**

```plaintext
{
    "accountID": "26",
    "type": "networkInterface",
    "parent": {
        "id": 52180,
        "type": "site"
    }
}
```
