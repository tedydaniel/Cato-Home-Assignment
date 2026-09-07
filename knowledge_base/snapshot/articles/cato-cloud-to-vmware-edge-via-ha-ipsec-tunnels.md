---
title: "Cato Cloud to VMware Edge via HA IPsec Tunnels"
slug: "cato-cloud-to-vmware-edge-via-ha-ipsec-tunnels"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/cato-cloud-to-vmware-edge-via-ha-ipsec-tunnels"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cato Cloud to VMware Edge via HA IPsec Tunnels

This article discusses how to connect an IPsec site with VMware Edge devices in a High Availability (HA) configuration to the Cato Cloud.

## Sample Network Topology

The diagram below shows the topology of a Cato IPsec site that uses VMware Edge devices to connect to the Cato Cloud in an active/passive HA configuration with IPsec.

![image1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247875948957.png)

## Creating an HA IPsec Site for Your Account with VMware Edge Devices

You can use the Cato Management Application to create an IPsec IKEv2 site to connect your VMware Edge device to the Cato Cloud. You first need to allocate an IP address for your Cato account. Then configure the settings in the VMware Edge devices to connect to the IP address. Finally, in the Cato Management Application create a new IPSec site, and configure the site settings to connect to the VMware Edge device.

**To configure a site to connect to the Cato Cloud with VMware Edge HA IPsec:**

1. In the Cato Management Application, allocate an IPsec Peer IP from a primary and secondary PoP:

| ![CMA_IP_Allocation](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247857095709.png) |
| --- |
  1. From the navigation menu, click **Network(1) > IP Allocation (2)**.
  2. In the **IP Allocation** screen, select two PoP locations that are the primary PoP and secondary PoP **(3)** for the IPsec tunnels.

After select the PoP location, the corresponding IPsec peer IP address is shown.
  3. Click **Save (4)**.
2. In the VMware SD-WAN Orchestrator navigation menu, select **Configure > Profiles (1)** , and click **New Profile (2)** to create a profile.

| ![image2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247860518557.png) |
| --- |
3. Under the profile, click the **Device** tab.

| ![image3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247857270941.png) |
| --- |
4. Scroll down to the **Cloud VPN** section, and enable the **Branch to Non SD-WAN Destination via Edge** option.

| ![image4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247867081373.png) |
| --- |
5. Add a new **Service**, from the drop-down menu select **New NVS via Edge…**.

| ![image5.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247844433309.png) |
| --- |
6. Enter a **Service Name (1)**, and from the **Service Type (2)** drop-down, select **Generic IKEv2 Router (Router Based VPN)**. Click **Next (3)**.

| ![image6.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247860848925.png) |
| --- |
7. In the **Non SD-WAN Destinations via Edge** window, click **Advanced** and configure the following settings:

| ![image7.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247860967581.png) |
| --- |
  1. For **Primary VPN Gateway Public IP (1)** enter the IP allocated from the primary PoP (in step 1 above).
  2. Set the **DH Group (2)** value to **15** (to match the Cato default value).
  3. In **Site Subnets (3)** , specify any Cato WAN subnets that are allowed access this VMware Edge device.
8. Enable the **Secondary VPN Gateway (1)** and configure the following settings:

| ![image8.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247867423133.png) |
| --- |
  1. For **Public IP (2)** enter the IP allocated from the secondary PoP in step 1 above.
  2. Enable the **Tunnel settings are same as Primary VPN Gateway (3)** option, and click **Save Changes (4)**.
9. Open the settings to associate the new profile with the appropriate VMware Edge device:

| ![image9.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247867519645.png) |
| --- |
  1. In the navigation menu, select **Configure > Edges (1)**.
  2. Click the hyperlink of the appropriate edge device **(2)**.
10. Click the **Edge Overview (1)** tab, and in the **Profile** section select the new profile from the **Profile** drop-down menu **(2)** and then click **Save Changes (3)**.

| ![image10.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247861255197.png) |
| --- |
11. Click the **Device** tab, and in the **Cloud VPN** section configure one of the following options:

| ![image11.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247861337245.png) |
| --- |

Click the **Add (2)** hyperlink for the service to add Tunnel information.
  - For a single production service connection - Select **Enable Edge Override (1)** and specify the service created for this connection
  - For multiple production service connections - Allow the service(s) to import automatically based on the profile you set in the previous step.
12. In the **Add Tunnel** window, configure the following settings:

| ![image12.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247861396125.png) |
| --- |
  1. Set the **Local Identification (1)** as the Public WAN Link IP Address.
  2. Enter a custom **PSK (2)**.
  3. In **Destination Primary Public IP (3)** enter the primary PoP IP address.
  4. In **Destination Secondary Public IP (4)** enter the secondary PoP IP address.
  5. Click **Save Changes**.
13. In the Cato Management Application, create a new site for the VMware Edge site:

| ![image3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247884173853.png) |
| --- |
  1. From the navigation menu, select **Network (1) > Sites (2)**.
  2. Click **New (3)**. The **Add Site** panel opens.
14. Configure the settings for the new VMware Edge site.

| ![image4.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247867959709.png) |
| --- |
  1. Enter a **Site Name (1)**.
  2. In **Connection Type (2)**, select **IPsec IKEv2**.
  3. Select the appropriate **Country (3)** and **State (4)**.
  4. In **Native Range (5)** specify a network range that sits behind the VMware Edge site that communicates with the ranges connected to the Cato Cloud.
  5. Click **Apply (6)**.
15. Click the name of the new site to open the site and configure the settings.

| ![image5.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247858451741.png) |
| --- |
16. From the navigation menu, select **Network > Site Configuration > IPsec (1)** and expand the **Primary (2)** section.

| ![image6.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247858531997.png) |
| --- |
17. Define the settings for the primary IPsec tunnel:

| ![image7.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247868224797.png) |
| --- |
  1. Define the **Public IP**:
    1. In **Cato IP (Egress) (1)**, from the drop-down menu choose the primary PoP IP.
    2. In the **Site IP (2)**, enter the VMware Edge Router Public WAN Link IP address.
  2. Enter the **Primary PSK (3)**.
18. Expand the **Secondary** tunnel configuration section and configure the settings for the secondary IPsec tunnel:

| ![image8.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247861941533.png) |
| --- |
  1. In **Cato IP (Egress) (1)**, select the secondary PoP IP address from the drop-down menu.
  2. In **Site IP (2)**, enter the VMware Edge Public WAN link IP address.
  3. Enter the **Secondary PSK (3)**.
19. Expand the **Routing** configuration section, and make sure that **Initiate connection by Cato** is not enabled.

| ![image9.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247862014237.png) |
| --- |

Don't specify any **Network Ranges**. This is a route-based policy and the VMware Edge router builds a single 0.0.0.0 - 255.255.255.255 security association with the Cato Cloud.
20. Go to the top of the **IPsec** screen and click **Save**.

Your site is now configured to connect to the Cato Cloud.
