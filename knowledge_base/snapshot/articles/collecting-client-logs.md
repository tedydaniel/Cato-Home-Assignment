---
title: "Collecting Client Logs"
slug: "collecting-client-logs"
updated: 2026-07-22T12:06:31Z
published: 2026-07-22T12:06:31Z
canonical: "knowledge.catonetworks.com/collecting-client-logs"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collecting Client Logs

To support troubleshooting by the Cato Support team, you can send them logs from the Client. This article explains how to collect Client logs.

## Overview

Sometimes users experience issues while using the Client and Cato needs the logs to help understand and resolve the issue. To support troubleshooting issues, Cato Support may need to inspect user logs.

There are two ways to collect the Client logs from the Client:

1. **Contact Support Button**: This collects the Client logs and automatically sends them to Cato Support. The user is provided a reference number to help the Cato Support team identify the logs.
2. **Log Collector**: The user can download logs directly to their device.

From Windows Client v5.5 and higher, the Client Self Service tool records data on the device while the User replicates the issue. We recommend using the Client Self Service tool to collect Client Logs. For more information, see [Recording Issues Using the SDP Client](/v1/docs/recording-issues-using-the-cato-client).

## Collecting Logs with the Contact Support Button

In the Cato Client, clicking the **Contact Support** button collects the logs and automatically sends them to Cato Support. This prevents the user from downloading the file locally and then uploading it to a ticket. The Client prepares the logs and provides contact details for support and a unique reference number for the logs. If you are opening a ticket to Cato Support, include this reference number so they can identify the correct logs.

The Contact Support policy must be enabled. For more information, see, [Customizing the Cato Client.](/v1/docs/customizing-the-cato-client)

### Contacting Support in the Windows Client

In the Windows Client, the **Contact Support** button is found on the **Support** tab. Clicking this button collects the logs. Once the logs are collected, click **Send SDP Logs** to automatically send the logs to the Cato Support team and receive the reference number.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/client_support.png)

### Contacting Support in the macOS and iOS Clients

In the macOS, iOS Clients the **Contact Support** button is found on the **Support** tab. Clicking this button collects the logs, sends them to the Cato Support team, and provides you with the reference number.

| ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/macos_client_support.png) | ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/ios_support.png) |
| --- | --- |

### Contacting Support in the Android Client

In the Android Client, the **Contact Support** button is in the menu. Clicking this button collects the logs. Once the logs are collected, click **Upload Logs** to automatically send the logs to the Cato Support team and receive the reference number.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/android_support.png)

### Contacting Support in the Linux Client

In the Linux Client, in the terminal, run the command `cato-sdp support`. This automatically collects the logs, sends them to the Cato Support team, and provides you with the reference number.

## Collecting Logs with the Log Collector

The Contact Log Collector feature allows users to download the log files locally and upload them to a Support ticket.

### Using the Log Collector in the Windows Client

To collect logs on Windows devices, the user should press the Windows Start button and search for **Cato Log Collector**. Opening this application collects the logs, saves them on the device, and provides the path to where they are saved.

### Using the Log Collector in the macOS and iOS Clients

To collect logs on macOS and iOS devices, on the **Settings** tab of the Client, click **Download Logs**. On macOS devices, the logs are saved in the Downloads folder and you are provided with the file name. On iOS devices, the file is available to be shared via email or other methods.

### Using the Log Collector in the Android Client

To collect logs on Android devices, in the main menu of the Client, click **Contact Support**. Clicking this button collects the logs. Once the logs are collected, click **Send Logs to Admin** to share the logs via email or other methods.

### Using the Log Collector in the Linux Client

In the Linux Client, in the terminal, the log files are saved under **~/.cato/support**.

On Linux devices with a GUI, open the file folder and navigate to Home. Press Ctrl+H to reveal the hidden folders. Open the `.cato` folder, the logs are saved in the `Support` subfolder.

## Log Storage Limits

Depending on your client version, the following limits apply to the number and size of stored log files.

| Client Type | Max Log Files | Max Size per File |
| --- | --- | --- |
| Windows | 10 | 1 MB |
| Linux | 10 | 1 MB |
| macOS | 7 | 100 MB |
| iOS | 7 | 1 MB |
| Android | No limit, but files are deleted after 10 days | 1 MB |
