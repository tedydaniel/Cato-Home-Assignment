---
title: "Migrating Network Range Tokyo DC2 - DC4"
slug: "migrating-network-range-tokyo-dc2-dc4"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/migrating-network-range-tokyo-dc2-dc4"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrating Network Range Tokyo DC2 - DC4

We recently introduced a new Tokyo_DC4 PoP location. As part of rolling out this new location, we are migrating the 150.195.219.0/24 range from Tokyo_DC2 to Tokyo_DC4. Starting February 23, 2025, we will gradually activate the Tokyo_DC4 location to existing traffic.

For Network Rules ([Network > Network Rules](/v1/docs/configuring-network-rules)) that are set to **Route Via** the PoP Location **Tokyo_DC2**, we will migrate them to use the **Tokyo_DC4** PoP Location instead.

## What Changes Do I Need to Make to the Network Rules?

You don't need to make any changes to the Network Rules in your account.

Starting from Feb 23, 2025, for Network Rules that are set to **Route Via** the PoP Location **Tokyo_DC2**, we will migrate them to use the **Tokyo_DC4** PoP Location instead.

**Note:** We are gradually rolling out this feature and it may take a few weeks to be enabled for your specific account.

## What is the Impact to My Account?

There is no impact on your account. You may notice improved connectivity and performance for sites and Clients that use the **Route Via** settings to egress traffic via the Tokyo PoP locations.

## Who Do I Talk to If I Have Questions?

Please talk to your authorized Cato representative.

## Who Do I Talk to If I Have Technical Issues?

Please contact Cato [Support](https://support.catonetworks.com/hc/en-us/requests/new).
