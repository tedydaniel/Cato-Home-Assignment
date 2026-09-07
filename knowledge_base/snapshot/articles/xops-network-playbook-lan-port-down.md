---
title: "XOps Network Playbook - LAN Port Down"
slug: "xops-network-playbook-lan-port-down"
updated: 2026-06-22T09:26:20Z
published: 2026-06-22T09:26:20Z
canonical: "knowledge.catonetworks.com/xops-network-playbook-lan-port-down"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# XOps Network Playbook - LAN Port Down

This playbook describes steps to resolve issues when the LAN Port is down.

## Overview

The Socket LAN port typically serves as the internal network connection for a site. In the case of Socket HA, keepalive signals are transmitted through this port to monitor the health and status of the HA connection. It's vital to be informed if the LAN port goes down, as this could disrupt communication, degrade network performance, and affect critical services.

When responding to Network XOps stories it is important to approach the problem by first verifying the problem is ongoing, then troubleshooting the problem and finally verifying the problem is resolved.

## Step 1 - Verifying the LAN Port Is Down

The following are the different ways that a Cato Management Application admin can verify that a LAN Port is showing down.

### Using the Story Drill-down

- An XOps story will be generated when the LAN port is down.
- Go to the **Stories Workbench** page and use the Network Operations preset, include the filter: Indication In **LAN port down,** and adjust the time frame if necessary. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22179635258013.png)
- Verify if a story is generated as shown below. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22179627492253.png)
- Click on the story to drill down into the details. It provides information on the site's current status, an incident timeline, and, more importantly, the connectivity status of the Socket interfaces. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22194157005469.png)
- As you scroll further down in the story drill-down, you'll find the Incident Timeline. This timeline highlights any changes in the status of the LAN interface. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22179627497501.png)

**NOTE:** The LAN Port Down does not generate any CMA Events. To be notified by email when the LAN port is down, you can configure a rule in the [Detection and Response Policy](https://support.catonetworks.com/hc/en-us/articles/19617058762269-Managed-XDR-Response-Policy).

### Socket WebUI

- Another way to verify that the LAN port is down is to access the Socket WebUI.
- To do that, refer to [https://support.catonetworks.com/hc/en-us/articles/4413265669905-Using-the-Socket-WebUI](https://support.catonetworks.com/hc/en-us/articles/4413265669905-Using-the-Socket-WebUI).
- As shown in the below screenshot, we can see that the LAN 01 is Down. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22168157561501.png)

## Step 2 - Troubleshooting LAN Port Down

This section covers the tools available in Cato for a structured troubleshooting approach to this type of incident. While the steps are generally meant to be followed in order, the results of each check may influence the next step in the process.

### Reviewing Changes in Audit Trail

- Review changes in the [Audit Trail page](/v1/docs/using-the-audit-trail) and see if there is a configuration change leading to this issue.
- For example, the screenshot below shows that the admin made configuration changes to LAN 02. If the timing of this activity aligns with the LAN interface going down, the admin can revert the changes to determine if the changes are the cause. ![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22180021749021.png)

### Layer 1 and 2 Checks

- Please verify the physical connectivity or cabling between the Socket and the network device connected to the affected LAN port.
- Additionally, review any recent or ongoing changes to the LAN-side configuration. For example, configuration changes on the switch connected to the Socket LAN interface, such as changes to VLANs or subnets, could be affecting the connection.
- Replacing the cable connected to the Socket LAN port or connecting it to a different port on the switch can help determine if the issue is hardware-related.

## Step 3 - Verifying the LAN Port Is Up

After identifying and resolving the issue causing the LAN to go down, verify that the port is now visible in both the Story drill-down and the Socket WebUI.

### Using the Story Drill-down

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22194149496605.png)

**NOTE:** Once the issue is resolved, the status of the story will change from "Open" to "Monitoring." It will remain in this state for the next two hours, provided there are no further incidents. For more information, refer to [Understanding the Stories Columns](https://support.catonetworks.com/hc/en-us/articles/19442391484061-Reviewing-XDR-Stories-in-the-Partner-Stories-Workbench#h_01J0TWBQYTPPZVCC9CYR2733GK).

### Incident Timeline

The incident timeline displays changes in the status of the LAN interface. You can use it to confirm whether the most recent status has been updated to "UP."

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22194149498909.png)

### Socket WebUI

Access the Socket WebUI to verify the status of the LAN port is up. To do that, refer to [https://support.catonetworks.com/hc/en-us/articles/4413265669905-Using-the-Socket-WebUI](/v1/docs/accessing-the-socket-webui).

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/22190724554909.png)

  

## Raising Cases to Cato Support

If following this playbook has not resolved an issue, submit a [Support ticket](/v1/docs/submitting-a-support-ticket). To get the most helpful response to a request, an administrator should provide the results of the troubleshooting steps taken.
