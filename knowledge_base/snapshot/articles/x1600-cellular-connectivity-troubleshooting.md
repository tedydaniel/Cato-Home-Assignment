---
title: "X1600 Cellular Connectivity Troubleshooting"
slug: "x1600-cellular-connectivity-troubleshooting"
updated: 2026-06-22T09:21:27Z
published: 2026-06-22T09:21:27Z
canonical: "knowledge.catonetworks.com/x1600-cellular-connectivity-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# X1600 Cellular Connectivity Troubleshooting

## Overview

Socket X1600 now has a hardware version that supports Cellular (LTE/5G) connections over cellular networks. By following these troubleshooting steps and considering the relationship between signal quality, data throughput, and related factors, users can proactively address and mitigate Cellular connectivity challenges.

## Symptoms

- Registration issues with the Cellular network.
- Unable to establish a connection. Connection attempts may result in errors or timeouts.
- No signal or poor signal strength. Signal bars may be consistently low or fluctuating.
- Frequent disconnections. Intermittent connectivity issues may lead to dropped connections.
- Reduced data transfer speeds compared to what is expected for a Cellular network.
- Increased latency or delays in data transmission.
- Connection drops during peak hours or in densely populated areas.

## Possible Causes

- Weak or no signal.
- SIM Card issues.
- Data Plan issues.
- Incorrect APN settings.
- Network congestion.
- Signal Interference.
- Weather conditions.

## Troubleshooting Cellular Connectivity

Before starting to troubleshoot any Cellular connectivity issues, make sure that:

- The Socket has an active SIM Card. Ensure a working **Micro SIM card** with an active data plan.
- The Cellular Socket has antennas plugged in and secured.
- Cellular connectivity LED is on the Socket front panel marked by an antenna icon next to it ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25452495246877(1).png).

### Initial steps

- Insert the SIM card into the slot and wait for the LED indicator to show connectivity:
  - **Red****:** Disconnected. Signal Strength = 0%
  - **Blue****:** The signal is low. Signal Strength 0%-45%
  - **Green****:** The signal is good. Signal Strength >45%
- By default, SIM Slot 1 is the active one, while Slot 2 is standby. You will not be able to switch from Slot 1 to Slot 2 when there is no SIM card in the first slot.
- Make sure that the Cellular interface is enabled on the CMA Socket page. To do this, set the destination as **Cato**.
- Cellular shall be the less-prioritized WAN Role. If only WAN1 is configured, Cellular shall be WAN2. If WAN2 is configured, Cellular shall be WAN3. Cellular default precedence is Last-Resort.

### Connection Status

The Cellular tab in the Socket WebUI can be a good starting point to identify the status of the Cellular connection. The following chart shows the different connection statuses with the possible related issues.

| Connection Status | Description | Possible Issues | Possible Solution |
| --- | --- | --- | --- |
| failed | The modem is unusable. | - No identified SIM Card - Wrong active slot | - Insert a new SIM Card and reboot the modem - Set the correct active slot in Network Settings |
| unknown | State unknown or not reportable. | - | - Reboot the modem |
| locked | The modem needs to be unlocked. | - Locked SIM | - Enter the PIN number in the Cellular tab |
| disabled | The modem is not enabled and is powered down. | - Cellular interface is disabled | - Set the interface destination as Cato in the CMA's Socket page. - Reboot the modem |
| disabling | The modem is currently transitioning to the Disabled state. | - | - |
| initializing | The modem is currently being initialized. | - | - |
| inactive | The modem is enabled and powered on but not registered with a network provider and not available for data connections. | - Registration failure with the carrier's network | - Activate Data Plan with the carrier. |
| searching | The modem is searching for a network provider to register with. | - | - |
| registered | The modem is registered with a network provider, and data connections and messaging may be available for use. | - Wrong APN | - Insert the correct APN in Network Settings |
| disconnecting | The modem is disconnecting and deactivating the last active packet data bearer. This state will not be entered if more than one packet data bearer is active and one of the active bearers is deactivated. | - | - |
| connecting | The modem is activating and connecting the first packet data bearer. Subsequent bearer activations when another bearer is already active do not cause this state to be entered. | - | - |
| connected | One or more packet data bearers is active and connected. | - Cellular connection is up | - |

### Basic Connectivity Troubleshooting

If the Cellular interface fails to connect and auto SIM failover is not enabled, continue with the next steps below:

- Check the SIM Card Status
  - Ensure that the SIM card is properly inserted and not damaged.
  - Ensure that the right SIM Slot is configured as active on the WebUI’s network settings page.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16310071591709(1).png)
- ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36483334049053.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36483347868445.png)
  - You can also view the active SIM Slot in the Topology. The Socket page will show the slot green when the SIM card is detected and gray when it's not detected.
- Check the Signal Bars

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36483334050717.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36483334050845.png)
  - Check the signal strength indicator from the Topology or Socket page. To do this, hover over the connection status of the Cellular interface.
  - If the Signal is very low, confirm Cellular coverage in your area using the carrier’s network coverage map.
  - Move the Socket to an open area for better reception if this indicator is too low.
