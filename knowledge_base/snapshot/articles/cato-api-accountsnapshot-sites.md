---
title: "Cato API - AccountSnapshot > Sites"
slug: "cato-api-accountsnapshot-sites"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/cato-api-accountsnapshot-sites"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato API - AccountSnapshot > Sites

## AccountSnapshot > Sites

The SiteSnapshot field contains data related to one or more sites in the account.

## SiteSnapshot Fields

The SiteSnapshot fields contain data for sites and their links. Use the IDs argument to specify which sites are included in the query.

These are the details that the SiteSnapshot fields can return for the query:

- id - site ID
- connectivityStatus - connectivity to the Cato Cloud (array with nested fields)
- operationalStatus - status for a site or VPN user (array with nested fields)
- lastConnected - timestamp for when the site connected to the PoP
- connectedSince - time that the site is continuously connected to the PoP
- popName - name of the PoP that the site is connected to
- devices - data related to the Sockets for a site (array with nested fields)
- info - general real-time information about the site (array with nested fields)
- hostCount - number of hosts connected to a site

## ID

The ID field shows the unique site internal ID for the account, this value isn't shown in the Cato Management Application.

## connectivityStatus

The Site > connectivityStatus field shows the connectivity for a site:

- **connected** to the Cato Cloud
- **disconnected** from the Cato Cloud

## operationalStatus

The Site > operationalStatus field shows the site status:

- active - passing traffic
- disabled - disabled in the Cato Management Application
- locked - license has expired for this site and you can't configure it
- new - after you create the site before it is connected to the Cato Cloud
- pending_user_configuration - not relevant for sites
- pending_mfa_configuration - not relevant for sites
- pending_code_generation - not relevant for sites

## lastConnected

The lastConnected field shows the timestamp that shows the last time that the site connected to the PoP in the Cato Cloud. This data is generally used for a site that is disconnected from the Cato Cloud.

## connectedSince

The connectedSince field shows the total amount of time that the site is connected to the PoP.

## popName

The popName field shows the name of the PoP that the site is connected to.

## Devices

The DeviceSnapshot field shows contains data related to the Socket for the site (or both Sockets for high availability).

For more about the DeviceSnapshot field for AccountSnapshot, see [Cato API - AccountSnapshot > Sites > Devices](/v1/docs/cato-api-accountsnapshot-sites-devices).

## Info

The SiteInfo fields show real-time data about sites similar to the **Site > General** window in the Cato Management Application. For more about SiteInfo, see the explanation for [Cato API - AccountMetrics > Sites > SiteInfo](/v1/docs/cato-api-accountmetrics-sites-siteinfo).

## hostCount

The hostCount field shows the number of hosts that are currently connected to the site, similar to the Topology window in the Cato Management Application.

## SiteSnapshot IDs Argument

Enter the site IDs for the data that the query returns.
