---
title: "Cato API - AccountSnapshot"
slug: "cato-api-accountsnapshot"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/cato-api-accountsnapshot"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato API - AccountSnapshot

We strongly recommend that before you start using the Cato API, please review the [Support Policy for the Cato API](/v1/docs/support-policy-for-the-cato-api).

## Overview of AccountSnapshot

Current snapshot based metrics that show near real‑time data for the account. Provides analytics that are similar to the Topology page for the account.

For reseller accounts, you can create separate API keys inside each customer account that you are connecting to the Cato API. For more about rate limiting and the accountSnapshot API query, see [Understanding Cato API Rate Limiting](/v1/docs/understanding-cato-api-rate-limiting).

## Details for the AccountSnapshot Fields

These are the details that the AccountSnapshot fields can return for the query:

- ID - account ID
- sites -data that is returned for each site (array with nested queries and fields)
- users - data that is returned for VPN users that are connected to the Cato Cloud
- timestamp - amount of time (in milliseconds) from the epoch (1.1.1970)

## AccountSnapshot ID

Shows the unique account internal ID.

This account ID isn't shown in the Cato Management Application, instead it is the number in the URL for the Cato Management Application. For example, the account ID is 26 for the following URL: https://cc2.catonetworks.com/#!/**26**/topology.

## AccountSnapshot Sites

The Sites field contains data related to one or more sites in the account. You can also specify data for VPN users with their user IDs.

For more about Sites field for AccountSnapshot, see [Cato API - AccountSnapshot > Sites](/v1/docs/cato-api-accountsnapshot-sites).

## AccountSnapshot Timestamp

Shows the timestamp for the metrics that are returned for the query based on the amount of time since the epoch.

## Arguments for the AccountSnapshot

These are the arguments that you can pass and define the data that is returned by the query:

- accountID - account ID
- ID - account ID (legacy argument)

## AccountSnapshot accountID Argument

Enter the account ID for the data that the query returns. This argument is mandatory.
