---
title: "Blocking NordVPN"
slug: "blocking-nordvpn"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/blocking-nordvpn"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Blocking NordVPN

## Issue

NordVPN is a personal VPN service known for its ability to bypass firewalls, granting users access to websites that might otherwise be restricted by firewall policies such as those implemented by the Cato Firewall.

Attempts to block NordVPN through conventional means, such as blocking the NordVPN application itself in firewall rules, often prove ineffective, as NordVPN traffic can still find its way through.

## Solution

While NordVPN is notorious for its diverse array of modes, each equipped with unique evasive techniques, configuring specific firewall rules within the Cato Management Application (CMA) can target and neutralize NordVPN traffic.

To mitigate the impact of NordVPN on network security, consider enabling[**TLS inspection**](/v1/docs/configuring-tls-inspection-policy-for-the-account) and blocking the **NordVPN Application** as well as the following specific services commonly utilized by NordVPN to evade detection and restrictions:

- OpenVPN Protocol
- Evasive traffic over tcp/443
- Evasive traffic over DNS
- WireGuard Protocol

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17973444986781.png)
