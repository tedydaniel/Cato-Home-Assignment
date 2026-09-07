---
title: "MAC Address of SDP Clients"
slug: "mac-address-of-sdp-clients"
updated: 2026-06-22T09:24:59Z
published: 2026-06-22T09:24:59Z
canonical: "knowledge.catonetworks.com/mac-address-of-sdp-clients"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# MAC Address of SDP Clients

This article provides details of the MAC addresses of SDP Clients.

## Summary

The following table shows a summary of the MAC addresses of SPD Clients.

| Platform | Version | Type of Interface | Layer 3 Only? | L2 |
| --- | --- | --- | --- | --- |
| Windows | >5.4 | WinTUN | Yes | N/A |
| macOS | >5 | utun | Yes | N/A |
| iOS | >5 | utun | Yes | N/A |
| Android | >5 | TUN | Yes | N/A |
| Linux | >5 | TUN | Yes | N/A |

## Use Case

A remote SDP client connects to the private network and joins the domain. To enhance security, a server has been configured to exclusively permit connections from a MAC and IP addresses within the private network.

## Windows SDP Client

The Windows SDP client uses WinTUN, a type of TUN driver. Wintun is a very simple and minimal TUN driver for the Windows kernel, which provides userspace programs with a simple network adapter for reading and writing packets.

### What is TUN?

TUN interfaces are software-only interfaces, meaning that they exist only in the kernel, and, unlike regular network interfaces, they have no physical hardware component. TUN is a type of kernel virtual network device that simulates a network layer device and operates at layer 3, carrying IP packets. A TUN interface outputs (and must be given) raw IP packets, and no ethernet headers are added by the kernel.

After setting up a TUN interface, it can be utilized similarly to any other network interface. This implies that IP addresses can be allocated to it, its traffic can be inspected, firewall regulations can be configured, and routes pointing to it can be established.

## macOS and iOS SDP Clients

The macOS and iOS SDP clients use the utun device driver.

### What is utun?

macOS and iOS include a built-in utun device driver for the TUN interface.

## Android and Linux SDP Clients

The Android and Linux SDP clients both use the TUN device driver.
