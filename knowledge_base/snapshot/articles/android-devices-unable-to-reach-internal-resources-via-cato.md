---
title: "Android Devices Unable to Reach Internal Resources Via Cato"
slug: "android-devices-unable-to-reach-internal-resources-via-cato"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/android-devices-unable-to-reach-internal-resources-via-cato"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Android Devices Unable to Reach Internal Resources Via Cato

## Issue

On Android Devices, users aren't able to reach internal resources when connected to Cato

## Environment

- Android v9 and above
- Cato SDP Client regardless of the version
- DNS forwarding configured for internal domains

## The Problem

This issue may be related to Android's private DNS. The feature is enabled by default in version 9 and above and uses a secure channel to connect to the DNS server if the server supports it.

By default, Private DNS is set to "Automatic", which means it uses the network-specified (WiFi adapter) DNS server, and it attempts a DoT (DNS over TLS) connection over port 853 before falling back to UDP-based DNS on port 53.

Cato doesn't intercept DoT queries, DNS forwarding fails, and the user can't reach internal resources or the retrieved DNS results aren't the expected ones.

## The Solution

The following solutions can be implemented:

1. Block **DoH (DNS over HTTP)** and **DNS over TLS** in a [Firewall rule](/v1/docs/managing-the-internet-firewall-policy) to prevent these protocols from being reachable via Cato. This will force Android to switch to UDP-based DNS, allowing DNS forwarding.

[![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19020079119261.png)](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19020079119261.png)
2. The device may still try to reach the network-specified DNS server via UDP/53, to which Cato does not apply DNS forwarding. If that's the case, disable Private DNS on the device. Go to Settings > Network and Internet (or equivalent) on your Android device and turn Private DNS off.
