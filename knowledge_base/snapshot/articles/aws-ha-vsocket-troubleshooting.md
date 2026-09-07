---
title: "AWS HA vSocket Troubleshooting"
slug: "aws-ha-vsocket-troubleshooting"
updated: 2026-06-22T09:21:22Z
published: 2026-06-22T09:21:22Z
canonical: "knowledge.catonetworks.com/aws-ha-vsocket-troubleshooting"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AWS HA vSocket Troubleshooting

## Overview

This guide provides a detailed troubleshooting framework for addressing common issues encountered during the deployment of AWS vSocket High Availability (HA). Whether deploying manually or via the AWS Marketplace, these steps aim to help identify and resolve potential problems effectively.

## Symptoms

Common issues in AWS vSocket HA deployments may include:

- **HA Failover Failure**
  - Failed HA API tests from the vSocket WebUI.
  - Failed HA failover, resulting in traffic not being forwarded to the secondary vSocket.
- **HA Status Not Ready**
  - CMA displays the site's HA status as "Not Ready"

## Possible Causes

HA deployment failures are often due to the following:

- Use of non-public DNS in AWS.
- Management interface lacking internet access.
- IAM role misconfiguration.
- Restrictive Security Group and Routing settings in AWS.
- Failure to assign the appropriate network interface to the LAN routing table.
- LAN connectivity issues.

## Troubleshooting the Issue

> [!NOTE]
> IMPORTANT:
> 
> Before starting to troubleshoot, ensure that all prerequisites for AWS HA vSocket deployment are verified. See [Deploying an AWS vSocket Site Manually](/v1/docs/deploying-an-aws-vsocket-site-manually), [Deploying a vSocket Site from the AWS Marketplace](/v1/docs/deploying-a-vsocket-site-from-the-aws-marketplace) and [Configuring HA for AWS vSockets](/v1/docs/configuring-ha-for-aws-vsockets)

### Troubleshooting HA Failover Failure

If traffic isn't routing to the secondary vSocket during failover, consider the following troubleshooting steps:

#### Running the HA API Test

- From the vSocket WebUI, run the API Test tool for both vSockets.
- This tool validates that the API Call to AWS can be made successfully.
- Any errors related to permissions or routing table updates can be seen here. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23539990574621.png)

#### Checking AWS DNS Configuration

- Verify that the default **AWS DNS server** is configured for the associated VPC.
- To check AWS DNS configuration, see [Fixing DNS configuration issues](/v1/docs/aws-ha-vsocket-troubleshooting#fixing-dns-configuration-issues)
- If a custom DNS server (e.g., a private DNS server) is configured, ensure that it can resolve public domains. Verify that it can resolve the FQDN **ec2.<region>.amazonaws.com** (e.g., *ec2.us-east-1.amazonaws.com)*, which is used by the API.
- The Security Group associated with the MGMT interface should allow DNS requests to 8.8.8.8 and 8.8.4.4, even if the default AWS DNS server is configured.

#### Verifying the LAN Routing Table

- To route traffic to the master vSocket, AWS assigns the current master vSocket's LAN network interface to the LAN routing table.
- Go to **VPC > Route Tables** and select the LAN routing table. Under the **Routes** tab, verify that the master vSocket's LAN network interface is the default route's gateway (target). If not, continue with the next steps. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23543388344861.png)
- Note that manually modifying the LAN routing table can be a quick workaround if the target NIC wasn't changed during failover.

#### Verifying IAM Role

- During [AWS vSocket deployment](/v1/docs/configuring-ha-for-aws-vsockets), the HA **IAM Role** is created and associated with both primary and secondary vSockets.
- Under each instance's details page, confirm that the correct IAM Role is assigned. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23490131069341.png)
- Click on the IAM role link, and under the permissions tab, verify that the IAM policy contains the correct statement, as shown below. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23490133532701.png)

**Note:** In case of missing IAM role, once the role is added, the sockets must be rebooted in order for the added roles to take affect.

#### Verifying IMDS Settings

- Ensure both vSockets use matching IMDS settings (optional or required). For more information, review [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html?icmpid=docs_ec2_console).
- Starting vSocket build 20.0.18221, IMDSv2 is supported.
- To modify IMDS settings, select the instance, and under actions, click on **Instance settings > Modify instance metadata options**.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23539832291741.png)

#### Verifying the Network Security Group.

- Ensure the network security group isn't blocking outbound traffic to the management interface.
- Under **EC2 > Network Interfaces**, find the Security Group associated with the Management Interface. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23543388345629.png)
- Verify that the Security Group's outbound rules allow ports 80, 443, and 53. In this case, all outbound traffic is allowed. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23543372946461.png)

#### Verifying the MGMT Interface Routing for Internet Traffic.

