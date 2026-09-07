---
title: "Azure HA vSocket Troubleshooting"
slug: "azure-ha-vsocket-troubleshooting"
status: "update"
updated: 2026-09-03T08:58:30Z
published: 2026-09-03T08:58:30Z
canonical: "knowledge.catonetworks.com/azure-ha-vsocket-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure HA vSocket Troubleshooting

## Overview

This article provides insights into common Azure vSocket HA deployment issues and offers troubleshooting steps to resolve them. This guide aims to assist in identifying and addressing potential hurdles during and after deploying the HA solution either via HA script or Marketplace.

## Symptoms

When deploying Azure vSocket HA, you might encounter the following symptoms:

- **HA Script Failure**
  - Failure in executing the create_ha_settings script in manual deployment.
  - Issues with secondary vSocket deployment via Marketplace.
- **HA Failover Failure**
  - Failed HA API tests from the Socket WebUI.
  - Failed HA failover resulting in traffic not being forwarded to the secondary vSocket.
- **HA Status Not Ready**
  - CMA shows that the HA status of the Site is Not Ready

## Possible Causes

The most frequent causes of HA deployment failures include:

- Use of non-public DNS in Azure.
- Management interface lacking internet access.
- Insufficient Azure account permissions.
- Restrictive Security Group and Routing settings in Azure.
- Failure to assign the floating IP address to the LAN interface.
- LAN connectivity issues.

## Troubleshooting the Issue

> [!NOTE]
> IMPORTANT:
> 
> Before starting to troubleshoot, ensure to verify all prerequisites for Azure HA vSocket deployment. See [Configuring HA for Azure vSockets](/v1/docs/configuring-ha-for-azure-vsockets) and [Deploying Azure vSockets from the Marketplace](/v1/docs/deploying-azure-vsockets-from-the-marketplace)

### Troubleshooting HA Script Failure

The Azure HA script (create_ha_settings) and secondary vSocket deployment via Marketplace validate that the Azure subscription has two valid vSockets and then assign the **Identity Roles** that create the HA and failover mechanism. If the script run fails, follow these troubleshooting steps:

#### Checking Activity logs

- In Azure, **Activity Logs** store all the events that happened inside each Azure resource. Review these logs if the deployment isn't successful and one of the roles is not assigned. Browse to the **VM** or the **NIC** and select the activity log ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17227011216413(1).png)

#### Checking Azure Naming Restrictions

- When entering the vSocket Name in the script, make sure that the name doesn't include spaces or restricted characters as explained in [Naming rules and restrictions](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules).
- If a naming issue occurs during deployment, the following error will be shown in the Error log

```plaintext
The value of parameter disk.name is invalid. (Code: InvalidParameter, Target: disk.name)
```

#### Checking Azure DNS Configuration

- Make sure that the default Azure DNS is configured for both the VNET and the associated NICs. If the default DNS isn't configured in Azure in both the VNET and NIC, Role creation will fail.
- To check what the Azure DNS configuration is, see [Fixing DNS configuration issues](/v1/docs/azure-ha-vsocket-troubleshooting#h_01HQ15Z6JN49GPAHHNTMBGAJXA)

#### Checking Azure Permissions

- To successfully run the HA script, make sure that the Azure user has owner permissions. Go to **Resource Group** > **Access Control IAM > View My Access**, and verify that the user account is set to **Owner** or higher role. See [Azure built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles). ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17227040198813(1).png)

#### Verifying Azure Role Assignment

- Run the steps provided in [Verifying Azure Role Assignment](/v1/docs/azure-ha-vsocket-troubleshooting#01J7BXC8KYJKXSG7YXCV4AS93V) to confirm that the identity role listed in the resource group is assigned to the LAN NICs, LAN subnet, and both vSocket VMs.

#### Re-running the HA script

- As a last resort, the HA script (create_ha_settings) can be re-run once the previous steps have been checked.
- Make sure to [renew the Azure token](/v1/docs/azure-ha-vsocket-troubleshooting#h_01HQ162RV8ERWVSZ6S2VK3GQXW) and remove the Azure Managed Identity if it was created during the first script run.

### Troubleshooting HA Failover Failure

If the HA script runs successfully but the vSocket HA failover doesn't occur as expected (e.g. traffic isn't routed to the secondary vSocket), follow these steps:

#### Running HA API Test

- From the vSocket webUI, run the API Test tool from both vSockets which validates that the API Call to Azure can be made successfully. Any errors with permissions or Floating IP assignments can be seen here. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17227011268253(1).png)

