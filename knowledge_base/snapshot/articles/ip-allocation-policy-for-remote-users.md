---
title: "IP Allocation Policy for Remote Users"
slug: "ip-allocation-policy-for-remote-users"
updated: 2026-08-17T08:28:52Z
published: 2026-08-17T08:28:52Z
canonical: "knowledge.catonetworks.com/ip-allocation-policy-for-remote-users"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# IP Allocation Policy for Remote Users

This article explains how to use the IP Allocation Policy to define **Default**, **Dynamic**, and **Static** IP ranges that are allocated to users in your account.

## Overview

The IP Allocation Policy lets admins control which internal IP addresses are allocated to the Cato Client when connecting a device to the network. Users are allocated IP addresses in one of these ways:

- **Default IP Allocation:** The default range, allocated to a user that:

By default, this range is 10.41.0.0/16. You can update this to a range you choose.
  - Does not meet a Dynamic IP Allocation rule
  - Is not allocated a static IP address
  - Matches a rule where the IP range is exhausted
- **Dynamic IP Allocation:** IP ranges are allocated to users or groups based on an ordered rulebase.
- **Static IP Allocation:** A fixed IP address allocated to a specific user

For the Client to allocate an IP address, users must manually disconnect and reconnect when switching between:

- Default and dynamic allocation
- Different dynamic rules (e.g., when moving to one with higher priority)

**Note:** The IP Allocation Policy is not applied to users behind a site.

### Policy Revisions and Concurrent Editing by Multiple Admins

The IP Allocation Policy lets different admins edit the policy in parallel. Each admin can edit rules and save the changes to the rulebase in their own private revision, and then publish them to the account policy (the published revision). For more information on how to manage policy revisions, see [Working with Policy Revisions](/v1/docs/working-with-policy-revisions).

### Use Case - Static IP Addresses

XYZ Corporation operates equipment that enforces access using Access Control Lists (ACLs), allowing connections only from predefined source IP addresses. For example, a router may only permit access from the IP address 192.168.0.25.

As the system administrator, you configure a static IP assignment in the Cato Management Application (CMA) and apply it in the IP Allocation Policy. When the user connects using the Cato Client, the platform assigns the same static IP address each time, ensuring compliance with the ACL restrictions defined on the router.

### Use Case - Dynamic IP Addresses

ABC Company operates as a call center for multiple companies. Each operative must connect to a client’s environment from a specific source IP range, based on that client’s access control requirements. For example, Company X accepts IP addresses from 192.168.0.0/24, and Company Y accepts IP addresses from 10.0.0.0/16.

As the system administrator, you define the dynamic IP ranges 192.168.0.0/24 and 10.0.0.0/16 in the Cato Management Application (CMA) and apply them in the IP Allocation Policy. When operatives connect using the Cato Client, the platform assigns an IP address from the appropriate range according to the policy rules you configure, ensuring compliance with each client’s IP-based restrictions.

## Allocating IPs to Remote Users

Follow these steps to allocate IP addresses to remote users:

1. Add [Global IP ranges](/v1/docs/using-ip-ranges-in-policies) to your account
2. Define the IP Ranges for each IP allocation method
3. Define users or user groups to be allocated IP addresses dynamically or statically

### Step 1: Add IP Ranges to your Account

Remote users can only be assigned IP ranges that are within the **Global IP Range** entity for your account. For more information about how to add an IP range to the **Global IP Range** entity, see [Using IP Ranges in Policies](/v1/docs/using-ip-ranges-in-policies).

### Step 2: Define the IP Ranges for Each IP Allocation Method

Define the IP ranges allocated to remote users with each allocation method. Each range must be a unique network range and can’t overlap with any other network range defined in your account.

**Best Practice:** Configure the largest Client IP range possible to decrease the chances of an IP conflict that causes the Client to disconnect.

![IP_allocation_policy.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/33142393443357.png)

**To define the IP Ranges for each IP allocation method:**

1. From the navigation menu, click **Access > IP Allocation Policy**.
2. Click the **Settings** tab.
3. Enter the IP ranges for each IP allocation method.
4. Click **Save**.

### Step 3: Define Users or User Groups to be Allocated IP Addresses Dynamically or Statically

You can allocate IPs to specific users or user groups either dynamically or statically. If a user is in a rule for a dynamically allocated IP and is allocated a static IP, the static IP takes priority. After you allocate IPs, the Client automatically disconnects and reconnects with the new IP if a user switches between an IP from:

- A dynamically allocated IP to a static IP, or vice versa
- The default range to a static IP, or vice versa

If you are only updating the Default IP range for your account. This step is not required

#### Allocating IPs to Users or User Groups Dynamically

You can dynamically allocate IPs using an ordered rulebase that sequentially checks if a user or user group matches a rule. For example, create a rule when accessing customer A that draws an IP address from one IP range, and another rule for customer B that draws an IP address from another IP range. Once a rule is matched, IPs are allocated from the **Allocated Range** configured in the rule. Rules that are listed in the policy after the matching rule are not applied. If no rule is matched, an IP is allocated from the default range. The lease time for the dynamically allocated IP addresses is 2 minutes after the Client is disconnected. After this time, the IP address is available for other users.

Different admins can edit the policy in parallel and save the changes in their own private revision before the rule is published. For more information, see [Working with Policies](/v1/docs/working-with-policy-revisions).

**Note:** If you have an **Any Any** rule, make sure it is placed correctly, otherwise, it will take precedence over rules below it. Then all IP addresses for lower priority rules will be allocated dynamically and not from the default or static IP addresses.

**Source PoP Condition for Rules**

The **Source PoP** condition lets you allocate an IP range based on the PoP that the Client connects to. The Client makes a best-effort attempt to connect to the closest PoP based on the user’s physical location. However, the Client may connect to a PoP in another country. For example, a user located in France might connect to a PoP outside France.

![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/dynamic_source_pop.png)

**To allocate IPs to users or user groups dynamically:**

1. From the navigation menu, click **Access > IP Allocation Policy**.
2. Click **New**.

The **New Rule** panel opens.
3. Enter a name for the rule and define the position.
4. Define the **User/Groups**, **Platforms**, **Public ISP IP Range**, **Source PoP**, **Countries**, and the **IP Range**.
5. Click **Save**. The panel closes, and the settings are updated in the policy. The changes are saved to your unpublished revision and are available for editing until they are published or discarded.
6. Repeat steps 2-6 for each rule.
7. Click **Publish**. A confirmation window opens, click **Publish**.
8. Enable **Dynamic IP Allocation**.

The slider ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27468566714013.png) is green when the rule is enabled, and gray when the rule is disabled.

#### Allocating Static IPs to Users

For users, you can define a static IP that is allocated to them when they use the Client to connect to the network. Each static IP can only be allocated to one device at a time. If a user connects to the network with multiple devices, the first device is allocated the static IP address. Other devices are allocated IPs from the **Dynamic IP Range** or the **Default IP Range**.![](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/static_ip.png)

**To allocate static IPs to users:**

1. From the navigation menu, click **Access > IP Allocation Policy**.
2. Click the **Static IP Allocation** tab.
3. Click **New**.
4. Select the **User** and enter the static **IP** address.
5. Repeat the previous step for additional users.
6. Set the **Enable Static IPs** toggle to **Enabled**.

The toggle is green ![toggle.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/27468566714013.png) when enabled.
7. Click **Save**. The panel closes, and the settings are updated in the policy. The changes are saved to your unpublished revision and are available for editing until they are published or discarded.
8. Click **Publish**. A confirmation window opens, click **Publish**.
