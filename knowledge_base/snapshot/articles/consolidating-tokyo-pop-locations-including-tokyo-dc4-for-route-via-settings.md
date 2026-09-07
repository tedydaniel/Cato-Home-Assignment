---
title: "Consolidating Tokyo PoP Locations (Including Tokyo_DC4) for Route Via Settings"
slug: "consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/consolidating-tokyo-pop-locations-including-tokyo-dc4-for-route-via-settings"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Consolidating Tokyo PoP Locations (Including Tokyo_DC4) for Route Via Settings

We recently introduced a new PoP location Tokyo_DC4. As part of rolling out this new location, we are updating the **Route Via** settings in the Cato Management Application ([Network > Network Rules](/v1/docs/configuring-network-rules)). Today, the policy rule configuration load balances egress traffic via all three Tokyo locations (Tokyo, Tokyo_DC2, and Tokyo_DC3) by default. Starting February 23, 2025, we will add the Tokyo_DC4 location to existing and new **Route Via** rule configurations. Once you select any of the Tokyo locations, it will automatically include all four locations.

## What are the Changes for the Route Via Settings?

If you have Network Rules with **Route Via** settings that only include the **Tokyo**, **Tokyo_DC2**, **Tokyo_DC3** PoP locations, the settings will be changed automatically to include **Tokyo_DC4** PoP as well.

## What Changes Do I Need to Make to the Network Rules?

You don't need to make any changes to the Network Rules in your account.

Starting from February 23, 2025, for the Route Via settings, you will be able to add the Tokyo option which includes all Tokyo PoP locations.

**Note:** We are gradually rolling out this feature and it may take a few weeks to be enabled for your specific account.

## What is the Impact to My Account?

There is no impact on your account. You may notice improved connectivity and performance for sites and Clients that use the **Route Via** settings to egress traffic via the Tokyo PoP locations.

## Who Do I Talk to If I Have Questions?

Please talk to your authorized Cato representative.

## Who Do I Talk to If I Have Technical Issues?

Please contact Cato [Support](https://support.catonetworks.com/hc/en-us/requests/new).
