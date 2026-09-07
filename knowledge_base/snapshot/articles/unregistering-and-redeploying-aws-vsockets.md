---
title: "Unregistering and Redeploying AWS vSockets"
slug: "unregistering-and-redeploying-aws-vsockets"
updated: 2026-06-22T09:21:25Z
published: 2026-06-22T09:21:25Z
canonical: "knowledge.catonetworks.com/unregistering-and-redeploying-aws-vsockets"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Unregistering and Redeploying AWS vSockets

This articles describes how to unregister and redeploy AWS vSockets.

## Overview

Sometimes it is necessary to migrate a vSocket to a different VM resource, or reinstall a vSocket on a different VM instance type. You can use the Cato Management Application to unregister an existing vSocket from a site, and then recreate the vSocket and redeploy it on a new VM instance. The configurations and settings for the site are preserved when it is redeployed. You can redeploy vSockets for sites with a single vSocket and for high availability (HA) sites with two vSockets.

## Single vSocket Sites

This section discusses how to unregister and redeploy a vSocket for sites with a single AWS vSocket.

### Unregistering a Single vSocket

Use the Cato Management Application to unregister the vSocket instance from the site. Once the old vSocket is unregistered, a new serial number (S/N) is automatically generated in the Cato Management Application. You will use the new serial number (S/N) when you redeploy the vSocket.

> [!NOTE]
> Note:
> 
> Make sure the EC2 vSocket instance in AWS is turned off before you unregister the vSocket.

![unregister-vsocket.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247810114845.png)

**To unregister a single vSocket:**

1. From the navigation pane, select **Network > Sites**, and select the site.
2. From the navigation pane, click **Site Configuration > Socket**, and select the Socket you are unregistering.
3. Under **Actions** , click **Unregister**. The vSocket is now unregistered and a new S/N is generated which you will use when deploying the new vSocket instance.

#### Deploying a Single vSocket

Use the AWS console to delete the previous instance and then deploy a new one. Make sure to enter the new vSocket S/N displayed in the Cato Management Application in **Network > Sites > [site name] > Site Configuration > Socket**.

After you complete the deployment, the vSocket automatically connects to the site in the Cato Cloud.

**To redeploy a single vSocket:**

1. Select and delete the vSocket instance in AWS under **Instances > Delete**.
2. Deploy the vSocket instance either manually or using the AWS marketplace. For more about deploying an AWS instance see [Deploying an AWS vSocket Site Manually](/v1/docs/deploying-an-aws-vsocket-site-manually) and [Deploying a vSocket Site from the AWS Marketplace](/v1/docs/deploying-a-vsocket-site-from-the-aws-marketplace), respectively.
3. Start the AWS vSocket from the EC2 dashboard:
  1. In the navigation menu select **Instances > Instances**.
  2. Right-click the vSocket instance and choose **Start instance**.
4. Confirm the site is running in the Cato Management Application in the **Network > Sites** page.

## High Availability vSocket Sites

This section discusses how to unregister and redeploy a vSocket for sites with a two vSockets in an HA configuration.

You can choose to unregister the primary or the secondary vSocket first.

- If the primary vSocket is unregistered, a failover takes places to the secondary vSocket.
- If the secondary vSocket is unregistered, the primary vSocket remains active.
- If both vSockets are unregistered simultaneously, the site becomes disconnected.

### Unregistering High Availability vSockets

Use the Cato Management Application to unregister a vSocket instances from the site, then use the new S/N when you redeploy the new AWS vSocket EC2 instance.

> [!NOTE]
> Note:
> 
> Once the secondary vSocket is unregistered, you can optionally remove High Availability settings from the site and delete the secondary vSocket settings. This converts the site from HA configuration to a single vSocket site.

**To unregister a vSocket for an HA site:**

1. From the navigation pane, select **Network > Sites**, and select the site.
2. From the navigation pane, click **Site Configuration > Socket**, and select the Socket you are unregistering.
3. Under **Actions** , click **Unregister**. The vSocket is now unregistered and a new S/N is generated which you will use when deploying the new vSocket instance.

#### Redeploying High Availability vSocket

Use the AWS console to delete the previous instance for the secondary vSocket, and then deploy a new one. The vSocket automatically connects to the site in the Cato Cloud after you complete the deployment.

When you re-deploy the vSocket, make sure to enter the new S/N from the previous section. You can find the S/N for the site in the Cato Management Application in **Network > Sites > [site name] > Site Configuration > Socket**. In addition, remember to assign the correct IAM role to the vSocket by selecting the vSocket instance > Security > Attach IAM Role and assign AWS-HA-role.

**To redeploy a vSocket for an HA site:**

1. Select and delete the vSocket instance in AWS under **Instances > Delete**.
2. Deploy a vSocket instance by using the AWS AMI provided by Cato Support. For more about deploying an AWS instance see [Configuring HA for AWS vSockets](/v1/docs/configuring-ha-for-aws-vsockets).
3. Start the AWS vSocket from the EC2 dashboard:
  1. Start the AWS vSocket from the EC2 dashboard:
  2. Right-click the vSocket instance and choose **Start instance**.
4. Confirm the site is running in the Cato Management Application in the **Network > Sites** page.

## Verifying vSocket Connectivity

Once you complete re-deploying the vSocket, you can verify the connectivity status of the vSocket:

- In **Network > Sites** all available sites appear. If at least one vSocket is running the site appears as ‘Connected’ under ‘Connectivity Status’.
- In **Network > Sites > [site name] > Site Configuration > Socket** you can inspect High Availability configuration and HA readiness. For more about HA Status, see [What is Socket High Availability](/v1/docs/what-is-socket-ha).
- In **Network > Sites > [site name] > Site Configuration > Socket** connect to the WebUI of a vSocket. The WebUI should be reachable once the vSocket is running.
