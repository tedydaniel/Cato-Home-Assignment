---
title: "Configuring High Availability (HA) for GCP vSocket Sites Using Terraform"
slug: "configuring-high-availability-ha-for-gcp-vsocket-sites-using-terraform"
updated: 2026-06-22T09:21:29Z
published: 2026-06-22T09:21:29Z
canonical: "knowledge.catonetworks.com/configuring-high-availability-ha-for-gcp-vsocket-sites-using-terraform"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring High Availability (HA) for GCP vSocket Sites Using Terraform

This article describes how to deploy a High Availability (HA) configuration for a GCP vSocket site.

## Overview

You can configure High Availability (HA) for Cato vSockets in Google Cloud Platform (GCP) by deploying two vSockets in separate zones and placing a Google Cloud Load Balancer in front of their LAN interfaces. The Load Balancer provides a single static IP address that internal resources use to connect to the vSockets. It continuously monitors the health of each vSocket and forwards traffic only to the active (master) vSocket. This can be either the primary Socket or, in case of a failover, the secondary.

In addition, the vSockets use Virtual Router Redundancy Protocol (VRRP) to exchange state information between them. When the secondary Socket is in standby mode, it reports to the Load Balancer as unhealthy so that traffic is forwarded only to the active vSocket. Together, the Load Balancer health checks and VRRP provide automatic failover with minimal disruption. Typical failover time is approximately 3–5 seconds.

> [!NOTE]
> Note:
> 
> The minimum supported vSocket version for HA in GCP is 24.0.20395.

HA vSocket configurations in GCP rely solely on the Load Balancer to direct traffic to the active vSocket.

### GCP vSocket Failover Workflow

This is the workflow when the primary active vSocket fails over to the secondary standby one in a GCP site.

1. In normal operation, the primary vSocket has the active role, and the secondary vSocket has the standby role.
  1. The load balancer probes the Sockets for their health status. The primary reports that it is healthy, the secondary reports it is unhealthy.
  2. The primary and secondary Sockets communicate over the LAN using VRRP protocol.
  3. The load balancer IP directs traffic to the primary vSocket’s IP.
  4. The LAN route table prefixes use the load balancer IP as the next hop.
2. The primary (active) vSocket goes down.
  1. The secondary (standby) vSocket stops receiving keepalive packets from the primary vSocket.
  2. The secondary vSocket assumes the active (master) role and starts reporting to the load balancer as healthy.
  3. The load balancer stops receiving responses from primary vSocket, and now directs traffic only to secondary vSocket.
3. The secondary vSocket is now the active vSocket and passes traffic for the site in both directions.
4. When the primary vSocket recovers, it resumes the active role, and the secondary vSocket returns to standby status. The load balancer now directs the traffic back to the primary vSocket.

## Prerequisites for Terraform Deployment

- A GCP project with permissions to create the following resources:
  - VPCs and subnets
  - Compute instances
  - Firewall rules
  - Load balancer
  - Health checks
  - Static IPs
  - Service accounts
- Terraform is installed and authenticated to GCP
- Cato account credentials or tokens required by the Terraform module
- Two availability zones in the target region (for example, us-central1-a and us-central1-b)
- (Optional) Reserved DNS name pointing to the Load Balancer’s static IP address
- Minimum vSocket version: 24.0.20395

## Reference Architecture

- Each vSocket includes three interfaces: MGMT, WAN, and LAN. The LAN interfaces participate in VRRP for state synchronization.
- The load balancer operates on the LAN side to provide a consistent IP address to internal clients.
- Health checks probe each vSocket’s LAN interface. Only instances that report to the load balancer as healthy receive traffic.
- VRRP ensures state synchronization between the two vSockets.

![GCP_HA_Diagram.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32642279663773(1).png)

## Using Terraform to Deploy HA for a GCP vSocket Site

All required resources (VPCs, vSockets, Load Balancer, and health checks) should be defined in a single Terraform stack.

