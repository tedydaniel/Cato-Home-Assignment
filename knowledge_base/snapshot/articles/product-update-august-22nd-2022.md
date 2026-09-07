---
title: "Product Update - August 22nd, 2022"
slug: "product-update-august-22nd-2022"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/product-update-august-22nd-2022"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Update - August 22nd, 2022

## New Features & Enhancements

- **Use SDP Device Posture, Source Operating System and Source Country Conditions in Firewall Policies:** Starting on August 28, new source device settings are supported for WAN and Internet firewall rules and gives you the ability to include conditional access based on the actual device of the SDP user.
- **Enhancement to BGP for Azure vSocket HA:** Azure vSockets configured in an HA cluster now support BGP.
  - Requires Socket v14
- **Blocking Local Routing when a Site is Disconnected from the PoP:** If a site is temporarily disconnected from the Cato Cloud (for example moving to a different PoP), the default behavior for local routing is fail-open and the Socket allows the local routing traffic. You can change the behavior to fail-closed and block the local routing traffic for specific sites or the entire account. [Read more](/v1/docs/working-with-advanced-configuration-for-the-account).
  - Advanced configuration for the entire account (Assets > Advanced Configuration) or a specific site (Network > Sites > {site name} > Site Configuration > Advanced Configuration)
  - Requires Socket v15
- **Use the Socket WebUI to Reset Registration Data for a Socket:** After using the Cato Management Application to unassign a Socket, if you can't reassign the Socket to a different site, use the Socket WebUI to force the Socket to enter the unassigned state. [Read more](/v1/docs/managing-sockets).
  - After the Socket is unassigned, a notification is shown in the Cato Management Application that lets you assign the Socket to a different site
  - Requires Socket v15
- **Cato Management Application Enhancements:**
  - **Easier to Manage Always-On for SDP Clients:** Starting on August 28, you the Client Access > Connectivity Policy screen will have a new look and feel and improved usability.
    - Renamed to Always-On
    - Generate bypass codes and manage Always-On for all supported Client OS
  - **Sockets Inventory Screen Shows Status of Installed and Ordered Sockets:** We are starting the gradual rollout of the Sockets Inventory screen which provides visibility for all of the Sockets in your account, including Sockets that Cato has already shipped. [Read more](/v1/docs/using-the-socket-assignment-page).
    - The screen shows the current Socket status, serial number, Socket version, and more.
    - For Sockets that have shipped, you can also see the shipping date, delivery carrier, and tracking number.
  - **Multi-Select for Items in Security Policies:** You can select multiple items when configuring a rule for the Security policy.
  - **Users Screen Sorted According to Connectivity Status:** The default for the behavior in the Users screen (Access > Users) is to show the SDP users according to the **Connectivity Status**.

## Cato SDP Client Releases

- **Feb 2023 - EoL for Windows and macOS Clients Earlier than v5.0:** On February 1, 2023, Cato is announcing End of Life (EoL) for our Windows and macOS Clients earlier than v5.0. After this date, Cato will no longer support these earlier Clients, and can’t guarantee that they will continue to work and connect to the network. Please upgrade to the newest Client versions before February 1, 2023. [Read more](/v1/docs/eos-for-windows-and-macos-clients-earlier-than-v5-0).

## Security Updates

- **IPS Signatures:**
  - CVE-2022-34713 (Dogwalk) - Microsoft Support Diagnostic Tool Directory Traversal
  - Malware BPFDoor (New)
  - Malware Malicious Beaconing (New)
  - Malware Cobalt Strike (Enhancement)
  - Usage of Trello for command and control (C2)
  - CVE-2022-33980
  - CVE-2022-28219
  - CVE-2021-46442
  - CVE-2021-46441
  - CVE-2021-44228 (Log4j, Enhancement)
  - CVE-2019-7195
  - CVE-2019-7194
  - CVE-2019-7193
- **Application Database:**
  - Added over 300 new applications, and updated 25 applications
  - You can view the SaaS apps in Monitoring > Cloud Apps Catalog
- **Application Control Policy:** New granular actions added to this app:
  - Zendesk – Export, Download, Upload

## Knowledge Base Updates

- [What is Cato's ZTNA Solution](/v1/docs/what-is-cato-s-ztna-solution)
- [Importing Users to Cato](/v1/docs/importing-users-to-cato)
- [Authenticating SDP Users](/v1/docs/authenticating-sdp-users)
- [Distributing Cato Clients to Devices](/v1/docs/distributing-cato-clients-to-devices)
- [Client Lifecycle Management](/v1/docs/client-lifecycle-management)
