---
title: "QoS Policies Explained"
slug: "qos-policies-explained"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/qos-policies-explained"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# QoS Policies Explained

## Introduction

Both WAN and Internet traffic routed to Cato Cloud for processing. Usually, that is fine, but in case of congestion, there's need to make sure that business traffic is processed first (usually WAN). For that purpose, there's Quality of Service (QoS).

QoS is being applied both in the cloud and locally on the Socket according to the configuration. For example, throttling YouTube will be done in the cloud because of the connection established from the cloud. But forcing YouTube to be routed only from WAN2 interface will be applied on the Socket.

QoS policy is defined by the L7 information of the traffic, i.e., by a service like SSH or RDP, application like Facebook or Skype, or by IP subnet or host. Each network flow tagged with a P parameter. P parameter can have a value between 10 and 255. Low P equals significant traffic (processed first).

## Default QoS Policy

For each account the following QoS rules are created by default:

1. P10 - Voice traffic over WAN or Internet.
2. P20 - Remote Desktop (RDP) over WAN or Internet.
3. P30 - File Sharing (SMB) over WAN or Internet.
4. P40 - all remaining WAN traffic (everything that wasn't matched to the previous Ps).
5. P255 - Default - all remaining traffic which is the Internet.

## Configuring QoS Rules

QoS policy is managed from the Networking menu, and it includes two submenus:

- BW Management - this is where you configure the P values. As explained above, the value on its own has no real meaning, only relative to other configured values. In other words, if you want to prioritize Skype over Facebook, just make sure to give Skype traffic lower P value than to Facebook.
- Network Rules - you can find full instructions about it in the online help of the Cato Management Application but in general, this is where you match between the traffic and the P. For each networking rule attached the priority.

## Monitoring and Tracking QoS Policies

In order to review how QoS rules were applied to traffic, go to the Analytics of the site. Then, choose Real-Time and click on QoS. This will detail how QoS rules are being used. Expanding each P will provide additional details.

## Exercise: Limiting Guests WiFi

In the following exercise, we will show how to create a new priority, assign it to a specific network and eventually limit WiFi for guests.

1. Go to BW Management and create two new priorities: P200 and P250. For P250, select Limit when line is congested.
2. Navigate to Network Rules and change the priority in the last rule (Internet traffic) to P200 instead of Default.
3. Assuming you have a few sites with dedicated networks for Guests, combine them all into one group - Guests Networks. Now create a new Internet rule at the top with the following parameters:
  - What (application) - Any.
  - From - Guests Networks group.
  - Priority - P250.
4. That's it! Now navigate to the Analytics of the site and verify the P250 is now in use for Guest network.
