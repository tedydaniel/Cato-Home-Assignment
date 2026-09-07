---
title: "Configuring Local Port Forwarding for a Site"
slug: "configuring-local-port-forwarding-for-a-site"
updated: 2026-06-22T09:21:18Z
published: 2026-06-22T09:21:18Z
canonical: "knowledge.catonetworks.com/configuring-local-port-forwarding-for-a-site"
---

> ## Documentation Index
> Fetch the complete documentation index at: https://knowledge.catonetworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Local Port Forwarding for a Site

## Using Local Port Forwarding

> [!NOTE]
> Note:
> 
> Local Port Forwarding isn't supported for IPsec sites.

The local port forwarding feature lets remote Internet hosts connect to a host or server on the LAN of the Socket site. This feature is intended for cases where it's necessary to bypass the Cato Cloud and allow the source host direct access to the Socket and then the internal host. You can also configure the Allowed Remote IPs as an access control list (ACL) that defines which external IP addresses can access the internal host.

You can't define the protocol for a local port forwarding rule. The Socket listens on the specified port for both TCP and UDP traffic.

In general, we recommend that you use remote port forwarding (see [Configuring Remote Port Forwarding for the Account](/v1/docs/configuring-remote-port-forwarding-for-the-account)) to route traffic to internal resources whenever it's possible.

**To define a local port forwarding rule:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Local Port Forwarding**.
3. Click **New**. The **Create Rule** panel opens.

You can configure the local port settings for this host by entering:
  - A **Name** for the rule.
  - The **External Port** or ports (range) that the Socket listens to. ​​**Note:**​​ You can't use the same ports for multiple rules, each rule must use a unique port.
  - The **Internal IP** address and **Internal Port** or ports (range) that the Socket NATs the external traffic to.
4. **(Optional)** You can configure the **Allowed Remote IPs** that are allowed to connect to this host.
  - Under **Allowed Remote IPs**, you can enter a specific IP address, an IP range (10.2.1.1-10.1.2.5) or a CIDR block (10.1.3.0/29).
  - You can also paste a comma separated list with multiple IP addresses and ranges, for example: 10.1.1.1, 10.2.1.1-10.2.1.105
5. Click **Apply**.

**To delete a local port forwarding rule:**

1. From the navigation menu, click **Network > Sites** and select the site.
2. From the navigation menu, click **Site Configuration > Local Port Forwarding**.
3. Click the More icon ( ![More_icon.png](https://cdn.document360.io/81d0367c-2b69-4ba8-b412-1c8f46ce677e/Images/Documentation/24247787975709.png) ) on the rule line to delete and select **Delete Rule**.
4. In the confirmation window, click **Delete**. The rule is removed.
