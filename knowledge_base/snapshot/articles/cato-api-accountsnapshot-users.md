---
title: "Cato API - AccountSnapshot > Users"
slug: "cato-api-accountsnapshot-users"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/cato-api-accountsnapshot-users"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato API - AccountSnapshot > Users

## AccountSnapshot > Users

The UserSnapshot field contains data related to VPN users in the account. When you run a query for all users in the account (the ID argument is empty), then the API call returns data for users that are currently connected to the VPN and the Cato Cloud.

If you use the ID argument to run a query for specific users, the API call returns data for those users even when they aren't connected to the VPN.

## UserSnapshot Fields

The UserSnapshot fields contain data for connected VPN users and their connections to the Cato Cloud. Use the IDs argument to specify which VPN users are included in the query.

These are the details that the UserSnapshot fields can return for the query:

- id - VPN user ID
- connectivityStatus - connectivity to the Cato Cloud (array with nested fields)
- operationalStatus - status for a site or VPN user (array with nested fields)
- name - name of the VPN user
- deviceName - name of the computer or device
- uptime - how long the Client has been connected to the Cato Cloud (in seconds)
- lastConnected - timestamp for when the VPN user connected to the PoP
- version - Client software version (string)
- versionNumber - Client software version (INT)
- popID - ID of the PoP that the Client is connected to
- popName - name of the PoP that the VPN user is connected to
- RemoteIP - IP address of the Client
- RemoteIPInfo - IP address, ISP, and geographical information related to the Client
- internalIP - IP address of the PoP that the Client is connected to
- osType - operating system of the device the Client is running on
- osVersion - version of the operating system for the device
- devices - data related to the Client (array with nested fields)
- connectedInOffice - shows if the Client is connected to the VPN using Office Mode
- info - general information about the VPN user (array with nested fields)
- recentConnections - data related to the most recent completed VPN connections (array with nested queries and fields)

## ID

Shows the unique VPN user internal ID for the account, this value isn't shown in the Cato Management Application.

## connectivityStatus

The Users > connectivityStatus field shows the connectivity for a VPN user:

- **connected** to the Cato Cloud
- **disconnected** from the Cato Cloud

## operationalStatus

The Users > operationalStatus field shows the VPN user status:

- active - passing traffic
- disabled - disabled in the Cato Management Application
- locked - account for this VPN user is locked
- new - not relevant for VPN users
- pending_user_configuration - waiting for the VPN user to confirm the account
- pending_mfa_configuration - waiting for the VPN user to configure the MFA settings
- pending_code_generation - waiting for the VPN user to enter the registration code

## Name

The name field shows the name of the VPN user in the Cato Management Application.

## DeviceName

The deviceName field shows the name of the computer or device that is connected to the Cato Cloud.

## uptime

The uptime field shows the total amount of time in seconds, that the VPN user is connected to the Cato Cloud.

## lastConnected

For a VPN user that isn't connected to the Cato Cloud, the lastConnected field shows the time stamp for the last time the Client connected to the Cato Cloud.

## version

The version field shows the version of the Client as the type STRING.

## versionNumber

The versionNumber field shows the version of the Client as the type INT.

## PopID

The Users > PoPID field shows the ID of the PoP that the Client is connected to.

## PopName

The Users > PoPName field shows the name of the PoP that the Client is connected to.

## RemoteIP

The Users > RemoteIP field shows the IP address of the Client.

## RemoteIPInfo

The Users > RemoteIPInfo fields shows data related to the IP address, ISP, and physical location of the PoP that the Client is connected to. These are the details for the fields:

- ip - IP address of the WAN connection to the PoP
- countryCode - code for the physical location of the PoP (based on IP address geo-location)
- countryName - country that is the physical location of the PoP (based on IP address geo-location)
- city - city where the PoP is located (based on IP address geo-location)
- state - state where the PoP is located (based on IP address geo-location)
- provider - ISP provider for the last-mile connection between the Cato Cloud and the PoP
- latitude - latitude of the PoP (based on IP address geo-location)
- longitude - longitude of the PoP (based on IP address geo-location)