#### Checking the Activity log

- In Azure, **Activity Logs** store all the events that happened inside each Azure resource. Review these logs to identify if the floating IP failed to be pushed to the **LAN NIC** or if the API Test isn't successful. Browse to the **NIC** and select the activity log ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17227011279005(1).png)

#### (Optional) Pinging the Floating IP

- From a host within the LAN network, utilize the Ping tool, and ping the Floating IP address. If this test isn't successful, continue with [Verifying the Floating IP assignment](/v1/docs/azure-ha-vsocket-troubleshooting#h_01HQ16A0B631616G6Z8RB7TNXR) ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/image(211).png)

#### Verifying the Floating IP assignment

- To route traffic to the master vSocket, Azure assigns the Floating IP to the LAN NIC of the current master vSocket. Go to the primary vSocket VM **LAN NIC > IP Configuration** and verify that the Floating IP exists as "Secondary". If not, continue with the next steps. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17227040280477(1).png)

#### Verifying Azure Role Assignment

The HA Managed Identity must be correctly associated with all Azure resources participating in failover.

- During Azure vSocket deployment, the HA **Identity Role** is created and stored in Azure **Managed Identities.**
- Only **one user-assigned** role should be assigned to each resource. If a policy adds **system-assigned** identities in Azure, the vSockets must be excluded from it.
- This role is assigned to the various virtual resources attached to the vSocket. The components in the Azure infrastructure that use the Role are:
  - LAN Network Interface (NIC) for each vSocket
  - The LAN subnet associated with the LAN NICs
  - Both vSocket VMs
- The role assignment for the **NICs** can be checked under **Access control > Role Assignments** and should be assigned for both Primary and Secondary **LAN NICs**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17227040208669(1).png)
- The role assignment for the **LAN subnet** can be checked under **VNET > Subnet**, then select the LAN subnet and click **Manage users > Role Assignments**. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/21650248417181(1).png)
- For each **vSocket VM**, the identity role can be checked under **Security > Identity** > **User assigned,** as shown in the screenshot below. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17227011257757(1).png)
- No **system-assigned** role should be assigned to the VM. To verify this, navigate to **Security > Identity > System assigned** and ensure the **Status** option is set to **Off** for each vSocket VM.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/36264165100957.png)
- If the HA identity role is not installed on any of the above resources, the deployment process may have failed to do so. You can run the [Cato HA script](/v1/docs/configuring-ha-for-azure-vsockets) once again if the role is missing from any of the involved resources. Alternatively, the secondary Azure vSocket can be [redeployed](/v1/docs/deploying-azure-vsockets-from-the-marketplace) ,which will install the missing HA identity roles.

#### Checking that the Management interface has DNS and internet access

- Verify that the management interface has internet access and can connect to the configured DNS server.
- Check DNS resolution for *management.azure.com* from the Azure portal. The HA API Call uses this FQDN.
  - Go to the **Virtual machine > vSocket > Run command > RunShellScript**
  - Enter **dig management.azure.com** in the text box
  - Click Run
- The dig output will be displayed in the portal with a DNS response. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17227040290333(1).png)
- If there's no DNS resolution, see [Fixing DNS configuration issues](/v1/docs/azure-ha-vsocket-troubleshooting#h_01HQ15Z6JN49GPAHHNTMBGAJXA).
- From the same page, try to reach any internet resource to confirm internet access. For example, `ping -c 4 8.8.8.8` If the ping is not successful, continue with the next steps. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/18381368031389(1).png)

#### Check if the Network Security Group is blocking outbound traffic.

> [!NOTE]
> Note:
> 
> If the [2-NIC solution](/v1/docs/migrating-azure-vsockets-to-a-2-nic-solution) is implemented on the vSockets. Perform this troubleshooting step on the WAN interface.

- A quick way to check is to go to the MGMT network interface in Azure and click "Effective security rules" at the bottom left side of the screen.
- The screenshot below shows no NSG assigned, so outbound traffic is not blocked.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17227011319837(1).png)

