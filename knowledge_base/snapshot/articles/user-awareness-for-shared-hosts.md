---
title: "User Awareness for Shared Hosts"
slug: "user-awareness-for-shared-hosts"
updated: 2026-08-05T10:30:19Z
published: 2026-08-05T10:30:19Z
canonical: "knowledge.catonetworks.com/user-awareness-for-shared-hosts"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# User Awareness for Shared Hosts

This topic provides information about configuring user awareness for shared hosts.

## Overview

Universal ZTNA (UZTNA) delivers identity-based, least-privilege access to private applications, SaaS, and Internet resources through its global SASE platform. It applies consistent user-to-application segmentation, real-time threat prevention, and device posture checks, enabling secure access for users across mobile, branch, and cloud environments.

![User_Awareness_-__Shared_Hosts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/28674318531613.png)

With user awareness for shared hosts, Cato lets you identify and track multiple users connecting from a single device, such as a Windows Terminal Server, Citrix environment, or Azure Virtual Desktop (AVD). Users connect to the shared device from their devices and can then access resources via the shared device according to your organization's policy.

User Awareness provides critical visibility into user activities, enabling more granular policy enforcement, improving security auditing, and enhancing threat detection. It ensures that access controls and monitoring remain effective, even in environments where multiple users share the same host.

> [!NOTE]
> Note:
> 
> - Cato recommends that you install the Cato Client for all of your users to get the benefits of user awareness, device posture, and experience monitoring capabilities.
> - This feature requires the Windows Client v5.15 or later

### Information Flow

Users connect from their device to the shared host located behind a site (Socket, vSocket, IPSec), for example, via an RDP session. Each user connection to the shared host is flagged with a key specific to that user. When traffic is sent from the shared host to the Cato Cloud over the GRE tunnel, the key is matched to the user identity, and the traffic is inspected and monitored based on the policies applied to that user or user group. For example, users from R&D might be granted access to a repository, but not to Salesforce, while Sales Engineers will be granted access to Saleforce, but not the repository.

By default, the traffic is sent using the default GRE IP protocol 47. For networks where sending GRE traffic is not possible (e.g., Microsoft Azure) or not desirable due to security or other restrictions, it is possible to encapsulate GRE traffic within UDP. This can be enabled using the registry key, [as described below](/v1/docs/user-awareness-for-shared-hosts#to-install-the-cato-client). Once enabled, all traffic is encapsulated in UDP and sent over port 4754.

> [!NOTE]
> Note:
> 
> Traffic is sent to the Cato system range from the Clients, which by default is 10.254.254.0/24, to terminate the GRE tunnel. Therefore, this destination must be routed to a Socket within the network that hosts the Clients.

For traffic that you don't want to send to the Cato Cloud, e.g., to a DNS server, you can configure exceptions so that it does not go through the GRE tunnel. This lets you keep local traffic in the LAN so that it does not have to go out to the PoP.

## Configuring User Awareness for Shared Hosts

To enable user awareness for shared hosts, you need to do the following:

1. Configure which traffic is sent through the shared host and which is not
2. Install the Cato Client on the shared hosts

### Configuring Traffic to the Shared Hosts

You can configure which shared hosts can communicate with the Cato Cloud via the GRE tunnel, and the traffic to exclude. For example, internet traffic should be sent via the GRE tunnel, but DNS traffic should be excluded.

![shared-host-newRule.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26963590772509.png)

**Configure traffic to the shared hosts**

1. Navigate to **Access > User Awareness** and click the **Shared Hosts** tab.
2. Click **New > New Rule**.
  1. In the **IP Address** field, select the host or CIDR to which to apply the rule.

IP ranges are not supported, e.g. 10.10.10.5-10.10.10.10.
  2. **Define Routing Exceptions** for traffic that should not be sent through the GRE tunnel, for example, to a DNS server or Active Directory.
3. Click **Save** and **Publish** to propagate the changes.

### Install the Cato Client on the Shared Hosts

You need to install the Cato Client on the shared hosts to enable the GRE tunnel.

![shared-hosts.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/26940676149149.png)

The following operating systems are supported:

- Windows Server 2019 and higher
- For Azure Virtual Desktop, Windows 10 or Windows 11

#### **To install the Cato Client**

1. Follow the instructions to [install the Cato Client](/v1/docs/preparing-to-install-the-cato-client).
2. Install via the command line and run:

`.\&lt;setup_file.exe&gt;/props="CATO_INSTALL_UATS=1"`
3. For Azure Virtual Desktop Windows 10 or Windows 11, after the installation completes:
  1. In the Windows Registry, navigate to HKEY_LOCAL_MACHINE\SOFTWARE\CatoNetworksVPN
  2. Create the DWORD GREOverUDP and set the value to 1
4. In the same Windows Registry location, to verify that the install was successful, ensure that the GREMode registry was created and the value is set to 1.
