---
title: "Getting Started with the Linux Client"
slug: "getting-started-with-the-linux-client"
updated: 2026-08-18T07:27:17Z
published: 2026-08-18T07:27:17Z
canonical: "knowledge.catonetworks.com/getting-started-with-the-linux-client"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with the Linux Client

This article explains how to install and run the Cato Linux Client v5.1.

## Overview

Starting with version 5.1, the Linux Client supports Device Posture checks that can be included in your Client Connectivity and Security policies. This version also includes support for user awareness, automatic upgrades that are managed by Cato and SSO without a browser.

### Prerequisites

- Review the Prerequisites (especially the minimum device operating system) listed in [Preparing to Install the Cato Client](/v1/docs/preparing-to-install-the-cato-client).
- For SSO and GUI-based features:
  - All Linux desktop versions are supported (e.g. Gnome and KDE)
  - Define a default browser for the device (generally the default setting is for GNOME)
  - Headless SSO is supported for Azure only. For more information on how to configure Azure SSO, see [Configuring Azure SSO for Your Account](/v1/docs/configuring-azure-sso-for-your-account)
- The installation and execution scripts are run from the CLI, and require you to open a terminal app

### Known Limitations

- Automatic re-authentication is not supported. End-users must re-authenticate to the IdP in the browser.

## Installing the Linux Client

Download the Client file and run it on your Linux device.

**To install the Client on a Linux device:**

