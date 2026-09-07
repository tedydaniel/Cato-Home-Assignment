---
title: "Configuration API - Adding, Updating, and Removing networkRange"
slug: "configuration-api-adding-updating-and-removing-networkrange"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/configuration-api-adding-updating-and-removing-networkrange"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration API - Adding, Updating, and Removing networkRange

We strongly recommend that before you start using the Cato API, please review the [Support Policy for the Cato API](/v1/docs/support-policy-for-the-cato-api).

This article explains how to use the Cato API to manage network ranges for a site with these commands:

- addNetworkRange
- updateNetworkRange
- removeNetworkRange

## Overview of networkRange

Use the networkRange mutation APIs to add, update, and remove network ranges for a Socket site in your account and define the following settings for the site:

- Network range ID (created automatically for `addNetworkRange`)
- LAN Socket interface ID
- Settings for the network range including: subnet, Local IP or Gateway IP, and VLAN
- For Azure vSocket HA configurations, the Floating IP address
- DHCP settings for the network range

For reseller accounts, you can create separate API keys inside each customer account that you are configuring the settings with the Cato API.

### Locating the accountId for Your Account

The account ID is shown in the Administration> General Info page.

Enter this ID in the `accountId` argument for the site creation API, for example:

```plaintext
site(accountId: 26) {
    addSocketSite(input: $addSocketSite) { 
        siteId 
    } 
}
```

## Details for the addNetworkRange and updateNetworkRange Arguments

The same arguments are used for creating or updating a network range for a Socket site using the Cato configuration API. For addNetworkRange, the arguments are mandatory unless marked as optional. For updateNetworkRange, include the arguments for the Socket interface settings that you are updating.

- networkRangeId - ID for the network range (for updateNetworkRange)
- lanSocketInterfaceId - ID for the network interface that the network range is associated with (for addNetworkRange)
- name - Name of the network range
- rangeType - Type of network range (Routed, Direct, and so on)
- subnet - Native range for the LAN interface in CIDR format
- localIP - Local IP address for the LAN network range
- gateway - For Routed ranges, the next hop IP address for the neighboring router
- vlan - VLAN ID for the network range
- azureFloutingIP - For Azure HA configurations, the next hop IP address for the LAN route table
- dhcpSettings - Defines if this network range uses the default account DHCP settings or customized settings

### networkRangeId (for updateNetworkRange)

The networkRangeId can be retrieved using the [entityLookup](/v1/docs/cato-api-entitylookup) read-only API, use the `type` with the value **siteRange**

You can also use the `search` parameter with the value as the name of the site, and the query filters out ranges from other sites.

### lanSocketInterfaceId (for addNetworkRange)

Use the entityLookup API query to retrieve values for the lanSocketInterfaceId arguments, as follows. For more information, see [Cato API - EntityLookup](/v1/docs/cato-api-entitylookup).

Use the `type` with value **networkInterface**, and the values from these `parent` fields:

- id - <site id>
- name - <name of interface>

See a sample script for the lanSocketInterfaceId below, [Sample Postman Script](/v1/docs/configuration-api-adding-updating-and-removing-networkrange#sample-postman-script).

### networkRange name

The `name` argument is for the name of the network range.

### networkRange rangeType

The `rangeType` is an enum argument that defines the type of network range.

These are the options:

- Routed - Network range that connects to a Socket through a route
- Direct - Network range directly connected to the Socket or firewall (not via a router), but the IP range is different than the site's Native range.
- VLAN - VLANs that connect to Cato are similar to a trunk port
- Native - IP range defined for each LAN interface
- SecondaryNative - For Socket HA configurations, the Native range for the secondary Socket

### networkRange subnet

Define the IP range for the network range for the site in the `subnet` argument in the CIDR IPSubnet format. /31 and /32 CIDR blocks aren't supported.

### networkRange localIP

(Mandatory for these ranges: Native, SocendaryNative, Direct, VLAN) Define the local IP address for the LAN network range in the `localIP` argument.

### networkRange gateway

(Mandatory for Routed ranges) Define the Gateway IP address for the LAN network range in the `gateway` argument.

### networkRange vlan

(Mandatory for VLAN ranges) Define the VLAN ID for the LAN network range in the `vlan` argument.

### networkRange azureFloatingIp

(Mandatory for Azure HA Socket configurations) Define the Floating IP for the LAN network range in the `azureFloatingIp` argument.

### networkRange dhcpSettings (optional)

The `dhcpSettings` is an enum argument that defines the DHCP settings for the network range.

These are the options:

- dhcpType - Configure one of the following DHCP types for the network range:
  - DHCP_RELAY - The network range uses a DHCP relay configured for the account (defined in the `relayGroupId` argument)
  - DHCP_RANGE - The network range uses the Cato DHCP server for DHCP, according to the IP range defined in the `ipRange` argument
  - ACCOUNT_DEFAULT - The network range uses the default DHCP relay defined for the account
  - DHCP_DISABLED - DHCP is disabled for this network range
- ipRange - For the DHCP_Range option above, define the IP range that the Cato DHCP server can assign to hosts
- relayGroupId - Enter the ID for the DHCP Relay Group that this network range uses

For entityLookup, use the `type` with the value **dhcpRelayGroup**

## removeNetworkRange

Use the `removeNetworkRange` API to delete a Network Range from a site. You only need to use the `networkRangeId` with this API.

## Sample Postman Script

### Sample entityLookup for lanSocketInterfaceID

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
        }
    }
}
```

**GraphQL Variables for entityLookup for lanSocketInterfaceID**

```plaintext
{    
"accountID": "26",    
"type": "networkInterface",    
"parent": {
        "id": 26,
        "type": "site"
    }
}
```

### Sample Postman Script to Create New VLAN Range

```plaintext
mutation addNetworkRange ($accountId: ID!, $lanSocketInterfaceId: ID!, $input: AddNetworkRangeInput!) {
    site(accountId: $accountId) {
        addNetworkRange (lanSocketInterfaceId: $lanSocketInterfaceId, input: $input) {
            networkRangeId
        }
    }
}
```

**GraphQL Variable for New VLAN Range**

```plaintext
{
    "accountId": "26",
    "lanSocketInterfaceId": 26,
    "input": {
        "name": "Guest WIFI",
        "rangeType": "VLAN",
        "subnet": "10.1.0.0/24",
        "localIp": "10.1.0.0.1",
        "vlan": 100
    }
}
```

### Related Resources

- [Using the Cato Site Creation API with Postman](/v1/docs/using-the-cato-site-creation-api-with-postman)
- [Configuration API Scripts](https://support.catonetworks.com/hc/en-us/articles/8130916998429)
