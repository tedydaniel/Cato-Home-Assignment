---
title: "Generating API Keys for the Cato API"
slug: "generating-api-keys-for-the-cato-api"
updated: 2026-07-13T07:53:13Z
published: 2026-07-13T07:53:13Z
canonical: "knowledge.catonetworks.com/generating-api-keys-for-the-cato-api"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating API Keys for the Cato API

There are separate CMA pages for the two types of API keys:

- API Keys - for personal use of individual admins
- Service Keys - for shared use between different service principals

## Overview

Cato lets you generate API keys in the Cato Management Application (CMA) that are used to authenticate API calls to the Cato API server. Enter the API key for an API client, code, scripts, Terraform, SIEM integration, MCP, and more to securely interact with Cato services.

These are the types of API keys:

- **Admin API Keys** are personal keys tied to your admin account, which you use for your own API workflows. You can only create admin API keys for yourself. For more information, see below [Admin API Keys](/v1/docs/generating-api-keys-for-the-cato-api#admin-api-keys).
- **Service API Keys** are shared keys used by system processes, automation, or third-party integrations. These keys are not tied to an individual admin login and are best suited for operational use cases. For more information, see below [Service Principal API Keys](/v1/docs/generating-api-keys-for-the-cato-api#service-principal-api-keys).

Cato provides granular support for two levels of API calls:

- Query APIs - Perform read-only API calls to retrieve data for your account

**Viewer** permissions let you only run query API calls. This applies whether the permissions are assigned through a role or limited to specific CMA pages.
- Configuration APIs - Perform write API calls to make configuration changes to your account

**Edit** permissions let you only run configuration or query API calls. This applies whether the permissions are assigned through a role or limited to specific CMA pages.

### Adding API Keys to an API Client

To authenticate requests to the Cato API, include an HTTP header named x-api-key in your API client. Set the value of this header to your Cato API key using the format: `x-api-key: &lt;api-key&gt;`. For example: `x-api-key: abcdef12345`. This header authorizes your request and grants access to the relevant Cato API endpoints based on the permissions associated with your key.

## Service Principals

A Service Principal is a special type of CMA admin created specifically for API-based workflows. To securely support system integrations and automation processes, create Service Principals for your account. This allows you to generate API keys that are decoupled from personal login credentials and can't be used to access the CMA.

The Service Principal credentials are used exclusively for API authentication with a corresponding service API key. This setup enhances security and enforces the separation of duties for automated operations.

**Note:** A new CMA admin with the name **Automation Service Principal (Editor)** is automatically created as part of adding the Service Principal API key to existing accounts.

**To create a Service Principal:**

1. From the navigation menu, click **Account > Administrators**.
2. Click **New**.

The **Create Administrator** panel opens.
3. Select **Create New**, and **Create as Service Principal**.
4. Enter the **General** settings for the admin.
5. Select the **Role** and any specific sites and users that will define the permissions for this admin. To learn about roles, see [Managing Admin Roles Using RBAC](/v1/docs/managing-admin-roles-using-rbac).

These permissions will be applied to the Service Principal API key.
6. Click **Apply**. The admin is added to the **Administrators** page, and the Service Principal is automatically activated.

## Generating API Keys

The API Keys and Service API Keys pages let you generate and revoke API keys. The **Name** for the API key is only used to identify each key and isn't used as part of the authentication process.

For additional security, you can restrict the source IPs or IP range (CIDR) for API and Service API keys.

**Note:** Make sure that you copy the API key value from the pop-up window. Once you close the pop-up window, you can't access the key value again.

### Admin API Keys

When you need to support your own automation workflows as an individual admin, create an admin API Key that is tied to your CMA admin credentials. You can only create admin API keys for your own use, not for other admins, and only via the CMA.

When an admin is deleted, the associated API key is automatically deactivated. If an admin is disabled, the key is marked as **Disabled**, and API calls using it will return an error.

**RBAC Permissions for Admin API Keys**

- Each admin API key inherits the RBAC permissions and roles of the admin who created it. The permissions update dynamically if the admin’s RBAC roles change, including permissions for specific sites, user groups, groups, etc...
- Admins with the **Viewer** role can see all the API key information (not the actual key value)
- Admins with an **Editor** RBAC role that includes the API Keys page can see the API keys in the account and also revoke (delete) them

![admin_API_Keys.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33341845866781.png)

**To generate an admin API key:**

1. In the navigation menu, click **Resources > Admin API Keys**.
2. Click **New**. The **Create API Key** panel opens.
3. Enter a **Key Name**.
4. To apply view-only permissions for this key, select **Downgrade to View**.
5. **(Optional)** For additional security, in **Allow access from IPs**, select **Specific IP list**, and define the IP addresses or IP range that are allowed to use this API key.

The default setting is to allow this API key for **Any IP** address.
6. **(Optional)** Select a date that the API key **Expires at**.

For API keys with **Edit** permissions, we recommend setting a date that the API key will **Expire at**.
7. Click **Apply**. The API key is added to the page, and a pop-up window containing the value for the new API key is displayed.
8. Click the button to copy the API **Key** that is generated by the CMA and save it to a secure location.

Once you close this window, you can't access the value for the API key.
9. Click **OK** to close the pop-up window.

### Service Principal API Keys

When you need to support shared operational or integration workflows, create a service API Key from the Service API Keys page. These keys are designed for use by automation services and scripts that do not require access to the CMA. They are connected to the Service Principal who created the key.

Service API Keys can be used across systems and teams, enabling scalable integration with external tools and services. These types of keys aren't tied to a CMA admin and are intended for backend operations or continuous delivery pipelines.

**RBAC Permissions for Service API Keys**

- Only admins with the **Editor** role can create or manage service principal API keys
- Each service API Key inherits the RBAC permissions and roles of the Service Principal associated with the key. If the RBAC permissions for the admin change, then the service principal API key is automatically updated with the new permissions.

![service_api_key.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33341993177629.png)

**To generate a service API key:**

1. In the navigation menu, click **Resources > Service API Keys**.
2. Click **New**. The **Create API Key** panel opens.
3. Select the **Service Principal** who is associated with this key.
4. Enter a **Key Name**.
5. To apply view-only permissions for this key, select **Downgrade to View**.
6. **(Optional)** For additional security, in **Allow access from IPs**, select **Specific IP list**, and define the IP addresses or IP range that are allowed to use this API key.

The default setting is to allow this API key for **Any IP** address.
7. **(Optional)** Select a date that the API key **Expires at**.

For API keys with **Edit** permissions, we recommend setting a date that the API key will **Expire at**.
8. Click **Apply**. The API key is added to the page, and a pop-up window containing the value for the new API key is displayed.
9. Click the button to copy the API **Key** that is generated by the CMA and save it to a secure location.

Once you close this window, you can't access the value for the API key.
10. Click **OK** to close the pop-up window.

## Revoking an API Key

You can revoke the API key and remove it from the CMA. Once revoked, the key can't be used to authenticate to the API server.

**To revoke an API key:**

1. In the navigation menu, click **Resources > Admin API Keys** or **Service API Keys**.
2. In the row with the API key, click the delete icon at the end of the row.
3. In the confirmation window, click **Delete**. The API key is revoked and removed from your account.
