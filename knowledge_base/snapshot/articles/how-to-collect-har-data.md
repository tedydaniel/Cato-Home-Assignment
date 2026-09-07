---
title: "How to Collect HAR Data"
slug: "how-to-collect-har-data"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/how-to-collect-har-data"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Collect HAR Data

## Overview

HAR data is an invaluable tool when it comes to troubleshooting website and webpage connectivity issues. It provides valuable insights into the connections between a web browser and a server, offering crucial information that helps identify potential root causes.

This article provides an overview on how to capture HAR data in the commonly used browsers.

## Environment

[Google Chrome](/v1/docs/how-to-collect-har-data#google-chrome)

[Mozilla Firefox](/v1/docs/how-to-collect-har-data#mozilla-firefox)

[Microsoft Edge](/v1/docs/how-to-collect-har-data#microsoft-edge)

[Apple Safari](/v1/docs/how-to-collect-har-data#apple-safari)

## Instructions

In this section, we will show you how to capture the HAR data on some of the commonly used browsers in Windows and Mac.

### Google Chrome:

1. Open Google Chrome on your computer.
2. Go to the webpage or website for which you want to capture the HAR data.
3. Right-click anywhere on the page and select "Inspect" from the context menu. Alternatively, you can use the keyboard shortcut Ctrl + Shift + I (or Command + Option + I on a Mac).
4. This will open the Chrome Developer Tools panel. Make sure you are in the "Network" tab within the Developer Tools.
5. Click the "Record" button (a small circle) at the top-left corner of the Developer Tools panel. It should turn red to indicate that network requests are being recorded.
6. Interact with the webpage, performing actions or reproducing the connectivity issue you want to capture.
7. Once you have reproduced the issue or gathered the desired data, click the "Stop" button (a small square) in the Developer Tools panel. It will stop recording network activity.
8. You can now explore the captured network requests and data within the Network tab. You can filter, sort, and analyze the requests as needed.
9. To save the captured data as a HAR file, click the download button (Export HAR) in the toolbar. Choose a suitable location to save the HAR file and provide it with an appropriate name.

### Mozilla Firefox:

1. Open Mozilla Firefox on your computer.
2. Go to the webpage or website for which you want to capture the HAR data.
3. Right-click anywhere on the page and select "Inspect Element" from the context menu. Alternatively, you can use the keyboard shortcut Ctrl + Shift + I (or Command + Option + I on a Mac).
4. This will open the Firefox Developer Tools panel. Make sure you are in the "Network" tab within the Developer Tools.
5. The recording should start automatically.
6. Interact with the webpage, performing actions or reproducing the connectivity issue you want to capture.
7. Once you have reproduced the issue or gathered the desired data, to save the captured data as a HAR file, right-click anywhere within the Network tab and select "Save All As HAR.". Choose a suitable location to save the HAR file and provide it with an appropriate name.

### Microsoft Edge:

- Open Microsoft Edge on your computer.
- Go to the webpage or website for which you want to capture the HAR data.
- Right-click anywhere on the page and select "Inspect" from the context menu. Alternatively, you can use the keyboard shortcut Ctrl + Shift + I (or Command + Option + I on a Mac).
- This will open the Microsoft Edge Developer Tools panel. Make sure you are in the "Network" tab within the Developer Tools.
- Click the "Record" button (a small circle) at the top-left corner of the Developer Tools panel. It should turn red to indicate that network requests are being recorded.
- Interact with the webpage, performing actions or reproducing the connectivity issue you want to capture.
- Once you have reproduced the issue or gathered the desired data, click the "Stop" button (a small square) in the Developer Tools panel. It will stop recording network activity.
- You can now explore the captured network requests and data within the Network tab. You can filter, sort, and analyze the requests as needed.
- To save the captured data as a HAR file, right-click anywhere within the Network tab, Hover over the Copy option and select "Copy all as HAR (with sensitive data)". Choose a suitable location to save the HAR file and provide it with an appropriate name.

### Apple Safari:

1. Open Safari on your Mac computer.
2. Go to the webpage or website for which you want to capture the HAR data.
3. Enable the Develop menu in Safari if it is not already visible. To do this, go to Safari > Settings. In the Settings window, click on the "Advanced" tab, and then check the box that says "Show Develop menu in the menu bar." ![developmenu.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/11226975721117.jpeg)
4. Once the Develop menu is enabled, go to the Develop menu in the menu bar and select "Show Web Inspector." ![webinspector.jpg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/11226950283549.jpeg)
5. This will open the Safari Web Inspector panel. Make sure you are in the "Network" tab within the Web Inspector.
6. Interact with the webpage, performing actions or reproducing the connectivity issue you want to capture.
7. You can now explore the captured network requests and data within the Network tab. You can filter, sort, and analyze the requests as needed.
8. To save the captured data as a HAR file, right-click anywhere under the Name column and select "Export HAR" Choose a suitable location to save the HAR file and provide it with an appropriate name.