- If MGMT interface traffic is routed through a third-party firewall in AWS, check that UDP/53, TCP/80, and TCP/443 outbound connections are allowed.
- From the network interface page, click on the MGMT interface's Subnet ID. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23543372946717.png)
- On the Subnet page, select the **Route Table** tab. The screenshot below shows the default route pointing at the Internet Gateway, so a firewall is not blocking the traffic. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23543388350109.png)
- Open the related **Route Table** and verify that all MGMT subnets are listed as associated subnets. In the case of dual Availability Zone, two MGMT subnets will exist, one for each vSocket, as explained in [Creating a Subnet for the Secondary vSocket LAN Interfaces](/v1/docs/configuring-ha-for-aws-vsockets#h_01JA4VNYFPEPQGXA3KRNMWMTKT). ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24082498314397.png)
- On the VPC's Resource Map tab, all associated subnets and their routing configurations are visually represented for easy reference. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24102418615453.png)
- Confirm that an elastic IP is associated with the MGMT interface. This can be seen from the instance's networking tab. The MGMT interface can be identified by its **device index** of 0. The WAN and LAN interfaces should be associated with device indexes 1 and 2, respectively. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23544401804445.png)

#### Checking CloudTrail logs

- Enable AWS CloudTrail to log API calls to AWS for debugging failed modifications of the LAN routing table during HA failover.
- You may follow the process to create a trail, define the S3 bucket to store logs, and select management events that include API activity. See [Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html?icmpid=docs_cloudtrail_console). ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23488035472541.png)

### Troubleshooting HA Status Not Ready

If CMA shows that the HA Status is Not Ready and both vSockets are up and running, both vSockets will take the Master role (split-brain scenario). This may occur due to:

- Both vSockets are running different firmware versions
- HA Keepalive messages do not reach the secondary vSocket

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23543474264349.png)

It is recommended to check both vSockets [WebUI](/v1/docs/accessing-the-socket-webui) pages to confirm the HA status of each one of them. A split-brain scenario will manifest if both primary and secondary vSockets are in a Master role. The WebUI will show the current role at the top of the main Monitoring page.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23543474264989.png)

#### Checking Firmware versions

To satisfy the compatible version criteria, both vSockets must run the same **MAJOR** version, e.g. v17.xx.yy or v18.xx.yy. vSockets perform an initial upgrade after first being deployed. If one of the vSockets fails to upgrade, this issue must be troubleshot. Submit a [Support ticket](/v1/docs/submitting-a-support-ticket) to report this issue.

#### Checking HA Keepalives

Keepalive packets use port UDP/20480 for AWS vSocket and will be sent only from the Master vSocket to the Standby vSocket. The split-brain condition occurs when both vSockets have the Master role, which can happen due to LAN connectivity issues between the vSockets that create a situation in which the HA Keepalive messages do not reach the secondary vSocket.

Run the following checks to confirm LAN connectivity:

- Check if the Network Security Group is blocking port UDP/20480. A quick way to check NSG rules is to go to each LAN network interface in AWS and check inbound and outbound rules as explained in [Check if the Network Security Group is blocking outbound traffic.](/v1/docs/aws-ha-vsocket-troubleshooting#verifying-the-network-security-group)
- Confirm that both LAN interfaces are associated with different LAN subnets.
- Run a [packet capture](/v1/docs/how-to-capture-traffic-on-a-socket) from the WebUI of both vSockets and identify if the secondary vSocket is receiving the keepalives sent by the primary.

## Resolving Discovered Issues

#### Fixing DNS configuration issues

- To fix DNS configuration issues, check that the default AWS DNS server is configured for the VPC.
- Under the VPC details, find the **DHCP option set** configured for it. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23489820776093.png)
- Open the DHCP option set and verify that the defined **Domain name server** is AmazonProvidedDNS.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/23489820777629.png)
- It isn't possible to change the existing Domain name servers. For that, create a new DHCP option set, which will use the AmazonProvidedDNS by default.

#### Unregistering and Redeploying an AWS vSocket

- If after following all the above troubleshooting steps, the HA failover continues to fail, it is possible to unregister and redeploy one or both vSockets. See [Redeploy High Availability vSocket Sites](/v1/docs/unregistering-and-redeploying-aws-vsockets)
- It is important to remove the Virtual Machine but retain network interfaces, associated public IPs, and IAM role before redeploying a vSocket.
- In addition, remember to reattach the correct IAM role to the vSocket by selecting the vSocket instance > Security > Attach IAM Role and assigning the AWS-HA role.

## Raising cases to Cato Support

Submit a [Support ticket](/v1/docs/submitting-a-support-ticket) with the results of the above troubleshooting steps. Please include the following information in the ticket:

- A clear description of the issue, including any error messages.
- DNS configuration in the VPC.
- API Test results.
- Screenshots of the LAN routing table and configured IAM roles.
- If possible, CloudTrail log files at the time of the failed failover.