The official Cato vSocket Terraform modules, available in the Terraform Registry, include detailed documentation and examples for vSockets in a High Availability configuration. For more information about the GCP HA module, see [here](https://registry.terraform.io/modules/catonetworks/vsocket-gcp-ha/cato/latest).

To extend the configuration for HA in GCP:

1. Deploy two vSockets across different zones using the same approach
2. Add a Load Balancer resource on the LAN side to front both vSockets
3. Allow VRRP communication between the two vSockets for state synchronization

> [!NOTE]
> Note:
> 
> Refer to the official Cato vSocket Terraform module documentation for details on module inputs, outputs, and advanced configuration options

## Managing GCP High Availability

This section explains how to manage HA for the GCP site:

- Show the HA status for each vSocket
- Change the load balancer IP for the site
- Change the management IP addresses for the vSockets
- Disable HA for the site and remove the secondary vSocket

### Showing the High Availability Information and Status

The **Network > Sites > Socket** page for the site shows the HA status for the primary and secondary vSockets.

| Item | Description |
| --- | --- |
| HA Status | The High Availability status for the site (**Ready** or **Not Ready**) only shows Ready when each HA status indicator is OK |
| **Connected** (status indicator) | The status ![allow.svg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32642293639453.svg) indicates that both vSockets have WAN connectivity to the Cato Cloud |
| **Keepalive** (status indicator) | The status ![allow.svg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32642293639453.svg) indicates that one vSocket is the master and one is the standby (If both vSockets are status master, then there is an HA split brain issue) |
| **Same Version** (status indicator) | The status ![allow.svg](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/32642293639453.svg) indicates that both vSockets are running the same Socket version |

### Changing the IP Settings for the Site

If you change the IP address settings for the vSockets in GCP, you need to update the same settings in the Cato Management Application. These are the settings that you can configure:

- Native Range subnet - Use the **Networks** section for the site
- Load balancer IP - Use the **Networks** or **High Availability** section for the site (the new value is automatically updated in the other section)
- Management IP - Use the **High Availability** section for the site

#### Changing the Native Range Subnet

Use the **Networks** section to change the Native Range subnet.

**To change the Native Range subnet for the site:**

1. From the navigation menu, click **Network > Sites** and select the GCP site.
2. From the navigation menu, select **Site Configuration > Networks**.
3. Edit the **Native** range, enter a new value for the **Subnet**.
4. Click **Apply**. The **Edit IP range** panel closes.
5. Click **Save**.

#### Changing the Load Balancer IP and Management IP

Use the **High Availability** section to change the Load Balancer IP and the Management IP. You can also change the load balancer IP in the Networks section.

**To change the load balancer or Management IP for a site:**

1. From the navigation menu, click **Network > Sites** and select the GCP site.
2. From the navigation menu, click **Site Configuration > Socket**.
3. Expand the **High Availability Configurations** section.
4. Enter the new **Primary Management IP**.
5. Enter the new **Secondary Management IP**.
6. Enter the new **LAN Load Balancer IP**.
7. Click **Save**.

### Disabling High Availability for the GCP Site

You can remove the secondary vSocket from a GCP site and disable HA for that site. After you remove the secondary vSocket from the Cato Management Application, the deployed vSocket can no longer connect to the Cato Cloud. The settings for the site are restored to the configuration for a single vSocket:

- The **High Availability** section is disabled and no longer appears on the page
- In the **Networks** section, the Local IP replaces the Load Balancer IP

> [!NOTE]
> Note:
> 
> You can't undo the **Unassign Socket** action. The serial number for the secondary vSocket is no longer valid.
> 
> If you want to add the secondary vSocket again, you must install a new vSocket on the VM with the new serial number.

**To disable HA for the GCP site:**

1. From the navigation menu, click **Network > Sites** and select the GCP site.
2. From the navigation menu, click **Site Configuration > Socket**.
3. From the **Actions** menu of the **Secondary** vSocket, click **Unassign**.
4. In the Warning window, click **OK**. HA is disabled for the site, and the secondary vSocket is removed from it.

## Known Limitations

- In GCP HA deployments, failback to the primary vSocket can take longer than failover to the secondary vSocket. During failback, traffic can be interrupted for up to 8 seconds.
- During a split-brain condition in a GCP HA deployment, existing continuous ping traffic can continue through both the primary and secondary vSockets. This can cause GCP load balancer health checks to show both vSockets as healthy and make failover validation less clear, although new traffic initiated after the split-brain condition is routed only through the secondary vSocket.
