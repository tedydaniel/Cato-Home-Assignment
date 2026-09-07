---
title: "Recovering Failed Add-On Installations on X1700"
slug: "recovering-failed-add-on-installations-on-x1700"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/recovering-failed-add-on-installations-on-x1700"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Recovering Failed Add-On Installations on X1700

## Issue

Add-On cards can be installed on X1700 Sockets to expand the number of interfaces or install fiber links to the device. If the installation process isn't strictly followed as explained in the [X1700 Socket Deployment Guide](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Socket_X1700_Deployment_Guide%20(1).pdf), the device may present the following symptoms:

- Add-On interfaces don't show in the Socket WebUI.
- The number of interfaces in the WebUI does not correspond with the installed Add-On card.
- The physical connections do not correspond with the logical interfaces in the WebUI.

**Note:** You can only install one network card add-on in the X1700 Socket at one time, multiple network cards are NOT supported.

## Environment

- X1700 or X1700B devices with failed installed add-on cards.

## Solution

To recover failed add-on card installations, the Socket must be re-installed following the steps below:

- Unassign the Socket from the site in CMA. See [Managing Sockets](/v1/docs/managing-sockets).
- Power off the Socket and remove the Add-On Card.
- Power on the Socket and perform a Factory Reset using a USB drive as explained in [How to Reset an X1700 Socket](/v1/docs/how-to-reset-an-x1700-socket-usb-drive)
- Perform an initial boot of the Socket with the WAN cable plugged in.
- The Socket will be upgraded to the latest version. Re-assign the Socket to the Site.
- Power off the Socket and install the Add-On Card as explained in the [X1700 Socket Deployment Guide](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/Socket_X1700_Deployment_Guide%20(2).pdf).
- Power on the Socket and configure the Add-On in CMA.
