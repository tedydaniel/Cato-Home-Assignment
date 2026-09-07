---
title: "Configuring a KVM vSocket Site"
slug: "configuring-a-kvm-vsocket-site"
updated: 2026-08-17T12:19:50Z
published: 2026-08-17T12:19:50Z
canonical: "knowledge.catonetworks.com/configuring-a-kvm-vsocket-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring a KVM vSocket Site

**Note:** This is an Early Availability (EA) feature that is only available for limited release. For more information, contact your Cato Networks representative or send an email to [ea@catonetworks.com](mailto:ea@catonetworks.com).

This article describes how to deploy a vSocket for a data center or universal CPE (uCPE) running Linux KVM (libvirt/QEMU).

The KVM vSocket is distributed as a QCOW2 image and bootstrapped with cloud-init, and it supports High Availability (HA) deployments.

## Preparing to Provision the KVM vSocket

These are the prerequisites to prepare to create the KVM vSocket and connect it to the Cato Cloud:

- Download the QCOW2 image for the KVM vSocket from the Cato Networks repository.
- A Linux KVM host with libvirt/QEMU and UEFI (OVMF) firmware support.
- Internet connectivity for the WAN1 interface on the vSocket.
- Public DNS service must be available for the WAN1 interface on the vSocket.
- A tool to generate a cloud-init seed ISO (for example, `mkisofs` or `genisoimage)`.
- Only attach up to 4 network interfaces (NICs) to the vSocket. Attaching more than 4 NICs may result in issues for the vSocket.
- Use the virtio driver for network and storage interfaces (the supported and default model).

## Creating the KVM vSocket Site

In the Cato Management Application (CMA), create a new site for the KVM vSocket.

After you create the site, the CMA assigns a unique serial number (S/N) to it. We recommend that you copy and paste the serial number into a text file. You need to enter this serial number (including dashes) in the cloud-init configuration when you deploy the KVM VM.

**To create a KVM vSocket site:**

1. From the CMA navigation menu, click **Network > Sites**.
2. Click **New**. The **Add Site** panel opens.
3. Configure the **General** settings for the site:
  1. Enter the **Name** for the site.
  2. Select the **Site Type**. This option determines which icon is used for the site in the **Topology** window.
  3. Select **vSocket KVM** for the **Connection Type**.
  4. Configure the **Country**, **State**, and **Time Zone** to set the time frame for the **Maintenance Window**.
4. Configure the **WAN Interface Settings**, including the **Downstream** and **Upstream** bandwidth according to your ISP bandwidth.
5. Configure the **LAN Interface Settings** with the Native range address for the KVM site. This must be the same as the LAN1 subnet IP range on the KVM host.
6. Click **Apply**. The site is added to the **Sites** list.
  1. From the navigation menu, click **Site Configuration > Socket**. Copy the serial number (S/N) and save it.
  2. You need to enter this serial number in the cloud-init `user-data` file when you deploy the QCOW2 image.

## Best Practices for Deploying a KVM vSocket

- Deploy the vSocket directly from the Cato QCOW2 image to avoid hardware compatibility issues and to ensure all required hardware settings are applied correctly.
- **Keep an untouched copy of the original QCOW2 image. The cloud-init seed ISO runs only on the first boot. If the configuration was not applied correctly, stop the VM, replace the QCOW2 disk with a clean copy of the template, and start it again.**
- Use virtio for both network and disk devices — no NIC emulation is required.
- Make sure to meet the minimum VM requirements documented below.

## Deploying the VM on KVM

You can deploy the KVM vSocket using `virt-manager` (GUI), `virt-install` (CLI), or `virsh` with a domain XML definition. The performance of the KVM vSocket depends on the hardware configuration of the KVM host.

### Minimum Requirements for the vSocket

| Resource | Requirement |
| --- | --- |
| CPU | 2 vCPUs , Haswell-class architecture or newer |
| Memory | 4 GB RAM |
| Storage | 8 GB backing store for the QCOW2 disk (thin — the image starts at ~100 MB and grows with use) |
| Firmware | UEFI (OVMF) boot |
| Network | virtio NICs with 2, 3, or 4 interfaces |
| Image format | QCOW2 |

**Note:** Hardware NIC passthrough (PCI passthrough) and SR-IOV are not supported.

### Step 1 – Prepare the Host Networks

Create the libvirt networks (bridges) that the vSocket interfaces connect to. For example, a NAT-enabled WAN network and a LAN network:

```xml
<!-- wan1.xml: WAN1 with NAT + DHCP -->
<network>
  <name>kvm-wan1</name>
  <bridge name='kvmwan1'/>
  <forward mode='nat'/>
  <ip address='192.168.50.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.50.50' end='192.168.50.200'/>
    </dhcp>
  </ip>
</network>
```

```xml
<!-- lan1.xml: LAN1 -->
<network>
  <name>kvm-lan1</name>
  <bridge name='kvmlan1'/>
  <forward mode='none'/>
</network>
```

Define and start the networks:

```bash
virsh net-define wan1.xml
virsh net-define lan1.xml
virsh net-start kvm-wan1
virsh net-start kvm-lan1
virsh net-autostart kvm-wan1
virsh net-autostart kvm-lan1
```

For an HA deployment, both vSockets' LAN interfaces must share the same broadcast domain (bridge). To connect the vSocket to a physical NIC, use a bridged network attached to the host interface instead of a NAT network.

### Step 2 – Create the cloud-init Seed ISO

The KVM vSocket is bootstrapped with `cloud-init` using a NoCloud seed ISO. Create a directory with one file:

```bash
TMPDIR=$(mktemp -d)
touch $TMPDIR/user-data
```

Populate `user-data` with the site configuration. The file uses a simple TOML (`key = value`) format. The serial number is mandatory; the per-interface network settings are optional (interfaces default to DHCP).

```plaintext
# Mandatory: the serial number from the CMA site (Site Configuration > Socket)
serial = "XXXX-XXXX-XXXX-XXXX"

# Optional per-interface network settings.
# Repeat the [[network]] block for each interface; the name must be unique
# and match the real interface (WAN1, WAN2, LAN1, ...).

[[network]]
name = "WAN1"                       # mandatory
addressing_type = "Static"          # "Static" or "DHCP"
address = "192.168.50.201"          # mandatory if Static
netmask = "255.255.255.0"           # mandatory if Static
default_gw = "192.168.50.1"         # mandatory if Static
primary_dns = "192.168.50.1"        # mandatory if Static
secondary_dns = "8.8.4.4"           # optional

# DHCP is the default, so this block is optional/redundant.
[[network]]
name = "WAN2"
addressing_type = "DHCP"
```

Pack the files into a seed ISO labeled `cidata`:

```bash
pushd $TMPDIR
mkisofs -output seed.iso -volid cidata -joliet -rock user-data
popd
```

Create a separate seed ISO with its own serial number for each vSocket (including each member of an HA pair).

### Step 3 – Deploy the VM

#### Option A — `virt-install` (CLI):

```bash
virt-install \
  --name kvm-vsocket \
  --memory 4096 \
  --vcpus 2 \
  --cpu host-passthrough \
  --boot uefi \
  --disk path=/var/lib/libvirt/images/vsocket.qcow2,bus=virtio,format=qcow2 \
  --disk path=/var/lib/libvirt/images/seed.iso,device=cdrom \
  --network network=kvm-wan1,model=virtio \
  --network network=kvm-lan1,model=virtio \
  --os-variant generic \
  --import --noautoconsole
```

#### Option B — `virsh` (Domain XML)

Define a domain that references the QCOW2 disk, the seed ISO as a CD-ROM, OVMF firmware, and virtio interfaces, then create it:

```bash
virsh define kvm-vsocket.xml
virsh start kvm-vsocket
virsh net-autostart kvm-vsocket
```

Key elements of the domain XML:

```xml
<os>
  <type arch='x86_64' machine='pc-q35-8.0'>hvm</type>
  <loader readonly='yes' type='pflash'>/usr/share/OVMF/OVMF_CODE_4M.fd</loader>
  <nvram template='/usr/share/OVMF/OVMF_VARS_4M.fd'/>
  <boot dev='hd'/>
</os>
...
<disk type='file' device='disk'>
  <driver name='qemu' type='qcow2'/>
  <source file='/var/lib/libvirt/images/vsocket.qcow2'/>
  <target dev='vda' bus='virtio'/>
</disk>
<disk type='file' device='cdrom'>
  <driver name='qemu' type='raw'/>
  <source file='/var/lib/libvirt/images/seed.iso'/>
  <target dev='sdc' bus='sata'/>
  <readonly/>
</disk>
<interface type='network'>
  <source network='kvm-wan1'/>
  <model type='virtio'/>
</interface>
<interface type='network'>
  <source network='kvm-lan1'/>
  <model type='virtio'/>
</interface>
```

Full XML Version:

```xml
<domain type='kvm'>
  <name>CHANGEME_MACHINE_NAME</name>
  <uuid>CHANGEME_UUID</uuid>
  <memory unit='MiB'>4096</memory>
  <vcpu placement='static'>2</vcpu>
  <os>
    <type arch='x86_64' machine='pc-q35-8.0'>hvm</type>
    <!-- OVMF boot firmware -->
    <loader readonly='yes' type='pflash'>/usr/share/OVMF/OVMF_CODE_4M.fd</loader>
    <nvram template='/usr/share/OVMF/OVMF_VARS_4M.fd'/>
    <boot dev='hd'/>
  </os>
  <features>
    <acpi/>
    <apic/>
  </features>
  <cpu mode='host-passthrough' check='partial'>
    <model fallback='forbid'>Haswell</model>
    <feature policy='require' name='vmx'/>
  </cpu>
  <devices>
    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      <source file='CHANGEME_FULL_PATH_TO_THE_QCOW2_IMAGE'/>
      <target dev='vda' bus='virtio'/>
    </disk>
    <!-- Cloud init seed file -->
    <disk type='file' device='cdrom'>
      <driver name='qemu' type='raw'/>
      <source file='CHANGEME_PATH_TO_SEED_DIR_SEE_THE_DOCS/seed.iso'/>
      <target dev='sdc' bus='sata'/>
      <readonly/>
    </disk>
    <!-- Network interfaces -->
    <!-- Mandatory WAN network -->
    <interface type='network'>
      <source network='kvm-wan1'/>
      <model type='virtio'/>
    </interface>
    <!-- Mandatory LAN network -->
    <interface type='network'>
      <source network='kvm-lan1'/>
      <model type='virtio'/>
    </interface>
    <!-- Optional management network -->
    <interface type='network'>
      <source network='kvm-mgmt'/>
      <!-- MAC may be added for DHCP static assignment -->
      <!-- <mac address='52:54:00:b2:0b:02'/> -->
      <model type='virtio'/>
    </interface>
    <!-- Optional WAN2 network -->
    <!-- <interface type='network'> -->
      <!-- <source network='kvm-wan2'/> -->
      <!-- <model type='virtio'/> -->
    <!-- </interface> -->
    <!-- SERIAL console 0 (early boot) -->
    <console type='pty'>
      <target type='serial' port='0'/>
    </console>
    <serial type='pty'>
      <target port='0'/>
    </serial>
  </devices>
</domain>
```

#### Option C — `virt-manager` (GUI)

Import the QCOW2 as an existing disk (virtio bus), add the seed ISO as a CD-ROM device, set firmware to UEFI, attach the virtio networks, then start the VM.

> **Important!** Do not start the VM until everything is configured. The `cloud-init` seed ISO is only read on the first boot.

## Connecting the vSocket to the CMA

The CMA automatically detects the vSocket and uses the serial number (from the `cloud-init` `user-data`) to connect it to the site. To register, the WAN1 interface must have Internet connectivity and access to a public DNS so it can reach the Cato Cloud and the Cato Management Application.

- If WAN1 receives a dynamic IP address via DHCP, the vSocket automatically starts registering to the Cato Cloud.
- If DHCP is not available, configure a static IP address for WAN1 in the `cloud-init` `user-data` (see Step 2).
- By default, the WAN2 interface is disabled and the vSocket uses only WAN1 to register.

## Configuring a Static IP Address on the WAN1 Interface

The way to assign a static WAN1 address on KVM is through the `cloud-init` `user-data` file at first boot (set `addressing_type = "Static"` for the `WAN1` interface, as shown in Step 2).

## High Availability (HA) Deployment

HA behaves like a physical HA pair, using VRRP between the two KVM vSockets.

- Deploy two KVM vSockets, each with its own QCOW2 disk and its own `cloud-init` seed ISO (each with the appropriate serial number for the primary and secondary socket).
- Both LAN interfaces must be on the same broadcast domain (the same LAN bridge/network) so VRRP can operate.
- Add the secondary socket to the site in the Cato Management Application. The two members form the HA pair, exchange health/state, and fail over according to the product HA design.
- HA health and state are visible in the Cato Management Application.

## Changing Socket VM Configuration

You can change some VM settings if the new configuration uses supported values. Restart the Socket VM for the changes to take effect.

The following VM settings can be changed:

- CPU
- Memory
- Networking, such as adding or removing a network interface
