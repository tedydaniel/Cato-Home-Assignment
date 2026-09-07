---
title: "Working with Managed Networks"
slug: "working-with-managed-networks"
updated: 2026-08-16T16:51:57Z
published: 2026-08-16T16:51:57Z
canonical: "knowledge.catonetworks.com/working-with-managed-networks"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working with Managed Networks

This article explains how to define Managed Networks in Cato Networks. Managed networks can be used as a parameter that you can base your Access policies on.

## Overview

Cato gives you granular control over how user traffic is routed and when Always-On is enforced, based on the type of network the user is connected to.

This network classification allows you to integrate with existing security architectures while ensuring consistent traffic handling across trusted, managed, and unmanaged environments.

The Cato Client determines its configuration at runtime using specific criteria, such as:

- Whether it identifies that it is behind a Cato site (Socket, IPsec, vSocket)
- Whether it can successfully receive a response from a pre-defined probe to a given destination

Based on these conditions, the Client applies one of the following behaviors:

- Behind a Cato site (Office Mode) - If the Client identifies that it is behind a Cato site, Office Mode is enabled and all traffic is routed through Cato.
- Behind a Managed Network - If the Client is not behind a site, it checks whether the network is defined as Managed. If so:
  - Managed Network (not trusted) - The tunnel to Cato is maintained, and the Split Tunnel policy is applied. Only certain traffic is routed through Cato (e.g., Internet-bound traffic), while other traffic is routed through the third-party firewall.
  - Trusted Managed Network - If the network is also marked as Trusted, Always on is suspended, the Client disconnects from the Cato tunnel, and all traffic is routed through the third-party firewall.
- Unmanaged Network - If the network is neither behind a site nor defined as Managed (e.g., your home WiFi, airport, hotel, coffee shop), it is considered a public network and treated as Unmanaged. All traffic is routed through Cato.

### Use Case - Gradual Onboarding to Cato

Company ABC has 70 offices and over 10,000 employees. They are a new Cato customer that will use the Cato Client for networking and security solutions with Always-on to provide Internet security (in line with the company’s UZTNA best practices). During the Cato onboarding process, the company will deploy the Clients over a few weeks, whereas SD-WAN will be gradually deployed in 20 offices over the next several months. The offices are protected by a third-party vendor until that time.

The company designates the network ranges for the physical offices as Managed networks. The admin creates a rule in the Split Tunnel policy to route the traffic based on the network source:

- Managed network - Users are connected behind a site that has not been onboarded to Cato. Only Internet traffic is routed to the Cato Cloud for added security.
- Unmanaged network - Remote users, all traffic is routed to the Cato Cloud

### Prerequisites

- Supported from Windows Client v5.17 and higher

## How We Detect a Managed Network

You can configure Network checks to define what is a managed network. The Client uses pre-defined probes to identify if the network the Client connected to is a Managed network. This check occurs every time the Client connects, after every network change, and every 30 seconds while connected.

The Client sends out probes to check for connectivity to different types of internal resources:

- **HTTPS resource request**: Define a URL that is only accessible when connected to the managed network. After accessing the URL, the Client verifies that the response is either HTTP 200 or HTTP 300 and then verifies that the certificate is trusted based on the local machine’s certificate store
- **DNS query**: Define a hostname for the Client to send a DNS request to, and the IP address that is the expected response
- **Ping to an IP address or URL**: Define an IP address or URL for the Client to ping. The Client verifies if there is a response with the ICMP protocol

![Managed_Network.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33814599279261(2).png)

If any of the checks are satisfied, the Source network is considered Managed. If all of the checks fail, the network is considered Unmanaged.

![Unmanaged_Network2.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33814614005533(2).png)

When behind a Cato site, the Client transitions seamlessly to Office-Mode as before.

For example, the internal company DNS server uses the hostname companyabc.local, and it resolves to 10.10.10.26. So you would define the Managed network as a DNS query that resolves to the host companyabc.local with that IP address.

## Configuring Managed Networks

To designate a network as managed, first create a Managed Network object in the Cato Management Application (CMA). This object represents a network, such as an office or known corporate location. The customer must also define the probe that the Client uses to identify when it is operating within this network. These probes may include DNS, HTTP, or Ping (ICMP packets). When the Client detects a match based on the defined probes, it classifies the network as managed and applies the relevant policies accordingly.

**Note:** You define up to 5 Network Checks with the type **HTTPS Response**.

![Trusted_Networks.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33814614036509(2).png)

**To configure managed networks:**

1. From the navigation menu, click **Access > Managed Networks**.
2. Click **New** and configure the following:
  - Name of the probe
  - (Optional) A description of the probe
  - Type of probe, i.e., HTTPS, DNS query, or ping
  - Hostname or IP address of the probe
3. Click **Save**.
4. Repeat steps 2 for each Managed Network.
5. Enable Managed Networks and click **Save**.

### Configuring Trusted Networks

For scenarios where you are routing all the traffic to the destination, and not to the Cato Cloud, you can define all of your Managed Networks as Trusted. When a host device connects to a Trusted Network:

- The Client identifies the network as a Trusted Network, Connect on Boot is disabled, [Always-On](/v1/docs/protecting-users-with-always-on-security) is bypassed, and the Client does not try to connect (or reconnect) to the Cato Cloud
- As long as the host device is connected to the Trusted Network, the Client remains disconnected, and the Split Tunnel policy is not applied
- Users still have the option to click **Connect** in the Client, and the device is connected to the Cato Cloud

For example, developers who need to access a dev environment that is protected by the Cato Cloud

**To configure all managed networks as trusted:**

1. From the navigation menu, click **Access > Managed Networks**.
2. Navigate to the **Settings** tab.
3. Select the **Define all managed networks as Trusted Networks** checkbox.
4. Click **Save**.
