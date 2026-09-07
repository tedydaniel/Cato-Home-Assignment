---
title: "Configuring a KVM vSocket in Proxmox VE"
slug: "configuring-a-kvm-vsocket-in-proxmox-ve"
updated: 2026-08-26T15:07:19Z
published: 2026-08-26T15:07:19Z
canonical: "knowledge.catonetworks.com/configuring-a-kvm-vsocket-in-proxmox-ve"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring a KVM vSocket in Proxmox VE

**Note:** This is an Early Availability (EA) feature that is only available for limited release. For more information, contact your Cato Networks representative or send an email to [ea@catonetworks.com](mailto:ea@catonetworks.com).


## Overview

This article describes how to deploy a KVM vSocket on a host that is managed with Proxmox Virtual Environment (Proxmox VE). Proxmox VE uses QEMU/KVM, so the vSocket deployment model is the same as for a standard Linux KVM (libvirt/QEMU) host: the vSocket is distributed as a QCOW2 image and bootstrapped with cloud-init. The difference is the management layer — you create and manage the VM from the Proxmox web UI instead of using `virt-install` or `virsh`.

For the general KVM vSocket requirements, the cloud-init `user-data` settings, and the site creation flow in the Cato Management Application (CMA), see [Configuring a KVM vSocket Site](https://knowledge.catonetworks.com/configuring-a-kvm-vsocket-site).

These are the main stages to deploy a KVM vSocket on Proxmox VE:

1. Create the vSocket site in the CMA and copy the serial number (S/N).
2. Download the QCOW2 image and generate the cloud-init seed ISO.
3. Upload the QCOW2 image and the seed ISO to the Proxmox storage.
4. Create the VM in the Proxmox web UI with UEFI firmware and virtio devices.
5. Add the serial port and the additional network interfaces to the VM.
6. Start the VM and verify that the vSocket connects to the CMA.

## Preparing to Provision the KVM vSocket in Proxmox VE

These are the prerequisites to prepare to create the KVM vSocket and connect it to the Cato Cloud:

- A Proxmox VE host with KVM (hardware virtualization) enabled, and UEFI (OVMF) support for guests.
- The Proxmox host CPU is Haswell-class architecture or newer.
- The QCOW2 image for the KVM vSocket, downloaded from the Cato Networks repository.
- A cloud-init seed ISO, generated in advance with the serial number of the site (see [Create the cloud-init Seed ISO](/v1/docs/configuring-a-kvm-vsocket-in-proxmox-ve#step-2-–-create-the-cloudinit-seed-iso)).
- A tool to generate the seed ISO (for example, `mkisofs` or `genisoimage`).
- Internet connectivity and a public DNS service for the WAN1 interface of the vSocket.
- Proxmox bridges (for example, `vmbr0`) that connect the WAN, LAN, and optional management interfaces to the relevant networks.
- Only attach up to 4 network interfaces (NICs) to the vSocket. Attaching more than 4 NICs may result in issues for the vSocket.

**Note:** Hardware NIC passthrough (PCI passthrough) and SR-IOV are not supported.

### Recommended VM Settings

| Setting | Recommended value |
| --- | --- |
| Machine type | q35 |
| BIOS / Firmware | OVMF (UEFI), without an EFI disk |
| CPU type | host (Haswell-class architecture or newer host CPU) |
| vCPU | 2 or more |
| Memory | 4096 MB or more |
| Primary disk | Imported QCOW2 image, VirtIO Block bus (8 GB thin backing store) |
| Cloud-init media | The seed ISO, attached as a CD-ROM drive |
| NIC model | VirtIO (paravirtualized) |
| NIC count | 2 to 4 interfaces |

## Best Practices for Deploying a KVM vSocket in Proxmox VE

- Deploy the vSocket directly from the Cato QCOW2 image to avoid hardware compatibility issues and to ensure all required hardware settings are applied correctly.
- **Keep an untouched copy of the original QCOW2 image, and import a clean copy of the image for each vSocket VM. The cloud-init seed ISO runs only on the first boot. If the configuration was not applied correctly, it is usually faster to recreate the VM from a clean image than to fix a partially initialized VM.**
- Take a Proxmox snapshot of the VM before the first boot, so that you can roll back to the initial state if the bootstrap configuration is not correct.
- Create a unique seed ISO, with the serial number of the relevant site, for each vSocket VM (including each member of an HA pair).
- Use virtio for both network and disk devices — no NIC emulation is required.
- Do not start the VM until the VM is fully configured. The cloud-init seed ISO is only read on the first boot.

## Creating the KVM vSocket Site

In the CMA, create a new site with the **vSocket KVM** connection type, and then copy the serial number (S/N) from **Site Configuration > Socket**. You need to enter this serial number (including dashes) in the cloud-init `user-data` file.

For the full procedure, see [Configuring a KVM vSocket Site](https://knowledge.catonetworks.com/configuring-a-kvm-vsocket-site).

## Deploying the vSocket VM on Proxmox VE

### Step 1 – Prepare the Proxmox Networks

Make sure that the Proxmox host has a Linux bridge for each interface that you connect to the vSocket:

- **WAN1** – A bridge with Internet connectivity and access to a public DNS service (for example, `vmbr0`). This is a mandatory interface.
- **LAN1** – A bridge for the LAN segment behind the vSocket. This is a mandatory interface.
- **MGMT** (optional) – A bridge for management access to the vSocket.
- **WAN2** (optional) – A bridge for a second WAN link.

You can use a VLAN tag on the network device to separate LAN segments that share the same bridge.

For an HA deployment, the LAN interfaces of both vSockets must be in the same broadcast domain (the same bridge and VLAN).

### Step 2 – Create the cloud-init Seed ISO

The KVM vSocket is bootstrapped with `cloud-init` using a NoCloud seed ISO. Create a directory with one file:

```bash
TMPDIR=$(mktemp -d)
touch $TMPDIR/user-data
```

Populate `user-data` with the site configuration. The file uses a simple TOML (`key = value`) format, and comments are supported. The serial number is mandatory; the per-interface network settings are optional (interfaces default to DHCP).

```plaintext
# Mandatory: the serial number from the CMA site (Site Configuration > Socket)
serial = "XXXX-XXXX-XXXX-XXXX"

# Optional per-interface network settings.
# Repeat the [[network]] block for each interface; the name must be unique
# and match the real interface (WAN1, WAN2, LAN1, ...).

[[network]]
name = "WAN1"                       # mandatory
addressing_type = "Static"          # "Static" or "DHCP"
address = "192.168.50.201"          # mandatory if Static
netmask = "255.255.255.0"           # mandatory if Static
default_gw = "192.168.50.1"         # mandatory if Static
primary_dns = "192.168.50.1"        # mandatory if Static
secondary_dns = "8.8.4.4"           # optional

# DHCP is the default, so this block is optional/redundant.
[[network]]
name = "WAN2"
addressing_type = "DHCP"
```

Pack the file into a seed ISO labeled `cidata`:

```bash
pushd $TMPDIR
mkisofs -output seed.iso -volid cidata -joliet -rock user-data
popd
```

Give the ISO a name that identifies the vSocket VM that uses it (for example, `seed-<site-name>.iso`), so that you can select the correct ISO when you create the VM.

### Step 3 – Upload the Files to the Proxmox Storage

1. Upload the seed ISO to the ISO image storage of the node that hosts the VM (for example, the **local** storage, in the **ISO Images** section).
2. Upload the vSocket QCOW2 image to the **Import** section of a storage on the same node. The storage must have the **Import** content type enabled.

Use a clean copy of the QCOW2 image for each vSocket VM.

> Screenshot placeholder – uploading the seed ISO to the Proxmox storage.

> Screenshot placeholder – uploading or importing the QCOW2 image.

### Step 4 – Create the VM

In the Proxmox web UI, click **Create VM** and configure the tabs of the wizard as follows.

**To create the vSocket VM:**

1. In the **General** tab, select the **Node**, and then enter the **VM ID** and the **Name** for the vSocket VM. Leave the **Add to HA** checkbox cleared (see [High Availability (HA) Deployment](/v1/docs/configuring-a-kvm-vsocket-in-proxmox-ve#high-availability-ha-deployment)).
2. In the **OS** tab:
   1. Select **Use CD/DVD disc image file (iso)**.
   2. For **Storage** and **ISO image**, select the seed ISO that you created for this vSocket.
   3. For **Guest OS**, keep the default values (**Type**: **Linux**, **Version**: **6.x - 2.6 Kernel**).

   > Screenshot placeholder – selecting the cloud-init seed ISO in the OS tab.

3. In the **System** tab:
   1. For **BIOS**, select **OVMF (UEFI)**.
   2. Clear the **Add EFI Disk** checkbox. The vSocket image does not require an EFI disk.
   3. For **Machine**, select **q35**.
   4. Keep the default **SCSI Controller** (**VirtIO SCSI single**).

   > Screenshot placeholder – UEFI firmware selected and Add EFI Disk cleared.

4. In the **Disks** tab:
   1. Delete the default disk (**virtio0**).
   2. Click **Import**, and then select the vSocket QCOW2 image in **Select Image**.
   3. For **Bus/Device**, select **VirtIO Block**, and select the **Target Storage** for the disk.

   > Screenshot placeholder – removing the default disk.

   > Screenshot placeholder – importing the QCOW2 image as the VM disk.

5. In the **CPU** tab, configure at least 2 **Cores**, and select **host** for the **Type**.

   > Screenshot placeholder – CPU cores and the host CPU type.

6. In the **Memory** tab, enter at least **4096** MB.
7. In the **Network** tab, configure the first network device (**net0**). This interface is the WAN1 interface of the vSocket:
   1. For **Bridge**, select the bridge with Internet connectivity.
   2. For **Model**, select **VirtIO (paravirtualized)**.
   3. Optionally, clear the **Firewall** checkbox.
8. In the **Confirm** tab, make sure that **Start after created** is NOT selected, and then click **Finish**.

**Important!** Do not start the VM until it is fully configured. The `cloud-init` seed ISO is only read on the first boot.

### Step 5 – Add the Serial Port and the Remaining Interfaces

After the VM is created, add the remaining hardware from the **Hardware** section of the VM.

**To complete the VM hardware configuration:**

1. Click **Add > Serial Port** and add serial port **0** (`serial0`). The serial port is used for console access to the vSocket.
2. Click **Add > Network Device** and add the LAN1 interface:
   1. For **Bridge**, select the LAN bridge.
   2. For **Model**, select **VirtIO (paravirtualized)**.
   3. Optionally, enter a **VLAN Tag** to separate LAN segments that use the same bridge.
3. Repeat the previous step for each additional interface (management or WAN2), up to a total of 4 interfaces.

The network devices are mapped to the vSocket interfaces according to their order: **net0** is WAN1, **net1** is LAN1, and the following devices are the optional interfaces.

> Screenshot placeholder – adding a serial port.

> Screenshot placeholder – adding an additional network device.

> Screenshot placeholder – the completed hardware list for the vSocket VM.

### Step 6 – (Recommended) Take a Snapshot

Before the first boot, in the **Snapshots** section of the VM, click **Take Snapshot** and create a snapshot of the initial state (for example, `pristine`). If the first-boot configuration is not correct, you can roll back to this snapshot instead of recreating the VM.

> Screenshot placeholder – taking a snapshot of the initial VM state.

### Step 7 – Start the VM

Start the VM. On the first boot, the vSocket reads the configuration from the seed ISO and starts to register to the Cato Cloud.

## Connecting the vSocket to the CMA

The CMA automatically detects the vSocket and uses the serial number (from the `cloud-init` `user-data`) to connect it to the site. To register, the WAN1 interface must have Internet connectivity and access to a public DNS so it can reach the Cato Cloud and the CMA.

- If WAN1 receives a dynamic IP address via DHCP, the vSocket automatically starts registering to the Cato Cloud.
- If DHCP is not available, configure a static IP address for WAN1 in the `cloud-init` `user-data` (see Step 2).
- By default, the WAN2 interface is disabled and the vSocket uses only WAN1 to register.

To follow the boot process and the registration, use the **Console** section of the VM in the Proxmox web UI. The vSocket sends its boot output to the serial console, so to see this output, set **Hardware > Display > Graphic card** to **Serial terminal 0**.

## High Availability (HA) Deployment

HA behaves like a physical HA pair, using VRRP between the two KVM vSockets. This is separate from the Proxmox cluster HA feature (the **Add to HA** option), which restarts a VM on another node and is not used for vSocket HA.

- Deploy two vSocket VMs, each one with its own copy of the QCOW2 image and its own seed ISO (each with the serial number of the primary or the secondary socket).
- The LAN interfaces of both VMs must be in the same broadcast domain (the same bridge and VLAN tag) so that VRRP can operate. If the VMs are on different Proxmox nodes, the LAN bridges must be connected to the same Layer 2 segment.
- Add the secondary socket to the site in the CMA. The two members form the HA pair, exchange health/state, and fail over according to the product HA design.
- HA health and state are visible in the CMA.

## Deploying Additional vSocket VMs

To run more than one vSocket VM on the same Proxmox host or cluster:

- Import a clean copy of the QCOW2 image for each VM.
- Generate a new seed ISO with the serial number of the relevant site.
- Use a unique VM name and VM ID.
- Use separate LAN bridges or VLAN tags where isolation is required.

## Changing the vSocket VM Configuration

You can change some VM settings if the new configuration uses supported values. Restart the vSocket VM for the changes to take effect.

The following VM settings can be changed:

- CPU
- Memory
- Networking, such as adding or removing a network interface

## Troubleshooting

### The VM boots but the vSocket does not register

- Verify that the seed ISO is attached as a CD-ROM.
- Verify that the ISO contains the `user-data` file.
- Verify that the `serial` value matches the serial number of the site in the CMA.
- Verify that WAN1 has Internet access and access to a public DNS service.
- Verify that the first network device (**net0**) is connected to the intended WAN bridge.

### Changes to the cloud-init configuration are ignored

The vSocket bootstrap runs on the first boot only. If you change `user-data` after the VM is initialized, the changes are not applied to the existing boot disk. Roll back to the snapshot of the initial state, or recreate the VM with a clean copy of the QCOW2 image and a new seed ISO.

### There is no console output

- Verify that the serial port (`serial0`) is added to the VM.
- To see the serial output in the web UI console, set **Hardware > Display > Graphic card** to **Serial terminal 0**.

### The network does not behave as expected

- Verify the bridge that each network device is connected to.
- Verify the order of the network devices in the VM configuration (**net0** is WAN1, **net1** is LAN1).
- Verify that the `[[network]]` sections in the `user-data` file use DHCP or static settings as intended.

## Related Articles

- [Configuring a KVM vSocket Site](https://knowledge.catonetworks.com/configuring-a-kvm-vsocket-site)
