---
title: "Changing the Interface Role Generates Reconnect Events"
slug: "changing-the-interface-role-generates-reconnect-events"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/changing-the-interface-role-generates-reconnect-events"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Changing the Interface Role Generates Reconnect Events

## Question

I modified the interface role for a Socket WAN port (for example from **Cato** to **disabled**), and then in **Event**, I see reconnect events for all the WAN ports. Why do I see events for ports that I didn't make any changes to?

## Answer

By design, when you change the interface role for a WAN port, all the Socket ports reconnect to the Cato Cloud and the Socket generates an event each time the port reconnects.
