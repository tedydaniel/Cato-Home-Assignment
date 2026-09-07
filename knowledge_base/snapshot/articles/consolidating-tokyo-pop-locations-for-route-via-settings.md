---
title: "Consolidating Tokyo PoP Locations for Route Via Settings"
slug: "consolidating-tokyo-pop-locations-for-route-via-settings"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/consolidating-tokyo-pop-locations-for-route-via-settings"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Consolidating Tokyo PoP Locations for Route Via Settings

To improve the Cato service for traffic that uses the Tokyo PoP location, we will change the Cato Management Application setting for the **Route Via** setting in the [Network > Network Rules policy](/v1/docs/configuring-network-rules). Currently, you can egress traffic from the **Tokyo**, **Tokyo_DC2,** and/or **Tokyo_DC3** PoP locations. Starting on April 28, 2024, we are gradually consolidating these PoP locations, and when you select any of the **Tokyo**, **Tokyo_DC2,** and/or **Tokyo_DC3** options for the **Route Via** setting, it will include all the **Tokyo**, **Tokyo_DC2,** and/or **Tokyo_DC3** PoP locations. The other Tokyo PoP locations will be automatically added to the **Route Via** setting.

## What are the Changes for the Route Via Settings?

If you have Network Rules with **Route Via** settings that only include the **Tokyo, Tokyo_DC2**, and/or **Tokyo_DC3** PoP locations, the settings will be changed automatically to include both options. This is an example of a Network Rule with both Tokyo PoP locations:

![Route_via_3PoP.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18256749359901.png)

## What Changes Do I Need to Make to the Network Rules?

You don't need to make any changes to the Network Rules in your account.

Starting from April 28, 2024, for the Route Via settings, you will be able to add the Tokyo option which includes all Tokyo PoP locations.

Note: We are gradually rolling out this feature and it may take a few weeks to be enabled for your specific account.

## What is the Impact on My Account?

There is no impact on your account. You may notice improved connectivity and performance for sites and Clients that use the Route Via settings to egress traffic via the Tokyo PoP locations.

## Who Do I Talk to If I Have Questions?

Please talk to your authorized Cato representative.

## Who Do I Talk to If I Have Technical Issues?

Please contact Support.
