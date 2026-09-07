---
title: "Socket Deployment and Registration Troubleshooting"
slug: "socket-deployment-and-registration-troubleshooting"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/socket-deployment-and-registration-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Socket Deployment and Registration Troubleshooting

## Overview

Socket deployment is the first critical step onboarding a site to the Cato cloud. Failures to register a socket to the cloud represent the first hurdle in utilising the feature set that Cato offers. This playbook supports administrators in troubleshooting any issues they may face on socket deployment.

## Symptoms

A failure in socket registration can manifest in a number of ways. An administrator may note the following symptoms:

- No new socket notification when connecting socket to internet
- New socket notification is received but the initial firmware upgrade fails
- No site found when assigning a Socket
- Socket registered to site successfully but site goes offline shortly after
- Socket not assignable after unassigning from a site

## Possible Causes

The majority of cases in which registration is failing falls under the following causes:

- Registration mismatch between Socket and CMA
- DTLS tunnel Connectivity issues
- Scheduled license causes site to go offline.

## Troubleshooting the Issue

Steps to troubleshoot the symptoms an Administrator may encounter are listed below. These steps are intended to identify possible causes for the issues faced. The resolution steps will be highlighted later in the playbook.

### Troubleshooting No New Socket Notification When Connecting Socket

When a new socket is connected to the internet for the first time, it will reach out to Cato and begin upgrading to the relevant firmware. This is shown as a notification on the account in which the socket has been assigned to on purchase.

![Monosnap Cato|Liam-lab - Topology 2024-02-21 11-28-51.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16924724813085.png)

A failure to receive this notification suggests that the connection has not been completed successfully.

#### Checking Socket Connectivity

Ensure you are familiar with the [Cato Socket Connection pre-requisites](/v1/docs/cato-socket-connection-prerequisites-and-known-limitations).

The socket's connectivity status can be seen via it's local WebUI, see [Logging in to the Socket WebUI Locally.](/v1/docs/accessing-the-socket-webui#logging-in-to-the-socket-webui-locally-for-a-new-or-reimaged-socket) In order for the registration to succeed, the WAN port that is being used to service the connection to the Cato cloud should show a green status icon. An indicator other than green suggests a connectivity problem. The meaning of different status icon colours is described in [Understanding the Link Status Icons](/v1/docs/accessing-the-socket-webui)

![thumbnail_image.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16946436291741.png)

For a red icon ensure that there is a working physical link between the socket and the ISP device.

A warning icon will indicate other types of connectivity issues, such as IP conflict. If the WebUI reports an IP conflict issue, see [IP Address Conflict Reported](/v1/docs/ip-address-conflict-reported-on-socket-ui-even-after-it-s-resolved)

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17460650053405.png)

In the event of a connectivity problem we can utilise the **Tools** tab to further test. In order to register to Cato, the socket requires L3 access to the CMA using the hostname cc2.catonetworks.com, or the hardcoded IP address. To identify the IP address, see [Source IP Address for the Cato Management Application](https://support.catonetworks.com/hc/en-us/articles/20511945810589) (you must be signed in to view this article). Use the ping tool to ensure that this hostname and IP address are reachable over the WAN port directly. If neither are reachable please view the [resolving connectivity issues](/v1/docs/socket-deployment-and-registration-troubleshooting#resolving-connectivity-issues) section.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16944889642909.png)

Ensure that the WAN IP address is excluded from SSL/TLS inspection performed by any device in the upstream direction.

If these tests pass, a [packet capture](/v1/docs/how-to-capture-traffic-on-a-socket) can also be performed to ensure that the socket's registration request to CMA is being responded to. When capturing on the WAN port in question, bi-directional packets on TCP/443 to CMA and UDP/443 to the PoP should be seen.

**TCP connection to cc2.catonetworks.com**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/34094461456285.png)

**UDP connection to the PoP**

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16985464951709.png)

