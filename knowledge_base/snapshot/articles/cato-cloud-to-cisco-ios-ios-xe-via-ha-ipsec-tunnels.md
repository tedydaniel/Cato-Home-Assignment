---
title: "Cato Cloud to Cisco IOS/IOS-XE via HA IPSec Tunnels"
slug: "cato-cloud-to-cisco-ios-ios-xe-via-ha-ipsec-tunnels"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/cato-cloud-to-cisco-ios-ios-xe-via-ha-ipsec-tunnels"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Cloud to Cisco IOS/IOS-XE via HA IPSec Tunnels

This article discusses how to connect an IPsec site with Cisco IOS/IOS-XE devices in a High Availability (HA) configuration to the Cato Cloud.

## Sample Network Topology

The diagram below shows the topology of a Cato IPsec site that uses Cisco IOS/IOS-XE devices to connect to the Cato Cloud in an active/passive HA configuration.

![Topology.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247856032285.png)

## Creating an HA IPsec Site for Your Account with Cisco IOS/IOS-XE Devices

You can use the Cato Management Application to create an IPsec IKEv2 site to connect your Cisco devices to the Cato Cloud. You first need to allocate an IP address for your Cato account. Then configure the settings in the Cisco devices to connect to the Cato public IP address. Finally, configure the IPsec site settings to connect to the Cisco devices.

**To configure an IPsec site to connect to the Cato Cloud with Cisco devices:**

1. From the Cato Management Application, allocate an IPsec Peer IP from a primary and secondary PoP.

| ![CMA_IP_Allocation](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247843394461.png) |
| --- |
  1. From the navigation menu, click **Network(1) > IP Allocation (2)**.
  2. In the **IP Allocation** screen, select two PoP locations that are the primary PoP and secondary PoP **(3)** for the IPsec tunnels.

After select the PoP location, the corresponding IPsec peer IP address is shown.
  3. Click **Save (4)**.
2. From the Cisco IOS CLI, create an IKEv2 Proposal and Policy. Open the Configure Terminal prompt and create an IKEv2 Proposal and Profile (similar to the example below):

```plaintext
crypto ikev2 proposal CATO_IKEv2_PROPOSAL
encryption aes-gcm-256
prf sha512group 21
!
crypto ikev2 policy CATO_IKEv2_POLICY
proposal CATO_IKEv2_PROPOSAL
!
```
3. Create an IKEv2 Keyring and Profile (similar to the example below):

```plaintext
crypto ikev2 keyring CATO_KEYRING
peer Dallas
address x.x.x.x
pre-shared-key local Cato1234
pre-shared-key remote Cato1234
!
peer Chicago y.y.y.y
pre-shared-key local Cato1234
pre-shared-key remote Cato1234
!
crypto ikev2 profile CATO_IKEv2_PROFILE
match identity remote address x.x.x.x 255.255.255.255
match identity remote address y.y.y.y 255.255.255.255
authentication remote pre-share
authentication local pre-share
keyring local CATO_KEYRING
!
```
4. Create an IPec Transform-set and Profile (similar to the example below):

```plaintext
!
crypto ipsec transform-set CATO_TSET esp-gcm 256
!
crypto ipsec profile CATO_IPSEC_PROFILE
set transform-set CATO_TSET
set pfs group21
set ikev2-profile CATO_IKEv2_PROFILE
!
```
5. Create IPsec Tunnel interfaces with a tunnel source of the external public facing interface (similar to the example below):

```plaintext
interface Tunnel0
ip address 172.16.3.1 255.255.255.252
tunnel source GigabitEthernet2
tunnel mode ipsec ipv4
tunnel destination x.x.x.x
tunnel protection ipsec profile CATO_IPSEC_PROFILE
!
interface Tunnel1
ip address 172.16.4.1 255.255.255.252
tunnel source GigabitEthernet2
tunnel mode ipsec ipv4
tunnel destination y.y.y.y
tunnel protection ipsec profile CATO_IPSEC_PROFILE
!
```
6. Set the routes on the Cisco device based on the requirements for the site:
  1. Selective traffic to Cato - Create static routes to point specific subnets to Cato via the IPSec tunnel interfaces (similar to the example below):

```plaintext
ip route x.x.x.x x.x.x.x 255.255.255.255 Tunnel0 172.16.3.2
ip route x.x.x.x x.x.x.x 255.255.255.255 Tunnel1 172.16.4.2 250
```
  2. All traffic to Cato – Create static routes to point Cato Peer IP addresses towards the public Internet and a default route towards the Cato tunnels (similar to the example below):

```plaintext
ip route x.x.x.x 255.255.255.255 GigabitEthernet2 z.z.z.z name (Cato Primary Peer route)
ip route y.y.y.y 255.255.255.255 GigabitEthernet2 z.z.z.z name (Cato Secondary Peer route)
ip route 0.0.0.0 0.0.0.0 Tunnel0 172.16.3.2
ip route 0.0.0.0 0.0.0.0 Tunnel1 172.16.4.2 250
```
7. In the Cato Management Application, create a new site for the Cisco site.

| ![image3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247859665821.png) |
| --- |
  1. From the navigation menu, click **Network (1) > Sites (2)**.
  2. Click **New (3)**. The **Add Site** panel opens.
8. Configure the settings for the new Cisco site.

| ![image4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247856350237.png) |
| --- |
  1. Enter a **Site Name (1)** .
  2. In **Connection Type (2)** select **IPSec IKEv2**.
  3. Define the appropriate **Country (3)** and **State (4)**, if applicable.
  4. In **Native Range (5)**, specify a network range that sits behind the Cisco site that communicates with the ranges connected to the Cato Cloud.
  5. Click **Apply (6)**.
9. Click the name of the new site to open the site and configure the settings.

| ![image5.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247875556253.png) |
| --- |
10. From the navigation menu, select **Site Configuration > IPSec (1)**, and expand the **Primary (2)** tunnel configuration section.

| ![image6.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247832068125.png) |
| --- |
11. Define the settings for the primary IPsec tunnel.

| ![image7.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247856674205.png) |
| --- |
  1. Define the **Public IP**:
    1. In **Cato IP (Egress) (1)**, from the drop-down menu choose the primary PoP IP.
    2. In the **Site IP (2)**, enter the Cisco Router Public WAN Link IP address.
  2. Enter the **Primary PSK (3)**.
12. Expand the **Secondary** tunnel configuration section and configure the settings for the secondary IPsec tunnel:

| ![image8.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247816170653.png) |
| --- |
  1. In **Cato IP (Egress) (1)**, from the drop-down menu choose the backup PoP IP.
  2. In the **Site IP (2)**, Enter the Cisco Router Public WAN Link IP address.
  3. Enter the **PSK (3)**.
13. Expand the **Routing** configuration section, and make sure that **Initiate connection by Cato** is not enabled.

| ![image9.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247832341277.png) |
| --- |

Don't specify any **Network Ranges**. This is a route-based policy and the Cisco IOS router builds a single 0.0.0.0 - 255.255.255.255 security association with the Cato Cloud.
14. Go to the top of the **IPsec** screen and click **Save**.

Your site is now configured to connect to the Cato Cloud.
