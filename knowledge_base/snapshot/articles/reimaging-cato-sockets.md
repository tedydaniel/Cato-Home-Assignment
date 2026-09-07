---
title: "Reimaging Cato Sockets"
slug: "reimaging-cato-sockets"
updated: 2026-09-01T09:22:48Z
published: 2026-09-01T09:22:53Z
canonical: "knowledge.catonetworks.com/reimaging-cato-sockets"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reimaging Cato Sockets

This article discusses reimaging Sockets and resetting them to factory default settings.

In some cases, you may need to reimage a Cato Socket using a USB flash drive. Common scenarios that require reimaging are:

1. Storage corruption (the Socket's link LED lights usually fail to illuminate even when the ports are connected).
2. The Socket requires a factory reset.
3. Cato Support tells you the Socket needs to be reimaged.

**Note:** If the Socket is currently shown in the Cato Management Application as assigned to a site, unassign the Socket from the site (see Managing Sockets). Then, after the new image is installed, you can assign the Socket to the site again.

By using the USB image to factory reset the Socket back to the earlier version, the device will return to the complete factory-default configuration. The Socket version will need to be upgraded and settings like the password and static WAN links, will need to be reconfigured on it.

> [!NOTE]
> Important:
> 
> The USB drive should have at least 8GB of storage space available. If you need to format the USB drive, use the exFAT32 format.

Since each Socket hardware model requires a unique image file, you must correctly identify your Socket model. See below for more information on identifying the following socket hardware model types:

- [X1500 Socket models](/v1/docs/overview-of-reimaging-cato-sockets#h_01KTJXFZCRT7R5ETQK9DR7KNPQ)
- [X1700 Socket models](/v1/docs/overview-of-reimaging-cato-sockets#h_01KTJXFZCRQTRS8RY5BXJ78XMN)

## Identifying the Socket Models

Each Socket model uses a unique image for factory reset. This section explains how to distinguish between the different X1500 and X1700 Socket models.

### Identifying the Correct X1500 Socket Model

In May 2022, Cato introduced a second hardware model for the X1500 Socket. The new hardware model is referred to as X1500**B,** and it uses a different image than the X1500 Socket.

There are two ways to identify the X1500B model - the PSU (power supply unit) port on the back panel and the sticker on the underside of the Socket.

- PSU on the back panel (X1500)

![X1500_back_panel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248008602653(1).png)
- PSU on the back panel (X1500B)

![X1500B_Back_Panel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248024598429(1).png)
- Sticker on the underside (X1500B)

![X1500B_Sticker.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248024713245(1).png)

### Identifying the Correct X1700 Socket Model

Cato has 3 certified Socket hardware models for X1700 sites: X1700A, X1700B, and X1700C.

The images below help you identify the different models.

You can identify your model by the layout of the Cato logo and ports on the front panel. Some Sockets also have a sticker on the underside that identifies the model.

- X1700A front panel layout of the Cato logo, and MGMT, COM, USB ports:

![X1700_Orig_Front_Panel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248039861021(1).png)
- X1700B front panel layout of the Cato logo, MGMT, COM, USB ports:

![X1700B_Front_Panel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248056521117(1).png)
- Sticker on the underside (X1700B)

![X1700B_Sticker.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248015320477(1).png)
- X1700C front panel layout of the Cato logo, MGMT, COM, USB ports:

![X1700C front panel port layout.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36669179472157.png)

## Installing the Image on the Socket

Use the links below for more information about installing the image on the appropriate Socket model:

- [How to Reset an X1500 Socket (USB Drive)](/v1/docs/how-to-reset-an-x1500-socket-usb-drive)
- [How to Reset an X1500B Socket (USB Drive)](/v1/docs/how-to-reset-an-x1500b-socket-usb-drive)
- [How to Reset an X1600 Socket (USB Drive)](/v1/docs/how-to-reset-an-x1600-socket-usb-drive)
- [How to Reset an X1700 Socket (USB Drive)](/v1/docs/how-to-reset-an-x1700-socket-usb-drive)
- [How to Reset an X1700B Socket (USB Drive)](/v1/docs/how-to-reset-an-x1700b-socket-usb-drive)
- [How to Reset an X1700C Socket (USB Drive)](/v1/docs/how-to-reset-an-x1700c-socket-usb-drive)
