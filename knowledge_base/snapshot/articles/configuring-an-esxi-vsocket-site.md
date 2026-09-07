---
title: "Configuring an ESXi vSocket Site"
slug: "configuring-an-esxi-vsocket-site"
updated: 2026-08-06T09:54:08Z
published: 2026-08-06T09:54:08Z
canonical: "knowledge.catonetworks.com/configuring-an-esxi-vsocket-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring an ESXi vSocket Site

This article describes how to deploy a vSocket for a data center or universal CPE (uCPE) running VMware ESXi.

## Preparing to Provision the ESXi vSocket

These are the prerequisites to prepare to create the VMware ESXi vSocket and connect it to the Cato Cloud:

- Download the OVA image for the ESXi vSocket from the Cato Networks repository, see [Socket and vSocket Image Files](/v1/docs/socket-and-vsocket-image-files)
- Internet connectivity for the WAN1 interface on the vSocket
- Public DNS service must be available for the WAN1 interface on the vSocket
- Only attach 4 network interfaces (NICs) to the vSocket. Attaching more than 4 NICs may result in issues for the vSocket

## Creating the ESXi vSocket Site

In the Cato Management Application, create a new site for the ESXi vSocket.

After you create the site, the Cato Management Application assigns a unique serial number (S/N) to it. We recommend that you copy and paste the serial number in a text file.

You need to enter this serial number (including dashes) for the **Customize template** window in vSphere when you create the ESXi VM.

**To create an ESXi vSocket site:**

1. From the Cato Management Application's navigation menu, click **Network > Sites**.
2. Click **New**. The **Add Site** panel opens.

![esxNewSite.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247841632157.png)
3. Configure the **General** settings for the site:
  1. Enter the **Name** for the site.
  2. Select the **Site Type**. This option determines which icon is used for the site in the **Topology** window.
  3. Select **vSocket ESXi** for the **Connection Type**.
  4. Configure the **Country**, **State**, and **Time Zone** to set the time frame for the **Maintenance Window**.
4. Configure the **WAN Interface Settings**, including the **Downstream** and **Upstream** bandwidth according to your ISP bandwidth.
5. Configure the LAN Interface Settings with the Native range address for the ESXi site. This must be the same as the LAN1 subnet IP range in ESXi.
6. Click **Apply**. The site is added to the **Sites** list.
  1. Copy and save the vSocket serial number for the vSocket configuration script.

You need to enter this serial number when you deploy the ESXi OVA file.
  2. From the navigation menu, click **Site Configuration > Socket**. Copy the serial number (S/N) and save it.

## Best Practices for Deploying an ESXi vSocket

- When you deploy an ESXi vSocket, we recommend creating the VM directly from the OVA file in vSphere, instead of creating a VM first and then attaching the OVA file to it. Deploying directly from the OVA file ensures that all necessary hardware settings are correctly applied and helps avoid potential hardware compatibility issues.

