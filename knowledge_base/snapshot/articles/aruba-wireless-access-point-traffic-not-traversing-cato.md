---
title: "Aruba Wireless Access Point Traffic Not Traversing Cato"
slug: "aruba-wireless-access-point-traffic-not-traversing-cato"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/aruba-wireless-access-point-traffic-not-traversing-cato"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Aruba Wireless Access Point Traffic Not Traversing Cato

## Challenge

Aruba wireless Access Points (AP) use IPSec to tunnel traffic back to the Headquarter wireless controller.

The APs IPSec traffic is marked with a Do Not Fragment bit, which causes the ICMP Fragmentation Needed message sent from the Cato Socket back to the local AP.

In this case, the AP is not then adjusting the MTU accordingly, and you can see a failure of the communication between the AP and the controller.

## Solution

Check the Aruba deployment and adjust the MTU of the wireless access point according to the MTU of the IPSec tunnel.
