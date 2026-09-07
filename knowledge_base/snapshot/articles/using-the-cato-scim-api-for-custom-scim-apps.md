---
title: "Using the Cato SCIM API for Custom SCIM Apps"
slug: "using-the-cato-scim-api-for-custom-scim-apps"
updated: 2026-06-22T09:25:07Z
published: 2026-06-22T09:25:07Z
canonical: "knowledge.catonetworks.com/using-the-cato-scim-api-for-custom-scim-apps"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Cato SCIM API for Custom SCIM Apps

This article describes how to use Cato's SCIM API for user and user group provisioning with an identity provider (IdP).

For more information about custom SCIM apps in the IdP tenant, see [Creating a Custom SCIM App for an IdP](/v1/docs/creating-a-custom-scim-app-for-an-idp).

## Custom Cato SCIM App

To use a custom SCIM app to provision users and user groups to your Cato account, create the app in the Cato Management Application (CMA). In addition, you need to map the Cato SCIM attributes to the attributes for your IdP.

### Create a Custom SCIM App in the CMA

To use the SCIM API, you must first create a custom SCIM app in the CMA. This app allows you to integrate your identity provider (IdP) with the Cato platform.

**To create a custom SCIM app in the CMA:**

1. From the navigation menu, select **Access > Directory Services**.
2. Under the SCIM tab, click **New.**
3. Enter a name for the app.
4. Under **Provider**, select **Custom**.
5. Click **Generate Token** and copy the value; it will not be available after you save and you'll need to create a new token.
6. Click **Save**.
7. When calling the SCIM API endpoints described below, you'll need the following values to authenticate:
  - **SCIM Base URL:** Used as the base path for API requests
  - **Bearer Token:** Used for authenticating API requests

### Cato SCIM Attributes

These are the SCIM attributes for Cato users and user groups that you need to map to the corresponding IdP attributes.

| Cato User Attribute | Description |
| --- | --- |
| userName | User name for authentication |
| user.firstName | First name of user |
| user.lastName | Last name of user |
| user.email | Email address |
| user.displayName | Display name for user |
| phoneNumbers[type eq "work"].value | Work phone number for the user (including prefix) |
| externalId | ID for user (used in events) |

| Cato User Group Attribute | Description |
| --- | --- |
| active | User is assigned and active in the SCIM app |
| displayName | Name of user group |
| members | Users who belong to the user group |
| externalId | ID for user group (used in events) |

## Understanding the Cato SCIM API

### Authenticating to the Cato SCIM API

Clients authenticate to the SCIM API using bearer token authentication, as defined by RFC 6750. All API requests must include the following HTTP headers:

```plaintext
Authorization: Bearer <access_token>
Content-Type: application/json
```

You can obtain the access token from the Cato Management Application.

### Base Path for SCIM Endpoints

All SCIM API endpoints use the following base path:

```plaintext
/scim/v2/{accountId}/{sourceId}
```

**Path Parameters:**

- `accountId` (string): Unique identifier of your Cato tenant account
- `sourceId` (integer): An identifier assigned by Cato to uniquely represent a specific IdP integration

These parameters are required in all requests but are omitted from individual endpoint paths in this article for brevity.

## Managing Users

This section describes how to create, update, delete, and retrieve SCIM user entities using the Cato SCIM API.

### Create a User

**HTTP Method:**`POST /Users`

**Required Fields:**

- `userName` (string): Unique username (e.g., email address)
- `externalId` (string): External identifier from the IdP
- `active` (boolean): Must be `true` to activate the user

**Note:**`id` is returned by the SCIM service and must be used in subsequent API calls. `externalId` is optional and cannot be used in API paths.

**Response:**

- Status: `201 Created`

**Errors:**

- `400 Bad Request`: Invalid schema
- `401 Unauthorized`
- `409 Conflict`: Duplicate `userName` or `externalId`

### Update a User

#### PUT

**HTTP Method:**`PUT /Users/{id}`

