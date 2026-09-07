---
title: "Supported Socket Transceivers and USB Ethernet Adapters"
slug: "supported-socket-transceivers-and-usb-ethernet-adapters"
updated: 2026-08-27T12:39:37Z
published: 2026-08-27T12:39:37Z
canonical: "knowledge.catonetworks.com/supported-socket-transceivers-and-usb-ethernet-adapters"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Supported Socket Transceivers and USB Ethernet Adapters

These are the supported types of SFP (Small Form-factor Pluggable) transceivers that you can use with X1700 Socket add-on cards and the X1600 Socket. You can mix LR (long-range) and SR (short-range) transceivers in the same Socket.

- SR generally supports up to 25m (or 200-300m for advanced cables)
- LR generally supports up to 10km

For more information, see [Cato Socket Deployment Guides and Data Sheets](/v1/docs/cato-socket-deployment-guides-and-data-sheets).

### Hot-Swap Support and Limitations

Supported SFP modules are hot-swappable when the Socket interface does not need to renegotiate or change the operating speed. If the SFP module or connected device requires the Socket interface to change speeds, for example from 10G to 1G, the Socket must be restarted after inserting the module to establish connectivity. When the Socket port, SFP module, and connected device already use the same interface speed, the module can be hot-swapped.

## X1700 Socket Supported Transceivers

This section lists the supported transceiver types, and the Cato part numbers (P/N) for X1700 add-on cards. Each add-on card includes either 1G or 10G ports. 10G ports do not support 1G SFPs. 1G ports do not support dual-speed SFPs. When more than one P/N is available, you can order either option:

> [!NOTE]
> Caution:
> 
> Using unsupported SFP transceivers may cause unexpected behavior during Socket bootup.

- Supported 1G transceivers:
  - Transceiver 1G LR (P/N FTLF1318P2BTL)
  - Transceiver 1G SR (P/N FTLF8519P3BNL)
- Supported 10G transceivers:
  - Transceiver 10G LR (P/N FTLX1471D3BCL), (P/N FTLX1471D3BCV), and (P/N FTLX1475D3BCV)
  - Transceiver 10G SR (P/N FTLX8574D3BCV)

## X1600 Socket Supported Transceivers

These are the supported types of SFP (Small Form-factor Pluggable) transceivers that you can use with the X1600 Sockets. When more than one P/N is available, you can order either option:

> [!NOTE]
> Caution:
> 
> Using unsupported SFP transceivers may cause unexpected behavior during Socket bootup.

### Socket Ports 1-2

These ports support the following 1G transceivers. They do not support dual speed transceivers.

- Transceiver 1G Multi-Mode SR (P/N FTLF8519P3BNL)
- Transceiver 1G Multi-Mode SR (P/N FTLF8519P2BNL)
- Transceiver 1G Single-Mode LR (P/N FTLF1318P2BTL) and (P/N FTLF1318P3BTL)

### Socket Ports 3-4

These ports support 1G transceivers (see above) and the following 10G transceivers, including dual-speed transceivers. If the SFP module or connected device requires the Socket interface to change between 1G and 10G, restart the Socket after inserting the module to establish connectivity. For more information, see above [Hot-Swap Support and Limitations](/v1/docs/supported-socket-transceivers-and-usb-ethernet-adapters#hotswap-support-and-limitations).

- Transceiver 1G/10G Multi-Mode SR (P/N FTLX8574D3BCV)
- Transceiver 10G Single-Mode LR (P/N FTLX1471D3BCL)
- Transceiver 1G/10G Single-Mode LR (P/N FTLX1471D3BCV)

## X1500 and X1600 Sockets Support USB Ethernet Adapters

You can enable the USB1 and USB2 ports on an X1500 or X1600 Socket to use an Ethernet adapter as a WAN link for the Cato Cloud or as a VRRP link for HA keepalive traffic. This article lists the adapters that are supported by Cato for all X1500 and X1600 Socket models.

> [!NOTE]
> Note:
> 
> Cato recommends that you configure ethernet interfaces as WAN ports. Sockets support up to 3 WAN connections.
> 
> X1700 Sockets with Socket v20 and above support 4 WAN interfaces.

The maximum supported bandwidth for each USB WAN link is 25 Mbps for each direction (upload and download).

- For Socket v14.0 and higher, the following adapters are supported:
  - Buffalo model：LUA4-U3-AGTE-BK
  - Elecom model：EDC-GUA3-B
  - Sanwa Supply model：USB-CVLAN1WN
  - Dell DBJBCBC064 USB 3.0
- For Socket versions v5.0 - v13.x, the following adapter is supported:
  - Dell DBJBCBC064 USB 3.0
