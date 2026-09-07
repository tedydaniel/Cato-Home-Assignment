---
title: "Socket X1500 Deployment Guide"
slug: "socket-x1500-deployment-guide"
updated: 2026-07-13T07:30:44Z
published: 2026-07-13T07:30:44Z
canonical: "knowledge.catonetworks.com/socket-x1500-deployment-guide"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket X1500 Deployment Guide

## Welcome to Your New Cato Socket

This guide explains how to deploy the Socket to a site and connect the site to the Cato Cloud.

You can also watch the following video tutorial on the Cato Academy: [Cato Socket Setup: Unboxing to Rack Ready](https://academy.catonetworks.com/cato-socket-setup-unboxing-to-rack-ready)

### Typical Site Topology

A typical deployment scenario is where the Cato Socket replaces the site's existing firewall. There are many other topologies and scenarios that are also supported.

The following diagram shows a typical topology for a site with two X1500 Sockets in a high availability (HA) configuration connected to two different ISPs.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-spnunlx0.png)

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

After Cato opens an account for your organization, your account administrator must onboard to the Cato Management Application (CMA). This administrative access is required to create, configure, and assign the Socket to the appropriate site.

The onboarding procedure starts when your account’s administrator receives an invitation email from Cato Networks.

If you already have an account for the CMA, please skip to [Deploying the X1500 Socket](/v1/docs/socket-x1500-deployment-guide#deploying-the-x1500-socket) .

**To set your account password:**

1. Click the activation link to redirect to the password configuration window in your browser.
2. Set your password.
3. You will receive a second email and a link to the CMA.

## Deploying the X1500 Socket

This is a high-level overview of the process to deploy an X1500 Socket at the physical location of the site:

1. Power on the Socket and connect the WAN links to the Internet ([Connecting the X1500 Socket to the Cato Cloud](/v1/docs/socket-x1500-deployment-guide#connecting-the-x1500-socket-to-the-cato-cloud)).
2. Create the site in the CMA ([Creating a Site in the CMA](/v1/docs/socket-x1500-deployment-guide#creating-a-site-in-the-cma)).
3. In the CMA, assign the X1500 Socket to the relevant site ([Assigning the Socket to a Site](/v1/docs/socket-x1500-deployment-guide#assigning-the-socket-to-a-site)).
4. Edit the site and define the LAN segments ([Configuring the LAN](/v1/docs/socket-x1500-deployment-guide#configuring-the-lan)).

### Connecting the X1500 Socket to the Cato Cloud

Connect the LAN and WAN ports on the X1500 rear panel to the internal network and to the ISP.

These instructions apply to all X1500 Socket models.

**Note:** Deploying a Socket temporarily interrupts Internet connectivity for the site.

1. Unbox the Socket.
2. Connect the LAN cables:
  - If the Socket is replacing a firewall, disconnect the Ethernet cable from the firewall and connect the cable to the Socket’s port 1 (some X1500 Sockets refer to this port as LAN1).
  - If the LAN is routed from a network device or existing firewall that is not being replaced, connect the Ethernet cable from the relevant port on that device to the Socket’s port 1.
3. Connect the WAN cables:
  - If the Socket is connected directly to the ISP router, connect the Ethernet cable from the ISP device to the Socket’s port 3 (or port 3 and port 4 if you have multiple ISP connections).
  - Some X1500 Sockets refer to these ports as WAN1 and WAN2.
4. After the LAN and WAN networks are connected, connect the power supply.

### Creating a Site in the CMA

Create a site in the Cato Management Application (CMA) for the site where you are deploying your new Socket.

**To create a new X1500 Socket site:**

1. Log in to the CMA.
2. From the navigation menu, click **Network > Sites**.
3. Click **New**. The **Add Site** panel opens. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-7mj4xnjh.png)
4. Configure the **General** settings for the site:
  1. Enter the **Site Name**.
  2. Select the **Site Type**. This option determines which icon is used for the site in the **Topology** window.
  3. In **Connection Type**, select **Socket X1500**.
  4. Configure the **Country**, and **State**, for the physical location of the site.
  5. **(Optional)** Customize the **Time Zone**. This setting is used to set the time frame for the Socket update Maintenance Window.
5. In the **WAN Interface Settings** section, configure the settings for the Sockets:
  1. If the site uses a link for the secondary ISP connection, select **Enable WAN2**. **IMPORTANT:** If you are connecting a single ISP to WAN2, select this option to prevent connectivity loss when first connecting to Cato Cloud.
  2. Enter the values (in Mbps) for the **WAN1 Bandwidth** and **WAN2 Bandwidth** for **Downstream** and **Upstream**.

**Note:** Your upstream and downstream bandwidth for the WAN1 and WAN2 links are set according to the ISP bandwidth and the license that was purchased from Cato.
  3. If necessary, repeat the previous step for the **WAN2 Bandwidth**.
6. In the **LAN Interface Settings** section, configure the LAN **Native Range** for the site. **Note:** You can't use /31 or /32 CIDR blocks.

### Assigning the Socket to a Site

Once a Socket is up and running, it automatically connects to an optimal PoP in the Cato Cloud and checks if a new version of the Socket firmware is available.

**Note:** If the Socket detects that a new version of the firmware is available, it automatically performs an upgrade, and the CMA shows the **New Socket Detected** notification.

When the Socket has the latest firmware, the CMA displays the **Activate New Socket** notification and sends an email to the Activate New Socket mailing list. You can then activate and assign the Socket to the relevant site.

**To activate the Socket and assign it to a site:**

1. Click the notification icon ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-g3lb42bf.png).
2. In the list, locate the **Activate New Socket** notification and click **ACCEPT**.
3. In the **Assign Cato Socket to Site** window, in **Choose Site to assign Socket**, select the site for the new Socket and click **OK**.
4. The site is shown as connected in the **Monitoring > Topology** screen.

### Configuring the LAN

After you create the site, configure the network settings for the LAN.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-n56mi7hq.png)

**To configure the LAN settings for the site:**

1. From the navigation menu, click **Network > Sites** and select the new Socket site.
2. From the navigation menu, click **Site Configuration > Networks**.
3. Expand the LAN interface.
4. Review the **Local IP** and **DCHP Settings** for the site.

- For more about configuring the settings for a site, see the [network range articles](https://support.catonetworks.com/hc/en-us/articles/4413280508433) in the Cato Networks Knowledge Base.

## Working with Your X1500 Socket

### Identifying the X1500 Socket Model

In 2022, Cato introduced a second hardware model for the X1500 Socket. This hardware model is referred as X1500B.

In 2026, Cato introduced a third hardware model for the X1500 Socket, referred to as the X1500C.

Each hardware model has a different rear panel and uses a different firmware image.

For the X1500 and X1500B, to identify which model you have, see [Overview of Reimaging Cato Sockets](https://support.catonetworks.com/hc/en-us/articles/5180985131933-Overview-of-Reimaging-Cato-Sockets). The X1500C is identified by a USB Type-C Console port on the rear panel.

### Overview of the X1500 Socket

These are the rear panel components of the X1500 Socket:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-a6x4i5ar.png)

| Item | Description |
| --- | --- |
| 1 | Power input |
| 2 | LAN ports (on some models labeled LAN1 and LAN2) |
| 3 | WAN ports for Internet connectivity (on some models labeled WAN1 and WAN2) |
| 4 | Serial console port (not shown in the CMA) |

### Link Negotiation Limitation for X1500C Sockets

The X1500C Socket supports only autonegotiation mode for link negotiation. You can’t manually configure a custom speed or duplex setting for X1500C interfaces.

Make sure the Internet connection is connected to a device interface that supports the required speed setting. If the connected ISP device requires a fixed speed or duplex setting, contact your Internet Service Provider (ISP) to reconfigure the interface to use autonegotiation.

### Connecting a Cellular Modem

You can connect a socket to a cellular modem for Internet connectivity. Make sure to use your cellular modem manual as a reference guide.

1. Install the SIM card according to the manufacturers' instructions. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-8iea8r1h.png)
2. Connect the cellular modem to a power supply and verify that the cellular signal strength LEDs indicate network connectivity.
3. Using a network cable, connect your PC to the cellular modem LAN port.
4. On your PC, open a command prompt and run the following command:

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

### X1500 Socket Electrical Specifications

This article shows the details for the power consumption and specifications for the Cato X1500 series Socket models.

#### X1500 BTU/HR Details

| Socket Model | Idle | Full Loading |
| --- | --- | --- |
| X1500 | 16 | 41 |
| X1500B and X1500C | 12.3 | 14.5 |

#### General Description

This specification defines the input, output characteristics, and performance requirements for 24-watt switching mode AC to DC adapter.

#### Electrical Specifications for X1500 series Socket Models

- Input Requirement
  - Input Voltages And Frequency Normal Voltages
  - Normal Voltages 100-240VAC Voltage Variation Range 90-264 VAC
  - Normal Frequency 50-60Hz
  - Frequency Variation Range 47Hz to 63 Hz
  - Input Current
  - AC input current shall not exceed 0.6A MAX, when operated at 100-240VAC with no load to full load.
  - Inrush Current
  - The inrush current must be limited to 50A when operated at 240VAC. Inrush current is measured at an ambient temperature of 25 °C with the test temperature stabilized in the power off condition until at ambient temperature
  - Power Consumption
  - The power consumption shall not exceed 0.075W when operated at normal voltage 100-240VAC with no load
- Input Protection
  - Input Current Protection
  - A fuse with a rating of 2.0A shall be installed on the input line side near the input connector to provided protection to the power supply
- Output Requirement
  - Output Voltage - Current And Ripple Under any combinations of line and load variation and environmental conditions, output shall remain within the tolerance defined below:
    - Input normal voltage: 100 - 240VAC
    - Output Nominal Voltage - 12VDC
    - Output Regulation +/- 5%
    - Minimum Load (A) 0
    - Maximum Load(A) 0
    - Ripple (m Vp-p) 200
    - Output power (w) 24
  - **Note**
    - Output voltages shall be measured at the output connector.
    - Ripple measurements shall be made with an oscilloscope of at least 20 MHz bandwidth. Output shall be bypassed at the connector with a 0.1uF ceramic disk capacitor and a 10uF electrolytic capacitor to simulate system loading at a temperature 25°C.
  - Short Circuit Protection and Over Current Protection
    - The power supply shall be protected from damage of accidentally shorting the Output for a long time period or overcurrent Protection (2.2-3.0)A and auto-recovery when the fault is removed.

## X1500 Socket Rack Mounting

There are two rack mounting guides for the X1500 Socket models. To identify which X1500 Socket model you have, see Overview of Reimaging Cato Sockets:

- X1500 Socket Mounting Guide
- X1500 Dual Model Rack Mounting Guide

### Overview of Dual Rack Mounting Kit

This guide contains instructions for the Rack Mounting Kit for these Socket models: X1500, X1500B, and X1500C. For more information about identifying the X1500 Socket model, see [Overview of Reimaging Cato Sockets](https://support.catonetworks.com/hc/en-us/articles/5180985131933).

You can choose to install the Socket in the rack in these configurations:

- X1500 Socket model:
  - Socket ports facing the front of the rack ([Mounting the X1500 Socket - Ports Front](/v1/docs/socket-x1500-deployment-guide#mounting-the-x1500-socket-ports-front))
  - Socket ports facing the back of the rack ([Mounting the X1500 Socket - Ports Back](/v1/docs/socket-x1500-deployment-guide#mounting-the-x1500-socket-ports-back))
- X1500B and X1500C Socket models:
  - Socket ports facing the front of the rack ([Mounting the X1500B/X1500C Socket - Ports Front](/v1/docs/socket-x1500-deployment-guide#mounting-the-x1500bx1500c-socket-ports-front))
  - Socket ports facing the back of the rack ([Mounting the X1500B/X1500C Socket - Ports Back](/v1/docs/socket-x1500-deployment-guide#mounting-the-x1500bx1500c-socket-ports-back))

### Mounting the X1500 Socket - Ports Front

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-ni4ro4q4.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-8cci70j6.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-0dftv5db.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-0en2ypnr.png)

### Mounting the X1500 Socket - Ports Back

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-3glcacb6.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-wr1xqf5h.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-h20sy2t2.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-pmq4w7n6.png)

### Mounting the X1500B/X1500C Socket - Ports Front

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-3gcxnsbh.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-nrs21cqq.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-x3kojcaa.png)

### Mounting the X1500B/X1500C Socket - Ports Back

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-oaal8wz3.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-vr4vz6fl.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/socket-x1500-deployment-guide-image-5xiuoa28.png)

## Additional Resources

- Online documentation is available in the [Cato Networks Knowledge Base](https://support.catonetworks.com/hc/en-us)
- Learn more about Cato Support at: [https://www.catonetworks.com/support/](https://www.catonetworks.com/support/)