- Check the APN Settings
  - The Access Point Name (APN) value is usually auto-assigned by the modem. Either by the “Common APN” list or by the cellular carrier network.
  - Verify the correct APN settings in the WebUI (Network Settings).
  - If the APN needs to be entered manually, use the override option to modify the APN. This value supports up to 64 characters.
    - Find the correct APN to set from the carrier's website.
    - Some carriers require a username and a password. Modify Cellular network settings according to the carrier’s requirements or leave them blank.
    - The credentials won’t show in the UI after reloading the page due to security measures.
  - One indication of APN misconfiguration is SIM detected but no connectivity to Cato.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16310243678237(1).png)
- 
  - Once the network settings page is updated, the Socket will initiate a connection attempt.
- Reboot the Modem

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16311514696861(1).png)
  - Go to “Administration” in the WebUI and reboot the Cellular modem
  - This will not affect other processes/interfaces of the Socket.
  - This reboot process takes up to 30 seconds to happen.
  - This should “clear” all Cellular configurations and issues back to normal.
- Last-Resort: Reboot Socket
  - Go to “Administration” in the WebUI and reboot the Socket.
  - Alternatively, power-cycle the device if the Cellular interface remains down.

### Cellular Signal Quality Troubleshooting

The following tools can be leveraged to measure Cellular signal quality on the Socket:

- Cellular Tab in Socket WebUI.
  - For details about each field in the Cellular tab, see [References](/v1/docs/x1600-cellular-connectivity-troubleshooting#h_01HMYABFT6WV7YNPAGNV0WMABN).
  - Monitor RSSI, RSRP, SINR, and RSRQ for signal strength and quality. Review the signal strength and signal quality thresholds for each metric. See [References](/v1/docs/x1600-cellular-connectivity-troubleshooting#h_01HMYABFT6WV7YNPAGNV0WMABN).
  - When the Network Type is 3G, only Signal Strength is retrieved (No RSRP, RSRQ, RSSI, or SINR).
  - The values as refreshed each second.
  - You must factor in **both** signal strength and signal quality. It is possible to have excellent RSSI but disconnects because of poor RSRQ quality (and vice versa).
- Real-Time Tab in CMA.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16497422637469(1).png)
  - Use Cellular Analytics for real-time monitoring of Cellular metrics.
  - Excellent/Good/Poor signal levels can be found on this page.
  - Values are updated each second with a delay of 30 seconds.
- Cellular Tab in Network Analytics

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16497183131037(1).png)
  - Analyze signal behavior over time to identify trends (7-minute delay). Only the active SIM card will report stats.

### Data Usage Monitoring

- Cellular data plans are both pricy and crucial. You want to ensure the package you acquired is available for when there is an Internet outage (In case the Cellular is a backup).
- Use the Total Traffic widget from Network Analytics to analyze utilization, and use the filter to investigate trends in usage.

### Connection SLA for Cellular

Cellular connections are usually defined with a relatively high number of latency (distance) and packet loss due to environmental factors.

Make sure to configure permissive [SLA thresholds](/v1/docs/configuring-the-connection-sla-settings-for-active-passive-socket-sites) and [Last Resort Link](/v1/docs/configuring-a-last-resort-link) (if Cellular is configured as such) values for the site.

### Additional Tips

- **Analyze Trends:**
  - Identify patterns in signal quality metrics.
- **Interference Investigation:**
  - Investigate potential sources of interference.
- **Device Placement:**
  - Experiment with device placement for optimal signal reception.
- **Consider Changing Carrier:**
  - Explore alternative carriers if signal issues persist.
- **Best Practice - Dual SIM Cards:**
  - Implement dual SIM cards from different carriers for redundancy.
  - Monitor both SIMs and choose the best one as active.

## Resolving Discovered Issues

#### Signal Interference

