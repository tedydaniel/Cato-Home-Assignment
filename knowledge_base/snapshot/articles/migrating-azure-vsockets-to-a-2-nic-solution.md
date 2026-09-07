---
title: "Migrating Azure vSockets to a 2-NIC Solution"
slug: "migrating-azure-vsockets-to-a-2-nic-solution"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/migrating-azure-vsockets-to-a-2-nic-solution"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrating Azure vSockets to a 2-NIC Solution

This article explains how to migrate an Azure vSocket from a VM with 3 network interfaces (NICs) to 2 NICs.

## Overview

This article provides information about Cato's supported Azure vSockets. Previously, Cato only supported Azure vSockets with 3 network interfaces. Starting with Socket v21, you can now create new Azure instances that have 2 interfaces, and migrate your existing vSockets to a 2-NIC instance.

The following sections explain how to migrate your existing vSockets to a Standard_D2s_v5 instance.

You are not required to migrate to a 2-NIC instance and can continue using the supported 3-NIC instances

### 2 NICs or 3 NICs

There are two main differences between the 2-NIC and 3-NIC Azure vSockets:

- 3-NIC instances support a MGMT interface, which is not available for 2-NIC instances
- 2-NIC instances are cheaper than the 3-NIC instance

For information about the supported 3-NIC Azure instances, see [this document](/v1/docs/changing-azure-vsockets-to-a-different-vm-size). For information about Azure pricing, see the relevant Microsoft documentation.

## Instructions

In an HA configuration, you should run the migration procedure on your secondary vSocket before your primary vSocket.

1. If you are currently on the Standard_D2S_v4 Azure instance, before upgrading to Socket v21, you have to [resize](/v1/docs/changing-azure-vsockets-to-a-different-vm-size) your instance to the 3-NIC supported instance. If you are already on the 3-NIC supported instance, you can skip to the next step.

> [!NOTE]
> Note:
> 
> For Azure HA vSockets with Standard_D2S_v4 instances and Availability Set, there is downtime for the site during this process for up to 17 minutes.
2. [Manually upgrade](/v1/docs/manually-upgrading-a-socket) to Socket v21. **Note:** Make sure to wait for a Cato notification that the upgrade was completed successfully, the upgrade process can take up to 17 minutes. The successful upgrade is notified with an event, email, and message in the CMA notification area.
3. After upgrading, run the [migration script](/v1/docs/migrating-azure-vsockets-to-a-2-nic-solution#running-the-migration-script) using AzureCLI. The script will disassociate the management interface from the Azure instance. As part of the process, the vSocket will shut down and come up after one minute.
4. [Downsize](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/resize-vm?tabs=portal) your instance to Standard_D2s_v5.
5. [Confirm](/v1/docs/migrating-azure-vsockets-to-a-2-nic-solution#confirm-connectivity-to-cato) that you are connected to the Cato Cloud.

If you are in an HA configuration, repeat this process for the primary vSocket.

### (Optional) Switch back to a 3-NIC solution

1. If you are currently running on Standard_D2S_v4 or Standard_D2S_v5 first [resize](/v1/docs/changing-azure-vsockets-to-a-different-vm-size) to a supported 3-NIC instance.
2. Proceed to run the [migration script](/v1/docs/migrating-azure-vsockets-to-a-2-nic-solution#running-the-migration-script) and in step 5 select No, the script will then ask if you would you like to add a Management Network interface, select Yes and select the relevant NIC from the list to finish the process.

## Running the Migration Script

After the vSocket is upgraded to v21, run the migration script to remove the management interface from the vSocket:

1. Download the [migration script](https://catonetworks.files.com/preview/f/041f10609b03b0bc/Azure%20vSocket/add_remove_mgmt_iface_v5_Socket_21.sh)
2. Connect to Azure CLI from within the Azure user interface only and, under Manage files, upload the script

> [!NOTE]
> Note:
> 
> Running the script outside of the Azure user interface might cause the script to fail.

![Screenshot 2024-09-22 at 13.48.57.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21745531019165.png)
3. Change the run permissions on the script using the following command:

```plaintext
 chmod 755 <filename>
```
4. Run the script using the following command:

```plaintext
 sh <filename>
```
  1. Enter the subscription ID.
  2. Select VM Resource Group.
  3. Select Location
  4. Select the relevant VM instance
  5. Select Yes to remove the MGMT network interface and select the NIC to remove.
  6. Select the relevant WAN NIC. At this point, the MGMT interface is disconnected and the script completes.

### Confirm HA Failover

If you are in an HA configuration, it is important that you also confirm that the HA failover works during this procedure.

Go to the WebUI's Network Tools section and run the [API Test Tool](/v1/docs/configuring-ha-for-azure-vsockets#testing-high-availability-from-the-socket-webui).

- If the test fails, follow the troubleshooting steps mentioned in [Troubleshooting Azure HA vSocket](/v1/docs/azure-ha-vsocket-troubleshooting).
- If the API Test is successful, follow the steps described in the next sections.

> [!NOTE]
> Note:
> 
> During the resize operation, the Socket WebUI API Test Tool on the Secondary vSocket might return the following message:

`Azure API Test state 'Retrieve NIC configuration for current socket' failed! Azure API BLOCK state 'Unblock ALL AZ API'`

If the test succeeds on the Primary vSocket, this message is a mistake and you can safely ignore this specific result and continue with the resizing procedure below.

### Confirm Connectivity to Cato

- From the **Monitoring** > **Topology** page, select the Azure vSocket site and in the **Site > Socket Configuration** section, click **Action > Socket WebUI** for the Primary and Secondary vSockets.

The browser opens a new tab and logs in to the Socket WebUI.

When the vSocket is functioning correctly, the Socket WebUI displays the Monitor tab and the active links have green **Link Status** icons. The example below shows the WAN links (1 and 4) have green icons.

![vSocket_webUI.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21283750517533.png)
