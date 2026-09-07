---
title: "Changing Azure vSockets to a Different VM Size"
slug: "changing-azure-vsockets-to-a-different-vm-size"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/changing-azure-vsockets-to-a-different-vm-size"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Changing Azure vSockets to a Different VM Size

This article explains the process to change the Azure virtual machine to a different VM size for an Azure virtual Socket (vSocket).

## Overview

There are different situations where it may be necessary to change the Azure vSocket VM to a different size. The resizing process is managed in your Azure tenant, and resizing the VM doesn't impact the vSocket or site settings. There's no need to make changes in the Cato Management Application or the Socket WebUI.

Depending on the Azure vSocket version and configuration, there will be some down-time for the site.

### Limitation

The default VM for new deployments is Standard_D8ls_v5. If your environment does not currently support this VM, contact your Azure admin.

## Step 1 - Verifying the Quota for vCPU Cores

Before resizing your vSocket VM, it's important to confirm that the allocated quota in the respective region permits an increase in the number of vCPU Cores. Azure sets a quota on the maximum number of VM vCPUs allowable per region. When adjusting the size of a VM and the new VM size has more vCPUs, you need to verify that you won't exceed the vCPU quota for that region. For example, an Azure HA site has 2 **Standard_D2s_v4** vSocket VMs and each one uses 2 vCPUs, and you are resizing them to the **Standard_D8ls_v5** VM which uses 8 vCPUs. The resizing requires an additional 12 vCPUs (6 for each vSocket), and you need to verify that adding 12 vCPUs to the region doesn't exceed the Azure vCPU quota.

If necessary, submit a request to Microsoft to increase the vCPU quota for the relevant regions. When the vCPU quota is exceeded, the VM doesn't deploy to the new size.

For more information, see the relevant Microsoft documentation: [View quotas](https://learn.microsoft.com/en-us/azure/quotas/view-quotas) and [Check vCPU quotas](https://learn.microsoft.com/en-us/azure/virtual-machines/quotas?tabs=cli).

## Step 2 - Changing the vSocket VM to a Different Size

This section discusses resizing the vSocket VM for an HA (high availability) site and for a site with a single vSocket.

### Changing vSocket VMs for an HA Site (v19 and higher)

For HA sites running vSocket version v19 or higher, confirm whether the VMs were deployed in an **Availability Set** from the Virtual Machine's Overview Page. Follow the sections below accordingly:

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17457172607261.png)

It's important that you also confirm that the HA failover will work during this procedure. Go to the WebUI's Network Tools section and run the [API Test Tool](/v1/docs/configuring-ha-for-azure-vsockets#testing-high-availability-from-the-socket-webui).

- If the test fails, follow the troubleshooting steps mentioned in [Troubleshooting Azure HA vSocket](/v1/docs/azure-ha-vsocket-troubleshooting#troubleshooting-ha-failover-failure)
- If the API Test is successful, proceed to follow the steps described in next sections.

> [!NOTE]
> Note:
> 
> During the resize operation, if the Socket WebUI API Test Tool on the Secondary vSocket returns the following message:

`Azure API Test state 'Retrieve NIC configuration for current socket' failed! Azure API BLOCK state 'Unblock ALL AZ API'`

If the test succeeds on the Primary vSocket, then this message is a mistake and you can safely ignore this specific result and continue with the resizing procedure below.

#### HA vSockets WITHOUT Availability Set

If the vSockets are NOT deployed in an **Availability Set**, follow the steps below to resize each VM individually: [Change the size of a virtual machine](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/resize-vm?tabs=portal). There should be no downtime during the process.

1. Resize the Primary vSocket. The vSocket reboots as part of the resizing process and the site automatically fails over to the Secondary vSocket.
2. After the resizing process is complete and the Primary vSocket is running, the site automatically falls back to the Primary vSocket.
3. Resize the Secondary vSocket. The vSocket reboots as part of the resizing process.
4. Finally, test HA failover by power cycling the Primary VM to confirm that HA is working for the vSockets.

#### HA vSockets WITH Availability Set

> [!NOTE]
> Note:
> 
> Please contact Microsoft for assistance resizing a Standard_D2s_v4 VM with 3 NICs in an Availability Set. We have seen that the steps below successfully resize HA vSockets with Availability Sets.

If the vSockets are deployed in an **Availability Set**, follow the steps below to resize each VM individually: [Change the size of a virtual machine](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/resize-vm?tabs=portal). There will be some downtime during the process.

1. Attempt to resize the Secondary vSocket. The resize operation will fail with an error reporting that the Primary vSocket exceeded the NIC limit.
2. Resize the Primary vSocket which will succeed. This will cause both vSockets to reboot and the tunnels to reconnect.
3. Both vSockets will come online, but it's possible that the LAN traffic will fail to route due to resizing. The API call to assign the floating IP on the Primary vSocket may initially fail.
4. If you have routing issues, shut down the Secondary vSocket which should restore connectivity through the Primary vSocket.
5. Start the Secondary vSocket. Traffic may stop communication for about 2 minutes while the vSocket boots up.

#### Changing vSocket VMs for an HA Site (lower than v19)

For HA sites running vSocket versions lower than v19, we recommend that you deploy new VMs for the Primary (active) and Secondary (stand-by) vSocket. See [Unregistering and Redeploying Azure vSockets](/v1/docs/unregistering-and-redeploying-azure-vsockets). The vSocket deploys to the new VM size with v19.x.

If it is necessary to keep the same version, please contact Support to manually recreate the site.

### Resizing a Single vSocket VM for a Site (v19 or higher)

For sites with a single Azure vSocket v19.x or higher, the VM reboots as part of the resizing process and there is some down-time for the site.

Refer to the Microsoft documentation for details on how to resize the VM: [Change the size of a virtual machine](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/resize-vm?tabs=portal).

#### Changing vSocket VMs for an Single vSocket Site (lower than v19)

For single vSocket sites running vSocket versions lower than v19, we recommend that you use the the Azure Marketplace to deploy new VMs. The vSocket deploys to the new VM size with v19.x. See [Deploying Azure vSockets from the Marketplace](/v1/docs/deploying-azure-vsockets-from-the-marketplace).

If it is necessary to keep the same version, please contact Support to manually recreate the site.

## Step 3 - Verifying the Resized vSocket

To verify that the vSocket is functioning correctly after resizing the VM, use the Cato Management Application to log in to the Socket WebUI for the vSocket.

**To log in to the Socket WebUI and verify the resized vSocket:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Socket**.
3. From the **Actions** menu of the socket, select **Socket WebUI**.

The browser opens a new tab and logs in to the Socket WebUI.

When the vSocket is functioning correctly, the Socket WebUI displays the Monitor tab and the active links have green **Link Status** icons.

![webUI_status.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17452013213469.png)

For HA configurations, repeat the step above for the Secondary vSocket.
