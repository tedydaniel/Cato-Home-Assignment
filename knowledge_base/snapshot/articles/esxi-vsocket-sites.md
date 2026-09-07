---
title: "Unregistering and Redeploying ESXi vSockets"
slug: "unregistering-and-redeploying-esxi-vsockets"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/unregistering-and-redeploying-esxi-vsockets"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Unregistering and Redeploying ESXi vSockets

This articles describes how to unregister and redeploy VMware ESXi vSockets.

## Overview

Sometimes it is necessary to migrate a vSocket to a different VM resource, or reinstall a vSocket on a different VM instance type. You can use the Cato Management Application to unregister an existing vSocket from a site, and then recreate the vSocket and redeploy it on a new VM instance. The configurations and settings for the site are preserved when it is redeployed.

## Unregistering an ESXi vSocket

Use the Cato Management Application to unregister the vSocket instance from the site. Once the old vSocket is unregistered, a new serial number (S/N) is automatically generated in the Cato Management Application. You will use the new serial number (S/N) when you redeploy the vSocket.

> [!NOTE]
> Note:
> 
> Make sure the ESXi vSocket instance is turned off before you unregister the vSocket.

![unregister-vsocket.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247814141213.png)

**To unregister a vSocket:**

1. From the navigation pane, select **Network > Sites**, and select the site.
2. From the navigation pane, click **Site Configuration > Socket**, and select the Socket you are unregistering.
3. Under **Actions** , click **Unassign**. The vSocket is now unassigned and a new S/N is generated which you will use when deploying the new vSocket instance.

### Redeploying an ESXi vSocket

Use the ESXi vSphere portal to delete the previous instance and then deploy a new one. Make sure to enter the new vSocket S/N displayed in the Cato Management Application in **Network > Sites > [site name] > Site Configuration > Socket**.

After you complete the deployment, the vSocket automatically connects to the site in the Cato Cloud.

**To redeploy a vSocket:**

1. Delete the VM instance in vSphere by selecting the vSocket VM under **Virtual Machines > [vSocket VM] > Actions > Delete**.
2. Deploy the vSocket instance by using the OVA image. For more read [Configuring an ESXi vSocket Site](/v1/docs/configuring-an-esxi-vsocket-site).
3. Start the ESXi vSocket from the vSphere Portal:
  1. In the navigation menu, go to **Virtual Machines**, select the vSocket instance.
  2. On the vSocket instance page click **Power on**.
4. Confirm the site is running in the Cato Management Application in the **Network > Sites** page.

## Verifying vSocket Connectivity

Once you complete re-deploying the vSocket, you can verify the connectivity status of the vSocket:

- In **Network > Sites** all available sites appear. If at least one vSocket is running the site appears as ‘Connected’ under ‘Connectivity Status’.
- In **Network > Sites > [site name] > Site Configuration > Socket** connect to the WebUI of a vSocket. The WebUI should be reachable once the vSocket is running.
