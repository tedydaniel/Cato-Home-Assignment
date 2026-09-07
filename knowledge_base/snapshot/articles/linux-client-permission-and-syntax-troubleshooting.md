---
title: "Linux Client Permission and Syntax Troubleshooting"
slug: "linux-client-permission-and-syntax-troubleshooting"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/linux-client-permission-and-syntax-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Linux Client Permission and Syntax Troubleshooting

## Overview

The following article covers common issues with the SDP Linux Clients related to:

- Installation issues
- Login issues

## Installation Issues - Wrong Permissions

To complete the installation of the SDP Linux Client, see [Installing and Running the Linux Client v5.1](/v1/docs/getting-started-with-the-linux-client).

The most common issue during the installation of the Client is the permission issue, as seen in the picture below:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/12474531704477.png) To solve this permission issue, please ensure you have permission to run the file (sudoer). If you're still getting the following error, you should add execute permission to the installation file as explained below:

```plaintext
chmod +x <installation file>
```

Then run the command to install the Client again.

## Syntax Issues

Another common issue is syntax mistakes for connecting to Cato. Please take a look at our Installing and Running the Linux Client articles for more syntax options.

**Note:** If your username or password contains special characters, you must add apostrophes, for example: **'**@password1**'** instead of @password1.

After the session is established, you can check the connection status by using the commands of your currently installed version - [Installing the Cato Client](/v1/docs/preparing-to-install-the-cato-client)