[RSSI](https://wiki.teltonika-networks.com/view/RSSI) for Cellular is calculated from several other signal-related measurements: RSSI = wideband power = noise + serving cell power + interference power. For example, a Cellular modem might report an RSSI of -68 dBm (considered excellent), but:

**RSRP = -102 dBm (Poor)**

**RSRQ = -16 dB (Poor)**

**SINR = -1.8 dB (Poor)**

In this case, the signal quality is actually very poor. This could be due to the device being some distance away from the Cellular base station. It’s also possible that something is interfering with the signal, such as a building or other obstructions between the device and the tower. Weather conditions may severely affect cellular signals as well.

#### Locked SIM Card

If the SIM Card is newly acquired and hasn't yet been activated, the SIM may be locked. If that's the case, the lock status in the Cellular tab will show **locked**.

To solve this issue, enter the provided SIM PIN in the Cellular tab of the Socket webUI. If the PIN is accepted, the status will change to registered or connected.

#### SIM Card Failover

If Slot 1 is the active SIM card (by default) and Slot 2 is acting as standby, it may be possible that the Slot 2 carrier has better performance than Slot 1 at a given time.

To solve this issue, perform a failover to Slot 2 by making it the active Slot in the Web UI's Network Settings page. Just pulling out the Slot 1 SIM card will not perform a failover as it's required to have a SIM card in the first slot.

#### Performing Failover

To failover between two SIM cards please follow these steps:

- In Socket UI, browse to the Network Settings and scroll down to the "Cellular-> Cato" entry.
- If manual configuration is required, change "Select APN" to Override (if not already set) and add the required values including authentication (if required) and proceed to the next step.
- Select "SIM Slot 2" and click on update, at this point the Cellular modem will reset and will connect using the 2nd SIM card (this process can take up to a minute).

## Raising cases to Cato Support

Submit a [Support ticket](/v1/docs/submitting-a-support-ticket) with the results of the above troubleshooting steps. Include connectivity events from CMA and the results of the Cellular page in the Socket WebUI.

## References

**Disclaimer:** Measured or reported values vary by carrier and network environment. The thresholds displayed below are references based on documented Cellular tests. There is no black/white answer to what constitutes a good connection. Although signal strength may appear to be adequate, throughput speeds may vary due to dependencies on cellular tower loads.

#### Understanding Cellular Signal Strength and Quality

- Signal Strength - Signal Strength as indicated by the modem. Signal strength is shown as a percentage between 0 and 100%

|  | Signal strength | Description |
| --- | --- | --- |
| > 75% | **Excellent** | Strong signal with maximum data speeds |
| 50% to 75% | **Good** | Strong signal with good data speeds |
| 1% to 50% | **Poor** | Performance will drop drastically |
| 0% | **No signal** | Disconnection |
- RSSI - Received Signal Strength Indicator. RSSI is a negative value, and the closer to 0, the stronger the signal.

|  | Signal strength | Description |
| --- | --- | --- |
| > -65 dBm | **Excellent** | Strong signal with maximum data speeds |
| -65 dBm to -80 dBm | **Good** | Strong signal with good data speeds |
| -80 dBm to -95 dBm | **Poor** | Performance will drop drastically |
| <= -95 dBm | **No signal** | Disconnection |
- SINR - Signal to Interference plus Noise Ratio (A minimum of -20 dB SINR is needed to detect RSRP/RSRQ). Indicates the throughput capacity of the channel. As the name implies, SINR is the strength of the signal divided by the strength of any interference

|  | Signal strength | Description |
| --- | --- | --- |
| >= 20 dB | **Excellent** | Strong signal with maximum data speeds |
| 13 dB to 20 dB | **Good** | Strong signal with good data speeds |
| 0 dB to 13 dB | **Poor** | Reliable data speeds may be attained, but marginal data with drop-outs is possible. When this value gets close to 0, performance will drop drastically |
| <= 0 dB | **No signal** | Disconnection |
- RSRP - the Reference Signal Received Power is the power of the Cellular Reference Signals spread over the full bandwidth and narrowband

|  | Signal strength | Description |
| --- | --- | --- |
| >= -80 dBm | **Excellent** | Strong signal with maximum data speeds |
| -80 dBm to -90 dBm | **Good** | Strong signal with good data speeds |
| -90 dBm to -100 dBm | **Poor** | Reliable data speeds may be attained, but marginal data with drop-outs is possible. When this value gets close to -100, performance will drop drastically |
| <= -100 dBm | **No signal** | Disconnection |
- RSRQ - Reference Signal Received Quality is a C/I type of measurement, and it indicates the quality of the received reference signal (similar to EC/IO)

|  | Signal quality | Description |
| --- | --- | --- |
| >= -10 dB | **Excellent** | Strong signal with maximum data speeds |
| -10 dB to -15 dB | **Good** | Strong signal with good data speeds |
| -15 dB to -20 dB | **Poor** | Reliable data speeds may be attained, but marginal data with drop-outs is possible. When this value gets close to -20, performance will drop drastically |
| <= -20 dB | **No signal** | Disconnection |

#### WebUI Cellular tab

- Active SIM: Configurable from Socket Network Settings page. Default is 1
- Cellular Modem: The modem name.
- Modem Status: OK/Error/Unknown/partial_information.
- Connection Status: connected/connecting/disconnected/registered/locked/failed
- MDN/Number: Mobile Directory Number
- Serial Number: Serial of the modem
- IMEI: The **International Mobile Equipment Identity** (**IMEI**) is a numeric identifier, usually unique to mobile modems, usually a 15-digit number.
- IMSI: The **international mobile subscriber identity** is a number that uniquely identifies every user of a cellular network. Usually, it’s a 15-long digit number.
- Network Type: 3G/4G
- APN: The string that is assigned with the connection as the gateway of the network. This is automatically assigned and can be overridden in the “Network Settings” tab
- Signal Strength: shown as a percentage
- Operator ID (or Name): The unique ID of the operator (i.e 311480 = Verizon)
- ICCID: integrated circuit card identifier. Each SIM is internationally identified by its ICCID, which is unique, and usually 20 digits long.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16310780689693(1).png)
