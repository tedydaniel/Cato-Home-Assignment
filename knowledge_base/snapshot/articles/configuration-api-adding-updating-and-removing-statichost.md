---
title: "Configuration API - Adding, Updating, and Removing staticHost"
slug: "configuration-api-adding-updating-and-removing-statichost"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/configuration-api-adding-updating-and-removing-statichost"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration API - Adding, Updating, and Removing staticHost

We strongly recommend that before you start using the Cato API, please review the [Support Policy for the Cato API](/v1/docs/support-policy-for-the-cato-api).

This article explains how to use the Cato API to manage hosts that are defined for a site with these commands:

- addStaticHost
- updateStaticHost
- removeStaticHost

## Overview of staticHost

Use the staticHost mutation APIs to add, update, and remove hosts for a site in your account and define the following settings for the host:

- Name of the host
- IP address of the host
- MAC address (optional - used for reserving a DHCP IP assignment for the host)

For reseller accounts, you can create separate API keys inside each customer account that you are configuring the settings with the Cato API.

### Locating the siteID for a Site

The site ID isn't shown in the Cato Management Application, you can locate the site ID:

- Using the entityLookup API query (see [Cato API - EntityLookup](/v1/docs/cato-api-entitylookup)), use the `type` with the value **site**

You can also use the `search` parameter with the value as the name of the site, and the query returns the site ID
- Number in the URL for the Cato Management Application, when you selected a site (Network > Sites > {site name}). For example, the site ID is 12345 for the following URL: https://cc.catonetworks.com/#/26/sites/12345/networkAnalytics

## Details for the addStaticHost and updateStaticHost Arguments

The same arguments are used for creating or updating a host behind a site using the Cato configuration API. For `addStaticHost`, the arguments are mandatory unless marked as optional. For `updateStaticHost`, include the arguments for the host settings that you are updating.

- hostId - For `updateStaticHost`, enter the ID for the host you are updating

For `addStaticHost`, this ID is generated when the new host is created
- name - Name of the host behind the site
- ip - IP address of the host behind the site
- macAddress - (optional) MAC address of the host behind the site

The host MAC address is used to for DHCP reservation for hosts with a static IP address

### StaticHost hostId

The `hostId` is the internal Cato ID for the host entity.

The `networkRangeId` can be retrieved using the [entityLookup](/v1/docs/cato-api-entitylookup) read-only API, use the `type` with the value **host**

### StaticHost name

Use the `name` argument to define the name of the host.

### StaticHost ip

Use the `ip` argument to define the IP address of the host.

### StaticHost macAddress (Optional)

Use the `macAddress` argument to define the MAC address of the host for DHCP reservation.

For accounts that use Cato as the DHCP server, the IP address of hosts defined with a MAC address is reserved and can't be assigned to a different host. Make sure that the IP address for the host isn't within the DHCP range for a network segment defined for the site.

## removeStaticHost

Use the `removeStaticHost` API to delete a host that is defined for a site. You only need to use the `hostId` with this API.

## Sample Postman Script

```plaintext
mutation addStaticHost ($accountId: ID!, $siteId: ID!, $input:AddStaticHostInput!) {
    site(accountId: $accountId) {
      addStaticHost(
        siteId: $siteId, 
        input: $input
      ) {
      hostId
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
