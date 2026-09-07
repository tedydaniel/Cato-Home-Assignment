---
title: "How to Capture Traffic for SDP Client Issues with Wireshark"
slug: "how-to-capture-traffic-for-sdp-client-issues-with-wireshark"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/how-to-capture-traffic-for-sdp-client-issues-with-wireshark"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Capture Traffic for SDP Client Issues with Wireshark

When collecting PCAPs on your local device for SDP Client-related issues, ensure that you always collect from both the wireless/wired interface AND the tunnel interface. Otherwise, you aren’t capturing all the VPN-related traffic.

PCAPs can be captured using Wireshark.

## **For Windows machine running WVPN before v5.4**

Running Wireshark and selecting the wireless/wired interface and CatoNetworksVPN tunnel interface -

Step 1: Launch Wireshark and click the **Capture Option**.

![option_1_pic_1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/6327965596957.png)

Step 2: Select the wireless and/or wired interface, and the CatoNetworksVPN interface.

![mceclip2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/6353186227357.png)

Step 3: Click **Start** to start capturing traffic on the selected interface.

## **For Windows machines running WVPN v5.4 and later**

![wvpn5.4-wireshark.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/6354388754973.png)

*******Note:** In later versions, the tunnel adapter is called "CatoNetworks"

## **For MAC machine**

Step 1: Open the MVPN and check assigned Cato IP address

![mac_vpn.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/6354421152157.png)

Step 2: Launch the terminal and run “ifconfig”. Then check which utun interface was assigned with the Cato IP address

To display utun interfaces only: ifconfig | grep -A5 "^utun" or ifconfig | awk '/^utun/{flag=1} flag{print} /status:/{flag=0}'

Results should display output as below, making it easier to capture traffic.

![mac_cli.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/6354392219677.png)

Step 3: Launch wireshark and select wireless and/or wired interface, and the associated utun interface as identified in Step 2.

![mac_wireshark.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/6354392732957.png)
