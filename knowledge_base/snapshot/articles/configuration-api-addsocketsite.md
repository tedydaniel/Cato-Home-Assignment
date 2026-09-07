---
title: "Configuration API - addSocketSite"
slug: "configuration-api-addsocketsite"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/configuration-api-addsocketsite"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration API - addSocketSite

We strongly recommend that before you start using the Cato API, please review the [Support Policy for the Cato API](/v1/docs/support-policy-for-the-cato-api).

## Overview of addSocketSite

Use the addSocketSite mutation API to create a new Socket site in your account and define the following settings for the site:

- Name
- Description
- Type
- Connection Type
- Timezone
- Country
- State
- Address
- Native Range

The site is created with default bandwidth settings, 25 Mbps Downstream and 25 Mbps Upstream, and is created without a license assigned to it.

For reseller accounts, you can create separate API keys inside each customer account that you are configuring the settings with the Cato API.

### Locating the accountId for Your Account

This account ID isn't shown in the Cato Management Application, instead it is the number in the URL for the Cato Management Application. For example, the account ID is 26 for the following URL: https://cc.catonetworks.com/#!/26/topology.

Enter this ID in the `accountId` argument for the site creation API, for example:

```plaintext
site(accountId: 26) {
    addSocketSite(input: $addSocketSite) { 
        siteId 
    } 
}
```

## Details for the addSocketSite Arguments

These are the arguments for creating a new Socket site using the Cato configuration API. The arguments are mandatory unless marked as optional:

- name - Name of the site
- connectionType - Physical Socket or vSocket for this site
- siteType - Type of site in your organization, for example Cloud Data Center
- description - (optional) Description of the site
- nativeNetworkRange - IP range for native LAN behind the site, in CIDR format
- siteLocation - Data about the physical location of the site

### AddSocketSite name

Define the name of the Socket site you are creating.

### AddSocketSite connectionType

The `connectionType` is an enum argument that defines the type of physical or virtual Socket for the site.

These are the options:

- SOCKET_X1500 - X1500 or X1500B Socket for a physical site
- SOCKET_X1600 - X1600 Socket for a physical site
- SOCKET_X1700 - X1700 or X1700B Socket for a physical site
- SOCKET_ESX - vSocket for a virtual VMware site
- SOCKET_AWS - vSocket for a virtual AWS site
- SOCKET_AZURE - vSocket for a virtual Azure site

### AddSocketSite siteType

The `siteType` is an enum argument that defines the type of site which determines which icon is used for the site in the Monitoring > Topology screen in the Cato Management Application.

These are the options:

- BRANCH - Physical or virtual sites
- HEADQUARTERS - Physical sites for corporate headquarters
- CLOUD_DC - Virtual sites for cloud-based datacenters
- DATACENTER - Physical sites for datacenters

### AddSocketSite description (Optional)

The `description` is an optional free-text field to describe the site.

### AddSocketSite nativeNetworkRange

Define the IP range for the LAN native range for the site in the `nativeNetworkRange` argument in the IPSubnet format. The native range uses CIDR for the subnet, and /32 CIDR blocks aren't supported.

### AddSocketSite siteLocation

The `siteLocation` arguments define the following physical details for the site. The `countryCode` is relevant to the number of site licenses that are available for a specific **Region** in your account.

You can use the entityLookup API query to retrieve values for these arguments, see [Cato API - EntityLookup](/v1/docs/cato-api-entitylookup).

These are the `siteLocation` arguments:

- countryCode - Two letter code (ISO 3166-1 alpha-2) for the country where the site is located

For entityLookup, use the `type` with the value **country**
- stateCode - (Optional) For the applicable countries, the state where the site is located

For entityLookup, use the `type` with the value **countryState**
- timezone - Time zone for the site, used to set the time frame for the Maintenance Window for Socket and vSocket upgrades

For entityLookup, use the `type` with the value **timezone**
- address - (Optional) Street address for the physical site

## Sample Postman Script

```plaintext
mutation addSocketSite ($accountId: ID!, $input: AddSocketSiteInput!) {
    site(accountId: $accountId) {
        addSocketSite (input: $input) {
            siteId
        }
    }
}
```

**GraphQL Variables**

```plaintext
{
    "accountId": "26",
    "input": {
        "name": "SampleUsSite2",
        "description": "My first API site",
        "siteType": "BRANCH",
        "connectionType": "SOCKET_X1500",
        "nativeNetworkRange": "10.0.0.0/24",
        "siteLocation": {
            "countryCode": "US",
            "timezone": "US/Central",
            "stateCode": "US-AL"
        }
    }
}
```

**Related Resources**

- [Using the Cato Site Creation API with Postman](/v1/docs/using-the-cato-site-creation-api-with-postman)
