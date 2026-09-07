---
title: "Using Cellular Modems with a Socket"
slug: "using-cellular-modems-with-a-socket"
updated: 2026-06-22T09:21:20Z
published: 2026-06-22T09:21:20Z
canonical: "knowledge.catonetworks.com/using-cellular-modems-with-a-socket"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Cellular Modems with a Socket

## Connecting a Socket to a Cellular Modem

You can connect a socket to a cellular modem for internet connectivity.

> [!NOTE]
> Note:
> 
> Perform the following steps using your cellular modem manual as a guide.

**To connect a cellular modem to the Socket:**

1. Install the SIM card according to the manufacturer instructions.

![Cellular_Modem_01.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248099495453.png)
2. Connect the cellular modem to a power supply and verify that the cellular signal strength LEDs indicate network connectivity.
3. Using a network cable, connect your PC to the cellular modem LAN port.

![Cellular_Modem_03.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248092599325.png)
4. On your PC, open a command prompt and run the following command:

`ping google.com`
  - If the ping is successful (see the following example), you are connected to the internet.

`ping google.com`

`Pinging google.com [172.217.22.78] with 32 bytes of data: Reply from 172.217.22.78: bytes=32 time=81ms TTL=90 Reply from 172.217.22.78: bytes=32 time=79ms TTL=90 Reply from 172.217.22.78: bytes=32 time=79ms TTL=90 Reply from 172.217.22.78: bytes=32 time=87ms TTL=90 Ping statistics for 172.217.22.78: Packets: Sent = 4, Received = 4, Lost = 0 (0% loss), Approximate round trip times in milli-seconds: Minimum = 79ms, Maximum = 87ms, Average = 81ms`
  - If the ping fails (see the following example), contact your cellular modem vendor/distributor for support.

`ping google.com Ping request could not find host google.com....`
5. If the ping was successful: using a network cable, connect the Cato Socket to the cellular modem LAN port.

![Cellular_Modem_04.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24248067621277.png)
6. Configure and monitor the connection as required using the Cato Management Application.
