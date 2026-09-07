---
title: "Cato API - AccountMetrics > Sites > SiteInfo"
slug: "cato-api-accountmetrics-sites-siteinfo"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/cato-api-accountmetrics-sites-siteinfo"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato API - AccountMetrics > Sites > SiteInfo

## AccountMetrics > Sites > SiteInfo

The **AccountMetrics > SiteMetrics > SiteInfo** fields contains general data about sites and not related to performance data.

## SiteInfo Fields

The SiteInfo fields contains data for sites similar to the **Site > General** section in the Cato Management Application. These are the details and fields for the query:

- name - **Name** for the site
- type - site type in the Cato Management Application, such as branch office or datacenter (array with nested fields)
- description - user defined description of the site
- countryCode - code for the **Country** that is the physical location of the site
- region - geographical PoP region that the site is licensed to use
- countryName - **Country** that is the physical location of the site
- isHA - when this boolean value is true, the site is enabled for high availability
- connType - the **Connection Type** field defines how the site connects to the Cato Cloud, such as X1500 Socket or AWS vSocket (array with nested fields)
- creationTime - timestamp for when the site was created
- socketInfo - data related to Socket and vSocket sites, such as serial number and Socket version (array with nested fields)
- ipsecInfo - data related to IPsec sites, such as IKE version (array with nested fields)

## Name

Name of the site in the Cato Management Application.

## Type

Shows the site type that is defined in the Cato Management Application. The values are: Branch, Headquarters, Cloud_DC (datacenter), and datacenter.

## Description

Shows the description for the site that is defined in the Cato Management Application.

## countryCode

The **Country** drop-down menu in the Cato Management Application lets you choose the country that is the physical location of the site.

## isHA

The **isHA** field shows if the site is configured for high availability (HA). When the boolean value is **true**, then HA is enabled for this site.

## connType

The **Connection type** drop-down menu in the Cato Management Application defines how the site connects to the Cato Cloud. The values are:

- SOCKET_X1 - legacy value
- SOCKET_X1500 - X1500 Socket
- VSOCKET_VSH - legacy virtual Socket to connect a public cloud to the Cato Cloud
- VSOCKET_VGS - legacy virtual Socket to connect a public cloud to the Cato Cloud
- VSOCKET_VGX - legacy virtual Socket to connect a public cloud to the Cato Cloud
- GRE_TUNNEL - legacy value (no longer supported)
- IPSEC_HOST - IPsec IKEv1
- IPSEC_CLIENT - legacy firewall initiated IPsec IKEv1
- CROSS_CONNECT_VRF - legacy value
- IPSEC_V2 - IPsec IKEv2
- CROSS_CONNECT_L2 - legacy value
- SOCKET_X1700 - X1700 Socket
- SOCKET_AWS1500 - Virtual Socket for the AWS public cloud
- SOCKET_RPI64 - legacy value
- VSOCKET_VGX_AWS - legacy value
- VSOCKET_VGX_ESX - legacy value
- SOCKET_AZ1500 - Virtual Socket for the Azure public cloud
- SOCKET_ESX1500 - Virtual Socket for VMware ESX
- PORTAL_LISTENER - legacy value
- NOT_DEFINED - **Connection Type** isn't defined for this site

## creationTime

The **creationTime** field shows the timestamp when the site was created in the Cato Management Application.

## sockets

The **socketInfo** field shows data about the Socket, such as version number and serial number. These are the details for the fields:

- id - unique ID for Socket
- serial - serial number for the Socket
- isPrimary - for HA configurations, when this boolean value is true, this is the primary Socket
- platform - Shows Socket type:
  - not_set - no platform set for the Socket
  - VM - legacy value
  - X1 - legacy value
  - X1500 - X1500 Socket
  - NATIVE - legacy value
  - X1500_BR2 - TBD
  - X1700 - X1700 Socket
  - AWS1500 - AWS vSocket
  - RPI64 - legacy value
  - AZ1500 - Azure vSocket
  - ESX1500 - VMware ESX vSocket
- version - software version number that is currently installed on the Socket
- versionUpdateTime - timestamp when the Socket upgraded to the current hardware version

## ipsec

The **ipsec** field shows data about the connection settings for the IPsec site. These are the details for the fields:

- isPrimary - for HA configurations, when this boolean value is true, this the primary IPsec firewall or routing device
- catoIP - The source IP address for the IPsec tunnel in the Cato Cloud
- remoteIP - the destination IP address for the IPsec tunnel (in the site)
- ikeVersion - shows 1 for IKEv1 and 2 for IKEv2