If only outbound DTLS packets are detected please view [resolving DTLS traffic one way only](/v1/docs/socket-deployment-and-registration-troubleshooting#resolving-dtls-traffic-one-way-only).

#### Checking Socket Registration Status

In order for a new socket with internet connectivity to produce a notification in your account, it has to be assigned to the relevant account. In order to verify the registration status of all sockets assigned to an account, view the sockets inventory under **Account** > **Sockets Inventory**.

![16302436a9beb2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16931866393245.png)

By searching for the MAC or serial of a given socket, it can be determined whether the socket is assigned to your account correctly and what the CMA's current view of registration status is. An administrator connecting a new socket to the internet can expect the socket to move from status **Delivered** to **Installed** as described in [Showing All Sockets in the Account (Sockets Inventory)](/v1/docs/using-the-socket-assignment-page)

If the socket does not appear in the inventory, or the socket registration status does not move to **Installed** when connected to a working internet connection please view the [Resolving Registration Mismatch Settings](/v1/docs/socket-deployment-and-registration-troubleshooting#resolving-registration-mismatch-settings) section.

#### Virtual Socket Registration

Unlike physical Sockets, vSockets do not need to be pre-added to the account's Socket Inventory. Once a vSocket site is created in CMA, it enters a 'Pending' state until the deployment on the cloud platform is complete.

After successful deployment and internet access via the WAN interface, the vSocket automatically registers with the Cato Cloud, triggering a 'New Socket Detected' notification in CMA, containing the vSocket's WAN public IP.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24796048501789.png)

If this notification does not appear, follow these troubleshooting steps:

- Verify Internet Access – Ensure the vSocket's WAN interface has internet access. Check Network Security Group (NSG) rules and the WAN subnet routing table for any restrictions.
- Restart the vSocket – Try rebooting the vSocket instance from the cloud platform.
- Re-deploy as a Last Resort – If the issue persists, [unregister the vSocket](/v1/docs/unregistering-and-redeploying-azure-vsockets) from CMA → **Site Configuration → Socket**, then redeploy it. After re-deployment, monitor CMA for the notification.

### Troubleshooting Failed Initial Firmware Upgrade

When a newly deployed Socket first connects to the Internet, it will continuously attempt to reach out to Cato via its WAN port using port TCP/443, and it will attempt to upgrade its firmware version.

If there are no "Socket upgraded successfully" or "Activate New Socket" Notifications in CMA, ensure a socket's connectivity to the internet is being serviced correctly by viewing the troubleshooting steps for [Checking Socket Connectivity](/v1/docs/socket-deployment-and-registration-troubleshooting#checking-socket-connectivity)

If the connectivity of the socket is verified in the above steps, please view the [resolving registration status mismatches](/v1/docs/socket-deployment-and-registration-troubleshooting#resolving-registration-mismatch-settings) section.

### Troubleshooting No Site Found when Assigning a Socket

As mentioned in [Managing Sockets](/v1/docs/managing-sockets), when the 'New Socket' notification is received in CMA, the next step is to assign the Socket to an already-configured site. However, if the configured site does not show listed or the window shows 'No Results', verify that the Connection Type configured in the site's general settings matches the Socket model installed on the site.

For example, if the Site is configured as connection type Socket X1600 LTE, the Socket model installed on the site must be an X1600 LTE model.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/20540978117789.png)

### Troubleshooting Socket Goes Offline Shortly After Successful Register

Ensure your socket [still has connectivity](/v1/docs/socket-deployment-and-registration-troubleshooting#checking-socket-connectivity).

If after the new socket detected notification was received, and the initial firmware upgrade completes successfully, the socket goes offline after a brief time, check the following:

- In the CMA, **Account** > **License** > **Bandwidth**, ensure that the license shown in the Plan column is Trial or Commercial.
- If the license status is scheduled, it will cause the Socket to disconnect after being added to the Site. See [License Life Cycles for Accounts and Sites](/v1/docs/working-with-cato-license-types) for more information on scheduled licenses.

If you see the License is scheduled, please view the [Resolving Scheduled license Causing Site to Go Offline](/docs/socket-deployment-and-registration-troubleshooting#h_01HQ6ANM80VPK72K9GBKTAJ9S3) section.

If your license is correct, follow the reset process outlined in [Resolving Registration Mismatch Settings.](/docs/socket-deployment-and-registration-troubleshooting#h_01HQ6AJJ08Y7XY1T3V8VBK6PBP)

### Troubleshooting Socket Not Assignable after Unassigning From Site

[Unassigning a socket](/v1/docs/managing-sockets#h_01HTVS0KT1EFCVQ076PGJJNEB4) from a site is the main action in making a socket assignable to a different site. This however must be done while the socket is online. If, after unassigning, the socket does not get detected as new within your notifications, follow this troubleshooting flow.

#### Checking Registration Status in CMA and in Socket

In order to verify the registration status of all sockets assigned to an account view the sockets inventory under **Account** > **Sockets Inventory**.

![16302436a9beb2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16931866393245.png)

By searching for the MAC or serial of a given socket, it can be determined whether the socket is assigned has correctly been unassigned from a site from the CMA's point of view. An administrator should expect that an unassigned socket will move to the **Installed** state.

The registration status of the socket according to CMA should match with the socket's own view. The socket's view can be checked by accessing the WebUI of the socket, see [Logging in to the Socket WebUI Locally.](/v1/docs/accessing-the-socket-webui#logging-in-to-the-socket-webui-locally-for-a-new-or-reimaged-socket)

The socket's registration target is visible on the main page of the WebUI in the format ' | <sitename>.<accountname> | ' in the location shown below. ![Monosnap Cato Networks - Monitor 🔊 2024-02-21 17-08-20.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16932175645213.png)

If this doesn't account for the unregistering of the socket, please follow the troubleshooting flow outlined in [Checking Socket Connectivity](/v1/docs/socket-deployment-and-registration-troubleshooting#checking-socket-connectivity).

If connectivity appears to be fine, please view the [resolving registration status mismatches](/v1/docs/socket-deployment-and-registration-troubleshooting#resolving-registration-mismatch-settings) section.

## Resolving Discovered Issues

### Resolving Connectivity Issues

It is important to isolate if connectivity issues only affect the socket. If you plug a laptop into the same ISP connection, do you encounter the same issues with resolving DNS or pinging addresses? If so reach out to your ISP in order to progress.

If the connectivity issues are isolated to your socket, ensure that the IP configuration is correct under the **Network Settings** tab of the WebUI:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16945768577693.png)

If these settings are correct, ensure with your provider that DTLS traffic on UDP port 443 is allowed to egress towards the internet. If necessary, this port can be changed as described in [Setting a Different Port to Connect to the Cato PoP](/v1/docs/setting-a-different-port-to-connect-to-the-cato-pop).

### Resolving DTLS Traffic One Way Only

Ensure with your provider that DTLS traffic on UDP port 443 is allowed to egress towards the internet. If necessary this port can be changed as described in [Setting a Different Port to Connect to the Cato PoP](/v1/docs/setting-a-different-port-to-connect-to-the-cato-pop).

### Resolving Registration Mismatch Settings

If there is a mismatch of the CMA and the Socket as to the register status, then a reset of the Socket can be performed to restart the registration process. Before carrying out a reset, first determine if the Socket has previously been registered to a site.

In the **About** tab, a Socket that has not previously been registered to a site will display the message **"Still not registered in CC2"** as shown below:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16993223675165.png)

For a Socket that has not been registered to a site, reset the socket by pressing the **Reset/FD button** for 30-35 seconds as described in [Resetting the Admin Password and Resetting a Socket](/v1/docs/managing-sockets#h_01HTVS0KT1TGSZNY8M9ACAX812).

For Sockets with a site registration, while the Socket is not connected to the Cato cloud, click 'Unassign' from the **Administration** tab to reset the socket.

![thumbnail_image (1).png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/16993223717149.png)

In both instances, ensure that the Socket is also unassigned from any assigned site in CMA.

### Resolving Scheduled license Causing Site to Go Offline

Please contact your Cato SE or CSM representative to have the license updated.

## Reaching Out to Cato Support

If following this playbook has not resolved an issue, submit a [Support ticket](/v1/docs/submitting-a-support-ticket) with the results of the above troubleshooting steps. Include connectivity test results and confirmation that a reset has been performed as per the above instructions.
