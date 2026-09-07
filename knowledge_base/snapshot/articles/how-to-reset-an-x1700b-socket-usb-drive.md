---
title: "How to Reset an X1700B Socket (USB Drive)"
slug: "how-to-reset-an-x1700b-socket-usb-drive"
updated: 2026-09-01T09:25:55Z
published: 2026-09-01T09:25:55Z
canonical: "knowledge.catonetworks.com/how-to-reset-an-x1700b-socket-usb-drive"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Reset an X1700B Socket (USB Drive)

This article explains how to reset an X1700B Socket to the factory image using a USB drive.

> [!NOTE]
> **WARNING!**
> 
> Cato has certified Socket hardware models for X1700 sites (X1700, X1700B, X1700C). Make sure that you identify the exact Socket model before installing the image on the Socket.

For more information about various X1700 Socket models, see [Reimaging Cato Sockets](/v1/docs/reimaging-cato-sockets).

## Identifying the USB Ports on the X1700B Socket

The X1700B Socket front panel has two USB ports on the front panel, you can use either port to install an image using a USB drive. As of Socket v17, you can use USB 2.0 or USB 3.0 drives. These are the X1700B Socket front panel USB ports.

![X1700_Front_USB.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28559108264093.png)

## Resetting the Socket to the Factory Default Configuration and Version

This is a high-level overview of the steps to reset a Socket to the factory image using a USB drive.

1. Prepare the image - download and untar it.
2. Burn the image to the USB drive.
3. Install the image on the Socket.

### Resetting the Socket with Add-Ons

For X1700 and X1700B Sockets with add-on modules, you must remove the modules during the entire reimaging process.

After the Socket successfully boots, reinsert the add-on module into the Socket.

### Preparing the Socket Image

1. Download the image file from [here](/v1/docs/socket-and-vsocket-image-files).
2. Untar the image (see instructions below).

After you untar the image, the file is located in the following directory: `live`
3. Get a USB drive with at least 8GB. If you need to format the USB drive, use either exFAT or FAT32. If you use FAT32, the USB drive must be 32 GB or smaller.

### Burning the Image to the USB Drive

This section explains how to burn the Socket image to the USB drive for Windows, macOS, and Linux.

After you untar the image, compare the file hash of the uncompressed DD image file to the Cato verified, correct file hash. This confirms the disk image integrity before writing the Socket firmware to the hard drive.

- A file with the verified hash is attached to this article
- Save the file to the same directory as the uncompressed disk image

#### Burning the Image with Windows

1. Connect the USB drive to your Windows device.
2. Untar the image, from the elevated Powershell in the same directory as both files, run `tar -xf &lt;archive-filename&gt;`

> [!NOTE]
> **Note:**
> 
> Common decompression software (such as WinZip, 7-Zip, or WinRAR) will corrupt the image, resulting in a ~135 MB file. Extracting the file with the Windows CLI tar command should produce a file larger than 1GB.
3. Make sure to place the hash file in the same directory as the image file.
4. Run the following command to compare the file hash of the Socket image:

```powershell
(Get-FileHash -Algorithm SHA256 .\IMAGE_INSTALL_socket_X1700B_19049_production_socket_v21.1_20240919_2025_01_07.dd).Hash -eq (gc .\X1700B-hash.txt).split()[0]
```

The command returns **True** when the hashes are the same.
5. Download and install disk imager software, such as Win32 Disk Imager.
6. Write the image to the USB drive. (You may need to show all the files with *.* to see the DD file)

#### Burning the Image with macOS

1. Connect the USB drive.
2. Open a terminal window.
3. Identify the new drive using the command `diskutil list`
4. Unmount the identified drive using `diskutil unmountDisk &lt;diskN&gt;`
5. Untar the image (double-click the file).
6. Run the following command to compare the file hash of the Socket image:

```bash
shasum -a 256 <archive-filename>
```

Compare the output of this command with the hash attached to this article.
7. Run the following command to write the image to the USB drive:

```bash
dd if=./IMAGE_INSTALL_socket_X1700B_19049_production_socket_v21.1_20240919_2025_01_07.dd of=/dev/diskN bs=16m
```

**Notes:**
  - For supported versions, you can append `status=progress` to the `dd` command to see the status of the write-to-USB operation.
  - Make sure you write the image on the USB drive and not on your hard disk.

### Burning the Image with Linux

1. Connect the USB drive to your Linux machine
2. Identify which device is your USB `/dev/sdb` or `/dev/sdc`
3. Untar the image.
4. Run the following command to view the hash of the image file:

```bash
shasum -a 256 /<path to file>/<image filename>
```
5. Compare the output of the command to the hash attached to this article.
6. Run the following command to write the image to the USB:

```bash
dd if=./IMAGE_INSTALL_socket_X1700B_19049_production_socket_v21.1_20240919_2025_01_07.dd of=/dev/sdX
```

**Notes:**
  - For supported versions, you can append `status=progress` to the `dd` command to see the status of the write-to-USB operation.
  - Make sure you write the image on the USB drive and not on your hard disk.

### Installing the Image on the X1700B Socket

After the Socket image is prepared on the USB drive, insert the drive into the Socket. When the Socket boots up, it installs the image and resets to factory default settings.

> [!NOTE]
> Note:
> 
> If the Socket is currently shown in the Cato Management Application as assigned to a site, unassign the Socket from the site (see [Managing Sockets](/v1/docs/managing-sockets)). Then, after the new image is installed, you can assign the Socket to the site again.

**To install the image on an X1700B Socket:**

1. Power off the X1700B Socket.
2. For Sockets with add-on modules, remove the entire module from the Socket.
3. Insert the USB flash drive that you prepared in section 2 into a USB port.
4. Power on the X1700B Socket.
5. Installation starts upon X1700B boot, it should last approximately 5 minutes, depending on the USB flash drive speed.
6. After installation is completed, the X1700B will power off automatically, so when the Socket powers off, the new image is installed on the Socket.
7. Remove the USB flash drive from the Socket.
8. **IMPORTANT!** Disconnect the power cord, then reconnect it to power on the Socket.
9. For Sockets with add-on modules, do the following:
  1. Make sure that you have upgraded to at least Socket v18.
  2. Power down the Socket, and insert the module.
  3. Power on the X1700B Socket.

### Verifying the Socket Version

After installing the Socket image, you can verify that the process has been successful by using the Socket WebUI to verify the Socket version.

For more about logging in to the Socket WebUI, see [Accessing the Socket WebUI](/v1/docs/accessing-the-socket-webui).

> [!NOTE]
> Note:
> 
> If you log in to the Socket WebUI locally after installing the Socket image, the username and password are reset to their default values.

**To verify the Socket version locally:**

1. Log in to the Socket WebUI.

You can use an Ethernet cable to connect the MGMT port on the Socket to the computer.
2. Navigate to the **About** page.
3. Confirm that the **Version** is the same as the image file you downloaded above.

[X1700B-hash.txt](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/X1700B-hash.txt)