**Required Field:**

- `id`: Internal SCIM ID from Cato

**Response:**

- Status: `200 OK`

**Errors:**

- `401 Unauthorized`
- `404 Not Found`
- `409 Conflict`: Duplicate `userName` or `externalId`

#### PATCH

**HTTP Method:**`PATCH /Users/{id}`

**Response:**

- Status: `200 OK`

**Errors:**

- `400 Bad Request`: Invalid schema or patch syntax
- `401 Unauthorized`
- `404 Not Found`
- `409 Conflict`: Duplicate identifiers

### Delete a User

**HTTP Method:**`DELETE /Users/{id}`

**Response:**

- Status: `204 No Content`

This is a soft delete. The user remains in the system but is not returned in searches.

### Get a User by ID

**HTTP Method:**`GET /Users/{id}`

**Response:**

- Status: `200 OK`

**Errors:**

- `401 Unauthorized`
- `404 Not Found`

### Search Users

**HTTP Method:**`GET /Users`

**Query Parameters:**

- `filter`: Query to filter users (e.g., `userName eq "user@domain.com"`)
- `count` (optional)
- `startIndex` (optional)

**Supported Filters:**

- Only `eq` is supported
- Supported attributes: `userName`, `email`, `givenName`, `familyName`
- Compound filters are supported only in this format:

```plaintext
filter=emails[type eq "work"] and email eq "bob@cato.com"
```

**Response:**

- Status: `200 OK`

**Errors:**

- `401 Unauthorized`

## Managing Groups

This section explains how to use the SCIM API to create, update, delete, and retrieve group entities in your Cato environment.

### Create a Group

**HTTP Method:**`POST /Groups`

**Response:**

- Status: `201 Created`

**Errors:**

- `401 Unauthorized`
- `409 Conflict`: Duplicate `displayName` or object ID

### Update a Group

#### PUT

**HTTP Method:**`PUT /Groups/{id}`

**Response:**

- Status: `200 OK`

**Errors:**

- `401 Unauthorized`
- `404 Not Found`
- `409 Conflict`

#### PATCH

**HTTP Method:**`PATCH /Groups/{id}`

**Supported Patch Paths:**

- `displayName`
- `members`

**Response:**

- Status: `200 OK`

**Errors:**

- `400 Bad Request`: Invalid schema or patch syntax
- `401 Unauthorized`
- `404 Not Found`
- `409 Conflict`

### Delete a Group

**HTTP Method:**`DELETE /Groups/{id}`

**Response:**

- Status: `204 No Content`

> [!NOTE]
> Important:
> 
> This is a hard delete. The group is permanently removed.

### Get a Group by ID

**HTTP Method:**`GET /Groups/{id}`

**Optional Query Parameters:**

- `excludeAttributes` (e.g., `members`)

**Response:**

- Status: `200 OK`

**Errors:**

- `401 Unauthorized`
- `404 Not Found`

### Search Groups

**HTTP Method:**`GET /Groups`

**Query Parameters:**

- `filter`: Only `displayName eq "Group Name"` is supported
- `count` (optional)
- `startIndex` (optional)

Compound filters or unsupported operators return all groups without filtering.

**Response:**

- Status: `200 OK`

**Errors:**

- `401 Unauthorized`

## Notes

### Behavior of the id Field on Create

- The `id` field is optional in user and group creation requests.
- If omitted, the SCIM service generates a unique `id`.
- Always use the returned `id` value in subsequent API calls.

> [!NOTE]
> Important:
> 
> Avoid using client-generated IDs unless required. The SCIM id is the authoritative identifier.

### Deletion Behavior

- **User deletion** via `DELETE /Users/{id}` performs a *soft delete* by setting the `active` field to `false`. The user is retrievable via `GET /Users/{id}` but excluded from `GET /Users` results.
- **Group deletion** via `DELETE /Groups/{id}` performs a *hard delete*. The group is permanently removed.
