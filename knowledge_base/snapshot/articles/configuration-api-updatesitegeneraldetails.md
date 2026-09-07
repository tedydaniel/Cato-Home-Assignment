---
title: "Configuration API - updateSiteGeneralDetails"
slug: "configuration-api-updatesitegeneraldetails"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/configuration-api-updatesitegeneraldetails"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration API - updateSiteGeneralDetails

We strongly recommend that before you start using the Cato API, please review the [Support Policy for the Cato API](/v1/docs/support-policy-for-the-cato-api).

## Overview of updateSiteGeneralDetails

Use the updateSiteGeneralDetails mutation API to update the following settings in the **General** section for a site in the Cato Management Application (Network > Sites > {site name} > Site Configuration > General)

- Name
- Description
- Type
- Timezone
- Country
- State
- Address

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

### Locating the siteID for a Site

The site ID isn't shown in the Cato Management Application, you can locate the site ID:

- Using the entityLookup API query (see [Cato API - EntityLookup](/v1/docs/cato-api-entitylookup)), use the `type` with the value **site**

You can also use the `search` parameter with the value as the name of the site, and the query returns the site ID
- Number in the URL for the Cato Management Application, when you selected a site (Network > Sites > {site name}). For example, the site ID is 12345 for the following URL: https://cc.catonetworks.com/#/26/sites/12345/networkAnalytics

## Details for the updateSiteGeneralDetails Arguments

These are the arguments for updating the following General settings for a site using the Cato configuration API. The arguments are mandatory unless marked as optional:

- name - Name of the site
- siteType - Type of site in your organization, for example Cloud Data Center
- description - (optional) Description of the site
- siteLocation - Data about the physical location of the site

### updateSiteGeneralDetails Name

Update the name of the site.

### updateSiteGeneralDetails siteType

The `siteType` is an enum argument that defines the type of site which determines which icon is used for the site in the Monitoring > Topology screen in the Cato Management Application.

These are the options:

- BRANCH - Physical or virtual sites
- HEADQUARTERS - Physical sites for corporate headquarters
- CLOUD_DC - Virtual sites for cloud-based datacenters
- DATACENTER - Physical sites for datacenters

### updateSiteGeneralDetails description (Optional)

The `description` is an optional free-text field to describe the site.

### updateSiteGeneralDetails siteLocation

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
mutation updateSiteGeneralDetails ($accountId: ID!, $siteID: ID!, $input: UpdateSiteGeneralDetailsInput!) {
    site(accountId: $accountId) {
        updateSiteGeneralDetails (siteId: $siteID, input: $input) {
            siteId
        }
    }
}
```

**GraphQL Variables**

```plaintext
{
    "accountId": "",
    "siteID": "",
    "input": {
        "name": "MySite",
        "description": "My first DC using the API",
        "siteType": "DATACENTER",
        "siteLocation": {
            "countryCode": "FR",
            "timezone": "Europe/Paris"
        }
    }
}
```

**Related Resources**

- [Using the Cato Site Creation API with Postman](/v1/docs/using-the-cato-site-creation-api-with-postman)
- [Configuration API Scripts](https://support.catonetworks.com/hc/en-us/articles/8130916998429)
