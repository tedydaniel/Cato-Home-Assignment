---
title: "How to Reset an X1600 Socket (USB Drive)"
slug: "how-to-reset-an-x1600-socket-usb-drive"
updated: 2026-08-27T12:21:40Z
published: 2026-08-27T12:21:40Z
canonical: "knowledge.catonetworks.com/how-to-reset-an-x1600-socket-usb-drive"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Reset an X1600 Socket (USB Drive)

This article explains how to reset an X1600 Socket to the factory image using a USB drive.

## Resetting the Socket to the Factory Default Configuration and Version

This is a high-level overview of the steps to reset a Socket to the factory image using a USB drive.

1. Prepare the image - download and untar it.
2. Burn the image to the USB drive.
3. Install the image on the Socket.

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
2. Move both downloaded files to the same directory, for example `c:\Cato`
3. Untar the image. From an elevated PowerShell prompt in the same directory as both files, run `tar -xf &lt;archive-filename&gt;`

> [!NOTE]
> **Note:**
> 
> Common decompression software (such as WinZip, 7-Zip, or WinRAR) will corrupt the image, resulting in a ~135 MB file. Extracting the file with the Windows CLI tar command should produce a file larger than 1GB.
4. Make sure to place the hash file in the same directory as the image file.
5. Run the following command to compare the file hash of the Socket image:

```powershell
(Get-FileHash -Algorithm SHA256 .\IMAGE_INSTALL_socket_X1600_19524_production_socket_v23.0_20250220_2025_04_27.dd).Hash -eq (gc .\X1600-hash.txt).split()[0]
```

The command returns **True** when the hashes are the same.
6. Download and install disk imager software, such as Win32 Disk Imager.
7. Write the image to the USB drive. (You may need to show all the files with *.* to see the DD file)

**WARNING:** Make sure you write the image on the USB drive and not on your hard disk.

#### Burning the Image with macOS

1. Connect the USB drive.
2. Open a terminal window.
3. Identify the new drive using the command `diskutil list`
4. Unmount the identified drive using `diskutil unmountDisk &lt;diskN&gt;`

<diskN> is a variable which you identify in the previous step, this sample output shows the drive as `disk0`:

```bash
diskutil list
/dev/disk0 (internal, physical)
```
5. Untar the image (double-click the file).
6. Run the following command to compare the file hash of the Socket image:

```bash
shasum -a 256 <archive-filename>
```

Compare the output of this command with the hash attached to this article.
7. Run the following command to write the image file to the USB:

```bash
dd if=.IMAGE_INSTALL_socket_X1600_19524_production_socket_v23.0_20250220_2025_04_27.dd of=/dev/diskN bs=16m
```

**Notes:**
  - For supported versions, you can append `status=progress` to the `dd` command to see the status of the write-to-USB operation.
  - Make sure you write the image on the USB drive and not on your hard disk.

#### Burning the Image with Linux

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
dd if=.IMAGE_INSTALL_socket_X1600_19524_production_socket_v23.0_20250220_2025_04_27.dd of=/dev/sdX
```

**Notes:**
  - For supported versions, you can append `status=progress` to the `dd` command to see the status of the write-to-USB operation.
  - Make sure you write the image on the USB drive and not on your hard disk.

### Installing the Image on the X1600 Socket

After the Socket image is prepared on the USB drive, insert the drive in the Socket. When the Socket boots up, it installs the image and resets to factory default settings.

> [!NOTE]
> Note:
> 
> If the Socket is currently shown in the Cato Management Application as assigned to a site, unassign the Socket from the site (see [Managing Sockets](/v1/docs/managing-sockets)). Then after the new image is installed, you can assign the Socket to the site again.

**To install the image on an X1600 LTE Socket:**

1. Power off the X1600 LTE Socket.
2. Insert the USB flash drive that you prepared [above](/v1/docs/how-to-reset-an-x1600-socket-usb-drive#burning-the-image-to-the-usb-drive) into a USB port in the Socket.
3. Power on the X1600 LTE Socket.
4. Installation starts when the X1600 LTE Socket is booting and generally takes about 5 minutes, depending on the USB drive speed.

During installation, the power LED turns as follows: flashing amber to blue and then to solid amber (process is ready).
5. Once the LED turns to a solid amber state, remove the USB flash drive and unplug the X1600 LTE Socket.

**IMPORTANT!** Disconnect the power cord and then connect it again to power on the X1600 appliance.
6. Plug the Socket back into the outlet.

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

The example below shows the version for an X1500 Socket with Socket version 17.x:

![x1500_sebui_v17.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28559084473885.png)

[X1600-hash.txt](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/X1600-hash.txt)
