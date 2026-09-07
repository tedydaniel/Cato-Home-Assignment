---
title: "XOps Network Playbook - WMI DC Connectivity Playbook"
slug: "xops-network-playbook-wmi-dc-connectivity-playbook"
updated: 2026-06-22T09:26:32Z
published: 2026-06-22T09:26:32Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-wmi-dc-connectivity-playbook"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - WMI DC Connectivity Playbook

## Overview

This playbook guides you through resolving WMI Sync failure alert, which can occur due to multiple issues, such as permissions or invalid credentials.

## Verify scheduled sync failed

- In Stories Workbench use the Network Operations preset and add a new Indication filter with "DC Connectivity Failure - WMI" ![indication_filter_wmi.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32768937693213.jpeg)
- Verify a story is generated as shown below. ![wmi_story.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32768940606237.jpeg)
- Check the story event message and Source IP to find the error and source server. ![dtory_event_message.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32768940606877.jpeg)
- In CMA, Browse to **Access > Directory Services > LDAP**, find the entry and click on "Test Connection" to confirm the error.
- Proceed to the corresponding troubleshooting section and follow the outlined steps to resolve the issue.

## NT_STATUS_ACCESS_DENIED

This error message indicates a permissions issue. The Cato Management Application notifies when it’s unable to access the DC. This error message is usually followed by “DC_Connectivity_Failure” event in the analytics section. The Cato Management Application generates this event (once an hour) when the connection with the DC fails.

The error appears in CMA when selecting "Test Connection" in Access > Directory Services > LDAP section for Real-Time Sync, or when sending an email to the Account Admins.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32440406983069.png)

### Possible Causes

- The DC is down
- Firewall rules that block traffic on the DC
- Routing issues to the DC
- Bad configuration of the Domain Controller
- Wrong password entered in Cato, or password expiration

### Troubleshooting Steps

1. Check the username and password. Verify that you entered the correct Login DN and password.
2. Verify that the Cato Socket sends the correct username in the connection attempt by capturing the packets (PCAP) on the LAN interface of the Socket or the DC itself.
  - Filter the capture for the IP address of the DC and destination port 135.
  - Using Wireshark, you should see a packet with **Fault** at the beginning of the info field and **nca_s_fault_access_denied** at the end. The packet before this contains the username and domain sent by Cato to the DC as shown in the screenshot below:[![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32414336776477.png)](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32414336776477.png)
3. Check the user permissions to read the event log from the domain controller settings. Follow the online help guide - Windows configuration.
4. If you enabled the Daily sync Directory Service Groups and Users (User Awareness), verify that you configure the Domain Controllers for Real Time Sync. Click “Test Connection” and see if you get a “Connection Successful” result.
5. Check for events in the Events in the Monitoring section. You can filter the events based on event type: system and event subtype: Directory Services and look for DC connectivity or sync errors.
6. Follow the online help guide and verify the domain controller configuration settings.
7. Check that traffic isn’t blocked by the internet or WAN firewall. A firewall rule that blocks unidentified users can block the Cato sync user and block the directory services.
8. Walk through all the configuration steps in the Online Help Guide once again to verify that every step was performed correctly. If permissions are not set correctly on the service account used for the connection, you will get an access denied error.

## NT_STATUS_UNSUCCESSFUL

The error will appear when the PoP cannot access the Domain Controller for Real-time sync. This error shows up when selecting "Test Connection" in CMA, under Access > Directory Services > LDAP for Real-Time Sync.

This error usually indicates a misconfiguration of the User Awareness feature settings. It can also occur due to a firewall or routing misconfiguration.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32414336779165.png)

### Possible Causes

- Users are not identified in Events and Analytics
- Traffic is blocked by the Internet/WAN Firewall due to users not being identified
- Customer's new setup of User Awareness and getting DC sync errors
- Bad configuration of User Awareness
- Routing issue

### Troubleshooting Steps

1. Check the Events and verify if there are events of unidentified users.
2. Check that traffic isn’t blocked by Internet/WAN Firewall because of unidentified users.
3. If this is the first time you've enabled the User Awareness feature and you're getting DC sync errors, verify that every step is configured correctly.
4. Make sure that the DC is up and running.
5. Run a traffic capture from the Socket UI, capturing the packets (PCAP) on the LAN interface of the Socket.
  - Click on the Show Status button.
  - Stop the capture and look for the WMI query from the Cato PoP and the server response in the capture file (using any network packet analyzer tool such as Wireshark). If the DC is behind an IPsec site, run the capture on the DC itself.

## NT_RPC_NT_CALL_FAILED

The error indicates that the RPC service on the DC doesn’t respond. This error appears when clicking on the "Show Status" button in the Domain Controllers for Real Time Sync.

### Possible Causes

- RPC service or its dependencies are stopped or unresponsive.
- The WMI service is stopped or hung
- High CPU or memory utilization is causing RPC timeouts.

### Troubleshooting Steps

1. Verify that the Domain controller is up and running, and check the CPU and memory. Sometimes high CPU or memory usage causes the server to overload.
2. Verify that the DC Windows services are started and set for automatic startup:
  - Server
  - Remote Registry
  - WMI

## NT Code 0x80010111

This error means the PoP cannot communicate with the DC because of an RPC header mismatch between the PoP and the DC.

[![uacode.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32409787751581.png)](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32409787751581.png)

### Possible Causes

This error specifically is common on Windows Server 2022, where the DC's RPC version is validated. This is a known issue that customers may run into.

### Troubleshooting Steps

If you receive this error, please open a ticket with Cato Support to address it.

## UA Sync Error NT code 0xc002001b

