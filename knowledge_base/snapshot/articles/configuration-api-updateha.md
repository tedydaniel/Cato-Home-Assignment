---
title: "Configuration API - updateHa"
slug: "configuration-api-updateha"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/configuration-api-updateha"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration API - updateHa

We strongly recommend that before you start using the Cato API, please review the [Support Policy for the Cato API](/v1/docs/support-policy-for-the-cato-api).

## Overview of updateHa

Use the `updateHa` mutation API to update the following settings in the **Socket** section for a site with Socket High Availability (HA) configuration in the Cato Management Application (Network > Sites > {site name} > Site Configuration > Socket):

- Management IP address for the primary and secondary Socket
- VRID - ID for VRRP messages that identify when the primary Socket is down, and when it is functional again

> [!NOTE]
> Note:
> 
> You can only run the `updateHa` API after both Sockets are assigned to a site, and it is configured as a Socket HA site using the Cato Management Application.

### Locating the siteID for a Site

The site ID isn't shown in the Cato Management Application, you can locate the site ID:

- Using the entityLookup API query (see [Cato API - EntityLookup](/v1/docs/cato-api-entitylookup)), use the `type` with the value **site**

You can also use the `search` parameter with the value as the name of the site, and the query returns the site ID
- Number in the URL for the Cato Management Application, when you selected a site (Network > Sites > {site name}). For example, the site ID is 12345 for the following URL: https://cc.catonetworks.com/#/26/sites/12345/networkAnalytics

## Details for the updateHa Arguments

These are the arguments for updating the following HA Socket settings for a site using the Cato configuration API. All of the `updateHaInput` arguments are optional:

- primaryManagementIp - Management IP address for the primary Socket
- secondaryManagementIp- Management IP address for the secondary Socket
- VRID - Virtual router identifier for the VRRP messages

### updateHaInput primaryManagementIp

Update the management IP address for the primary Socket. You can use this IP address to access Socket WebUI for the primary Socket.

### updateHaInput secondaryManagementIp

Update the management IP address for the secondary Socket. You can use this IP address to access Socket WebUI for the secondary Socket.

### updateHaInput vrid

Update the VRID (Virtual Router Identifier) for the VRRP messages between the primary and secondary Sockets. The default VRID is 100.

## Sample Postman Script

```plaintext
mutation updateHa ($accountId: ID!, $siteId: ID!, $input: UpdateHaInput!) {
    site(accountId: $accountId) {
        updateHa (siteId: $siteId, input: $input) {
            siteId
        }
    }
}
```

**GraphQL Variables**

```plaintext
{
    "accountId": "26",
    "siteId": 126,
    "input": {
        "primaryManagementIp": "192.168.4.2",
        "secondaryManagementIp": "192.168.4.3",
        "vrid": 100
    }
}
```

**Related Resources**

- [Using the Cato Site Creation API with Postman](/v1/docs/using-the-cato-site-creation-api-with-postman)
- [Configuration API Scripts](https://support.catonetworks.com/hc/en-us/articles/8130916998429)
