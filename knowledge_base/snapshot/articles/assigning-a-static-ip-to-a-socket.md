---
title: "Assigning a Static IP to a Socket"
slug: "assigning-a-static-ip-to-a-socket"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/assigning-a-static-ip-to-a-socket"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Assigning a Static IP to a Socket

This article explains how to use the Socket WebUI of a Cato Socket to configure an Internet facing WAN port with a static IP address.

## Connecting the Socket to the Internet for the First Time

If this is the first time that the Socket is connecting to the public Internet and the Cato Cloud, use a computer to connect to the local Socket WebUI of a Cato Socket using the default management IP, 169.254.100.1.

For more about using the Socket WebUI, see [Using the Socket WebUI](/v1/docs/accessing-the-socket-webui).

### Prerequisites

When you are assigning a static IP to a Socket for the initial connection to the Internet, you need to physically connect an Ethernet cable between the Socket and a local computer.

### X1500 Socket - Logging in Locally to Socket WebUI

Log in to the X1500 Socket WebUI using the default management IP address 169.254.100.1.

**To log in to the X1500 Socket WebUI locally:**

1. Use an Ethernet cable to connect an interface from the computer to **port 2** (LAN2) on the Socket.
2. Configure the computer interface with a static IP address that is on the same subnet as the **port 2** (LAN2) interface, for example:

You can also use the Ethernet adapter in the computer in DHCP client mode. The computer will automatically receive an IP address within the network range: 169.254.0.0/24.
  - Computer IP address: 169.254.100.2
  - Computer network mask: 255.255.0.0
3. From an Internet browser, go to **https://169.254.100.1**.
4. Enter the default login credentials:
  - Username: admin
  - Password: admin
5. Change the password for the Socket WebUI, in the new window, enter the default password **admin**, and then enter a new complex password.

You are logged in to the Socket WebUI, continue with step 2 below, [Assigning a Static IP to the Socket WAN Interface](/v1/docs/assigning-a-static-ip-to-a-socket#assigning-a-static-ip-to-the-socket-wan-interface).

### X1600 Socket - Logging in Locally to Socket WebUI

Log in to the X1600 or X1600 LTE Socket WebUI using the default management IP address 169.254.100.1.

**To log in to the X1600 Socket WebUI locally:**

1. Use an Ethernet cable to connect an interface from the computer to **port 8** on the Socket.
2. Configure the computer interface with a static IP address that is on the same subnet as the **port 8** interface, for example:

You can also use the Ethernet adapter in the computer in DHCP client mode. The computer will automatically receive an IP address within the network range: 169.254.0.0/24.
  - Computer IP address: 169.254.100.2
  - Computer network mask: 255.255.0.0
3. From an Internet browser, go to **https://169.254.100.1**.
4. Enter the default login credentials:
  - Username: admin
  - Password: admin
5. Change the password for the Socket WebUI, in the new window, enter the default password **admin**, and then enter a new complex password.

You are logged in to the Socket WebUI, continue with step 2 below, [Assigning a Static IP to the Socket WAN Interface](/v1/docs/assigning-a-static-ip-to-a-socket#assigning-a-static-ip-to-the-socket-wan-interface).

### X1700 Socket - Logging in Locally to Socket WebUI

Log in to the X1700 Socket WebUI using the default management IP address 169.254.100.1.

**To log in to the X1700 Socket WebUI locally:**

1. Use an Ethernet cable to connect an interface from the computer to the **Management Port** on the Socket.
2. Configure the computer interface with a static IP address that is on the same subnet as the **Management Port**, for example:

You can also use the Ethernet adapter in the computer in DHCP client mode. The computer will automatically receive an IP address within the network range: 169.254.0.0/24.
  - Computer IP address: 169.254.100.2
  - Computer network mask: 255.255.0.0
3. From an Internet browser, go to **https://169.254.100.1**.
4. Enter the default login credentials:
  - Username: admin
  - Password: admin
5. Change the password for the Socket WebUI, in the new window, enter the default password **admin**, and then enter a new complex password.

You are logged in to the Socket WebUI, continue with step 2 below, [Assigning a Static IP to the Socket WAN Interface](/v1/docs/assigning-a-static-ip-to-a-socket#assigning-a-static-ip-to-the-socket-wan-interface).

## Assigning a Static IP to the Socket WAN Interface

If you are already logged in to the Socket WebUI, start with step 2 below.

**To assign a static IP to the Socket WAN interface:**

1. From the **Home > Topology** page, select the site and in the **Site Sockets** section, click **Socket WebUI**.
2. Click the **Network Settings** tab.
3. From the WAN interface that is connecting to the public Internet, select the **Static Address** option.
4. Enter the IP address settings for the WAN interface.

The following screenshot shows a sample static IP address for the WAN1 interface on an X1500 Socket:

![StaticIP_WAN_X1500.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18115084355357.png)

The example above shows these settings:
  - IP address: 88.0.0.2
  - Mask: 255.255.255.248
  - Gateway: 88.0.0.1
  - Primary DNS: 8.8.8.8
  - Secondary DNS: 1.1.1.1
5. Click **Update**. The static IP address is assigned to the Socket WAN interface.