The error appears when the RPC service on the domain controller has failed to respond.

This error can appear when selecting "Test Connection" under Access > User Awareness > LDAP or when emailing the Account Admins. Possible outcome:

- Users are not identified in Events and Analytics.
- Traffic is blocked by the Internet/WAN Firewall due to users not being identified.
- Customer's new setup of User Awareness and getting DC sync errors.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32418443915677.png)

### Possible Causes

This issue might happen due to exhausted resources on the Domain controller.

### Troubleshooting Steps

The following steps are troubleshooting steps that can be followed:

1. Verify that the Domain controller is up and that it is not exhausted (no CPU or RAM spikes).
2. Increase the amount of RAM and CPUs on the server if possible.
  - If adding more physical resources to the server is not possible, follow the steps below to increase WMI Provider Service memory, handle quotas, and decrease the size of the Security Event logs:
  - Increase the **WMI** **MemoryPerHost** value (see [Increase WMI Quota properties to maximum values](https://blogs.technet.microsoft.com/bulentozkir/2014/01/14/increase-wmi-quota-properties-to-maximum-values/))
  - Follow the steps below to reduce the Security Log size limit to 1MB:
    - Open the **Event Viewer**
    - Navigate to **Event Viewer > Windows Logs > Security**
    - Right-click **Security** and click **Properties**
    - Set the **Maximum log size (KB)** to **1024**
    - **When the maximum event log size is reached,** select **Overwrite events as needed (oldest events first)** or **Archive the log when full, do not overwrite events.**
    - Click OK
3. Verify that the required domain controller services are running (open services.msc and check that Server, Remote Registry, and Windows Management Instrumentation are started and set for automatic startup.
4. In case the domain controller is showing stress signs, it might be required to restart the server.

## Cannot connect to Domain Controller 0xc0000001 NT_STATUS_UNSUCCESSFUL

This general error can result from misconfigurations of the Domain Controller. We recommend following the configuration guide. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32449112497309.png)

## Cannot connect to Domain Controller (code 6)

RPC failure/access or connectivity issues, indicating the system cannot establish communication with a Domain Controller (DC)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32440249933469.png)

### Possible causes

- Connectivity issue between the DC and Cato Cloud
- DC is offline, rebooting, or overloaded.
- RPC service or dependencies are not running on the DC

### Troubleshooting Steps

Sometimes this problem is solved when you use the Socket WebUI to disconnect and reconnect the Socket to the Cato Cloud.

Please see: [/v1/docs/accessing-the-socket-webui](/v1/docs/accessing-the-socket-webui)

**WARNING!** A Socket reconnect action disconnects all current sessions for the site. The Socket reconnects to the Cato Cloud within a few seconds, and connectivity is restored immediately. However, some connection-sensitive traffic (like phone calls) is dropped.

**To perform a reconnect action on the Socket:**

1. Connect to the Socket WebUI, in your web browser, enter **https://<Cato Socket IP address>** For example: **https://10.0.0.26**
2. Enter the username and password.
3. Select the **Cato Connection Settings** tab.
4. Click **Reconnect:**

[![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32440243601053.png)](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32440243601053.png)
5. Log out of the Socket WebUI.

After you perform the Socket reconnect action, the DC error persists. Here are some additional suggestions to troubleshoot connectivity to the DC:

1. Verify the DC connection to the Cato Cloud.
2. Verify that there is two-way communication between the DC and the Cato Cloud.

**To verify that the DC is connected to the Cato Cloud:**

1. Make sure that your DC is powered on.
2. In the Cato Management Application, go to **Home > Topology** and make sure that the site with the DC is connected to the Cato Cloud.
3. Verify that you ping the DC from a host at a different site, or while you are connected to the Cato VPN.
4. If you can't ping the DC, here are some ways to troubleshoot the problem:
  - Check Home > Events for a block event in the Cato Management Application. Do you need to change the **WAN Firewall** policy to allow ICMP traffic to the DC?
  - Check the DC's routing table and ensure the traffic is routed to the Cato Socket or IPsec tunnel.
  - Check the Windows Firewall policy on the DC to make sure that ICMP traffic is not blocked.

**To verify the communication between the DC and the Cato Cloud:**

1. Run a packet capture on the Socket's LAN interface. Please see: [/v1/docs/how-to-capture-traffic-on-a-socket](/v1/docs/how-to-capture-traffic-on-a-socket)
  - If the DC is behind an IPsec site, run the capture on the DC itself.
2. If there is two-way communication, you can see a connection on TCP/135 to your DC initiated from the Cato VPN range (10.41.0.0/16 by default). **Note:** Cato can initiate the connection with any IP address from the VPN range. **Note:** Starting in Windows Server 2008, you must also allow TCP 49152-65535 for the WMI process through any firewall. Adding a Windows firewall rule for the WMI service is also possible. See: [https://docs.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista](https://docs.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista)
3. If you can't find a connection that shows two-way communication, here are some steps to troubleshoot the problem:
  - Contact Cato support if you don't see any traffic from the VPN range to the DC.
  - If you only see SYN packets on TCP/135 from the Cato VPN range to your DC, check the connectivity of the DC:
    - Inspect the DC's routing table and ensure traffic is routed to the Cato Socket or IPsec tunnel.
    - Check the Windows Firewall policy on the DC and make sure that the traffic is not blocked.

## Raising Cases to Cato Support

If following this playbook has not resolved an issue, submit a [Support ticket](/v1/docs/submitting-a-support-ticket). To get the most helpful response to a request, an administrator should provide the results of the troubleshooting steps taken.
