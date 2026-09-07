---
title: "Configuration API - updateSocketInterface"
slug: "configuration-api-updatesocketinterface"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/configuration-api-updatesocketinterface"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration API - updateSocketInterface

We strongly recommend that before you start using the Cato API, please review the [Support Policy for the Cato API](/v1/docs/support-policy-for-the-cato-api).

## Overview of updateSocketInterface

Use the updateSocketInterface mutation API to update the following Socket interface settings in the **Socket** section for a site in the Cato Management Application (Network > Sites > {site name} > Site Configuration > Socket)

- Destination for the interface
- Name
- LAN interface settings
- Site bandwidth
- WAN interface settings
- Off Cloud (for Cato destination)
- Alt WAN interface settings
- LAG (link aggregation) member
- VRRP type

### Locating the siteID for a Site

The site ID isn't shown in the Cato Management Application, you can locate the site ID:

- Using the entityLookup API query (see [Cato API - EntityLookup](/v1/docs/cato-api-entitylookup)), use the `type` with the value **site**

You can also use the `search` parameter with the value as the name of the site, and the query returns the site ID
- Number in the URL for the Cato Management Application, when you selected a site (Network > Sites > {site name}). For example, the site ID is 12345 for the following URL: https://cc.catonetworks.com/#/26/sites/12345/networkAnalytics

### Understanding the socketInterfaceId Values for a Socket

The `socketInterfaceId` is an enum which contains values for the Cato Sockets. The interface names are shown in the Sockets screen for a site (Network > Sites > {site name} > Site Configuration > Socket) as follows:

- X1500 Socket - Automatic, LAN1, LAN2, WAN1, WAN2, WAN3, USB1, USB2
- X1600 Socket - 1-8, USB1, USB2
- X1700 Socket - INT_1 - INT_12

## Details for the updateSocketInterfaceInput Arguments

These are the arguments for updating the following Socket Interface settings for a site using the Cato configuration API. Only the destType argument is mandatory, otherwise include the arguments for the Socket interface settings that you are updating.

- destType - Destination for the interface
- name - Name of the site
- lan - LAN interface settings
- bandwidth - Site upstream and downstream bandwidth
- wan - WAN interface settings
- offCloud - Settings for **Off Cloud** for interfaces with the destination **Cato**
- altWAN - Settings for interfaces with the destination **Alternative WAN** or **Alternative WAN (Layer-2)**
- lag - For the destination LAN LAG Master, minimum number of links (including master and member) for this link aggregation (LAG)
- vrrp - For Socket high availability (HA) configuration, type of VRRP connection between the Sockets

### updateSocketInterfaceInput destType

The destType is an enum argument, which defines the destination for the interface.

These are the options:

- CATO - WAN traffic for the Cato Cloud
- LAN - Internal LAN behind the Socket
- VRRP_AND_LAN - For Socket HA, the interface is used for LAN and VRRP traffic
- INTERFACE_DISABLED - Interface is disabled and isn't passing traffic
- ALTERNATIVE - WAN traffic not over the Cato Cloud, such as MPLS
- LAYER_2_WAN - **Alternative WAN (Layer-2)** option for a MPLS network with Socket sites on the same subnet
- VRRP - For Socket HA, the interface is used only for VRRP traffic
- LAN_LAG_MASTER_AND_VRRP - For Socket HA and LAN LAG configuration, the interface is the LAN LAG Master and is used for VRRP traffic
- LAN_LAG_MASTER - For LAN LAG configuration, the interface is the LAN LAG Master
- LAN_LAG_MEMBER - For LAN LAG configuration, the interface is a LAN LAG member
- LAN_AND_HA - For vSocket HA in Azure and AWS, the interface is for LAN and HA traffic

### updateSocketInterfaceInput name

The `name` argument is for the name of the Socket interface.

### updateSocketInterfaceInput lan

The `lan` arguments are for the settings for a LAN interface for the Socket.

These are the options:

- subnet - Native range for the LAN interface in CIDR format
- localIP - Local IP address for the LAN network range

### updateSocketInterfaceInput bandwidth

For interfaces that are used for WAN traffic, the `bandwidth` arguments define the upstream and downstream bandwidth for the interface.

These are the options:

- upstreamBandwidth - the maximum upstream bandwidth for this interface
- downstreamBandwidth - the maximum downstream bandwidth for this interface

### updateSocketInterfaceInput wan

The `wan` arguments are for the settings for a WAN interface for the Socket. The WAN roles are generally used for to define traffic in network rules. The precedence is used for failover precedence for a Socket with active and passive interfaces

