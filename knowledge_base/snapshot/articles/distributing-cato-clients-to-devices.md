---
title: "Distributing Cato Clients to Devices"
slug: "distributing-cato-clients-to-devices"
updated: 2026-07-06T14:30:20Z
published: 2026-07-06T14:30:20Z
canonical: "knowledge.catonetworks.com/distributing-cato-clients-to-devices"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Distributing Cato Clients to Devices

The Cato Client is installed on the user device and connects to the Cato Cloud to provide secure granular, policy-based remote access.

## Overview of the Cato Client

The Client is Cato's software that lets users access their organization’s data and applications with Cato's global private backbone, the Cato Cloud. The Client automatically connects to the optimal Cato PoP, the traffic is inspected by all the relevant security services for the account before reaching the destination.

- Windows
- macOS
- Linux
- iOS
- Android and Chromebook

### Remote User Licenses for the Cato Client

> [!NOTE]
> Note:
> 
> Cato account licenses use one of two models. This section applies to the Enforcement Model only and is not relevant to the [Bursting Model](https://knowledge.catonetworks.com/docs/jan-2027-license-bursting-model) (starting in January 2027). Not sure which license model your account uses? See [Identifying your License Model](https://knowledge.catonetworks.com/docs/identifying-your-license-model).

Each remote user requires a separate ZTNA license to use the Client to connect to the network. When a user is disabled, that user is not assigned a ZTNA user license, and you can assign that license to a different user. Disabled users can't use the Client to connect to the network. For more information about ZTNA licenses, see [Working with Cato License Types](/v1/docs/working-with-cato-license-types).

## Installing the Client on Devices for Remote Users

Cato supports manually installing the Client on devices and also managed deployment solutions. End-users can install the Client manually on individual devices, or you can use your organization’s device management mechanism to deploy the Client. Admin permissions on the device are required to install the Client.

You have the account option to automatically send an invitation email to new users with the account name, SDP user name, and a link to the [Client download portal.](https://clientdownload.catonetworks.com/)

### Installing the Client Using a Managed Deployment Solution

You can use managed solutions (such as Group Policy (GPO) or an MDM) to deploy the Client to devices in your organization. Add the Client install file to the solution and then deploy it to the relevant users.

For more information about deploying the Client with managed solutions, see:

- [Deploying and Upgrading macOS Clients with an MDM](/v1/docs/deploying-and-upgrading-macos-clients-with-an-mdm)
- [Managing the Rollout of Client Versions (Client Upgrade Policy)](/v1/docs/managing-the-rollout-of-client-versions-client-upgrade-policy)

### Manually Installing the Client

Remote users with Windows, macOS, and Linux devices can download the newest version of the Cato Client directly from the [Client download portal.](https://clientdownload.catonetworks.com/)

For iOS and Android devices, the Clients are available to download from the App Store and Google Play Store.

For more information about installing the Client on a supported OS, see [Cato Client Installation Guides](/v1/docs/cato-client-installation-guides).

For more information about downloading the installation file for the Windows, macOS, and Linux Clients, see [Downloading the Cato Client](/v1/docs/downloading-the-cato-client).

## Preparing to Install the Cato Clients on Devices

Cato recommends that you test the Client on all the computers and devices that require remote access in your organization. This lets you discover and resolve any issues related to the Client before it is fully deployed to all end-users.

Make sure that you review the prerequisites and the files and processes to allowlist in this article, [Installing the Cato Client](/v1/docs/preparing-to-install-the-cato-client).

## Installing the Cato Certificate on Devices

Several Cato features require that the Cato certificate is installed on devices as a root certificate. The Cato certificate is automatically installed for Windows and macOS Clients. For more information, see [Installing the Cato Client](/v1/docs/preparing-to-install-the-cato-client)