## InternalIP

The Users > internalIP field shows the IP address of the PoP that the Client is connected to.

## osType

The osType field shows the operating system of the device that the Client is installed on.

## osVersion

The osVersion field shows the operating system version of the device that the Client is installed on.

## Devices

The Users > DeviceSnapshot fields show metrics and data of the device that is connected to the Cato Cloud. Some fields in DeviceSnapshot are repeated to give you greater flexibility with the data. Also, the same DeviceSnapshot infrastructure is used for VPN users and for sites, and some of the fields are only relevant to users or sites.

This is the data that you can see:

- id - unique internal Cato ID for the device
- name - name of the device
- identifier - unique identifier for the device
- connected - a boolean value that indicates if the Client is connected to the Cato Cloud
- haRole - this field is used in SiteSnapshot > Site> Devices
- interfaces - shows real-time data for the Client (array with nested queries and fields)

For more about the Interfaces fields for DeviceSnapshot, see [Cato API - AccountSnapshot > Sites > Devices > Interfaces](/v1/docs/cato-api-accountsnapshot-sites-devices-interfaces).
- lastConnected - timestamp for when the Client connected to the Cato Cloud
- lastDuration - total amount of time that the Client has been connected to the Cato Cloud
- connectedSince - shows the timestamp for how long the Client is actively connected to the Cato Cloud
- lastPopName - the PoP name that the Client is connected to
- lastPopID - the ID of the PoP that the Client is connected to
- recentConnections - data related to the most recent completed traffic flows (array with nested queries and fields)

For more about the recentConnections fields for DeviceSnapshot, see [Cato API - AccountSnapshot > Sites > Devices](/v1/docs/cato-api-accountsnapshot-sites-devices).
- type - shows the device type
- uptimeSeconds - shows the number of seconds that this Client has been active
- socketInfo - this field is used in SiteSnapshot > Site> Devices
- interfacesLinkState - this field is used in SiteSnapshot > Site> Devices
- osType - operating system of the device the Client is running on
- osVersion - version of the operating system for the device
- version - Client software version, for example 4.4.1234 (string)
- versionNumber - Client major software version, for example 4 (INT)
- releaseGroup - shows the release status for the Client, such as GA or EA
- mfaExpirationTime - Shows the amount of time remaining before the MFA token expires

## connectedInOffice

The connectedInOffice field is a boolean value, and when it is **true**, it shows that the Client is connected to the network using Office Mode.

## Info

The UserInfo fields show basic information about the VPN user, in a concise branch. These are the details for the fields:

- name - name of the VPN user
- status - status of the Client as the type STRING
- email - email address of the VPN user
- creationTime - timestamp when the VPN user was created in the account
- phoneNumber - phone number for the VPN user
- origin - shows how the VPN user was added to the account:
  - regular - manually added in the Cato Management Application
  - LDAP - added with LDAP sync
- authMethod - Multi Factor Authentication (MFA) settings for this VPN user:
  - None - the VPN user doesn't require MFA to authenticate to the Client
  - MFA - the VPN user requires MFA to authenticate to the Client

## RecentConnections

The Users > RecentConnections field shows data related to the most recent Client connections to the Cato Cloud. These are the details that this field can return for a query:

- duration - total amount of time for the query data
- interfaceName - Name for the port in the Cato Management Application
- deviceName - Name of the device the Client is installed on
- lastConnected - Shows the time stamp when the Client initiated the connection to the Cato Cloud
- popID - The ID of the PoP that the Client was connected to
- popName - The name of the PoP that the Client was connected to
- remoteIP - IP address of the Client
- remoteIPInfo - IP address, ISP, and geographical information related to the PoP that the traffic flow was connected to

## Snapshot > Users IDs Argument

Enter the VPN user IDs for the data that the query returns. When this argument is empty, the query returns all the VPN users for connected to the Cato Cloud.