1. From the [Client download portal](https://clientdownload.catonetworks.com/), select the Linux tab and download the Client.

The following file types are available:
  - .rpm (Red Hat Package Manager)
  - Debian (.deb)
2. Run the Client file:
  - For the .rpm file, enter the following command in the terminal: **sudo rpm -i cato-client-install.rpm**
  - For the Debian file, enter the following command in the terminal: **sudo dpkg -i cato-client-install.deb**

## Running the Linux Client

To connect the Client to the Cato Cloud on a browser based device, run the command: **cato-sdp start**

To connect the Client to the Cato Cloud on a headless (without a browser) based device, run the command: **cato-sdp start --account <account name> --user <remote user's email address>**

**Note:** The account name is the account Subdomain. To find the Subdomain, navigate to **Access > Single Sign-On**.

### Browser Authentication

On a device with a browser, after you run the start command, a browser opens. You can use the browser to authenticate to Cato using the authentication method configured for your account.

### Headless SSO (Authentication Without a Browser)

To authenticate with SSO on devices without a browser, you can use a different device that has a browser to authenticate on behalf of the headless device.

#### Overview of Headless SSO

You can use headless SSO to authenticate remote users in non-browser environments, for example, a command line tool or a printer, without requiring a browser. With headless SSO, you can use a different device that has a browser to authenticate on behalf of the non-browser device. After successfully authenticating through the browser, the non-browser device connects to the Cato Cloud.

Silent re-authentication is not possible with headless SSO. After the token expires, remote users are required to re-authenticate.

#### Authenticating with Headless SSO

Headless SSO lets you authenticate on devices without a browser.

**To authenticate on a headless device:**

1. On the headless device, run the command: **cato-sdp start --account <account name>**.

A unique code and URL are returned.

**Note:**

- The account name is the account Subdomain. To find the Subdomain, navigate to Access > Single Sign-On.

- For authentication without SSO, add the parameter --no-sso

- The --headless parameter is not required in version 5.1.0.21 and higher
2. On a device that has a browser, access the URL and enter the unique code.
3. Sign in with your SSO credentials.

The headless device is connected to the Cato Cloud.

## Actions for the Linux OS Client

These are the actions that you can use in the Linux Client. Precede each parameter with **cato-sdp**.

| Parameter | Description |
| --- | --- |
| start | The Client connects to the Cato Cloud |
| stop | The Client disconnects from the Cato Cloud |
| help | Displays the list of available arguments |
| status | Displays the connectivity status |
| version | Display the Client version |
| Support | Contact Technical Support |
| Update | Update the Client to the latest version |
| import-cert | Import device certificate |

## Arguments for the Linux OS Client

These are the optional arguments that you can use for different features and settings when you run the Client. Each parameter should be preceded by **cato-sdp start**.

| Parameter | Description |
| --- | --- |
| --address<PoP IP address> | The Client connects to a specific Cato PoP (contact Support for the specific IP address). The default behavior is that the Client automatically connects to the best PoP in the Cato Cloud. |
| --append {head\|tail} | Preserves the existing configuration in **/etc/resolv.conf**. When connected, the Client replaces **/etc/resolv.conf** with the DNS configuration received from Cato. Using this parameter appends the Cato configuration to the existing configuration. - head - adds the DNS configuration from Cato before the existing configuration, giving preference to the Cato configuration. - tail - adds the DNS configuration from Cato after the existing configuration, giving preference to the existing configuration. In both cases, **/etc/resolv.conf** is restored to its original contents on disconnection. If Split Tunnel is enabled in the Cato Management Application, this parameter is ignored, and the Client always replaces the contents of **/etc/resolv.conf** |
| --cato-sdp support | Download Client logs or send them directly to the Technical support team. |
| --floglevel --gloglevel | Sets the file (floglevel) or global (gloglevel) logging settings for the Client: - 0 - verbose - 1 - debug - 2 - info - 3 - warning - 4 - error - 5 - none |
| --headless --no-sso | The Client runs in headless mode. **no-sso** prompts the remote user for a password. Use this argument on a headless device in accounts with no SSO authentication configured. |
| --help | Shows the help screen. |
| --metric _metric_ | The route created for VPN traffic (see --route). If not specified, this route has the highest priority on the system (identical to specifying --metric 0). |
| --port | Changes the DTLS port (443 or 1337), port 443 is the default setting. |
| --reconn _seconds_ | Following a disconnect, the number of seconds the Client waits before attempting to reconnect. The Client attempts to reconnect at this interval until a connection is established or the client is stopped externally. If this parameter is not specified, the client attempts to reconnect once and if unsuccessful, exits immediately. |
| --reg_code | Uses a registration code to authenticate to the Client. |
| --route | A single subnet that is routed to the tunnel instead of the default route. For example: --route 10.24.0.0/16 creates a specific route so only this subnet is routed through the encrypted tunnel. If not specified, the Client adds a default route so all traffic is routed through the VPN on the device (identical to specifying --route 0.0.0.0/0). |
| --user, --account, --password, --reset-password, --reset-cred | Cato user credentials. These values are optional for users that authenticate with the web browser. **password** is optional. When a password is required, the user is prompted to add a new one. **reset-cred** resets all the user credentials and removes the authentication token (supported on v5.0 and higher). |
| --use-systemd-resolv | Uses **systemd-resolv** (instead of editing **/dev/resolv.conf directly**). The values for this parameter are: - 1 - true - 0 - false (default value) When using the **--use-systemd-resolv** parameter with the Client, do NOT use the **append** parameter. **Note:** We don't recommend using the **--password** argument. |
| --version | Shows information about the Client version. |
| --pin | Enter a MFA code |

### Arguments for Client File Parameters

You can save the arguments for the Linux Client to a file, and then load the parameters when you start the Client. These are the arguments for the Client file:

| Parameter | Description |
| --- | --- |
| --load_file_ | Uses the parameter values stored in the file previously with --save. You can override any stored setting by specifying it on the command line. Since the credentials are also stored in this file, make sure you keep it private, as anyone can use this file to connect with the saved credentials. Alternately, you can store an empty or incorrect password in the file and specify the correct one on the command line. For example: **--load _file_ --password '******'** |
| --save_file_ | Saves all arguments passed on the command line to the given file for use with the --load parameter. |
| --show_file_ | Displays the settings stored in the file using --save. |

## Arguments for Device Authentication with Certificates

This section contains arguments that are used for the Linux Clients that use Device Authentication with a device certificate. For more information, see [Distributing and Installing Device Certificates](/v1/docs/distributing-and-installing-device-certificates).

| Parameter | Description |
| --- | --- |
| --cert <certificate path> | Path to the certificate file for Device Authentication. The default path is: `/opt/cato/client_cert/device_cert.p12` |

## Uninstalling the Client

If you no longer need the Client on a device, you can uninstall it. Once the Client is uninstalled, there is no way for network rules or security policies to be applied to the device.

**To uninstall the Client:**

1. In the terminal, run the command for the file type that was installed:
  - .rpm `sudo rpm -e cato-client-install`
  - .deb `sudo dpkg -r cato-linux-install`
2. **(Optional)** After the uninstallation process is complete, remove the remaining configuration files in these locations
  - sudo rm -rf /opt/cato
  - sudo rm -rf /usr/lib/cato/
  - sudo rm -rf /var/log/cato*.log
  - sudo rm -rf ~/.cato/
3. Reboot your device.

If you made changes to your system network configuration during the Cato client installation, you may need to revert those changes manually.
