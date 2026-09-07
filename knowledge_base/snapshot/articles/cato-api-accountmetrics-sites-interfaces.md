---
title: "Cato API - AccountMetrics > Sites > Interfaces"
slug: "cato-api-accountmetrics-sites-interfaces"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/cato-api-accountmetrics-sites-interfaces"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato API - AccountMetrics > Sites > Interfaces

## AccountMetrics > Sites > Interfaces

The AccountMetrics > Sites > Interfaces fields contains data related to the Socket WAN links for a site.

## InterfaceMetrics Fields

The InterfaceMetrics fields contains data for the Socket WAN links. These are the details and fields for the query:

- metrics - traffic data for the link (array with nested fields)
- name - link name in the Cato Management Application
- timeseries - time frame for the data, and defines the relationship between the buckets and the data (array with nested queries and fields)
- annotations - time stamp annotation that shows a time increment for a GUI (array with nested queries and fields)
- periods - object that is a specific time duration (array with nested fields)
- info (SocketInterface) - data related to the link, such as Gateway IP address (array with nested fields)
- remoteIPinfo - data related to the link IP address, such as country code (array with nested fields)
- remoteIP - IP address of the ISP for this link
- socketInfo - data related to Socket and vSocket sites, such as serial number and Socket version (array with nested fields)
- ipsecInfo - data related to IPsec sites, such as IKE version (array with nested fields)
- interfaceInfo - basic configuration information about the Socket interface (array with nested fields)

## Metrics (InterfaceMetrics)

The Metrics field shows the traffic analytics for the WAN links. These are the details for the fields:

- duration - total amount of time for the Socket data
- granularity - duration in seconds for a single metrics bucket
- bytesDownstream - total downstream traffic (from the Cato Cloud to the Socket)
- bytesUpstream - total upstream traffic (from the Socket to the Cato Cloud)
- bytesTotal - total traffic for the Socket
- lostDownstream - number of packets lost for downstream traffic
- lostDownstreamPcnt - percent of packets lost for downstream traffic
- lostUpstream - number of packets lost for upstream traffic
- lostUpstreamPcnt - percent of packets lost for upstream traffic
- packetsDownstream - total downstream packets
- packetsUpstream - total upstream packets
- jitterUptstream - jitter for upstream traffic (difference in time delay in milliseconds (ms) between data packets)
- jitterDownstream - jitter for downstream traffic (difference in time delay in milliseconds (ms) between data packets)
- packetsDiscardedDownstream - total packets discarded for downstream traffic
- packetsDiscardedUpstream - total packets discarded for upstream traffic
- rtt - round-trip time from the Socket to the Cato Cloud

toRate Argument

When the boolean argument toRate is set to **true**, then the data is returned as per second. When the argument is set to false, then the query returns the data over the entire time period.

The toRate argument only applies to types with data in bytes, it doesn't apply to rtt, health, and so on.

## Name

The Name field show the name for the link that is configured in the Cato Management Application (**Configuration > Sites >** Socket **Configuration**).

## Timeseries

The InterfaceMetrics timeseries fields show the metrics for the link according to the specified time-frame (buckets) in the query. Includes historical and near real-time statistics and metrics.

The details for the InterfaceMetrics timeseries fields and arguments are the same as the AccountMetrics timeseries, see [Cato API - AccountMetrics > Timeseries](/v1/docs/cato-api-accountmetrics-timeseries).

## Annotations

The Annotations fields and arguments show specific events according to the time and the event type. These are the details for the fields:

- time - timestamp of the event
- label - description of the event
- shortLabel - brief description of the event
- type - type of event
  - popChange - the site connects to a different PoP
  - roleChange - change for HA status role
  - remoteIPChange - the ISP IP address (remote IP) changed
  - generic - other events that are included in annotations

Annotations Types Argument

Specify the event type that is included in the query: popChange, roleChange, or generic.

## Periods

The Periods fields show the PeriodType metrics for the specified time duration. These are the details for the fields:

- duration - A tuple of two numbers that represent the start and endtime (in ms) according to the index for the starting and ending bucket index
- title - Label that describes the metrics
- type - An enum array that identifies the type of data for this period:
  - packeLoss- packet loss due to a connectivity issue
  - missingData - no available data for the period
  - passiveLink - the link is in standby mode and doesn't pass traffic
  - active - the link is in active load and passes traffic
  - overflowed - some packets were queued and sent after a delay
  - congested - some packets were discarded because they timed out in the queue
  - lastmilePacketLoss - packet loss measured between the Socket and the PoP
  - lastmileLatency - latency measured between the Socket and the PoP
  - generic - something effected the link from an unknown
  - pop - specific PoP that the link is currently connected to

## remoteIPInfo

The remoteIPInfo fields show data that IP address for the link. These are the details for the fields related to the IP address:

- ip - IP address of the link
- countryCode - Geolocation ISO country code
- countryName - Geolocation country name
- city - Geolocation city
- state - Geolocation state
- provider - ISP Internet provider
- latitude - Geolocation latitude for the ISP
- longitude - Geolocation longitude for the ISP

## remoteIP

The remoteIP field shows the IP address of the link, without the extra data from remoteIPInfo.

## socketInfo

The **socketInfo** field shows data about the Socket, such as version number and serial number. These are the details for the fields:

- id - unique ID for Socket
- serial - serial number for the Socket
- isPrimary - for HA configurations, when this boolean value is true, this the primary Socket
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

## ipsecInfo

The **ipsecInfo** field shows data about the connection settings for the IPsec site. These are the details for the fields:

- isPrimary - for HA configurations, when this boolean value is true, this the primary IPsec firewall or routing device
- catoIP - The source IP address for the IPsec tunnel in the Cato Cloud
- remoteIP - the destination IP address for the IPsec tunnel (in the site)
- ikeVersion - shows 1 for IKEv1 and 2 for IKEv2

## interfaceInfo

The interfaceInfo fields contains data related to a Socket ports for a site that are configured in the Cato Management Application (**Configuration > Sites >** Socket **Configuration**). These are the details for the fields:

- id - ID for the Socket port in the Socket WebUI **Monitor** tab
- name - name for the port in the Cato Management Application
- upstreamBandwidth - Maximum allowed bandwidth on this port, for traffic from the site to the Cato Cloud
- downstreamBandwidth - Maximum allowed bandwidth for traffic on this port, from the Cato Cloud to the site
