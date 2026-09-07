---
title: "Creating Floating Ranges for an Account"
slug: "creating-floating-ranges-for-an-account"
updated: 2026-06-22T09:25:58Z
published: 2026-06-22T09:25:58Z
canonical: "knowledge.catonetworks.com/creating-floating-ranges-for-an-account"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Floating Ranges for an Account

Floating ranges are global IP ranges that are not connected to a specific site, but can be learned from any site with a BGP neighbor. For more information, see [Using BGP in the Cato Cloud](/v1/docs/using-bgp-in-the-cato-cloud).

## Floating Ranges

Floating ranges are global IP ranges that are not connected to a specific site, but can be learned from any site with a BGP neighbor. For example, in a Disaster Recovery (DR) scenario, many applications (such as VMware NSX) can move servers from one location to the other while maintaining their IP addresses. In these cases, BGP helps to update the remaining network objects and advertises where these servers now reside.

Floating ranges are defined as global objects. Floating Ranges are not associated with a particular Site and must be defined in Security or Networking rules (Site association can change dynamically). You can leverage the global object definition to explicitly create network and/or security rules as per your organization policy requirements.

In order for a BGP dynamic range to inherit the security or network policy for a site, it must exactly match the floating range. For example, if the BGP dynamic range is 192.168.1.0/24 and the floating range is defined as 192.168.1.1/32, then there is no connection between them and the BGP dynamic range doesn't inherit the policies from the floating range.

> [!NOTE]
> Note:
> 
> Floating Ranges cannot overlap with static ranges.

![newfloatingrange.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24447588103581.png)

**To define a Floating Range:**

1. From the navigation menu, click **Resources > Floating Ranges**.
2. Click **New**. The **New Floating Range** panel opens.
3. Enter a **Name** for the Floating Range global object in the Cato Management Application.
4. Define the **Subnet** range.
5. Click **Apply**.

**To delete a Floating Range object:**

1. From the navigation menu, click **Resources > Floating Ranges**.
2. Click ![Delete.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24447629223965.svg-xml) (delete) next to the floating range. The floating range is removed.
3. Click **Save**. The floating range is deleted.
