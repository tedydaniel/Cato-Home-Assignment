---
title: "XOps Network Playbook - Socket Offline After Upgrade"
slug: "xops-network-playbook-socket-offline-after-upgrade"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-socket-offline-after-upgrade"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - Socket Offline After Upgrade

## Overview

Socket upgrade failures can occur during various stages, from initial deployment to scheduled maintenance windows and manual upgrades. Understanding and resolving these issues promptly is crucial for maintaining network integrity. This playbook is designed to walk you through a story in which your site could not establish a tunnel to the Cato Cloud after an upgrade.

## Step 1 - verify that the Site is Disconnected

- Navigate to Home > Stories Workbench and select the Network Operations Preset to find Site down stories that are not closed or not muted.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29088181328541(2).png)
- Navigate to Home > Events and search for events labeled Action Failed with the message "No open tunnel after grace time." These events indicate that the Socket was reported offline after the Socket Upgrade period ended (17 minutes).

## Step 2- Check Socket connectivity to Cato Cloud

- Sockets connectivity status can be checked through the socket WebUI. To access the socket WebUI locally, see [Logging in to the Socket WebUI Locally](/v1/docs/accessing-the-socket-webui).
- In the Socket Monitor Tab, verify the WAN port used to connect to the Cato Cloud. If the Link status shows down (Red), check if there is an active physical link between the socket and the ISP device. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29050366050717(2).png)
- If we have internet connectivity but no connection to the Cato Cloud, go to the Traffic Capture tab, select the relevant WAN interface, and start the capture. After one minute, click on Download & Stop. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29052289868189(2).png)
- Proceed to [Raising Cases to Cato Support](/v1/docs/xops-network-playbook-socket-offline-after-upgrade) section and provide all collected data.

## Step 3 - Resolving Socket Inaccessible after an upgrade

On-site personnel is required to perform the following steps:

> [!NOTE]
> Note:
> 
> Whenever possible, contact [Cato Support](/v1/docs/socket-upgrade-failure-troubleshooting) to collect Socket log files via console **before** rebooting the Socket. These logs are crucial for root cause analysis.

- **Collect Console Logs.** Connect a console cable to the Socket. Go to Device Manager > Ports, and note the COM port of the console cable. Open Putty or a similar terminal application and use the parameters below.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/29050394817693(2).png)

Save the console output in a text file for future investigation.
  - On physical Sockets, this step must be done before rebooting the Socket as Socket logs get lost after reboot.
  - For Azure vSockets, console logs can be obtained from Azure under the VM > Help > Boot diagnostics > Serial log > Download serial log. These logs are collected for up to 6 boots.
- **Reboot.** The next step is to reboot if the tunnel fails to establish or the Socket becomes inaccessible after an upgrade.
- **Unassign and Re-Assign Socket to Site.** If the reboot doesn't help bring up the tunnel/Socket, unassign the Socket in CMA. If the Socket is detected, it will appear in the CMA notification after a few minutes. Assign the Socket back to the same site.
- **Flash the Socket.** If there's no CMA notification, the next step is to flash the Socket to its factory default state. You can either press and hold the F/D button for 30-35 seconds or perform a USB reset to do that.
  - For **F/D reset**, follow [Resetting a Socket](/v1/docs/managing-sockets).
  - If the F/D reset didn't work for some reason, you can perform the **USB Reset**. Follow the below articles on how to perform the USB reset for the respective socket models: - [X1500](/v1/docs/how-to-reset-an-x1500-socket-usb-drive) - [X1500B](/v1/docs/how-to-reset-an-x1500b-socket-usb-drive) - [X1600](/v1/docs/how-to-reset-an-x1600-socket-usb-drive) - [X1700](/v1/docs/how-to-reset-an-x1700-socket-usb-drive) - [X1700B](/v1/docs/how-to-reset-an-x1700b-socket-usb-drive)
- **Contact Support.** Submit the collected console logs to Support and request to initiate an **RMA** process for the Socket. We recommend initiating this process if all the above steps have been performed and failed.

## Raising cases to Cato Support

Submit a [Support ticket](/v1/docs/submitting-a-support-ticket) with the results of the above troubleshooting steps. Please include the following information in the ticket:

- Details of the affected Sockets and overall impact.
- Related CMA events and notifications showing the Socket upgrade failure.
- Results of manual upgrades and maintenance window rescheduling.
- Collected console logs if the Socket becomes inaccessible.
