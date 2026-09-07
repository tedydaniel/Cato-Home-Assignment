---
title: "Socket Upgrade Failure Troubleshooting"
slug: "socket-upgrade-failure-troubleshooting"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/socket-upgrade-failure-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Upgrade Failure Troubleshooting

## Overview

Socket upgrade failures can occur during various stages, from initial deployment to scheduled maintenance window, and manual upgrades. Understanding and resolving these issues promptly is crucial for maintaining network integrity. Here's an overview of the troubleshooting process for addressing Socket upgrade failures.

## Symptoms

- Failed Initial Upgrade: Occurs during Socket deployment.
- Maintenance Window Issues: Large numbers of Sockets were not upgraded during scheduled maintenance.
- Established tunnel after failed upgrade: The Socket upgrade failed, but the tunnel remains up.
- Inaccessibility Post-Upgrade: Sockets become inaccessible after an upgrade.

## Possible Causes

- Connectivity Issues: Timeout due to slow internet or improper MTU settings.
- DNS Resolution Failures: Inability to resolve cc2.catonetworks.com.
- Firewall Restrictions: Firewalls with SSL inspection.
- Port Limitations: WAN1/Port1 restrictions.

## Reschedule Automatic Upgrades

If the reason the upgrade was missed was due to a flapping ISP link, which caused the automatic upgrade to be skipped for the entire account, we can [pause automatic upgrades](/v1/docs/manually-upgrading-a-socket) for the affected socket and [reschedule](/v1/docs/understanding-cato-s-managed-socket-upgrade-service#rescheduling-automatic-upgrades) the automatic upgrade for the next maintenance window.

Once the issue has been resolved, we can proceed to [manually upgrade](/v1/docs/socket-upgrade-failure-troubleshooting#cma-manual-upgrade) the problematic socket.

## Troubleshooting Socket Upgrade Failure

> [!NOTE]
> Note:
> 
> Before starting to troubleshoot, make sure to understand how Socket upgrades work at Cato in the following article: [Understanding Cato's Managed Socket Upgrade Service](/v1/docs/understanding-cato-s-managed-socket-upgrade-service)

Socket upgrades will take place during the configured [maintenance window](/v1/docs/configuring-the-socket-upgrade-maintenance-window) in CMA or during initial deployment. This section will delve into the steps involved in troubleshooting Socket upgrade failures. There are primarily three possible outcomes for upgrade failures:

1. The initial Socket Upgrade fails during Socket Deployment.
2. The tunnel remains up and established despite the upgrade failure.
3. The tunnel fails to come up and the Socket becomes inaccessible following the upgrade failure.

### Initial Upgrade Failure

When a newly deployed or factory-reset Socket first connects to the Internet, it will continuously attempt to reach out to Cato via its WAN port, and it will attempt to upgrade its firmware version.

To troubleshoot Initial Upgrade failures please see [Troubleshooting Failed Initial Firmware Upgrade](/v1/docs/socket-deployment-and-registration-troubleshooting#troubleshooting-failed-initial-firmware-upgrade)

### Tunnel is Established After an Upgrade Failure

During a maintenance window, the Socket upgrade process might not succeed resulting in an upgrade failure that prevents other Sockets in the entire account from being upgraded. It's important to identify the failed upgrades and focus on upgrading them before scheduling a new maintenance window.

#### Analyzing CMA Events

Review Socket upgrade-related events by filtering the *Sub-type* as **Socket Upgrade** and *Action* as **Not Succeeded**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18271182902941.png)

Events with action **Skipped** may indicate that the Socket was offline during the maintenance window or that a different Socket failed to upgrade (No open tunnel after grace time), which led to all the remaining Sockets being skipped. The reason for the skip action can be seen in the **Event Message**. For example:

- Upgrade was skipped. Primary socket was offline during maintenance window.
- Upgrade was skipped. Skipped pending upgrade for this Socket, because a different Socket couldn't complete the upgrade.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18271183826845.png)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18295421939229.png)

Events with action **Failed** indicate that the Socket upgrade was attempted but the upgrade process itself failed. The reason for the failed action can be seen in the **Event Message**

**![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19019826267421.png)**

If the Socket becomes inaccessible after this failure, go to [Tunnel Fails to Establish after an Upgrade](/v1/docs/socket-upgrade-failure-troubleshooting#tunnel-fails-to-establish-after-an-upgrade).

Continue the troubleshooting process by focusing on Sockets with action **Failed**.

#### Troubleshooting Failures During the Upgrade

During the upgrade process, the Socket will attempt to download the firmware image. Timeouts may occur due to the following reasons:

- Failure to resolve DNS properly for *cc2.catonetworks.com*
- Slow or unreliable internet connection prevents the firmware download.
- Improper MTU setting on WAN interfaces.

To rule out the above reasons, check the following:

- Use the Ping Tool from the [WebUI](https://support.catonetworks.com/hc/en-us/articles/4413265669905-Using-the-Socket-WebUI) to confirm that the Socket can resolve *cc2.catonetworks.com* via the tunnel. If the FQDN is not resolvable, check the DNS settings on the WAN port. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18272213596573.png)
- In [Network Analytics](/v1/docs/showing-the-site-network-analytics), check if the tunnel presented packet loss during the maintenance window. If so, check if there is also Last-Mile packet loss and report this issue to the ISP. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18272213602845.png)
- Cato Sockets run PMTUD (MTU discovery) with the PoP to determine the allowed MTU over the tunnel. However, manually setting the MTU on the WAN interface may lead to packet fragmentation and performance degradation. Check the configured MTU value in the WebUI. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18272213606301.png)

#### Troubleshooting Failures After the Upgrade

Once the firmware has been downloaded and installed on the Socket, the Socket will enter a grace period (10 minutes) where several checks are run to determine that the newly installed version is stable:

- The socket process is running.
- Ping works to cc2.catonetworks.com, 8.8.8.8, and Facebook over the internet
- The connection to the PoP is established for at least 5 minutes.
- There were at least ten successful syncs between the Socket and the PoP.
- cURL works to cc2.catonetworks.com via the tunnel.

If the checks aren't successful during the grace period, the Socket will roll back to the previous version, assuming that the new version is unstable. Ensure that the Socket keeps its internet access for 10 minutes after the upgrade is completed.

#### Performing a Socket Reboot

In some **Fatal** upgrade failures, rebooting the Socket may be helpful before re-trying the firmware upgrade. If the tunnel is still up after the upgrade failure, a remote Socket reboot can be done via [WebUI](/v1/docs/accessing-the-socket-webui) under the Administration tab.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/19019826268957.png)

If the Socket is inaccessible after the upgrade failure, go to [Tunnel Fails to Establish after an Upgrade](/v1/docs/socket-upgrade-failure-troubleshooting#tunnel-fails-to-establish-after-an-upgrade).

#### Manual Socket Upgrade and Rescheduling

Sockets with action **Skipped** during the maintenance window can be manually upgraded from CMA once the Socket is back online. Sockets with action **Failed** must follow the above troubleshooting steps before attempting to upgrade them manually. For information about manually upgrading in CMA see [CMA Manual Upgrade](/v1/docs/socket-upgrade-failure-troubleshooting#cma-manual-upgrade).

For large accounts, CMA manual upgrades may take a long time to complete. Instead of manually upgrading each Socket, it may be only necessary to troubleshoot and upgrade the Socket that failed (action **Failed**) during the first maintenance window and then schedule a new maintenance window. For information about re-scheduling a maintenance window in CMA see [Rescheduling the Upgrade Process](/docs/socket-upgrade-failure-troubleshooting#h_01HVPEVJC95R3GQBAHMVF6YVNV).

If the upgrade process continues to fail with the same or other Sockets, submit a [Support ticket](/v1/docs/submitting-a-support-ticket) with the results of the above troubleshooting.

### Tunnel Fails to Establish after an Upgrade

#### Analyzing CMA Events

Socket upgrade events with Action **Failed** and event message **No open tunnel after grace time** indicate that the Socket was reported offline after the Socket Upgrade period ended (17 minutes).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18272241941533.png)

On-site personnel will have to be on-site and follow the steps explained in [Resolving Inaccessible Socket after an Upgrade](/v1/docs/socket-upgrade-failure-troubleshooting#resolving-inaccessible-socket-after-an-upgrade).

## Resolving Discovered Issues

### CMA Manual Upgrade

An upgrade failure may have been caused by a momentary connectivity issue and could succeed the second time around. To attempt a new Socket upgrade, manually initiate the upgrade from Site Configuration > Socket > Actions > Upgrade. See [Manually Upgrading a Socket](/v1/docs/manually-upgrading-a-socket)

It is recommended to select the latest available firmware version with the upgrade mechanism being "Cato Cloud Initiated". 17 minutes after the manual firmware upgrade starts, CMA will show an "upgraded successfully" notification indicating that the Socket reported a successful upgrade after the grace period. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18290528146717.png)

### Resolving Inaccessible Socket after an Upgrade

On-site personnel will have to follow the following steps:

> [!NOTE]
> Note:
> 
> Whenever possible, contact [Cato Support](/v1/docs/socket-upgrade-failure-troubleshooting#raising-cases-to-cato-support) to collect Socket log files via console **before** rebooting the Socket. These logs are crucial for root cause analysis.

1. **Collect Console Logs.** Connect a console cable to the Socket. Go to Device Manager > Ports, and note the COM port of the console cable. Open Putty or a similar terminal application and use the parameters below.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18374864135709.png)Save the console output in a text file for future investigation.
  - On physical Sockets, this step must be done before rebooting the Socket as Socket logs get lost after reboot.
  - For Azure vSockets, console logs can be obtained from Azure under the VM > Help > Boot diagnostics > Serial log > Download serial log. These logs are collected for up to 6 boots.
2. **Reboot.** The next step is to reboot if the tunnel fails to establish or the Socket becomes inaccessible after an upgrade.
3. **Unassign and Re-Assign Socket to Site.** If the reboot doesn't help bring up the tunnel/Socket, unassign the Socket in CMA. If the Socket is detected, it will appear in the CMA notification after a few minutes. Assign the Socket back to the same site.
4. **Flash the Socket.** If there's no CMA notification, the next step is to flash the Socket to its factory default state. You can either press and hold the F/D button for 30-35 seconds or perform a USB reset to do that.
  - For **F/D reset**, follow [Resetting a Socket](/v1/docs/managing-sockets).
  - If the F/D reset didn't work for some reason, you can perform the **USB Reset**. Follow the below articles on how to perform the USB reset for the respective socket models: - [X1500](/v1/docs/how-to-reset-an-x1500-socket-usb-drive) - [X1500B](/v1/docs/how-to-reset-an-x1500b-socket-usb-drive) - [X1600](/v1/docs/how-to-reset-an-x1600-socket-usb-drive) - [X1700](/v1/docs/how-to-reset-an-x1700-socket-usb-drive) - [X1700B](/v1/docs/how-to-reset-an-x1700b-socket-usb-drive)
5. **Contact Support.** Submit the collected console logs to Support and request to initiate an **RMA** process for the Socket. We recommend initiating this process if all the above steps have been performed and failed.

## Raising cases to Cato Support

Submit a [Support ticket](/v1/docs/submitting-a-support-ticket) with the results of the above troubleshooting steps. Please include the following information in the ticket:

- Details of the affected Sockets and overall impact.
- Related CMA events and notifications showing the Socket upgrade failure.
- Results of manual upgrades and maintenance window rescheduling.
- Collected console logs if the Socket becomes inaccessible.