These are the options:

- role - define the role for the WAN interface: none, automatic, wan_1, wan_2, wan_3
- precedence - define the failover precedence for the interface: ACTIVE, PASSIVE, LAST_RESORT

[LAST_RESORT](/v1/docs/configuring-a-last-resort-link) is the lowest precedence interface

### updateSocketInterfaceInput offCloud

The `offCloud` arguments are for Socket sites that use the [Off-Cloud feature](/v1/docs/routing-traffic-to-an-off-cloud-link) to route traffic over the public Internet instead of over the Cato Cloud.

These are the options:

- enabled - Boolean value, when `true` then Off-Cloud traffic is enabled for the site
- publicIP (optional) - Defines a static public IP address to initiate the connection to the Internet
- publicStaticPort (optional) - Defines a static port number for Off-Cloud traffic

### updateSocketInterfaceInput altWan

The `altWan` arguments are for Socket sites that connect to an Alternative WAN network, such as MPLS. Generally, private IPs and interfaces are used for connecting directly to the MPLS provider.

These are the options:

- privateInterfaceIp - Private IP address for the Socket interface for the traffic
- privateNetwork - Private IP range (with CIDR) for the LAN
- privateGatewayIp - Private IP address for the Alternative WAN gateway (such as MPLS firewall or router)
- privateVlanTag (optional) - VLAN tag for the interface (private IP address)
- publicInterfaceIP (optional) - Public IP address for the Socket interface for the traffic
- publicNetwork (optional) - Public IP range (with CIDR) for the LAN
- publicGatewayIp (optional) - Public IP address for the Alternative WAN gateway (such as MPLS firewall or router)
- publicVlantag (optional) - VLAN tag for the interface (public IP address)

### updateSocketInterfaceInput lag

The `lag` argument is for the master LAN LAG interface and defines the minimum number of interfaces (including master and member) for the LAG for this Socket site.

This is the option:

- minLinks - minimum number of interfaces (links) in the LAG

### updateSocketInterfaceInput vrrp

The `vrrp` enum argument is for Socket HA configurations and defines the type of VRRP connection between the Sockets for the keepalive messages.

These are the options:

- VIA_SWITCH - The VRRP connection is routed via a switch between the Sockets
- DIRECT_LINK - The VRRP connection is routed directly between the Sockets

## Sample Postman Script

### Sample Script - Updating Native Range and Name

This is an example of using the configuration API to change the name of the LAN1 interface to LAN-01, and update the subnet and localIP of the native range for Socket.

```plaintext
mutation updateSocketInterface ($accountId: ID!, $siteId: ID!, $socketInterfaceId: SocketInterfaceIDEnum!, $input: UpdateSocketInterfaceInput!) {
    site(accountId: $accountId) {
        updateSocketInterface (siteId: $siteId, socketInterfaceId: $socketInterfaceId, input: $input) {
            siteId
            socketInterfaceId
        }
    }
}
```

**GraphQL Variables**

```plaintext
{
    "accountId": "26",
    "siteId": 26,
    "socketInterfaceId": "LAN1",
    "input": {
        "name": "LAN-01",
        "destType": "LAN",
        "lan": {
            "subnet": "10.0.0.0/24",
            "localIp": "10.0.0.1"
        }
    }
}
```

### Sample Script - Changing Bandwidth and Name

This is an example of using configuration API to change the bandwidth and name for the WAN interface.

```plaintext
mutation updateSocketInterface ($accountId: ID!, $siteId: ID!, $socketInterfaceId: SocketInterfaceIDEnum!, $input: UpdateSocketInterfaceInput!) {
    site(accountId: $accountId) {
        updateSocketInterface (siteId: $siteId, socketInterfaceId: $socketInterfaceId, input: $input) {
            siteId
            socketInterfaceId
        }
    }
}
```

**GraphQL Variables**

```plaintext
{
    "accountId": "26",
    "siteId": 126,
    "socketInterfaceId": "WAN1",
    "input": {
        "name": "WAN Demo",
        "destType": "CATO",
        "bandwidth": {
            "upstreamBandwidth": 100,
            "downstreamBandwidth": 100
        }
    }
}
```

### Related Resources

- [Using the Cato Site Creation API with Postman (EA)](/v1/docs/using-the-cato-site-creation-api-with-postman)
- [Configuration API Scripts](https://support.catonetworks.com/hc/en-us/articles/8130916998429)
