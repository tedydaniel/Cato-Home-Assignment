---
title: "No Internet Error on Windows - NCSI Troubleshooting"
slug: "no-internet-error-on-windows-ncsi-troubleshooting"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/no-internet-error-on-windows-ncsi-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# No Internet Error on Windows - NCSI Troubleshooting

## Issue

Windows reports that there is no internet connectivity on the Ethernet or WiFi link even though the user can successfully access the Internet. This may also cause various Microsoft features to not work properly, such as Office 365 setup.

Windows Network Connectivity Status Indicator (NCSI) checks using active and passive probing may fail when the Windows PC is connected to Cato.

![ncsi.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13184507119901.jpeg)

## Environment

Windows PC behind a socket or connected via Cato VPN.

## Troubleshooting

When Windows connects to a new network, it checks for internet connectivity using Active Probing which involves a series of tasks. After determining that there's internet connectivity, Windows switches to Passive Probing until the connection remains active.

## Basic Troubleshooting

Below are some troubleshooting steps for each type of probing:

### 1. Active Probing

Windows uses active probing to validate that internet connectivity is possible on each network interface, then updates the Network Connectivity Status Indicator (NCSI). During active probing, Windows probes several Microsoft DNS servers and uses the responses to determine an active internet connection.

```plaintext
For more information see: NCSI active probes and the network status alert
```

For Windows 10 or later versions:

- NCSI sends a DNS request to resolve the address of the`www.msftconnecttest.com`FQDN.
- If NCSI receives a valid response from a DNS server, NCSI sends a plain HTTP GET request to`http://www.msftconnecttest.com/connecttest.txt`.
- If NCSI successfully downloads the text file, it makes sure that the file contains Microsoft Connect Test.
- NCSI sends another DNS request to resolve the address of the`dns.msftncsi.com`FQDN.
  - If any of these requests fails, the network alert appears in the Task Bar. If you hover over the icon, you see a message such as "No connectivity" or "Limited Internet access" (depending on which requests failed).
  - If all of these requests succeed, the Task Bar shows the usual network icon. If you hover over the icon, you see a message such as "Internet access".

If you receive reports of Windows showing no internet connectivity, check if any of the connections mentioned above are failing. Taking PCAPs and checking Events/flows would be one way to verify.

NCSI checks logging

It is also possible to log active NCSI checks using the following method:

- Start the trace by issuing the command:

```plaintext
netsh trace start scenario=NetConnection tracefile=noint.etl
```
- Now reproduce the problem (disconnect and then reconnect the client from the network) and then stop the trace with the command:

```plaintext
netsh trace stop
```
- Here is an example of the sort of information that can be found in the trace file:

![44152-image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13097080703901.png)

Windows Registry setting blocking active probes

It is possible that active probes can be blocked by a Windows Registry setting, and in that case, Windows will rely entirely on passive probing.

Verify that the following key has the **default** windows value:

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\Connections] "WinHttpSettings"=hex:18,00,00,00,00,00,00,00,01,00,00,00,00,00,00,00,00,00,00,00

In the following example, a system proxy modified the "WinHttpSettings" registry key via GPO which imports this hexadecimal registry value that overrides the default value Windows automatically puts into place. This will cause active probing to fail.

![gpo.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13097126372637.png)

### 2. Passive Probing

Live network traffic is captured and analyzed, without interfering with the network, i.e. not sending any packets out. Passive probing looks at the TTL (Time To Live) in the IP header of TCP/UDP packets which can determine how many "hops" the packet has taken to reach the computer. A packet with more than 8 hops is considered to have Internet Connectivity.

Cato's TCP proxy would set the TTL in IP headers to 96 as illustrated below. Packet capture can be performed on the Windows machine to validate on the TTL value received.

![mceclip1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/13097087559581.png)

## Workarounds:

Below are some potential workarounds that have been proven to resolve the issue in the field: -

1. Set the below registry key to utilize the WinTAP (layer 2) adapter instead of WinTUN (layer 3): `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN\UseWintun=0` (DWORD)
2. Change the below registry key to switch to a new mode where the original route is not being deleted. `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN\RTNoRemoveMode=1` (DWORD)

Below are the steps to edit/add the registry keys:

- **Open the Registry Editor**:
  - Press `Win + R` to open the Run dialog.
  - Type `regedit` and press Enter. This will open the Registry Editor.
- **Navigate to the Key**:
  - In the Registry Editor, navigate to `HKEY_LOCAL_MACHINE\SOFTWARE`.
  - If the `CatoNetworksVPN` key doesn't exist, you'll need to create it. Right-click on the `SOFTWARE` key, select `New`, and then choose `Key`. Name the key `CatoNetworksVPN`.
- **Create the DWORD Value**:
  - Right-click on the `CatoNetworksVPN` key you just created.
  - Select `New` and then choose `DWORD (32-bit) Value`.
  - Name the new DWORD value `UseWintun` or `RTNoRemoveMode`.
- **Set the Value Data**:
  - Double-click on the `UseWintun` DWORD value.
  - In the appropriate "Value data" field, enter `0` or `1`(without quotes).
- **Confirm and Close**:
  - Click `OK` to save the changes.
  - Close the Registry Editor.
- **Restart Your VPN Client**:
  - Restart the VPN client for the registry key to take effect.