If you have already deployed and need to add memory, you can do so without having to redeploy your vSocket.
- Make sure to meet the VM vSocket minimum requirements for both vSphere and VM resources, as documented [below](/v1/docs/configuring-an-esxi-vsocket-site#minimum-requirements-for-the-vsocket).

## Deploying the VM in ESXi

In vSphere, deploy a new VM for the vSocket based on the Cato OVA template. The performance of the ESXi vSocket depends on the hardware configuration of the ESXi host.

### Minimum Requirements for the vSocket

These are the minimum requirements for the VM vSocket:

- vSphere requirements:
  - Minimum ESXi version - ESXi 8.0
  - Image format - OVA
- Required VM resources:
  - 2 vCPUs
  - 4 GB RAM
  - At least 7 GB HDD

### Deploying the VM

Deploy the vSocket template to a VM in vSphere and configure the settings for the vSocket interfaces.

**To deploy the vSocket to a VM:**

1. Right-click the ESXi host or folder and select **Deploy OVF Template**.
2. In the **Select an OVF template window**, select **Local file** and click **Choose Files**.
3. Select the OVA file with the vSocket image. Click **Next**.
4. In the **Select a name and folder window**, enter a VM name and select the location. Click **Next**.
5. In the **Select a compute resource**, select the host for the VM. Click **Next**.

vSphere validates the settings for the OVF template.
6. In the **Review details** window, click **Next**.
7. In the **Select storage** window, select the virtual disk. Click **Next**.
8. In the **Select networks** window, configure each **Destination Network** according to the following Socket **Source Networks**:
  1. WAN1 interface
  2. WAN2 interface
  3. LAN1 interface
  4. LAN2 Management interface

Click **Next**.
9. In the **Customize template** window, enter the serial number for the vSocket site in the Cato Management Application.

You need to enter the exact serial number (including dashes).
10. Click **Next**.
11. In the **Ready to complete** window, click **Finish**. vSphere deploys the vSocket VM.
12. If necessary, click **Edit Settings** and change the resources and networks for the VM.

## Connecting the vSocket to the Cato Management Application

The Cato Management Application automatically detects the vSocket and uses the serial number to connect it to the site in the Cato Management Application. To register the vSocket, the WAN1 interface must have Internet connectivity and access to a public DNS so it can reach the Cato Cloud and the Cato Management Application.

If the connected router uses DHCP to provide a dynamic IP address to the vSocket WAN1 interface, then the vSocket can automatically start registering to Cato Cloud. If DHCP is not available, then you need to manually configure the IP address for WAN1 interface with the Socket WebUI (see below, [Configuring the Static IP Address on the WAN1 Interface](/v1/docs/configuring-an-esxi-vsocket-site#configuring-the-static-ip-address-on-the-wan1-interface)).

By default, the WAN2 interface is disabled and the vSocket only uses the WAN1 interface to register to the Cato Management Application.

### Configuring the Static IP Address on the WAN1 Interface

When the WAN1 interface can't be assigned a dynamic IP address, use the Socket WebUI to assign a static IP address to WAN1.

#### Accessing Socket WebUI using the Preconfigured IP Address for LAN2

You can use a VM that is on the same network as the vSocket LAN2 interface to connect to the Socket WebUI. The vSocket LAN2 interface has the preconfigured static IP address of 169.254.100.1. From the VM OS, configure a static IP address from the 169.254.0.0/16 network for an interface that is connected to the same network as the vSocket LAN2 interface.

For VMs with a Windows based OS, when DHCP service isn't available, then the network interface automatically generates an IP address in the 169.254.0.0/16 range (APIPA). You can use this Windows VM to connect to the Socket WebUI without configuring a static IP address for the interface.

**To connect to the Socket WebUI using the LAN2 preconfigured IP address:**

1. Connect to another VM on the same subnet as the vSocket.
2. For non-Windows VMs, configure a manual IP address for an interface in the 169.254.0.0/16 range. For example, 169.254.100.100 with the subnet mask 255.255.0.0.
3. Open a Web browser and connect to the Socket WebUI, enter `https://169.254.100.1` .
4. Log in to the Socket WebUI with these credentials:
  - Username: **admin**
  - Password: **admin**
5. In the **Network Settings** tab, configure a static **IP address** for the WAN1 interface.
6. Save the configuration. The vSocket starts registering to the Cato Cloud.

#### Accessing Socket WebUI using a Dynamic IP Address for LAN2

When the interface can receive an IP address from the DHCP server that is available on the LAN2 network, then you can connect to the Socket WebUI using that IP address.

**To connect to the Socket WebUI using the LAN2 dynamic IP address:**

1. Connect to another VM on the same subnet as the vSocket.
2. Open a Web browser and connect to the Socket WebUI using the LAN2 interface, enter `https://&lt;LAN2 interface ip&gt;` .
3. Log in to the Socket WebUI with these credentials:
  - Username: **admin**
  - Password: **admin**
4. Change the password as prompted.
5. In the **Network Settings** tab, configure a static **IP address** for the WAN1 interface.
6. Save the configuration. The vSocket starts registering to the Cato Cloud.

## Known Limitations

- The ESXi vSocket doesn't support high availability (HA) deployments.
