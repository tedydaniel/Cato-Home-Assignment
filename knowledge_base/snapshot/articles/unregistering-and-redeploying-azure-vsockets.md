---
title: "Unregistering and Redeploying Azure vSockets"
slug: "unregistering-and-redeploying-azure-vsockets"
updated: 2026-06-22T09:21:23Z
published: 2026-06-22T09:21:23Z
canonical: "knowledge.catonetworks.com/unregistering-and-redeploying-azure-vsockets"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Unregistering and Redeploying Azure vSockets

This articles describes how to unregister and redeploy Azure vSockets.

## Overview

Sometimes it is necessary to migrate a vSocket to a different VM resource, or reinstall a vSocket on a different VM instance type. You can use the Cato Management Application to unregister an existing vSocket from a site, and then recreate the vSocket and redeploy it on a new VM instance. The configurations and settings for the site are preserved when it is redeployed. You can redeploy vSockets for sites with a single vSocket and for high availability (HA) sites with two vSockets.

### Redeploying vSockets from the Azure Marketplace

For vSockets that were originally deployed using the Azure Marketplace, there are some virtual resources that you can't re-use as part of redeploying the vSocket. Instead, you need to delete the following virtual resources before you redeploy the vSocket:

- VM instance
- Network interfaces (NICs) attached to the VM and their public IP addresses

## Single vSocket Sites

This section discusses how to unregister and redeploy a vSocket for sites with a single Azure vSocket.

### Unregistering a Single vSocket

Use the Cato Management Application to unregister the vSocket instance from the site. Once the old vSocket is unregistered, a new serial number (S/N) is automatically generated in the Cato Management Application. You will use the new serial number (S/N) when you redeploy the vSocket.

> [!NOTE]
> Note:
> 
> Make sure the Azure vSocket instance is turned off before you unregister the vSocket.

![unregister-vsocket.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247830403741.png)

**To unregister a single vSocket:**

1. From the navigation pane, select **Network > Sites**, and select the site.
2. From the navigation pane, click **Site Configuration > Socket**, and select the Socket you are unregistering.
3. Under **Actions** , click **Unregister**. The vSocket is now unregistered and a new S/N is generated which you will use when deploying the new vSocket instance.

#### Deploying a Single vSocket

Use the Azure portal to delete the previous instance and then deploy a new one. Make sure to enter the new vSocket S/N displayed in the Cato Management Application in **Network > Sites > [site name] > Site Configuration > Socket**.

After you complete the deployment, the vSocket automatically connects to the site in the Cato Cloud.

**To redeploy a single vSocket:**

1. In the Azure portal, delete the VM instance (**Home > Virtual Machines**) and the NICs (**Home > Network interfaces**).

Alternatively force-delete all deployment resources in Azure (see [Troubleshooting Deployment Failures](/v1/docs/deploying-azure-vsockets-from-the-marketplace)).
2. Deploy the vSocket instance via the Azure marketplace application. For more information, see [Deploying Azure vSockets from the Marketplace](/v1/docs/deploying-azure-vsockets-from-the-marketplace).

**Note:** In some cases it is necessary to deploy the vSocket manually, for example, in China where Azure Marketplace is not supported. For more information, see [Deploying an Azure vSocket Site Manually (EA 2 NIC Support)](/v1/docs/deploying-an-azure-vsocket-site-manually).
3. Start the Azure vSocket from the Azure Portal:
  1. In the navigation menu go to **Virtual Machines** and select the vSocket instance.
  2. On the vSocket instance **Overview** page click **Start**. The instance status will change to **Running**.
4. Confirm the site is running in the Cato Management Application in the **Network > Sites** page.

## High Availability vSocket Sites

This section discusses how to unregister and redeploy a vSocket for sites with a two vSockets in an HA configuration.

You can choose to first unregister the primary or the secondary vSocket.

- If the primary vSocket is unregistered, a failover takes places to the secondary vSocket
- If the secondary vSocket is unregistered, the primary vSocket remains active
- If both vSockets are unregistered at the same time, the site disconnects from the Cato Cloud

### Unregistering High Availability vSockets

Use the Cato Management Application to unregister a vSocket instances from the site, then use the new S/N when you redeploy the new Azure vSocket instance.

> [!NOTE]
> Note:
> 
> Once the secondary vSocket is unregistered, you can optionally remove High Availability settings from the site and delete the secondary vSocket settings. This converts the site from HA configuration to a single vSocket site.

**To unregister a vSocket for an HA site:**

1. From the navigation pane, select **Network > Sites**, and select the site.
2. From the navigation pane, click **Site Configuration > Socket**, and select the Socket you are unregistering.
3. Under **Actions** , click **Unregister**. The vSocket is now unregistered and a new S/N is generated which you will use when deploying the new vSocket instance.

#### Redeploying High Availability vSocket

Use the Azure portal to delete the previous instance for the secondary vSocket, and then deploy a new one. The vSocket automatically connects to the site in the Cato Cloud after you complete the deployment.

When you re-deploy the vSocket, make sure to enter the new S/N from the previous section. You can find the S/N for the site in the Cato Management Application in **Network > Sites > [site name] > Site Configuration > Socket**.

> [!NOTE]
> Notes:
> 
> - Make sure to delete the old Managed Identity from the Azure Resource Group before running the HA script
> - If the primary vSocket instance is re-deployed, you must run the dedicated script to bind both vSocket instances for HA

**To redeploy a vSocket for an HA site:**

1. In the Azure portal, delete the VM instance (**Home > Virtual Machines**) and the NICs (**Home > Network interfaces**).

Alternatively force-delete all deployment resources in Azure (see [Troubleshooting Deployment Failures](/v1/docs/deploying-azure-vsockets-from-the-marketplace)).
2. Deploy the primary and secondary vSocket instances via the Azure marketplace application. For more information, see [Deploying Azure vSockets from the Marketplace](/v1/docs/deploying-azure-vsockets-from-the-marketplace).

**Note:** In some cases it is necessary to deploy the vSocket manually, for example, in China where Azure Marketplace is not supported. For more information, see [Deploying an Azure vSocket Site Manually (EA 2 NIC Support)](/v1/docs/deploying-an-azure-vsocket-site-manually).
  1. For manually deployed vSockets, use the `create_ha_settings.sh` script to bind the primary and secondary vSockets for High Availability setting. Read more on using the script on [Configuring High Availability for Azure vSockets](/v1/docs/configuring-ha-for-azure-vsockets).
3. Start the Azure vSocket from the Azure Portal:
  1. In the navigation menu go to **Virtual Machines** and select the vSocket instance.
  2. On the vSocket instance **Overview** page click **Start**. The instance status will change to **Running**.
4. Confirm the site is running in the Cato Management Application in the **Network > Sites** page.

## Verifying vSocket Connectivity

Once you complete re-deploying the vSocket, you can verify the connectivity status of the vSocket:

- In **Network > Sites** all available sites appear. If at least one vSocket is running the site appears as ‘Connected’ under ‘Connectivity Status’.
- In **Network > Sites > [site name] > Site Configuration > Socket** you can inspect High Availability configuration and HA readiness. For more about HA Status, see [What is Socket High Availability](/v1/docs/what-is-socket-ha).
- In **Network > Sites > [site name] > Site Configuration > Socket** connect to the WebUI of a vSocket. The WebUI should be reachable once the vSocket is running.
