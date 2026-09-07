---
title: "How To Collect Console Logs on macOS"
slug: "how-to-collect-console-logs-on-macos"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/how-to-collect-console-logs-on-macos"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How To Collect Console Logs on macOS

## Overview

The console logs are written to the system logger from the operating system (OS) and external applications.

In many cases, the console logs are required to further investigate SDP Client issues and you should collect them while reproducing the issue and submit a ticket with Cato Networks. There is no need to interpret the logs, only collect, validate, and send them to Cato Support.

## Environment

macOS system with the built-in Console application (see Applications > Utilities).

## Collecting the Console Logs

> [!NOTE]
> Note:
> 
> Console logs are included in the log bundle starting with macOS SDP Client v5.6

**To collect the console logs on macOS:**

1. Open the **Console** application from your Launchpad or search bar.
2. Click the leftmost button in the toolbar to show the sidebar (make sure **All Messages** is selected in the tab bar).
3. If the **Activities** button in the toolbar is enabled with a blue icon, click it to turn this **off** and then click the **Start** button ![img1.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/4411037090193.png)
4. Now try to reproduce the issue that you were experiencing with the Cato Client.
5. Select all the logs.
  1. From the Console application, click **Pause**.
  2. Select the recent error messages from the main window, (or from the **Menu Bar** select **Edit > Select All**). ![img2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/4411031390353.png)
6. Copy the logs, from the Menu Bar, select **Edit > Copy.**
7. Open the TextEdit application and Paste the copied logs into a new plain text document.
8. Save the text document in .txt format, and upload the file to Cato Support. ![img3.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/4411031403153.png)
