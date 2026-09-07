---
title: "Socket X1700 Deployment Guide"
slug: "socket-x1700-deployment-guide"
updated: 2026-08-25T14:24:34Z
published: 2026-08-25T14:24:34Z
canonical: "knowledge.catonetworks.com/socket-x1700-deployment-guide"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket X1700 Deployment Guide

## Welcome to Your New Cato Socket

This guide explains how to deploy the Socket to a site and connect the site to the Cato Cloud.

You can also watch the following video tutorial on the Cato Academy: [Cato Socket Setup: Unboxing to Rack Ready](https://academy.catonetworks.com/cato-socket-setup-unboxing-to-rack-ready)

### Typical Site Topology

A typical deployment scenario is where the Cato Socket replaces the site's existing firewall. There are many other topologies and scenarios that are also supported.

The following diagram shows a typical topology for a site with two X1700 Sockets in a high availability (HA) configuration connected to two different ISPs.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1700-deployment-guide-image-p1439v9q.png)

#### Prerequisites

The following items are required before you start deploying the Socket:

- Cato Socket - The Socket model that was shipped to you
- ISP connection - the Internet connection through which the Socket connects to the Cato Cloud
- WAN IP - a DHCP or statically-assigned IP address
- Native Range - the LAN range that is directed towards the Socket
- DHCP Range - The DHCP assigned range(s) that the Socket supports (optional)
- Gateway IP - The network’s gateway's IP address
- Make sure that your networking devices and firewalls meet the requirements listed in [Cato Socket Connection Prerequisites and Known Limitations](https://support.catonetworks.com/hc/en-us/articles/360000891085-Cato-Socket-Connection-Prerequisites-and-Known-Limitations).

## Administrator Account Onboarding

After Cato opens an account for your organization, your account administrator must onboard to the Cato Management Application (CMA). This administrative access is required to create, configure, and assign the Socket with the appropriate site.

The onboarding procedure starts when your account’s administrator receives an invitation email from Cato Networks.

If you already have an account for the Cato Management Application, please skip to [Deploying the X1700 Socket](/v1/docs/socket-x1700-deployment-guide#deploying-the-x1700-socket).

**To set your account password:**

1. Click the activation link to redirect to the password configuration window in your browser.
2. Set your password.
3. You will receive a second email and a link to the CMA.

## Deploying the X1700 Socket

**Warning:** When you receive a new Socket from Cato, it arrives with the network card add-on uninstalled. You must perform an initial boot of the Socket before you install the add-on to the Socket. Otherwise you can damage the Socket or add-on card.

This is a high-level overview of the process to deploy an X1700 Socket at the physical location of the site:

1. Power on the Socket and connect the WAN links to the Internet ([Connecting the X1700 Socket to the Cato Cloud](/v1/docs/socket-x1700-deployment-guide#connecting-the-x1700-socket-to-the-cato-cloud)).
2. Create the site in the Cato Management Application ([Creating a Site in the CMA](/v1/docs/socket-x1700-deployment-guide#creating-a-site-in-the-cma)).
3. In the Cato Management Application, assign the X1700 Socket to the relevant site ([Assigning the Socket to a Site](/v1/docs/socket-x1700-deployment-guide#assigning-the-socket-to-a-site)).
4. For X1700 Sockets that use add-on network cards, also perform these steps:
  1. In the Cato Management Application, edit the X1700 Socket site and configure the add-on card ([Configuring the Add-on for the X1700 Socket](/v1/docs/socket-x1700-deployment-guide#configuring-the-addon-for-the-x1700-socket)).
  2. Make sure that the Socket is powered off and that the add-on cards are not installed.
  3. Install the add-on cards to the Socket ([Installing the Network Card Add-On](/v1/docs/socket-x1700-deployment-guide#installing-the-network-card-addon)).
  4. Power on the Socket.
5. Edit the site and define the LAN segments ([Configuring the LAN](/v1/docs/socket-x1700-deployment-guide#configuring-the-lan)).

### Connecting the X1700 Socket to the Cato Cloud

Connect the LAN and WAN ports on the X1700 front panel to the internal network and to the ISP.

These instructions apply to all X1700 Socket models.

**Note**

Deploying a Socket temporarily interrupts Internet connectivity for the site.

**Important:** If you have an add-on card, go to [X1700 Socket Network Card Add-On](/v1/docs/socket-x1700-deployment-guide#x1700-socket-network-card-addon).

1. Unbox the Socket.
2. Connect the LAN cables:
  - If the Socket is replacing a firewall, disconnect the Ethernet cable from the firewall and connect the cable to the Socket’s Port 3.
  - If the LAN is routed from a network device or existing firewall that is not being replaced, connect the Ethernet cable from the relevant port on that device to the Socket’s port 3.
3. Connect the WAN cables:
  - If the Socket is connected directly to the ISP router, connect the Ethernet cable from the ISP device to the Socket’s port 1 (or port 1 and port 2 if you have multiple ISP connections).
4. After the LAN and WAN networks are connected, connect both power cables to the AC power Sockets in the rear panel.

### Creating a Site in the CMA

Create a site in the Cato Management Application (CMA) for the site where you are deploying your new Socket.

If you are using an add-on hardware card with additional network interfaces for the Socket, this add-on is configured after the site is created. For more information, see [Configuring the Add-on for the X1700 Socket](/v1/docs/socket-x1700-deployment-guide#configuring-the-addon-for-the-x1700-socket).

**To create a new X1700 Socket site:**

1. Log in to the CMA.
2. From the navigation menu, click **Network > Sites**.
3. Click **New**. The **Add Site** panel opens.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1700-deployment-guide-image-ypl9xrp9.png)

1. Configure the **General** settings for the site:
  1. Enter the **Site Name**.
  2. Select the **Site Type**. This option determines which icon is used for the site in the **Topology** window.
  3. In **Connection Type**, select **Socket X1700**.
  4. Configure the **Country**, and **State**, for the physical location of the site.
  5. **(Optional)** Customize the **Time Zone**. This setting is used to set the time frame for the Socket update Maintenance Window.
2. In the **WAN Interface Settings** section, configure the settings for the Sockets:
  1. If the site uses a link for the secondary ISP connection, select **Enable WAN2**.
  - **IMPORTANT:** If you are connecting a single ISP to WAN2, select this option to prevent connectivity loss when first connecting to Cato Cloud.
  1. Enter the values (in Mbps) for the **WAN1 Bandwidth** and **WAN2 Bandwidth** for **Downstream** and **Upstream**.
  - **Note:** Your upstream and downstream bandwidth for the WAN1 and WAN2 links are set according to the ISP bandwidth and the license that was purchased from Cato.
  1. If necessary, repeat the previous step for the **WAN2 Bandwidth**.
3. In the **LAN Interface Settings** section, configure the LAN **Native Range** for the site.

- You can't use /31 or /32 CIDR blocks.

### Assigning the Socket to a Site

Once a Socket is up and running, it automatically connects to an optimal PoP in the Cato Cloud and checks if a new version of the Socket firmware is available.

**Note:** If the Socket detects that a new version of the firmware is available, it automatically performs an upgrade, and the CMA shows the **New Socket Detected** notification.

When the Socket has the latest firmware, the CMA displays the **Activate New Socket** notification and sends an email to the Activate New Socket mailing list. You can then activate and assign the Socket to the relevant site.

**To activate the Socket and assign it to a site:**

1. Click the notification icon ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1700-deployment-guide-image-eupk6wbx.png)
2. In the list, locate the **Activate New Socket** notification and click **ACCEPT**.
3. In the **Assign Cato Socket to Site** window, in **Choose Site to assign Socket**, select the site for the new Socket and click **OK**.
4. The site is shown as connected in the **Monitoring > Topology** screen.

### Configuring the LAN

After you create the site, configure the network settings for the LAN.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1700-deployment-guide-image-jpgr32qw.png)

**To configure the LAN settings for the site:**

1. From the navigation menu, click **Network > Sites** and select the new Socket site.
2. From the navigation menu, click **Site Configuration > Networks**.
3. Expand the LAN interface.
4. Review the **Local IP** and **DCHP Settings** for the site.

- For more about configuring the settings for a site, see the [network range articles](https://support.catonetworks.com/hc/en-us/articles/4413280508433) in the Cato Networks Knowledge Base.

### X1700 Socket Network Card Add-On

This section explains how to install the network card add-on in the X1700 Socket and then configure the site in the Cato Management Application for the card.

- The X1700 Socket supports only one network card add-on at one time, multiple network cards are NOT supported
- The X1700B and X1700C Sockets support a second 4x10 Gbps fiber add-on card, the first one must also be a 4x10 Gbps fiber add-on card. This provides a total of eight 10Gbps fiber ports
- The X1700C Socket supports a second 2x100 Gbps fiber add-on card, the first one must also be a 2x100Gbps fiber add-on card. This provides a total of four 100 gbps fiber ports

**Note:** If the add-on was not pre-ordered and installed by Cato, you must restart the Socket after the add-on is installed.

This is a high-level summary of installing add-ons to the Socket:

1. In the Cato Management Application, edit the X1700 Socket site and configure the add-on card ([Configuring the Add-on for the X1700 Socket](/v1/docs/socket-x1700-deployment-guide#configuring-the-addon-for-the-x1700-socket)).
2. Ensure that you have connectivity to the Cato Cloud via Port 1.
  1. The X1700 Socket requires a copper Ethernet (RJ45) connection to establish the tunnel to the Cato PoP (fiber-only connectivity is not supported).
  2. Wait at least 5 minutes before proceeding to the next step to ensure that the Socket receives the updated configuration.
3. Make sure that the Socket is powered off and that the add-on cards are not installed.
4. Install the add-on cards to the Socket ([Installing the Network Card Add-On](/v1/docs/socket-x1700-deployment-guide#installing-the-network-card-addon)).
5. Power on the Socket.

#### Configuring the Add-on for the X1700 Socket

The X1700 Socket may also include add-on cards, which are hardware cards with additional network interfaces that are inserted into the Socket expansion slots. Configure these add-on interfaces as you configure other interfaces.

- Add-on cards are often pre-ordered and installed by Cato Networks
- The add-on card supports mixing LR (long-range) and SR (short-range) transceivers
- For more information, see [Supported Socket Transceivers and USB Ethernet Adapters](https://support.catonetworks.com/hc/en-us/articles/5220124178717-Supported-Socket-Transceivers-and-USB-Ethernet-Adapters)
- The X1700 Socket requires a copper Ethernet (RJ45) connection to establish the tunnel to the Cato PoP (fiber-only connectivity is not supported).
- Before you insert add-ons in the expansion slot, turn off the Socket and disconnect the power supply
- See [X1700 Socket Network Card Add-On](/v1/docs/socket-x1700-deployment-guide#x1700-socket-network-card-addon) for details of the add-ons for each model.

The default setting in the CMA for the Socket **Add-on** option is **None**. If the configured add-on in the CMA and the actual hardware don't match, then the add-on interface is treated as if it were physically disconnected.

**To configure the add-on for the X1700 Socket in the CMA:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Click **New Add-on Card**, and in the panel, select the add-on type for the Socket.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1700-deployment-guide-image-hjy8js0j.png)

1. For X1700B and X1700C Sockets with a second add-on, click **Additional Add-On**.
2. Click **Save**.

- The additional ports are added to the Socket page.
- Once you select an add-on, the **Add Add-on Ports** button is disabled until you remove the existing add-on card.

1. Wait for at least 5 minutes before powering off the Socket and installing the add-on card.

##### Removing Add-on Ports

You can only configure one set of Add-on ports at a time. To configure a new add-on port, you must first remove the existing add-on ports.

**To remove the add-on ports for the X1700 Socket:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, select **Site Configuration > Socket**.
3. Click the three dots at the end of the row for the ports you want to remove, and click **Remove Add-On Port**.
4. In the confirmation window, click **Remove Add-On**.

#### Installing the Network Card Add-On

You can install the authorized network card add-on in the expansion slot for the X1700 Socket. The appliance must be shut down and powered off before you install the add-on, otherwise, the Socket or add-on can be damaged.

**IMPORTANT:** You must follow the instructions for installing the add-on card to the Socket. Otherwise, you can damage the Socket or add-on card.

##### Preparing to Install an Add-On Card

When you receive a new Socket from Cato, it arrives with the network card add-on uninstalled. You must perform the following before you install the add-on to the Socket. Otherwise, you can damage the Socket or add-on card.

- For new Sockets, perform an initial boot of the Socket
- Assign the Socket to a site, as detailed in [Assigning the Socket to a Site](/v1/docs/socket-x1700-deployment-guide#assigning-the-socket-to-a-site)
- Upgrade your Socket to the latest available version

After the Socket successfully boots, power down the Socket and then install the add-on card.

##### Installing a Single Add-On Card

Configure the add-on network card in the CMA before you install the card in the Socket, see [Configuring the Add-on for the X1700 Socket](/v1/docs/socket-x1700-deployment-guide#configuring-the-addon-for-the-x1700-socket).

These are the supported add-ons for installing a single add-on card in the X1700 or X1700B Socket:

- 4 x 1Gbps copper
- 2 x 1Gbps fiber
- 2 x 10Gbps fiber
- 4 x 10Gbps fiber

These are the supported add-ons for installing a single add-on card in the X1700C Socket:

- 4 x 1Gbps fiber
- 4 x 10Gbps fiber
- 2 x 100Gbps fiber

The fiber network add-ons support both SFP and SFP+.

For more information about supported add-ons, see [Supported Socket Transceivers and USB Ethernet Adapters](https://support.catonetworks.com/hc/en-us/articles/5220124178717-Supported-Socket-Transceivers-and-USB-Ethernet-Adapters).

This procedure involves hardware installation, we recommend that you schedule a maintenance window to avoid service interruption.

**To install the network card add-on to an X1700 series Socket:**

1. Shut down the Socket and remove the power cables.
2. Locate the cover plate for the expansion slot on the X1700 Socket.
3. **Note:** For X1700B and X1700C Sockets, the expansion slot is immediately to the right of 8 x 1 Gbps ports.

1. Loosen the thumb screws on the cover plate and remove it.
2. Carefully insert the network card add-on in the expansion slot.
3. Push the add-on to the back of the expansion slot.
4. Tighten the thumb screws on the network card add-on.
5. Reconnect the power cables and turn on the X1700 Socket.

##### X1700B and X1700C Sockets - Installing Two Add-On Cards

The X1700B and X1700C Sockets support up to two add-on interface cards as specified in [X1700 Socket Network Card Add-On](/v1/docs/socket-x1700-deployment-guide#x1700-socket-network-card-addon). Both cards must be identical fiber add-on cards to ensure consistent performance and compatibility.

Configure the add-on network card in the CMA before you install the card to the Socket, see [Configuring the Add-on for the X1700 Socket](/v1/docs/socket-x1700-deployment-guide#configuring-the-addon-for-the-x1700-socket).

When you are adding two new add-on cards to a Socket, add both cards and then power on the Socket.

This procedure involves hardware installation, we recommend that you schedule a maintenance window to avoid service interruption.

**To install two network card add-ons to an X1700B or X1700C Socket:**

1. Make sure that the Socket is running the newest Socket version (v24.x or higher).
2. Shut down the Socket and remove the power cables.
3. Locate the expansion slots to the right of 8 x 1Gbps ports.
4. Insert the fiber network card:
  1. Loosen the thumb screws on the cover plate and remove it.
  2. Carefully insert the network card add-on in the expansion slot.
  3. Push the add-on to the back of the expansion slot.
  4. Tighten the thumb screws on the network card add-on.
5. If you are adding two cards to a Socket, repeat step 4 for the second network card
6. Reconnect the power cables and turn on the X1700 Socket.

#### Replacing Add-ons for the X1700 Socket

##### Overview

To replace an existing add-on card with a different one, first update the configuration in the Cato Management Application (CMA) and then physically replace the hardware.

###### Prerequisites

- Ensure that the Socket is connected to the Internet via a WAN interface that is not in the add-on card you are replacing
- Identify which ports are associated with the current add-on card

##### Replacing the Add-On Card

Update the configuration in the CMA while the Socket is still powered on and connected through a different WAN interface. After saving the configuration, shut down the Socket, replace the card, and power it back on.

**To replace the add-on for the X1700 Socket:**

1. Configure the new add-on card in the CMA:
  1. From the navigation menu, click **Network > Sites** and select the site.
  2. From the navigation menu, select **Site Configuration > Socket**.
  3. Click **New Add-on Card**, and in the panel select the add-on type for the Socket. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1700-deployment-guide-image-0a0vzh44.png)
2. 
  1. For X1700B or X1700C Sockets with a second add-on, click **Additional Add-On**.
  2. Click **Save**.
  - The additional ports are added to the Socket page.
3. Wait for at least 5 minutes before powering off the Socket and installing the add-on card.
4. Power off the Socket.
5. Remove the existing add-on card.
6. Insert the new add-on card into the expansion slot, see [Installing the Network Card Add-On](/v1/docs/socket-x1700-deployment-guide#installing-the-network-card-addon).
7. Power on the Socket.

- The new add-on interfaces are now available and appear on the Socket page. You can assign roles and configure them as needed.

## Working with Your X1700 Socket

### Identifying the X1700 Socket Model

At the end of 2022, Cato introduced a second hardware model for the X1700 Socket. This hardware model is referred as X1700B.

In 2026, Cato introduced a third hardware model for the X1700, referred to as the X1700C.

Each hardware model has a different front panel and uses a different firmware image.

You can use the front panel images in the following sections to identify which Socket model you have.

### Overview of the X1700 Socket

These are the front panel components of the X1700 Socket:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1700-deployment-guide-image-jelht6jj.png)

**Note:** There are three cooling fans for the Socket located in the rear panel.

| Item | Description |
| --- | --- |
| 1 | Storage drives |
| 2 | Expansion slots for network card add-ons: 4 x 1Gbps copper2 x 1Gbps fiber2 x 10Gbps fiber4 x 10Gbps fiber |
| 3 | 8 x 1Gbps |
| 4 | Management port - connects to the Socket WebUI |

#### Front Panel LEDs and Reset Buttons

This section explains the LEDs and reset buttons on the front panel of the X1700 Socket.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1700-deployment-guide-image-lu0eqzd4.png)

| Item | Description |
| --- | --- |
| 1 | LEDs for network ports - Left LED (activity) - no color - port link is disconnected - green (steady color) - link has connectivity - green (blinking) - link is active and passing traffic - Right LED (link speed) - no color - link speed is 10 Mbit/s - green - link speed is 100 Mbit/s - amber - link speed is 1000 Mbit/s |
| 2 | FD button - reserved for future use |
| 3 | Reset button - restarts the Socket |
| 4 | USB1 port |
| 5 | USB2 port - You can use USB 2.0 flash drives to reimage the X1700 Socket with the USB2 port |
| 6 | Power LED - off - Socket is powered off - on - the Socket is powered on |
| 7 | HDD LED - off - the HDD for the Socket is currently inactive - on (blinking) - the Socket is accessing data on the HDD |

### Overview of the X1700B Socket

These are the front panel components of the X1700B Socket:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1700-deployment-guide-image-eidndqqm.png)

| Item | Description |
| --- | --- |
| 1 | Management and USB ports |
| 2 | Storage drives |
| 3 | 8 x 1Gbps |
| 4 | Expansion slots for network card add-ons: 4 x 1Gbps copper2 x 1Gbps fiber2 x 10Gbps fiber4 x 10Gbps fiber |
| 5 | Expansion slot for second network add-on 4 x 10Gbps fiber card |

**Note:** There are 3 cooling fans in the X1700B Socket.

#### Front Panel LEDs, Buttons, and Ports (X1700B)

This section explains the LEDs, buttons, and ports on the front panel of the X1700B Socket.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1700-deployment-guide-image-by7rwzeu.png)

| Item | Description |
| --- | --- |
| 1 | Power LED - off - the Socket is powered off - on - the Socket is powered on |
| 2 | HDD LED - off - the HDD for the Socket is currently inactive - on (blinking) - the Socket is accessing data on the HDD |
| 3 | Power button - Powers on & off the Socket |
| 4 | Reset button - resets the Socket - Reset Socket WebUI password to **admin** - press for 5 - 15 seconds - Reset Socket, delete all configuration files, and unassign from the site - press for 25 - 35 seconds |
| 5 | MGMT port - connects to the Socket WebUI **Note:** Only the lower port is the MGMT port |
| 6 | COM and USB ports - COM port - console port (used by Support to troubleshoot Socket) - USB ports - you can use USB 2.0 or 1.0 flash drives to reimage the X1700B Socket |
| 7 | LEDs for network ports - Left LED (activity) - no color - port link is disconnected - green (steady color) - link has connectivity - green (blinking) - link is active and passing traffic - Right LED (link speed) - no color - link speed is 10 Mbit/s - green - link speed is 100 Mbit/s - amber - link speed is 1000 Mbit/s |

### Overview of the X1700C Socket

These are the front panel components of the X1700C Socket:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/X1700 Front Panel overview.png)

| Item | Description |
| --- | --- |
| 1 | LEDs, buttons, Console, COM, and USB ports Note: The IPMI port is reserved for future use |
| 2 | Storage drives |
| 3 | 8 x 1Gbps |
| 4 | Expansion slots for network card add-ons: - 4 x 1Gbps fiber - 4 x 10Gbps fiber - 2 x 100Gbps fiber The fiber network add-ons support both SFP and SFP+. |
| 5 | Expansion slot for second network add-on fiber card (4 x 10Gbps or 2x100Gbps) |

**Note:** There are 3 cooling fans in the X1700C Socket.

#### Front Panel LEDs, Buttons, and Ports (X1700C)

This section explains the LEDs, buttons, and ports on the front panel of the X1700C Socket.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1700-deployment-guide-image-v1arotmj.png)

| Item | Description |
| --- | --- |
| 1 | HDD LED - off - the HDD for the Socket is currently inactive - on (blinking) - the Socket is accessing data on the HDD |
| 2 | Power LED - off - the Socket is powered off - on - the Socket is powered on |
| 3 | USB-C console port - used by Support to troubleshoot Socket |
| 4 | Power button - Powers on & off the Socket |
| 5 | FD button - reserved for future use |
| 6 | Console and USB ports - Console port - used by Support to troubleshoot Socket - USB ports - you can use USB 2.0 or 1.0 flash drives to reimage the X1700C Socket |
| 7 | COM ports: - Upper port - reserved for future use - Lower port - management port that connects to the Socket WebUI |
| 8 | IPMI port - reserved for future use |
| 9 | LEDs for network ports - Left LED (activity) - no color - port link is disconnected - green (steady color) - link has connectivity - green (blinking) - link is active and passing traffic - Right LED (link speed) - no color - link speed is 10 Mbit/s - green - link speed is 100 Mbit/s - amber - link speed is 1000 Mbit/s |

#### LED Behavior for Network Card Add-Ons

This section explains the meaning of LED behavior on 10Gbps network card add-ons for all X1700 Socket models.

- **Link/Activity LED**
  - no color - port link is disconnected, the port is not receiving power, or the interface is unavailable
  - green (steady color) - link has connectivity
  - green (blinking) - link is active and passing traffic
- **Link Speed LED**
  - no color - link speed is below 10 Gbps, or no link is established
  - blue - link speed is 10 Gbps

### Connecting a Cellular Modem

You can connect a socket to a cellular modem for Internet connectivity. Make sure to use your cellular modem manual as a reference guide.

1. Install the SIM card according to the manufacturers' instructions.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1700-deployment-guide-image-zb5qb7mf.png)

1. Connect the cellular modem to a power supply and verify that the cellular signal strength LEDs indicate network connectivity.
2. Using a network cable, connect your PC to the cellular modem LAN port.
3. On your PC, open a command prompt and run the following command:

- ping google.com
  - If the ping is successful (see the following example), you are connected to the Internet.
  - Pinging google.com [172.217.22.78] with 32 bytes of data: Reply from 172.217.22.78: bytes=32 time=81ms TTL=90 Reply from 172.217.22.78: bytes=32 time=79ms TTL=90 Reply from 172.217.22.78: bytes=32 time=79ms TTL=90 Reply from 172.217.22.78: bytes=32 time=87ms TTL=90 Ping statistics for 172.217.22.78: Packets: Sent = 4, Received = 4, Lost = 0 (0% loss), Approximate round trip times in milli-seconds: Minimum = 79ms, Maximum = 87ms, Average = 81ms
  - If the ping fails (see the following example), contact your cellular modem vendor/distributor for support.
  - Ping request could not find host google.com....

1. If the ping was successful, using a network cable, connect the Socket to the cellular modem LAN port.
2. Configure and monitor the connection as required using the CMA.

### Assigning a Static IP to the WAN (Optional)

If required by your ISP, you can set a static IP for the WAN interface.

**To set a static IP for the WAN interface:**

1. In your browser, type the URL https://[your Cato Socket's IP address]. For example: https://10.0.0.15

- If this is a new Socket that has never been connected, connect your computer to the MGMT port (for X1500 Socket models, use port 2 (sometimes labeled LAN2)), then in your browser type the following URL: https://169.254.100.1

1. Enter your login credentials.
  - If this is the first time that you are logging in to the window, use the following credentials:
  - **username** = admin
  - **password** = admin
  - You will then need to change these credentials to your own.
  - After six consecutive failed login attempts, you will be locked out of your account for at least 30 minutes.
2. In the Cato Socket Configuration window, click **Network Settings** and click **Static Address**.
3. In **IP Address**, enter the static IP address. If required, modify any other static address parameters.
4. Click **Update**.

### Connecting the Socket through PPPoE (Optional)

If required by your ISP, you can define a PPPoE connection for the WAN interface.

**To define a PPPoE connection for the WAN interface:**

1. In your browser, type the URL https://[your Cato Socket's IP address]. For example: https://10.0.0.15

- If this is a new Socket that has never been connected, connect your computer to the MGMT port (for X1500 Socket models, use port 2 (sometimes labeled LAN2)), then in your browser type the following URL: https://169.254.100.1

1. Enter your login credentials.
  - If this is the first time that you are logging in to the window, use the following credentials:
  - **username** = admin
  - **password** = admin
  - You will then need to change these credentials to your own.
  - After six consecutive failed login attempts, you will be locked out of your account for at least 30 minutes.
2. In the Cato Socket Configuration window, click **Network Settings** and click **PPPoE**.
3. In the **PPP account (user) name**, **PPP account secret (password)** and **Confirm password** fields, enter the information provided by your ISP. If required, modify any other PPPoE fields as instructed by your ISP.
4. Click **Update**.

### X1700 Socket Electrical Specifications

These are the power consumption details and electrical specifications for the X1700 and X1700B Socket models.

#### Socket BTU/HR Details

| Socket Model | Idle | Full Loading |
| --- | --- | --- |
| X1700 | 74 | 428 |
| X1700B | 105 | 263 |

#### Full Output Power

The Socket shall supply the full output power, as long the power supply module is operating within specifications. The table below shows the rated output power for each input voltage range:

| **Parameter** | **Minimum Input** | **Rated Input** | **Maximum Input** | **VAC Recover** | **VAC Low Limit** |
| --- | --- | --- | --- | --- | --- |
| 115 VAC | 90Vms | 100-127Vms | 132Vms | 85VAC +/- 5VAC | 75VAC +/- 5VAC |
| 230 VAC | 180Vms | 200-240Vms | 264Vms |  |  |
| Frequency | 47Hz | 50/60 Hz | 63 Hz |  |  |

#### Input Current

The maximum input current defines the maximum possible output current, to ensure the proper function of the Socket to meet all defined specifications. The following table shows the maximum input current:

| **Input Voltage** | **Input Current** | **Inrush Current** | **Max Power** | **Peak Power** |
| --- | --- | --- | --- | --- |
| 90-132VAC | 5A* | 40A* | 300W | 400W |
| 180-264VAC | 3A* | 60A* | 300W | 400W |

#### Line Fuse

The power supply module inserted into the Socket shall incorporate one input fuse on the line side for input overcurrent protection to prevent damage to the power supply and Socket, to meet product safety requirements.

Fuses should be slow-blow type or equivalent to prevent nuisance trips. AC inrush current shall not cause the AC line fuse to blow under any conditions. All protection circuits in the power supply shall not cause the AC fuse to blow unless a component in the power supply has failed. This includes DC output load short conditions.

## Additional Resources

- Online documentation is available in the [Cato Networks Knowledge Base](https://support.catonetworks.com/hc/en-us)
- Learn more about Cato Support at: [https://www.catonetworks.com/support/](https://www.catonetworks.com/support/)

## Socket X1700 Rack-Mounting Kit Assembly Guide

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1700-deployment-guide-image-2gi87ca5.png)

## Socket X1700B Rack-Mounting Kit Assembly Guide

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1700-deployment-guide-image-bx9dnzfu.png)
