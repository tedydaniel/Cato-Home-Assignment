---
title: "How to run an X1500 Socket using a USB Flash Drive"
slug: "how-to-run-an-x1500-socket-using-a-usb-flash-drive"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/how-to-run-an-x1500-socket-using-a-usb-flash-drive"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to run an X1500 Socket using a USB Flash Drive

## Overview

The X1500 Sockets have an internal SD-Card which is used to hold the Operating System. In the event that an SD card fails, and a spare is not available, it is possible to run the Socket using a USB flash drive while waiting on a replacement.

This article describes the process of preparing, installing, and using a USB flash drive using a Windows desktop.

## Environment

**Required Materials**

- Windows computer with at least one available USB-A port
- [DiskGenius](https://www.diskgenius.com/) or other drive formatting software that supports Ext2
- [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/) or other disk imaging software
- Two USB Flash Drives
  - 8+GB USB flash drive
  - 16+GB USB flash drive
- Phillips screwdriver
- (optional) Serial cable

## Instructions

### Preparing the USB Drives

1. The first required step is to prepare an 8GB+ USB drive with the Socket Image. This will be used in a later step. Please complete the process detailed in the following article:
  - [How to Reset an X1500B Socket (USB Drive)](/v1/docs/how-to-reset-an-x1500b-socket-usb-drive)
  - Once this step has been completed, please move to step 2.
2. The next step is to format your second USB flash drive (16+ GB USB flash) to an Ext2 file type.
  1. Plug the 16+ GB flash drive into the computer.
  2. Run DiskGenius.
  3. Right-click the USB flash drive and select **Quick Partition(F6)**.

![01_DiskGenius.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27401801627549.png)
  4. Under **Partition Count**, select **Custom:** and **1** next to **Partitions**.

![02_DiskGenius.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27401796314525.png)
  5. Click **OK**.
  6. If you get a warning that the USB flash drive already has partitions, click **Yes** to delete the existing partitions.

![03_DiskGenius.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27401801789213.png)
  7. Right-click the new partition under the USB flash drive and select **Format Current Partition(F)**.

![04_DiskGenius.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27401770016541.png)
  8. h. Select **Ext2** for **File System** and click **Format**.

![05_DiskGenius.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27401815270941.png)
  9. Click **Yes** at the prompt.
  10. Right-click the USB flash drive and select **Safely Eject Disk (J)**.
  11. Remove the USB flash drive from your computer and set it aside.

### Preparing the Socket

Now that the USB drives are ready for usage, it is time to prepare the Socket for usage.

1. Unplug the power cable from the Socket.
2. Using a Phillips screwdriver, remove the three screws securing the lid of the Socket to the case. There is one screw on each side of the Socket and one screw on the bottom.

**Bottom screw:**

![06_screw.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27401770135837.jpeg)

**Side screw (x2):**

![07_screw.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27401815446557.jpeg)
3. Remove the lid by sliding it toward the front of the Socket.
4. Locate the SD card next to the fan on the side of the Socket.

![08_sdcard.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27401796695965.jpeg)
5. Slide the metal SD card cover toward the fan to unlock it.
6. Lift the cover and remove the SD card.

![08_remove_sdcard.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27401796778269.jpeg)
7. Lower the cover (without the SD card inserted) and slide it away from the fan to lock it.
8. Slide the lid over the front of the Socket case.
9. Fasten the three screws securing the lid to the case.

### Implementing the USB Flash Drive

Now that the USB drives have been prepared, and the Socket is ready. The next step is implementing the USB flash drive to be used as a host for the Socket Operating System.

1. Plug the 8+ GB USB flash drive into the USB port located on the right, as viewed from the back. This is referred to as **USB2** on newer Sockets.

![09_socket_panel.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27401831345565.png)
2. Plug the 16+ GB USB flash drive into the left USB port as viewed from the back (**USB1** on newer Sockets).
3. (Optional) Connect a serial cable to the Socket’s console port and your computer and use a terminal to monitor the boot sequence. Set the baud rate to 115200.
4. Plug the power cable into the Socket.
5. The Socket will write the X1500 image from the 8 GB USB flash drive to the 16+ GB USB flash drive.
  1. If the process completes successfully, the Socket will automatically power down about one to two minutes after the initial boot.
  2. If a serial cable is connected to the Socket, the following output will display on the terminal when the process completes:

```plaintext
OS install done
[   59.996128] udevd[1874]: starting version 3.2.4
[   60.005390] udevd[1875]: starting eudev-3.2.4
[   63.287620] Starting cron daemon
[   63.295729] OK
[   63.353904] Boot command: x1500_install, exit
[   66.075231] Stopping X1500 socket service
[   66.091761] Stopping cron daemon
[   66.103955] OK
[   66.184215] Done
[   66.206945] Stopping X1500 boot config
[   66.226141] Done
[   69.657242] ACPI: Preparing to enter system sleep state S5
[   69.662978] reboot: Power down
[ 972586] OS install done
```
6. When complete, remove the 8+ GB USB flash drive from the right USB port (USB2).
7. Unplug the power cord from the Socket and plug it back in. The Socket will boot normally from the USB flash drive in the left USB port (USB1).
8. The Socket is now fully functional with the factory-default configuration.

a. If needed, access the Socket UI to configure static WAN IP addresses. Download the [X1500 Socket Hardware Guide](/docs/how-to-run-an-x1500-socket-using-a-usb-flash-drive#) for instructions.

b. If the Socket fails to connect to the Cato Cloud, un-assign the socket from CC2 and assign it again.

**Note:** If you need to repeat this procedure on the same Socket, remove all USB flash drives and power cycle the Socket to clear the memory of the bootable USB before proceeding.