#### Check the MGMT Interface Routing for Internet Traffic.

> [!NOTE]
> Note:
> 
> If the [2-NIC solution](/v1/docs/migrating-azure-vsockets-to-a-2-nic-solution) is implemented on the vSockets. Perform this troubleshooting step on the WAN interface.

- In case MGMT interface traffic is routed through a third-party firewall in Azure, check that UDP/53 and TCP/443 outbound connections are allowed.
- The route table can be reviewed on the management interface page in Azure by clicking the "Effective routes" option.
- The screenshot below shows the route for internet traffic using the Internet as the "Next Hop Type", so a firewall is not blocking the traffic. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17227011333149(1).png)

#### Checking the Routing Table's Next Hop

- Confirm that the LAN Routing table is pointing at the Floating IP. Change the **Next-hop IP address** accordingly if needed. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17227011341853(1).png)

### Troubleshooting HA Status Not Ready

If CMA shows that the HA Status is Not Ready and both vSockets are up and running, both vSockets will take the Master role (split-brain scenario). There could be two associated problems:

- Both vSockets are running different firmware versions
- HA Keepalive messages do not reach the secondary vSocket

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17227011352989(1).png)

It is recommended to check both vSockets [WebUI](/v1/docs/accessing-the-socket-webui) pages to confirm the HA status of each one of them. A split-brain scenario will manifest if both primary and secondary vSockets are in a Master role. The webUI will show the current role on the top of the main Monitoring page.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17227040342301(1).png)

#### Checking Firmware versions

To satisfy the compatible version criteria, both vSockets must be running the same **MAJOR** version, e.g. v17.xx.yy or v18.xx.yy. vSockets perform an initial upgrade after first being deployed. If one of the vSockets fails to upgrade, this issue must be troubleshot. Submit a [Support ticket](/v1/docs/submitting-a-support-ticket) to report this issue.

#### Checking HA Keepalives

Keepalive packets use port UDP/20480 for Azure vSocket and will be sent only from the Master vSocket to the Standby vSocket. The split-brain condition occurs when both vSockets have the Master role, which can happen due to LAN connectivity issues between the vSockets that create a situation in which the HA Keepalive messages do not reach the secondary vSocket.

Run the following checks to confirm LAN connectivity:

- Check if the Network Security Group is blocking port UDP/20480. A quick way to check NSG rules is to go to each LAN network interface in Azure and click "Effective security rules" at the bottom left side of the screen.
- Confirm that both LAN interfaces are associated with the same LAN subnet.
- Run a [packet capture](/v1/docs/how-to-capture-traffic-on-a-socket) from the WebUI of both vSockets and identify if the keepalives sent by the primary are being received by the secondary vSocket.

## Resolving Discovered Issues

#### Renewing Azure token

- If Azure Cloud Shell is used to deploy the HA script, open a new session and re-authenticate. This will renew the token used for querying the API. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17227011391005(1).png)

#### Fixing DNS configuration issues

- To fix the Azure DNS configuration and set it to the default value, go to **Virtual network** > **DNS servers** and to **Network Interface > DNS Servers**, and ensure that you're using the **Default** option or a **public DNS server**. Shut down the VM to make any DNS-related changes and then turn it back up. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/17227011434525(1).png)

#### Unregistering and Redeploying an Azure vSocket

- If after following all the above troubleshooting steps, the HA script or HA failover continues to fail, it is possible to unregister and redeploy one or both vSockets. See [Redeploy High Availability vSocket Sites](/v1/docs/unregistering-and-redeploying-azure-vsockets)
- It is important to follow the guidelines and remove the Virtual Machine, network interfaces, associated public IPs, and Managed Identity before redeploying a vSocket.
- If only the primary vSocket instance is re-deployed, you must run the dedicated HA script (create_ha_settings) to bind both vSocket instances for HA.

## Raising cases to Cato Support

Submit a [Support ticket](/v1/docs/submitting-a-support-ticket) with the results of the above troubleshooting steps. Please include the following information in the ticket:

- A clear description of the issue, including any error messages.
- DNS test results for **management.azure.com**
- API Test results.
- Screenshots of the assigned floating IP, configured identity role, effective routes, and effective security rules.
- Azure activity log screenshots, including any errors found.
