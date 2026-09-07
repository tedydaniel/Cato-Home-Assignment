---
title: "Defining Browser Access to Remote Hosts"
slug: "defining-browser-access-to-remote-hosts"
updated: 2026-08-31T13:30:52Z
published: 2026-08-31T13:30:52Z
canonical: "knowledge.catonetworks.com/defining-browser-access-to-remote-hosts"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Defining Browser Access to Remote Hosts

This article explains how to define hosts that users can access with a web browser over supported protocols (i.e. RDP or SSH).

## Overview of Browser Access Applications

You can extend the Browser Access Portal to provide secure remote access to specific hosts in your network. This eliminates the need to install the Cato Client, which can be helpful for contractors and third-party vendors who are using unmanaged devices.

When users log in to the Browser Access Portal, they only see the remote devices they are permitted to access. You can customize the name and icon for each device in the portal, however, each item represents access to one device.

When a user clicks the device in the portal, the application opens a remote connection either over RDP or SSH using the authentication details you provide when configuring the application connection.

For more information about working with Browser Access, see [Browser Access Portal Overview - Securing Remote Access to Applications.](/v1/docs/browser-application-portal-overview-securing-remote-access-to-applications)

### Limitations

The Browser Access Portal has the following limitations when defining access to a remote host:

- Touchscreen functionality is not supported
- Users connecting to a remote host via an RDP/SSH connection can't be connected to the Cato Cloud, neither behind a Socket nor via the Client.
- To enable file transfer, you must enable both the ​**Enable file transfer**​ and ​**File upload**​​ sliders.
- Only English QWERTY keyboard layouts are supported for ​connecting to a remote host via an RDP connection. Input from non-English keyboard layouts, such as Hebrew, may not be correctly transmitted or interpreted within the RDP session.
- Special characters (e.g., &, $, =, etc.) in passwords are not supported. If you use a special character, the connection will fail.

## Adding Access to a Host

When you add access to a host, define the connection parameters, such as the protocol, port, IP address, and more. Once you define the initial connection parameters, you can define additional settings, such as:

- How to authenticate to the remote host
- What actions you can take on the remote host, for example, copying and pasting content to and from the remote device
- How the connection is presented in the Application Portal, as well as the external URL for the remote host.

### Defining the Connection Parameters for the Remote Host

You must define the basic connection parameters, such as the protocol (RDP or SSH), host address, port, and more. Depending on the type of device you are connecting to, you have to set the necessary **Security Type**.

- If the remote host is a Windows VM and AD-joined, set the **Security Type** to **TLS**.
- If the remote host is a physical computer, set the **Security Type** to **NLA**.
- If you are connecting to a remote host using SSH, there is no **Security Type** setting.

### Configuring the Connection to the Remote Device

For each host that you are providing remote access to, create a new Browser Access application and define the settings for it. By default, Copy and Paste operations, as well as file transfers are disabled. You can enable these options when you configure the connection.

In addition, you can configure the look-and-feel, choose the icon that is shown in the Browser Access Portal, and the **Description** for the hover text.

Define a separate connection to each remote device you will need to access.

**To add a remote connection to a device:**

1. From the navigation menu, click **Access > Applications Portal**.
2. From the **Applications** tab, click **New**.

The **Add Application** panel opens.
3. Configure the **Connection Parameters**.
  - Under **Application Type**, select either **RDP** or **SSH** depending on the protocol you need to access the remote device
  - Under **Host Address** and **Port**, enter the IP address and port over which to connect to the remote device. For RDP, the default port is 3389 and for SSH, the default port is 22.
  - Configure after how long the **Session timeout** occurs. The session will timeout after the time configured whether the session was active or not.
  - For RDP connections, select the **Security Type**.
4. (Optional) Enter the **Authentication** parameters, for example, the **User Name** and **Password**, to connect to the remote host. If you do not provide this information in the connection definition, the user will be prompted to provide it when connecting.

> [!NOTE]
> Note:
> 
> If the remote host belongs to a domain, you must enter that information in the **Domain** field, for example, example.local. The user will not be able enter that information when they connect to the remote host.
5. Under **File Transfer**, configure the following:

> [!NOTE]
> Note
> 
> Currently, file transfer from the remote device is not supported.
  - Define the parameters for the SFTP host.

Make sure that the SFTP server is running and the relevant port is open in your firewall.
  - Determine whether to allow file transfer to the remote device.
  - If the SFTP server requires authentication, enter the credentials in the **Authentication for file transfer** section.
6. Configure **Additional Settings**, such as copying and pasting to and from the remote device.

> [!NOTE]
> Note:
> 
> The paste operation differs depending on the remote host connection method:
> 
> - For RDP, use CTRL + V
> - For SSH, use CTRL + SHFT + V
7. Define the **Application display settings** for the remote connection:
  1. In **Display Name**, enter the name that appears in the **Application Portal**.
  2. (Optional) Enter a description for the remote connection, for example, internal file hosting server.
  3. Under **URL Prefix**, enter the value of the URL Prefix that appears before the Application Portal URL. For example, SampleVM.
  4. **(Optional)** Upload an image file to display in the **Application Portal** to represent this connection.
8. Click **Apply**.
