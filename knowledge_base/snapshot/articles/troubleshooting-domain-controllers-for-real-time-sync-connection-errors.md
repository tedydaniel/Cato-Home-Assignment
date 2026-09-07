---
title: "Troubleshooting Domain Controllers for Real Time Sync Connection Errors"
slug: "troubleshooting-domain-controllers-for-real-time-sync-connection-errors"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/troubleshooting-domain-controllers-for-real-time-sync-connection-errors"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Domain Controllers for Real Time Sync Connection Errors

## Overview

You're seeing an error message in the Cato Management Application for the Domain Controller (DC). We're here to help! This article discusses troubleshooting steps and solutions for common errors when performing the connection test in the **Directory Services > Domain Controllers for Real Time Sync** section.

For more information, see [Configuring the Windows Server for Directory Services](/v1/docs/configuring-the-windows-server-for-directory-services).

## Error - Cannot connect to Domain Controller (code 6)

If you see a code 6 connection error in the Cato Management Application, as follows:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/360002921118.png)

There are some steps you can take to troubleshoot the problem.

### Reconnecting the Cato Socket

Sometimes this problem is solved when you use the Socket WebUI to disconnect and reconnect the Socket to the Cato Cloud.

**WARNING!** A Socket reconnect action disconnects all current sessions for the site. The Socket reconnects to the Cato Cloud within a few seconds, and connectivity is restored immediately. However, some connection-sensitive traffic (like phone calls) is dropped.

**To perform a reconnect action on the Socket:**

1. Connect to the Socket WebUI, in your web browser, enter **https://<Cato Socket IP address>**  
For example: **https://10.0.0.26**
2. Enter the username and password.
3. Select the **Cato Connection Settings** tab.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/360002841497.png)
4. Click **Reconnect**.
5. Log out of the Socket WebUI.

### Troubleshooting Connectivity to the DC

After you perform the Socket reconnect action, the DC error persists. Here are some additional suggestions to troubleshoot connectivity to the DC:

1. Verify the DC connection to the Cato Cloud.
2. Verify that there is two-way communication between the DC and the Cato Cloud.

**To verify that the DC is connected to the Cato Cloud:**

1. Make sure that your DC is powered on.
2. In the Cato Management Application, go to **Home > Topology** and make sure that the site with the DC is connected to the Cato Cloud.
3. <font color="#000066"> Verify that you ping the DC from a host at a different site, or while you are connected to the Cato VPN. </font>
4. If you can't ping the DC, here are some ways to troubleshoot the problem:
  - Check Home > Events for a block event in the Cato Management Application. Do you need to change the **WAN Firewall** policy to allow ICMP traffic to the DC?
  - Check the DC's routing table and ensure the traffic is routed to the Cato Socket or IPsec tunnel.
  - Check the Windows Firewall policy on the DC to make sure that ICMP traffic is not blocked.

**To verify the communication between the DC and the Cato Cloud:**

1. Run a packet capture on the Socket's LAN interface.
  - If the DC is behind an IPsec site, run the capture on the DC itself.
2. If there is two-way communication, you can see a connection on TCP/135 to your DC initiated from the Cato VPN range (10.41.0.0/16 by default).  
**Note:** Cato can initiate the connection with any IP address from the VPN range.  
**Note:** Starting in Windows Server 2008, you must also allow TCP 49152-65535 for the WMI process through any firewall. Adding a Windows firewall rule for the WMI service is also possible. See: [https://docs.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista](https://docs.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista)
3. If you can't find a connection that shows two-way communication, here are some steps to troubleshoot the problem:
  - Contact Cato support if you don't see any traffic from the VPN range to the DC.
  - If you only see SYN packets on TCP/135 from the Cato VPN range to your DC, check the connectivity of the DC:
    1. <font color="#000066"> Inspect the DC's routing table and ensure traffic is routed to the Cato Socket or IPsec tunnel. </font>
    2. <font color="#000066"> Check the Windows Firewall policy on the DC and make sure that the traffic is not blocked. </font>

## Error: Cannot connect to Domain Controller 0xc0000022 NT_STATUS_ACCESS DENIED

If you see an Access Denied error message in the Cato Management Application as follows:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/360002921138.png)

There are some steps you can take to troubleshoot the authentication problem:

1. Check the username and password in the Cato Management Application.
  - Make sure that the username is correct
  - Try to re-enter the password - maybe there was a typo
2. Verify that Cato is sending the correct username in the connection attempt. Run a packet capture on the LAN interface of the Socket or the DC itself.
  - Filter the capture for the IP address of the DC and destination port 135.
  - Using Wireshark, you should see a packet with **Fault** at the beginning of the info field and **nca_s_fault_access_denied** at the end. The packet before this contains the username and domain sent by Cato to the DC, as shown in the screenshot below.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/360002841477.png)
3. Walk through all the configuration steps in the Online Help Guide again to verify that every step was performed correctly. If permissions are not set correctly on the service account used for the connection, you will get an access denied error.  
**Hint:** To verify that a permission issue on the DC causes the error, you can temporarily set a Domain admin as the service user. Domain admins have all the necessary permissions by default.

## Error: Cannot connect to Domain Controller 0xc0000001 NT_STATUS_UNSUCCESSFUL

If you see the unsuccessful status error message in the Cato Management Application as follows:

"Cannot connect to Domain Controller 0xc0000001 NT_STATUS_UNSUCCESSFUL. Verify that you have correctly integrated the Domain Controller with Cato Network. If the issue persists, contact Cato Support for assistance. Click here for details."

This general error can result from misconfigurations of the Domain Controller. We recommend following the configuration guide.

## Error: 0xc00000b5 NT_STATUS_IO_TIMEOUT

In case the CMA shows a security event like the one in the picture below, showing error **0xc00000b5 NT_STATUS_IO_TIMEOUT** please get in touch with our Support

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27758243469853.png)
