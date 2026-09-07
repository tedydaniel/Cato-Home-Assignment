---
title: "Inconsistent Blocking of 'My Drive' in Google Drive with CASB"
slug: "inconsistent-blocking-of-my-drive-in-google-drive-with-casb"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/inconsistent-blocking-of-my-drive-in-google-drive-with-casb"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Inconsistent Blocking of 'My Drive' in Google Drive with CASB

## Issue

The following CASB rule has been configured to block users from accessing 'My Drive' in Google Drive. It is matched based on the '**Full Path URL**' containing 'my-drive'.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25574835744285.png)

However, the block to 'My Drive' was intermittent. Despite this rule, some users were blocked successfully, while others could still connect to 'My Drive' in Google Drive.

## Environment

TLS inspection enabled

## Troubleshooting

- When users accessed the URL directly - [https://drive.google.com/drive/my-drive](https://drive.google.com/drive/my-drive), the traffic was matched and blocked successfully by the CASB rule.
- However, if the user first visits the Google Drive homepage ([https://drive.google.com/drive/home](https://drive.google.com/drive/home)) and clicks "My Drive" in the left navigation pane, the page loads with a randomly generated URL. Even though the screenshot below shows [https://drive.google.com/drive/my-drive](https://drive.google.com/drive/my-drive) in the address bar, the HAR data reveals that no corresponding network request is made for the updated URL path.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25727456839197.png)
- This shows that the app relies on client-side routing. The browser does not send a new request for /drive/my-drive. Instead, JavaScript intercepts the action and updates the page content accordingly.
- As a result, the traffic fails to match the configured CASB rule, and the connection is not blocked.

## Solution

This technical limitation can only be resolved by Google changing how it loads its pages. A potential workaround would be to configure the rule to block based on Download, Upload, or View instead of blocking based on Full Path URL.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/25728909605021.png)
