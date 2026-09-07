---
title: "Cato API - AccountSnapshot > Sites > Devices"
slug: "cato-api-accountsnapshot-sites-devices"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/cato-api-accountsnapshot-sites-devices"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato API - AccountSnapshot > Sites > Devices

## AccountSnapshot > Sites > Devices

This articles explains the **SiteSnapshot > Site> Devices** fields and data related to Sockets for a site.

## DeviceSnapshot Fields

The DeviceSnapshot fields contains data for Sockets and their links. The same DeviceSnapshot infrastructure is used for VPN users and for sites, and some of the fields are only relevant to users or sites.

These are the details that the DeviceSnaphsot field can return for the query:

- id - unique internal Cato ID for the Socket
- name - this field is used in SiteSnapshot > Users > Devices
- identifier - this field is used in SiteSnapshot > Users > Devices
- connected - a boolean value that indicates if the site is connected to the Cato Cloud
- haRole - shows if this is the primary or secondary Socket in high availability mode
- interfaces - shows real-time data for the WAN links (outbound traffic) (array with nested queries and fields)
- lastConnected - timestamp for when the Socket connected to the PoP
- lastDuration - total amount of time that the Socket has been connected to the PoP
- lastPopID - the ID of the PoP that the Socket is connected to
- lastPopName - the PoP name that the Socket is connected to
- recentConnections - data related to the most recent completed traffic flows (array with nested queries and fields)
- type - shows the Socket model or vSocket type
- uptimeSeconds - total amount of time that the Socket has been connected to the PoP
- socketInfo - shows data related to the Socket, such as version and serial number
- interfacesLinkState - shows real-time data of all the Socket links (array with nested queries and fields)
- osType - operating system of the Socket
- osVersion - version of the Socket operating system
- version - Socket version
- versionNumber - Socket major version
- releaseGroup - shows the release group for the site
- mfaExpirationTime - this field is used in SiteSnapshot > Users > Devices

## ID

The ID field shows the internal Cato ID for the Socket.

## Connected

The Connected field is a boolean value that shows **true** when the site connected to the Cato Cloud.

## HaRole

The HaRole field shows contains data related to high availability mode for the Socket. The primary Socket is active and the secondary one is passive.

## Interfaces

The Interfaces fields shows data for the WAN interfaces. The field uses an array with nested queries.

For more about the Devices > Interfaces fields for AccountSnapshot, see [Cato API - AccountSnapshot > Sites > Devices > Interfaces](/v1/docs/cato-api-accountsnapshot-sites-devices-interfaces).

## LastConnected

The LastConnected field is for active connections, and shows the timestamp when the Socket initiated the connection to the PoP.

## LastDuration

The LastDuration field shows the total amount of time that the Socket is actively connected to the PoP.

## LastPopID

The Socket is connected to the PoP with this LastPopID.

## LastPopName

Shows the name of the PoP that the Socket is connected to.

## RecentConnections

The Device > RecentConnections field shows data related to the most recent traffic flow. These are the details that this field can return for a query:

- duration - total amount of time for the query data
- interfaceName - Name for the port in the Cato Management Application
- deviceName - Serial number for the Socket
- lastConnected - Shows the time stamp when the flow initiated the connection to the Socket
- popID - The ID of the PoP that the traffic flow was connected to
- popName - The name of the PoP that the traffic flow was connected to
- remoteIP - IP address of the ISP for this link
- remoteIPInfo - IP address, ISP, and geographical information related to this link

## Recent Connections > RemoteIPInfo

The RecentConnections > RemoteIPInfo fields shows data related to the IP address, ISP, and physical location of the PoP that the WAN link is connected to. These are the details for the fields:

- ip - IP address of the WAN connection to the PoP
- countryCode - code for the physical location of the PoP (based on IP address geo-location)
- countryName - country that is the physical location of the PoP (based on IP address geo-location)
- city - city where the PoP is located (based on IP address geo-location)
- state - state where the PoP is located (based on IP address geo-location)
- provider - ISP provider for the last-mile connection between the Cato Cloud and the PoP
- latitude - latitude of the PoP (based on IP address geo-location)
- longitude - longitude of the PoP (based on IP address geo-location)

## Type

The type field shows the model of a physical Socket or the cloud environment for the vSocket. These settings are configured in the Cato Management Application (**Configuration > Site > General**).

## UptimeSeconds

The uptimeSeconds field shows the total time (in seconds) that this Socket is connected to the PoP.

## socketInfo

The **socketInfo** field shows data about the Socket, such as version number and serial number. These are the details for the fields:

- id - unique ID for Socket (shown in Socket WebUI**About > Device id**)
- serial - serial number for the Socket
- isPrimary - for HA configurations, when this boolean value is true, this the primary Socket
- platform - Shows Socket type:
  - not_set - no platform set for the Socket
  - VM - legacy value
  - X1 - legacy value
  - X1500 - X1500 Socket
  - NATIVE - legacy value
  - X1500_BR2 - legacy value
  - X1700 - X1700 Socket
  - AWS1500 - AWS vSocket
  - RPI64 - legacy value
  - AZ1500 - Azure vSocket
  - ESX1500 - VMware ESX vSocket
- version - hardware version number that is currently installed on the Socket
- versionUpdateTime - timestamp when the Socket upgraded to the current hardware version

## InterfaceLinkState

The interfacesLinkState field shows that status of all the ports in the Socket. The data for this query is similar to the **Monitor** tab in the Socket WebUI. These are the details that this field can return for a query:

- ID - the ID for the specific Socket port, for example LAN1 or LAN2
- Up - when this boolean value is true, then the link for the port is up
- MediaIn - when this boolean value is true, then a cable is connected to the Socket port
- LinkSpeed - shows the maximum bandwidth configured for the link
- Duplex - shows the duplex mode for the link

## OsType

The osType field shows the operating system for the Socket.

## OsVersion

The osVersion field shows the operating system version for the Socket.

## Version

The version field shows the Socket that is installed.

## VersionNumber

The versionNumber field shows the major Socket version that is installed.

## ReleaseGroup

The releaseGroup field shows the release group for new Socket versions for this site.
