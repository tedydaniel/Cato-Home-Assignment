---
title: "Cato API - AccountSnapshot > Sites > Devices > Interfaces"
slug: "cato-api-accountsnapshot-sites-devices-interfaces"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/cato-api-accountsnapshot-sites-devices-interfaces"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato API - AccountSnapshot > Sites > Devices > Interfaces

## AccountSnapshot > Sites > Devices > Interfaces

The SiteSnapshot > Sites > Devices >Interfaces fields contains data related to the Socket WAN links for a site.

## InterfaceSnapshot Fields

The InterfaceSnapshot fields contains data for the Socket WAN links.

These are the details that the InterfaceDevices field can return for the query:

- connected - shows if the WAN link is connected to the PoP
- ID - interface ID for the WAN link
- name - WAN link name in the Cato Management Application
- physicalport - physical WAN port on the Socket
- popID - the ID of the PoP that the WAN link is connected to (deprecated - use popName instead)
- popName - the name of the PoP that the WAN link is connected to
- previousPopID - the ID of the PoP that the WAN link was connected to before the current one
- previousPopName - the name of the PoP that the WAN link was connected to before the current one
- tunnelConnectionReason - reason that the tunnel required a new connection (for example, PoP or Socket restarted)
- tunnelUptime - number of seconds that the tunnel is connected to a PoP
- tunnelRemoteIP - IP address of the WAN ISP
- tunnelRemoteIPInfo - IP address, ISP, and geographical information related to the WAN ISP
- type - this field is for future use
- info - data about the WAN link that is configured in the **Socket Configuration** window for the site

## ID

The ID field shows the ID or name for the for a Socket WAN port.

## Connected

The connected field is a boolean value that shows if the link has connectivity to the PoP.

## Name

The Name field shows the name of the WAN link in the Cato Management Application (**Configuration > Sites > Socket Configuration**).

## physicalport

The physicalport field shows the name for the physical WAN port on the Socket, for example WAN1 or WAN2.

## popID (deprecated - use popName instead)

The PoPID field shows the ID of the PoP that the WAN link is currently connected to.

## previousPopID

The previousPopID field shows the ID of the PoP that the WAN link was connected to before the current one.

## previousPopName

The previousPopName field shows the name of the PoP that the WAN link was connected to before the current one.

## tunnelConnectionReason

The tunnelConnectionReason field shows the reason that the tunnel required a new connection (for example, PoP or Socket restarted).

## tunnelUptime

The tunnelUptime field shows the total number of seconds that the tunnel for the WAN link is currently connected to a PoP.

## tunnelRemoteIP

The tunnelRemoteIP field shows the IP address of the PoP that the WAN link is connected to.

## tunnelRemoteIPInfo

The tunnelRemoteIPInfo fields shows data related to the IP address, ISP, and physical location of the PoP that the WAN link is connected to. These are the details for the fields:

- ip - IP address of the WAN connection to the PoP
- countryCode - code for the physical location of the PoP (based on IP address geo-location)
- countryName - country that is the physical location of the PoP (based on IP address geo-location)
- city - city where the PoP is located (based on IP address geo-location)
- state - state where the PoP is located (based on IP address geo-location)
- provider - ISP provider for the last-mile connection between the Cato Cloud and the PoP
- latitude - latitude of the PoP (based on IP address geo-location)
- longitude - longitude of the PoP (based on IP address geo-location)

## type

This field is for future use.

## info

The InterfaceInfo field shows the name and bandwidth settings for the Socket port which are configured in the **Socket Configuration** window for the site. These are the details for the fields:

- id - the inteface ID for the WAN link
- name - name of the port
- upstreamBandwidth - the maximum upstream bandwidth for this link
- downstreamBandwidth - the maximum downstream bandwidth for this link
